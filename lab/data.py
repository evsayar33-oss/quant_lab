"""Free market data loader with a local CSV cache.

Sources (all free, no API key):
  - yfinance : BIST (.IS), US stocks/ETFs, FX, indices
  - ccxt     : crypto spot/perp OHLCV from public endpoints (bitget -> okx fallback)

Output: wide DataFrame of adjusted close prices (index = date, columns = tickers).
"""
from __future__ import annotations

import os
import time
from pathlib import Path

import numpy as np
import pandas as pd

CACHE = Path(__file__).resolve().parent.parent / "data" / "cache"
CACHE.mkdir(parents=True, exist_ok=True)
MAX_CACHE_AGE_H = float(os.environ.get("LAB_CACHE_HOURS", "20"))


def _is_crypto(t: str) -> bool:
    return "/" in t  # e.g. BTC/USDT


def _cache_path(t: str, field: str) -> Path:
    safe = t.replace("/", "_").replace("^", "IDX_").replace("=", "_")
    return CACHE / f"{safe}__{field}.csv"


def _fresh(p: Path) -> bool:
    return p.exists() and (time.time() - p.stat().st_mtime) < MAX_CACHE_AGE_H * 3600


def _yf_download(tickers: list[str], start: str) -> dict[str, pd.DataFrame]:
    import yfinance as yf

    out: dict[str, pd.DataFrame] = {}
    if not tickers:
        return out
    raw = yf.download(tickers, start=start, auto_adjust=True, progress=False,
                      group_by="ticker", threads=True)
    for t in tickers:
        try:
            df = raw[t] if isinstance(raw.columns, pd.MultiIndex) else raw
            df = df.dropna(how="all")
            if len(df):
                out[t] = df[["Open", "High", "Low", "Close", "Volume"]]
        except KeyError:
            pass
    return out


def _ccxt_download(symbol: str, start: str, timeframe: str = "1d") -> pd.DataFrame | None:
    import ccxt

    since0 = int(pd.Timestamp(start, tz="UTC").timestamp() * 1000)
    for ex_id in ("bitget", "okx", "kucoin"):
        try:
            ex = getattr(ccxt, ex_id)({"enableRateLimit": True})
            rows, since = [], since0
            for _ in range(200):
                batch = ex.fetch_ohlcv(symbol, timeframe, since=since, limit=200)
                if not batch:
                    break
                rows += batch
                nxt = batch[-1][0] + 1
                if nxt <= since:
                    break
                since = nxt
                if len(batch) < 2:
                    break
            if rows:
                df = pd.DataFrame(rows, columns=["ts", "Open", "High", "Low", "Close", "Volume"])
                df = df.drop_duplicates("ts")
                df.index = pd.to_datetime(df["ts"], unit="ms").dt.tz_localize(None).dt.normalize()
                return df.drop(columns="ts")
        except Exception as e:  # noqa: BLE001 - try next exchange
            print(f"[data] {ex_id} {symbol} failed: {e}")
    return None


def load_ohlcv(tickers: list[str], start: str = "2010-01-01") -> dict[str, pd.DataFrame]:
    """Return {ticker: OHLCV DataFrame}. Uses cache when fresh."""
    result: dict[str, pd.DataFrame] = {}
    need_yf: list[str] = []
    for t in tickers:
        p = _cache_path(t, "ohlcv")
        if _fresh(p):
            df = pd.read_csv(p, index_col=0, parse_dates=True)
            if len(df) and df.index[0] <= pd.Timestamp(start) + pd.Timedelta(days=10):
                result[t] = df
                continue
        if _is_crypto(t):
            df = _ccxt_download(t, start)
            if df is not None:
                df.to_csv(p)
                result[t] = df
        else:
            need_yf.append(t)
    for t, df in _yf_download(need_yf, start).items():
        df.to_csv(_cache_path(t, "ohlcv"))
        result[t] = df
    missing = [t for t in tickers if t not in result]
    if missing:
        print(f"[data] WARNING no data for: {missing}")
    return result


def load_prices(tickers: list[str], start: str = "2010-01-01", field: str = "Close") -> pd.DataFrame:
    data = load_ohlcv(tickers, start)
    px = pd.DataFrame({t: d[field] for t, d in data.items()}).sort_index()
    px = px[px.index >= pd.Timestamp(start)]
    # Remove impossible prints (zero / negative) and forward-fill short gaps only.
    px = px.where(px > 0).ffill(limit=5)
    return px


def synthetic_prices(n_assets: int = 10, n_days: int = 2000, seed: int = 0) -> pd.DataFrame:
    """Random-walk prices for offline tests (no edge by construction)."""
    rng = np.random.default_rng(seed)
    idx = pd.bdate_range("2015-01-01", periods=n_days)
    rets = rng.normal(0.0003, 0.02, size=(n_days, n_assets))
    return pd.DataFrame(100 * np.exp(np.cumsum(rets, axis=0)), index=idx,
                        columns=[f"A{i}" for i in range(n_assets)])
