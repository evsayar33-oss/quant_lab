"""Panel: the container every strategy receives.

  panel.o / .h / .l / .c / .v   wide OHLCV frames (dates x assets)
  panel.bench                   benchmark close (Series) or None
  panel.fund                    dict[field] -> wide point-in-time fundamental frame (may be empty)
"""
from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
import pandas as pd


@dataclass
class Panel:
    o: pd.DataFrame
    h: pd.DataFrame
    l: pd.DataFrame
    c: pd.DataFrame
    v: pd.DataFrame
    bench: pd.Series | None = None
    fund: dict = field(default_factory=dict)
    name: str = ""

    @property
    def index(self):
        return self.c.index

    @property
    def columns(self):
        return self.c.columns

    def slice(self, end) -> "Panel":
        s = lambda x: x.loc[:end] if x is not None else None  # noqa: E731
        return Panel(s(self.o), s(self.h), s(self.l), s(self.c), s(self.v), s(self.bench),
                     {k: s(v) for k, v in self.fund.items()}, self.name)

    @staticmethod
    def from_ohlcv(data: dict[str, pd.DataFrame], bench: pd.Series | None = None, name: str = "") -> "Panel":
        def wide(col):
            return pd.DataFrame({t: d[col] for t, d in data.items()}).sort_index()
        c = wide("Close")
        c = c.where(c > 0).ffill(limit=5)
        o, h, l = (wide(k).reindex(c.index) for k in ("Open", "High", "Low"))
        # Repair missing/invalid OHLC with the close so stops never see NaN highs/lows.
        o = o.where(o > 0, c); h = h.where(h > 0, c); l = l.where(l > 0, c)
        h = np.maximum(h, np.maximum(o, c)); l = np.minimum(l, np.minimum(o, c))
        v = wide("Volume").reindex(c.index).fillna(0)
        if bench is not None:
            bench = bench.reindex(c.index).ffill()
        return Panel(o.where(c.notna()), h.where(c.notna()), l.where(c.notna()), c, v, bench, {}, name)

    @staticmethod
    def from_close(c: pd.DataFrame, seed: int = 0, name: str = "synthetic") -> "Panel":
        """Build a plausible OHLCV panel from closes (for offline tests)."""
        rng = np.random.default_rng(seed)
        prev = c.shift(1).fillna(c)
        o = prev * (1 + rng.normal(0, 0.003, c.shape))
        spread = np.abs(rng.normal(0, 0.008, c.shape))
        h = np.maximum(o, c) * (1 + spread)
        l = np.minimum(o, c) * (1 - spread)
        v = pd.DataFrame(rng.lognormal(13, 0.4, c.shape), index=c.index, columns=c.columns)
        return Panel(o, h, l, c, v, c.mean(axis=1), {}, name)
