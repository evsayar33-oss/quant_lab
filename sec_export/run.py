"""Geçici: us_f1_bot araştırması için SEC SUE ve GP/A (point-in-time) verisini çıkarır."""
import json, os, sys
import pandas as pd
sys.path.insert(0, os.path.dirname(__file__))
import sec_fundamentals as SF
m = pd.read_csv(os.path.join(os.path.dirname(__file__), "sp500_membership.csv.gz"))
m = m[m["date"] >= "2009-12-01"]
tick = sorted({x.strip().upper().replace(".", "-") for s in m["tickers"] for x in str(s).split(",") if x.strip()})
res, miss = SF.download_all(tick, cache_dir="/tmp/sec")
print(len(res), "ok", len(miss), "eksik")
json.dump(res, open(os.path.join(os.path.dirname(__file__), "sec_parsed.json"), "w"))
