"""Download free 1H data for the Pine ports. BTC: ccxt (okx -> kucoin -> bitget). XAU: dukascopy CSV (made by npx) or yfinance GC=F."""
import sys
from pathlib import Path

import pandas as pd

D = Path(__file__).resolve().parents[2] / "results" / "pine_ports" / "data"
D.mkdir(parents=True, exist_ok=True)


def btc(start="2019-01-01"):
    import ccxt
    since0 = int(pd.Timestamp(start, tz="UTC").timestamp() * 1000)
    for ex_id in ("okx", "kucoin", "bitget", "gate"):
        try:
            ex = getattr(ccxt, ex_id)({"enableRateLimit": True})
            rows, since = [], since0
            for _ in range(5000):
                b = ex.fetch_ohlcv("BTC/USDT", "1h", since=since, limit=100 if ex_id == "okx" else 1000)
                if not b:
                    break
                rows += b
                nxt = b[-1][0] + 3600_000
                if nxt <= since:
                    break
                since = nxt
            df = pd.DataFrame(rows, columns=["ts", "Open", "High", "Low", "Close", "Volume"]).drop_duplicates("ts")
            df.index = pd.to_datetime(df.pop("ts"), unit="ms")
            print(ex_id, len(df), df.index.min(), df.index.max())
            if len(df) and df.index.min() < pd.Timestamp(start) + pd.Timedelta(days=60):
                df.sort_index().to_csv(D / "btc_1h.csv")
                return
        except Exception as e:  # noqa: BLE001
            print(ex_id, "failed", e)
    sys.exit("no BTC data")


def xau():
    parts = []
    for f in sorted(Path("dukas").glob("*.csv")):
        if f.stat().st_size > 100:
            parts.append(pd.read_csv(f))
    if parts:
        df = pd.concat(parts)
        df.index = pd.to_datetime(df.pop("timestamp"), unit="ms")
        df = df[~df.index.duplicated()].sort_index().rename(columns=str.capitalize)
        print("dukascopy", len(df), df.index.min(), df.index.max())
        if len(df) > 5000:
            df.to_csv(D / "xau_1h.csv")
            return
    import yfinance as yf
    df = yf.download("GC=F", period="730d", interval="1h", auto_adjust=False, progress=False)
    df.columns = [c[0] if isinstance(c, tuple) else c for c in df.columns]
    print("yfinance GC=F", len(df), df.index.min(), df.index.max())
    df[["Open", "High", "Low", "Close", "Volume"]].to_csv(D / "xau_1h.csv")


if __name__ == "__main__":
    {"btc": btc, "xau": xau}[sys.argv[1]]()
