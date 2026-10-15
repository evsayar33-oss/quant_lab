"""Bar-by-bar Python ports of two TradingView strategies, with TradingView fill rules.

- BTC "Quantum Flow Sentinel" (1H liquidity sweep + Kaufman ER + 4H EMA200 filter)
- XAU "Apex Multi-Factor Sentinel" (1H EMA50/200 + RSI cross + session + circuit breakers)

TradingView broker emulation that is copied here:
- Orders are sent at bar close; market entries fill at the next bar open +/- slippage ticks.
- strategy.exit orders are (re)sent at bar close and act from the next bar.
  So the fill bar of an entry has no stop.
- Intrabar path: open -> nearest extreme -> other extreme -> close.
- Stops fill at the stop price (or the open on a gap) with slippage; limits fill at the limit, no slippage.
- Commission is a percent of the notional on each fill.
- request.security(..., "240", lookahead_off): a 1H bar sees the last CLOSED 4H EMA200 only.

Ad-hoc study. It does not write decisions/registry.json.
"""
from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass, field, replace
from pathlib import Path

import numpy as np
import pandas as pd

OUT = Path(__file__).resolve().parents[2] / "results" / "pine_ports"


# ----------------------------------------------------------------------------- indicators (Pine semantics)
def rma(x: pd.Series, n: int) -> pd.Series:
    return x.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()


def atr(df: pd.DataFrame, n: int) -> pd.Series:
    pc = df["Close"].shift(1)
    tr = pd.concat([df["High"] - df["Low"], (df["High"] - pc).abs(), (df["Low"] - pc).abs()], axis=1).max(axis=1)
    tr.iloc[0] = df["High"].iloc[0] - df["Low"].iloc[0]
    return rma(tr, n)


def ema(x: pd.Series, n: int) -> pd.Series:
    return x.ewm(span=n, adjust=False, min_periods=n).mean()


def rsi(x: pd.Series, n: int) -> pd.Series:
    d = x.diff()
    up, dn = rma(d.clip(lower=0), n), rma((-d).clip(lower=0), n)
    return 100 - 100 / (1 + up / dn)


def htf_ema_no_lookahead(df: pd.DataFrame, n: int = 200, rule: str = "4h") -> pd.Series:
    """4H EMA as a 1H bar sees it with lookahead_off: value of the last 4H bar that has closed."""
    c4 = df["Close"].resample(rule, label="left", closed="left").last().dropna()
    e4 = ema(c4, n)
    end = e4.index + pd.Timedelta(rule)              # 4H bar end time
    bar_end = df.index + pd.Timedelta("1h")          # 1H bar end time
    s = pd.Series(e4.values, index=end)
    return s.reindex(bar_end, method="ffill").set_axis(df.index)


# ----------------------------------------------------------------------------- params
@dataclass
class BtcP:
    capital: float = 1500.0
    risk_pct: float = 1.5
    max_exp_pct: float = 50.0
    atr_len: int = 14
    atr_stop: float = 2.0
    be_r: float = 1.0
    be_off_r: float = 0.15
    tp1_r: float = 1.5
    trail_r: float = 2.0
    trail_atr: float = 2.0
    sweep_lb: int = 20
    er_len: int = 10
    er_min: float = 0.35
    volz_min: float = 0.2
    use_macro: bool = True
    comm: float = 0.0005
    slip_ticks: float = 5
    tick: float = 0.1
    funding_8h: float = 0.0          # optional perp funding cost per 8h on notional (stress test)


@dataclass
class XauP:
    capital: float = 1000.0
    risk_pct: float = 1.5
    max_exp_pct: float = 50.0
    max_daily: float = 2.5
    max_weekly: float = 5.0
    atr_len: int = 14
    atr_stop: float = 1.5
    tp1_r: float = 1.2
    be_off_r: float = 0.10
    tp2_r: float = 2.5
    lock_r: float = 1.2
    trail_atr: float = 1.5
    tp2_pct: float = 50.0            # Pine sends 50 in strategy.exit (the alert says 33)
    use_macro: bool = True
    sess_from: int = 7
    sess_to: int = 18
    contract_oz: float = 0.1
    qty_mult: float = 1.0            # 1.0 = TradingView fills qty in oz; 0.1 = OKX contracts of 0.1 oz
    comm: float = 0.0005
    slip_ticks: float = 15
    tick: float = 0.01
    funding_8h: float = 0.0


# ----------------------------------------------------------------------------- signals
def btc_signals(df: pd.DataFrame, p: BtcP) -> pd.DataFrame:
    c = df["Close"]
    a = atr(df, p.atr_len)
    er = (c - c.shift(p.er_len)).abs() / c.diff().abs().rolling(p.er_len).sum()
    er = er.fillna(0.0)
    vm, vs = df["Volume"].rolling(20).mean(), df["Volume"].rolling(20).std(ddof=0)
    vz = ((df["Volume"] - vm) / vs).where(vs != 0, 0.0)
    hp = df["High"].shift(1).rolling(p.sweep_lb).max()
    lp = df["Low"].shift(1).rolling(p.sweep_lb).min()
    volok = vz > p.volz_min
    bull = (df["Low"] < lp) & (c > lp) & volok
    bear = (df["High"] > hp) & (c < hp) & volok
    e50 = ema(c, 50)
    macro = htf_ema_no_lookahead(df, 200)
    mb = (c > macro) if p.use_macro else True
    ms = (c < macro) if p.use_macro else True
    clean = er > p.er_min
    long_ = bull & (e50 > e50.shift(2)) & mb & clean
    short = bear & (e50 < e50.shift(2)) & ms & clean
    return pd.DataFrame({"atr": a, "long": long_.fillna(False), "short": short.fillna(False)})


def xau_signals(df: pd.DataFrame, p: XauP) -> pd.DataFrame:
    c = df["Close"]
    a = atr(df, p.atr_len)
    ef, es = ema(c, 50), ema(c, 200)
    r = rsi(c, 14)
    lx = (r > 45) & (r.shift(1) <= 45)
    sx = (r < 55) & (r.shift(1) >= 55)
    h, wd = df.index.hour, df.index.dayofweek          # UTC, Mon=0
    sess = pd.Series((h >= p.sess_from) & (h < p.sess_to) & (wd <= 4), index=df.index)
    vol = a >= a.rolling(20).mean()
    macro = htf_ema_no_lookahead(df, 200)
    mb = (c > macro) if p.use_macro else True
    ms = (c < macro) if p.use_macro else True
    long_ = (ef > es) & (ef > ef.shift(2)) & mb & lx & sess & vol
    short = (ef < es) & (ef < ef.shift(2)) & ms & sx & sess & vol
    return pd.DataFrame({"atr": a, "long": long_.fillna(False), "short": short.fillna(False)})


# ----------------------------------------------------------------------------- simulator
@dataclass
class Pos:
    side: int
    qty0: float
    qty: float
    entry: float
    t_in: pd.Timestamp
    i_in: int
    initR: float = math.nan
    stop: float = math.nan
    tp1: float = math.nan
    tp2: float = math.nan
    ext: float = math.nan
    stage: int = 0
    tp1_done: bool = False
    tp2_done: bool = False
    pnl: float = 0.0
    fees: float = 0.0
    fills: list = field(default_factory=list)


def _path(o, h, l, c):
    return [o, h, l, c] if abs(h - o) <= abs(l - o) else [o, l, h, c]


def simulate(df: pd.DataFrame, kind: str, p) -> tuple[pd.Series, pd.DataFrame]:
    sig = btc_signals(df, p) if kind == "btc" else xau_signals(df, p)
    O, H, L, C = (df[k].to_numpy(float) for k in ("Open", "High", "Low", "Close"))
    A, LG, SH = sig["atr"].to_numpy(float), sig["long"].to_numpy(bool), sig["short"].to_numpy(bool)
    idx = df.index
    slip = p.slip_ticks * p.tick
    cash = p.capital
    pos: Pos | None = None
    pending = None                      # (side, qty) to fill at next open
    eq = np.empty(len(df))
    trades = []
    day_key = week_key = None
    sod = sow = p.capital
    fund_rate_bar = getattr(p, "funding_8h", 0.0) / 8.0

    def close_part(q, px, why, t):
        nonlocal cash
        g = pos.side * (px - pos.entry) * q
        f = abs(px * q) * p.comm
        cash += g - f
        pos.pnl += g - f
        pos.fees += f
        pos.qty -= q
        pos.fills.append((str(t), why, px, q))

    for i in range(len(df)):
        t = idx[i]
        # ---- 1. fill pending market entry at the open
        if pending is not None and pos is None:
            side, q = pending
            px = O[i] + side * slip
            f = px * q * p.comm
            cash -= f
            pos = Pos(side, q, q, px, t, i, fees=f, pnl=-f)
        pending = None
        # ---- 2. intrabar exits from orders sent at the previous close
        if pos is not None and i > pos.i_in and not math.isnan(pos.stop):
            for a, b in zip(_path(O[i], H[i], L[i], C[i])[:-1], _path(O[i], H[i], L[i], C[i])[1:]):
                if pos is None or pos.qty <= 1e-12:
                    break
                fav = (b > a) if pos.side > 0 else (b < a)
                if fav:
                    for lvl_name in ("tp1", "tp2"):
                        lvl = getattr(pos, lvl_name)
                        done = getattr(pos, lvl_name + "_done")
                        if math.isnan(lvl) or done or pos.qty <= 1e-12:
                            continue
                        lo, hi = min(a, b), max(a, b)
                        start_beyond = (a >= lvl) if pos.side > 0 else (a <= lvl)
                        if start_beyond or lo <= lvl <= hi:
                            px = a if start_beyond else lvl
                            pct = 50.0 if kind == "btc" else (33.0 if lvl_name == "tp1" else p.tp2_pct)
                            q = min(pos.qty, round(pos.qty0 * pct / 100.0, 10))
                            close_part(q, px, lvl_name, t)
                            setattr(pos, lvl_name + "_done", True)
                else:
                    s = pos.stop
                    gap = (a <= s) if pos.side > 0 else (a >= s)
                    hit = gap or (min(a, b) <= s <= max(a, b))
                    if hit:
                        px = (a if gap else s) - pos.side * slip
                        close_part(pos.qty, px, "stop", t)
            if pos is not None and pos.qty <= 1e-12:
                trades.append(pos)
                pos = None
        # ---- funding (optional stress)
        if pos is not None and fund_rate_bar:
            f = abs(C[i] * pos.qty) * fund_rate_bar
            cash -= f
            pos.pnl -= f
            pos.fees += f
        # ---- 3. script at bar close
        equity = cash + (pos.side * (C[i] - pos.entry) * pos.qty if pos else 0.0)
        eq[i] = equity
        if pos is not None:
            if math.isnan(pos.initR):                      # first close after the fill
                pos.initR = A[i] * p.atr_stop
                pos.ext = H[i] if pos.side > 0 else L[i]
                pos.stop = pos.entry - pos.side * pos.initR
                pos.tp1 = pos.entry + pos.side * p.tp1_r * pos.initR
                if kind == "xau":
                    pos.tp2 = pos.entry + pos.side * p.tp2_r * pos.initR
                if pos.tp1_done:                           # never on fill bar, kept for safety
                    pass
            R = pos.initR
            if pos.side > 0:
                pos.ext = max(pos.ext, H[i])
                if kind == "btc":
                    if pos.stage == 0 and H[i] >= pos.entry + p.be_r * R:
                        pos.stage = 1
                        pos.stop = max(pos.stop, pos.entry + p.be_off_r * R)
                    if H[i] >= pos.entry + p.trail_r * R:
                        pos.stage = 2
                    if pos.stage == 2:
                        pos.stop = max(pos.stop, pos.ext - p.trail_atr * A[i])
                else:
                    if pos.stage == 0 and H[i] >= pos.tp1:
                        pos.stage = 1
                        pos.stop = max(pos.stop, pos.entry + p.be_off_r * R)
                    if pos.stage in (0, 1) and H[i] >= pos.tp2:
                        pos.stage = 2
                        pos.stop = max(pos.stop, pos.entry + p.lock_r * R)
                    if pos.stage >= 2:
                        pos.stop = max(pos.stop, pos.ext - p.trail_atr * A[i])
            else:
                pos.ext = min(pos.ext, L[i])
                if kind == "btc":
                    if pos.stage == 0 and L[i] <= pos.entry - p.be_r * R:
                        pos.stage = 1
                        pos.stop = min(pos.stop, pos.entry - p.be_off_r * R)
                    if L[i] <= pos.entry - p.trail_r * R:
                        pos.stage = 2
                    if pos.stage == 2:
                        pos.stop = min(pos.stop, pos.ext + p.trail_atr * A[i])
                else:
                    if pos.stage == 0 and L[i] <= pos.tp1:
                        pos.stage = 1
                        pos.stop = min(pos.stop, pos.entry - p.be_off_r * R)
                    if pos.stage in (0, 1) and L[i] <= pos.tp2:
                        pos.stage = 2
                        pos.stop = min(pos.stop, pos.entry - p.lock_r * R)
                    if pos.stage >= 2:
                        pos.stop = min(pos.stop, pos.ext + p.trail_atr * A[i])
        allowed = True
        if kind == "xau":
            dk, wk = (t.day), (t.isocalendar().week)
            if dk != day_key:
                sod, day_key = equity, dk
            if wk != week_key:
                sow, week_key = equity, wk
            allowed = (sod - equity) / sod * 100 < p.max_daily and (sow - equity) / sow * 100 < p.max_weekly
        if pos is None and allowed and not math.isnan(A[i]) and (LG[i] or SH[i]):
            side = 1 if LG[i] else -1
            risk_budget = equity * p.risk_pct / 100
            exp_budget = equity * p.max_exp_pct / 100
            if kind == "btc":
                q = min(risk_budget / (A[i] * p.atr_stop), exp_budget / C[i])
                q = max(0.01, math.floor(q * 100) / 100)
            else:
                q = min(risk_budget / (A[i] * p.atr_stop * p.contract_oz), exp_budget / (C[i] * p.contract_oz))
                q = max(1, math.floor(q)) * p.qty_mult
            if equity > 0:
                pending = (side, q)
    if pos is not None:                                   # mark open trade at the last close
        close_part(pos.qty, C[-1], "eod", idx[-1])
        trades.append(pos)
        eq[-1] = cash
    tr = pd.DataFrame([{
        "t_in": x.t_in, "t_out": pd.Timestamp(x.fills[-1][0]), "side": "long" if x.side > 0 else "short",
        "entry": x.entry, "qty": x.qty0, "notional": x.entry * x.qty0, "R_usd": x.initR * x.qty0,
        "pnl": x.pnl, "fees": x.fees, "stage": x.stage, "exits": "+".join(f[1] for f in x.fills),
    } for x in trades])
    if len(tr):
        tr["r_mult"] = tr["pnl"] / (tr["R_usd"]).replace(0, np.nan)
        tr["bars"] = ((tr["t_out"] - tr["t_in"]) / pd.Timedelta("1h")).round()
    return pd.Series(eq, index=idx), tr


# ----------------------------------------------------------------------------- metrics
def stats(eq: pd.Series, tr: pd.DataFrame, cap: float) -> dict:
    d = eq.resample("1D").last().dropna()
    r = d.pct_change().dropna()
    yrs = (eq.index[-1] - eq.index[0]).days / 365.25
    dd = eq / eq.cummax() - 1
    out = {
        "start": str(eq.index[0].date()), "end": str(eq.index[-1].date()), "years": round(yrs, 2),
        "final_equity": round(eq.iloc[-1], 2), "net_return_pct": round((eq.iloc[-1] / cap - 1) * 100, 2),
        "cagr_pct": round(((eq.iloc[-1] / cap) ** (1 / yrs) - 1) * 100, 2) if eq.iloc[-1] > 0 else -100.0,
        "max_dd_pct": round(dd.min() * 100, 2),
        "sharpe": round(r.mean() / r.std() * math.sqrt(365), 2) if r.std() > 0 else 0.0,
        "sortino": round(r.mean() / r[r < 0].std() * math.sqrt(365), 2) if (r < 0).any() else 0.0,
        "trades": int(len(tr)),
    }
    out["calmar"] = round(out["cagr_pct"] / abs(out["max_dd_pct"]), 2) if out["max_dd_pct"] else None
    if len(tr):
        w, l = tr[tr.pnl > 0], tr[tr.pnl <= 0]
        out.update({
            "win_rate_pct": round(len(w) / len(tr) * 100, 1),
            "profit_factor": round(w.pnl.sum() / -l.pnl.sum(), 2) if len(l) and l.pnl.sum() < 0 else None,
            "avg_trade_usd": round(tr.pnl.mean(), 2), "avg_R": round(tr.r_mult.mean(), 3),
            "median_R": round(tr.r_mult.median(), 3),
            "fees_usd": round(tr.fees.sum(), 2), "gross_pnl_usd": round((tr.pnl + tr.fees).sum(), 2),
            "avg_bars": round(tr.bars.mean(), 1), "trades_per_year": round(len(tr) / yrs, 1),
            "long_n": int((tr.side == "long").sum()), "long_pnl": round(tr[tr.side == "long"].pnl.sum(), 2),
            "short_n": int((tr.side == "short").sum()), "short_pnl": round(tr[tr.side == "short"].pnl.sum(), 2),
            "max_notional_x_equity": None,
            "t_stat_R": round(tr.r_mult.mean() / tr.r_mult.std() * math.sqrt(len(tr)), 2) if len(tr) > 2 else None,
        })
    return out


def yearly(eq: pd.Series) -> dict:
    y = eq.resample("YE").last()
    prev = pd.concat([pd.Series([eq.iloc[0]]), y.iloc[:-1]]).to_numpy()
    return {str(k.year): round((v / pv - 1) * 100, 1) for k, v, pv in zip(y.index, y.to_numpy(), prev)}


def monte_carlo(tr: pd.DataFrame, cap: float, n: int = 2000, seed: int = 7) -> dict:
    """Bootstrap trade returns (as % of equity at entry) -> distribution of final return and max DD."""
    if len(tr) < 10:
        return {}
    eq_before = cap + tr.pnl.cumsum().shift(1).fillna(0)
    rr = (tr.pnl / eq_before).to_numpy()
    rng = np.random.default_rng(seed)
    fin, mdd = [], []
    for _ in range(n):
        s = rng.choice(rr, len(rr), replace=True)
        path = np.cumprod(1 + s)
        fin.append(path[-1] - 1)
        mdd.append((path / np.maximum.accumulate(np.r_[1.0, path])[1:] - 1).min())
    fin, mdd = np.array(fin), np.array(mdd)
    return {"p5_return_pct": round(np.percentile(fin, 5) * 100, 1), "p50_return_pct": round(np.median(fin) * 100, 1),
            "p95_return_pct": round(np.percentile(fin, 95) * 100, 1), "prob_loss_pct": round((fin < 0).mean() * 100, 1),
            "p50_maxdd_pct": round(np.median(mdd) * 100, 1), "p95_maxdd_pct": round(np.percentile(mdd, 5) * 100, 1)}


def buy_hold(df: pd.DataFrame) -> dict:
    c = df["Close"]
    d = c.resample("1D").last().dropna()
    dd = (d / d.cummax() - 1).min()
    yrs = (c.index[-1] - c.index[0]).days / 365.25
    return {"net_return_pct": round((c.iloc[-1] / c.iloc[0] - 1) * 100, 1),
            "cagr_pct": round(((c.iloc[-1] / c.iloc[0]) ** (1 / yrs) - 1) * 100, 1), "max_dd_pct": round(dd * 100, 1)}


# ----------------------------------------------------------------------------- study
def study(kind: str, df: pd.DataFrame) -> dict:
    P = BtcP if kind == "btc" else XauP
    base = P()
    res = {"bars": len(df)}
    eq, tr = simulate(df, kind, base)
    res["base"] = stats(eq, tr, base.capital)
    res["base"]["max_notional_x_equity"] = round(float((tr.notional / (base.capital + tr.pnl.cumsum().shift(1).fillna(0))).max()), 2) if len(tr) else None
    res["yearly"] = yearly(eq)
    res["monte_carlo"] = monte_carlo(tr, base.capital)
    res["buy_hold"] = buy_hold(df)
    res["exit_mix"] = tr.exits.value_counts().head(8).to_dict() if len(tr) else {}
    OUT.mkdir(parents=True, exist_ok=True)
    tr.to_csv(OUT / f"{kind}_trades.csv", index=False)
    eq.resample("1D").last().to_csv(OUT / f"{kind}_equity_daily.csv")
    # out-of-sample style split: first 60% vs last 40% of time
    cut = df.index[int(len(df) * 0.6)]
    res["split"] = {}
    for nm, part in (("first_60pct", df[df.index < cut]), ("last_40pct", df[df.index >= cut])):
        e2, t2 = simulate(part, kind, base)
        res["split"][nm] = stats(e2, t2, base.capital)
    # cost and variant stress
    var = {"no_costs": replace(base, comm=0.0, slip_ticks=0), "costs_x2": replace(base, comm=base.comm * 2, slip_ticks=base.slip_ticks * 2),
           "funding_0.01pct_8h": replace(base, funding_8h=0.0001), "no_macro_filter": replace(base, use_macro=False)}
    if kind == "xau":
        var["okx_contract_sizing(qty*0.1)"] = replace(base, qty_mult=0.1)
        var["tp2_33pct_like_alert"] = replace(base, tp2_pct=33.0)
    res["variants"] = {}
    for nm, pv in var.items():
        e2, t2 = simulate(df, kind, pv)
        res["variants"][nm] = stats(e2, t2, pv.capital)
    # parameter neighbourhood (one at a time, +/- ~25 %)
    grid = {"btc": {"atr_stop": [1.5, 2.5], "tp1_r": [1.2, 2.0], "trail_atr": [1.5, 3.0], "sweep_lb": [10, 30], "er_min": [0.25, 0.45], "volz_min": [0.0, 0.5]},
            "xau": {"atr_stop": [1.0, 2.0], "tp1_r": [0.9, 1.5], "tp2_r": [2.0, 3.0], "trail_atr": [1.0, 2.0], "sess_to": [16, 21]}}[kind]
    res["sensitivity"] = {}
    for k, vals in grid.items():
        for v in vals:
            e2, t2 = simulate(df, kind, replace(base, **{k: v}))
            s = stats(e2, t2, base.capital)
            res["sensitivity"][f"{k}={v}"] = {x: s.get(x) for x in ("net_return_pct", "max_dd_pct", "sharpe", "trades", "profit_factor")}
    return res


def load(kind: str, path: str) -> pd.DataFrame:
    df = pd.read_csv(path, index_col=0, parse_dates=True)
    df.index = pd.to_datetime(df.index, utc=True).tz_localize(None)
    df = df[~df.index.duplicated()].sort_index()
    if "Volume" not in df:
        df["Volume"] = 0.0
    return df[["Open", "High", "Low", "Close", "Volume"]].astype(float).dropna()


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--btc")
    ap.add_argument("--xau")
    a = ap.parse_args()
    report = {}
    for kind, pth in (("btc", a.btc), ("xau", a.xau)):
        if pth:
            report[kind] = study(kind, load(kind, pth))
            print(kind, json.dumps(report[kind]["base"], indent=1))
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "report.json").write_text(json.dumps(report, indent=1, default=str))
