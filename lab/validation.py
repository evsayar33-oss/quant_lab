"""Validation pipeline: the gate a hypothesis must pass before any bot may use it.

Steps
  1. Full-sample parameter sweep (all grid points)  -> counts the trials for DSR
  2. Walk-forward: choose params on a rolling in-sample window, trade them out-of-sample
  3. Out-of-sample stats + Deflated Sharpe Ratio (corrected for number of trials)
  4. Cost stress: 2x costs must still beat the benchmark
  5. Stationary block bootstrap of OOS returns -> P(Sharpe > 0), 5th-percentile CAGR
  6. Sub-period stability: OOS Sharpe per calendar-year block
  7. Verdict: ACCEPT / WATCH / REJECT with the reasons written out
"""
from __future__ import annotations

import itertools
import math

import numpy as np
import pandas as pd

from lab import engine, metrics
from lab.engine import Costs
from lab.strategies import Strategy, get


def grid_points(grid: dict) -> list[dict]:
    if not grid:
        return [{}]
    keys = list(grid)
    return [dict(zip(keys, v)) for v in itertools.product(*(grid[k] for k in keys))]


def sweep(strat: Strategy, prices: pd.DataFrame, costs: Costs) -> pd.DataFrame:
    rows = []
    for p in grid_points(strat.grid):
        try:
            res = engine.run(prices, strat(prices, **p), costs)
            rows.append({**p, "sharpe": metrics.sharpe(res.returns), "cagr": metrics.cagr(res.returns),
                         "max_dd": metrics.max_drawdown(res.returns), "_returns": res.returns})
        except Exception as e:  # noqa: BLE001
            rows.append({**p, "sharpe": np.nan, "error": str(e)})
    return pd.DataFrame(rows)


def walk_forward(strat: Strategy, prices: pd.DataFrame, costs: Costs,
                 train_years: float = 3.0, test_months: int = 6) -> tuple[pd.Series, list[dict]]:
    """Anchored-free rolling walk-forward. Returns stitched OOS returns and the chosen params."""
    points = grid_points(strat.grid)
    idx = prices.index
    train = int(train_years * 252)
    step = int(test_months * 21)
    warm = 260  # indicators need history before the train window
    oos_parts, log = [], []
    t0 = warm + train
    while t0 < len(idx) - 5:
        tr = slice(idx[t0 - train], idx[t0 - 1])
        te_end = idx[min(t0 + step, len(idx)) - 1]
        best, best_sr = points[0], -np.inf
        if len(points) > 1:
            for p in points:
                w = strat(prices.iloc[:t0], **p)
                r = engine.run(prices.iloc[:t0], w, costs).returns.loc[tr]
                sr = metrics.sharpe(r)
                if sr > best_sr:
                    best, best_sr = p, sr
        # Trade the chosen params on data that includes the test window; weights at t
        # only use data <= t, so computing on the longer slice adds no look-ahead.
        hist = prices.iloc[: min(t0 + step, len(idx))]
        r_all = engine.run(hist, strat(hist, **best), costs).returns
        oos_parts.append(r_all.loc[idx[t0]:te_end])
        log.append({"test_start": str(idx[t0].date()), "test_end": str(te_end.date()),
                    "params": best, "is_sharpe": round(float(best_sr), 3) if np.isfinite(best_sr) else None})
        t0 += step
    oos = pd.concat(oos_parts) if oos_parts else pd.Series(dtype=float)
    return oos[~oos.index.duplicated()], log


def block_bootstrap(r: pd.Series, n: int = 1000, block: int = 21, seed: int = 7) -> dict:
    r = r.dropna().values
    if len(r) < block * 3:
        return {"p_sharpe_pos": None, "cagr_p05": None, "maxdd_p05": None}
    rng = np.random.default_rng(seed)
    T = len(r)
    srs, cg, dd = [], [], []
    for _ in range(n):
        out = np.empty(T)
        i = 0
        while i < T:
            s = rng.integers(0, T - block)
            L = min(rng.geometric(1 / block), T - i)
            seg = r[s:s + L]
            out[i:i + len(seg)] = seg
            i += max(len(seg), 1)
        sr = out.mean() / out.std() * math.sqrt(252) if out.std() > 0 else 0
        srs.append(sr)
        eq = np.cumprod(1 + out)
        cg.append(eq[-1] ** (252 / T) - 1 if eq[-1] > 0 else -1)
        dd.append((eq / np.maximum.accumulate(eq) - 1).min())
    return {"p_sharpe_pos": round(float(np.mean(np.array(srs) > 0)), 3),
            "cagr_p05": round(float(np.percentile(cg, 5)), 4),
            "maxdd_p05": round(float(np.percentile(dd, 5)), 4)}


def yearly_sharpe(r: pd.Series) -> dict:
    return {str(y): round(metrics.sharpe(g), 2) for y, g in r.groupby(r.index.year) if len(g) > 40}


# Gate thresholds. Change them only with a written reason in hypotheses/CHANGELOG.md.
GATE = {
    "min_oos_years": 3.0,
    "min_dsr": 0.90,          # deflated Sharpe probability
    "min_oos_sharpe": 0.5,
    "min_p_sharpe_pos": 0.85,  # bootstrap
    "max_dd_floor": -0.45,
    "min_pos_year_frac": 0.55,
}


def verdict(rep: dict) -> tuple[str, list[str]]:
    o, why = rep["oos"], []
    ok = True
    def check(cond, msg):
        nonlocal ok
        if not cond:
            ok = False
            why.append(msg)
    check(o["years"] >= GATE["min_oos_years"], f"OOS too short ({o['years']}y < {GATE['min_oos_years']}y)")
    check(rep["dsr"] >= GATE["min_dsr"], f"DSR {rep['dsr']} < {GATE['min_dsr']} (may be luck after {rep['n_trials']} trials)")
    check(o["sharpe"] >= GATE["min_oos_sharpe"], f"OOS Sharpe {o['sharpe']} < {GATE['min_oos_sharpe']}")
    check(o["max_dd"] >= GATE["max_dd_floor"], f"OOS MaxDD {o['max_dd']} worse than {GATE['max_dd_floor']}")
    bs = rep["bootstrap"]["p_sharpe_pos"]
    check(bs is not None and bs >= GATE["min_p_sharpe_pos"], f"bootstrap P(SR>0) {bs} < {GATE['min_p_sharpe_pos']}")
    ys = list(rep["yearly_sharpe"].values())
    frac = (sum(v > 0 for v in ys) / len(ys)) if ys else 0
    check(frac >= GATE["min_pos_year_frac"], f"only {frac:.0%} of years positive")
    beats = rep["stress_2x_cost"]["sharpe"] > rep["benchmark"]["sharpe"]
    check(beats, "with 2x costs it does not beat the equal-weight benchmark")
    if ok:
        return "ACCEPT", ["all gate checks passed"]
    soft = o["sharpe"] > 0 and rep["dsr"] >= 0.5 and o["years"] >= 1
    return ("WATCH" if soft else "REJECT"), why


def validate(strategy_name: str, prices: pd.DataFrame, costs: Costs,
             train_years: float = 3.0, test_months: int = 6) -> dict:
    strat = get(strategy_name)
    sw = sweep(strat, prices, costs)
    trial_srs = [s / math.sqrt(252) for s in sw["sharpe"].dropna()]  # per-period for DSR
    n_trials = max(len(trial_srs), 1)
    oos, wf_log = walk_forward(strat, prices, costs, train_years, test_months)
    bench = engine.run(prices, get("equal_weight")(prices), costs).returns
    stress = Costs(costs.commission * 2, costs.slippage * 2, costs.borrow_annual)
    oos_stress, _ = walk_forward(strat, prices, stress, train_years, test_months) if len(oos) else (oos, [])
    b_oos = bench.reindex(oos.index).fillna(0) if len(oos) else bench
    rep = {
        "strategy": strategy_name,
        "source": strat.source,
        "n_assets": int(prices.shape[1]),
        "data_start": str(prices.index[0].date()),
        "data_end": str(prices.index[-1].date()),
        "costs": {"commission": costs.commission, "slippage": costs.slippage},
        "n_trials": n_trials,
        "full_sample_sweep": sw.drop(columns=[c for c in sw.columns if c.startswith("_")])
                               .sort_values("sharpe", ascending=False).head(10).round(4).to_dict("records"),
        "oos": metrics.summary(oos, bench=b_oos) if len(oos) > 30 else {"years": 0, "sharpe": 0, "max_dd": 0},
        "dsr": round(metrics.dsr(oos, n_trials, trial_srs), 3) if len(oos) > 30 else 0.0,
        "benchmark": metrics.summary(b_oos) if len(b_oos) > 30 else {"sharpe": 0},
        "stress_2x_cost": {"sharpe": round(metrics.sharpe(oos_stress), 3) if len(oos_stress) else 0.0},
        "bootstrap": block_bootstrap(oos),
        "yearly_sharpe": yearly_sharpe(oos) if len(oos) else {},
        "walk_forward": wf_log,
        "current_params": wf_log[-1]["params"] if wf_log else strat.defaults,
    }
    rep["verdict"], rep["reasons"] = verdict(rep)
    rep["_oos_returns"] = oos
    return rep


def current_targets(strategy_name: str, prices: pd.DataFrame, params: dict) -> dict:
    """Latest target weights (what a bot should hold from the next session)."""
    w = get(strategy_name)(prices, **params)
    last = w.iloc[-1]
    return {k: round(float(v), 4) for k, v in last[last.abs() > 1e-6].sort_values(ascending=False).items()}
