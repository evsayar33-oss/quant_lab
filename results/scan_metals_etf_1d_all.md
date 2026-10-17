# Scan — metals_etf

- Variants tried: **2394** · global PBO: **0.558** · equal-weight benchmark Sharpe: 0.377 · Reality Check p (best vs benchmark): 0.5133333333333333 · timeframe 1d · runtime 442s
- Single ideas and two-signal combinations (`A+B` = A confirmed by B): 30 combo families. Every variant's own result is in the matching `_variants.csv`.
- Ranked by walk-forward OOS Sharpe per family. Full-sample DSR is deflated by ALL trials.
- A scan result is a LEAD, not a decision. Register a hypothesis and run the gate.

| # | family | variants | WF OOS Sharpe | OOS CAGR | OOS MaxDD | 2x-cost Sharpe | family PBO | best full Sharpe | DSR(all trials) |
|---|---|---|---|---|---|---|---|---|---|
| 1 | hammer_star+williams_reversal | 3 | 0.979 | 0.0049 | -0.0085 | 0.942 | 0.007 | 0.859 | 0.847 |
| 2 | st_reversal | 6 | 0.847 | 0.2093 | -0.3662 | 0.781 | 0.238 | 0.558 | 0.454 |
| 3 | max_effect | 4 | 0.826 | 0.1744 | -0.3327 | 0.817 | 0.104 | 0.498 | 0.411 |
| 4 | idio_vol | 4 | 0.806 | 0.1855 | -0.3703 | 0.803 | 0.44 | 0.393 | 0.266 |
| 5 | betting_against_beta | 4 | 0.777 | 0.1616 | -0.2961 | 0.776 | 0.18 | 0.517 | 0.363 |
| 6 | high_52w | 3 | 0.768 | 0.1689 | -0.378 | 0.758 | 0.49 | 0.5 | 0.389 |
| 7 | low_vol | 6 | 0.767 | 0.1632 | -0.3315 | 0.765 | 0.287 | 0.496 | 0.334 |
| 8 | williams_reversal+bollinger_reversion | 3 | 0.745 | 0.0375 | -0.0857 | 0.724 | 0.708 | 0.458 | 0.281 |
| 9 | residual_momentum | 4 | 0.737 | 0.1731 | -0.3745 | 0.731 | 0.704 | 0.477 | 0.35 |
| 10 | trend_quality | 4 | 0.734 | 0.168 | -0.3413 | 0.729 | 0.734 | 0.404 | 0.228 |
| 11 | vol_managed_momentum | 4 | 0.734 | 0.1196 | -0.2656 | 0.728 | 0.272 | 0.335 | 0.176 |
| 12 | usdtry_hedge_switch | 4 | 0.73 | 0.163 | -0.334 | 0.73 | 1.0 | 0.367 | 0.2 |
| 13 | bollinger_reversion+williams_reversal | 3 | 0.725 | 0.0182 | -0.0324 | 0.709 | 0.004 | 0.53 | 0.396 |
| 14 | williams_reversal+stochrsi_reversal | 3 | 0.72 | 0.0524 | -0.0914 | 0.689 | 0.584 | 0.366 | 0.225 |
| 15 | stochrsi_reversal+williams_reversal | 3 | 0.72 | 0.0482 | -0.0988 | 0.68 | 0.157 | 0.351 | 0.203 |
| 16 | mom_acceleration | 2 | 0.701 | 0.1548 | -0.3182 | 0.698 | 0.491 | 0.363 | 0.205 |
| 17 | bollinger_reversion+stochrsi_reversal | 3 | 0.665 | 0.013 | -0.0442 | 0.652 | 0.587 | 0.446 | 0.281 |
| 18 | hurst_switch+bollinger_reversion | 3 | 0.659 | 0.0007 | -0.0008 | 0.642 | 0.622 | 0.289 | 0.126 |
| 19 | volume_shock | 4 | 0.652 | 0.1444 | -0.3963 | 0.628 | 0.822 | 0.367 | 0.2 |
| 20 | bollinger_reversion | 48 | 0.647 | 0.0331 | -0.0881 | 0.607 | 0.704 | 0.592 | 0.493 |
| 21 | bollinger_reversion+hammer_star | 3 | 0.639 | 0.0017 | -0.0042 | 0.624 | 0.335 | 0.044 | 0.02 |
| 22 | williams_reversal+hammer_star | 3 | 0.635 | 0.0174 | -0.0681 | 0.614 | 0.918 | 0.16 | 0.085 |
| 23 | ml_ridge_rank | 8 | 0.62 | 0.1361 | -0.3481 | 0.616 | 0.22 | 0.608 | 0.545 |
| 24 | copper_gold_rotation | 3 | 0.615 | 0.1363 | -0.5352 | 0.556 | 0.669 | 0.295 | 0.153 |
| 25 | frog_in_pan | 4 | 0.614 | 0.1378 | -0.4162 | 0.611 | 0.67 | 0.397 | 0.2 |

## Skipped / failed families
- linreg_slope+bollinger_reversion: no trades / flat returns in every variant

```yaml
# Suggested hypotheses from the scan (copy into hypotheses/registry.yaml, give real ids)
- id: S900
  rule: hammer_star
  confirm: williams_reversal
  confirm_within: [0, 3, 5]
  universe: metals_etf
  for_system: TODO
  status: active
  filters: [none, trend_sma200, regime_bench200]
  side: long
  note: "scan lead: WF OOS Sharpe 0.979, family PBO 0.007"
- id: S901
  strategy: st_reversal
  universe: metals_etf
  for_system: TODO
  status: active
  note: "scan lead: WF OOS Sharpe 0.847, family PBO 0.238"
- id: S902
  strategy: max_effect
  universe: metals_etf
  for_system: TODO
  status: active
  note: "scan lead: WF OOS Sharpe 0.826, family PBO 0.104"
- id: S903
  strategy: idio_vol
  universe: metals_etf
  for_system: TODO
  status: active
  note: "scan lead: WF OOS Sharpe 0.806, family PBO 0.44"
- id: S904
  strategy: betting_against_beta
  universe: metals_etf
  for_system: TODO
  status: active
  note: "scan lead: WF OOS Sharpe 0.777, family PBO 0.18"
```
