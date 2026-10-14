"""Offline tests: no network. Run with `python -m pytest -q` or `python tests/test_core.py`."""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from lab import data, engine, metrics, validation  # noqa: E402
from lab.engine import Costs  # noqa: E402
from lab.strategies import REGISTRY  # noqa: E402


def test_no_lookahead():
    """A signal built from day-t's close must not earn day-t's return: the engine lags weights."""
    px = data.synthetic_prices(5, 800, seed=1)
    today = px.pct_change(fill_method=None)  # known only at close t
    w = engine.rank_top_n(today, 1)
    cheat = engine.run(px, w, Costs(0, 0)).returns
    # Weight from close t is held on t+1 -> earns the t+1 return, which is noise.
    assert abs(metrics.sharpe(cheat)) < 1.5, metrics.sharpe(cheat)
    # Sanity: without the lag the cheat would be huge.
    nolag = engine.run(px, w, Costs(0, 0), lag=0).returns
    assert metrics.sharpe(nolag) > 5


def test_costs_reduce_returns():
    px = data.synthetic_prices(5, 600, seed=2)
    w = REGISTRY["st_reversal"](px)
    a = engine.run(px, w, Costs(0, 0)).returns.sum()
    b = engine.run(px, w, Costs(0.002, 0.002)).returns.sum()
    assert b < a


def test_all_strategies_run_and_are_bounded():
    px = data.synthetic_prices(8, 700, seed=3)
    for name, s in REGISTRY.items():
        w = s(px)
        assert w.shape == px.shape, name
        assert np.isfinite(w.values).all(), name
        assert (w.abs().sum(axis=1) <= 2.0 + 1e-9).all(), name


def test_random_walk_is_not_accepted():
    """On pure noise the gate must not say ACCEPT (protects against false discoveries)."""
    px = data.synthetic_prices(10, 2200, seed=4)
    rep = validation.validate("xs_momentum", px, Costs())
    assert rep["verdict"] != "ACCEPT", rep["reasons"]


def test_planted_edge_is_found():
    """Plant a real momentum edge; the pipeline must see positive OOS Sharpe."""
    rng = np.random.default_rng(5)
    n, T = 10, 2400
    drift = rng.normal(0, 0.0012, n)
    rets = np.zeros((T, n))
    for t in range(T):
        if t % 250 == 0:
            drift = 0.7 * drift + rng.normal(0, 0.0008, n)  # persistent trends -> momentum works
        rets[t] = drift + rng.normal(0, 0.012, n)
    px = pd.DataFrame(100 * np.exp(np.cumsum(rets, 0)), index=pd.bdate_range("2012-01-01", periods=T),
                      columns=[f"S{i}" for i in range(n)])
    rep = validation.validate("xs_momentum", px, Costs(0.0005, 0.0005))
    assert rep["oos"]["sharpe"] > 0.3, rep["oos"]


def test_dsr_penalises_trials():
    r = pd.Series(np.random.default_rng(6).normal(0.0005, 0.01, 1500))
    assert metrics.dsr(r, 1) > metrics.dsr(r, 200)


if __name__ == "__main__":
    for k, f in list(globals().items()):
        if k.startswith("test_"):
            f()
            print("ok", k)
