"""Rule-based screening funnel: the "AI agent" of the video, without an LLM.

A candidate = one entry/exit rule (lab/rules.py) on ONE coin. Every rule's whole parameter grid is
run on every coin (all of them are counted as trials). For each (coin, rule) the funnel picks the
centre of the most robust parameter region (best neighbourhood average, not the single best point),
then eliminates step by step. The FIRST failed step is written down as the reason, in plain words.

  S0 data      : at least `min_years` of history
  S1 windows   : net profitable in EVERY report window the data covers (last 3y, last 5y, full)
                 and at least `min_trades` trades
  S2 quality   : profit factor >= min_profit_factor, 1x max drawdown >= max_dd_floor
  S3 costs     : still profitable with cost_stress x (commission + slippage)
  S4 plateau   : >= min_neighbour_share_pos of the neighbouring parameter sets are profitable
  S5 delay     : entering one bar late keeps >= min_delay_retained of the Sharpe
  S6 stability : >= min_pos_year_frac of calendar years profitable
  S7 PSR       : P(true Sharpe > 0) >= min_psr
  tier A       : survivors whose Deflated Sharpe (ALL funnel trials counted) >= tier_a_min_dsr
                 -> suggested as hypotheses for the real decision gate (walk-forward, PBO, ...)

A funnel result is a LEAD, never a decision (CLAUDE.md). Survivors go to the paper arena; only the
validation gate writes decisions/registry.json.
"""
from __future__ import annotations

import math
import os
from concurrent.futures import ProcessPoolExecutor
from dataclasses import replace

import numpy as np
import pandas as pd

from lab import metrics, perp, rules
from lab.engine import Costs
from lab.panel import Panel
from lab.rules import Signals
from lab.trade_engine import EXIT_GRID, run_trades

_G: dict = {}
STAGE_TR = {
    "S0": "veri yetersiz", "S1": "her dönemde kârlı değil / az işlem", "S2": "kâr faktörü veya düşüş zayıf",
    "S3": "yüksek maliyette zarar", "S4": "plato yok (komşu ayarlar zararda)", "S5": "1 bar gecikmeye dayanıksız",
    "S6": "yılların çoğunda kârlı değil", "S7": "istatistiksel güven düşük (PSR)", "OK": "geçti",
}


# ------------------------------------------------------------------ helpers shared with the arena
def subpanel(p: Panel, cols: list[str]) -> Panel:
    cols = [c for c in cols if c in p.columns]
    q = replace(p, o=p.o[cols], h=p.h[cols], l=p.l[cols], c=p.c[cols], v=p.v[cols],
                member=None if p.member is None else p.member.reindex(columns=cols))
    q.fund = {k: v.reindex(columns=cols) for k, v in (p.fund or {}).items()}
    q.extra = {k: (v.reindex(columns=cols) if isinstance(v, pd.DataFrame) else v) for k, v in (p.extra or {}).items()}
    return q


def shift_signals(s: Signals, k: int = 1) -> Signals:
    def sh(x):
        return None if x is None else x.shift(k).fillna(False).astype(bool)
    return Signals(sh(s.entry_long), sh(s.exit_long), sh(s.entry_short), sh(s.exit_short))


def run_variant(p: Panel, rule: str, params: dict, exit_id: int, side: str, costs: Costs, delay: int = 0):
    """Run one rule variant on every coin of `p` at once (equal 1/N sizing, no slot limit, so each coin
    trades independently). Returns stand-alone 1x returns per coin, SIGNED held exposure per coin
    (+1 long, -1 short, 0 flat; partial exits give fractions) and the trade log."""
    sig = rules.RULES[rule].fn(p, **params)
    if delay:
        sig = shift_signals(sig, delay)
    n = p.c.shape[1]
    res = run_trades(p, sig, EXIT_GRID[exit_id], costs, side, None, per_asset=True)
    R = res.meta["asset_returns"] * n
    X = res.meta["held_weights"].reindex(R.index).fillna(0.0) * n
    R = R.where(p.c.notna().cummax(), np.nan)          # NaN before a coin has data
    return R, X, res.meta["trades"]


def first_valid(p: Panel) -> dict:
    return {c: p.c[c].first_valid_index() for c in p.columns}


def fmt(params: dict) -> str:
    return ",".join(f"{k}={v}" for k, v in params.items())


def _sr_bar(r: pd.Series) -> float:
    r = r.dropna()
    sd = r.std()
    return float(r.mean() / sd) if len(r) > 30 and sd > 0 else 0.0


# ------------------------------------------------------------------ grid sweep (parallel)
def _sweep_job(args):
    rule, gi, params, exit_id, side, costs = args
    p = _G["panel"]
    try:
        R, _, tr = run_variant(p, rule, params, exit_id, side, costs)
    except Exception as e:  # noqa: BLE001
        return rule, gi, None, str(e)
    out = {}
    for c in R.columns:
        r = R[c].dropna()
        nt = int((tr["asset"] == c).sum()) if len(tr) else 0
        out[c] = (_sr_bar(r), float((1 + r).prod() - 1) if len(r) else 0.0, nt)
    return rule, gi, out, None


def sweep(p: Panel, rule_names: list[str], exit_id: int, side: str, costs: Costs, workers: int | None = None):
    """Every grid point of every rule on every coin. Returns {rule: {grid_index: {coin: (sr, ret, n)}}}."""
    jobs = []
    for rn in rule_names:
        for gi, gp in enumerate(rules.grid_points(rules.RULES[rn].grid)):
            jobs.append((rn, gi, gp, exit_id, side, costs))
    workers = workers or int(os.environ.get("LAB_WORKERS", os.cpu_count() or 1))
    _G["panel"] = p
    if workers > 1 and len(jobs) > 4:
        import multiprocessing as mp
        try:
            with ProcessPoolExecutor(workers, mp_context=mp.get_context("fork")) as ex:
                res = list(ex.map(_sweep_job, jobs, chunksize=max(1, len(jobs) // (workers * 8))))
        except Exception:  # noqa: BLE001
            res = [_sweep_job(j) for j in jobs]
    else:
        res = [_sweep_job(j) for j in jobs]
    out, errors = {}, {}
    for rn, gi, d, err in res:
        if d is None:
            errors[f"{rn}#{gi}"] = err
            continue
        out.setdefault(rn, {})[gi] = d
    return out, errors, len(jobs)


def neighbours(grid: dict) -> dict[int, list[int]]:
    """Grid points that differ in exactly one parameter by one step in its list."""
    keys = list(grid)
    pts = rules.grid_points(grid)
    pos = [tuple(grid[k].index(pt[k]) for k in keys) for pt in pts]
    where = {ps: i for i, ps in enumerate(pos)}
    nb = {}
    for i, ps in enumerate(pos):
        lst = []
        for d in range(len(keys)):
            for step in (-1, 1):
                q = list(ps); q[d] += step
                j = where.get(tuple(q))
                if j is not None:
                    lst.append(j)
        nb[i] = lst
    return nb


def plateau_pick(stats: dict, nb: dict, coin: str):
    """Centre of the most robust region. Score = min(own Sharpe, mean Sharpe of its neighbours):
    a point is good only when it AND its surroundings are good (a lone spike or a bad point between
    good ones both score low). Returns (grid_index, share of profitable neighbours or None)."""
    best, best_score = None, -np.inf
    for gi, d in stats.items():
        if coin not in d:
            continue
        nbs = [j for j in nb.get(gi, []) if j in stats and coin in stats[j]]
        own = stats[gi][coin][0]
        sc = min(own, float(np.mean([stats[j][coin][0] for j in nbs]))) if nbs else own
        if sc > best_score:
            best, best_score = gi, sc
    if best is None:
        return None, None
    nbs = [j for j in nb.get(best, []) if j in stats and coin in stats[j]]
    share = float(np.mean([stats[j][coin][1] > 0 for j in nbs])) if nbs else None
    return best, share


# ------------------------------------------------------------------ the funnel
def run(p: Panel, costs: Costs, cfg: dict, workers: int | None = None) -> dict:
    sc = cfg.get("screen", {})
    ppy = p.ppy
    metrics.set_periods(ppy)
    windows = cfg.get("report_windows_years", [3, 5, 0])
    exit_id, side = int(cfg.get("exit_id", 28)), cfg.get("side", "both")
    cps = costs.per_turnover
    stress = Costs(costs.commission * sc.get("cost_stress", 2.0), costs.slippage * sc.get("cost_stress", 2.0),
                   costs.borrow_annual, costs.funding_annual)
    fv = first_valid(p)
    end = p.index[-1]
    years = {c: ((end - t).days / 365.25 if t is not None else 0.0) for c, t in fv.items()}
    log: list[dict] = []
    for c, y in years.items():
        if y < sc.get("min_years", 3.0):
            log.append({"coin": c, "rule": "*", "params": "", "stage": "S0",
                        "why": f"{y:.1f} yıl veri var, en az {sc.get('min_years', 3.0)} yıl gerekli"})
    coins = [c for c, y in years.items() if y >= sc.get("min_years", 3.0)]
    if not coins:
        return {"error": "no coin has enough history", "log": log}
    q = subpanel(p, coins)
    rule_names = list(rules.RULES) if sc.get("rules", "all") == "all" else list(sc["rules"])
    print(f"[screen] sweeping {len(rule_names)} rules x full grids on {len(coins)} coins ...")
    stats, errors, n_jobs = sweep(q, rule_names, exit_id, side, costs, workers)
    trial_srs = [v[0] for d in stats.values() for g in d.values() for v in g.values()]
    n_trials = max(1, len(trial_srs))
    print(f"[screen] {n_jobs} variants x {len(coins)} coins = {n_trials} trials")

    # pick the plateau centre for every (coin, rule)
    picks: dict[tuple, dict] = {}
    for rn, st in stats.items():
        nb = neighbours(rules.RULES[rn].grid)
        pts = rules.grid_points(rules.RULES[rn].grid)
        for c in coins:
            gi, share = plateau_pick(st, nb, c)
            if gi is not None:
                picks[(c, rn)] = {"gi": gi, "params": pts[gi], "nb_share": share}

    # group identical variants -> one run over their coins
    def groups(keys):
        g: dict[tuple, list] = {}
        for (c, rn) in keys:
            pk = picks[(c, rn)]
            g.setdefault((rn, pk["gi"]), []).append(c)
        return g

    rows: dict[tuple, dict] = {}
    series: dict[tuple, tuple] = {}
    for (rn, gi), cs in groups(list(picks)).items():
        prm = picks[(cs[0], rn)]["params"]
        R, X, tr = run_variant(subpanel(q, cs), rn, prm, exit_id, side, costs)
        for c in cs:
            r = R[c].dropna()
            t = tr[tr["asset"] == c] if len(tr) else tr
            card = perp.card(r, t, ppy, windows, cfg.get("account", {}), cps, costs.funding_annual, fv[c])
            rows[(c, rn)] = {"coin": c, "rule": rn, "family": rules.RULES[rn].family, "params": fmt(prm),
                             "nb_share": picks[(c, rn)]["nb_share"], "card": card,
                             "sharpe": round(metrics.sharpe(r), 3), "max_dd": round(metrics.max_drawdown(r), 4),
                             "psr": round(metrics.psr(r), 3), "pos_years": round(perp.pos_year_frac(r, ppy), 3),
                             "trades": int(len(t)), "stage": None, "why": ""}
            series[(c, rn)] = (r, t)

    def fail(key, stage, why):
        rows[key]["stage"], rows[key]["why"] = stage, why

    # S1, S2
    for key, row in rows.items():
        cd = row["card"]
        rets = {k: v["ret"] for k, v in cd.items() if not v.get("no_data")}
        bad = [k for k, v in rets.items() if v <= 0]
        if bad or row["trades"] < sc.get("min_trades", 30):
            txt = ", ".join(f"{k} {v:+.0%}" for k, v in rets.items())
            fail(key, "S1", f"{txt}; {row['trades']} işlem" + (f" (zararlı: {', '.join(bad)})" if bad else ""))
            continue
        pf = cd.get("full", {}).get("profit_factor")
        if pf is None or pf < sc.get("min_profit_factor", 1.15) or row["max_dd"] < sc.get("max_dd_floor", -0.40):
            fail(key, "S2", f"PF {pf}, 1x maks. düşüş {row['max_dd']:.0%}")

    alive = [k for k, r in rows.items() if r["stage"] is None]
    # S3 cost stress
    for (rn, gi), cs in groups(alive).items():
        R, _, _ = run_variant(subpanel(q, cs), rn, picks[(cs[0], rn)]["params"], exit_id, side, stress)
        for c in cs:
            r = R[c].dropna()
            tot = float((1 + r).prod() - 1)
            rows[(c, rn)]["stress_ret"] = round(tot, 4)
            if tot <= 0:
                fail((c, rn), "S3", f"{sc.get('cost_stress', 2.0)}x maliyette getiri {tot:+.0%}")
    # S4 plateau
    for key in [k for k, r in rows.items() if r["stage"] is None]:
        sh = rows[key]["nb_share"]
        if sh is None or sh < sc.get("min_neighbour_share_pos", 0.5):
            fail(key, "S4", "komşu ayar yok" if sh is None else f"komşu ayarların %{sh * 100:.0f}'i kârlı")
    # S5 delay
    alive = [k for k, r in rows.items() if r["stage"] is None]
    for (rn, gi), cs in groups(alive).items():
        R, _, _ = run_variant(subpanel(q, cs), rn, picks[(cs[0], rn)]["params"], exit_id, side, costs, delay=1)
        for c in cs:
            s0 = rows[(c, rn)]["sharpe"]
            s1 = metrics.sharpe(R[c].dropna())
            kept = s1 / s0 if s0 > 0 else 0.0
            rows[(c, rn)]["delay_kept"] = round(kept, 3)
            if kept < sc.get("min_delay_retained", 0.4):
                fail((c, rn), "S5", f"1 bar geç girişte Sharpe'ın %{max(kept, 0) * 100:.0f}'i kalıyor")
    # S6, S7, DSR
    for key in [k for k, r in rows.items() if r["stage"] is None]:
        row = rows[key]
        if row["pos_years"] < sc.get("min_pos_year_frac", 0.6):
            fail(key, "S6", f"yılların %{row['pos_years'] * 100:.0f}'i kârlı")
            continue
        if row["psr"] < sc.get("min_psr", 0.9):
            fail(key, "S7", f"PSR {row['psr']}")
            continue
        row["stage"], row["why"] = "OK", "tüm adımlar geçti"
    for key, row in rows.items():
        if row["stage"] in ("OK", "S6", "S7", "S5"):
            row["dsr"] = round(metrics.dsr(series[key][0], n_trials, trial_srs), 3)
        row["tier"] = ("A" if row.get("dsr", 0) >= sc.get("tier_a_min_dsr", 0.9) else "B") if row["stage"] == "OK" else None
        log.append({"coin": row["coin"], "rule": row["rule"], "params": row["params"], "stage": row["stage"],
                    "why": row["why"]})

    total = len(years) * len(rule_names)
    s0 = (len(years) - len(coins)) * len(rule_names) + (len(coins) * len(rule_names) - len(rows))
    funnel, remaining = [], total
    for s in ["S0", "S1", "S2", "S3", "S4", "S5", "S6", "S7"]:
        k = s0 if s == "S0" else sum(1 for r in rows.values() if r["stage"] == s)
        remaining -= k
        funnel.append({"stage": s, "label": STAGE_TR[s], "eliminated": k, "remaining": remaining})
    return {"rows": rows, "series": series, "log": log, "funnel": funnel, "n_trials": n_trials,
            "n_variant_runs": n_jobs, "errors": errors, "coins": coins, "candidates_total": total,
            "years": {c: round(y, 2) for c, y in years.items()}, "data_start": str(p.index[0]),
            "data_end": str(p.index[-1]), "ppy": ppy, "first_valid": {c: str(t) for c, t in fv.items()}}


def rank_key(row: dict):
    tier = {"A": 0, "B": 1}.get(row.get("tier"), 2)
    stage = ["OK", "S7", "S6", "S5", "S4", "S3", "S2", "S1"].index(row["stage"]) if row["stage"] in \
        ["OK", "S7", "S6", "S5", "S4", "S3", "S2", "S1"] else 9
    return (tier, stage, -(row.get("dsr") or 0), -row["sharpe"])


def markdown(res: dict, cfg: dict, roster_note: str = "") -> str:
    tf, uni = cfg.get("timeframe"), cfg.get("universe")
    L = [f"# Eleme motoru — {uni} {tf}", "",
         f"Veri: {res['data_start'][:10]} → {res['data_end'][:10]}. Coin: {len(res['coins'])} uygun "
         f"(toplam {len(res['years'])}). Denenen varyant: {res['n_variant_runs']} × coin = **{res['n_trials']} deneme**.",
         "Her (coin, kural) için tek en iyi nokta değil, **en sağlam bölgenin merkezi** seçildi. "
         "Bu bir aday listesidir, karar değildir. Karar sadece doğrulama kapısında verilir.", "",
         "## Huni", "", "| Adım | Ne kontrol edilir | Elenen | Kalan |", "|---|---|---|---|"]
    for f in res["funnel"]:
        L.append(f"| {f['stage']} | {f['label']} | {f['eliminated']} | {f['remaining']} |")
    ok = sorted([r for r in res["rows"].values() if r["stage"] == "OK"], key=rank_key)
    L += ["", f"## Geçenler ({len(ok)})", ""]
    if not ok:
        L.append("**Daha iyisi bulunamadı:** kurala göre hiçbir strateji tüm adımları geçmedi. "
                 "Arena sadece kontrol üyeleriyle çalışır; switcher para ayırmaz.")
    else:
        L += ["| Tier | Coin | Kural | Ayar | 3y | 5y | Tüm | Sharpe | 1x DD | PF | DSR |", "|---|---|---|---|---|---|---|---|---|---|---|"]
        for r in ok:
            cd = r["card"]
            def w(k):
                v = cd.get(k, {})
                return "veri yok" if v.get("no_data") else f"{v.get('ret', 0):+.0%}"
            L.append(f"| {r['tier']} | {r['coin']} | {r['rule']} | `{r['params']}` | {w('3y')} | {w('5y')} | {w('full')} | "
                     f"{r['sharpe']} | {r['max_dd']:.0%} | {cd.get('full', {}).get('profit_factor')} | {r.get('dsr')} |")
    # agent-style narration per coin
    L += ["", "## Coin coin özet (ajan günlüğü)", ""]
    by = {}
    for r in res["rows"].values():
        by.setdefault(r["coin"], []).append(r)
    for c in sorted(res["years"]):
        if c not in by:
            why = next((x["why"] for x in res["log"] if x["coin"] == c and x["stage"] == "S0"), "işlem yok")
            L.append(f"- **{c}**: elendi (S0: {why}).")
            continue
        rs = sorted(by[c], key=rank_key)
        n_ok = sum(1 for r in rs if r["stage"] == "OK")
        best = rs[0]
        txt = (f"- **{c}**: {len(rs)} kural denendi, {n_ok} kaldı. En iyi aday {best['rule']} (`{best['params']}`): "
               f"{best['stage']} — {best['why']}.")
        L.append(txt)
    L += ["", "## Zayıf yönler (dürüst liste)", "",
          f"- {res['n_trials']} deneme yapıldı. Bu kadar çok denemede şans eseri iyi görünen strateji çıkar. "
          "DSR bunu düzeltir; tier A sadece DSR ≥ eşik olanlardır.",
          "- Seçim ve test aynı geçmiş veride yapıldı. Gerçek test arenadaki ileri (paper) kayıttır.",
          "- Survivorship: liste bugünün coinlerinden oluşur. Borsadan silinen coinler yok, bu sonucu iyimser yapar.",
          "- Funding sabit yıllık oranla, likidasyon işlem bazında yaklaşık modellenir.",
          "- Tek borsa verisi (Bitget, yoksa OKX/KuCoin). Emir defteri ve piyasa etkisi modellenmez."]
    if roster_note:
        L += ["", "## Arena", "", roster_note]
    return "\n".join(L)


def suggested_yaml(res: dict, cfg: dict, next_id: int) -> str:
    out = []
    for r in sorted([r for r in res["rows"].values() if r.get("tier") == "A"], key=rank_key):
        out.append(f"""- id: H{next_id:03d}
  rule: {r['rule']}
  universe: {cfg['universe']}
  tickers: [{r['coin']}]
  timeframe: {cfg['timeframe']}
  for_system: karma_perp_bot
  start: "{cfg.get('start', '2018-01-01')}"
  filters: [none]
  exits: [{cfg.get('exit_id', 28)}]
  side: {cfg.get('side', 'both')}
  status: active
  note: "Arena funnel tier A ({r['coin']} {r['rule']} {r['params']}, DSR {r.get('dsr')})"
""")
        next_id += 1
    return "\n".join(out)


def to_frame(res: dict) -> pd.DataFrame:
    rec = []
    for r in res["rows"].values():
        cd = r["card"]
        d = {k: r.get(k) for k in ("coin", "rule", "family", "params", "stage", "why", "tier", "sharpe", "max_dd",
                                   "psr", "dsr", "pos_years", "trades", "nb_share", "stress_ret", "delay_kept")}
        for w, v in cd.items():
            if not v.get("no_data"):
                d[f"ret_{w}"] = v["ret"]
                d[f"sharpe_{w}"] = v["sharpe"]
        rec.append(d)
    return pd.DataFrame(rec)


__all__ = ["run", "subpanel", "run_variant", "markdown", "suggested_yaml", "to_frame", "rank_key", "math"]
