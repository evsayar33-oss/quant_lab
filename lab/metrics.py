"""Performance and statistical-significance metrics.

Includes the Probabilistic Sharpe Ratio (PSR) and the Deflated Sharpe Ratio (DSR)
(Bailey & Lopez de Prado, 2014). DSR corrects the Sharpe ratio for the number of
strategy variants tried, so a parameter sweep cannot buy a false "edge".
"""
from __future__ import annotations

import math

import numpy as np
import pandas as pd
from scipy import stats

ANN = 252
EULER = 0.5772156649


def sharpe(r: pd.Series, periods: int = ANN) -> float:
    r = r.dropna()
    sd = r.std()
    return float(r.mean() / sd * math.sqrt(periods)) if sd > 0 else 0.0


def sortino(r: pd.Series, periods: int = ANN) -> float:
    r = r.dropna()
    dd = r[r < 0].std()
    return float(r.mean() / dd * math.sqrt(periods)) if dd and dd > 0 else 0.0


def max_drawdown(r: pd.Series) -> float:
    eq = (1 + r.fillna(0)).cumprod()
    return float((eq / eq.cummax() - 1).min()) if len(eq) else 0.0


def cagr(r: pd.Series, periods: int = ANN) -> float:
    r = r.dropna()
    if len(r) < 2:
        return 0.0
    total = float((1 + r).prod())
    yrs = len(r) / periods
    return total ** (1 / yrs) - 1 if total > 0 else -1.0


def psr(r: pd.Series, sr_benchmark: float = 0.0) -> float:
    """P(true Sharpe > benchmark). Inputs and benchmark are per-period (not annual)."""
    r = r.dropna()
    n = len(r)
    if n < 30 or r.std() == 0:
        return 0.0
    sr = r.mean() / r.std()
    g3 = stats.skew(r)
    g4 = stats.kurtosis(r, fisher=False)
    denom = math.sqrt(max(1e-12, 1 - g3 * sr + (g4 - 1) / 4 * sr ** 2))
    return float(stats.norm.cdf((sr - sr_benchmark) * math.sqrt(n - 1) / denom))


def expected_max_sharpe(n_trials: int, sr_var: float) -> float:
    """Expected max per-period Sharpe among n_trials skill-less variants."""
    if n_trials <= 1:
        return 0.0
    z1 = stats.norm.ppf(1 - 1 / n_trials)
    z2 = stats.norm.ppf(1 - 1 / (n_trials * math.e))
    return math.sqrt(max(sr_var, 0)) * ((1 - EULER) * z1 + EULER * z2)


def dsr(r: pd.Series, n_trials: int, trial_sharpes: list[float] | None = None) -> float:
    """Deflated Sharpe Ratio: PSR against the Sharpe that luck alone would give."""
    r = r.dropna()
    if trial_sharpes and len(trial_sharpes) > 1:
        var = float(np.var(trial_sharpes, ddof=1))
    else:
        var = 1.0 / max(len(r), 1)  # var of SR estimator under the null
    return psr(r, expected_max_sharpe(n_trials, var))


def summary(r: pd.Series, turnover: pd.Series | None = None, bench: pd.Series | None = None) -> dict:
    r = r.dropna()
    out = {
        "start": str(r.index[0].date()) if len(r) else None,
        "end": str(r.index[-1].date()) if len(r) else None,
        "years": round(len(r) / ANN, 2),
        "cagr": round(cagr(r), 4),
        "vol": round(float(r.std() * math.sqrt(ANN)), 4),
        "sharpe": round(sharpe(r), 3),
        "sortino": round(sortino(r), 3),
        "max_dd": round(max_drawdown(r), 4),
        "calmar": round(cagr(r) / abs(max_drawdown(r)), 3) if max_drawdown(r) < 0 else None,
        "hit_rate": round(float((r > 0).mean()), 3) if len(r) else None,
        "psr": round(psr(r), 3),
    }
    if turnover is not None and len(turnover):
        out["turnover_ann"] = round(float(turnover.mean() * ANN), 2)
    if bench is not None:
        b = bench.reindex(r.index).fillna(0)
        out["bench_cagr"] = round(cagr(b), 4)
        out["bench_sharpe"] = round(sharpe(b), 3)
        ex = r - b
        te = ex.std() * math.sqrt(ANN)
        out["info_ratio"] = round(float(ex.mean() * ANN / te), 3) if te > 0 else None
        cov = np.cov(r, b)
        out["beta"] = round(float(cov[0, 1] / cov[1, 1]), 3) if cov[1, 1] > 0 else None
    return out


def pbo(R: pd.DataFrame, S: int = 16) -> float | None:
    """Probability of Backtest Overfitting via CSCV (Bailey, Borwein, Lopez de Prado & Zhu, 2017).

    R: T x K matrix of per-period returns, one column per tried variant.
    Splits time into S blocks; for every half/half combination picks the in-sample best
    variant and records its out-of-sample rank. PBO = share of splits where that variant
    lands in the bottom half out of sample. 0 = robust selection, >0.5 = selection is noise.
    """
    import itertools

    R = R.dropna(how="all").fillna(0.0)
    T, K = R.shape
    if K < 2 or T < S * 20:
        return None
    blocks = np.array_split(np.arange(T), S)
    vals = R.values
    combos = list(itertools.combinations(range(S), S // 2))
    if len(combos) > 2000:  # cap work; sample evenly
        combos = combos[:: len(combos) // 2000 + 1]
    logits = []
    for is_b in combos:
        is_idx = np.concatenate([blocks[b] for b in is_b])
        oos_idx = np.concatenate([blocks[b] for b in range(S) if b not in is_b])
        def sr(ix):
            x = vals[ix]
            sd = x.std(axis=0)
            return np.where(sd > 0, x.mean(axis=0) / np.where(sd > 0, sd, 1), -np.inf)
        best = int(np.argmax(sr(is_idx)))
        oos = sr(oos_idx)
        rank = (oos < oos[best]).sum() + 0.5 * ((oos == oos[best]).sum() - 1)
        w = (rank + 1) / (K + 1)
        logits.append(np.log(w / (1 - w)))
    return float(np.mean(np.array(logits) <= 0))


def regime_breakdown(r: pd.Series, bench: pd.Series | None) -> dict:
    """Sharpe of the strategy inside market regimes (bull/bear trend, calm/stressed vol)."""
    if bench is None or len(r) < 100:
        return {}
    b = bench.reindex(r.index).ffill()
    full_b = bench.ffill()
    trend = (full_b > full_b.rolling(200, min_periods=150).mean()).reindex(r.index)
    vol = full_b.pct_change(fill_method=None).rolling(21).std()
    hi_vol = (vol > vol.rolling(252, min_periods=126).median()).reindex(r.index)
    out = {}
    for name, mask in (("bull", trend == True), ("bear", trend == False),  # noqa: E712
                       ("calm", hi_vol == False), ("stressed", hi_vol == True)):  # noqa: E712
        x = r[mask.fillna(False)]
        if len(x) > 60:
            out[name] = {"sharpe": round(sharpe(x), 2), "ann_ret": round(float(x.mean() * ANN), 4),
                         "days": int(len(x))}
    _ = b
    return out
