"""Strategy arena: ~100 strategies tracked on paper, every closed bar, plus the regime switcher.

Files (all small, on main):
  decisions/arena/roster.json        members with FROZEN settings and the date they joined (ids never reused)
  decisions/arena/switcher_gate.json backtest part of the switcher gate (written by the monthly screen)
  decisions/arena/switcher.json      what the switcher holds NOW + regime per coin + gate status (bots read this)
  decisions/arena/state.json         positions at the last run (to report changes once)
  decisions/arena/screen_summary.json last funnel table (dashboard)

Forward (paper) record: every run recomputes each member on fresh data with its frozen settings and
keeps only the bars AFTER it joined. Everything is causal, so this equals trading it live on closed bars.
Members are never re-fit. A member is retired (no longer chosen by the switcher) when:
  * its forward drawdown is worse than dd_mult x its backtest drawdown (any time), or
  * after min_forward_days its forward Sharpe is below min_forward_sharpe.
Retired members keep being tracked (status "retired") so the record stays complete.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

from lab import metrics, perp, regime, screen, switcher
from lab.engine import Costs
from lab.panel import Panel
from lab.trade_engine import EXIT_GRID

ROOT = Path(__file__).resolve().parent.parent
DIR = ROOT / "decisions" / "arena"
ROSTER, STATE, SWITCH, GATE, SUMMARY = (DIR / n for n in
                                        ("roster.json", "state.json", "switcher.json", "switcher_gate.json",
                                         "screen_summary.json"))


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _read(p: Path, default):
    try:
        return json.loads(p.read_text())
    except Exception:  # noqa: BLE001
        return default


def _write(p: Path, obj) -> None:
    DIR.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, indent=1, default=str, ensure_ascii=False))


def _params(d: dict) -> dict:
    """JSON turns tuples into lists; the rule functions expect the original tuples."""
    return {k: tuple(v) if isinstance(v, list) else v for k, v in (d or {}).items()}


def member_key(coin, rule, params: dict, exit_id, side, tf) -> str:
    return f"{coin}|{rule}|{screen.fmt(_params(params))}|x={exit_id}|{side}|{tf}"


# ------------------------------------------------------------------ roster
def update_roster(res: dict, cfg: dict) -> tuple[dict, str]:
    """Merge funnel survivors into the roster. Existing members keep their id, settings and join date."""
    from lab import rules as RL
    ac = cfg.get("arena", {})
    cap = int(ac.get("max_members", 100))
    ro = _read(ROSTER, None) or {"universe": cfg["universe"], "timeframe": cfg["timeframe"],
                                 "start": cfg.get("start", "2018-01-01"), "created_at": now_iso(),
                                 "next_id": 1, "members": []}
    if ro.get("timeframe") != cfg["timeframe"] or ro.get("universe") != cfg["universe"]:
        for m in ro["members"]:          # config changed: old members stop, record is kept
            if m["status"] != "retired":
                m.update(status="retired", retired_at=now_iso(), why="arena config changed")
        ro.update(universe=cfg["universe"], timeframe=cfg["timeframe"], created_at=now_iso())
    keys = {m["key"]: m for m in ro["members"]}
    ranked = sorted(res["rows"].values(), key=screen.rank_key)
    added, promoted = 0, 0

    def grid_params(row):
        pts = RL.grid_points(RL.RULES[row["rule"]].grid)
        return next(p for p in pts if screen.fmt(p) == row["params"])

    def n_live():
        return sum(1 for m in ro["members"] if m["status"] in ("active", "control"))

    for want_tier, status in (("ok", "active"), ("near", "control")):
        for row in ranked:
            is_ok = row["stage"] == "OK"
            if (want_tier == "ok") != is_ok:
                continue
            if want_tier == "near" and (not ac.get("fill_controls", True) or row["stage"] in ("S0", "S1", None)):
                continue
            prm = grid_params(row)
            k = member_key(row["coin"], row["rule"], prm, cfg["exit_id"], cfg["side"], cfg["timeframe"])
            bt = {"card": row["card"], "sharpe": row["sharpe"], "max_dd": row["max_dd"], "dsr": row.get("dsr"),
                  "stage": row["stage"], "why": row["why"], "tier": row.get("tier"), "screened_at": now_iso()}
            if k in keys:
                m = keys[k]
                m["backtest"] = bt
                if m["status"] == "control" and status == "active":
                    m["status"] = "active"; promoted += 1
                continue
            if n_live() >= cap:
                if status == "active":   # a survivor replaces the weakest control member
                    ctl = [m for m in ro["members"] if m["status"] == "control"]
                    if not ctl:
                        continue
                    weakest = min(ctl, key=lambda m: m["backtest"].get("sharpe") or 0)
                    weakest.update(status="retired", retired_at=now_iso(), why="replaced by a funnel survivor")
                else:
                    continue
            mid = f"A{ro['next_id']:04d}"
            ro["next_id"] += 1
            m = {"id": mid, "key": k, "coin": row["coin"], "rule": row["rule"], "params": prm,
                 "exit_id": cfg["exit_id"], "side": cfg["side"], "timeframe": cfg["timeframe"],
                 "status": status, "added_at": now_iso(), "backtest": bt}
            ro["members"].append(m)
            keys[k] = m
            added += 1
    ro["updated_at"] = now_iso()
    _write(ROSTER, ro)
    act = sum(1 for m in ro["members"] if m["status"] == "active")
    ctl = sum(1 for m in ro["members"] if m["status"] == "control")
    note = (f"Arena: {act} aktif (eleme geçen), {ctl} kontrol (yakın aday, switcher kullanmaz), "
            f"{added} yeni üye, {promoted} kontrolden aktife. Üst sınır {cap}.")
    return ro, note


# ------------------------------------------------------------------ compute
def compute(ro: dict, p: Panel, costs: Costs, members: list[dict] | None = None):
    """Recompute every member with its frozen settings. Returns R (stand-alone 1x returns),
    X (signed exposure), trades per member id."""
    members = members if members is not None else ro["members"]
    groups: dict[tuple, list[dict]] = {}
    for m in members:
        if m["coin"] not in p.columns:
            continue
        groups.setdefault((m["rule"], json.dumps(m["params"], sort_keys=True), m["exit_id"], m["side"]), []).append(m)
    R, X, T = {}, {}, {}
    for (rule, pj, ex, side), ms in groups.items():
        coins = sorted({m["coin"] for m in ms})
        r, x, tr = screen.run_variant(screen.subpanel(p, coins), rule, _params(json.loads(pj)), ex, side, costs)
        for m in ms:
            R[m["id"]] = r[m["coin"]]
            X[m["id"]] = x[m["coin"]]
            T[m["id"]] = tr[tr["asset"] == m["coin"]] if len(tr) else tr
    return pd.DataFrame(R), pd.DataFrame(X), T


def member_regimes(reg: pd.DataFrame, ids: list[str], coin_of: dict) -> pd.DataFrame:
    return pd.DataFrame({i: reg[coin_of[i]] for i in ids if coin_of[i] in reg.columns}, index=reg.index)


def regime_sharpe(r: pd.Series, g: pd.Series) -> dict:
    """Sharpe of a member inside each regime (returns of bar t credited to the regime known at t-1)."""
    gp = g.shift(1).reindex(r.index)
    out = {}
    for k in regime.CODES:
        x = r[gp == k].dropna()
        out[regime.NAMES[k]] = round(metrics.sharpe(x), 2) if len(x) > 30 else None
    return out


def _eligible(ro: dict, R: pd.DataFrame, forward: bool) -> pd.DataFrame:
    E = pd.DataFrame(True, index=R.index, columns=R.columns)
    for m in ro["members"]:
        if m["id"] not in E.columns:
            continue
        if m["status"] == "control":
            E[m["id"]] = False
            continue
        if forward:
            a = pd.Timestamp(m["added_at"]).tz_localize(None)
            E.loc[E.index < a, m["id"]] = False
        if m["status"] == "retired" and m.get("retired_at"):
            z = pd.Timestamp(m["retired_at"]).tz_localize(None)
            E.loc[E.index >= z, m["id"]] = False
    return E


def gate_backtest(ro: dict, p: Panel, costs: Costs, cfg: dict) -> dict:
    """Monthly (screen job): switcher grid backtest vs equal weight, plus the cost-stress check."""
    sw = cfg.get("switcher", {})
    pool = [m for m in ro["members"] if m["status"] == "active" or (sw.get("pool") == "all" and m["status"] == "control")]
    if not pool:
        out = {"backtest_pass": False, "reason": "no active members", "checked_at": now_iso()}
        _write(GATE, out)
        return out
    R, X, _ = compute(ro, p, costs, pool)
    st = cfg.get("screen", {}).get("cost_stress", 2.0)
    Rs, _, _ = compute(ro, p, Costs(costs.commission * st, costs.slippage * st, costs.borrow_annual,
                                    costs.funding_annual), pool)
    coin_of = {m["id"]: m["coin"] for m in pool}
    reg = regime.classify(p, cfg.get("regime", {}))
    G = member_regimes(reg, list(R.columns), coin_of)
    alive = pd.DataFrame({i: p.c[coin_of[i]].notna() for i in R.columns})
    ev = switcher.evaluate(R.fillna(0), G, X, coin_of, alive, p.ppy, costs.per_turnover,
                           {**sw, "cost_stress": st}, cfg.get("report_windows_years", [3, 5, 0]), Rs.fillna(0))
    out = {k: v for k, v in ev.items() if k not in ("returns", "equal_weight")}
    out.update(checked_at=now_iso(), pool=len(pool),
               spark=perp.sparkline(ev["returns"]), spark_ew=perp.sparkline(ev["equal_weight"]))
    _write(GATE, out)
    return out


# ------------------------------------------------------------------ the 4-hourly run
def run(p: Panel, costs: Costs, cfg: dict) -> dict:
    ro = _read(ROSTER, None)
    if not ro or not ro.get("members"):
        return {"error": "roster is empty: run the screen first (python run.py --screen)"}
    ppy = p.ppy
    metrics.set_periods(ppy)
    ac, sw = cfg.get("arena", {}), cfg.get("switcher", {})
    R, X, T = compute(ro, p, costs)
    coin_of = {m["id"]: m["coin"] for m in ro["members"]}
    reg = regime.classify(p, cfg.get("regime", {}))
    G = member_regimes(reg, list(R.columns), coin_of)
    end = p.index[-1]
    cps, fund = costs.per_turnover, costs.funding_annual
    windows = cfg.get("report_windows_years", [3, 5, 0])

    # ---- forward record, retirement
    ret_cfg = ac.get("retire", {})
    members_out = []
    changed = False
    for m in ro["members"]:
        i = m["id"]
        if i not in R.columns:
            continue
        r = R[i].dropna()
        a = pd.Timestamp(m["added_at"]).tz_localize(None)
        f = r[r.index > a]
        days = (end - a).days if end > a else 0
        fwd = {"days": int(days), "bars": int(len(f)), "ret": round(float((1 + f).prod() - 1), 4) if len(f) else 0.0,
               "sharpe": round(metrics.sharpe(f), 3) if len(f) > 20 else None,
               "max_dd": round(metrics.max_drawdown(f), 4) if len(f) else 0.0,
               "trades": int((T[i]["entry"] > a).sum()) if len(T[i]) else 0}
        if m["status"] == "active":
            bt_dd = (m.get("backtest") or {}).get("max_dd") or -0.2
            why = None
            if len(f) > 20 and fwd["max_dd"] < ret_cfg.get("dd_mult", 1.5) * bt_dd:
                why = f"ileri düşüş {fwd['max_dd']:.0%} < {ret_cfg.get('dd_mult', 1.5)}× backtest ({bt_dd:.0%})"
            elif days >= ret_cfg.get("min_forward_days", 120) and (fwd["sharpe"] or 0) < ret_cfg.get("min_forward_sharpe", 0.0):
                why = f"{days} gün sonra ileri Sharpe {fwd['sharpe']}"
            if why:
                m.update(status="retired", retired_at=now_iso(), why=why)
                changed = True
                print(f"[arena] retired {i}: {why}")
        x = X[i]
        pos = float(x.iloc[-1]) if len(x) else 0.0
        members_out.append({
            "id": i, "coin": m["coin"], "rule": m["rule"], "params": screen.fmt(_params(m["params"])),
            "exit": EXIT_GRID[m["exit_id"]].label(), "side": m["side"], "status": m["status"],
            "tier": (m.get("backtest") or {}).get("tier"), "added_at": m["added_at"][:10], "why": m.get("why", ""),
            "position": "long" if pos > 1e-9 else ("short" if pos < -1e-9 else "flat"), "exposure": round(pos, 3),
            "forward": fwd, "card": perp.card(r, T[i], ppy, windows, cfg.get("account", {}), cps, fund),
            "regime_sharpe": regime_sharpe(r, G[i]) if i in G.columns else {},
            "regime_now": regime.NAMES[int(G[i].iloc[-1])] if i in G.columns else "unknown",
            "spark": perp.sparkline(r), "spark_fwd": perp.sparkline(f, 60),
        })
    if changed:                 # the roster is rewritten only when a member's status changes (small git history)
        ro["updated_at"] = now_iso()
        _write(ROSTER, ro)

    # ---- switcher: current picks (backtest-trained) + forward record (eligibility from join date)
    pool_ids = [m["id"] for m in ro["members"] if m["id"] in R.columns and m["status"] != "control"]
    Rp, Xp, Gp = R[pool_ids].fillna(0), X[pool_ids], G.reindex(columns=pool_ids)
    d = sw.get("default", {"halflife_days": 30, "top_k": 5})
    base = switcher.params_of(sw)
    act = {m["id"] for m in ro["members"] if m["status"] == "active"}
    e_now = pd.DataFrame({i: i in act for i in pool_ids}, index=Rp.index)   # today: only active members
    live_now = switcher.run(Rp, Gp, Xp, coin_of, ppy, cps, **d, **base, eligible=e_now) if pool_ids else None
    fwd_run = switcher.run(Rp, Gp, Xp, coin_of, ppy, cps, **d, **base,
                           eligible=_eligible(ro, Rp, forward=True)) if pool_ids else None
    since = pd.Timestamp(ro.get("created_at")).tz_localize(None)
    alive = pd.DataFrame({i: p.c[coin_of[i]].notna() for i in pool_ids}, index=Rp.index)
    elig_f = _eligible(ro, Rp, forward=True)
    ew_f = switcher.equal_weight(Rp, alive & elig_f) if pool_ids else pd.Series(dtype=float)
    sf = fwd_run["returns"][fwd_run["returns"].index > since] if fwd_run else pd.Series(dtype=float)
    ef = ew_f[ew_f.index > since] if len(ew_f) else ew_f
    gate = _read(GATE, {})
    gcfg = sw.get("gate", {})
    fwd_days = max(0, (end - since).days)
    f_sr, e_sr = (metrics.sharpe(sf) if len(sf) > 20 else None), (metrics.sharpe(ef) if len(ef) > 20 else None)
    checks = {"backtest_gate": bool(gate.get("backtest_pass")),
              "forward_days": fwd_days >= gcfg.get("min_forward_days", 180),
              "forward_beats_equal_weight": f_sr is not None and e_sr is not None and f_sr > e_sr}
    picks = []
    if live_now:
        for i, w in sorted(live_now["current"].items(), key=lambda kv: -kv[1]):
            mo = next(x for x in members_out if x["id"] == i)
            m = next(x for x in ro["members"] if x["id"] == i)
            picks.append({"id": i, "coin": m["coin"], "rule": m["rule"], "params": _params(m["params"]),
                          "exit_id": m["exit_id"], "side": m["side"], "timeframe": m["timeframe"],
                          "weight": w, "position": mo["position"], "regime": mo["regime_now"]})
    sw_out = {"updated_at": now_iso(), "data_end": str(end), "universe": ro["universe"], "timeframe": ro["timeframe"],
              "usable": all(checks.values()), "checks": checks, "settings": d,
              "cash": round(1 - sum(x["weight"] for x in picks), 4), "picks": picks,
              "forward": {"since": str(since.date()), "days": fwd_days,
                          "ret": round(float((1 + sf).prod() - 1), 4) if len(sf) else 0.0,
                          "sharpe": round(f_sr, 3) if f_sr is not None else None,
                          "ew_ret": round(float((1 + ef).prod() - 1), 4) if len(ef) else 0.0,
                          "ew_sharpe": round(e_sr, 3) if e_sr is not None else None,
                          "max_dd": round(metrics.max_drawdown(sf), 4) if len(sf) else 0.0},
              "regimes": regime.summary(reg)}
    _write(SWITCH, sw_out)

    # ---- changes since the last run (for Telegram)
    st = _read(STATE, {})
    prev_pos, prev_w = st.get("positions", {}), st.get("switcher", {})
    events = []
    held = {x["id"] for x in picks} | set(prev_w)
    notify = ac.get("notify", "switcher")
    for mo in members_out:
        old = prev_pos.get(mo["id"], "flat")
        if mo["position"] != old and (notify == "all" or (notify == "switcher" and mo["id"] in held)):
            events.append(f"{mo['id']} {mo['coin']} {mo['rule']}: {old} → {mo['position']}")
    new_w = {x["id"]: x["weight"] for x in picks}
    for i in sorted(set(new_w) | set(prev_w)):
        if abs(new_w.get(i, 0) - prev_w.get(i, 0)) > 1e-6:
            events.append(f"switcher {i}: ağırlık {prev_w.get(i, 0):.0%} → {new_w.get(i, 0):.0%}")
    last_bar = st.get("last_bar")
    new_bar = str(end) != last_bar
    hour = datetime.now(timezone.utc).hour
    today = datetime.now(timezone.utc).date().isoformat()
    summary_due = hour >= ac.get("daily_summary_hour_utc", 20) and st.get("last_summary") != today
    _write(STATE, {"last_bar": str(end), "positions": {x["id"]: x["position"] for x in members_out},
                   "switcher": new_w, "last_summary": today if summary_due else st.get("last_summary"),
                   "updated_at": now_iso()})
    return {"members": members_out, "switcher": sw_out, "gate": gate, "events": events if new_bar else [],
            "summary_due": summary_due, "regimes": sw_out["regimes"], "data_end": str(end),
            "spark_switch_fwd": perp.sparkline(sf, 90), "spark_ew_fwd": perp.sparkline(ef, 90)}


def telegram_text(out: dict, summary: bool) -> str:
    sw = out["switcher"]
    L = []
    if out["events"]:
        L.append("🏟️ quant_lab arena — yeni bar " + out["data_end"][:16])
        L += [f"• {e}" for e in out["events"][:25]]
    if summary:
        f = sw["forward"]
        L.append(f"📊 Arena günlük özet ({sw['timeframe']})")
        L.append(f"Switcher {'✅ kullanılabilir' if sw['usable'] else '🧪 paper (kapı geçmedi)'} — "
                 f"ileri {f['ret']:+.1%} (SR {f['sharpe']}) vs eşit ağırlık {f['ew_ret']:+.1%} (SR {f['ew_sharpe']}), "
                 f"{f['days']} gün")
        for x in sw["picks"]:
            L.append(f"  {x['id']} {x['coin']} {x['rule']} {x['weight']:.0%} [{x['regime']}] {x['position']}")
        L.append(f"  nakit {sw['cash']:.0%}")
        act = [m for m in out["members"] if m["status"] == "active"]
        top = sorted(act, key=lambda m: -(m["forward"]["ret"]))[:5]
        if top:
            L.append("En iyi ileri kayıt: " + ", ".join(f"{m['id']} {m['coin']} {m['forward']['ret']:+.1%}" for m in top))
    return "\n".join(L)
