# Scan — bist30

- Variants tried: **1591** · global PBO: **0.013** · equal-weight benchmark Sharpe: 1.265 · Reality Check p (best vs benchmark): 0.0033333333333333335 · timeframe 1d · runtime 412s
- Single ideas and two-signal combinations (`A+B` = A confirmed by B): 30 combo families. Every variant's own result is in the matching `_variants.csv`.
- Ranked by walk-forward OOS Sharpe per family. Full-sample DSR is deflated by ALL trials.
- A scan result is a LEAD, not a decision. Register a hypothesis and run the gate.

| # | family | variants | WF OOS Sharpe | OOS CAGR | OOS MaxDD | 2x-cost Sharpe | family PBO | best full Sharpe | DSR(all trials) |
|---|---|---|---|---|---|---|---|---|---|
| 1 | qvm_composite | 18 | 1.955 | 0.7494 | -0.4461 | 1.933 | 0.217 | 1.699 | 0.841 |
| 2 | value_sp | 6 | 1.918 | 0.683 | -0.3833 | 1.907 | 0.647 | 1.736 | 0.816 |
| 3 | vol_managed_momentum | 4 | 1.893 | 0.3117 | -0.1602 | 1.854 | 0.219 | 1.646 | 0.783 |
| 4 | value_momentum | 6 | 1.814 | 0.6563 | -0.3894 | 1.785 | 0.225 | 1.556 | 0.677 |
| 5 | frog_in_pan | 4 | 1.741 | 0.5783 | -0.3121 | 1.699 | 0.956 | 1.523 | 0.549 |
| 6 | xs_momentum | 18 | 1.707 | 0.6802 | -0.4394 | 1.666 | 0.487 | 1.646 | 0.748 |
| 7 | small_size | 6 | 1.687 | 0.6393 | -0.4094 | 1.681 | 0.129 | 1.688 | 0.852 |
| 8 | value_bp | 6 | 1.646 | 0.597 | -0.3574 | 1.64 | 0.66 | 1.562 | 0.585 |
| 9 | betting_against_beta | 4 | 1.64 | 0.4558 | -0.3269 | 1.619 | 0.815 | 1.502 | 0.499 |
| 10 | value_ep | 6 | 1.607 | 0.5837 | -0.3942 | 1.598 | 0.531 | 1.562 | 0.617 |
| 11 | low_leverage | 6 | 1.587 | 0.4858 | -0.2939 | 1.581 | 0.097 | 1.45 | 0.411 |
| 12 | residual_momentum | 4 | 1.58 | 0.523 | -0.3208 | 1.539 | 0.973 | 1.508 | 0.551 |
| 13 | trend_quality | 4 | 1.572 | 0.5446 | -0.3583 | 1.524 | 0.05 | 1.532 | 0.56 |
| 14 | dual_momentum | 6 | 1.563 | 0.7081 | -0.4526 | 1.526 | 0.516 | 1.563 | 0.685 |
| 15 | core_tsmom_vt | 1 | 1.55 | 0.249 | -0.177 | 1.353 | nan | 1.299 | 0.208 |
| 16 | high_52w | 3 | 1.528 | 0.4726 | -0.3271 | 1.445 | 0.322 | 1.447 | 0.419 |
| 17 | piotroski_f | 6 | 1.519 | 0.4596 | -0.3738 | 1.498 | 0.151 | 1.394 | 0.34 |
| 18 | smc_choch | 6 | 1.507 | 0.196 | -0.1828 | 1.439 | 0.729 | 1.218 | 0.181 |
| 19 | rsi_midline+obv_trend | 3 | 1.505 | 0.1266 | -0.1363 | 1.32 | 0.442 | 1.267 | 0.261 |
| 20 | ml_ridge_rank | 8 | 1.498 | 0.5042 | -0.379 | 1.427 | 0.212 | 1.375 | 0.408 |
| 21 | elder_impulse+obv_trend | 3 | 1.494 | 0.1642 | -0.1612 | 1.24 | 0.798 | 1.24 | 0.22 |
| 22 | core_dual_trend_vt_band | 1 | 1.468 | 0.2522 | -0.2012 | 1.341 | nan | 1.252 | 0.172 |
| 23 | obv_trend | 8 | 1.465 | 0.2391 | -0.1937 | 1.338 | 0.246 | 1.234 | 0.173 |
| 24 | smc_bos+elder_impulse | 3 | 1.463 | 0.2247 | -0.2025 | 1.364 | 0.586 | 1.249 | 0.21 |
| 25 | elder_impulse+rsi_midline | 3 | 1.461 | 0.1103 | -0.1124 | 1.284 | 0.986 | 1.167 | 0.146 |

## Skipped / failed families
- value_cfp: fundamental field 'cfp' unavailable or coverage too low
- low_accruals: fundamental field 'accruals' unavailable or coverage too low
- dxy_metal_switch: macro series DX-Y.NYB unavailable
- real_yield_switch: macro series TIP unavailable
- gold_silver_ratio: macro series GC=F unavailable
- copper_gold_rotation: macro series HG=F unavailable
- cot_contrarian: COT positioning unavailable for this universe
- cot_commercial_follow: COT positioning unavailable for this universe
- cot_commercial: no trades / flat returns in every variant
- cot_extreme: no trades / flat returns in every variant
- funding_extreme: no trades / flat returns in every variant

> ⚠️ **Zaman makinesi kontrolü önerilir.** Bir tarama sonucu karar değil, adaydır; birçok varyant arasından seçilen sonuçlar ileride çökebilir. Önce `run.py --hypothesis` kapısı, seçim süreci için `Time machine test`. Kural: CLAUDE.md / AGENTS.md.


```yaml
# Suggested hypotheses from the scan (copy into hypotheses/registry.yaml, give real ids)
- id: S900
  strategy: qvm_composite
  universe: bist30
  for_system: TODO
  status: active
  note: "scan lead: WF OOS Sharpe 1.955, family PBO 0.217"
- id: S901
  strategy: value_sp
  universe: bist30
  for_system: TODO
  status: active
  note: "scan lead: WF OOS Sharpe 1.918, family PBO 0.647"
- id: S902
  strategy: vol_managed_momentum
  universe: bist30
  for_system: TODO
  status: active
  note: "scan lead: WF OOS Sharpe 1.893, family PBO 0.219"
- id: S903
  strategy: value_momentum
  universe: bist30
  for_system: TODO
  status: active
  note: "scan lead: WF OOS Sharpe 1.814, family PBO 0.225"
- id: S904
  strategy: frog_in_pan
  universe: bist30
  for_system: TODO
  status: active
  note: "scan lead: WF OOS Sharpe 1.741, family PBO 0.956"
```
