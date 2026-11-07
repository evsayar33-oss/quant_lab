# Scan — crypto_major

- Variants tried: **1469** · global PBO: **0.406** · equal-weight benchmark Sharpe: 0.852 · Reality Check p (best vs benchmark): 0.5466666666666666 · timeframe 1w · runtime 63s
- Single ideas and two-signal combinations (`A+B` = A confirmed by B): 30 combo families. Every variant's own result is in the matching `_variants.csv`.
- Ranked by walk-forward OOS Sharpe per family. Full-sample DSR is deflated by ALL trials.
- A scan result is a LEAD, not a decision. Register a hypothesis and run the gate.

| # | family | variants | WF OOS Sharpe | OOS CAGR | OOS MaxDD | 2x-cost Sharpe | family PBO | best full Sharpe | DSR(all trials) |
|---|---|---|---|---|---|---|---|---|---|
| 1 | supertrend_flip+roc_breakout | 3 | 0.705 | 0.1606 | -0.376 | 0.701 | 0.761 | 0.878 | 0.174 |
| 2 | hammer_star | 4 | 0.69 | 0.0503 | -0.0517 | 0.674 | 0.585 | 0.558 | 0.001 |
| 3 | psar_flip+cci_breakout | 3 | 0.685 | 0.1482 | -0.3227 | 0.679 | 0.692 | 0.946 | 0.198 |
| 4 | supertrend_flip+psar_flip | 3 | 0.682 | 0.1039 | -0.1676 | 0.677 | 0.981 | 0.944 | 0.1 |
| 5 | psar_flip+heikin_ashi | 3 | 0.667 | 0.1817 | -0.3298 | 0.662 | 0.918 | 1.045 | 0.262 |
| 6 | heikin_ashi | 6 | 0.665 | 0.2105 | -0.4587 | 0.634 | 0.009 | 1.27 | 0.554 |
| 7 | psar_flip+roc_breakout | 3 | 0.643 | 0.1484 | -0.2914 | 0.638 | 0.935 | 0.882 | 0.179 |
| 8 | psar_flip | 6 | 0.628 | 0.172 | -0.4746 | 0.62 | 0.079 | 1.124 | 0.33 |
| 9 | supertrend_flip+heikin_ashi | 3 | 0.624 | 0.1676 | -0.3193 | 0.619 | 0.54 | 1.024 | 0.23 |
| 10 | cci_breakout+roc_breakout | 3 | 0.613 | 0.1473 | -0.3643 | 0.604 | 0.918 | 1.007 | 0.242 |
| 11 | roc_breakout+supertrend_flip | 3 | 0.605 | 0.0817 | -0.2301 | 0.597 | 0.983 | 0.497 | 0.025 |
| 12 | cci_breakout+heikin_ashi | 3 | 0.601 | 0.1581 | -0.3774 | 0.591 | 0.391 | 1.047 | 0.29 |
| 13 | roc_breakout+cci_breakout | 3 | 0.576 | 0.1273 | -0.2678 | 0.568 | 0.521 | 0.931 | 0.143 |
| 14 | supertrend_flip | 10 | 0.562 | 0.1513 | -0.3938 | 0.556 | 0.051 | 1.044 | 0.263 |
| 15 | cci_breakout | 12 | 0.555 | 0.1374 | -0.424 | 0.546 | 0.083 | 1.006 | 0.247 |
| 16 | roc_breakout+heikin_ashi | 3 | 0.528 | 0.1349 | -0.4968 | 0.516 | 0.182 | 0.954 | 0.198 |
| 17 | hammer_star+heikin_ashi | 3 | 0.504 | 0.0063 | -0.0125 | 0.49 | 0.923 | 0.565 | 0.002 |
| 18 | macro_risk_switch | 12 | 0.493 | 0.1323 | -0.6118 | 0.488 | 0.026 | 0.964 | 0.236 |
| 19 | supertrend_flip+cci_breakout | 3 | 0.485 | 0.0995 | -0.3271 | 0.48 | 0.522 | 0.922 | 0.16 |
| 20 | psar_flip+supertrend_flip | 3 | 0.483 | 0.0904 | -0.2517 | 0.478 | 0.525 | 0.942 | 0.16 |
| 21 | roc_breakout | 30 | 0.472 | 0.1093 | -0.4702 | 0.462 | 0.174 | 0.977 | 0.232 |
| 22 | vwap_cross | 6 | 0.458 | 0.1121 | -0.5723 | 0.44 | 0.025 | 1.048 | 0.294 |
| 23 | heikin_ashi+psar_flip | 3 | 0.457 | 0.0243 | -0.0626 | 0.448 | 0.766 | 0.756 | 0.01 |
| 24 | elder_impulse | 4 | 0.456 | 0.112 | -0.5745 | 0.441 | 0.013 | 1.009 | 0.29 |
| 25 | chaikin_osc | 4 | 0.447 | 0.1052 | -0.5016 | 0.433 | 0.032 | 1.092 | 0.327 |

## Skipped / failed families
- dxy_metal_switch: macro series DX-Y.NYB unavailable
- real_yield_switch: macro series TIP unavailable
- gold_silver_ratio: macro series GC=F unavailable
- copper_gold_rotation: macro series HG=F unavailable
- cot_contrarian: COT positioning unavailable for this universe
- cot_commercial_follow: COT positioning unavailable for this universe
- cot_commercial: no trades / flat returns in every variant
- cot_extreme: no trades / flat returns in every variant
- funding_extreme: no trades / flat returns in every variant
- gap_fade: no trades / flat returns in every variant
- halloween: no trades / flat returns in every variant
- hammer_star+cci_breakout: no trades / flat returns in every variant
- hammer_star+supertrend_flip: no trades / flat returns in every variant
- ml_ridge_rank: no trades / flat returns in every variant
- weekday_long: no trades / flat returns in every variant

> ⚠️ **Zaman makinesi kontrolü önerilir.** Bir tarama sonucu karar değil, adaydır; birçok varyant arasından seçilen sonuçlar ileride çökebilir. Önce `run.py --hypothesis` kapısı, seçim süreci için `Time machine test`. Kural: CLAUDE.md / AGENTS.md.


```yaml
# Suggested hypotheses from the scan (copy into hypotheses/registry.yaml, give real ids)
```
