# Scan — metals

- Variants tried: **2394** · global PBO: **0.401** · equal-weight benchmark Sharpe: 0.352 · Reality Check p (best vs benchmark): 0.87 · timeframe 1d · runtime 440s
- Single ideas and two-signal combinations (`A+B` = A confirmed by B): 30 combo families. Every variant's own result is in the matching `_variants.csv`.
- Ranked by walk-forward OOS Sharpe per family. Full-sample DSR is deflated by ALL trials.
- A scan result is a LEAD, not a decision. Register a hypothesis and run the gate.

| # | family | variants | WF OOS Sharpe | OOS CAGR | OOS MaxDD | 2x-cost Sharpe | family PBO | best full Sharpe | DSR(all trials) |
|---|---|---|---|---|---|---|---|---|---|
| 1 | williams_reversal+linreg_slope | 3 | 0.766 | 0.0051 | -0.0081 | 0.751 | nan | 0.059 | 0.006 |
| 2 | stoch_reversal+williams_reversal | 3 | 0.71 | 0.071 | -0.1585 | 0.669 | 0.554 | 0.59 | 0.348 |
| 3 | obv_trend+stoch_reversal | 3 | 0.698 | 0.0628 | -0.185 | 0.683 | 0.797 | 0.476 | 0.193 |
| 4 | st_reversal | 6 | 0.688 | 0.1468 | -0.3103 | 0.624 | 0.223 | 0.493 | 0.212 |
| 5 | ultimate_reversal+obv_trend | 3 | 0.683 | 0.0106 | -0.0289 | 0.648 | 0.297 | 0.735 | 0.53 |
| 6 | williams_reversal | 48 | 0.682 | 0.0422 | -0.106 | 0.61 | 0.382 | 0.556 | 0.276 |
| 7 | vol_managed_momentum | 4 | 0.665 | 0.1003 | -0.2862 | 0.661 | 0.193 | 0.292 | 0.056 |
| 8 | high_52w | 3 | 0.657 | 0.1289 | -0.3486 | 0.652 | 0.442 | 0.427 | 0.129 |
| 9 | idio_vol | 4 | 0.64 | 0.1295 | -0.3364 | 0.64 | 1.0 | 0.347 | 0.084 |
| 10 | residual_momentum | 4 | 0.64 | 0.1295 | -0.3364 | 0.64 | 1.0 | 0.408 | 0.127 |
| 11 | mom_acceleration | 2 | 0.64 | 0.1295 | -0.3364 | 0.64 | 1.0 | 0.339 | 0.08 |
| 12 | low_vol | 6 | 0.64 | 0.1295 | -0.3364 | 0.64 | 1.0 | 0.378 | 0.084 |
| 13 | frog_in_pan | 4 | 0.64 | 0.1295 | -0.3364 | 0.64 | 0.5 | 0.378 | 0.084 |
| 14 | max_effect | 4 | 0.64 | 0.1295 | -0.3364 | 0.64 | 1.0 | 0.339 | 0.084 |
| 15 | usdtry_hedge_switch | 4 | 0.64 | 0.1295 | -0.3364 | 0.64 | 1.0 | 0.364 | 0.084 |
| 16 | trend_quality | 4 | 0.64 | 0.1295 | -0.3364 | 0.64 | 1.0 | 0.378 | 0.084 |
| 17 | volume_shock | 4 | 0.64 | 0.1295 | -0.3364 | 0.64 | 1.0 | 0.352 | 0.084 |
| 18 | betting_against_beta | 4 | 0.64 | 0.1295 | -0.3364 | 0.64 | 1.0 | 0.378 | 0.084 |
| 19 | obv_trend | 16 | 0.638 | 0.0713 | -0.2328 | 0.609 | 0.371 | 0.475 | 0.195 |
| 20 | cot_commercial_follow | 4 | 0.627 | 0.0609 | -0.1693 | 0.595 | 0.437 | 0.442 | 0.173 |
| 21 | williams_reversal+stoch_reversal | 3 | 0.623 | 0.0424 | -0.1381 | 0.574 | 0.505 | 0.469 | 0.171 |
| 22 | ml_ridge_rank | 8 | 0.623 | 0.1248 | -0.3364 | 0.622 | 0.101 | 0.531 | 0.252 |
| 23 | stoch_reversal+stochrsi_reversal | 3 | 0.618 | 0.0463 | -0.1284 | 0.58 | 0.461 | 0.464 | 0.204 |
| 24 | obv_trend+ultimate_reversal | 3 | 0.612 | 0.0344 | -0.0925 | 0.603 | 0.131 | 0.561 | 0.308 |
| 25 | xs_momentum | 18 | 0.602 | 0.129 | -0.4271 | 0.594 | 0.578 | 0.405 | 0.133 |

## Skipped / failed families
- linreg_slope+williams_reversal: no trades / flat returns in every variant

```yaml
# Suggested hypotheses from the scan (copy into hypotheses/registry.yaml, give real ids)
- id: S900
  rule: williams_reversal
  confirm: linreg_slope
  confirm_within: [0, 3, 5]
  universe: metals
  for_system: TODO
  status: active
  filters: [none, trend_sma200, regime_bench200]
  side: long
  note: "scan lead: WF OOS Sharpe 0.766, family PBO nan"
- id: S901
  rule: stoch_reversal
  confirm: williams_reversal
  confirm_within: [0, 3, 5]
  universe: metals
  for_system: TODO
  status: active
  filters: [none, trend_sma200, regime_bench200]
  side: long
  note: "scan lead: WF OOS Sharpe 0.71, family PBO 0.554"
- id: S902
  rule: obv_trend
  confirm: stoch_reversal
  confirm_within: [0, 3, 5]
  universe: metals
  for_system: TODO
  status: active
  filters: [none, trend_sma200, regime_bench200]
  side: long
  note: "scan lead: WF OOS Sharpe 0.698, family PBO 0.797"
- id: S903
  strategy: st_reversal
  universe: metals
  for_system: TODO
  status: active
  note: "scan lead: WF OOS Sharpe 0.688, family PBO 0.223"
- id: S904
  rule: ultimate_reversal
  confirm: obv_trend
  confirm_within: [0, 3, 5]
  universe: metals
  for_system: TODO
  status: active
  filters: [none, trend_sma200, regime_bench200]
  side: long
  note: "scan lead: WF OOS Sharpe 0.683, family PBO 0.297"
```
