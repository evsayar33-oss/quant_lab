"""Event-style trade engine for entry/exit rules (bar-by-bar, vectorized across assets).

Execution model (conservative, no look-ahead):
  * Signals are read at the CLOSE of day t-1 and executed at the OPEN of day t.
  * Order of events on day t:  open (signal exits, then entries)  ->  intraday stops/targets
    (stop wins if both are touched in the same bar)  ->  close (trailing stop update, time stop).
  * Gaps: if the open is already beyond the stop/target, the fill is the open price.
  * Every fill pays costs.per_turnover on the traded slot.
  * Position size = 1/max_positions (default 1/N assets). With max_positions < N, new
    entries are ranked by 63-day momentum (documented tie-break, no hidden choice).

Exit options (ExitCfg): stop (ATR x or %), target (ATR x, % or R-multiple),
trailing stop (ATR chandelier or %), max holding days, plus the rule's own exit signal.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass

import numpy as np
import pandas as pd

from lab import indicators as I
from lab.engine import Costs, Result
from lab.panel import Panel
from lab.rules import Signals


@dataclass(frozen=True)
class ExitCfg:
    stop_atr: float | None = None
    stop_pct: float | None = None
    tp_atr: float | None = None
    tp_pct: float | None = None
    tp_r: float | None = None          # target = R x initial risk (needs a stop)
    trail_atr: float | None = None
    trail_pct: float | None = None
    max_hold: int | None = None
    atr_n: int = 14
    use_signal_exit: bool = True

    def label(self) -> str:
        d = {k: v for k, v in asdict(self).items() if v not in (None, 14, True)}
        return ",".join(f"{k}={v}" for k, v in d.items()) or "signal_only"


EXIT_GRID: list[ExitCfg] = [
    ExitCfg(),
    ExitCfg(stop_atr=2.0), ExitCfg(stop_atr=3.0),
    ExitCfg(stop_pct=0.05), ExitCfg(stop_pct=0.08),
    ExitCfg(stop_atr=2.0, tp_r=2.0), ExitCfg(stop_atr=2.0, tp_r=3.0),
    ExitCfg(stop_atr=1.5, tp_atr=3.0),
    ExitCfg(trail_atr=3.0), ExitCfg(trail_pct=0.10),
    ExitCfg(stop_atr=2.0, trail_atr=3.0),
    ExitCfg(max_hold=5), ExitCfg(max_hold=10), ExitCfg(max_hold=20),
    ExitCfg(stop_atr=2.0, max_hold=10),
    ExitCfg(stop_atr=2.0, tp_r=2.0, use_signal_exit=False),
    ExitCfg(trail_atr=3.0, use_signal_exit=False),
]


def run_trades(p: Panel, sig: Signals, ex: ExitCfg = ExitCfg(), costs: Costs = Costs(),
               side: str = "long", max_positions: int | None = None) -> Result:
    idx, cols = p.index, p.columns
    T, N = p.c.shape
    c_raw = p.c.values
    C = p.c.ffill().values
    O = np.where(np.isnan(p.o.values), C, p.o.values)
    H = np.where(np.isnan(p.h.values), C, p.h.values)
    L = np.where(np.isnan(p.l.values), C, p.l.values)
    A = I.atr(p.h, p.l, p.c, ex.atr_n).values
    score = (p.c / p.c.shift(63)).values

    def arr(x):
        return np.zeros((T, N), bool) if x is None else x.reindex(index=idx, columns=cols).fillna(False).values.astype(bool)

    eL, xL = arr(sig.entry_long), arr(sig.exit_long)
    eS, xS = arr(sig.entry_short), arr(sig.exit_short)
    if side == "long":
        eS[:] = False
    elif side == "short":
        eL[:] = False

    slots = max_positions or N
    w = 1.0 / slots
    cpt = costs.per_turnover

    pos = np.zeros(N)                 # +1 / -1 / 0
    entry_px = np.full(N, np.nan)
    stop = np.full(N, np.nan)
    tgt = np.full(N, np.nan)
    ext = np.full(N, np.nan)          # extreme since entry (for trailing)
    held = np.zeros(N, int)
    entry_i = np.zeros(N, int)
    time_exit = np.zeros(N, bool)

    port = np.zeros(T)
    turn = np.zeros(T)
    wts = np.zeros((T, N))
    trades: list[tuple] = []

    def close_pos(mask, px, i, reason, start):
        nonlocal_r = np.where(mask, pos * (px / start - 1), 0.0)
        for j in np.nonzero(mask)[0]:
            trades.append((idx[entry_i[j]], idx[i], cols[j], int(pos[j]), float(entry_px[j]), float(px[j]),
                           float(pos[j] * (px[j] / entry_px[j] - 1)), int(held[j]), reason))
        return nonlocal_r

    for i in range(1, T):
        r = np.zeros(N)
        traded = np.zeros(N)
        start = C[i - 1].copy()
        alive = ~np.isnan(c_raw[i])

        # ---------- open: signal / time exits decided at close i-1
        if ex.use_signal_exit:
            want_exit = ((pos > 0) & xL[i - 1]) | ((pos < 0) & xS[i - 1])
        else:
            want_exit = np.zeros(N, bool)
        # opposite entry also closes the position (reversal)
        want_exit |= ((pos > 0) & eS[i - 1]) | ((pos < 0) & eL[i - 1])
        for m, why in ((time_exit & (pos != 0) & alive, "time"), (want_exit & (pos != 0) & alive, "signal")):
            if m.any():
                r += close_pos(m, O[i], i, why, start)
                traded += m
                pos[m] = 0
        time_exit[:] = False

        # ---------- open: entries decided at close i-1
        cand_l = eL[i - 1] & (pos == 0) & alive & ~np.isnan(A[i - 1])
        cand_s = eS[i - 1] & (pos == 0) & alive & ~np.isnan(A[i - 1]) & ~cand_l
        cand = cand_l | cand_s
        if cand.any():
            free = slots - int((pos != 0).sum())
            if free <= 0:
                cand[:] = False
            elif cand.sum() > free:
                sc = np.where(cand, np.nan_to_num(np.where(cand_l, score[i - 1], -score[i - 1]), nan=-np.inf), -np.inf)
                keep = np.argsort(-sc)[:free]
                mask = np.zeros(N, bool); mask[keep] = True
                cand &= mask
            new_side = np.where(cand_l & cand, 1.0, np.where(cand_s & cand, -1.0, 0.0))
            newm = new_side != 0
            pos[newm] = new_side[newm]
            entry_px[newm] = O[i][newm]
            entry_i[newm] = i
            held[newm] = 0
            ext[newm] = O[i][newm]
            a = A[i - 1]
            risk = np.full(N, np.nan)
            if ex.stop_atr:
                risk = ex.stop_atr * a
            elif ex.stop_pct:
                risk = ex.stop_pct * O[i]
            stop[newm] = (O[i] - pos * risk)[newm]
            t = np.full(N, np.nan)
            if ex.tp_atr:
                t = O[i] + pos * ex.tp_atr * a
            elif ex.tp_pct:
                t = O[i] * (1 + pos * ex.tp_pct)
            elif ex.tp_r and (ex.stop_atr or ex.stop_pct):
                t = O[i] + pos * ex.tp_r * risk
            tgt[newm] = t[newm]
            start = np.where(newm, O[i], start)
            traded += newm

        # ---------- intraday stops / targets
        live = (pos != 0) & alive
        if live.any():
            lg, sh = live & (pos > 0), live & (pos < 0)
            hit_s = (lg & (L[i] <= stop)) | (sh & (H[i] >= stop))
            hit_t = (lg & (H[i] >= tgt)) | (sh & (L[i] <= tgt)) & ~hit_s
            hit_t &= ~hit_s
            if hit_s.any():
                fill = np.where(lg, np.minimum(O[i], stop), np.maximum(O[i], stop))
                fill = np.where(entry_i == i, stop, fill)  # entered today: stop price
                r += close_pos(hit_s, fill, i, "stop", start)
                traded += hit_s
                pos[hit_s] = 0
            if hit_t.any():
                fill = np.where(lg, np.maximum(O[i], tgt), np.minimum(O[i], tgt))
                fill = np.where(entry_i == i, tgt, fill)
                r += close_pos(hit_t, fill, i, "target", start)
                traded += hit_t
                pos[hit_t] = 0

        # ---------- close: mark to market, trailing, time stop
        live = pos != 0
        r += np.where(live, pos * (C[i] / start - 1), 0.0)
        if live.any():
            held[live] += 1
            ext = np.where(live & (pos > 0), np.fmax(ext, H[i]), np.where(live & (pos < 0), np.fmin(ext, L[i]), ext))
            if ex.trail_atr:
                trail = ext - pos * ex.trail_atr * A[i]
            elif ex.trail_pct:
                trail = ext * (1 - pos * ex.trail_pct)
            else:
                trail = None
            if trail is not None:
                stop = np.where(live & (pos > 0), np.fmax(stop, trail),
                                np.where(live & (pos < 0), np.fmin(stop, trail), stop))
            if ex.max_hold:
                time_exit = live & (held >= ex.max_hold)

        port[i] = w * r.sum() - w * cpt * traded.sum()
        turn[i] = w * traded.sum()
        wts[i] = pos * w

    ret = pd.Series(port, idx)
    tlog = pd.DataFrame(trades, columns=["entry", "exit", "asset", "side", "entry_px", "exit_px",
                                         "ret", "bars", "reason"])
    held_w = pd.DataFrame(wts, idx, cols)
    first = held_w.abs().sum(axis=1).gt(0)
    if first.any():
        s = first.idxmax()
        ret, held_w = ret.loc[s:], held_w.loc[s:]
        turnover = pd.Series(turn, idx).loc[s:]
    else:
        turnover = pd.Series(turn, idx)
    return Result(ret, ret, held_w, turnover, meta={"trades": tlog, "exit": ex.label()})


def trade_stats(tlog: pd.DataFrame) -> dict:
    if tlog is None or tlog.empty:
        return {"n_trades": 0}
    r = tlog["ret"]
    wins, losses = r[r > 0], r[r <= 0]
    pf = wins.sum() / abs(losses.sum()) if losses.sum() != 0 else None
    return {
        "n_trades": int(len(r)),
        "win_rate": round(float((r > 0).mean()), 3),
        "avg_trade": round(float(r.mean()), 4),
        "avg_win": round(float(wins.mean()), 4) if len(wins) else None,
        "avg_loss": round(float(losses.mean()), 4) if len(losses) else None,
        "profit_factor": round(float(pf), 3) if pf is not None else None,
        "payoff": round(float(wins.mean() / abs(losses.mean())), 3) if len(wins) and len(losses) and losses.mean() else None,
        "avg_bars": round(float(tlog["bars"].mean()), 1),
        "exit_reasons": tlog["reason"].value_counts().to_dict(),
        "trades_per_year": None,
    }
