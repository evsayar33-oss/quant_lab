"""Entry / exit rule catalog for the trade engine.

A rule is fn(panel, **params) -> Signals with four boolean frames:
  entry_long, exit_long, entry_short, exit_short   (signal at close t -> trade at open t+1)
`entry_short`/`exit_short` may be None (long-only idea).

Every rule has a parameter GRID with indicator-setting variants (e.g. RSI 7/9/14/21/28).
The scanner sweeps the whole grid and the Deflated Sharpe Ratio pays for every variant.

FILTERS restrict entries (trend, ADX, market regime, volatility, volume, fundamentals).
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable

import numpy as np
import pandas as pd

from lab import indicators as I
from lab.panel import Panel


@dataclass
class Signals:
    entry_long: pd.DataFrame
    exit_long: pd.DataFrame
    entry_short: pd.DataFrame | None = None
    exit_short: pd.DataFrame | None = None


@dataclass
class Rule:
    name: str
    family: str
    fn: Callable[..., Signals]
    grid: dict = field(default_factory=dict)
    source: str = ""


RULES: dict[str, Rule] = {}


def rule(name: str, family: str, grid: dict, source: str = ""):
    def deco(fn):
        RULES[name] = Rule(name, family, fn, grid, source)
        return fn
    return deco


def _b(x: pd.DataFrame) -> pd.DataFrame:
    return x.fillna(False).astype(bool)


def _osc(osc: pd.DataFrame, lo: float, hi: float, exit_lo: float, exit_hi: float) -> Signals:
    """Mean-reversion oscillator: long when it crosses back up through `lo`."""
    return Signals(_b(I.cross_up(osc, lo)), _b(osc > exit_lo),
                   _b(I.cross_down(osc, hi)), _b(osc < exit_hi))


def _cross(fast: pd.DataFrame, slow: pd.DataFrame) -> Signals:
    up, dn = _b(I.cross_up(fast, slow)), _b(I.cross_down(fast, slow))
    return Signals(up, dn, dn, up)


def _state(direction: pd.DataFrame) -> Signals:
    """Trend-state indicator (+1/-1): enter on flip, exit on opposite flip."""
    d = direction
    up = _b((d > 0) & (d.shift(1) <= 0))
    dn = _b((d < 0) & (d.shift(1) >= 0))
    return Signals(up, dn, dn, up)


# =================================================================== MOMENTUM OSCILLATORS (mean reversion)
@rule("rsi_reversal", "oscillator",
      {"n": [2, 3, 5, 7, 9, 14, 21, 28], "lo": [10, 20, 25, 30, 35], "exit": [50, 60, 70]},
      "Wilder (1978) RSI; Connors (2009)")
def rsi_reversal(p: Panel, n, lo, exit):
    r = I.rsi(p.c, n)
    return _osc(r, lo, 100 - lo, exit, 100 - exit)


@rule("rsi_midline", "momentum", {"n": [9, 14, 21, 28], "level": [50, 55, 60]}, "RSI regime shift")
def rsi_midline(p: Panel, n, level):
    r = I.rsi(p.c, n)
    return Signals(_b(I.cross_up(r, level)), _b(I.cross_down(r, 50)),
                   _b(I.cross_down(r, 100 - level)), _b(I.cross_up(r, 50)))


@rule("stoch_reversal", "oscillator",
      {"k": [5, 9, 14, 21], "d": [3, 5], "smooth": [1, 3], "lo": [10, 20, 25]}, "Lane stochastic")
def stoch_reversal(p: Panel, k, d, smooth, lo):
    kk, dd = I.stoch(p.h, p.l, p.c, k, d, smooth)
    el = _b(I.cross_up(kk, dd) & (dd < lo + 10))
    es = _b(I.cross_down(kk, dd) & (dd > 90 - lo))
    return Signals(el, _b(kk > 80), es, _b(kk < 20))


@rule("stochrsi_reversal", "oscillator", {"n": [9, 14, 21], "lo": [5, 10, 20]}, "Chande & Kroll StochRSI")
def stochrsi_reversal(p: Panel, n, lo):
    k, _ = I.stoch_rsi(p.c, n)
    return _osc(k, lo, 100 - lo, 80, 20)


@rule("williams_reversal", "oscillator", {"n": [7, 10, 14, 21], "lo": [-95, -90, -80]}, "Williams %R")
def williams_reversal(p: Panel, n, lo):
    w = I.williams_r(p.h, p.l, p.c, n)
    return _osc(w, lo, -100 - lo, -30, -70)


@rule("cci_reversal", "oscillator", {"n": [14, 20, 40], "lo": [-200, -150, -100]}, "Lambert (1980) CCI")
def cci_reversal(p: Panel, n, lo):
    x = I.cci(p.h, p.l, p.c, n)
    return _osc(x, lo, -lo, 0, 0)


@rule("cci_breakout", "momentum", {"n": [14, 20, 40], "level": [100, 150]}, "CCI trend entry")
def cci_breakout(p: Panel, n, level):
    x = I.cci(p.h, p.l, p.c, n)
    return Signals(_b(I.cross_up(x, level)), _b(x < 0), _b(I.cross_down(x, -level)), _b(x > 0))


@rule("mfi_reversal", "oscillator", {"n": [10, 14, 21], "lo": [10, 20, 30]}, "Quong & Soudack MFI")
def mfi_reversal(p: Panel, n, lo):
    return _osc(I.mfi(p.h, p.l, p.c, p.v, n), lo, 100 - lo, 60, 40)


@rule("ultimate_reversal", "oscillator", {"a": [5, 7], "lo": [25, 30, 35]}, "Williams Ultimate Oscillator")
def ultimate_reversal(p: Panel, a, lo):
    return _osc(I.ultimate(p.h, p.l, p.c, a, 2 * a, 4 * a), lo, 100 - lo, 60, 40)


@rule("wavetrend_reversal", "oscillator",
      {"n1": [9, 10, 12], "n2": [18, 21, 26], "lo": [-60, -53, -40]}, "LazyBear WaveTrend (ATVS)")
def wavetrend_reversal(p: Panel, n1, n2, lo):
    w1, w2 = I.wavetrend(p.h, p.l, p.c, n1, n2)
    el = _b(I.cross_up(w1, w2) & (w1 < lo))
    es = _b(I.cross_down(w1, w2) & (w1 > -lo))
    return Signals(el, _b(I.cross_down(w1, w2) & (w1 > 0)), es, _b(I.cross_up(w1, w2) & (w1 < 0)))


@rule("zscore_reversion", "mean_reversion", {"n": [10, 20, 50], "z": [1.5, 2.0, 2.5]}, "Statistical mean reversion")
def zscore_reversion(p: Panel, n, z):
    x = I.zscore(p.c, n)
    return Signals(_b(I.cross_up(x, -z)), _b(x > 0), _b(I.cross_down(x, z)), _b(x < 0))


@rule("bollinger_reversion", "mean_reversion", {"n": [10, 20, 30], "k": [1.5, 2.0, 2.5, 3.0]}, "Bollinger (2001)")
def bollinger_reversion(p: Panel, n, k):
    lo, mid, up = I.bollinger(p.c, n, k)
    return Signals(_b(I.cross_up(p.c, lo)), _b(p.c > mid), _b(I.cross_down(p.c, up)), _b(p.c < mid))


@rule("ibs_reversion", "mean_reversion", {"lo": [0.1, 0.2, 0.3], "hi": [0.7, 0.8]}, "Internal Bar Strength")
def ibs_reversion(p: Panel, lo, hi):
    x = I.ibs(p.h, p.l, p.c)
    return Signals(_b(x < lo), _b(x > hi), _b(x > 1 - lo), _b(x < 1 - hi))


@rule("down_days", "mean_reversion", {"n": [3, 4, 5], "hold_exit": [1, 3]}, "Consecutive down closes")
def down_days(p: Panel, n, hold_exit):
    e = _b(I.consecutive(p.c, n, up=False))
    x = _b(I.consecutive(p.c, hold_exit, up=True))
    return Signals(e, x, _b(I.consecutive(p.c, n, up=True)), _b(I.consecutive(p.c, hold_exit, up=False)))


# =================================================================== TREND / MOMENTUM
@rule("ma_cross", "trend",
      {"kind": ["sma", "ema", "hma", "dema", "tema", "kama"],
       "pair": [(5, 20), (10, 30), (10, 50), (20, 50), (20, 100), (50, 150), (50, 200)]},
      "Moving-average crossover")
def ma_cross(p: Panel, kind, pair):
    f, s = pair
    return _cross(I.ma(p.c, f, kind), I.ma(p.c, s, kind))


@rule("price_ma", "trend", {"kind": ["sma", "ema", "hma", "kama"], "n": [20, 50, 100, 150, 200]},
      "Faber (2007) price vs moving average")
def price_ma(p: Panel, kind, n):
    return _cross(p.c, I.ma(p.c, n, kind))


@rule("triple_ma", "trend", {"set": [(5, 20, 50), (10, 50, 200), (20, 50, 100)], "kind": ["sma", "ema"]},
      "Triple MA alignment")
def triple_ma(p: Panel, set, kind):
    a, b, c = (I.ma(p.c, n, kind) for n in set)
    bull = (a > b) & (b > c); bear = (a < b) & (b < c)
    return Signals(_b(bull & ~bull.shift(1, fill_value=False)), _b(a < b),
                   _b(bear & ~bear.shift(1, fill_value=False)), _b(a > b))


@rule("macd_cross", "trend",
      {"cfg": [(12, 26, 9), (8, 21, 5), (5, 35, 5), (19, 39, 9), (6, 13, 4)], "zero_filter": [False, True]},
      "Appel MACD")
def macd_cross(p: Panel, cfg, zero_filter):
    line, sig, _ = I.macd(p.c, *cfg)
    s = _cross(line, sig)
    if zero_filter:
        s.entry_long = s.entry_long & (line < 0)
        s.entry_short = s.entry_short & (line > 0)
    return s


@rule("macd_zero", "trend", {"cfg": [(12, 26, 9), (8, 21, 5), (5, 35, 5)]}, "MACD zero-line cross")
def macd_zero(p: Panel, cfg):
    line, _, _ = I.macd(p.c, *cfg)
    return _cross(line, I.level(line, 0))


@rule("ppo_cross", "trend", {"cfg": [(12, 26, 9), (10, 30, 9)]}, "Percentage Price Oscillator")
def ppo_cross(p: Panel, cfg):
    line, sig, _ = I.ppo(p.c, *cfg)
    return _cross(line, sig)


@rule("trix_cross", "trend", {"n": [9, 12, 15, 21], "signal": [7, 9]}, "Hutson TRIX")
def trix_cross(p: Panel, n, signal):
    line, sig = I.trix(p.c, n, signal)
    return _cross(line, sig)


@rule("tsi_cross", "trend", {"cfg": [(25, 13, 7), (13, 7, 7), (40, 20, 10)]}, "Blau True Strength Index")
def tsi_cross(p: Panel, cfg):
    line, sig = I.tsi(p.c, *cfg)
    return _cross(line, sig)


@rule("roc_breakout", "momentum", {"n": [10, 21, 63, 126, 252], "th": [0, 5, 10]}, "Rate-of-change momentum")
def roc_breakout(p: Panel, n, th):
    r = I.roc(p.c, n)
    return Signals(_b(I.cross_up(r, th)), _b(r < 0), _b(I.cross_down(r, -th)), _b(r > 0))


@rule("awesome_zero", "momentum", {"fast": [5], "slow": [34, 50]}, "Bill Williams Awesome Oscillator")
def awesome_zero(p: Panel, fast, slow):
    a = I.awesome(p.h, p.l, fast, slow)
    return _cross(a, I.level(a, 0))


@rule("coppock_turn", "momentum", {"scale": [5, 21]}, "Coppock curve 14/11/10 (weekly or monthly bars)")
def coppock_turn(p: Panel, scale):
    x = I.coppock(p.c, 14 * scale, 11 * scale, 10 * scale)
    up = _b((x.diff() > 0) & (x.diff().shift(1) <= 0) & (x < 0))
    return Signals(up, _b((x.diff() < 0) & (x > 0)), None, None)


@rule("adx_trend", "trend", {"n": [10, 14, 20], "th": [20, 25, 30]}, "Wilder DMI/ADX")
def adx_trend(p: Panel, n, th):
    pdi, mdi, adx = I.dmi(p.h, p.l, p.c, n)
    strong = adx > th
    return Signals(_b(I.cross_up(pdi, mdi) & strong), _b(I.cross_down(pdi, mdi)),
                   _b(I.cross_down(pdi, mdi) & strong), _b(I.cross_up(pdi, mdi)))


@rule("aroon_cross", "trend", {"n": [14, 25, 50]}, "Chande Aroon")
def aroon_cross(p: Panel, n):
    up, dn = I.aroon(p.h, p.l, n)
    return _cross(up, dn)


@rule("vortex_cross", "trend", {"n": [14, 21, 28]}, "Botes & Siepman Vortex")
def vortex_cross(p: Panel, n):
    vp, vm = I.vortex(p.h, p.l, p.c, n)
    return _cross(vp, vm)


@rule("supertrend_flip", "trend",
      {"cfg": [(7, 2.0), (10, 2.0), (10, 3.0), (14, 3.0), (20, 4.0)]}, "Supertrend (ATR bands)")
def supertrend_flip(p: Panel, cfg):
    return _state(I.supertrend(p.h, p.l, p.c, *cfg))


@rule("psar_flip", "trend", {"cfg": [(0.01, 0.1), (0.02, 0.2), (0.03, 0.3)]}, "Wilder Parabolic SAR")
def psar_flip(p: Panel, cfg):
    return _state(I.psar(p.h, p.l, *cfg))


@rule("ichimoku_cloud", "trend", {"cfg": [(9, 26, 52), (7, 22, 44), (20, 60, 120)]}, "Ichimoku Kinko Hyo")
def ichimoku_cloud(p: Panel, cfg):
    t, k, a, b = I.ichimoku(p.h, p.l, p.c, *cfg)
    top, bot = np.maximum(a, b), np.minimum(a, b)
    bull = (p.c > top) & (t > k); bear = (p.c < bot) & (t < k)
    return Signals(_b(bull & ~bull.shift(1, fill_value=False)), _b(p.c < k),
                   _b(bear & ~bear.shift(1, fill_value=False)), _b(p.c > k))


@rule("heikin_ashi", "trend", {"confirm": [1, 2, 3]}, "Heikin-Ashi colour change")
def heikin_ashi(p: Panel, confirm):
    d = I.heikin_ashi_dir(p.o, p.h, p.l, p.c)
    up = (d > 0).astype(int).rolling(confirm).sum() == confirm
    dn = (d < 0).astype(int).rolling(confirm).sum() == confirm
    return Signals(_b(up & ~up.shift(1, fill_value=False)), _b(d < 0),
                   _b(dn & ~dn.shift(1, fill_value=False)), _b(d > 0))


@rule("linreg_slope", "trend", {"n": [20, 50, 100], "th": [0.0005, 0.001]}, "Regression slope")
def linreg_slope(p: Panel, n, th):
    s = I.linreg_slope(p.c, n)
    return Signals(_b(I.cross_up(s, th)), _b(s < 0), _b(I.cross_down(s, -th)), _b(s > 0))


@rule("elder_impulse", "trend", {"ema_n": [13, 21], "macd_cfg": [(12, 26, 9)]}, "Elder Impulse System")
def elder_impulse(p: Panel, ema_n, macd_cfg):
    e = I.ema(p.c, ema_n); _, _, hist = I.macd(p.c, *macd_cfg)
    green = (e.diff() > 0) & (hist.diff() > 0); red = (e.diff() < 0) & (hist.diff() < 0)
    return Signals(_b(green & ~green.shift(1, fill_value=False)), _b(red),
                   _b(red & ~red.shift(1, fill_value=False)), _b(green))


# =================================================================== BREAKOUT / VOLATILITY
@rule("donchian_breakout", "breakout", {"entry": [20, 40, 55, 100], "exit": [10, 20]}, "Turtle / Donchian")
def donchian_breakout(p: Panel, entry, exit):
    lo_e, hi_e = I.donchian(p.h, p.l, entry)
    lo_x, hi_x = I.donchian(p.h, p.l, exit)
    return Signals(_b(p.c > hi_e.shift(1)), _b(p.c < lo_x.shift(1)),
                   _b(p.c < lo_e.shift(1)), _b(p.c > hi_x.shift(1)))


@rule("bollinger_breakout", "breakout", {"n": [20, 50], "k": [1.5, 2.0, 2.5]}, "Bollinger band breakout")
def bollinger_breakout(p: Panel, n, k):
    lo, mid, up = I.bollinger(p.c, n, k)
    return Signals(_b(I.cross_up(p.c, up)), _b(p.c < mid), _b(I.cross_down(p.c, lo)), _b(p.c > mid))


@rule("bb_squeeze", "breakout", {"n": [20], "q": [0.1, 0.2], "look": [126, 252]}, "Bollinger squeeze release")
def bb_squeeze(p: Panel, n, q, look):
    w = I.bb_width(p.c, n)
    squeezed = w <= w.rolling(look, min_periods=look // 2).quantile(q)
    lo, mid, up = I.bollinger(p.c, n)
    was = squeezed.shift(1, fill_value=False)
    return Signals(_b(was & (p.c > up)), _b(p.c < mid), _b(was & (p.c < lo)), _b(p.c > mid))


@rule("keltner_breakout", "breakout", {"n": [20, 50], "k": [1.5, 2.0, 2.5]}, "Keltner channel")
def keltner_breakout(p: Panel, n, k):
    lo, mid, up = I.keltner(p.h, p.l, p.c, n, k)
    return Signals(_b(I.cross_up(p.c, up)), _b(p.c < mid), _b(I.cross_down(p.c, lo)), _b(p.c > mid))


@rule("atr_breakout", "breakout", {"n": [10, 20], "k": [1.0, 1.5, 2.0]}, "Volatility (ATR) breakout")
def atr_breakout(p: Panel, n, k):
    a = I.atr(p.h, p.l, p.c, n)
    up = p.c > p.c.shift(1) + k * a.shift(1)
    dn = p.c < p.c.shift(1) - k * a.shift(1)
    m = I.sma(p.c, n)
    return Signals(_b(up), _b(p.c < m), _b(dn), _b(p.c > m))


@rule("nr7_breakout", "breakout", {"n": [4, 7]}, "Crabel narrow-range breakout")
def nr7_breakout(p: Panel, n):
    setup = I.nr(p.h, p.l, n).shift(1, fill_value=False)
    return Signals(_b(setup & (p.c > p.h.shift(1))), _b(p.c < p.l.shift(1)),
                   _b(setup & (p.c < p.l.shift(1))), _b(p.c > p.h.shift(1)))


@rule("high_52w_break", "breakout", {"n": [126, 252], "exit_ma": [50, 100]}, "George & Hwang 52-week high")
def high_52w_break(p: Panel, n, exit_ma):
    hi = p.h.rolling(n, min_periods=n).max().shift(1)
    m = I.sma(p.c, exit_ma)
    return Signals(_b(p.c > hi), _b(p.c < m), None, None)


@rule("volume_breakout", "breakout", {"n": [20, 50], "rv": [1.5, 2.0, 3.0]}, "Price breakout on volume surge")
def volume_breakout(p: Panel, n, rv):
    hi = p.h.rolling(n, min_periods=n).max().shift(1)
    lo = p.l.rolling(n, min_periods=n).min().shift(1)
    surge = I.rel_volume(p.v, n) > rv
    m = I.sma(p.c, n)
    return Signals(_b((p.c > hi) & surge), _b(p.c < m), _b((p.c < lo) & surge), _b(p.c > m))


@rule("gap_fade", "mean_reversion", {"g": [0.02, 0.03, 0.05]}, "Opening gap fade (close-based)")
def gap_fade(p: Panel, g):
    gp = I.gap(p.o, p.c)
    return Signals(_b(gp < -g), _b(p.c > p.c.shift(1)), _b(gp > g), _b(p.c < p.c.shift(1)))


# =================================================================== VOLUME
@rule("obv_trend", "volume", {"n": [20, 50], "price_n": [20, 50]}, "Granville OBV")
def obv_trend(p: Panel, n, price_n):
    o = I.obv(p.c, p.v)
    up = (o > I.ema(o, n)) & (p.c > I.ema(p.c, price_n))
    dn = (o < I.ema(o, n)) & (p.c < I.ema(p.c, price_n))
    return Signals(_b(up & ~up.shift(1, fill_value=False)), _b(o < I.ema(o, n)),
                   _b(dn & ~dn.shift(1, fill_value=False)), _b(o > I.ema(o, n)))


@rule("cmf_flow", "volume", {"n": [10, 20, 40], "th": [0.05, 0.1, 0.2]}, "Chaikin Money Flow")
def cmf_flow(p: Panel, n, th):
    x = I.cmf(p.h, p.l, p.c, p.v, n)
    return Signals(_b(I.cross_up(x, th)), _b(x < 0), _b(I.cross_down(x, -th)), _b(x > 0))


@rule("chaikin_osc", "volume", {"cfg": [(3, 10), (5, 20)]}, "Chaikin oscillator")
def chaikin_osc(p: Panel, cfg):
    x = I.chaikin_osc(p.h, p.l, p.c, p.v, *cfg)
    return _cross(x, I.level(x, 0))


@rule("vwap_cross", "volume", {"n": [10, 20, 50]}, "Rolling VWAP cross")
def vwap_cross(p: Panel, n):
    return _cross(p.c, I.rolling_vwap(p.h, p.l, p.c, p.v, n))


@rule("force_index", "volume", {"n": [2, 13]}, "Elder Force Index")
def force_index(p: Panel, n):
    f = I.force_index(p.c, p.v, n)
    trend = p.c > I.ema(p.c, 50)
    return Signals(_b((f < 0) & trend & (f.shift(1) >= 0)), _b(f > 0), None, None)


# =================================================================== CANDLESTICK
@rule("engulfing", "candle", {"trend_n": [0, 50, 200]}, "Nison candlestick engulfing")
def engulfing(p: Panel, trend_n):
    bull, bear = I.bullish_engulfing(p.o, p.c), I.bearish_engulfing(p.o, p.c)
    if trend_n:
        m = I.sma(p.c, trend_n)
        bull, bear = bull & (p.c > m), bear & (p.c < m)
    return Signals(_b(bull), _b(I.bearish_engulfing(p.o, p.c)), _b(bear), _b(I.bullish_engulfing(p.o, p.c)))


@rule("hammer_star", "candle", {"lookback_low": [10, 20]}, "Hammer at a local low / shooting star at a high")
def hammer_star(p: Panel, lookback_low):
    at_low = p.l <= p.l.rolling(lookback_low).min()
    at_high = p.h >= p.h.rolling(lookback_low).max()
    m = I.sma(p.c, lookback_low)
    return Signals(_b(I.hammer(p.o, p.h, p.l, p.c) & at_low), _b(p.c > m),
                   _b(I.shooting_star(p.o, p.h, p.l, p.c) & at_high), _b(p.c < m))


@rule("inside_bar", "candle", {"trend_n": [50, 200]}, "Inside-bar breakout with trend")
def inside_bar(p: Panel, trend_n):
    ib = I.inside_bar(p.h, p.l).shift(1, fill_value=False)
    m = I.sma(p.c, trend_n)
    return Signals(_b(ib & (p.c > p.h.shift(1)) & (p.c > m)), _b(p.c < m),
                   _b(ib & (p.c < p.l.shift(1)) & (p.c < m)), _b(p.c > m))


# =================================================================== REGIME-ADAPTIVE
@rule("hurst_switch", "adaptive", {"n": [100, 200], "fast": [20], "rsi_n": [2, 5]},
      "Trend-follow when persistent, mean-revert when anti-persistent")
def hurst_switch(p: Panel, n, fast, rsi_n):
    hp = I.hurst_proxy(p.c, n)
    m = I.sma(p.c, fast); r = I.rsi(p.c, rsi_n)
    trend_e = (hp > 0.55) & I.cross_up(p.c, m)
    mr_e = (hp < 0.45) & (r < 10)
    return Signals(_b(trend_e | mr_e), _b(((hp > 0.55) & (p.c < m)) | ((hp <= 0.55) & (r > 70))), None, None)


@rule("chop_switch", "adaptive", {"n": [14], "lo": [38.2], "hi": [61.8]}, "Choppiness-index regime switch")
def chop_switch(p: Panel, n, lo, hi):
    ch = I.choppiness(p.h, p.l, p.c, n)
    lo_, mid, up = I.bollinger(p.c, 20, 2)
    _, hi_d = I.donchian(p.h, p.l, 20)
    trend_e = (ch < lo) & (p.c > hi_d.shift(1))
    range_e = (ch > hi) & I.cross_up(p.c, lo_)
    return Signals(_b(trend_e | range_e), _b(p.c < mid), None, None)


# =================================================================== FILTERS
FILTERS: dict[str, Callable[[Panel], tuple[pd.DataFrame, pd.DataFrame]]] = {}


def filt(name):
    def deco(fn):
        FILTERS[name] = fn
        return fn
    return deco


def _all(p: Panel, val: bool = True):
    return pd.DataFrame(val, index=p.index, columns=p.columns)


@filt("none")
def f_none(p):
    return _all(p), _all(p)


for _n in (50, 100, 200):
    def _mk(n):
        def f(p):
            m = I.sma(p.c, n)
            return _b(p.c > m), _b(p.c < m)
        return f
    FILTERS[f"trend_sma{_n}"] = _mk(_n)


for _t in (20, 25):
    def _mk_adx(t):
        def f(p):
            _, _, adx = I.dmi(p.h, p.l, p.c, 14)
            s = _b(adx > t)
            return s, s
        return f
    FILTERS[f"adx{_t}"] = _mk_adx(_t)


@filt("regime_bench200")
def f_regime(p):
    """Longs only when the market (benchmark) is above its 200-day SMA; shorts only below."""
    if p.bench is None:
        return _all(p), _all(p)
    up = p.bench > p.bench.rolling(200, min_periods=200).mean()
    L = pd.DataFrame(np.repeat(up.values[:, None], p.c.shape[1], 1), index=p.index, columns=p.columns)
    return _b(L), _b(~L)


@filt("low_vol")
def f_low_vol(p):
    n = I.natr(p.h, p.l, p.c, 20)
    calm = n < n.rolling(252, min_periods=126).median()
    return _b(calm), _b(calm)


@filt("volume_confirm")
def f_vol(p):
    s = _b(I.rel_volume(p.v, 20) > 1.0)
    return s, s


@filt("fund_quality")
def f_quality(p):
    """ROE above the cross-sectional median (needs fundamentals; otherwise no filter)."""
    roe = p.fund.get("roe")
    if roe is None or roe.notna().sum().sum() == 0:
        return _all(p), _all(p)
    med = roe.median(axis=1)
    good = roe.gt(med, axis=0)
    return _b(good), _b(~good)


@filt("fund_value")
def f_value(p):
    ep = p.fund.get("ep")
    if ep is None or ep.notna().sum().sum() == 0:
        return _all(p), _all(p)
    cheap = ep.gt(ep.median(axis=1), axis=0)
    return _b(cheap), _b(~cheap)


def grid_points(grid: dict) -> list[dict]:
    import itertools
    if not grid:
        return [{}]
    keys = list(grid)
    return [dict(zip(keys, v)) for v in itertools.product(*(grid[k] for k in keys))]


def apply_filter(sig: Signals, p: Panel, name: str) -> Signals:
    if name == "none":
        return sig
    fl, fs = FILTERS[name](p)
    return Signals(sig.entry_long & fl, sig.exit_long,
                   None if sig.entry_short is None else sig.entry_short & fs, sig.exit_short)


def n_variants() -> int:
    return sum(len(grid_points(r.grid)) for r in RULES.values())


# ------------------------------------------------------------------ higher-timeframe (multi-timeframe) filters
def _htf_trend(p: Panel, rule: str, n: int):
    """Trend of a HIGHER timeframe built only from completed higher-timeframe bars."""
    hc = p.c.resample(rule).last()
    up = hc > hc.rolling(n, min_periods=n).mean()
    intraday = len(p.index) > 1 and (p.index[1:] - p.index[:-1]).min() < pd.Timedelta(hours=20)
    if intraday:  # a weekly/monthly close is only known after that day ends
        up.index = up.index.normalize() + pd.Timedelta(days=1)
    al = up.astype(float).reindex(up.index.union(p.index)).sort_index().ffill().reindex(p.index)
    return al


for _nm, (_rule, _n) in {"htf_week_sma30": ("W-FRI", 30), "htf_week_sma10": ("W-FRI", 10),
                         "htf_month_sma10": ("ME", 10)}.items():
    def _mk_htf(rule, n):
        def f(p):
            al = _htf_trend(p, rule, n)
            return _b(al == 1), _b(al == 0)
        return f
    FILTERS[_nm] = _mk_htf(_rule, _n)


# ------------------------------------------------------------------ macro regime filters
def _macro_bool(p: Panel, key: str, fn):
    s = p.macro.get(key) if p.macro else None
    if s is None:
        return None
    ok = fn(s)
    return pd.DataFrame(np.repeat(ok.values[:, None], p.c.shape[1], 1), index=p.index, columns=p.columns)


@filt("vix_below_25")
def f_vix(p):
    m = _macro_bool(p, "^VIX", lambda s: s < 25)
    return (_all(p), _all(p)) if m is None else (_b(m), _b(~m))


@filt("vix_spike_buy")
def f_vix_spike(p):
    """Contrarian: allow longs only after fear spikes (VIX > 30)."""
    m = _macro_bool(p, "^VIX", lambda s: s > 30)
    return (_all(p), _all(p)) if m is None else (_b(m), _b(m))


@filt("usdtry_calm")
def f_usdtry(p):
    """BIST: avoid longs while the lira is under acute stress (USDTRY 20-day move > 5%)."""
    m = _macro_bool(p, "USDTRY=X", lambda s: s.pct_change(20, fill_method=None) < 0.05)
    return (_all(p), _all(p)) if m is None else (_b(m), _b(~m))


@filt("curve_normal")
def f_curve(p):
    """Longs only when the US yield curve (10y - 3m) is not inverted."""
    if not p.macro or p.macro.get("^TNX") is None or p.macro.get("^IRX") is None:
        return _all(p), _all(p)
    ok = (p.macro["^TNX"] - p.macro["^IRX"]) >= 0
    m = pd.DataFrame(np.repeat(ok.values[:, None], p.c.shape[1], 1), index=p.index, columns=p.columns)
    return _b(m), _b(~m)


@filt("member_only")
def f_member(p):
    """Survivorship control: entries only while the asset was an index member."""
    if p.member is None:
        return _all(p), _all(p)
    return _b(p.member), _b(p.member)


# ------------------------------------------------------------------ two-signal confirmation (combinations)
def confirm(primary: Signals, secondary: Signals, within: int = 0) -> Signals:
    """Entry only when the primary rule fires AND the secondary rule fired on the same bar
    or within the previous `within` bars. Exits follow the primary rule.
    Example: RSI oversold cross confirmed by a MACD bullish cross in the last 3 bars."""
    def win(x):
        if x is None:
            return None
        return x if within <= 0 else x.astype(int).rolling(within + 1, min_periods=1).max().astype(bool)
    el = primary.entry_long & win(secondary.entry_long)
    es = None
    if primary.entry_short is not None and secondary.entry_short is not None:
        es = primary.entry_short & win(secondary.entry_short)
    return Signals(_b(el), primary.exit_long, None if es is None else _b(es), primary.exit_short)
