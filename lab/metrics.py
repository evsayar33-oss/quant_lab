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
