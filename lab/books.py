"""Paper portfolio books on top of the arena (A / B / C ...): frozen membership, leverage, costs,
per-position liquidation cap, optional volatility target. Forward record = bars after the book was created.

Top-N = highest backtest Sharpe among ACTIVE members on the creation day, one strategy per coin.
"""
from __future__ import annotations

import json

import numpy as np
import pandas as pd

from lab import metrics, perp, protect


def _now():
    from lab.arena import now_iso
    return now_iso()


def ensure(path, ro: dict, cfg: dict) -> dict:
    """Create the frozen books once; later runs only add books that are new in the config."""
    bc = cfg.get("books", {})
    data = json.loads(path.read_text()) if path.exists() else {"books": {}}
    active = [m for m in ro["members"] if m["status"] == "active"]
    sharpe = {m["id"]: ((m.get("backtest") or {}).get("sharpe") or 0) for m in active}
    coin = {m["id"]: m["coin"] for m in active}
    ranked, seen = [], set()
    for i in sorted(sharpe, key=lambda k: -sharpe[k]):
        if coin[i] not in seen:
            ranked.append(i); seen.add(coin[i])
    changed = False
    for b in bc.get("list", []):
        if b["id"] in data["books"]:
            continue
        ids = [m["id"] for m in active] if b.get("select") == "all" else ranked[: int(b.get("n", 5))]
        data["books"][b["id"]] = {**b, "members": ids, "created_at": _now()}
        changed = True
    if changed:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(data, indent=1, ensure_ascii=False))
    return data


def returns(book: dict, R: pd.DataFrame, X: pd.DataFrame, ro: dict, p, cps: float, mmr: float) -> pd.Series:
    ids = [i for i in book["members"] if i in R.columns]
    if not ids:
        return pd.Series(0.0, index=R.index)
    L = float(book.get("leverage", 1))
    by_id = {m["id"]: m for m in ro["members"]}
    alive = pd.DataFrame({i: p.c[by_id[i]["coin"]].notna() for i in ids}, index=R.index)
    for i in ids:                                    # retired -> its share goes to cash from that date
        z = by_id[i].get("retired_at")
        if by_id[i]["status"] == "retired" and z:
            alive.loc[alive.index >= pd.Timestamp(z).tz_localize(None), i] = False
    Rl = (R[ids] * L).clip(lower=-(1.0 - mmr * L))  # isolated margin: loss per bar capped at the margin
    if book.get("weighting") == "invvol":             # past 90 days, monthly; retired -> cash
        r = protect.weighted_book(Rl, X[ids], alive, ids, "invvol", cps * L, p.ppy)
    else:
        n0 = len(ids)
        W = alive.astype(float) / n0                # fixed 1/N slots: an empty slot stays in cash
        ones = pd.DataFrame(1.0, index=R.index, columns=ids)
        r = protect.book(Rl, X[ids], W, ones, cps * L)
    if book.get("vol_target"):
        sc = protect.vol_target_scale(r, float(book["vol_target"]), p.ppy)
        r = r * sc - sc.diff().abs().fillna(0) * cps * L
    return r


def report(data: dict, R, X, ro, p, cps, cfg) -> list[dict]:
    mmr = cfg.get("books", {}).get("maint_margin", 0.005)
    metrics.set_periods(p.ppy)
    end = R.index[-1]
    out = []
    for bid, b in data["books"].items():
        r = returns(b, R, X, ro, p, cps, mmr)
        a = pd.Timestamp(b["created_at"]).tz_localize(None)
        f = r[r.index > a]
        bt = r[r.index <= a]
        bt = bt[bt.ne(0).cummax()]
        out.append({
            "id": bid, "name": b["name"], "members": b["members"], "leverage": b.get("leverage", 1),
            "vol_target": b.get("vol_target"), "created_at": b["created_at"][:10],
            "forward": {"days": max(0, (end - a).days), "ret": round(float((1 + f).prod() - 1), 4) if len(f) else 0.0,
                        "balance_1000": round(1000 * float((1 + f).prod()), 2) if len(f) else 1000.0,
                        "sharpe": round(metrics.sharpe(f), 2) if len(f) > 20 else None,
                        "max_dd": round(metrics.max_drawdown(f), 4) if len(f) else 0.0},
            "backtest": {"cagr": round(metrics.cagr(bt), 4) if len(bt) > 30 else None,
                         "max_dd": round(metrics.max_drawdown(bt), 4) if len(bt) else None,
                         "sharpe": round(metrics.sharpe(bt), 2) if len(bt) > 30 else None},
            "spark_fwd": perp.sparkline(f, 90), "spark_bt": perp.sparkline(bt, 120),
        })
    return out
