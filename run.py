"""quant_lab command line.

  python run.py --list                         list strategies and hypotheses
  python run.py --hypothesis H001              validate one registered hypothesis
  python run.py --all                          validate every active hypothesis
  python run.py --strategy xs_momentum --universe bist30 [--start 2012-01-01]
                                               ad-hoc test (not written to the decision registry)
  python run.py --synthetic                    offline smoke test on random-walk data
Options: --telegram  send a summary (needs TELEGRAM_TOKEN and CHAT_ID env vars)
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path

import yaml

from lab import data, decision, validation
from lab.engine import Costs
from lab.strategies import REGISTRY

ROOT = Path(__file__).resolve().parent
RESULTS = ROOT / "results"


def load_yaml(p: str):
    return yaml.safe_load((ROOT / p).read_text())


def universe(name: str) -> dict:
    u = load_yaml("config/universes.yaml")
    if name not in u:
        sys.exit(f"Unknown universe '{name}'. Known: {sorted(u)}")
    return u[name]


def report_md(hid: str, meta: dict, rep: dict, targets: dict) -> str:
    o, b = rep["oos"], rep["benchmark"]
    icon = {"ACCEPT": "✅", "WATCH": "🟡", "REJECT": "❌"}[rep["verdict"]]
    lines = [
        f"# {hid} — {meta['strategy']} on {meta['universe']}  {icon} {rep['verdict']}",
        "",
        f"- Source: {rep['source']}",
        f"- For system: `{meta.get('for_system', '-')}`",
        f"- Data: {rep['data_start']} → {rep['data_end']}, {rep['n_assets']} assets",
        f"- Costs/side: commission {rep['costs']['commission']}, slippage {rep['costs']['slippage']}",
        f"- Parameter trials (for DSR): {rep['n_trials']}",
        "",
        "## Walk-forward out-of-sample",
        "| Metric | Strategy | Equal-weight benchmark |",
        "|---|---|---|",
    ]
    for k in ["years", "cagr", "vol", "sharpe", "sortino", "max_dd", "calmar"]:
        lines.append(f"| {k} | {o.get(k)} | {b.get(k)} |")
    lines += [
        "",
        f"- Deflated Sharpe (prob.): **{rep['dsr']}**",
        f"- PSR: {o.get('psr')} · Info ratio: {o.get('info_ratio')} · Beta: {o.get('beta')}",
        f"- Sharpe with 2× costs: {rep['stress_2x_cost']['sharpe']}",
        f"- Bootstrap: {rep['bootstrap']}",
        f"- Yearly OOS Sharpe: {rep['yearly_sharpe']}",
        "",
        "## Verdict reasons",
        *[f"- {r}" for r in rep["reasons"]],
        "",
        "## Current parameters and target weights",
        f"`{rep['current_params']}`",
        "",
        "```json", json.dumps(targets, indent=1), "```",
        "",
        "> Survivorship bias: universes use today's members. Treat results as an upper bound.",
    ]
    return "\n".join(lines)


def telegram(text: str) -> None:
    tok, chat = os.environ.get("TELEGRAM_TOKEN"), os.environ.get("CHAT_ID")
    if not tok or not chat:
        print("[telegram] TELEGRAM_TOKEN/CHAT_ID not set, skipped")
        return
    body = urllib.parse.urlencode({"chat_id": chat, "text": text[:4000]}).encode()
    try:
        urllib.request.urlopen(f"https://api.telegram.org/bot{tok}/sendMessage", body, timeout=15)
    except Exception as e:  # noqa: BLE001
        print(f"[telegram] failed: {e}")


def run_one(hid: str, meta: dict, write_registry: bool, synthetic: bool = False) -> dict:
    u = universe(meta["universe"]) if not synthetic else {"costs": {}, "tickers": []}
    costs = Costs(**u.get("costs", {}))
    if synthetic:
        prices = data.synthetic_prices()
    else:
        prices = data.load_prices(u["tickers"], meta.get("start", "2012-01-01"))
    prices = prices.dropna(axis=1, how="all")
    if prices.shape[1] == 0 or len(prices) < 600:
        print(f"[{hid}] not enough data ({prices.shape}) — skipped")
        return {"verdict": "NO_DATA"}
    rep = validation.validate(meta["strategy"], prices, costs,
                              train_years=float(meta.get("train_years", 3)),
                              test_months=int(meta.get("test_months", 6)))
    targets = validation.current_targets(meta["strategy"], prices, rep["current_params"])
    RESULTS.mkdir(exist_ok=True)
    stem = f"{hid}_{meta['strategy']}_{meta['universe']}"
    (RESULTS / f"{stem}.md").write_text(report_md(hid, meta, rep, targets))
    rep["_oos_returns"].rename("oos_return").to_csv(RESULTS / f"{stem}_oos.csv")
    clean = {k: v for k, v in rep.items() if not k.startswith("_")}
    (RESULTS / f"{stem}.json").write_text(json.dumps(clean, indent=2, default=str))
    if write_registry:
        decision.record(hid, meta, rep, targets)
    o = rep["oos"]
    print(f"[{hid}] {rep['verdict']}  OOS Sharpe={o.get('sharpe')} CAGR={o.get('cagr')} "
          f"MaxDD={o.get('max_dd')} DSR={rep['dsr']}")
    return rep


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--hypothesis")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--strategy")
    ap.add_argument("--universe")
    ap.add_argument("--start", default="2012-01-01")
    ap.add_argument("--synthetic", action="store_true")
    ap.add_argument("--telegram", action="store_true")
    a = ap.parse_args()

    hyps = load_yaml("hypotheses/registry.yaml") or []
    if a.list:
        print("Strategies:")
        for n, s in sorted(REGISTRY.items()):
            print(f"  {n:15s} grid={s.grid}  [{s.source}]")
        print("Universes:", ", ".join(load_yaml("config/universes.yaml")))
        print("Hypotheses:")
        for h in hyps:
            print(f"  {h['id']} {h['strategy']} / {h['universe']} -> {h.get('for_system')} [{h['status']}]")
        return

    results = {}
    if a.synthetic:
        results["SYN"] = run_one("SYN", {"strategy": a.strategy or "xs_momentum", "universe": "synthetic"},
                                 write_registry=False, synthetic=True)
    elif a.strategy and a.universe:
        meta = {"strategy": a.strategy, "universe": a.universe, "start": a.start}
        results["ADHOC"] = run_one(f"ADHOC_{date.today():%Y%m%d}", meta, write_registry=False)
    else:
        todo = [h for h in hyps if h.get("status") == "active"]
        if a.hypothesis:
            todo = [h for h in hyps if h["id"] == a.hypothesis]
            if not todo:
                sys.exit(f"Unknown hypothesis {a.hypothesis}")
        elif not a.all:
            ap.print_help()
            return
        for h in todo:
            try:
                results[h["id"]] = run_one(h["id"], h, write_registry=True)
            except Exception as e:  # noqa: BLE001 - one bad hypothesis must not stop the batch
                print(f"[{h['id']}] ERROR {e}")
                results[h["id"]] = {"verdict": "ERROR", "reasons": [str(e)]}

    if a.telegram and results:
        icon = {"ACCEPT": "✅", "WATCH": "🟡", "REJECT": "❌"}
        msg = ["🧪 quant_lab validation"]
        for hid, r in results.items():
            o = r.get("oos", {})
            msg.append(f"{icon.get(r.get('verdict'), '⚠️')} {hid} {r.get('strategy', '')} "
                       f"SR={o.get('sharpe')} DD={o.get('max_dd')} DSR={r.get('dsr')}")
        telegram("\n".join(msg))


if __name__ == "__main__":
    main()
