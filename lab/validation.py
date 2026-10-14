"""Validation pipeline: the gate a hypothesis must pass before any bot may use it.

  1. Sweep every variant on the full history (causal -> reusable slices). Counts trials.
     Rule candidates: stage 2 adds every exit config to the best stage-1 variants.
  2. Walk-forward: in each rolling train window pick the best Sharpe variant, trade it on
     the next test window. Stitched test windows = out-of-sample (OOS) record.
  3. Deflated Sharpe Ratio of OOS (corrected for ALL trials) and PBO via CSCV.
  4. Cost stress: OOS minus an extra 1x cost on the realised turnover (= 2x costs).
  5. Block bootstrap of OOS, yearly stability, market-regime breakdown, trade statistics.
  6. Verdict ACCEPT / WATCH / REJECT with every failed check written out.
"""
from __future__ import annotations

import math

import numpy as np
import pandas as pd

from lab import candidates as CD
from lab import metrics
from lab.engine import Costs
from lab.panel import Panel
from lab.trade_engine import trade_stats

GATE = {
    "min_oos_years": 3.0,
    "min_dsr": 0.90,
    "min_oos_sharpe": 0.5,
    "min_p_sharpe_pos": 0.85,
    "max_dd_floor": -0.45,
    "min_pos_year_frac": 0.55,
    "max_pbo": 0.50,
    "min_trades": 30,          # rule candidates only
}


def _matrix(runs: dict, index) -> tuple[pd.DataFrame, pd.DataFrame]:
    R = pd.DataFrame({k: v[0] for k, v in runs.items()}).reindex(index).fillna(0.0)
    TO = pd.DataFrame({k: v[1] for k, v in runs.items()}).reindex(index).fillna(0.0)
    return R, TO


def walk_forward(R: pd.DataFrame, TO: pd.DataFrame, train_years=3.0, test_months=6, warm=260):
    idx = R.index
    train, step = int(train_years * 252), int(test_months * 21)
    parts, tparts, log = [], [], []
    t0 = warm + train
    while t0 < len(idx) - 5:
        te = min(t0 + step, len(idx))
        tr = R.iloc[t0 - train:t0]
        sd = tr.std()
        sr = (tr.mean() / sd.where(sd > 0)).fillna(-np.inf)
        best = sr.idxmax()
        parts.append(R[best].iloc[t0:te])
        tparts.append(TO[best].iloc[t0:te])
        log.append({"test_start": str(idx[t0].date()), "test_end": str(idx[te - 1].date()),
                    "variant": best, "is_sharpe": round(float(sr[best] * math.sqrt(252)), 3)})
        t0 += step
    if not parts:
        return pd.Series(dtype=float), pd.Series(dtype=float), log
    return pd.concat(parts), pd.concat(tparts), log


def block_bootstrap(r: pd.Series, n: int = 1000, block: int = 21, seed: int = 7) -> dict:
    x = r.dropna().values
    if len(x) < block * 3:
        return {"p_sharpe_pos": None, "cagr_p05": None, "maxdd_p05": None}
    rng = np.random.default_rng(seed)
    T = len(x)
    srs, cg, dd = [], [], []
    for _ in range(n):
        out = np.empty(T); i = 0
        while i < T:
            s = rng.integers(0, T - block)
            L = min(rng.geometric(1 / block), T - i)
            seg = x[s:s + L]
            out[i:i + len(seg)] = seg
            i += max(len(seg), 1)
        srs.append(out.mean() / out.std() * math.sqrt(252) if out.std() > 0 else 0)
        eq = np.cumprod(1 + out)
        cg.append(eq[-1] ** (252 / T) - 1 if eq[-1] > 0 else -1)
        dd.append((eq / np.maximum.accumulate(eq) - 1).min())
    return {"p_sharpe_pos": round(float(np.mean(np.array(srs) > 0)), 3),
            "cagr_p05": round(float(np.percentile(cg, 5)), 4),
            "maxdd_p05": round(float(np.percentile(dd, 5)), 4)}


def yearly_sharpe(r: pd.Series) -> dict:
    return {str(y): round(metrics.sharpe(g), 2) for y, g in r.groupby(r.index.year) if len(g) > 40}


def verdict(rep: dict) -> tuple[str, list[str]]:
    o, why = rep["oos"], []
    ok = True

    def check(cond, msg):
        nonlocal ok
        if not cond:
            ok = False
            why.append(msg)
    check(o["years"] >= GATE["min_oos_years"], f"OOS too short ({o['years']}y < {GATE['min_oos_years']}y)")
    check(rep["dsr"] >= GATE["min_dsr"], f"DSR {rep['dsr']} < {GATE['min_dsr']} (luck cannot be excluded after {rep['n_trials']} trials)")
    check(o["sharpe"] >= GATE["min_oos_sharpe"], f"OOS Sharpe {o['sharpe']} < {GATE['min_oos_sharpe']}")
    check(o["max_dd"] >= GATE["max_dd_floor"], f"OOS MaxDD {o['max_dd']} worse than {GATE['max_dd_floor']}")
    bs = rep["bootstrap"]["p_sharpe_pos"]
    check(bs is not None and bs >= GATE["min_p_sharpe_pos"], f"bootstrap P(SR>0) {bs} < {GATE['min_p_sharpe_pos']}")
    ys = list(rep["yearly_sharpe"].values())
    frac = (sum(v > 0 for v in ys) / len(ys)) if ys else 0
    check(frac >= GATE["min_pos_year_frac"], f"only {frac:.0%} of OOS years positive")
    check(rep["stress_2x_cost"]["sharpe"] > rep["benchmark"].get("sharpe", 0),
          "with 2x costs it does not beat the equal-weight benchmark")
    if rep["pbo"] is not None:
        check(rep["pbo"] <= GATE["max_pbo"], f"PBO {rep['pbo']} > {GATE['max_pbo']} (variant selection is overfit)")
    ts = rep.get("trade_stats") or {}
    if "n_trades" in ts:
        check(ts["n_trades"] >= GATE["min_trades"], f"only {ts['n_trades']} OOS trades (< {GATE['min_trades']})")
    if ok:
        return "ACCEPT", ["all gate checks passed"]
    soft = o["sharpe"] > 0 and rep["dsr"] >= 0.5 and o["years"] >= 1
    return ("WATCH" if soft else "REJECT"), why


def validate(spec: dict, p: Panel, costs: Costs, train_years: float = 3.0, test_months: int = 6) -> dict:
    cand = CD.from_spec(spec)
    vs = cand.variants()
    runs, errors = CD.run_all(cand, p, vs, costs)
    if not runs:
        raise RuntimeError(f"all variants failed: {list(errors.values())[:3]}")
    if isinstance(cand, CD.RuleCandidate) and cand.staged:
        R1, _ = _matrix(runs, p.index)
        top = R1.mean().div(R1.std().replace(0, np.nan)).sort_values(ascending=False).index[:cand.stage2_top]
        seeds = [v for v in vs if v.key in set(top)]
        vs2 = cand.variants(stage=2, seeds=seeds)
        r2, e2 = CD.run_all(cand, p, vs2, costs)
        runs.update(r2); errors.update(e2)
        vs = vs + vs2
    R, TO = _matrix(runs, p.index)
    n_trials = R.shape[1]
    trial_srs = [s for s in (R.mean() / R.std().replace(0, np.nan)).dropna()]

    oos, oos_to, wf_log = walk_forward(R, TO, train_years, test_months)
    bench_runs, _ = CD.run_all(CD.StrategyCandidate("equal_weight"), p,
                               CD.StrategyCandidate("equal_weight").variants(), costs, workers=1)
    bench = list(bench_runs.values())[0][0]
    b_oos = bench.reindex(oos.index).fillna(0) if len(oos) else bench
    stress = oos - oos_to * costs.per_turnover if len(oos) else oos

    final_key = wf_log[-1]["variant"] if wf_log else R.columns[0]
    final_v = next(v for v in vs if v.key == final_key)
    trades = runs[final_key][2]
    tstats = None
    if isinstance(trades, pd.DataFrame) and len(oos):
        tstats = trade_stats(trades[trades["exit"] >= oos.index[0]])
        yrs = len(oos) / 252
        tstats["trades_per_year"] = round(tstats["n_trades"] / yrs, 1) if yrs else None
    full_sweep = (pd.DataFrame({"variant": R.columns, "sharpe": (R.mean() / R.std().replace(0, np.nan) * math.sqrt(252)).values})
                  .sort_values("sharpe", ascending=False).head(15).round(3).to_dict("records"))
    has_oos = len(oos) > 30
    pbo_v = metrics.pbo(R.iloc[260:]) if n_trials > 1 else None
    rep = {
        "name": cand.name,
        "kind": "rule" if isinstance(cand, CD.RuleCandidate) else "strategy",
        "source": cand.source,
        "n_assets": int(p.c.shape[1]),
        "data_start": str(p.index[0].date()),
        "data_end": str(p.index[-1].date()),
        "costs": {"commission": costs.commission, "slippage": costs.slippage},
        "n_trials": n_trials,
        "failed_variants": len(errors),
        "full_sample_top": full_sweep,
        "oos": metrics.summary(oos, bench=b_oos) if has_oos else {"years": 0, "sharpe": 0, "max_dd": 0},
        "dsr": round(metrics.dsr(oos, n_trials, trial_srs), 3) if has_oos else 0.0,
        "pbo": round(pbo_v, 3) if pbo_v is not None else None,
        "benchmark": metrics.summary(b_oos) if len(b_oos) > 30 else {"sharpe": 0},
        "stress_2x_cost": {"sharpe": round(metrics.sharpe(stress), 3) if has_oos else 0.0},
        "bootstrap": block_bootstrap(oos),
        "yearly_sharpe": yearly_sharpe(oos) if has_oos else {},
        "regimes": metrics.regime_breakdown(oos, p.bench) if has_oos else {},
        "trade_stats": tstats,
        "walk_forward": wf_log,
        "final_variant": final_key,
        "final_params": final_v.params,
    }
    rep["verdict"], rep["reasons"] = verdict(rep)
    rep["targets"] = cand.targets(p, final_v)
    rep["_oos_returns"] = oos
    return rep
