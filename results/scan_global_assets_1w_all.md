# Scan — global_assets

- Variants tried: **1469** · global PBO: **0.706** · equal-weight benchmark Sharpe: 0.759 · Reality Check p (best vs benchmark): 0.12333333333333334 · timeframe 1w · runtime 133s
- Single ideas and two-signal combinations (`A+B` = A confirmed by B): 30 combo families. Every variant's own result is in the matching `_variants.csv`.
- Ranked by walk-forward OOS Sharpe per family. Full-sample DSR is deflated by ALL trials.
- A scan result is a LEAD, not a decision. Register a hypothesis and run the gate.

| # | family | variants | WF OOS Sharpe | OOS CAGR | OOS MaxDD | 2x-cost Sharpe | family PBO | best full Sharpe | DSR(all trials) |
|---|---|---|---|---|---|---|---|---|---|
| 1 | low_vol | 6 | 1.001 | 0.0898 | -0.1733 | 0.998 | 0.838 | 0.783 | 0.436 |
| 2 | core_tsmom_vt | 1 | 0.973 | 0.0581 | -0.0659 | 0.918 | nan | 0.835 | 0.495 |
| 3 | core_dual_trend_vt_band | 1 | 0.954 | 0.0625 | -0.0795 | 0.919 | nan | 0.862 | 0.571 |
| 4 | core_dual_trend_vt | 1 | 0.953 | 0.0625 | -0.0798 | 0.919 | nan | 0.862 | 0.571 |
| 5 | idio_vol | 4 | 0.944 | 0.1211 | -0.2681 | 0.939 | 0.253 | 0.88 | 0.58 |
| 6 | high_52w_break+elder_impulse | 3 | 0.943 | 0.0462 | -0.0506 | 0.937 | 0.434 | 0.845 | 0.527 |
| 7 | triple_ma | 12 | 0.936 | 0.0581 | -0.094 | 0.925 | 0.375 | 0.843 | 0.526 |
| 8 | rsi_midline+triple_ma | 3 | 0.927 | 0.0273 | -0.0338 | 0.919 | 0.555 | 0.933 | 0.662 |
| 9 | triple_ma+elder_impulse | 3 | 0.922 | 0.0456 | -0.0772 | 0.907 | 0.661 | 0.839 | 0.521 |
| 10 | high_52w_break | 8 | 0.913 | 0.0447 | -0.0553 | 0.908 | 0.08 | 0.825 | 0.498 |
| 11 | high_52w_break+rsi_midline | 3 | 0.902 | 0.0406 | -0.0517 | 0.895 | 0.599 | 0.814 | 0.481 |
| 12 | mom_acceleration | 2 | 0.894 | 0.0929 | -0.2069 | 0.887 | 0.947 | 0.74 | 0.374 |
| 13 | usdtry_hedge_switch | 4 | 0.893 | 0.0959 | -0.2129 | 0.893 | 1.0 | 0.8 | 0.382 |
| 14 | breadth_timing | 6 | 0.885 | 0.0753 | -0.1319 | 0.868 | 0.379 | 0.772 | 0.348 |
| 15 | rsi_midline+elder_impulse | 3 | 0.865 | 0.0418 | -0.061 | 0.854 | 0.548 | 0.898 | 0.598 |
| 16 | elder_impulse | 4 | 0.853 | 0.051 | -0.0771 | 0.803 | 0.89 | 0.759 | 0.401 |
| 17 | high_52w | 3 | 0.849 | 0.1047 | -0.2069 | 0.835 | 0.855 | 0.912 | 0.624 |
| 18 | vol_managed_momentum | 4 | 0.846 | 0.065 | -0.1491 | 0.841 | 0.368 | 0.853 | 0.538 |
| 19 | psar_flip | 6 | 0.844 | 0.0515 | -0.1302 | 0.806 | 0.45 | 0.83 | 0.421 |
| 20 | supertrend_flip | 10 | 0.842 | 0.0509 | -0.0721 | 0.831 | 0.501 | 0.922 | 0.605 |
| 21 | rsi_midline | 24 | 0.84 | 0.0485 | -0.067 | 0.818 | 0.368 | 0.903 | 0.568 |
| 22 | seasonality_same_month | 4 | 0.837 | 0.0924 | -0.2129 | 0.824 | 0.335 | 0.705 | 0.327 |
| 23 | turn_of_month | 33 | 0.836 | 0.0839 | -0.2069 | 0.782 | 0.356 | 0.8 | 0.382 |
| 24 | bollinger_breakout | 12 | 0.836 | 0.0418 | -0.067 | 0.826 | 0.154 | 0.827 | 0.502 |
| 25 | volume_shock | 4 | 0.824 | 0.089 | -0.2626 | 0.814 | 0.531 | 0.79 | 0.382 |

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
- halloween: no trades / flat returns in every variant
- ml_ridge_rank: no trades / flat returns in every variant
- weekday_long: no trades / flat returns in every variant

> ⚠️ **Zaman makinesi kontrolü önerilir.** Bir tarama sonucu karar değil, adaydır; birçok varyant arasından seçilen sonuçlar ileride çökebilir. Önce `run.py --hypothesis` kapısı, seçim süreci için `Time machine test`. Kural: CLAUDE.md / AGENTS.md.


```yaml
# Suggested hypotheses from the scan (copy into hypotheses/registry.yaml, give real ids)
- id: S900
  strategy: low_vol
  universe: global_assets
  for_system: TODO
  status: active
  note: "scan lead: WF OOS Sharpe 1.001, family PBO 0.838"
- id: S901
  strategy: core_tsmom_vt
  universe: global_assets
  for_system: TODO
  status: active
  note: "scan lead: WF OOS Sharpe 0.973, family PBO nan"
- id: S902
  strategy: core_dual_trend_vt_band
  universe: global_assets
  for_system: TODO
  status: active
  note: "scan lead: WF OOS Sharpe 0.954, family PBO nan"
- id: S903
  strategy: core_dual_trend_vt
  universe: global_assets
  for_system: TODO
  status: active
  note: "scan lead: WF OOS Sharpe 0.953, family PBO nan"
- id: S904
  strategy: idio_vol
  universe: global_assets
  for_system: TODO
  status: active
  note: "scan lead: WF OOS Sharpe 0.944, family PBO 0.253"
```
