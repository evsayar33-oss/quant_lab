# Scan — sp_megacap

- Variants tried: **1603** · global PBO: **0.369** · equal-weight benchmark Sharpe: 1.283 · Reality Check p (best vs benchmark): 0.0 · timeframe 1d · runtime 328s
- Single ideas and two-signal combinations (`A+B` = A confirmed by B): 30 combo families. Every variant's own result is in the matching `_variants.csv`.
- Ranked by walk-forward OOS Sharpe per family. Full-sample DSR is deflated by ALL trials.
- A scan result is a LEAD, not a decision. Register a hypothesis and run the gate.

| # | family | variants | WF OOS Sharpe | OOS CAGR | OOS MaxDD | 2x-cost Sharpe | family PBO | best full Sharpe | DSR(all trials) |
|---|---|---|---|---|---|---|---|---|---|
| 1 | value_cfp | 6 | 1.449 | 0.3669 | -0.3276 | 1.447 | 0.097 | 1.421 | 0.956 |
| 2 | value_momentum | 6 | 1.433 | 0.3149 | -0.2803 | 1.426 | 0.469 | 1.292 | 0.837 |
| 3 | value_sp | 6 | 1.363 | 0.2984 | -0.2694 | 1.361 | 0.877 | 1.412 | 0.896 |
| 4 | macro_risk_switch | 12 | 1.336 | 0.1276 | -0.161 | 1.281 | 0.419 | 1.48 | 0.948 |
| 5 | trend_quality | 4 | 1.295 | 0.276 | -0.2761 | 1.268 | 0.139 | 1.336 | 0.873 |
| 6 | mom_acceleration | 2 | 1.292 | 0.2536 | -0.2549 | 1.264 | 0.769 | 1.215 | 0.755 |
| 7 | value_bp | 6 | 1.292 | 0.2997 | -0.3366 | 1.29 | 0.502 | 1.349 | 0.921 |
| 8 | small_size | 6 | 1.275 | 0.2839 | -0.2858 | 1.273 | 0.222 | 1.435 | 0.932 |
| 9 | core_tsmom_vt | 1 | 1.268 | 0.1063 | -0.122 | 1.181 | nan | 1.249 | 0.758 |
| 10 | usdtry_hedge_switch | 4 | 1.264 | 0.2157 | -0.279 | 1.264 | 1.0 | 1.326 | 0.796 |
| 11 | inside_bar | 4 | 1.26 | 0.1103 | -0.1237 | 1.243 | 0.0 | 1.225 | 0.755 |
| 12 | value_ep | 6 | 1.255 | 0.3151 | -0.3657 | 1.253 | 0.532 | 1.346 | 0.919 |
| 13 | core_dual_trend_vt | 1 | 1.249 | 0.1125 | -0.1513 | 1.194 | nan | 1.217 | 0.718 |
| 14 | frog_in_pan | 4 | 1.249 | 0.2665 | -0.2808 | 1.231 | 0.768 | 1.216 | 0.718 |
| 15 | triple_ma+ichimoku_cloud | 3 | 1.245 | 0.0517 | -0.0566 | 1.226 | 0.11 | 1.194 | 0.671 |
| 16 | core_dual_trend_vt_band | 1 | 1.242 | 0.1112 | -0.1522 | 1.187 | nan | 1.212 | 0.711 |
| 17 | macd_zero | 6 | 1.241 | 0.0955 | -0.1018 | 1.181 | 0.374 | 1.163 | 0.645 |
| 18 | residual_momentum | 4 | 1.234 | 0.2623 | -0.314 | 1.217 | 0.966 | 1.118 | 0.62 |
| 19 | inside_bar+ibs_reversion | 3 | 1.222 | 0.0913 | -0.1151 | 1.208 | 0.088 | 1.193 | 0.719 |
| 20 | value_ebit_ev | 6 | 1.215 | 0.2726 | -0.3068 | 1.213 | 0.892 | 1.328 | 0.827 |
| 21 | triple_ma | 12 | 1.207 | 0.0877 | -0.1125 | 1.161 | 0.32 | 1.156 | 0.616 |
| 22 | ml_ridge_rank | 8 | 1.188 | 0.2721 | -0.2659 | 1.168 | 0.104 | 1.115 | 0.626 |
| 23 | macd_zero+smc_bos | 3 | 1.188 | 0.0461 | -0.0549 | 1.142 | 0.884 | 1.247 | 0.753 |
| 24 | xs_momentum | 18 | 1.173 | 0.3092 | -0.2632 | 1.161 | 0.756 | 1.22 | 0.723 |
| 25 | low_asset_growth | 6 | 1.168 | 0.2005 | -0.288 | 1.162 | 0.431 | 1.097 | 0.601 |

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

> ⚠️ **Zaman makinesi kontrolü önerilir.** Bir tarama sonucu karar değil, adaydır; birçok varyant arasından seçilen sonuçlar ileride çökebilir. Önce `run.py --hypothesis` kapısı, seçim süreci için `Time machine test`. Kural: CLAUDE.md / AGENTS.md.


```yaml
# Suggested hypotheses from the scan (copy into hypotheses/registry.yaml, give real ids)
- id: S900
  strategy: value_cfp
  universe: sp_megacap
  for_system: TODO
  status: active
  note: "scan lead: WF OOS Sharpe 1.449, family PBO 0.097"
- id: S901
  strategy: value_momentum
  universe: sp_megacap
  for_system: TODO
  status: active
  note: "scan lead: WF OOS Sharpe 1.433, family PBO 0.469"
- id: S902
  strategy: value_sp
  universe: sp_megacap
  for_system: TODO
  status: active
  note: "scan lead: WF OOS Sharpe 1.363, family PBO 0.877"
- id: S903
  strategy: macro_risk_switch
  universe: sp_megacap
  for_system: TODO
  status: active
  note: "scan lead: WF OOS Sharpe 1.336, family PBO 0.419"
- id: S904
  strategy: trend_quality
  universe: sp_megacap
  for_system: TODO
  status: active
  note: "scan lead: WF OOS Sharpe 1.295, family PBO 0.139"
```
