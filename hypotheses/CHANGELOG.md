# Gate and hypothesis changelog

- 2026-10-14: Initial gate (validation.GATE): OOS ≥ 3y, DSR ≥ 0.90, OOS Sharpe ≥ 0.5, MaxDD ≥ -45%, bootstrap P(SR>0) ≥ 0.85, ≥ 55% positive years, beats equal-weight with 2× costs. Hypotheses H001–H010 registered.
- 2026-10-14: Gate extended: PBO (CSCV) ≤ 0.50 and ≥ 30 OOS trades for rule candidates. Added rule-based hypotheses H011–H024 (technical entries with stops/targets, fundamental factors, crypto long/short).
- 2026-10-14: Gate v3: Sharpe measured in excess of the risk-free rate and in USD for local-currency markets; added White Reality Check p ≤ 0.10, 1-bar delay retention ≥ 40%, random-entry p ≤ 0.10 (rules), parameter-neighbourhood share ≥ 50%. Multi-timeframe support. Hypotheses H025–H032 (pairs, ML ridge, macro switch, 4h/1h crypto, weekly BIST, post-report drift, USDTRY switch).
- 2026-10-14: Two-signal confirmation combos (scan stage B + `confirm:` in hypotheses); per-variant scan CSV; heavy outputs moved to a force-pushed `results` branch; shared data prefetch + Actions cache + Yahoo retries.
- 2026-10-15: Stage 4 overlays (vol target, drawdown brake, equity-curve filter) become searchable variants counted as trials. Calibration suite added (8/8 passed on real data 2026-10-15).
- 2026-10-15: Metal drivers (DXY, real yields, gold/silver and copper/gold ratios, CFTC COT, own-month seasonality) and hypotheses H040-H047.
