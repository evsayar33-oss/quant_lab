# Scan — metals_etf

- Variants tried: **2394** · global PBO: **0.671** · equal-weight benchmark Sharpe: 0.367 · Reality Check p (best vs benchmark): 0.7633333333333333 · timeframe 1w · runtime 162s
- Single ideas and two-signal combinations (`A+B` = A confirmed by B): 30 combo families. Every variant's own result is in the matching `_variants.csv`.
- Ranked by walk-forward OOS Sharpe per family. Full-sample DSR is deflated by ALL trials.
- A scan result is a LEAD, not a decision. Register a hypothesis and run the gate.

| # | family | variants | WF OOS Sharpe | OOS CAGR | OOS MaxDD | 2x-cost Sharpe | family PBO | best full Sharpe | DSR(all trials) |
|---|---|---|---|---|---|---|---|---|---|
| 1 | down_days | 24 | 0.91 | 0.0555 | -0.0901 | 0.888 | 0.502 | 0.606 | 0.609 |
| 2 | st_reversal | 6 | 0.882 | 0.2203 | -0.3129 | 0.847 | 0.39 | 0.509 | 0.396 |
| 3 | rsi_reversal | 480 | 0.823 | 0.0537 | -0.1049 | 0.808 | 0.417 | 0.687 | 0.72 |
| 4 | betting_against_beta | 4 | 0.806 | 0.1747 | -0.2825 | 0.806 | 0.622 | 0.48 | 0.413 |
| 5 | max_effect | 4 | 0.77 | 0.1654 | -0.3183 | 0.768 | 0.029 | 0.511 | 0.453 |
| 6 | rsi_reversal+cci_reversal | 3 | 0.762 | 0.0392 | -0.0935 | 0.761 | 0.737 | 0.719 | 0.753 |
| 7 | rsi_reversal+down_days | 3 | 0.757 | 0.0487 | -0.0935 | 0.756 | 0.204 | 0.706 | 0.741 |
| 8 | vol_managed_momentum | 4 | 0.726 | 0.0625 | -0.1312 | 0.721 | 0.005 | 0.601 | 0.592 |
| 9 | low_vol | 6 | 0.718 | 0.1489 | -0.3043 | 0.717 | 0.3 | 0.525 | 0.48 |
| 10 | idio_vol | 4 | 0.713 | 0.1577 | -0.3165 | 0.712 | 0.36 | 0.434 | 0.349 |
| 11 | copper_gold_rotation | 3 | 0.71 | 0.1637 | -0.408 | 0.697 | 0.512 | 0.357 | 0.271 |
| 12 | high_52w | 3 | 0.699 | 0.1612 | -0.3358 | 0.696 | 0.751 | 0.447 | 0.365 |
| 13 | usdtry_hedge_switch | 4 | 0.696 | 0.1541 | -0.3139 | 0.696 | 1.0 | 0.363 | 0.246 |
| 14 | volume_shock | 4 | 0.669 | 0.1527 | -0.354 | 0.659 | 0.737 | 0.425 | 0.333 |
| 15 | rsi_rotation | 24 | 0.667 | 0.1545 | -0.4198 | 0.63 | 0.594 | 0.489 | 0.379 |
| 16 | bollinger_reversion+rsi_reversal | 3 | 0.655 | 0.0085 | -0.004 | 0.653 | 1.0 | 0.559 | 0.569 |
| 17 | gold_silver_ratio | 18 | 0.648 | 0.117 | -0.331 | 0.636 | 0.459 | 0.6 | 0.592 |
| 18 | residual_momentum | 4 | 0.644 | 0.1399 | -0.3251 | 0.643 | 0.465 | 0.56 | 0.533 |
| 19 | frog_in_pan | 4 | 0.641 | 0.1409 | -0.3099 | 0.639 | 0.635 | 0.502 | 0.445 |
| 20 | mom_acceleration | 2 | 0.64 | 0.1438 | -0.3457 | 0.636 | 0.339 | 0.534 | 0.494 |
| 21 | trix_cross | 32 | 0.627 | 0.0771 | -0.2098 | 0.619 | 0.365 | 0.45 | 0.368 |
| 22 | trend_quality | 4 | 0.623 | 0.1443 | -0.3457 | 0.622 | 0.523 | 0.447 | 0.365 |
| 23 | down_days+trix_cross | 3 | 0.623 | 0.0011 | -0.0023 | 0.614 | 0.962 | 0.271 | 0.139 |
| 24 | pairs_zscore | 24 | 0.618 | 0.0207 | -0.0513 | 0.593 | 0.436 | 0.594 | 0.59 |
| 25 | rsi_reversal+hammer_star | 3 | 0.598 | 0.0148 | -0.0574 | 0.597 | 0.426 | 0.466 | 0.389 |

## Skipped / failed families
- bollinger_reversion+cci_reversal: no trades / flat returns in every variant
- bollinger_reversion+hammer_star: no trades / flat returns in every variant
- bollinger_reversion+trix_cross: no trades / flat returns in every variant
- cci_reversal+hammer_star: no trades / flat returns in every variant
- cci_reversal+trix_cross: no trades / flat returns in every variant
- down_days+bollinger_reversion: no trades / flat returns in every variant
- down_days+cci_reversal: no trades / flat returns in every variant
- down_days+rsi_reversal: no trades / flat returns in every variant
- hammer_star+bollinger_reversion: no trades / flat returns in every variant
- ml_ridge_rank: no trades / flat returns in every variant
- trix_cross+bollinger_reversion: no trades / flat returns in every variant
- trix_cross+cci_reversal: no trades / flat returns in every variant
- trix_cross+down_days: no trades / flat returns in every variant
- trix_cross+rsi_reversal: no trades / flat returns in every variant

```yaml
# Suggested hypotheses from the scan (copy into hypotheses/registry.yaml, give real ids)
- id: S900
  rule: down_days
  universe: metals_etf
  for_system: TODO
  status: active
  filters: [none, trend_sma200, regime_bench200]
  side: long
  note: "scan lead: WF OOS Sharpe 0.91, family PBO 0.502"
- id: S901
  strategy: st_reversal
  universe: metals_etf
  for_system: TODO
  status: active
  note: "scan lead: WF OOS Sharpe 0.882, family PBO 0.39"
- id: S902
  rule: rsi_reversal
  universe: metals_etf
  for_system: TODO
  status: active
  filters: [none, trend_sma200, regime_bench200]
  side: long
  note: "scan lead: WF OOS Sharpe 0.823, family PBO 0.417"
- id: S903
  strategy: betting_against_beta
  universe: metals_etf
  for_system: TODO
  status: active
  note: "scan lead: WF OOS Sharpe 0.806, family PBO 0.622"
- id: S904
  strategy: max_effect
  universe: metals_etf
  for_system: TODO
  status: active
  note: "scan lead: WF OOS Sharpe 0.77, family PBO 0.029"
```
