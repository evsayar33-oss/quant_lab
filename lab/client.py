"""Drop-in client for the trading bots (copy this one file into a bot repo).

Usage in a bot:
    from quant_lab_client import approved
    for h in approved(system="bist_orderflow_quant"):
        print(h["id"], h["strategy"], h["targets"])

Only ACCEPT verdicts are returned. If the registry cannot be fetched or is stale,
it returns [] -> the bot must fall back to its own default (fail-safe, never fail-open).
"""
from __future__ import annotations

import json
import urllib.request
from datetime import datetime, timedelta, timezone

URL = "https://raw.githubusercontent.com/evsayar33-oss/quant_lab/main/decisions/registry.json"
MAX_AGE_DAYS = 10


def fetch(url: str = URL, timeout: int = 15) -> dict | None:
    try:
        with urllib.request.urlopen(url, timeout=timeout) as r:
            return json.loads(r.read().decode())
    except Exception as e:  # noqa: BLE001
        print(f"[quant_lab] registry fetch failed: {e}")
        return None


def approved(system: str | None = None, url: str = URL) -> list[dict]:
    reg = fetch(url)
    if not reg:
        return []
    out = []
    now = datetime.now(timezone.utc)
    for hid, h in reg.get("hypotheses", {}).items():
        if h.get("verdict") != "ACCEPT":
            continue
        if system and h.get("for_system") != system:
            continue
        try:
            age = now - datetime.fromisoformat(h["validated_at"])
        except Exception:  # noqa: BLE001
            continue
        if age > timedelta(days=MAX_AGE_DAYS):
            print(f"[quant_lab] {hid} is stale ({age.days}d) -> ignored")
            continue
        out.append({"id": hid, **h})
    return out
