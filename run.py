"""quant_lab command line.

  python run.py --list                          catalog: strategies, rules, filters, exits, universes, hypotheses
  python run.py --hypothesis H001               validate one registered hypothesis (writes the decision)
  python run.py --all                           validate every active hypothesis
  python run.py --strategy xs_momentum --universe bist30           ad-hoc weight strategy (no decision)
  python run.py --rule rsi_reversal --universe bist30 [--filters all] [--exits all] [--side both]
                                                ad-hoc entry/exit rule (no decision)
  python run.py --scan --universe bist30 [--families all|rules|strategies|factors] [--filters none,trend_sma200]
                                                try everything, rank honestly, suggest hypotheses
  python run.py --synthetic [--rule NAME | --strategy NAME]        offline smoke test
Options: --start YYYY-MM-DD  --telegram (needs TELEGRAM_TOKEN, CHAT_ID)
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

from lab import data, decision, rules, validation
from lab.engine import Costs
from lab.panel import Panel
from lab.strategies import REGISTRY
from lab.trade_engine import EXIT_GRID

ROOT = Path(__file__).resolve().parent
RESULTS = ROOT / "results"
ICON = {"ACCEPT": "✅", "WATCH": "🟡", "REJECT": "❌", "NO_DATA": "⚪", "ERROR": "⚠️", "DEGRADED": "🔻"}


def load_yaml(p: str):
    return yaml.safe_load((ROOT / p).read_text())


def universe(name: str) -> dict:
    u = load_yaml("config/universes.yaml")
    if name not in u:
        sys.exit(f"Unknown universe '{name}'. Known: {sorted(u)}")
    return u[name]


def get_panel(spec: dict, synthetic: bool) -> tuple[Panel, Costs]:
    if synthetic:
        return Panel.from_close(data.synthetic_prices(15, 2600, seed=11)), Costs()
    u = universe(spec["universe"])
    tf = spec.get("timeframe", "1d")
    p = data.load_panel(u, spec.get("start", "2012-01-01"), spec["universe"], timeframe=tf)
    return p, Costs(**u.get("costs", {}))


def _fmt_dict(d) -> str:
    return json.dumps(d, default=str, ensure_ascii=False)


def report_md(hid: str, spec: dict, rep: dict, charts: dict) -> str:
    o, b = rep["oos"], rep["benchmark"]
    what = spec.get("rule") or spec.get("strategy")
    L = [
        f"# {hid} — {what} on {spec.get('universe', 'synthetic')} [{rep['timeframe']}]  {ICON[rep['verdict']]} {rep['verdict']}",
        "",
        f"- Kind: {rep['kind']} · Source: {rep['source']}",
        f"- For system: `{spec.get('for_system', '-')}`",
        f"- Data: {rep['data_start']} → {rep['data_end']} · {rep['n_assets']} assets · {rep['bars_per_year']} bars/year"
        f" · survivorship mask: {rep['survivorship_mask']}",
        f"- Costs: {rep['costs']}",
        f"- Variants tried (DSR trials): {rep['n_trials']} (failed: {rep['failed_variants']})",
        f"- Final variant: `{rep['final_variant']}`",
        "",
        "## Verdict reasons", *[f"- {r}" for r in rep["reasons"]],
        "",
        "## Walk-forward out-of-sample",
    ]
    if charts.get("equity"):
        L += [f"![equity](charts/{charts['equity']})", ""]
    L += ["| Metric | Strategy | Equal-weight benchmark |", "|---|---|---|",
          *[f"| {k} | {o.get(k)} | {b.get(k)} |" for k in
            ["years", "cagr", "vol", "sharpe", "sharpe_excess_rf", "sortino", "max_dd", "max_dd_bars", "calmar",
             "ulcer", "var95", "cvar95", "omega", "tail_ratio", "skew", "kurtosis", "hit_rate", "turnover_ann"]],
          "",
          f"- **Gate Sharpe ({rep['gate_sharpe_basis']}): {rep['gate_sharpe']}**",
          f"- Deflated Sharpe: **{rep['dsr']}** · PBO: **{rep['pbo']}** · Reality Check p: **{rep['reality_check_p']}**",
          f"- PSR {o.get('psr')} · Info ratio {o.get('info_ratio')} · Beta {o.get('beta')} · Up/Down capture {o.get('up_capture')}/{o.get('down_capture')}",
          f"- Sharpe with 2× costs: {rep['stress_2x_cost']['sharpe']} · Walk-forward efficiency: {rep['wf_efficiency']}",
          f"- Bootstrap: {rep['bootstrap']}",
          f"- Yearly OOS Sharpe: {rep['yearly_sharpe']}"]
    if rep.get("oos_usd"):
        u = rep["oos_usd"]
        L.append(f"- In USD: CAGR {u['cagr']} · Sharpe {u['sharpe']} · excess-rf Sharpe {u['sharpe_excess_rf']} · MaxDD {u['max_dd']}")
    if charts.get("monthly"):
        L += ["", f"![monthly](charts/{charts['monthly']})"]
    L += ["", "## Regimes (where does it work?)", f"`{_fmt_dict(rep['regimes'])}`",
          "", "## Calendar profile (weekday / month / hour)", f"`{_fmt_dict(rep['calendar'])}`"]
    if rep.get("trade_stats"):
        L += ["", "## Trades (OOS)", f"`{_fmt_dict(rep['trade_stats'])}`"]
    if rep.get("robustness"):
        L += ["", "## Robustness"] + [f"- **{k}**: `{_fmt_dict(v)}`" for k, v in rep["robustness"].items()]
    st = rep.get("studies") or {}
    if st:
        L += ["", "## Timing, take-profit, stop-loss and profit studies (in-sample diagnostics)"]
        if "event_study_long" in st:
            L.append(f"- Event study (forward return by bars held): `{_fmt_dict(st['event_study_long'])}`")
            if charts.get("hold"):
                L.append(f"![hold](charts/{charts['hold']})")
        if "event_study_short" in st:
            L.append(f"- Event study short: `{_fmt_dict(st['event_study_short'])}`")
        if "exit_grid_long" in st:
            L.append(f"- Best stop / target / max-hold combinations: `{_fmt_dict(st['exit_grid_long'].get('top', [])[:5])}`")
            if charts.get("exit"):
                L.append(f"![exit](charts/{charts['exit']})")
        if "overlays" in st:
            L.append(f"- Portfolio overlays (vol target, drawdown brake, equity-curve filter): `{_fmt_dict(st['overlays'])}`")
        L.append("> Studies are in-sample diagnostics. To use a better exit, register it (exits: [...]) and let the gate judge it.")
    L += ["", "## Walk-forward windows", *[f"- {w['test_start']} → {w['test_end']}: IS {w['is_sharpe']} / OOS {w['oos_sharpe']} — `{w['variant']}`" for w in rep["walk_forward"][-12:]],
          "", "## Best variants (full sample, reference only)",
          *[f"- {r['variant']}: Sharpe {r['sharpe']}" for r in rep["full_sample_top"][:10]],
          "", "## Current targets / signals", "```json", json.dumps(rep["targets"], indent=1, default=str), "```",
          "", "> Survivorship bias: unless a membership mask is used, universes are today's members (upper-bound results)."]
    return "\n".join(L)


def telegram(text: str) -> None:
    tok, chat = os.environ.get("TELEGRAM_TOKEN"), os.environ.get("CHAT_ID")
    if not tok or not chat:
        print("[telegram] TELEGRAM_TOKEN/CHAT_ID not set, skipped")
        return
    for i in range(0, len(text), 3900):
        body = urllib.parse.urlencode({"chat_id": chat, "text": text[i:i + 3900]}).encode()
        try:
            urllib.request.urlopen(f"https://api.telegram.org/bot{tok}/sendMessage", body, timeout=15)
        except Exception as e:  # noqa: BLE001
            print(f"[telegram] failed: {e}")


def make_charts(stem: str, rep: dict) -> dict:
    from lab import charts as CH, metrics
    out = {}
    d = RESULTS / "charts"
    d.mkdir(parents=True, exist_ok=True)
    try:
        r = rep["_oos_returns"]
        if len(r) > 30:
            out["equity"] = CH.equity_dd(r, rep.get("_bench_oos"), d / f"{stem}_equity.png", f"{stem} — OOS equity")
            if rep["timeframe"] in ("1d", "1h", "4h", "1w"):
                out["monthly"] = CH.monthly_heatmap(metrics.monthly_table(r), d / f"{stem}_monthly.png")
        es = (rep.get("studies") or {}).get("event_study_long")
        if es:
            out["hold"] = CH.holding_curve(es, d / f"{stem}_hold.png")
        if rep.get("_exit_table") is not None:
            out["exit"] = CH.exit_heatmap(rep["_exit_table"], d / f"{stem}_exit.png")
    except Exception as e:  # noqa: BLE001 - charts must never break a validation
        print(f"[charts] {e}")
    return {k: v for k, v in out.items() if v}


def run_one(hid: str, spec: dict, write_registry: bool, synthetic: bool = False) -> dict:
    p, costs = get_panel(spec, synthetic)
    p.c = p.c.dropna(axis=1, how="all")
    if p.c.shape[1] == 0 or len(p.c) < 600:
        print(f"[{hid}] not enough data ({p.c.shape}) — skipped")
        return {"verdict": "NO_DATA", "reasons": ["not enough price history"]}
    rep = validation.validate(spec, p, costs, float(spec.get("train_years", 3)), int(spec.get("test_months", 6)))
    RESULTS.mkdir(exist_ok=True)
    stem = f"{hid}_{spec.get('rule') or spec.get('strategy')}_{spec.get('universe', 'synthetic')}_{spec.get('timeframe', '1d')}"
    charts = make_charts(stem, rep)
    (RESULTS / f"{stem}.md").write_text(report_md(hid, spec, rep, charts))
    rep["_oos_returns"].rename("oos_return").to_csv(RESULTS / f"{stem}_oos.csv")
    clean = {k: v for k, v in rep.items() if not k.startswith("_")}
    (RESULTS / f"{stem}.json").write_text(json.dumps(clean, indent=2, default=str))
    if write_registry:
        decision.record(hid, spec, rep, rep["targets"], oos_csv=f"results/{stem}_oos.csv")
    o = rep["oos"]
    print(f"[{hid}] {rep['verdict']}  OOS Sharpe={o.get('sharpe')} CAGR={o.get('cagr')} MaxDD={o.get('max_dd')} "
          f"DSR={rep['dsr']} PBO={rep['pbo']} trials={rep['n_trials']}")
    return rep


def summary_text(reg: dict) -> str:
    lines = ["🧭 quant_lab decisions"]
    for hid, h in sorted(reg["hypotheses"].items()):
        lines.append(f"{ICON.get(h['verdict'], '🔻')} {hid} {h['strategy']} {h['universe']}/{h.get('timeframe')} "
                     f"SR {h.get('gate_sharpe')} DSR {h.get('dsr')} → {h.get('for_system')}")
    for s, v in reg.get("systems", {}).items():
        lines.append(f"🤖 {s}: {v['allocation']} ({v['method']})")
    return "\n".join(lines)


def do_scan(a) -> None:
    from lab import scanner
    filters = [f for f in a.filters.split(",") if f] if a.filters != "all" else list(rules.FILTERS)
    spec = {"universe": a.universe or "synthetic", "start": a.start, "timeframe": a.timeframe}
    p, costs = get_panel(spec, a.synthetic)
    names = a.rules.split(",") if a.rules else None
    res = scanner.scan(p, costs, a.families, filters, a.side, names)
    RESULTS.mkdir(exist_ok=True)
    stem = f"scan_{spec['universe']}_{a.timeframe}_{a.families}"
    (RESULTS / f"{stem}.md").write_text(scanner.to_markdown(res) + "\n\n```yaml\n" +
                                        scanner.suggest_yaml(res, spec["universe"]) + "\n```\n")
    res["board"].to_csv(RESULTS / f"{stem}.csv", index=False)
    res["variants"].to_csv(RESULTS / f"{stem}_variants.csv", index=False)
    print(scanner.to_markdown(res, top=15))
    if a.telegram:
        top = res["board"].head(10)
        msg = [f"🔎 Scan {spec['universe']} — {res['n_trials']} variants, PBO {res['global_pbo']}, "
               f"bench SR {res['benchmark_sharpe']}"]
        msg += [f"{i}. {r.family} OOS SR {r.wf_oos_sharpe} DD {r.wf_oos_maxdd}" for i, r in enumerate(top.itertuples(), 1)]
        telegram("\n".join(msg))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--hypothesis")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--strategy")
    ap.add_argument("--rule")
    ap.add_argument("--universe")
    ap.add_argument("--start", default="2012-01-01")
    ap.add_argument("--timeframe", default="1d", help="1h | 4h | 1d | 1w | 1mo")
    ap.add_argument("--filters", default="none")
    ap.add_argument("--exits", default="")
    ap.add_argument("--side", default="long")
    ap.add_argument("--scan", action="store_true")
    ap.add_argument("--families", default="all")
    ap.add_argument("--rules", default="")
    ap.add_argument("--synthetic", action="store_true")
    ap.add_argument("--telegram", action="store_true")
    ap.add_argument("--ids", action="store_true", help="print active hypothesis ids as JSON (workflow matrix)")
    ap.add_argument("--merge", action="store_true", help="rebuild decisions/registry.json from parts")
    ap.add_argument("--live", action="store_true", help="paper-track ACCEPT decisions, demote on decay")
    ap.add_argument("--prefetch", action="store_true",
                    help="download & cache all data needed by active hypotheses (or --universe/--timeframe)")
    a = ap.parse_args()

    hyps = load_yaml("hypotheses/registry.yaml") or []
    if a.ids:
        print(json.dumps([h["id"] for h in hyps if h.get("status") == "active"]))
        return
    if a.prefetch:
        want = [(a.universe, a.timeframe, a.start)] if a.universe else sorted(
            {(h["universe"], h.get("timeframe", "1d"), h.get("start", "2012-01-01")) for h in hyps
             if h.get("status") == "active" and (not a.hypothesis or h["id"] in a.hypothesis.split(","))})
        for uni, tf, st in want:
            try:
                p = data.load_panel(universe(uni), st, uni, timeframe=tf)
                print(f"[prefetch] {uni} {tf}: {p.c.shape} fund={len(p.fund)} macro={list(p.macro)}")
            except Exception as e:  # noqa: BLE001
                print(f"[prefetch] {uni} {tf} failed: {e}")
        return
    if a.merge:
        reg = decision.merge()
        print(json.dumps({k: v["verdict"] for k, v in reg["hypotheses"].items()}, indent=1))
        print(json.dumps(reg["systems"], indent=1, default=str))
        if a.telegram:
            telegram(summary_text(reg))
        return
    if a.live:
        from lab import live
        st = live.run([h for h in hyps if h.get("status") == "active"])
        if a.telegram and st:
            telegram("📡 quant_lab live tracking\n" + "\n".join(
                f"{'🔻' if v['degraded'] else '🟢'} {k} live {v['live_return']:+.1%} SR {v['live_sharpe']} — {v['why']}"
                for k, v in st.items()))
        return
    if a.list:
        print(f"Weight strategies ({len(REGISTRY)}):")
        for n, s in sorted(REGISTRY.items()):
            print(f"  {n:24s} [{s.kind}] grid={s.grid}  — {s.source}")
        print(f"\nEntry/exit rules ({len(rules.RULES)}, {rules.n_variants()} parameter variants):")
        for n, r in sorted(rules.RULES.items()):
            print(f"  {n:22s} [{r.family}] grid={r.grid}  — {r.source}")
        print(f"\nFilters: {', '.join(rules.FILTERS)}")
        print("Exit configs:")
        for i, e in enumerate(EXIT_GRID):
            print(f"  {i:2d} {e.label()}")
        print("\nUniverses:", ", ".join(load_yaml("config/universes.yaml")))
        print("Hypotheses:")
        for h in hyps:
            print(f"  {h['id']} {h.get('rule') or h.get('strategy')} / {h['universe']} -> {h.get('for_system')} [{h['status']}]")
        return

    if a.scan:
        if not (a.universe or a.synthetic):
            sys.exit("--scan needs --universe")
        return do_scan(a)

    results = {}
    if a.synthetic or (a.universe and (a.strategy or a.rule)):
        spec = {"universe": a.universe or "synthetic", "start": a.start, "timeframe": a.timeframe}
        if a.rule:
            spec.update({"rule": a.rule, "side": a.side,
                         "filters": "all" if a.filters == "all" else a.filters.split(","),
                         "exits": "all" if a.exits == "all" else ([int(x) for x in a.exits.split(",")] if a.exits else None)})
        else:
            spec["strategy"] = a.strategy or "xs_momentum"
        hid = "SYN" if a.synthetic else f"ADHOC_{date.today():%Y%m%d}"
        results[hid] = run_one(hid, spec, write_registry=False, synthetic=a.synthetic)
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
                import traceback
                traceback.print_exc()
                print(f"[{h['id']}] ERROR {e}")
                results[h["id"]] = {"verdict": "ERROR", "reasons": [str(e)]}
        decision.merge()

    if a.telegram and results:
        msg = ["🧪 quant_lab validation"]
        for hid, r in results.items():
            o = r.get("oos", {})
            msg.append(f"{ICON.get(r.get('verdict'), '⚠️')} {hid} {r.get('name', '')} "
                       f"SR={o.get('sharpe')} DD={o.get('max_dd')} DSR={r.get('dsr')} PBO={r.get('pbo')}")
        telegram("\n".join(msg))


if __name__ == "__main__":
    main()
