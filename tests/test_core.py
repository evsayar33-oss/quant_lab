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
from lab.engine import rank_top_n  # noqa: E402,F401
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


def test_resample_and_ppy():
    p = Panel.from_close(data.synthetic_prices(3, 1300, seed=12))
    d = {c: pd.DataFrame({"Open": p.o[c], "High": p.h[c], "Low": p.l[c], "Close": p.c[c], "Volume": p.v[c]}) for c in p.columns}
    w = {k: data.resample(v, "1w") for k, v in d.items()}
    pw = Panel.from_ohlcv(w)
    assert 50 < pw.ppy < 54 and 250 < p.ppy < 265
    k = pw.index[10]
    assert abs(pw.c.iloc[10, 0] - p.c.loc[:k].iloc[-1, 0]) < 1e-9          # weekly close = last daily close
    assert abs(pw.h.iloc[10, 0] - p.h.loc[pw.index[9]:k].iloc[1:, 0].max()) < 1e-9


def test_htf_filter_is_causal_intraday():
    idx = pd.date_range("2024-01-01", periods=24 * 60, freq="h")   # 2024-01-01 is a Monday
    px = np.linspace(100, 200, len(idx))
    crash = idx >= pd.Timestamp("2024-02-09 00:00")                  # Friday of week 6
    px[crash] = px[crash] * 0.5
    p = Panel.from_close(pd.DataFrame({"A": px}, index=idx))
    al = rules._htf_trend(p, "W-FRI", 2)["A"]
    assert al.loc["2024-02-08 12:00"] == 1 and al.loc["2024-02-09 12:00"] == 1   # Friday cannot see Friday's close
    assert al.loc["2024-02-10 12:00"] == 0                                         # known from the next day


def test_partial_take_profit_and_breakeven():
    idx = pd.bdate_range("2021-01-01", periods=30)
    c = pd.DataFrame({"X": [100.0] * 30}, index=idx)
    o, h, l = c.copy(), c + 0.5, c - 0.5
    c.iloc[11:] = 110; o.iloc[11:] = 110; h.iloc[11] = 112; l.iloc[11:] = 109.5; h.iloc[12:] = 110.5
    l.iloc[14] = 99   # falls back: remaining half must exit at breakeven (entry price)
    p = Panel(o, h, l, c, c * 0 + 1e6, c["X"], {}, "toy")
    e = pd.DataFrame(False, index=idx, columns=["X"]); e.iloc[9] = True
    from lab.trade_engine import ExitCfg as EC
    res = run_trades(p, Signals(e, e & False), EC(stop_pct=0.05, partial_r=1.0), Costs(0, 0))
    t = res.meta["trades"]
    assert len(t) == 1 and t["reason"].iloc[0] == "breakeven"
    # bar 11 gaps above the +1R level (105) and opens at 110: half fills at the open (+10%),
    # the other half exits at breakeven -> +5% total
    assert abs(t["ret"].iloc[0] - 0.05) < 1e-9, t


def test_price_limit_blocks_entry():
    idx = pd.bdate_range("2021-01-01", periods=10)
    c = pd.DataFrame({"X": [100, 100, 100, 110, 121, 121, 121, 121, 121, 121.0]}, index=idx)
    o = c.copy()
    p = Panel(o, c * 1.0, c * 1.0, c, c * 0 + 1e9, c["X"], {}, "toy", costs_meta={"price_limit": 0.10})
    e = pd.DataFrame(False, index=idx, columns=["X"]); e.iloc[2] = True; e.iloc[3] = True
    t = run_trades(p, Signals(e, e & False), ExitCfg(max_hold=2), Costs(0, 0)).meta["trades"]
    assert t["entry"].iloc[0] == idx[5]   # opens at 110 and 121 are limit-up locked -> first fill on bar 5


def test_pairs_find_cointegration():
    rng = np.random.default_rng(13)
    T = 1500
    base = np.cumsum(rng.normal(0, 0.01, T))
    spread = np.zeros(T)
    for t in range(1, T):
        spread[t] = 0.9 * spread[t - 1] + rng.normal(0, 0.01)
    c = pd.DataFrame({"A": 100 * np.exp(base + spread), "B": 100 * np.exp(base),
                      "C": 100 * np.exp(np.cumsum(rng.normal(0, 0.01, T)))},
                     index=pd.bdate_range("2015-01-01", periods=T))
    w = REGISTRY["pairs_zscore"](c, form=126, entry_z=2.0, min_corr=0.3)
    r = engine.run(c, w, Costs(0.0005, 0.0005)).returns
    assert (w.abs().sum(axis=1) > 0).mean() > 0.05 and metrics.sharpe(r) > 1.0, metrics.sharpe(r)


def test_membership_mask_blocks_weights():
    px = data.synthetic_prices(4, 300, seed=14)
    mem = pd.DataFrame(True, index=px.index, columns=px.columns); mem.iloc[:150, 0] = False
    w = pd.DataFrame(0.25, index=px.index, columns=px.columns)
    res = engine.run(px, w, Costs(0, 0), member=mem)
    assert (res.weights.iloc[:150, 0] == 0).all() and (res.weights.iloc[200:, 0] > 0).all()


def test_usd_conversion():
    idx = pd.bdate_range("2020-01-01", periods=3)
    r = pd.Series([0.0, 0.10, 0.0], index=idx)
    fx = pd.Series([10.0, 11.0, 11.0], index=idx)  # lira loses 10% the same day
    u = validation.to_usd(r, fx)
    assert abs(u.iloc[1] - (1.10 * 10 / 11 - 1)) < 1e-12


def test_exit_grid_and_event_study():
    from lab import robustness as RB
    p = Panel.from_close(data.synthetic_prices(5, 800, seed=15))
    e = rules.RULES["rsi_reversal"].fn(p, n=14, lo=30, exit=60).entry_long
    es = RB.event_study(p, e)
    eg = RB.exit_grid_study(p, e)
    assert "best_holding_bars" in es and len(eg["top"]) > 0


def test_decision_merge_and_client(tmp_path=None):
    import json
    import tempfile
    from lab import client, decision
    d = Path(tempfile.mkdtemp())
    old = (decision.PARTS, decision.REG, decision.LIVE_STATUS, decision.ROOT)
    decision.PARTS, decision.REG, decision.LIVE_STATUS, decision.ROOT = d / "parts", d / "registry.json", d / "live.json", d
    try:
        decision.PARTS.mkdir()
        idx = pd.bdate_range("2020-01-01", periods=300)
        rng = np.random.default_rng(16)
        now = pd.Timestamp.now(tz="UTC").isoformat()
        for hid in ("H1", "H2", "H3"):
            pd.Series(rng.normal(0.0005, 0.01, 300), index=idx).to_csv(d / f"{hid}.csv")
            (decision.PARTS / f"{hid}.json").write_text(json.dumps({
                "verdict": "ACCEPT" if hid != "H3" else "WATCH", "for_system": "botA", "reasons": [],
                "oos_csv": f"{hid}.csv", "validated_at": now, "targets": {"X": 1}}))
        decision.LIVE_STATUS.write_text(json.dumps({"H2": {"degraded": True, "why": "test"}}))
        reg = decision.merge()
        assert reg["hypotheses"]["H2"]["verdict"] == "DEGRADED"
        assert reg["systems"]["botA"]["approved"] == ["H1"]
        url = (d / "registry.json").as_uri()
        assert [h["id"] for h in client.approved("botA", url)] == ["H1"]
        assert client.allocation("botA", url) == {"H1": 1.0}
    finally:
        decision.PARTS, decision.REG, decision.LIVE_STATUS, decision.ROOT = old


def test_live_decay_check():
    from lab import live
    r = pd.Series(np.r_[np.full(60, -0.01)], index=pd.bdate_range("2024-01-01", periods=60))
    bad, why = live.decay_check(r, {"oos": {"max_dd": -0.10, "sharpe": 1.0}})
    assert bad, why


def test_confirmation_combo():
    p = Panel.from_close(data.synthetic_prices(5, 700, seed=17))
    a = rules.RULES["rsi_reversal"].fn(p, n=14, lo=30, exit=60)
    b = rules.RULES["macd_cross"].fn(p, cfg=(12, 26, 9), zero_filter=False)
    c0 = rules.confirm(a, b, 0)
    c5 = rules.confirm(a, b, 5)
    assert (c0.entry_long <= a.entry_long).all().all() and (c0.entry_long <= b.entry_long).all().all()
    assert c5.entry_long.sum().sum() >= c0.entry_long.sum().sum()
    from lab import candidates as CD
    cand = CD.from_spec({"rule": "rsi_reversal", "confirm": "macd_cross"})
    assert cand.name == "rsi_reversal+macd_cross" and len(cand.variants()) <= 1500


def test_overlays_are_causal_and_derisk():
    from lab import overlays
    rng = np.random.default_rng(18)
    idx = pd.bdate_range("2015-01-01", periods=1500)
    r = pd.Series(rng.normal(0.0004, 0.02, 1500), index=idx)
    r.iloc[700:760] = -0.03  # crash
    for k in overlays.KINDS:
        sc = overlays.scale_series(r, k, 252)
        assert sc.max() <= 1.0 + 1e-12 and sc.min() >= 0
        r2 = r.copy(); r2.iloc[1000] = 5.0   # a future shock must not change earlier scales
        assert (overlays.scale_series(r2, k, 252).iloc[:1001] == sc.iloc[:1001]).all(), k
    dd = overlays.scale_series(r, "dd20", 252)
    assert dd.iloc[740:760].min() == 0.5


if __name__ == "__main__":
    for k, fn in list(globals().items()):
        if k.startswith("test_"):
            fn()
            print("ok", k)
