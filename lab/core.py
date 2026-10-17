"""Core study: simple, literature-based crypto rules with FIXED settings (config/core.yaml).

No parameter search and no selection: every rule runs once with its textbook setting, so the number of
trials is tiny (rules x 3 books) and the Deflated Sharpe penalty is small. Rules are evaluated on the full
history and on each forward window after the time-machine cutoffs (the rules never change, so a forward
window is simply "after that date"). Acceptance (written before results): see config/core.yaml.
"""
from __future__ import annotations

import math

import numpy as np
import pandas as pd

from lab import metrics, perp, regime

CRISES_KEY = "crypto"


def _bars(days, ppy):
    return regime.bars(days, ppy)


def exposure(close: pd.Series, rule: str, prm: dict, ppy: float) -> pd.Series:
    """Target exposure in [0, 1] decided at the close of each bar (used from the next bar)."""
    r = close.pct_change(fill_method=None)
    one = pd.Series(1.0, index=close.index)
    if rule == "buy_hold":
        e = one
    elif rule == "vol_target":
        e = _vt(r, prm, ppy)
    elif rule == "trend_sma200":
        e = (close > close.rolling(_bars(prm["sma_days"], ppy), min_periods=_bars(prm["sma_days"], ppy)).mean()).astype(float)
    elif rule == "tsmom":
        e = _tsmom(close, prm, ppy)
    elif rule == "tsmom_vt":
        e = _tsmom(close, prm, ppy) * _vt(r, prm, ppy)
    elif rule == "dual_trend_vt":
        n = _bars(prm["sma_days"], ppy)
        up = (close > close.rolling(n, min_periods=n).mean()).astype(float)
        e = up * (_tsmom(close, prm, ppy) > 0).astype(float) * _vt(r, prm, ppy)
    else:
        raise ValueError(rule)
    return e.where(close.notna()).fillna(0.0).clip(0, 1)


def _vt(r, prm, ppy):
    look = _bars(prm.get("lookback_days", 30), ppy)
    vol = r.rolling(look, min_periods=look // 2).std() * math.sqrt(ppy)
    return (prm.get("target", 0.4) / vol).clip(upper=1.0).fillna(0.0)


def _tsmom(close, prm, ppy):
    sig = [(close / close.shift(_bars(h, ppy)) - 1 > 0).astype(float) for h in prm["horizons_days"]]
    return sum(sig) / len(sig)


def book_returns(closes: dict, rule: str, prm: dict, ppy: float, cps: float) -> pd.Series:
    """Equal capital across the assets in `closes`; each asset follows the rule; costs on exposure changes."""
    parts = []
    for _, c in closes.items():
        e = exposure(c, rule, prm, ppy).shift(1).fillna(0.0)       # decided at t-1, held during t
        r = c.pct_change(fill_method=None).fillna(0.0)
        parts.append(e * r - e.diff().abs().fillna(e) * cps)
    out = sum(parts) / len(parts)
    first = max(c.first_valid_index() for c in closes.values())
    return out[out.index >= first]


def book_exposure(closes: dict, rule: str, prm: dict, ppy: float) -> pd.Series:
    ex = [exposure(c, rule, prm, ppy).shift(1).fillna(0.0) for c in closes.values()]
    return sum(ex) / len(ex)


def stats(r: pd.Series, ppy: float) -> dict:
    metrics.set_periods(ppy)
    r = r.dropna()
    if len(r) < 30:
        return {}
    yr = (1 + r).groupby(r.index.year).prod() - 1
    return {"start": str(r.index[0].date()), "final_1000": round(1000 * float((1 + r).prod()), 0),
            "cagr": round(metrics.cagr(r), 4), "sharpe": round(metrics.sharpe(r), 2),
            "max_dd": round(metrics.max_drawdown(r), 4), "worst_year": round(float(yr.min()), 4),
            "yearly": {str(k): round(float(v), 4) for k, v in yr.items()}}


def run(p, cfg: dict) -> dict:
    from lab import protect
    ppy = p.ppy
    cps = cfg["costs"]["commission"] + cfg["costs"]["slippage"]
    assets = [a for a in cfg["universe_assets"] if a in p.columns]
    books = {a.split("/")[0]: {a: p.c[a]} for a in assets}
    if len(assets) >= 2:
        books["BTC+ETH"] = {a: p.c[a] for a in assets}
    crises = protect.load_cfg(CRISES_KEY)["crises"]
    acc = cfg.get("accept", {})
    rows, series = [], {}
    for bname, closes in books.items():
        for rule, prm in cfg["rules"].items():
            r = book_returns(closes, rule, prm or {}, ppy, cps)
            series[(bname, rule)] = r
            row = {"book": bname, "rule": rule, "full": stats(r, ppy), "crises": protect.crisis_table(r, crises),
                   "windows": {c: stats(r[r.index > pd.Timestamp(c)], ppy) for c in cfg["cutoffs"]}}
            rows.append(row)
    # acceptance vs buy-and-hold of the same book, in every forward window
    n_trials = len(rows)
    srs = [series[k].mean() / series[k].std() for k in series if series[k].std() > 0]
    for row in rows:
        bh = next(x for x in rows if x["book"] == row["book"] and x["rule"] == "buy_hold")
        row["dsr"] = round(metrics.dsr(series[(row["book"], row["rule"])], n_trials, srs), 3)
        if row["rule"] == "buy_hold":
            row["approved"] = None
            continue
        chk = {}
        for c in cfg["cutoffs"]:
            w, b = row["windows"].get(c) or {}, bh["windows"].get(c) or {}
            if not w or not b:
                chk[c] = False
                continue
            dd_ok = w["max_dd"] >= b["max_dd"] * (1 - acc.get("dd_reduction_vs_buyhold", 0.33))
            sr_ok = w["sharpe"] >= b["sharpe"] - acc.get("max_sharpe_gap", 0.10)
            ret_ok = (w["final_1000"] > 1000) if acc.get("positive_return", True) else True
            chk[c] = {"dd": dd_ok, "sharpe": sr_ok, "ret": ret_ok}
        row["checks"] = chk
        row["approved"] = all(isinstance(v, dict) and all(v.values()) for v in chk.values())
    return {"timeframe": p.freq, "data_end": str(p.index[-1]), "n_trials": n_trials, "rows": rows,
            "spark": {f"{b}|{r}": perp.sparkline(s, 120) for (b, r), s in series.items()}}


NAMES = {"buy_hold": "Al-tut", "vol_target": "Volatilite hedefi %40", "trend_sma200": "Trend (SMA200)",
         "tsmom": "Zaman serisi momentumu (30/90/180g)", "tsmom_vt": "Momentum + vol hedefi",
         "dual_trend_vt": "SMA200 + momentum + vol hedefi"}


def markdown(o: dict, cfg: dict) -> str:
    f = lambda v: "–" if v is None else f"{v:+.0%}"   # noqa: E731
    cut = cfg["cutoffs"]
    L = [f"# Çekirdek çalışma — {o['timeframe']}", "",
         f"Sabit ayarlı {len(cfg['rules'])} kural × {len({r['book'] for r in o['rows']})} portföy = **{o['n_trials']} deneme** "
         "(ayar taraması yok). Kabul kuralları sonuçlardan önce yazıldı (`config/core.yaml`): her ileri pencerede aynı "
         "varlığın al-tutuna göre düşüş ≥ 1/3 az, Sharpe en fazla 0.10 düşük, getiri pozitif.", ""]
    for book in dict.fromkeys(r["book"] for r in o["rows"]):
        L += [f"## {book}", "", "| Kural | Tüm geçmiş $1000 → | Yıllık | Sharpe | Maks. düşüş | "
              + " | ".join(f"{c[:7]} → $" for c in cut) + " | " + " | ".join(f"{c[:7]} DD" for c in cut) + " | Onay |",
              "|---|---|---|---|---|" + "---|" * (2 * len(cut)) + "---|"]
        for r in [x for x in o["rows"] if x["book"] == book]:
            fu, w = r["full"], r["windows"]
            ap = "–" if r["approved"] is None else ("✅" if r["approved"] else "❌")
            L.append(f"| {NAMES.get(r['rule'], r['rule'])} | {fu.get('final_1000', 0):,.0f} | {f(fu.get('cagr'))} | {fu.get('sharpe')} | "
                     f"{f(fu.get('max_dd'))} | " + " | ".join(f"{(w.get(c) or {}).get('final_1000', 0):,.0f}" for c in cut) + " | "
                     + " | ".join(f(((w.get(c) or {}).get('max_dd'))) for c in cut) + f" | {ap} |")
        L.append("")
    L += ["## Zayıf yönler", "",
          "- Kurallar literatürden; ama kriptoda bu literatür kısa (2014 sonrası). Ayarlar (200 gün, 30/90/180 gün, %40) standart değerlerdir, kriptoya göre seçilmedi.",
          "- Sadece BTC/ETH: alt-coin getirisi yok; buna karşılık survivorship riski çok düşük.",
          "- Spot varsayımı: perp ile yapılırsa funding maliyeti eklenir.",
          "- Üç ileri pencere iç içedir (2022 penceresi 2023 ve 2024'ü de içerir); bağımsız üç test değildir."]
    return "\n".join(L)
