# Scan — global_assets

- Variants tried: **1469** · global PBO: **0.562** · equal-weight benchmark Sharpe: 0.744 · Reality Check p (best vs benchmark): 0.44666666666666666 · timeframe 1d · runtime 234s
- Single ideas and two-signal combinations (`A+B` = A confirmed by B): 30 combo families. Every variant's own result is in the matching `_variants.csv`.
- Ranked by walk-forward OOS Sharpe per family. Full-sample DSR is deflated by ALL trials.
- A scan result is a LEAD, not a decision. Register a hypothesis and run the gate.

| # | family | variants | WF OOS Sharpe | OOS CAGR | OOS MaxDD | 2x-cost Sharpe | family PBO | best full Sharpe | DSR(all trials) |
|---|---|---|---|---|---|---|---|---|---|
| 1 | breadth_timing | 6 | 1.002 | 0.0816 | -0.1066 | 0.962 | 0.052 | 0.794 | 0.457 |
| 2 | betting_against_beta | 4 | 0.989 | 0.0964 | -0.1889 | 0.988 | 0.592 | 0.75 | 0.336 |
| 3 | inside_bar+awesome_zero | 3 | 0.968 | 0.0341 | -0.0578 | 0.956 | 0.576 | 0.897 | 0.597 |
| 4 | inside_bar+macd_zero | 3 | 0.945 | 0.0372 | -0.0578 | 0.932 | 0.115 | 0.882 | 0.589 |
| 5 | idio_vol | 4 | 0.926 | 0.1135 | -0.2308 | 0.918 | 0.569 | 0.794 | 0.42 |
| 6 | macro_risk_switch | 12 | 0.922 | 0.0651 | -0.1212 | 0.872 | 0.19 | 0.665 | 0.261 |
| 7 | dual_momentum | 6 | 0.912 | 0.1318 | -0.2768 | 0.897 | 0.075 | 0.994 | 0.701 |
| 8 | awesome_zero+engulfing | 3 | 0.91 | 0.0212 | -0.0361 | 0.883 | 0.243 | 0.899 | 0.564 |
| 9 | usdtry_hedge_switch | 4 | 0.886 | 0.1026 | -0.2308 | 0.886 | 1.0 | 0.777 | 0.336 |
| 10 | low_vol | 6 | 0.882 | 0.0858 | -0.2223 | 0.874 | 0.631 | 0.75 | 0.336 |
| 11 | core_tsmom_vt | 1 | 0.878 | 0.0547 | -0.0923 | 0.762 | nan | 0.731 | 0.346 |
| 12 | frog_in_pan | 4 | 0.876 | 0.1148 | -0.2308 | 0.864 | 0.362 | 0.85 | 0.502 |
| 13 | mom_acceleration | 2 | 0.868 | 0.1023 | -0.2566 | 0.859 | 0.591 | 0.716 | 0.331 |
| 14 | macd_zero | 6 | 0.865 | 0.0499 | -0.0876 | 0.8 | 0.608 | 0.803 | 0.421 |
| 15 | max_effect | 4 | 0.849 | 0.0855 | -0.2215 | 0.829 | 0.91 | 0.752 | 0.336 |
| 16 | ts_momentum | 6 | 0.839 | 0.0584 | -0.131 | 0.819 | 0.811 | 0.748 | 0.354 |
| 17 | trend_quality | 4 | 0.833 | 0.1089 | -0.2443 | 0.816 | 0.489 | 0.841 | 0.507 |
| 18 | seasonality_same_month | 4 | 0.816 | 0.0954 | -0.2308 | 0.803 | 0.182 | 0.67 | 0.271 |
| 19 | core_dual_trend_vt | 1 | 0.815 | 0.0555 | -0.1075 | 0.742 | nan | 0.753 | 0.383 |
| 20 | core_dual_trend_vt_band | 1 | 0.815 | 0.0553 | -0.1069 | 0.742 | nan | 0.753 | 0.383 |
| 21 | inside_bar | 4 | 0.812 | 0.0463 | -0.066 | 0.779 | 0.02 | 0.843 | 0.519 |
| 22 | ml_ridge_rank | 8 | 0.811 | 0.099 | -0.2308 | 0.805 | 0.085 | 0.75 | 0.38 |
| 23 | high_52w | 3 | 0.803 | 0.0937 | -0.2308 | 0.783 | 0.094 | 0.937 | 0.644 |
| 24 | wavetrend_reversal | 54 | 0.77 | 0.0114 | -0.0306 | 0.743 | 0.386 | 0.984 | 0.706 |
| 25 | rsi_rotation | 24 | 0.758 | 0.1005 | -0.32 | 0.667 | 0.344 | 0.773 | 0.336 |

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
- wavetrend_reversal+awesome_zero: no trades / flat returns in every variant
- wavetrend_reversal+macd_zero: no trades / flat returns in every variant

> ⚠️ **Zaman makinesi kontrolü önerilir.** Bir tarama sonucu karar değil, adaydır; birçok varyant arasından seçilen sonuçlar ileride çökebilir. Önce `run.py --hypothesis` kapısı, seçim süreci için `Time machine test`. Kural: CLAUDE.md / AGENTS.md.


```yaml
# Suggested hypotheses from the scan (copy into hypotheses/registry.yaml, give real ids)
- id: S900
  strategy: breadth_timing
  universe: global_assets
  for_system: TODO
  status: active
  note: "scan lead: WF OOS Sharpe 1.002, family PBO 0.052"
- id: S901
  strategy: betting_against_beta
  universe: global_assets
  for_system: TODO
  status: active
  note: "scan lead: WF OOS Sharpe 0.989, family PBO 0.592"
- id: S902
  rule: inside_bar
  confirm: awesome_zero
  confirm_within: [0, 3, 5]
  universe: global_assets
  for_system: TODO
  status: active
  filters: [none, trend_sma200, regime_bench200]
  side: long
  note: "scan lead: WF OOS Sharpe 0.968, family PBO 0.576"
- id: S903
  rule: inside_bar
  confirm: macd_zero
  confirm_within: [0, 3, 5]
  universe: global_assets
  for_system: TODO
  status: active
  filters: [none, trend_sma200, regime_bench200]
  side: long
  note: "scan lead: WF OOS Sharpe 0.945, family PBO 0.115"
- id: S904
  strategy: idio_vol
  universe: global_assets
  for_system: TODO
  status: active
  note: "scan lead: WF OOS Sharpe 0.926, family PBO 0.569"
```
