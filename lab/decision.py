"""Decision registry: the single source of truth the trading bots read.

decisions/registry.json
{
  "updated": "...",
  "hypotheses": {
     "H001": {"verdict": "ACCEPT", "strategy": ..., "universe": ..., "for_system": ...,
              "params": {...}, "targets": {"THYAO.IS": 0.2, ...}, "oos": {...}, ...}
  }
}

A bot reads it from:
  https://raw.githubusercontent.com/<owner>/quant_lab/main/decisions/registry.json
and acts ONLY on entries with verdict == "ACCEPT" (see lab/client.py).
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REG = ROOT / "decisions" / "registry.json"
HISTORY = ROOT / "decisions" / "history.csv"


def load() -> dict:
    if REG.exists():
        return json.loads(REG.read_text())
    return {"updated": None, "hypotheses": {}}


def record(hid: str, meta: dict, report: dict, targets: dict) -> dict:
    reg = load()
    prev = reg["hypotheses"].get(hid, {}).get("verdict")
    entry = {
        "verdict": report["verdict"],
        "previous_verdict": prev,
        "reasons": report["reasons"],
        "strategy": meta.get("strategy") or meta.get("rule"),
        "kind": report["kind"],
        "universe": meta["universe"],
        "for_system": meta.get("for_system"),
        "variant": report["final_variant"],
        "params": report["final_params"],
        "targets": targets if report["verdict"] == "ACCEPT" else {},
        "targets_observe_only": targets,
        "pbo": report["pbo"],
        "trade_stats": report["trade_stats"],
        "regimes": report["regimes"],
        "oos": report["oos"],
        "dsr": report["dsr"],
        "n_trials": report["n_trials"],
        "bootstrap": report["bootstrap"],
        "validated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "data_end": report["data_end"],
    }
    reg["hypotheses"][hid] = entry
    reg["updated"] = entry["validated_at"]
    REG.parent.mkdir(parents=True, exist_ok=True)
    REG.write_text(json.dumps(reg, indent=2, ensure_ascii=False, default=str))
    new = not HISTORY.exists()
    with HISTORY.open("a") as f:
        if new:
            f.write("validated_at,id,strategy,universe,verdict,oos_sharpe,dsr,oos_cagr,oos_maxdd\n")
        o = report["oos"]
        f.write(f"{entry['validated_at']},{hid},{entry['strategy']},{meta['universe']},{entry['verdict']},"
                f"{o.get('sharpe')},{report['dsr']},{o.get('cagr')},{o.get('max_dd')}\n")
    return entry
