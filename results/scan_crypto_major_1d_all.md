# Scan — crypto_major

- Variants tried: **1469** · global PBO: **0.142** · equal-weight benchmark Sharpe: 0.851 · Reality Check p (best vs benchmark): 0.8466666666666667 · timeframe 1d · runtime 406s
- Single ideas and two-signal combinations (`A+B` = A confirmed by B): 30 combo families. Every variant's own result is in the matching `_variants.csv`.
- Ranked by walk-forward OOS Sharpe per family. Full-sample DSR is deflated by ALL trials.
- A scan result is a LEAD, not a decision. Register a hypothesis and run the gate.

| # | family | variants | WF OOS Sharpe | OOS CAGR | OOS MaxDD | 2x-cost Sharpe | family PBO | best full Sharpe | DSR(all trials) |
|---|---|---|---|---|---|---|---|---|---|
| 1 | atr_breakout+chop_switch | 3 | 1.211 | 0.1466 | -0.1514 | 1.179 | 0.446 | 1.558 | 0.303 |
| 2 | atr_breakout+ichimoku_cloud | 3 | 1.09 | 0.1032 | -0.1073 | 1.053 | 0.593 | 1.221 | 0.07 |
| 3 | atr_breakout+rsi_midline | 3 | 1.075 | 0.17 | -0.2343 | 1.015 | 0.328 | 1.759 | 0.517 |
| 4 | atr_breakout+keltner_breakout | 3 | 0.94 | 0.137 | -0.1613 | 0.896 | 0.908 | 1.682 | 0.449 |
| 5 | chop_switch+atr_breakout | 3 | 0.928 | 0.1562 | -0.2138 | 0.904 | 0.894 | 1.612 | 0.349 |
| 6 | atr_breakout+bollinger_breakout | 3 | 0.869 | 0.1141 | -0.1507 | 0.822 | 0.962 | 1.646 | 0.408 |
| 7 | bollinger_breakout+chop_switch | 3 | 0.863 | 0.1104 | -0.1613 | 0.839 | 0.782 | 1.608 | 0.398 |
| 8 | chop_switch | 2 | 0.862 | 0.1612 | -0.2425 | 0.83 | 0.228 | 1.653 | 0.386 |
| 9 | chop_switch+bollinger_breakout | 3 | 0.847 | 0.138 | -0.2004 | 0.821 | 0.96 | 1.626 | 0.401 |
| 10 | chop_switch+ichimoku_cloud | 3 | 0.842 | 0.0935 | -0.1349 | 0.816 | 0.947 | 1.336 | 0.124 |
| 11 | atr_breakout | 12 | 0.835 | 0.1366 | -0.2289 | 0.771 | 0.532 | 1.623 | 0.346 |
| 12 | keltner_breakout+bollinger_breakout | 3 | 0.831 | 0.1412 | -0.1952 | 0.8 | 0.95 | 1.659 | 0.351 |
| 13 | rsi_midline+atr_breakout | 3 | 0.803 | 0.1285 | -0.2434 | 0.757 | 0.984 | 1.499 | 0.227 |
| 14 | ichimoku_cloud+chop_switch | 3 | 0.791 | 0.0879 | -0.1236 | 0.772 | 0.431 | 1.195 | 0.09 |
| 15 | keltner_breakout | 12 | 0.787 | 0.1567 | -0.2191 | 0.757 | 0.305 | 1.63 | 0.318 |
| 16 | bollinger_breakout+keltner_breakout | 3 | 0.765 | 0.1308 | -0.2073 | 0.733 | 0.955 | 1.695 | 0.413 |
| 17 | keltner_breakout+rsi_midline | 3 | 0.744 | 0.1487 | -0.2486 | 0.709 | 0.228 | 1.597 | 0.316 |
| 18 | keltner_breakout+atr_breakout | 3 | 0.74 | 0.135 | -0.232 | 0.71 | 0.632 | 1.583 | 0.306 |
| 19 | ichimoku_cloud | 6 | 0.723 | 0.1645 | -0.3056 | 0.669 | 0.154 | 1.401 | 0.168 |
| 20 | keltner_breakout+chop_switch | 3 | 0.713 | 0.0944 | -0.1743 | 0.686 | 0.973 | 1.477 | 0.216 |
| 21 | bollinger_breakout | 12 | 0.666 | 0.1251 | -0.2807 | 0.627 | 0.412 | 1.617 | 0.328 |
| 22 | chop_switch+keltner_breakout | 3 | 0.66 | 0.0977 | -0.2067 | 0.628 | 0.741 | 1.642 | 0.372 |
| 23 | keltner_breakout+ichimoku_cloud | 3 | 0.659 | 0.0872 | -0.2037 | 0.625 | 0.837 | 1.374 | 0.165 |
| 24 | rsi_midline+ichimoku_cloud | 3 | 0.636 | 0.0764 | -0.1965 | 0.59 | 0.468 | 1.25 | 0.079 |
| 25 | rsi_midline | 24 | 0.627 | 0.1541 | -0.372 | 0.564 | 0.218 | 1.503 | 0.2 |

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
  rule: atr_breakout
  confirm: chop_switch
  confirm_within: [0, 3, 5]
  universe: crypto_major
  for_system: TODO
  status: active
  filters: [none, trend_sma200, regime_bench200]
  side: long
  note: "scan lead: WF OOS Sharpe 1.211, family PBO 0.446"
- id: S901
  rule: atr_breakout
  confirm: ichimoku_cloud
  confirm_within: [0, 3, 5]
  universe: crypto_major
  for_system: TODO
  status: active
  filters: [none, trend_sma200, regime_bench200]
  side: long
  note: "scan lead: WF OOS Sharpe 1.09, family PBO 0.593"
- id: S902
  rule: atr_breakout
  confirm: rsi_midline
  confirm_within: [0, 3, 5]
  universe: crypto_major
  for_system: TODO
  status: active
  filters: [none, trend_sma200, regime_bench200]
  side: long
  note: "scan lead: WF OOS Sharpe 1.075, family PBO 0.328"
- id: S903
  rule: atr_breakout
  confirm: keltner_breakout
  confirm_within: [0, 3, 5]
  universe: crypto_major
  for_system: TODO
  status: active
  filters: [none, trend_sma200, regime_bench200]
  side: long
  note: "scan lead: WF OOS Sharpe 0.94, family PBO 0.908"
- id: S904
  rule: chop_switch
  confirm: atr_breakout
  confirm_within: [0, 3, 5]
  universe: crypto_major
  for_system: TODO
  status: active
  filters: [none, trend_sma200, regime_bench200]
  side: long
  note: "scan lead: WF OOS Sharpe 0.928, family PBO 0.894"
```
