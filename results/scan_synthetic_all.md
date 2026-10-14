# Scan — synthetic

- Variants tried: **650** · global PBO: **0.151** · equal-weight benchmark Sharpe: 1.474 · runtime 237s
- Ranked by walk-forward OOS Sharpe per family. Full-sample DSR is deflated by ALL trials.
- A scan result is a LEAD, not a decision. Register a hypothesis and run the gate.

| # | family | variants | WF OOS Sharpe | OOS CAGR | OOS MaxDD | 2x-cost Sharpe | family PBO | best full Sharpe | DSR(all trials) |
|---|---|---|---|---|---|---|---|---|---|
| 1 | max_effect | 4 | 1.455 | 0.1502 | -0.1277 | 1.336 | 0.021 | 1.354 | 0.261 |
| 2 | betting_against_beta | 4 | 1.283 | 0.1458 | -0.131 | 1.234 | 0.291 | 1.236 | 0.205 |
| 3 | idio_vol | 4 | 1.231 | 0.1274 | -0.0935 | 1.171 | 0.064 | 1.283 | 0.176 |
| 4 | trend_quality | 4 | 1.151 | 0.1191 | -0.1474 | 1.111 | 0.009 | 1.387 | 0.296 |
| 5 | high_52w | 3 | 1.121 | 0.1129 | -0.1394 | 1.086 | 0.017 | 1.262 | 0.2 |
| 6 | low_vol | 6 | 1.082 | 0.1141 | -0.1893 | 1.037 | 0.033 | 1.453 | 0.361 |
| 7 | ts_momentum | 6 | 1.029 | 0.0248 | -0.0442 | 0.968 | 0.496 | 1.202 | 0.207 |
| 8 | volume_shock | 4 | 0.995 | 0.1011 | -0.1699 | 0.509 | 0.01 | 0.98 | 0.061 |
| 9 | rsi_reversal | 120 | 0.959 | 0.0391 | -0.0656 | 0.88 | 0.046 | 1.389 | 0.252 |
| 10 | rsi_rotation | 24 | 0.952 | 0.0937 | -0.131 | 0.691 | 0.073 | 1.344 | 0.17 |
| 11 | ma_timing | 4 | 0.95 | 0.0576 | -0.1011 | 0.885 | 0.297 | 1.254 | 0.172 |
| 12 | zscore_reversion | 9 | 0.91 | 0.0317 | -0.0481 | 0.736 | 0.019 | 1.108 | 0.044 |
| 13 | residual_momentum | 4 | 0.841 | 0.0866 | -0.146 | 0.789 | 0.16 | 1.324 | 0.358 |
| 14 | adx_trend | 9 | 0.827 | 0.0333 | -0.0901 | 0.432 | 0.728 | 0.629 | 0.003 |
| 15 | ma_cross | 42 | 0.821 | 0.049 | -0.0859 | 0.692 | 0.753 | 1.032 | 0.06 |
| 16 | xs_momentum | 18 | 0.799 | 0.0891 | -0.1832 | 0.752 | 0.103 | 1.355 | 0.313 |
| 17 | vol_managed_momentum | 4 | 0.799 | 0.0946 | -0.2183 | 0.756 | 0.309 | 1.077 | 0.112 |
| 18 | awesome_zero | 2 | 0.791 | 0.0466 | -0.0766 | 0.529 | 0.009 | 0.862 | 0.037 |
| 19 | cmf_flow | 9 | 0.79 | 0.0374 | -0.0801 | 0.585 | 0.647 | 0.869 | 0.028 |
| 20 | seasonality_same_month | 4 | 0.755 | 0.0799 | -0.1664 | 0.635 | 0.0 | 0.89 | 0.034 |
| 21 | mom_acceleration | 2 | 0.731 | 0.0934 | -0.2703 | 0.648 | 0.986 | 0.923 | 0.043 |
| 22 | chaikin_osc | 2 | 0.695 | 0.0403 | -0.0767 | 0.271 | 0.362 | 0.781 | 0.014 |
| 23 | linreg_slope | 6 | 0.681 | 0.0383 | -0.0943 | 0.623 | 0.098 | 1.061 | 0.064 |
| 24 | stoch_reversal | 48 | 0.673 | 0.0352 | -0.0595 | 0.445 | 0.056 | 1.212 | 0.119 |
| 25 | supertrend_flip | 5 | 0.662 | 0.038 | -0.0976 | 0.42 | 0.817 | 0.866 | 0.044 |

## Skipped / failed families
- gap_fade: no trades / flat returns in every variant
- hammer_star: no trades / flat returns in every variant

```yaml
# Suggested hypotheses from the scan (copy into hypotheses/registry.yaml, give real ids)
```
