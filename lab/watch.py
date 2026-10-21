"""Paper forward watch and leverage test for H063-H065 (rules: config/watch.yaml).

  python -m lab.watch lev    -> decisions/watch/leverage.json + leverage.md   (backtest, pre-registered pick)
  python -m lab.watch daily  -> decisions/watch/state.json + report.md        (paper record since `start`)

Signals use closed daily bars only. Paper only: no orders are sent.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path

import numpy as np
import pandas as pd
import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from lab import mega, metrics, screen  # noqa: E402

OUT = ROOT / "decisions" / "watch"


def cfg_load() -> dict:
    return yaml.safe_load((ROOT / "config" / "watch.yaml").read_text())


def idea_returns(idea: dict, panels: dict, synthetic: bool = False):
    cls = idea["cls"]
    if cls not in panels:
        panels[cls] = mega.load_class(cls, mega.cfg_load(), synthetic)
    p, costs = panels[cls]
    R, X, tr = screen.run_spec(p, idea["spec"], idea["side"], costs)
    pool = R.mean(axis=1, skipna=True).dropna()
    return p, pool, X, tr


def lever(r: pd.Series, L) -> pd.Series:
    return (r * L).clip(lower=-1.0)


def vt_scale(r: pd.Series, vt: dict, ppy: float) -> pd.Series:
    n = int(vt["lookback_days"] * ppy / 365.25)
    vol = r.rolling(n, min_periods=n // 2).std() * np.sqrt(ppy)
    return (vt["target"] / vol).clip(upper=vt["max_leverage"]).shift(1).fillna(1.0)


def _st(r: pd.Series) -> dict:
    if len(r) < 30:
        return {}
    eq = (1 + r).cumprod()
    return {"final_1000": round(float(1000 * eq.iloc[-1]), 0), "cagr": round(metrics.cagr(r), 4),
            "sharpe": round(metrics.sharpe(r), 3), "max_dd": round(metrics.max_drawdown(r), 4),
            "worst_day": round(float(r.min()), 4), "ruined": bool((eq <= 0.01).any())}


def leverage(cfg: dict, synthetic: bool = False) -> dict:
    lv = cfg["leverage"]
    panels, out = {}, {}
    for hid, idea in cfg["ideas"].items():
        p, pool, _, _ = idea_returns(idea, panels, synthetic)
        metrics.set_periods(p.ppy)
        bh = p.c.pct_change(fill_method=None).mean(axis=1, skipna=True).dropna()
        rows = {}
        for L in lv["static"]:
            r = lever(pool, L)
            rows[f"{L}x"] = {"full": _st(r), "windows": {w: _st(r[r.index >= pd.Timestamp(w)]) for w in lv["windows"]}}
        s = vt_scale(pool, lv["vol_target"], p.ppy)
        rv = (pool * s).clip(lower=-1.0)
        rows["vt"] = {"full": _st(rv), "windows": {w: _st(rv[rv.index >= pd.Timestamp(w)]) for w in lv["windows"]},
                      "avg_leverage": round(float(s.mean()), 2)}
        ok = []
        for L in lv["static"]:
            x = rows[f"{L}x"]
            parts = [x["full"]] + [v for v in x["windows"].values() if v]
            if x["full"] and all(v and v["max_dd"] >= lv["max_dd_floor"] and v["worst_day"] >= lv["worst_day_floor"] and not v["ruined"] for v in parts):
                ok.append(L)
        pick = max(ok) if ok else None
        out[hid] = {"name": idea["name"], "rows": rows, "pick": pick,
                    "bh": {"full": _st(bh), "windows": {w: _st(bh[bh.index >= pd.Timestamp(w)]) for w in lv["windows"]}}}
        print(f"[watch] {hid}: pick {pick}x")
    return {"date": date.today().isoformat(), "ideas": out}


def lev_markdown(o: dict, cfg: dict) -> str:
    f = lambda v: "—" if v is None else f"{v:+.0%}"   # noqa: E731
    lv = cfg["leverage"]
    L = ["# H063–H065 kaldıraç testi", "",
         f"Kural sonuçlardan ÖNCE yazıldı (`config/watch.yaml`): en yüksek kaldıraç seçilir, şu şartla: tüm geçmişte VE her pencerede "
         f"maks. düşüş ≥ %{lv['max_dd_floor']*100:.0f}, hiçbir gün %{lv['worst_day_floor']*100:.0f}'ten kötü değil, kasa hiç sıfırlanmamış.", ""]
    for hid, x in o["ideas"].items():
        L += [f"## {hid} — {x['name']}", "", f"Seçilen kaldıraç: **{'yok (1x bile şartı geçmedi)' if x['pick'] is None else str(x['pick']) + 'x'}**", "",
              "| Kaldıraç | Tüm geçmiş: $1000 → | Yıllık | Sharpe | Maks. düşüş | En kötü gün | " +
              " | ".join(f"{w} → bugün yıllık / DD" for w in lv["windows"]) + " |",
              "|---|---|---|---|---|---|" + "---|" * len(lv["windows"])]
        for k, v in list(x["rows"].items()) + [("al-tut", x["bh"])]:
            fu = v["full"]
            if not fu:
                continue
            ws = " | ".join(f"{f(v['windows'][w].get('cagr'))} / {f(v['windows'][w].get('max_dd'))}" for w in lv["windows"])
            name = f"vol hedefi %{lv['vol_target']['target']*100:.0f} (ort. {v.get('avg_leverage')}x)" if k == "vt" else k
            L.append(f"| {name} | {fu['final_1000']:,.0f} | {f(fu['cagr'])} | {fu['sharpe']} | {f(fu['max_dd'])} | {f(fu['worst_day'])} | {ws} |")
        L.append("")
    L += ["## Zayıf yönler", "",
          "- Kaldıraç kenar yaratmaz; kârı ve zararı aynı oranda büyütür. Sharpe değişmez.",
          "- Geçmişteki en kötü düşüş, gelecekteki en kötü düşüş değildir. Seçilen kaldıraç bu yüzden bir üst sınırdır, hedef değil.",
          "- Vadeli işlem kontrat büyüklüğü hesaba katılmadı (küçük kasada mikro kontrat gerekir). Roll maliyeti modellenmedi.",
          "- Bu üç fikir binlerce aday içinden seçildi. Paper kayıt gerçek testtir."]
    return "\n".join(L) + "\n"


def daily(cfg: dict, synthetic: bool = False) -> tuple[dict, list[str]]:
    OUT.mkdir(parents=True, exist_ok=True)
    prev = json.loads((OUT / "state.json").read_text()) if (OUT / "state.json").exists() else {}
    levj = json.loads((OUT / "leverage.json").read_text()) if (OUT / "leverage.json").exists() else {"ideas": {}}
    start = pd.Timestamp(cfg["start"])
    panels, st, msgs = {}, {"date": date.today().isoformat(), "start": cfg["start"], "ideas": {}}, []
    for hid, idea in cfg["ideas"].items():
        p, pool, X, tr = idea_returns(idea, panels, synthetic)
        metrics.set_periods(p.ppy)
        last = X.index[-1]
        held = {a: round(float(X.loc[last, a]), 3) for a in X.columns if abs(X.loc[last, a]) > 1e-9}
        pick = (levj["ideas"].get(hid) or {}).get("pick") or 1
        fw = pool[pool.index >= start]
        rec = {"name": idea["name"], "bar": str(last.date()), "held": held, "leverage_pick": pick,
               "paper_1x": _st(fw) or {"final_1000": round(float(1000 * (1 + fw).prod()), 0) if len(fw) else 1000.0, "days": int(len(fw))},
               f"paper_{pick}x": _st(lever(fw, pick)) or {"final_1000": round(float(1000 * (1 + lever(fw, pick)).prod()), 0) if len(fw) else 1000.0}}
        old = ((prev.get("ideas") or {}).get(hid) or {}).get("held", {})
        if held != old:
            ch = [f"{a}: {old.get(a, 0):+.2f} → {held.get(a, 0):+.2f}" for a in sorted(set(held) | set(old)) if held.get(a, 0) != old.get(a, 0)]
            msgs.append(f"{hid} {idea['name']} ({last.date()}): " + "; ".join(ch))
        st["ideas"][hid] = rec
    (OUT / "state.json").write_text(json.dumps(st, indent=1, default=str))
    return st, msgs


def daily_markdown(st: dict) -> str:
    L = ["# Paper izleme: H063–H065", "", f"Başlangıç: {st['start']}. Son çalışma: {st['date']}. Sadece sanal para; emir gönderilmez.", "",
         "| Hipotez | Fikir | Son bar | Pozisyon (+1 = varlığın 1/N payı tam long, −1 = tam short) | Paper 1x $1000 → | Seçilen kaldıraç | Paper kaldıraçlı $1000 → |",
         "|---|---|---|---|---|---|---|"]
    for hid, r in st["ideas"].items():
        pos = ", ".join(f"{a} {v:+.2f}" for a, v in r["held"].items()) or "nakit"
        pk = r["leverage_pick"]
        L.append(f"| {hid} | {r['name']} | {r['bar']} | {pos} | {r['paper_1x'].get('final_1000', 1000):,.0f} | {pk}x | "
                 f"{r.get(f'paper_{pk}x', {}).get('final_1000', 1000):,.0f} |")
    L += ["", "Kontrol: 2027-01-22 ve 2027-04-22 (zamanlanmış görev). Kural: `config/mega.yaml` baseline (rastgele giriş + al-tut)."]
    return "\n".join(L) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["lev", "daily"])
    ap.add_argument("--synthetic", action="store_true"); ap.add_argument("--telegram", action="store_true")
    x = ap.parse_args(argv)
    cfg = cfg_load()
    OUT.mkdir(parents=True, exist_ok=True)
    if x.cmd == "lev":
        o = leverage(cfg, x.synthetic)
        (OUT / "leverage.json").write_text(json.dumps(o, indent=1, default=str))
        md = lev_markdown(o, cfg)
        (OUT / "leverage.md").write_text(md)
        print(md)
        if x.telegram:
            from run import telegram
            telegram("🏋️ H063–H065 kaldıraç testi\n" + "\n".join(
                f"{h} {v['name']}: seçilen {v['pick'] or 'yok'}x" +
                (f" → yıllık {v['rows'][str(v['pick']) + 'x']['full']['cagr']:+.0%}, DD {v['rows'][str(v['pick']) + 'x']['full']['max_dd']:+.0%}" if v["pick"] else "")
                for h, v in o["ideas"].items()) + "\n⚠️ Kaldıraç kenar yaratmaz; paper kayıt gerçek testtir.")
    else:
        st, msgs = daily(cfg, x.synthetic)
        md = daily_markdown(st)
        (OUT / "report.md").write_text(md)
        print(md)
        if x.telegram and (msgs or date.today().weekday() == 4):
            from run import telegram
            body = "\n".join(msgs) if msgs else "Pozisyon değişikliği yok."
            summ = "\n".join(f"{h}: 1x ${r['paper_1x'].get('final_1000', 1000):,.0f} | {r['leverage_pick']}x "
                             f"${r.get('paper_' + str(r['leverage_pick']) + 'x', {}).get('final_1000', 1000):,.0f}" for h, r in st["ideas"].items())
            telegram("👀 Paper izleme (H063–H065, sanal para)\n" + body + "\n" + summ)


if __name__ == "__main__":
    main()
