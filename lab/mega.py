"""H062 mega multi-asset screen. Thresholds: config/mega.yaml (pre-registered, fixed).

One STRATEGY = one rule + one parameter set + one exit (R:R) + one side + one filter (+ optional
confirmation rule). It is applied with the SAME settings to every asset of a class (crypto, index
futures, metals, energy). A strategy that works on one coin only is luck; this screen asks for the
same settings to work on most assets of the class.

Data split: the last `holdout_years` are locked. Every selection step (D1-D5) uses only the bars
before the cut. The job stores the holdout result of its candidates in a sealed field; only the
aggregate step reads it, and only for the finalists that passed D1-D5.

Usage:
  python -m lab.mega job --cls metals --side long --out parts/metals_long.json [--synthetic]
  python -m lab.mega aggregate --parts parts --out decisions/mega/result.json --md results/mega_screen.md
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import date
from pathlib import Path

import numpy as np
import pandas as pd
import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from lab import metrics, perp, rules, screen  # noqa: E402
from lab.engine import Costs  # noqa: E402

_G: dict = {}


def cfg_load() -> dict:
    return yaml.safe_load((ROOT / "config" / "mega.yaml").read_text())


# ------------------------------------------------------------------ data
def load_class(cls: str, cfg: dict, synthetic: bool = False):
    if synthetic:   # random walks: no edge by construction (for tests and smoke runs)
        from lab.panel import Panel
        rng = np.random.default_rng(abs(hash(cls)) % 2**32)
        idx = pd.bdate_range("2012-01-02", periods=3200)
        cols = [f"{cls[:3].upper()}{i}" for i in range(6)]
        c = pd.DataFrame(100 * np.exp(np.cumsum(rng.normal(0.0002, 0.012, (len(idx), len(cols))), axis=0)), idx, cols)
        p = Panel.from_close(c, seed=1)
        p.freq, p.market = "1d", "multi"
        return p, Costs(0.0002, 0.0005)
    from lab import data
    u = yaml.safe_load((ROOT / "config" / "universes.yaml").read_text())[cfg["classes"][cls]]
    p = data.load_panel(u, (cfg.get("starts") or {}).get(cls, cfg.get("start", "2000-01-01")), cfg["classes"][cls], with_fundamentals=False,
                        timeframe=cfg.get("timeframe", "1d"))
    return p, Costs(**u.get("costs", {}))


def cut_date(p, cfg) -> pd.Timestamp:
    return p.index[-1] - pd.DateOffset(years=int(cfg["holdout_years"]))


# ------------------------------------------------------------------ one strategy on one class
def stats(R: pd.DataFrame, tr: pd.DataFrame, cut: pd.Timestamp, cps: float, ppy: float, part: str) -> dict:
    """Metrics on the discovery part (index < cut) or the holdout part (>= cut)."""
    sel = R.index < cut if part == "disc" else R.index >= cut
    Rp = R.loc[sel]
    if len(tr):
        tsel = tr["exit"] < cut if part == "disc" else tr["exit"] >= cut
        t = tr.loc[tsel]
    else:
        t = tr
    per = {}
    for a in Rp.columns:
        r = Rp[a].dropna()
        if not len(r):
            continue
        n = int((t["asset"] == a).sum()) if len(t) else 0
        ret = float((1 + r).prod() - 1)
        per[a] = {"ret": round(ret, 4), "ret_2x": round((1 + ret) * (1 - cps) ** (2 * n) - 1, 4), "trades": n}
    pool = Rp.mean(axis=1, skipna=True).dropna()
    ts = perp.trade_stats(t, cps)
    pos = [v["ret_2x"] > 0 for v in per.values()]
    return {"assets": per, "asset_share": float(np.mean(pos)) if pos else 0.0,
            "trades_per_asset": float(np.mean([v["trades"] for v in per.values()])) if per else 0.0,
            "pool_sharpe": round(metrics.sharpe(pool), 3) if len(pool) > 30 else 0.0,
            "pool_sr_bar": screen._sr_bar(pool),
            "pool_ret": round(float((1 + pool).prod() - 1), 4) if len(pool) else 0.0,
            "pool_ret_2x": round(float(np.mean([v["ret_2x"] for v in per.values()])), 4) if per else 0.0,
            "max_dd": round(metrics.max_drawdown(pool), 4) if len(pool) else 0.0,
            "pos_years": round(perp.pos_year_frac(pool, ppy), 3), **ts}


def d_checks(s: dict, d: dict) -> dict:
    return {"D1": s["asset_share"] >= d["min_asset_share"] and s["trades_per_asset"] >= d["min_trades_per_asset"],
            "D2": (s["pool_sharpe"] >= d["min_pooled_sharpe"] and (s.get("profit_factor") or 0) >= d["min_profit_factor"]
                   and s["max_dd"] >= d["max_dd_floor"] and (s.get("wr_margin") or -1) > d["min_wr_margin"]),
            "D4": s["pos_years"] >= d["min_pos_year_frac"]}


def _eval(args):
    key, spec = args
    p, side, costs, cut, cps, ppy = (_G[k] for k in ("panel", "side", "costs", "cut", "cps", "ppy"))
    try:
        R, _, tr = screen.run_spec(p, spec, side, costs)
    except Exception as e:  # noqa: BLE001
        return key, None, str(e)
    return key, stats(R, tr, cut, cps, ppy, "disc"), None


def _spec_key(spec: dict) -> str:
    c = spec.get("confirm")
    ck = f"|{c['rule']}:{json.dumps(c.get('params'), sort_keys=True)}:w{c['within']}" if c else ""
    return (f"{spec['rule']}|{json.dumps(spec['params'], sort_keys=True)}|x{spec['exit_id']}|"
            f"{spec.get('filter', 'none')}{ck}")


def _mid(grid: dict) -> dict:
    return {k: v[len(v) // 2] for k, v in (grid or {}).items()}


def job(cls: str, side: str, cfg: dict, synthetic: bool = False, rule_names: list | None = None,
        workers: int | None = None) -> dict:
    p, costs = load_class(cls, cfg, synthetic)
    ppy = p.ppy
    metrics.set_periods(ppy)
    cut = cut_date(p, cfg)
    d = cfg["discovery"]
    yrs = {a: float(p.c.loc[p.index < cut, a].notna().sum() / ppy) for a in p.columns}
    elig = [a for a, y in yrs.items() if y >= d["min_years"]]
    base = {"cls": cls, "side": side, "date": date.today().isoformat(), "data_end": str(p.index[-1].date()),
            "cut": str(cut.date()), "assets_years": {a: round(y, 1) for a, y in yrs.items()}, "eligible": elig}
    if len(elig) < d["min_assets"]:
        return {**base, "skipped": f"only {len(elig)} assets with >= {d['min_years']} years", "n_trials": 0,
                "trial_srs": [], "candidates": [], "funnel": {}}
    q = screen.subpanel(p, elig)
    _G.update(panel=q, side=side, costs=costs, cut=cut, cps=costs.per_turnover, ppy=ppy)
    names = rule_names or list(rules.RULES)

    # stage 1: every rule x grid x exit x filter
    specs, grids = {}, {}
    for rn in names:
        pts = rules.grid_points(rules.RULES[rn].grid)
        for ex in cfg["exits"]:
            for fl in cfg["filters"]:
                for gi, gp in enumerate(pts):
                    s = {"rule": rn, "params": gp, "exit_id": int(ex), "filter": fl}
                    k = _spec_key(s)
                    specs[k] = s
                    grids[k] = (rn, ex, fl, gi)
    print(f"[mega] {cls}/{side}: {len(specs)} stage-1 trials on {len(elig)} assets, cut {cut.date()}")
    res = {}
    for k, st, err in screen._pmap(_eval, list(specs.items()), workers):
        if st is not None:
            res[k] = st

    # plateau (D3): neighbours on the parameter grid with the same rule / exit / filter
    by_g = {(g[0], g[1], g[2], g[3]): k for k, g in grids.items()}
    plateau = {}
    for k, (rn, ex, fl, gi) in grids.items():
        if k not in res:
            continue
        nb = screen.neighbours(rules.RULES[rn].grid).get(gi, [])
        ks = [by_g.get((rn, ex, fl, j)) for j in nb]
        ok = [res[x]["asset_share"] >= 0.5 for x in ks if x in res]
        plateau[k] = float(np.mean(ok)) if ok else 0.0

    # stage 2: confirmations for the best D1+D2 candidates
    pre = [k for k, s in res.items() if (c := d_checks(s, d))["D1"] and c["D2"]]
    pre = sorted(pre, key=lambda k: -res[k]["pool_sharpe"])[: cfg["combos"]["top_per_job"]]
    cspecs = {}
    for k in pre:
        for cr in cfg["combos"]["confirm"]:
            if cr not in rules.RULES or cr == specs[k]["rule"]:
                continue
            for w in cfg["combos"]["within"]:
                s = {**specs[k], "confirm": {"rule": cr, "params": _mid(rules.RULES[cr].grid), "within": int(w)}}
                cspecs[_spec_key(s)] = s
    for k, st, err in screen._pmap(_eval, list(cspecs.items()), workers):
        if st is not None:
            res[k] = st
    specs.update(cspecs)
    for k, s in cspecs.items():
        if k not in res:
            continue
        sib = [_spec_key({**s, "confirm": {**s["confirm"], "within": int(w)}}) for w in cfg["combos"]["within"]
               if int(w) != s["confirm"]["within"]]
        ok = [res[x]["asset_share"] >= 0.5 for x in sib if x in res]
        base_ok = res.get(_spec_key({kk: vv for kk, vv in s.items() if kk != "confirm"}), {}).get("pool_sharpe", 0)
        # a combo counts only when it beats the rule alone (same rule as arena stage 2)
        plateau[k] = float(np.mean(ok)) if ok and res[k]["pool_sharpe"] > base_ok else 0.0

    funnel = {"trials": len(res), "D1": 0, "D2": 0, "D3": 0, "D4": 0}
    cands = []
    for k, s in res.items():
        c = d_checks(s, d)
        if not c["D1"]:
            continue
        funnel["D1"] += 1
        if not c["D2"]:
            continue
        funnel["D2"] += 1
        if plateau.get(k, 0.0) < d["min_plateau"]:
            continue
        funnel["D3"] += 1
        if not c["D4"]:
            continue
        funnel["D4"] += 1
        cands.append(k)
    cands = sorted(cands, key=lambda k: -res[k]["pool_sharpe"])[:200]

    # series for DSR (discovery) + the sealed holdout, candidates only
    out = []
    for k in cands:
        R, _, tr = screen.run_spec(q, specs[k], side, costs)
        pool = R.loc[R.index < cut].mean(axis=1, skipna=True).dropna()
        ho = stats(R, tr, cut, costs.per_turnover, ppy, "hold")
        out.append({"key": k, "spec": specs[k], "family": rules.RULES[specs[k]["rule"]].family,
                    "plateau": round(plateau[k], 3), "disc": {kk: vv for kk, vv in res[k].items()},
                    "disc_series": {"d": [str(x.date()) for x in pool.index], "r": [round(float(x), 6) for x in pool.values]},
                    "sealed_holdout": ho})
    return {**base, "n_trials": len(res), "trial_srs": [round(s["pool_sr_bar"], 5) for s in res.values()],
            "funnel": funnel, "candidates": out}


# ------------------------------------------------------------------ aggregate
def aggregate(parts: list[dict], cfg: dict) -> dict:
    n_total = sum(p_["n_trials"] for p_ in parts)
    srs = [x for p_ in parts for x in p_["trial_srs"]]
    d, h = cfg["discovery"], cfg["holdout"]
    pass4 = {}
    for p_ in parts:
        for c in p_["candidates"]:
            pass4.setdefault(f"{p_['side']}|{c['key']}", set()).add(p_["cls"])
    finals = []
    for p_ in parts:
        for c in p_["candidates"]:
            s = pd.Series(c["disc_series"]["r"], index=pd.to_datetime(c["disc_series"]["d"]))
            metrics.set_periods(252)
            dsr = metrics.dsr(s, n_total, srs)
            row = {"cls": p_["cls"], "side": p_["side"], "key": c["key"], "spec": c["spec"], "family": c["family"],
                   "plateau": c["plateau"], "dsr": round(float(dsr), 3), "disc": c["disc"],
                   "classes_d4": sorted(pass4[f"{p_['side']}|{c['key']}"])}
            row["strong"] = len(row["classes_d4"]) >= 2
            if dsr >= d["min_dsr"]:
                ho = c["sealed_holdout"]          # read ONCE, finalists only
                row["holdout"] = {k: ho[k] for k in ("pool_ret", "pool_ret_2x", "pool_sharpe", "asset_share", "max_dd",
                                                     "win_rate", "breakeven_wr", "wr_margin", "trades", "assets")}
                row["H"] = (ho["pool_ret_2x"] > h["min_return_2x"] and ho["pool_sharpe"] >= h["min_sharpe"]
                            and ho["asset_share"] >= h["min_asset_share"])
                finals.append(row)
    # luck bar: the best annual Sharpe expected from pure chance after n_total trials
    metrics.set_periods(252)
    var = float(np.var(srs, ddof=1)) if len(srs) > 1 else 0.0
    luck = round(metrics.expected_max_sharpe(n_total, var) * np.sqrt(252), 2) if n_total > 1 else None
    best = []
    for p_ in parts:
        for c in p_["candidates"]:
            s = pd.Series(c["disc_series"]["r"], index=pd.to_datetime(c["disc_series"]["d"]))
            best.append({"cls": p_["cls"], "side": p_["side"], "key": c["key"], "dsr": round(float(metrics.dsr(s, n_total, srs)), 3),
                         "pool_sharpe": c["disc"]["pool_sharpe"], "pool_ret": c["disc"]["pool_ret"], "max_dd": c["disc"]["max_dd"],
                         "win_rate": c["disc"].get("win_rate"), "breakeven_wr": c["disc"].get("breakeven_wr")})
    best = sorted(best, key=lambda r: -r["dsr"])[:15]
    near = []
    for p_ in parts:
        for c in p_["candidates"][:3]:
            near.append({"cls": p_["cls"], "side": p_["side"], "key": c["key"], "pool_sharpe": c["disc"]["pool_sharpe"],
                         "asset_share": c["disc"]["asset_share"]})
    winners = [f for f in finals if f["H"]]
    return {"date": date.today().isoformat(), "n_trials_total": n_total,
            "jobs": [{k: p_.get(k) for k in ("cls", "side", "cut", "data_end", "eligible", "skipped", "n_trials", "funnel")}
                     for p_ in parts],
            "d4_candidates": sum(len(p_["candidates"]) for p_ in parts),
            "finalists": finals, "winners": winners, "near_misses": near, "luck_sharpe": luck, "best_dsr": best,
            "verdict": ("PASSED_HOLDOUT" if winners else "NO_BETTER_FOUND")}


def markdown(o: dict, cfg: dict) -> str:
    f = lambda v: "—" if v is None else f"{v:+.0%}"   # noqa: E731
    L = ["# H062 dev tarama — tüm varlık sınıfları", "",
         f"Tarih: {o['date']}. Toplam deneme: **{o['n_trials_total']:,}** (DSR bu sayıyla hesaplandı).", "",
         "Kurallar sonuçlardan ÖNCE yazıldı: `config/mega.yaml`. Son "
         f"{cfg['holdout_years']} yıl kilitli; seçim bu dönemi hiç görmedi. Kilitli dönem sadece finalistler için bir kez okundu.", "",
         "## Huni (iş başına)", "", "| Sınıf | Yön | Kesim | Varlık | Deneme | D1 çok varlık | D2 kalite | D3 plato | D4 yıllar |",
         "|---|---|---|---|---|---|---|---|---|"]
    for j in o["jobs"]:
        fn = j.get("funnel") or {}
        L.append(f"| {j['cls']} | {j['side']} | {j.get('cut')} | {len(j.get('eligible') or [])} | {j.get('n_trials', 0):,} | "
                 f"{fn.get('D1', '—')} | {fn.get('D2', '—')} | {fn.get('D3', '—')} | {fn.get('D4', '—')} |"
                 + (f" atlandı: {j['skipped']}" if j.get("skipped") else ""))
    L += ["", f"D1–D4'ü geçen: **{o['d4_candidates']}**. D5 (DSR ≥ {cfg['discovery']['min_dsr']}) geçen finalist: "
          f"**{len(o['finalists'])}**. Kilitli dönemi de geçen: **{len(o['winners'])}**.", ""]
    if o["finalists"]:
        L += ["## Finalistler", "", "| Sınıf | Yön | Strateji | DSR | Keşif Sharpe | Keşif varlık payı | Kazanma / başabaş | "
              "Kilitli dönem 2x getiri | Kilitli Sharpe | Kilitli varlık payı | Sonuç | Güçlü |", "|---|---|---|---|---|---|---|---|---|---|---|---|"]
        for r in o["finalists"]:
            ds, ho = r["disc"], r.get("holdout") or {}
            L.append(f"| {r['cls']} | {r['side']} | `{r['key']}` | {r['dsr']} | {ds['pool_sharpe']} | {ds['asset_share']:.0%} | "
                     f"{(ds.get('win_rate') or 0):.0%} / {(ds.get('breakeven_wr') or 0):.0%} | {f(ho.get('pool_ret_2x'))} | "
                     f"{ho.get('pool_sharpe')} | {(ho.get('asset_share') or 0):.0%} | {'GEÇTİ' if r['H'] else 'KALDI'} | "
                     f"{'evet (' + ', '.join(r['classes_d4']) + ')' if r['strong'] else 'hayır'} |")
    if not o["winners"]:
        L += ["", "**Daha iyisi bulunamadı:** önceden yazılan kurala göre hiçbir strateji kilitli dönemi geçmedi. "
              "Bot kuralı (H054) değişmez."]
    else:
        L += ["", "**Kilitli dönemi geçenler hâlâ ipucudur, karar değildir.** Sonraki adım (sahibin onayıyla): "
              "hipotez olarak kaydet → karar kapısı (walk-forward, PBO, 2x maliyet) → zaman makinesi."]
    if o.get("luck_sharpe") is not None:
        L += ["", f"## Şans çizgisi", "", f"{o['n_trials_total']:,} denemede, hiçbir avantajı olmayan stratejilerden bile beklenen en iyi yıllık Sharpe "
              f"yaklaşık **{o['luck_sharpe']}**. Bir aday bu çizginin belirgin üstünde olmalı (DSR ≥ {cfg['discovery']['min_dsr']}).", "",
              "| Sınıf | Yön | Strateji | DSR | Keşif Sharpe | Keşif getiri | Düşüş | Kazanma / başabaş |", "|---|---|---|---|---|---|---|---|"]
        for r in o.get("best_dsr") or []:
            L.append(f"| {r['cls']} | {r['side']} | `{r['key']}` | {r['dsr']} | {r['pool_sharpe']} | {f(r['pool_ret'])} | {f(r['max_dd'])} | "
                     f"{(r['win_rate'] or 0):.0%} / {(r['breakeven_wr'] or 0):.0%} |")
    L += ["", "## En iyi D1–D4 adayları (DSR'ı geçmeyenler dahil, iş başına 3)", "", "| Sınıf | Yön | Strateji | Keşif Sharpe | Varlık payı |",
          "|---|---|---|---|---|"]
    for r in o["near_misses"]:
        L.append(f"| {r['cls']} | {r['side']} | `{r['key']}` | {r['pool_sharpe']} | {r['asset_share']:.0%} |")
    L += ["", "## Zayıf yönler", "",
          "- Yahoo `=F` serileri sürekli ön ay vadeli seridir; vade geçiş günlerinde küçük sıçramalar olabilir. Roll maliyeti modellenmedi.",
          "- Vadeli işlemlerde sadece günlük (1d) test var: ücretsiz kaynakta saatlik veri yalnız son 2 yıl.",
          "- Vade yapısı (carry) verisi ücretsiz değil; test edilemedi. Temel veri olarak sadece CFTC COT kullanıldı.",
          "- Kripto sınıfında 5 yıldan kısa verisi olan coinler dışarıda kaldı (listelenme yanlılığı azalır, kapsam düşer).",
          "- Sınıf başına varlık sayısı az (4–5): 'çok varlıkta çalışıyor' şartı küçük örneklemle ölçülür.", "",
          "> ⚠️ Bu bir seçim sürecidir (binlerce aday). Gerçek paraya aday olmadan önce **zaman makinesi** testi gerekir "
          "(`lab/timemachine.py`, workflow \"Time machine test\"). Kilitli dönem bu testin yerini tutmaz."]
    return "\n".join(L) + "\n"


def telegram_text(o: dict) -> str:
    t = f"🔭 H062 dev tarama: {o['n_trials_total']:,} deneme, D1–D4 {o['d4_candidates']}, finalist {len(o['finalists'])}, kilitli dönemi geçen {len(o['winners'])}."
    for w in o["winners"][:8]:
        t += f"\n✅ {w['cls']}/{w['side']} {w['key']} (kilitli 2x {w['holdout']['pool_ret_2x']:+.0%})"
    if not o["winners"]:
        t += "\nDaha iyisi bulunamadı. H054 değişmez."
    return t + "\n⚠️ Zaman makinesi kontrolü gerekli."


def main(argv=None):
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    j = sub.add_parser("job"); j.add_argument("--cls", required=True); j.add_argument("--side", required=True)
    j.add_argument("--out", required=True); j.add_argument("--synthetic", action="store_true")
    j.add_argument("--rules", default="")
    a = sub.add_parser("aggregate"); a.add_argument("--parts", required=True); a.add_argument("--out", required=True)
    a.add_argument("--md", required=True); a.add_argument("--telegram", action="store_true")
    x = ap.parse_args(argv)
    cfg = cfg_load()
    if x.cmd == "job":
        o = job(x.cls, x.side, cfg, x.synthetic, [r for r in x.rules.split(",") if r] or None)
        Path(x.out).parent.mkdir(parents=True, exist_ok=True)
        Path(x.out).write_text(json.dumps(o))
        print(f"[mega] {x.cls}/{x.side}: {o['n_trials']} trials, funnel {o['funnel']}")
    else:
        parts = [json.loads(p_.read_text()) for p_ in sorted(Path(x.parts).rglob("*.json"))]
        o = aggregate(parts, cfg)
        Path(x.out).parent.mkdir(parents=True, exist_ok=True)
        Path(x.out).write_text(json.dumps(o, indent=1, default=str))
        Path(x.md).parent.mkdir(parents=True, exist_ok=True)
        Path(x.md).write_text(markdown(o, cfg))
        print(markdown(o, cfg))
        if x.telegram:
            from run import telegram
            telegram(telegram_text(o))


if __name__ == "__main__":
    main()
