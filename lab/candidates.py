"""Candidate = a family of tradeable variants the validator can sweep.

Two kinds:
  * StrategyCandidate : weight-based strategy from lab.strategies (factor / rotation / timing)
  * RuleCandidate     : entry/exit rule from lab.rules + filters + exit configs, run through
                        the trade engine (stops, targets, trailing, time exits)

Every variant is computed ONCE on the full history. All computations are causal, so slicing
a full-history return series is identical to re-running on truncated data; the walk-forward
therefore selects among precomputed series (fast and exact).
"""
from __future__ import annotations

import os
from concurrent.futures import ProcessPoolExecutor
from dataclasses import dataclass

import pandas as pd

from lab import engine, rules
from lab.engine import Costs, Result
from lab.panel import Panel
from lab.strategies import get as get_strategy
from lab.trade_engine import EXIT_GRID, ExitCfg, run_trades

_G: dict = {}  # worker globals (fork start method shares the panel without pickling)


@dataclass
class Variant:
    key: str
    params: dict


class StrategyCandidate:
    def __init__(self, name: str):
        self.strat = get_strategy(name)
        self.name = name
        self.source = self.strat.source

    def variants(self) -> list[Variant]:
        pts = rules.grid_points(self.strat.grid)
        return [Variant(f"{self.name}|{_fmt(p)}", p) for p in pts]

    def run(self, p: Panel, v: Variant, costs: Costs) -> Result:
        return engine.run(p.c, self.strat(p, **v.params), costs)

    def targets(self, p: Panel, v: Variant) -> dict:
        w = self.strat(p, **v.params).iloc[-1]
        return {k: round(float(x), 4) for k, x in w[w.abs() > 1e-6].sort_values(ascending=False).items()}


class RuleCandidate:
    """rule x rule-grid x filters x exits. `staged=True` sweeps exits only on the best stage-1 variants."""

    def __init__(self, rule: str, filters=("none",), exits=None, side: str = "long",
                 max_positions: int | None = None, staged: bool = True, stage2_top: int = 3):
        self.rule = rules.RULES[rule]
        self.name = rule
        self.source = self.rule.source
        self.filters = list(filters)
        self.exits = list(exits) if exits is not None else None
        self.side = side
        self.max_positions = max_positions
        self.staged = staged
        self.stage2_top = stage2_top

    def variants(self, stage: int = 1, seeds: list[Variant] | None = None) -> list[Variant]:
        out = []
        if stage == 1:
            ex_list = (self.exits or [0])[:1] if self.staged else (self.exits or [0])
            for gp in rules.grid_points(self.rule.grid):
                for f in self.filters:
                    for e in ex_list:
                        out.append(Variant(f"{self.name}|{_fmt(gp)}|f={f}|x={EXIT_GRID[e].label()}",
                                           {**gp, "_filter": f, "_exit": e}))
        else:
            ex_list = self.exits if self.exits is not None else list(range(len(EXIT_GRID)))
            for s in seeds or []:
                for e in ex_list:
                    if e == s.params["_exit"]:
                        continue
                    p = {**s.params, "_exit": e}
                    gp = {k: v for k, v in p.items() if not k.startswith("_")}
                    out.append(Variant(f"{self.name}|{_fmt(gp)}|f={p['_filter']}|x={EXIT_GRID[e].label()}", p))
        return out

    def _signals(self, p: Panel, v: Variant):
        gp = {k: x for k, x in v.params.items() if not k.startswith("_")}
        return rules.apply_filter(self.rule.fn(p, **gp), p, v.params["_filter"])

    def run(self, p: Panel, v: Variant, costs: Costs) -> Result:
        return run_trades(p, self._signals(p, v), EXIT_GRID[v.params["_exit"]], costs,
                          self.side, self.max_positions)

    def targets(self, p: Panel, v: Variant) -> dict:
        res = self.run(p, v, Costs())
        w = res.weights.iloc[-1]
        s = self._signals(p, v)
        last = p.index[-1]
        return {
            "positions": {k: round(float(x), 4) for k, x in w[w.abs() > 1e-6].items()},
            "entry_long_next_open": [c for c in p.columns if bool(s.entry_long.loc[last, c])],
            "exit_long_next_open": [c for c in p.columns if bool(s.exit_long.loc[last, c])],
            "entry_short_next_open": [] if s.entry_short is None or self.side == "long"
            else [c for c in p.columns if bool(s.entry_short.loc[last, c])],
        }


def _fmt(d: dict) -> str:
    return ",".join(f"{k}={v}" for k, v in d.items() if not str(k).startswith("_"))


def _work(args):
    cand, v, costs = args
    p = _G["panel"]
    try:
        r = cand.run(p, v, costs)
        return v.key, r.returns, r.turnover, r.meta.get("trades")
    except Exception as e:  # noqa: BLE001
        return v.key, None, None, str(e)


def run_all(cand, p: Panel, variants: list[Variant], costs: Costs, workers: int | None = None):
    """Run variants (in parallel where possible). Returns {key: (returns, turnover, trades)}."""
    workers = workers or int(os.environ.get("LAB_WORKERS", os.cpu_count() or 1))
    _G["panel"] = p
    jobs = [(cand, v, costs) for v in variants]
    out, errors = {}, {}
    if workers > 1 and len(jobs) > 4:
        import multiprocessing as mp
        try:
            ctx = mp.get_context("fork")
            with ProcessPoolExecutor(workers, mp_context=ctx) as ex:
                res = list(ex.map(_work, jobs, chunksize=max(1, len(jobs) // (workers * 4))))
        except Exception:  # noqa: BLE001 - fall back to serial
            res = [_work(j) for j in jobs]
    else:
        res = [_work(j) for j in jobs]
    for key, r, t, tr in res:
        if r is None:
            errors[key] = tr
        else:
            out[key] = (r, t, tr)
    return out, errors


def from_spec(spec: dict):
    """Build a candidate from a hypotheses/registry.yaml entry."""
    if "rule" in spec:
        filters = spec.get("filters", ["none"])
        if filters == "all":
            filters = list(rules.FILTERS)
        exits = spec.get("exits")
        if exits == "all":
            exits = list(range(len(EXIT_GRID)))
        return RuleCandidate(spec["rule"], filters, exits, spec.get("side", "long"),
                             spec.get("max_positions"), spec.get("staged", True))
    return StrategyCandidate(spec["strategy"])


__all__ = ["StrategyCandidate", "RuleCandidate", "Variant", "run_all", "from_spec", "ExitCfg"]
