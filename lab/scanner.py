"""Discovery scan: try EVERYTHING on a universe, then rank honestly.

  * every entry/exit rule x every parameter variant x chosen filters (signal exit)
  * every weight strategy (price factors, fundamental factors, calendar) x its grid
Each family (one rule or one strategy) gets its own walk-forward OOS record.
Full-sample Deflated Sharpe uses the TOTAL number of trials in the scan, so a lucky
variant among thousands cannot look significant. A global PBO measures how much the
"pick the best backtest" step itself is overfit.

The scan never writes decisions. It proposes hypotheses (YAML snippet) for the families
that look best out of sample; those must then pass the full gate in run.py.
"""
from __future__ import annotations

import math
import time

import numpy as np
import pandas as pd

from lab import candidates as CD
from lab import metrics, rules
from lab.engine import Costs
from lab.panel import Panel
from lab.strategies import REGISTRY
from lab.strategies.fundamental_factors import NoData
from lab.validation import _matrix, walk_forward


def scan(p: Panel, costs: Costs, families: str = "all", filters=("none",), side: str = "long",
         rule_names: list[str] | None = None) -> dict:
    t0 = time.time()
    metrics.set_periods(p.ppy)
    all_runs, fam_of, errors = {}, {}, {}
    todo = []
    if families in ("all", "rules"):
        for name in (rule_names or list(rules.RULES)):
            todo.append(CD.RuleCandidate(name, filters, None, side, staged=False))
    if families in ("all", "strategies", "factors"):
        for name, s in REGISTRY.items():
            if name == "equal_weight":
                continue
            if families == "factors" and s.kind != "fundamental":
                continue
            if s.kind == "fundamental" and not p.fund:
                continue
            todo.append(CD.StrategyCandidate(name))
    for cand in todo:
        vs = cand.variants()
        runs, err = CD.run_all(cand, p, vs, costs)
        for k in runs:
            fam_of[k] = cand.name
        all_runs.update(runs)
        if err:
            msg = list(err.values())[0]
            errors[cand.name] = msg if not isinstance(msg, NoData) else "no fundamental data"
        print(f"[scan] {cand.name:24s} {len(runs):4d} variants ({len(err)} failed)  t={time.time() - t0:.0f}s")

    R, TO = _matrix(all_runs, p.index)
    K = R.shape[1]
    sr_d = R.mean() / R.std().replace(0, np.nan)
    trial_srs = list(sr_d.dropna())

    rows = []
    for fam in sorted(set(fam_of.values())):
        cols = [k for k, f in fam_of.items() if f == fam]
        if sr_d[cols].notna().sum() == 0:
            errors[fam] = "no trades / flat returns in every variant"
            continue
        oos, oos_to, log = walk_forward(R[cols], TO[cols])
        best = sr_d[cols].idxmax()
        rows.append({
            "family": fam,
            "variants": len(cols),
            "best_variant": best,
            "best_full_sharpe": round(float(sr_d[best] * math.sqrt(p.ppy)), 3),
            "best_full_dsr": round(metrics.dsr(R[best].iloc[int(p.ppy):], K, trial_srs), 3),
            "wf_oos_sharpe": round(metrics.sharpe(oos), 3) if len(oos) > 60 else None,
            "wf_oos_cagr": round(metrics.cagr(oos), 4) if len(oos) > 60 else None,
            "wf_oos_maxdd": round(metrics.max_drawdown(oos), 4) if len(oos) > 60 else None,
            "wf_oos_2x_cost_sharpe": round(metrics.sharpe(oos - oos_to * costs.per_turnover), 3) if len(oos) > 60 else None,
            "family_pbo": round(v, 3) if (v := metrics.pbo(R[cols].iloc[int(p.ppy):])) is not None else None,
        })
    board = pd.DataFrame(rows).sort_values("wf_oos_sharpe", ascending=False, na_position="last")
    bench = CD.run_all(CD.StrategyCandidate("equal_weight"), p,
                       CD.StrategyCandidate("equal_weight").variants(), costs, workers=1)[0]
    b = list(bench.values())[0][0]
    return {
        "universe": p.name,
        "n_trials": K,
        "global_pbo": round(g, 3) if (g := metrics.pbo(R.iloc[int(p.ppy):])) is not None else None,
        "benchmark_sharpe": round(metrics.sharpe(b.iloc[int(p.ppy):]), 3),
        "reality_check_p": metrics.reality_check(R.iloc[int(p.ppy):], b, n=300),
        "timeframe": p.freq,
        "board": board,
        "errors": errors,
        "seconds": round(time.time() - t0),
    }


def to_markdown(res: dict, top: int = 25) -> str:
    b = res["board"].head(top)
    lines = [f"# Scan — {res['universe']}",
             "",
             f"- Variants tried: **{res['n_trials']}** · global PBO: **{res['global_pbo']}** · "
             f"equal-weight benchmark Sharpe: {res['benchmark_sharpe']} · runtime {res['seconds']}s",
             "- Ranked by walk-forward OOS Sharpe per family. Full-sample DSR is deflated by ALL trials.",
             "- A scan result is a LEAD, not a decision. Register a hypothesis and run the gate.",
             "",
             "| # | family | variants | WF OOS Sharpe | OOS CAGR | OOS MaxDD | 2x-cost Sharpe | family PBO | best full Sharpe | DSR(all trials) |",
             "|---|---|---|---|---|---|---|---|---|---|"]
    for i, r in enumerate(b.itertuples(), 1):
        lines.append(f"| {i} | {r.family} | {r.variants} | {r.wf_oos_sharpe} | {r.wf_oos_cagr} | {r.wf_oos_maxdd} | "
                     f"{r.wf_oos_2x_cost_sharpe} | {r.family_pbo} | {r.best_full_sharpe} | {r.best_full_dsr} |")
    if res["errors"]:
        lines += ["", "## Skipped / failed families", *[f"- {k}: {v}" for k, v in res["errors"].items()]]
    return "\n".join(lines)


def suggest_yaml(res: dict, universe: str, n: int = 5, start_id: int = 900) -> str:
    out = ["# Suggested hypotheses from the scan (copy into hypotheses/registry.yaml, give real ids)"]
    good = res["board"][(res["board"]["wf_oos_sharpe"].fillna(-9) > res["benchmark_sharpe"])].head(n)
    for i, r in enumerate(good.itertuples()):
        key = "rule" if r.family in rules.RULES else "strategy"
        out += [f"- id: S{start_id + i}", f"  {key}: {r.family}", f"  universe: {universe}",
                "  for_system: TODO", "  status: active",
                *(['  filters: [none, trend_sma200, regime_bench200]', '  side: long'] if key == "rule" else []),
                f"  note: \"scan lead: WF OOS Sharpe {r.wf_oos_sharpe}, family PBO {r.family_pbo}\""]
    return "\n".join(out)
