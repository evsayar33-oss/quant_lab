# Scan — metals

- Variants tried: **2394** · global PBO: **0.736** · equal-weight benchmark Sharpe: 0.352 · Reality Check p (best vs benchmark): 0.87 · timeframe 1w · runtime 160s
- Single ideas and two-signal combinations (`A+B` = A confirmed by B): 30 combo families. Every variant's own result is in the matching `_variants.csv`.
- Ranked by walk-forward OOS Sharpe per family. Full-sample DSR is deflated by ALL trials.
- A scan result is a LEAD, not a decision. Register a hypothesis and run the gate.

| # | family | variants | WF OOS Sharpe | OOS CAGR | OOS MaxDD | 2x-cost Sharpe | family PBO | best full Sharpe | DSR(all trials) |
|---|---|---|---|---|---|---|---|---|---|
| 1 | supertrend_flip+awesome_zero | 3 | 0.681 | 0.032 | -0.0853 | 0.679 | 0.718 | 0.652 | 0.701 |
| 2 | copper_gold_rotation | 3 | 0.676 | 0.113 | -0.3241 | 0.649 | 0.786 | 0.363 | 0.278 |
| 3 | high_52w | 3 | 0.666 | 0.1368 | -0.2917 | 0.665 | 0.796 | 0.439 | 0.39 |
| 4 | gold_silver_ratio | 18 | 0.662 | 0.1066 | -0.2826 | 0.639 | 0.494 | 0.618 | 0.657 |
| 5 | dual_momentum | 6 | 0.629 | 0.1579 | -0.4142 | 0.627 | 0.372 | 0.465 | 0.428 |
| 6 | frog_in_pan | 4 | 0.615 | 0.1217 | -0.2917 | 0.615 | 0.456 | 0.473 | 0.441 |
| 7 | betting_against_beta | 4 | 0.615 | 0.1217 | -0.2917 | 0.615 | 1.0 | 0.39 | 0.32 |
| 8 | low_vol | 6 | 0.615 | 0.1217 | -0.2917 | 0.615 | 1.0 | 0.39 | 0.32 |
| 9 | idio_vol | 4 | 0.615 | 0.1217 | -0.2917 | 0.615 | 0.93 | 0.357 | 0.272 |
| 10 | max_effect | 4 | 0.615 | 0.1217 | -0.2917 | 0.615 | 1.0 | 0.357 | 0.272 |
| 11 | trend_quality | 4 | 0.615 | 0.1217 | -0.2917 | 0.615 | 0.467 | 0.404 | 0.34 |
| 12 | volume_shock | 4 | 0.615 | 0.1217 | -0.2917 | 0.615 | 1.0 | 0.397 | 0.33 |
| 13 | usdtry_hedge_switch | 4 | 0.615 | 0.1217 | -0.2917 | 0.615 | 1.0 | 0.372 | 0.272 |
| 14 | residual_momentum | 4 | 0.615 | 0.1217 | -0.2917 | 0.615 | 0.243 | 0.495 | 0.475 |
| 15 | ts_momentum | 6 | 0.599 | 0.0211 | -0.052 | 0.593 | 0.016 | 0.57 | 0.588 |
| 16 | st_reversal | 6 | 0.589 | 0.1196 | -0.3677 | 0.545 | 0.291 | 0.45 | 0.433 |
| 17 | cci_breakout+awesome_zero | 3 | 0.567 | 0.0439 | -0.1614 | 0.563 | 0.819 | 0.512 | 0.5 |
| 18 | xs_momentum | 18 | 0.563 | 0.1138 | -0.3629 | 0.559 | 0.434 | 0.545 | 0.551 |
| 19 | mom_acceleration | 2 | 0.554 | 0.1034 | -0.2917 | 0.554 | 1.0 | 0.473 | 0.441 |
| 20 | tsi_cross | 12 | 0.547 | 0.0598 | -0.2233 | 0.523 | 0.395 | 0.429 | 0.374 |
| 21 | seasonality_same_month | 4 | 0.544 | 0.1006 | -0.2917 | 0.544 | 0.084 | 0.465 | 0.428 |
| 22 | nr7_breakout | 8 | 0.544 | 0.0454 | -0.1128 | 0.523 | 0.013 | 0.507 | 0.507 |
| 23 | vol_managed_momentum | 4 | 0.544 | 0.0414 | -0.1119 | 0.542 | 0.437 | 0.494 | 0.474 |
| 24 | ma_timing | 4 | 0.542 | 0.0864 | -0.2895 | 0.539 | 0.383 | 0.505 | 0.49 |
| 25 | nr7_breakout+supertrend_flip | 3 | 0.533 | 0.0043 | -0.0068 | 0.53 | 1.0 | 0.667 | 0.778 |

## Skipped / failed families
- ma_cross+supertrend_flip: no trades / flat returns in every variant
- ml_ridge_rank: no trades / flat returns in every variant

```yaml
# Suggested hypotheses from the scan (copy into hypotheses/registry.yaml, give real ids)
- id: S900
  rule: supertrend_flip
  confirm: awesome_zero
  confirm_within: [0, 3, 5]
  universe: metals
  for_system: TODO
  status: active
  filters: [none, trend_sma200, regime_bench200]
  side: long
  note: "scan lead: WF OOS Sharpe 0.681, family PBO 0.718"
- id: S901
  strategy: copper_gold_rotation
  universe: metals
  for_system: TODO
  status: active
  note: "scan lead: WF OOS Sharpe 0.676, family PBO 0.786"
- id: S902
  strategy: high_52w
  universe: metals
  for_system: TODO
  status: active
  note: "scan lead: WF OOS Sharpe 0.666, family PBO 0.796"
- id: S903
  strategy: gold_silver_ratio
  universe: metals
  for_system: TODO
  status: active
  note: "scan lead: WF OOS Sharpe 0.662, family PBO 0.494"
- id: S904
  strategy: dual_momentum
  universe: metals
  for_system: TODO
  status: active
  note: "scan lead: WF OOS Sharpe 0.629, family PBO 0.372"
```
