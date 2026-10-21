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
    from lab.strategies.fundamental_factors import NoData
    p = Panel.from_close(data.synthetic_prices(8, 700, seed=4))
    for name, s in REGISTRY.items():
        if s.kind == "fundamental":
            continue
        try:
            w = s(p)
        except NoData:      # needs macro / COT data the synthetic panel does not have
            continue
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


def test_metal_strategies_run():
    c = data.synthetic_prices(5, 1500, seed=19)
    c.columns = ["GLD", "SLV", "CPER", "GDX", "SIL"]
    p = Panel.from_close(c)
    rng = np.random.default_rng(19)
    walk = lambda: pd.Series(100 * np.exp(np.cumsum(rng.normal(0, 0.01, len(c)))), index=c.index)  # noqa: E731
    p.macro = {k: walk() for k in ("DX-Y.NYB", "TIP", "IEF", "GC=F", "SI=F", "HG=F")}
    p.extra = {"cot_spec_net": pd.DataFrame(rng.normal(0, 0.1, c.shape), index=c.index, columns=c.columns).rolling(20).mean(),
               "cot_comm_net": pd.DataFrame(rng.normal(0, 0.1, c.shape), index=c.index, columns=c.columns).rolling(20).mean()}
    for n in ("dxy_metal_switch", "real_yield_switch", "gold_silver_ratio", "copper_gold_rotation",
              "cot_contrarian", "cot_commercial_follow", "ts_seasonality"):
        w = REGISTRY[n](p, years=3) if n == "ts_seasonality" else REGISTRY[n](p)   # 6y of data
        assert w.shape == p.c.shape and np.isfinite(w.values).all(), n
        assert (w.abs().sum(axis=1) <= 1 + 1e-9).all(), n
        assert (w.abs().sum(axis=1) > 0).mean() > 0.05, n
    for f in ("dxy_weak", "real_yield_falling"):
        a, b = rules.FILTERS[f](p)
        assert a.shape == p.c.shape


def test_studies_accept_every_variant_kind():
    """Robustness studies must work when the selected variant carries internal keys (overlay etc.)."""
    from lab import candidates as CD, robustness as RB
    p = Panel.from_close(data.synthetic_prices(6, 900, seed=20))
    for cand in (CD.StrategyCandidate("ts_momentum", overlays=["vt15", "dd20"]),
                 CD.from_spec({"rule": "rsi_reversal", "overlays": "all"})):
        base = cand.variants()[0]
        for v in [base] + cand.overlay_variants([base])[:2]:
            assert "sharpe_delayed_1bar" in RB.delay_test(cand, p, v, Costs())
            RB.noise_test(cand, p, v, Costs(), n=1)
            cand.targets(p, v)


def test_exits_and_overlays_are_opt_in():
    """Without `exits:` only the rule's own exit is used; without `overlays:` no overlay is tried."""
    from lab import candidates as CD, overlays
    c0 = CD.from_spec({"rule": "rsi_reversal"})
    assert c0.exits == [0] and c0.overlays == []
    seeds = c0.variants()[:2]
    assert c0.variants(stage=2, seeds=seeds) == [] and c0.overlay_variants(seeds) == []
    ca = CD.from_spec({"rule": "rsi_reversal", "exits": "all", "overlays": "all"})
    assert len(ca.exits) > 40 and ca.overlays == list(overlays.KINDS)
    cl = CD.from_spec({"strategy": "ts_momentum", "overlays": ["vt15"]})
    assert len(cl.overlay_variants(cl.variants()[:1])) == 1



def test_breakeven_win_rate():
    import pandas as pd
    from lab import perp
    # 40% win rate with 1:3 payoff is profitable: breakeven = 1/(1+3) = 25%
    s = perp.trade_stats(pd.DataFrame({"ret": [0.06, -0.02, -0.02, 0.06, -0.02]}), 0.0)
    assert abs(s["breakeven_wr"] - 0.25) < 1e-9 and abs(s["wr_margin"] - 0.15) < 1e-9
    # 60% win rate with 1:0.5 payoff loses: breakeven = 66.7%
    s = perp.trade_stats(pd.DataFrame({"ret": [0.01, 0.01, 0.01, -0.02, -0.02]}), 0.0)
    assert s["wr_margin"] < 0 and s["expectancy"] < 0
    assert perp.trade_stats(pd.DataFrame(), 0.001)["breakeven_wr"] is None



def test_mega_holdout_is_sealed():
    import pandas as pd
    from lab import mega, screen
    cfg = mega.cfg_load()
    p, c = mega.load_class("metals", cfg, synthetic=True)
    cut = mega.cut_date(p, cfg)
    R, _, tr = screen.run_variant(p, "ma_cross", {"fast": 20, "slow": 100} if "fast" in screen.rules.RULES["ma_cross"].grid
                                  else screen.rules.grid_points(screen.rules.RULES["ma_cross"].grid)[0], 28, "long", c)
    d = mega.stats(R, tr, cut, c.per_turnover, p.ppy, "disc")
    # changing holdout returns must not change any discovery number
    R2 = R.copy(); R2.loc[R2.index >= cut] = 0.05
    assert mega.stats(R2, tr, cut, c.per_turnover, p.ppy, "disc")["pool_sharpe"] == d["pool_sharpe"]
    assert set(mega.d_checks(d, cfg["discovery"])) == {"D1", "D2", "D4"}



def test_h054_bot_parity_fixture():
    """tests/fixtures/h054_parity.json is copied to h054_spot_bot/tests/fixtures/. The bot test checks its own
    bot/signal.py against it. If lab/core.py changes, this test fails: regenerate the fixture
    (python tests/make_parity_fixture.py), copy it to the bot repo, and update bot/signal.py."""
    import json
    import numpy as np
    import pandas as pd
    from lab import core
    fx = json.loads((Path(__file__).resolve().parent / "fixtures" / "h054_parity.json").read_text())
    close = pd.Series(fx["close"], pd.date_range(fx["index_start"], periods=len(fx["close"]), freq="4h"))
    e = core.exposure(close, fx["rule"], fx["params"], fx["ppy"])
    b = core.apply_band(e, fx["band"])
    assert np.allclose(e.values, fx["exposure_raw"], atol=1e-9), "lab core exposure changed: bot signal.py is now out of sync"
    assert np.allclose(b.values, fx["exposure_band"], atol=1e-9), "lab apply_band changed: bot signal.py is now out of sync"


def _cal_panel(prices_seed=0, n=520, extra=None):
    idx = pd.bdate_range("2021-01-04", periods=n)
    rng = np.random.default_rng(prices_seed)
    c = pd.DataFrame(100 * np.exp(np.cumsum(rng.normal(0, 0.01, (n, 2)), 0)), index=idx, columns=["A", "B"])
    return Panel(o=c, h=c * 1.01, l=c * 0.99, c=c, v=c * 0 + 1e6, extra=extra or {})


def test_seasonality_rules_are_calendar_only_and_causal():
    """Seasonality signals use the trading calendar only: other prices give the same signals, and the entry at
    close t happens exactly one bar before the window starts (fill at open t+1 = first bar of the window)."""
    for name, prm in (("turn_of_month", {"pre": 2, "post": 2}), ("weekday_long", {"day": 4}), ("halloween", {"start": 11, "end": 4})):
        s1 = rules.RULES[name].fn(_cal_panel(0), **prm)
        s2 = rules.RULES[name].fn(_cal_panel(7), **prm)
        assert s1.entry_long.equals(s2.entry_long) and s1.exit_long.equals(s2.exit_long), name
        assert s1.entry_long.any().all(), name
    p = _cal_panel(0)
    s = rules.RULES["weekday_long"].fn(p, day=4)           # Friday window: entry on Thursday's close
    ent = p.index[s.entry_long["A"].values]
    assert all(d.weekday() == 3 for d in ent), "weekday entry must be the bar BEFORE the window"
    tom = rules.RULES["turn_of_month"].fn(p, pre=1, post=1)
    last_bars = set(pd.Series(p.index, p.index).groupby(p.index.to_period("M")).last())
    firsts = [p.index[i + 1] for i in np.where(tom.entry_long["A"].values)[0] if i + 1 < len(p.index)]
    assert all(d in last_bars for d in firsts), "turn-of-month window must start on the last bar of a month"


def test_funding_rule_is_causal():
    """funding_extreme at bar t must not change when funding after t changes."""
    idx = pd.bdate_range("2021-01-04", periods=600)
    rng = np.random.default_rng(3)
    fr = pd.DataFrame(rng.normal(0.0003, 0.0004, (600, 2)), index=idx, columns=["A", "B"])
    fr2 = fr.copy()
    fr2.iloc[400:] = 0.05                                    # wild future funding
    s1 = rules.RULES["funding_extreme"].fn(_cal_panel(1, 600, {"funding_daily": fr}), n=90, th=1.5)
    s2 = rules.RULES["funding_extreme"].fn(_cal_panel(1, 600, {"funding_daily": fr2}), n=90, th=1.5)
    assert s1.entry_long.iloc[:400].equals(s2.entry_long.iloc[:400]) and s1.entry_short.iloc[:400].equals(s2.entry_short.iloc[:400])
    assert not rules.RULES["funding_extreme"].fn(_cal_panel(1), n=90, th=1.5).entry_long.any().any(), "no funding data -> no signal"


if __name__ == "__main__":
    for k, fn in list(globals().items()):
        if k.startswith("test_"):
            fn()
            print("ok", k)
