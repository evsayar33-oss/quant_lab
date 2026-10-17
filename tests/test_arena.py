"""Offline tests for the arena (funnel, report card, perp sim, regimes, switcher). No network.
Run: python tests/test_arena.py   (also runs under pytest)
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from lab import data, metrics, perp, regime, rules, screen, switcher  # noqa: E402
from lab.engine import Costs  # noqa: E402
from lab.panel import Panel  # noqa: E402
from lab.trade_engine import EXIT_GRID, run_trades  # noqa: E402


def _panel(n=6, T=1800, seed=3):
    return Panel.from_close(data.synthetic_prices(n, T, seed=seed), seed=seed)


def test_per_asset_returns_are_exact():
    """Per-coin returns sum to the portfolio, and x N they equal a stand-alone single-coin run."""
    p = _panel()
    sig = rules.RULES["rsi_reversal"].fn(p, n=14, lo=30, exit=50)
    res = run_trades(p, sig, EXIT_GRID[28], Costs(0.0006, 0.0005, 0.0, 0.08), "both", None, per_asset=True)
    A = res.meta["asset_returns"]
    assert np.allclose(A.sum(axis=1).loc[res.returns.index].to_numpy(), res.returns.to_numpy(), atol=1e-12)
    R, _, _ = screen.run_variant(p, "rsi_reversal", {"n": 14, "lo": 30, "exit": 50}, 28, "both",
                                 Costs(0.0006, 0.0005, 0.0, 0.08))
    c = p.columns[2]
    R1, _, _ = screen.run_variant(screen.subpanel(p, [c]), "rsi_reversal", {"n": 14, "lo": 30, "exit": 50}, 28,
                                  "both", Costs(0.0006, 0.0005, 0.0, 0.08))
    assert np.allclose(R[c].fillna(0).to_numpy(), R1[c].fillna(0).to_numpy(), atol=1e-10)


def test_perp_liquidation_and_leverage():
    tr = pd.DataFrame({"entry": pd.to_datetime(["2020-01-01", "2020-02-01"]),
                       "exit": pd.to_datetime(["2020-01-05", "2020-02-05"]),
                       "ret": [0.05, -0.03], "mae": [-0.02, -0.12], "bars": [10, 10]})
    s1 = perp.simulate(tr, 2190, 0.0, 0.0, 1000, 0.1, 1)
    s10 = perp.simulate(tr, 2190, 0.0, 0.0, 1000, 0.1, 10)
    assert s1["liquidations"] == 0 and s10["liquidations"] == 1     # -12% wick liquidates 10x, not 1x
    assert s10["final"] < 1000 * (1 + 0.1 * 10 * 0.05)              # the liquidated margin is lost
    assert abs(s1["final"] - 1000 * (1 + 0.1 * 0.05) * (1 - 0.1 * 0.03)) < 0.01


def test_report_card_windows():
    p = _panel(1, 252 * 4)
    r = p.c.iloc[:, 0].pct_change(fill_method=None).fillna(0)
    metrics.set_periods(252)
    cd = perp.card(r, None, 252, [3, 5, 0], {"leverages": [1]}, 0.001, 0.0)
    assert cd["5y"].get("no_data") and not cd["3y"].get("no_data") and not cd["full"].get("no_data")


def test_regime_is_causal_and_sticky():
    p = _panel(4, 1500, seed=8)
    cfg = {"confirm_bars": 3, "vol_rank_days": 120}
    full = regime.classify(p, cfg)
    cut = 1100
    q = Panel(p.o.iloc[:cut], p.h.iloc[:cut], p.l.iloc[:cut], p.c.iloc[:cut], p.v.iloc[:cut])
    part = regime.classify(q, cfg)
    assert (full.iloc[:cut].to_numpy() == part.to_numpy()).all()       # no future data used
    raw = regime.raw_regime(p, cfg)
    flips = lambda x: int((x.diff().fillna(0) != 0).sum().sum())       # noqa: E731
    assert flips(full) < flips(raw)
    assert set(np.unique(full.to_numpy())) <= {-1, 0, 1, 2, 3}


def test_switcher_is_causal_and_learns_regimes():
    rng = np.random.default_rng(1)
    T = 3000
    idx = pd.date_range("2020-01-01", periods=T, freq="4h")
    g = pd.Series(np.where((np.arange(T) // 300) % 2 == 0, regime.TREND_UP, regime.RANGE), idx)
    R = pd.DataFrame({"good_trend": rng.normal(0, 0.01, T), "good_range": rng.normal(0, 0.01, T)}, idx)
    gp = g.shift(1)
    R.loc[gp == regime.TREND_UP, "good_trend"] += 0.004
    R.loc[gp == regime.RANGE, "good_range"] += 0.004
    G = pd.DataFrame({"good_trend": g, "good_range": g})
    X = pd.DataFrame(1.0, idx, R.columns)
    asset = {"good_trend": "A", "good_range": "B"}
    res = switcher.run(R, G, X, asset, 2190, 0.0, halflife_days=20, top_k=1, rebalance_days=0.0,
                       prior_days=2, min_regime_days=5, max_asset_weight=1.0)
    W = res["weights"]
    late = W.index[1500:]
    trend_bars = late[g.loc[late] == regime.TREND_UP]
    range_bars = late[g.loc[late] == regime.RANGE]
    assert W.loc[trend_bars, "good_trend"].mean() > 0.8
    assert W.loc[range_bars, "good_range"].mean() > 0.8
    R2 = R.copy()
    R2.iloc[2000:] = -R2.iloc[2000:]                                   # change the future only
    W2 = switcher.run(R2, G, X, asset, 2190, 0.0, halflife_days=20, top_k=1, rebalance_days=0.0,
                      prior_days=2, min_regime_days=5, max_asset_weight=1.0)["weights"]
    assert np.allclose(W.iloc[:2001].to_numpy(), W2.iloc[:2001].to_numpy())


def test_plateau_pick_prefers_region_over_spike():
    grid = {"a": [1, 2, 3, 4, 5]}
    nb = screen.neighbours(grid)
    assert nb[0] == [1] and sorted(nb[2]) == [1, 3]
    sr = {0: -0.1, 1: 0.2, 2: 0.25, 3: -0.6, 4: 0.9}   # lone spike at the edge, small plateau at 1-2
    stats = {gi: {"X": (v, v, 50)} for gi, v in sr.items()}
    gi, share = screen.plateau_pick(stats, nb, "X")
    assert gi == 1, gi                                   # not the spike (4), not the bad middle (3)
    assert share == 0.5


def test_funnel_on_noise_finds_no_tier_a():
    """Random walks have no edge: the funnel must not produce tier-A survivors."""
    p = _panel(5, 2600, seed=21)
    cfg = {"report_windows_years": [3, 5, 0], "exit_id": 28, "side": "both",
           "screen": {"rules": ["rsi_reversal", "donchian_breakout"], "min_years": 3.0},
           "account": {"leverages": [1, 5]}}
    res = screen.run(p, Costs(0.0006, 0.0005), cfg, workers=1)
    assert res["n_trials"] == (120 + 8) * 5
    assert not [r for r in res["rows"].values() if r.get("tier") == "A"]
    f = res["funnel"]
    assert f[-1]["remaining"] == sum(1 for r in res["rows"].values() if r["stage"] == "OK")
    assert f[0]["remaining"] + f[0]["eliminated"] == 5 * 2


def test_stage2_filters_exits_combos():
    """Stage 2 widens only S1-passers, counts its trials, and its rows carry filter/exit/combo specs."""
    p = _panel(4, 2600, seed=33)
    cfg = {"report_windows_years": [3, 0], "exit_id": 28, "side": "both",
           "screen": {"rules": ["donchian_breakout", "macd_cross", "rsi_reversal"], "min_years": 3.0,
                      "min_trades": 5},
           "stage2": {"enabled": True, "filters": ["none", "trend_sma200"], "exits": [28, 0],
                      "combos": {"enabled": True, "top_families": 3, "within": [0, 3]}},
           "account": {"leverages": [1]}}
    res = screen.run(p, Costs(0.0006, 0.0005), cfg, workers=1)
    s1 = sum(1 for r in res["rows"].values() if r["stage_no"] == 1 and r["stage"] not in ("S0", "S1"))
    assert res["stage2"]["candidates"] == s1
    base_trials = sum(len(rules.grid_points(rules.RULES[r].grid)) for r in cfg["screen"]["rules"]) * 4
    assert res["n_trials"] == base_trials + res["stage2"]["trials"]
    for r in res["rows"].values():
        if r["stage_no"] == 2:
            sp = r["spec"]
            assert sp["filter"] != "none" or sp["exit_id"] != 28 or sp.get("confirm")
    if s1:
        assert res["stage2"]["trials"] > 0


def test_protection_study_runs_and_is_causal():
    from lab import arena, protect
    rng = np.random.default_rng(4)
    idx = pd.date_range("2019-06-01", periods=2190 * 5, freq="4h")
    cols = ["BTC/USDT", "ETH/USDT", "SOL/USDT"]
    c = pd.DataFrame(100 * np.exp(np.cumsum(rng.normal(0, 0.01, (len(idx), 3)), axis=0)), idx, cols)
    p = Panel.from_close(c, seed=4)
    mem = [{"id": f"A{i}", "coin": co, "rule": "donchian_breakout", "params": {"entry": 20, "exit": 10},
            "exit_id": e, "side": "both", "status": "active"} for i, (co, e) in enumerate(
        [("BTC/USDT", 28), ("ETH/USDT", 0), ("SOL/USDT", 28), ("SOL/USDT", 23)])]
    R, X, _ = arena.compute({"members": mem}, p, Costs(0.0006, 0.0005), mem)
    cfg = {"universe": "syn", "timeframe": "4h", "protection": {
        "max_coin_weight": 0.4, "tests": {"dd_brake": [[0.1, 0.2]], "daily_limit": [0.05],
                                          "crash_guard": [0.1], "catastrophe_stop": [0.12]},
        "crises": {"c1": ["2020-03-01", "2020-04-01"], "c2": ["2022-05-01", "2022-07-01"]},
        "accept": {}, "monte_carlo": {"paths": 50}}}
    res = protect.run(p, Costs(0.0006, 0.0005), cfg, R, X, mem)
    assert set(res["tests"]) == {"dd_brake", "daily_limit", "crash_guard", "catastrophe_stop"}
    assert res["catastrophe_members"] == 2                      # exits 0 and 23 have no hard stop
    assert "max_leverage" in res["leverage"] and res["leverage"]["max_leverage"] < 5
    md = protect.markdown(res, cfg)
    assert "Kasa koruma" in md
    # brake decisions use only the past: changing the future does not change earlier scales
    base = res["series"]["base"]
    s1 = protect.dd_brake_scale(base, 0.1, 0.2)
    b2 = base.copy(); b2.iloc[5000:] = -0.05
    s2 = protect.dd_brake_scale(b2, 0.1, 0.2)
    assert (s1.iloc[:5001] == s2.iloc[:5001]).all()


def test_drop_open_bar():
    now = pd.Timestamp.now(tz="UTC").tz_localize(None).floor("4h")
    idx = pd.date_range(end=now, periods=5, freq="4h")
    df = pd.DataFrame({"Close": range(5)}, index=idx)
    out = data._drop_open_bar(df, "4h")
    assert out.index[-1] == idx[-2]                      # the bar that opened at `now` is still forming


if __name__ == "__main__":
    for k, fn in list(globals().items()):
        if k.startswith("test_"):
            fn()
            print("ok", k)
