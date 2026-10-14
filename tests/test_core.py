"""Offline tests: no network. Run with `python tests/test_core.py` (also runs under pytest).

They prove the properties the decision gate relies on:
no look-ahead, correct fills/stops, costs hurt, noise is rejected, a real edge is found,
DSR/PBO penalise data mining, fundamentals respect publication dates.
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from lab import data, engine, fundamentals, metrics, rules, validation  # noqa: E402
from lab.engine import Costs  # noqa: E402
from lab.panel import Panel  # noqa: E402
from lab.rules import Signals  # noqa: E402
from lab.strategies import REGISTRY  # noqa: E402
from lab.strategies.fundamental_factors import derive  # noqa: E402
from lab.trade_engine import ExitCfg, run_trades  # noqa: E402


def test_no_lookahead_weights():
    """A signal built from day-t's close must not earn day-t's return: the engine lags weights."""
    px = data.synthetic_prices(5, 800, seed=1)
    w = engine.rank_top_n(px.pct_change(fill_method=None), 1)
    assert abs(metrics.sharpe(engine.run(px, w, Costs(0, 0)).returns)) < 1.5
    assert metrics.sharpe(engine.run(px, w, Costs(0, 0), lag=0).returns) > 5  # sanity: cheating works


def test_no_lookahead_trades():
    """Entering on today's up-close must not capture today's move (fills at next open)."""
    p = Panel.from_close(data.synthetic_prices(6, 900, seed=2), seed=2)
    up = p.c.pct_change(fill_method=None) > 0
    sig = Signals(up, ~up)
    r = run_trades(p, sig, ExitCfg(max_hold=1), Costs(0, 0)).returns
    assert abs(metrics.sharpe(r)) < 1.5, metrics.sharpe(r)


def _toy():
    idx = pd.bdate_range("2020-01-01", periods=40)
    c = pd.DataFrame({"X": np.linspace(100, 139, 40)}, index=idx)
    o = c.shift(1).fillna(100) + 0.5
    h, l, v = c + 1, c - 1, c * 0 + 1e6
    l.iloc[25] = 50          # crash bar to trigger a stop
    return Panel(o, np.maximum(h, o), np.minimum(l, o), c, v, c["X"], {}, "toy")


def test_entry_next_open_and_stop_fill():
    p = _toy()
    e = pd.DataFrame(False, index=p.index, columns=p.columns); e.iloc[20] = True
    x = pd.DataFrame(False, index=p.index, columns=p.columns)
    res = run_trades(p, Signals(e, x), ExitCfg(stop_pct=0.05), Costs(0, 0))
    t = res.meta["trades"]
    assert len(t) == 1
    assert t["entry"].iloc[0] == p.index[21]                       # next open
    assert abs(t["entry_px"].iloc[0] - p.o.iloc[21, 0]) < 1e-9
    assert t["reason"].iloc[0] == "stop" and t["exit"].iloc[0] == p.index[25]
    assert abs(t["exit_px"].iloc[0] - p.o.iloc[21, 0] * 0.95) < 1e-9  # filled at the stop price


def test_costs_reduce_returns():
    px = data.synthetic_prices(5, 600, seed=3)
    w = REGISTRY["st_reversal"](px)
    assert engine.run(px, w, Costs(0.002, 0.002)).returns.sum() < engine.run(px, w, Costs(0, 0)).returns.sum()


def test_all_weight_strategies_bounded():
    p = Panel.from_close(data.synthetic_prices(8, 700, seed=4))
    for name, s in REGISTRY.items():
        if s.kind == "fundamental":
            continue
        w = s(p)
        assert w.shape == p.c.shape, name
        assert np.isfinite(w.values).all(), name
        assert (w.abs().sum(axis=1) <= 2.0 + 1e-9).all(), name


def test_all_rules_run():
    p = Panel.from_close(data.synthetic_prices(5, 500, seed=5))
    for name, r in rules.RULES.items():
        for f in ("none", "trend_sma200", "regime_bench200"):
            s = rules.apply_filter(r.fn(p, **rules.grid_points(r.grid)[0]), p, f)
            res = run_trades(p, s, ExitCfg(stop_atr=2.0, trail_atr=3.0, max_hold=20), Costs(), "both")
            assert np.isfinite(res.returns.values).all(), name
            assert (res.weights.abs().sum(axis=1) <= 1 + 1e-9).all(), name


def test_random_walk_is_not_accepted():
    p = Panel.from_close(data.synthetic_prices(10, 2200, seed=6))
    rep = validation.validate({"strategy": "xs_momentum"}, p, Costs())
    assert rep["verdict"] != "ACCEPT", rep["reasons"]


def test_planted_edge_is_found():
    rng = np.random.default_rng(7)
    n, T = 10, 2400
    drift = rng.normal(0, 0.0012, n)
    rets = np.zeros((T, n))
    for t in range(T):
        if t % 250 == 0:
            drift = 0.7 * drift + rng.normal(0, 0.0008, n)
        rets[t] = drift + rng.normal(0, 0.012, n)
    px = pd.DataFrame(100 * np.exp(np.cumsum(rets, 0)), index=pd.bdate_range("2012-01-01", periods=T),
                      columns=[f"S{i}" for i in range(n)])
    rep = validation.validate({"strategy": "xs_momentum"}, Panel.from_close(px), Costs(0.0005, 0.0005))
    assert rep["oos"]["sharpe"] > 0.3, rep["oos"]


def test_dsr_penalises_trials():
    r = pd.Series(np.random.default_rng(8).normal(0.0005, 0.01, 1500))
    assert metrics.dsr(r, 1) > metrics.dsr(r, 200)


def test_pbo_noise_vs_edge():
    rng = np.random.default_rng(9)
    noise = pd.DataFrame(rng.normal(0, 0.01, (2000, 30)))
    assert 0.2 < metrics.pbo(noise) < 0.9
    edge = noise.copy(); edge[0] += 0.003
    assert metrics.pbo(edge) < 0.1


def test_fundamentals_point_in_time():
    idx = pd.bdate_range("2020-01-01", periods=300)
    long = pd.DataFrame([("A", "net_income", 10.0, pd.Timestamp("2020-03-16"), pd.Timestamp("2019-12-31")),
                         ("A", "net_income", 20.0, pd.Timestamp("2020-06-15"), pd.Timestamp("2020-03-31"))],
                        columns=["ticker", "field", "value", "avail", "period_end"])
    f = fundamentals.to_panels(long, idx, ["A"])["net_income"]["A"]
    assert np.isnan(f.loc["2020-03-13"]) and f.loc["2020-03-16"] == 10 and f.loc["2020-06-12"] == 10
    assert f.loc["2020-06-15"] == 20


def test_fundamental_strategies_run():
    p = Panel.from_close(data.synthetic_prices(12, 700, seed=10))
    rng = np.random.default_rng(10)
    mk = lambda lo, hi: pd.DataFrame(rng.uniform(lo, hi, p.c.shape), index=p.index, columns=p.columns).rolling(63).mean()  # noqa: E731
    p.fund = {k: mk(*v) for k, v in {"net_income": (1, 10), "equity": (50, 100), "revenue": (50, 200),
                                     "op_profit": (2, 20), "gross_profit": (10, 60), "cfo": (1, 12),
                                     "total_assets": (100, 300), "fin_debt": (10, 80), "shares": (1, 2),
                                     "cur_assets": (20, 60), "cur_liab": (10, 50)}.items()}
    for k in list(p.fund):
        p.fund[k + "_1y"] = p.fund[k].shift(252)
    derive(p)
    for name, s in REGISTRY.items():
        if s.kind == "fundamental":
            w = s(p)
            assert (w.abs().sum(axis=1) <= 1 + 1e-9).all(), name
            assert w.iloc[-1].abs().sum() > 0, name


if __name__ == "__main__":
    for k, fn in list(globals().items()):
        if k.startswith("test_"):
            fn()
            print("ok", k)
