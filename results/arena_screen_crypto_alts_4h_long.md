# Eleme motoru — crypto_alts 4h

Veri: 2018-01-11 → 2026-10-20. Coin: 34 uygun (toplam 35). Denenen varyant: 553 × coin = **40897 deneme**.
Her (coin, kural) için tek en iyi nokta değil, **en sağlam bölgenin merkezi** seçildi. Bu bir aday listesidir, karar değildir. Karar sadece doğrulama kapısında verilir.

## Huni

| Adım | Ne kontrol edilir | Elenen | Kalan |
|---|---|---|---|
| S0 | veri yetersiz | 62 | 2108 |
| S1 | her dönemde kârlı değil / az işlem | 1823 | 285 |
| S2 | kâr faktörü veya düşüş zayıf | 180 | 105 |
| S3 | yüksek maliyette zarar | 15 | 90 |
| S4 | plato yok (komşu ayarlar zararda) | 20 | 70 |
| S5 | 1 bar gecikmeye dayanıksız | 8 | 62 |
| S6 | yılların çoğunda kârlı değil | 20 | 42 |
| S7 | istatistiksel güven düşük (PSR) | 8 | 34 |

## 2. aşama: filtre × çıkış × kombo (sadece S1'i geçen adaylarda)

285 aday → 22095 ek deneme (DSR'a eklendi). Her aday için en sağlam filtre/çıkış hücresi ve en sağlam kombo seçildi; kombo sadece kuralı tek başına geçerse aday olur. Seçilenler aynı S1–S7 adımlarından geçti.

| Adım | Ne kontrol edilir | Elenen | Kalan |
|---|---|---|---|
| S0 | veri yetersiz | 0 | 492 |
| S1 | her dönemde kârlı değil / az işlem | 168 | 324 |
| S2 | kâr faktörü veya düşüş zayıf | 107 | 217 |
| S3 | yüksek maliyette zarar | 2 | 215 |
| S4 | plato yok (komşu ayarlar zararda) | 52 | 163 |
| S5 | 1 bar gecikmeye dayanıksız | 10 | 153 |
| S6 | yılların çoğunda kârlı değil | 27 | 126 |
| S7 | istatistiksel güven düşük (PSR) | 16 | 110 |

## Geçenler (144)

| Tier | Aşama | Coin | Kural | Ayar | Varyant | 3y | 5y | Tüm | Sharpe | 1x DD | PF | DSR |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| B | 2 | XLM/USDT | keltner_breakout | `n=20,k=2.0` | filtre=adx20 · çıkış=stop_atr=2.0,be_r=1.0 | +656% | veri yok | +637% | 1.482 | -35% | 5.2 | 0.083 |
| B | 2 | XLM/USDT | wavetrend_reversal | `n1=9,n2=21,lo=-53` | filtre=adx20 · çıkış=signal_only | +276% | veri yok | +307% | 1.406 | -28% | 5.802 | 0.076 |
| B | 2 | SOL/USDT | adx_trend | `n=10,th=20` | filtre=regime_bench200 · çıkış=signal_only | +206% | +723% | +2254% | 1.592 | -26% | 2.705 | 0.072 |
| B | 2 | SOL/USDT | bollinger_breakout | `n=50,k=2.0` | filtre=regime_bench200 · çıkış=stop_atr=2.0,be_r=1.0 | +378% | +751% | +3550% | 1.575 | -36% | 4.028 | 0.071 |
| B | 2 | SOL/USDT | inside_bar | `trend_n=50` | filtre=regime_bench200 · çıkış=stop_atr=2.0,be_r=1.0 | +286% | +804% | +3776% | 1.575 | -32% | 3.834 | 0.07 |
| B | 2 | ARB/USDT | smc_choch | `k=8` | filtre=regime_bench200 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +141% | veri yok | +199% | 1.452 | -19% | 2.856 | 0.07 |
| B | 2 | INJ/USDT | cmf_flow | `n=10,th=0.2` | filtre=regime_bench200 · çıkış=stop_atr=2.0,max_hold=10 | +464% | veri yok | +756% | 1.476 | -30% | 2.03 | 0.066 |
| B | 2 | XLM/USDT | cci_breakout | `n=40,level=100` | filtre=adx20 · çıkış=stop_atr=2.0,be_r=1.0 | +683% | veri yok | +629% | 1.399 | -39% | 5.321 | 0.066 |
| B | 2 | INJ/USDT | inside_bar | `trend_n=50` | filtre=regime_bench200 · çıkış=stop_atr=2.0,be_r=1.0 | +296% | veri yok | +1038% | 1.369 | -37% | 3.411 | 0.044 |
| B | 2 | SOL/USDT | high_52w_break | `n=126,exit_ma=50` | filtre=regime_bench200 · çıkış=stop_atr=2.0,be_r=1.0 | +229% | +398% | +1747% | 1.413 | -33% | 4.883 | 0.032 |
| B | 2 | ARB/USDT | ma_cross | `kind=sma,pair=(20, 50)` | filtre=regime_bench200 · çıkış=stop_atr=2.0,max_hold=10 | +135% | veri yok | +262% | 1.358 | -31% | 2.755 | 0.029 |
| B | 2 | SUI/USDT | bollinger_reversion | `n=30,k=2.5` | filtre=adx20 · çıkış=stop_atr=2.0,max_hold=10 | +266% | veri yok | +230% | 1.233 | -22% | 2.238 | 0.029 |
| B | 2 | SOL/USDT | ichimoku_cloud | `cfg=(9, 26, 52)` | filtre=trend_sma200 · çıkış=signal_only | +389% | +625% | +1379% | 1.388 | -32% | 2.6 | 0.028 |
| B | 2 | XLM/USDT | cmf_flow | `n=40,th=0.05` | filtre=trend_sma200 · çıkış=stop_atr=2.0,be_r=1.0 | +330% | veri yok | +330% | 1.189 | -33% | 3.661 | 0.027 |
| B | 2 | ARB/USDT | macd_divergence | `k=3,fast=12,slow=26` | filtre=regime_bench200 · çıkış=stop_atr=2.0,be_r=1.0 | +326% | veri yok | +282% | 1.215 | -30% | 2.587 | 0.02 |
| B | 1 | XLM/USDT | high_52w_break | `n=126,exit_ma=50` | çıkış=stop_atr=2.0,trail_atr=3.0 | +244% | veri yok | +244% | 1.18 | -26% | 3.898 | 0.02 |
| B | 1 | XLM/USDT | wavetrend_reversal | `n1=9,n2=21,lo=-53` | çıkış=stop_atr=2.0,trail_atr=3.0 | +130% | veri yok | +150% | 1.058 | -23% | 1.841 | 0.02 |
| B | 2 | BNB/USDT | macd_zero | `cfg=(12, 26, 9)` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_choch(≤5 bar) | +84% | veri yok | +99% | 1.149 | -15% | 2.989 | 0.018 |
| B | 2 | INJ/USDT | cmf_flow | `n=10,th=0.2` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=macd_divergence(≤5 bar) | +108% | veri yok | +127% | 1.162 | -19% | 2.878 | 0.017 |
| B | 2 | DOT/USDT | macd_divergence | `k=3,fast=12,slow=26` | filtre=regime_bench200 · çıkış=stop_atr=2.0,be_r=1.0 | +116% | +119% | +718% | 1.397 | -22% | 3.976 | 0.015 |
| B | 2 | BNB/USDT | awesome_zero | `fast=5,slow=34` | filtre=htf_week_sma10 · çıkış=stop_atr=2.0,trail_atr=3.0 | +155% | veri yok | +128% | 1.084 | -20% | 2.059 | 0.014 |
| B | 2 | ARB/USDT | atr_breakout | `n=10,k=2.0` | filtre=regime_bench200 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +87% | veri yok | +124% | 1.09 | -26% | 2.347 | 0.012 |
| B | 2 | INJ/USDT | volume_breakout | `n=20,rv=3.0` | filtre=regime_bench200 · çıkış=stop_atr=2.0,tp_r=3.0 | +79% | veri yok | +241% | 1.1 | -35% | 2.347 | 0.01 |
| B | 2 | INJ/USDT | mfi_reversal | `n=10,lo=10` | filtre=adx20 · çıkış=stop_atr=2.0,max_hold=10 | +120% | veri yok | +144% | 1.034 | -17% | 2.297 | 0.009 |
| B | 2 | SUI/USDT | atr_breakout | `n=20,k=2.0` | filtre=regime_bench200 · çıkış=stop_atr=2.0,max_hold=10 | +106% | veri yok | +108% | 0.983 | -17% | 2.311 | 0.009 |
| B | 2 | SUI/USDT | ichimoku_cloud | `cfg=(20, 60, 120)` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=roc_breakout(≤5 bar) | +228% | veri yok | +172% | 0.97 | -36% | 2.237 | 0.009 |
| B | 2 | ADA/USDT | cmf_flow | `n=20,th=0.2` | filtre=adx20 · çıkış=signal_only | +393% | veri yok | +430% | 1.081 | -40% | 2.578 | 0.008 |
| B | 1 | XLM/USDT | donchian_breakout | `entry=100,exit=10` | çıkış=stop_atr=2.0,trail_atr=3.0 | +166% | veri yok | +166% | 0.968 | -33% | 2.631 | 0.008 |
| B | 1 | SUI/USDT | wavetrend_reversal | `n1=9,n2=26,lo=-60` | çıkış=stop_atr=2.0,trail_atr=3.0 | +109% | veri yok | +138% | 0.958 | -31% | 2.335 | 0.008 |
| B | 2 | INJ/USDT | wavetrend_reversal | `n1=12,n2=21,lo=-53` | filtre=low_vol · çıkış=stop_atr=2.0,tp_r=3.0 | +132% | veri yok | +153% | 1.046 | -30% | 2.048 | 0.007 |
| B | 2 | XLM/USDT | smc_bos | `k=2` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=donchian_breakout(≤0 bar) | +165% | veri yok | +165% | 0.951 | -36% | 2.398 | 0.007 |
| B | 2 | BNB/USDT | rsi_reversal | `n=28,lo=35,exit=60` | çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +36% | veri yok | +58% | 0.942 | -17% | 2.145 | 0.007 |
| B | 2 | SUI/USDT | keltner_breakout | `n=50,k=2.5` | filtre=trend_sma200 · çıkış=stop_atr=2.0,max_hold=10 | +211% | veri yok | +161% | 0.895 | -32% | 1.612 | 0.007 |
| B | 2 | BNB/USDT | macd_zero | `cfg=(12, 26, 9)` | filtre=htf_week_sma10 · çıkış=stop_atr=2.0,be_r=1.0 | +146% | veri yok | +129% | 0.892 | -37% | 2.347 | 0.007 |
| B | 2 | BTC/USDT | rsi_midline | `n=28,level=60` | filtre=low_vol · çıkış=stop_atr=2.0,be_r=1.0 | +88% | +84% | +1770% | 1.347 | -38% | 3.338 | 0.006 |
| B | 2 | SOL/USDT | cci_breakout | `n=40,level=150` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=ma_cross(≤5 bar) | +180% | +277% | +366% | 1.174 | -26% | 2.901 | 0.006 |
| B | 2 | BNB/USDT | triple_ma | `set=(5, 20, 50),kind=ema` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_fvg(≤3 bar) | +76% | veri yok | +68% | 0.934 | -15% | 2.35 | 0.006 |
| B | 2 | SUI/USDT | bollinger_breakout | `n=20,k=2.5` | filtre=trend_sma200 · çıkış=stop_atr=2.0,max_hold=10 | +145% | veri yok | +142% | 0.897 | -26% | 1.717 | 0.006 |
| B | 1 | XLM/USDT | cci_breakout | `n=40,level=100` | çıkış=stop_atr=2.0,trail_atr=3.0 | +195% | veri yok | +169% | 0.871 | -36% | 1.812 | 0.006 |
| B | 1 | XLM/USDT | price_ma | `kind=sma,n=200` | çıkış=stop_atr=2.0,trail_atr=3.0 | +97% | veri yok | +97% | 0.811 | -27% | 1.73 | 0.006 |
| B | 2 | SOL/USDT | rsi_midline | `n=28,level=60` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=ma_cross(≤5 bar) | +148% | +269% | +269% | 1.135 | -24% | 3.53 | 0.005 |
| B | 2 | ADA/USDT | roc_breakout | `n=10,th=10` | filtre=htf_week_sma10 · çıkış=stop_atr=2.0,tp_r=3.0 | +157% | veri yok | +147% | 1.042 | -19% | 2.915 | 0.005 |
| B | 1 | ARB/USDT | hurst_switch | `n=200,fast=20,rsi_n=5` | çıkış=stop_atr=2.0,trail_atr=3.0 | +143% | veri yok | +135% | 0.958 | -31% | 2.171 | 0.005 |
| B | 2 | SUI/USDT | wavetrend_reversal | `n1=9,n2=26,lo=-60` | çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +60% | veri yok | +94% | 0.859 | -34% | 2.033 | 0.005 |
| B | 2 | XLM/USDT | rsi_divergence | `n=14,k=5,exit_level=50` | filtre=low_vol · çıkış=stop_atr=2.0,tp_r=3.0 | +24% | veri yok | +25% | 0.816 | -11% | 2.769 | 0.005 |
| B | 2 | ADA/USDT | bollinger_breakout | `n=20,k=2.5` | filtre=htf_week_sma10 · çıkış=stop_atr=2.0,trail_atr=3.0 | +230% | veri yok | +178% | 0.99 | -39% | 2.567 | 0.004 |
| B | 2 | INJ/USDT | psar_flip | `cfg=(0.01, 0.1)` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=wavetrend_reversal(≤5 bar) | +75% | veri yok | +179% | 0.929 | -30% | 2.394 | 0.004 |
| B | 1 | INJ/USDT | wavetrend_reversal | `n1=12,n2=21,lo=-53` | çıkış=stop_atr=2.0,trail_atr=3.0 | +22% | veri yok | +262% | 0.895 | -38% | 1.621 | 0.004 |
| B | 1 | SUI/USDT | bollinger_reversion | `n=30,k=2.5` | çıkış=stop_atr=2.0,trail_atr=3.0 | +140% | veri yok | +136% | 0.818 | -36% | 1.536 | 0.004 |
| B | 2 | BTC/USDT | linreg_slope | `n=20,th=0.0005` | filtre=low_vol · çıkış=stop_atr=2.0,be_r=1.0 | +57% | +60% | +1165% | 1.242 | -36% | 2.177 | 0.003 |
| B | 2 | BTC/USDT | price_ma | `kind=ema,n=150` | filtre=low_vol · çıkış=stop_atr=2.0,be_r=1.0 | +203% | +182% | +2253% | 1.238 | -38% | 2.963 | 0.003 |
| B | 2 | SOL/USDT | atr_breakout | `n=20,k=2.0` | filtre=regime_bench200 · çıkış=signal_only | +99% | +130% | +420% | 1.028 | -39% | 2.546 | 0.003 |
| B | 2 | BNB/USDT | ma_cross | `kind=tema,pair=(50, 150)` | filtre=adx20 · çıkış=stop_atr=2.0,tp_r=3.0 | +55% | veri yok | +67% | 0.816 | -20% | 1.822 | 0.003 |
| B | 2 | SUI/USDT | volume_breakout | `n=20,rv=1.5` | filtre=regime_bench200 · çıkış=signal_only | +166% | veri yok | +116% | 0.712 | -39% | 1.605 | 0.003 |
| B | 2 | XRP/USDT | high_52w_break | `n=126,exit_ma=50` | filtre=regime_bench200 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +107% | +150% | +603% | 1.259 | -21% | 2.898 | 0.002 |
| B | 2 | MINA/USDT | adx_trend | `n=20,th=20` | filtre=regime_bench200 · çıkış=stop_atr=2.0,be_r=1.0 | +187% | +214% | +514% | 0.979 | -33% | 3.868 | 0.002 |
| B | 2 | SOL/USDT | donchian_breakout | `entry=100,exit=10` | filtre=regime_bench200 · çıkış=stop_atr=2.0,be_r=1.0 | +85% | +165% | +467% | 0.965 | -34% | 2.4 | 0.002 |
| B | 1 | ADA/USDT | keltner_breakout | `n=20,k=2.5` | çıkış=stop_atr=2.0,trail_atr=3.0 | +201% | veri yok | +221% | 0.943 | -39% | 2.105 | 0.002 |
| B | 2 | ADA/USDT | high_52w_break | `n=126,exit_ma=50` | filtre=adx20 · çıkış=stop_atr=2.0,be_r=1.0 | +323% | veri yok | +239% | 0.922 | -38% | 3.504 | 0.002 |
| B | 1 | BNB/USDT | rsi_reversal | `n=28,lo=35,exit=60` | çıkış=stop_atr=2.0,trail_atr=3.0 | +30% | veri yok | +52% | 0.766 | -21% | 2.046 | 0.002 |
| B | 2 | BNB/USDT | bollinger_breakout | `n=50,k=1.5` | filtre=htf_week_sma10 · çıkış=stop_atr=2.0,tp_r=3.0 | +72% | veri yok | +65% | 0.72 | -31% | 1.454 | 0.002 |
| B | 1 | ETH/USDT | price_ma | `kind=sma,n=150` | çıkış=stop_atr=2.0,trail_atr=3.0 | +114% | +113% | +1087% | 1.183 | -32% | 2.105 | 0.001 |
| B | 2 | BTC/USDT | atr_breakout | `n=20,k=1.5` | filtre=low_vol · çıkış=signal_only | +81% | +99% | +571% | 1.158 | -24% | 2.199 | 0.001 |
| B | 2 | BTC/USDT | aroon_cross | `n=50` | filtre=adx20 · çıkış=stop_atr=2.0,be_r=1.0 | +85% | +124% | +727% | 1.113 | -24% | 3.125 | 0.001 |
| B | 2 | BTC/USDT | ma_cross | `kind=dema,pair=(20, 100)` | filtre=low_vol · çıkış=stop_atr=2.0,be_r=1.0 | +105% | +90% | +613% | 1.1 | -38% | 2.737 | 0.001 |
| B | 2 | BTC/USDT | ichimoku_cloud | `cfg=(9, 26, 52)` | filtre=low_vol · çıkış=stop_atr=2.0,be_r=1.0 | +55% | +84% | +611% | 1.095 | -33% | 2.035 | 0.001 |
| B | 2 | ETH/USDT | bollinger_breakout | `n=50,k=2.5` | filtre=regime_bench200 · çıkış=trail_atr=3.0 | +136% | +148% | +906% | 1.09 | -28% | 2.41 | 0.001 |
| B | 2 | SOL/USDT | roc_breakout | `n=10,th=10` | filtre=regime_bench200 · çıkış=signal_only | +81% | +119% | +335% | 0.91 | -25% | 2.144 | 0.001 |
| B | 2 | UNI/USDT | down_days | `n=5,hold_exit=3` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=pivot_bounce(≤3 bar) | +61% | +158% | +208% | 0.866 | -23% | 1.682 | 0.001 |
| B | 1 | SOL/USDT | donchian_breakout | `entry=100,exit=10` | çıkış=stop_atr=2.0,trail_atr=3.0 | +87% | +158% | +277% | 0.836 | -36% | 1.82 | 0.001 |
| B | 2 | OP/USDT | trix_cross | `n=21,signal=7` | filtre=regime_bench200 · çıkış=stop_atr=2.0,max_hold=10 | +85% | veri yok | +160% | 0.816 | -30% | 1.693 | 0.001 |
| B | 1 | ADA/USDT | ma_cross | `kind=kama,pair=(50, 200)` | çıkış=stop_atr=2.0,trail_atr=3.0 | +116% | veri yok | +101% | 0.797 | -21% | 2.294 | 0.001 |
| B | 2 | BNB/USDT | supertrend_flip | `cfg=(7, 2.0)` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_choch(≤0 bar) | +24% | veri yok | +37% | 0.676 | -23% | 2.026 | 0.001 |
| B | 1 | BNB/USDT | wavetrend_reversal | `n1=10,n2=26,lo=-40` | çıkış=stop_atr=2.0,trail_atr=3.0 | +62% | veri yok | +59% | 0.671 | -19% | 1.465 | 0.001 |
| B | 2 | ETH/USDT | donchian_breakout | `entry=55,exit=20` | filtre=low_vol · çıkış=trail_atr=3.0 | +61% | +59% | +686% | 1.034 | -28% | 2.186 | 0.0 |
| B | 2 | ETH/USDT | donchian_breakout | `entry=55,exit=20` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_fvg(≤3 bar) | +94% | +102% | +563% | 1.034 | -34% | 2.521 | 0.0 |
| B | 2 | BTC/USDT | atr_breakout | `n=20,k=1.5` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=ma_cross(≤0 bar) | +47% | +87% | +127% | 1.012 | -9% | 4.178 | 0.0 |
| B | 2 | TRX/USDT | ma_cross | `kind=sma,pair=(5, 20)` | filtre=trend_sma200 · çıkış=stop_atr=2.0,tp_r=3.0 | +49% | +78% | +872% | 1.011 | -34% | 1.678 | 0.0 |
| B | 2 | XRP/USDT | roc_breakout | `n=10,th=10` | filtre=trend_sma200 · çıkış=stop_atr=2.0,max_hold=10 | +118% | +173% | +878% | 0.982 | -33% | 2.245 | 0.0 |
| B | 2 | ETH/USDT | high_52w_break | `n=126,exit_ma=50` | filtre=low_vol · çıkış=signal_only | +74% | +100% | +700% | 0.979 | -33% | 2.656 | 0.0 |
| B | 2 | BTC/USDT | donchian_breakout | `entry=55,exit=20` | filtre=low_vol · çıkış=stop_atr=2.0,be_r=1.0 | +43% | +38% | +601% | 0.973 | -39% | 2.729 | 0.0 |
| B | 2 | BTC/USDT | bb_squeeze | `n=20,q=0.2,look=252` | filtre=htf_week_sma10 · çıkış=stop_atr=2.0,be_r=1.0 | +45% | +54% | +253% | 0.973 | -20% | 2.33 | 0.0 |
| B | 1 | XRP/USDT | high_52w_break | `n=126,exit_ma=50` | çıkış=stop_atr=2.0,trail_atr=3.0 | +141% | +157% | +740% | 0.956 | -39% | 2.54 | 0.0 |
| B | 2 | ETH/USDT | triple_ma | `set=(10, 50, 200),kind=ema` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_fvg(≤5 bar) | +43% | +30% | +266% | 0.956 | -18% | 3.065 | 0.0 |
| B | 2 | ETH/USDT | bollinger_breakout | `n=50,k=2.5` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_bos(≤3 bar) | +97% | +80% | +444% | 0.937 | -22% | 2.29 | 0.0 |
| B | 2 | ETH/USDT | atr_breakout | `n=10,k=1.5` | filtre=low_vol · çıkış=signal_only | +37% | +41% | +405% | 0.935 | -29% | 1.757 | 0.0 |
| B | 2 | ETH/USDT | price_ma | `kind=sma,n=150` | filtre=regime_bench200 · çıkış=stop_atr=2.0,trail_atr=3.0 | +96% | +65% | +332% | 0.931 | -26% | 2.05 | 0.0 |
| B | 2 | NEAR/USDT | macd_cross | `cfg=(12, 26, 9),zero_filter=True` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_order_block(≤5 bar) | +109% | +178% | +283% | 0.918 | -36% | 2.234 | 0.0 |
| B | 2 | ETH/USDT | linreg_slope | `n=100,th=0.0005` | filtre=regime_bench200 · çıkış=trail_atr=3.0 | +58% | +44% | +239% | 0.914 | -26% | 2.658 | 0.0 |
| B | 1 | BTC/USDT | bollinger_breakout | `n=50,k=2.0` | çıkış=stop_atr=2.0,trail_atr=3.0 | +100% | +124% | +385% | 0.894 | -26% | 1.756 | 0.0 |
| B | 2 | ETH/USDT | atr_breakout | `n=10,k=1.5` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_bos(≤5 bar) | +49% | +30% | +353% | 0.878 | -25% | 1.705 | 0.0 |
| B | 1 | ETH/USDT | bollinger_breakout | `n=50,k=2.5` | çıkış=stop_atr=2.0,trail_atr=3.0 | +81% | +50% | +498% | 0.871 | -29% | 1.917 | 0.0 |
| B | 1 | BTC/USDT | bb_squeeze | `n=20,q=0.2,look=252` | çıkış=stop_atr=2.0,trail_atr=3.0 | +65% | +69% | +256% | 0.855 | -28% | 1.683 | 0.0 |
| B | 1 | ETH/USDT | linreg_slope | `n=100,th=0.0005` | çıkış=stop_atr=2.0,trail_atr=3.0 | +53% | +39% | +258% | 0.825 | -39% | 2.102 | 0.0 |
| B | 1 | BTC/USDT | triple_ma | `set=(10, 50, 200),kind=ema` | çıkış=stop_atr=2.0,trail_atr=3.0 | +117% | +122% | +231% | 0.815 | -40% | 1.863 | 0.0 |
| B | 1 | MANA/USDT | hammer_star | `lookback_low=10` | çıkış=stop_atr=2.0,trail_atr=3.0 | +35% | +169% | +254% | 0.812 | -34% | 1.671 | 0.0 |
| B | 2 | ETH/USDT | high_52w_break | `n=126,exit_ma=50` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=roc_breakout(≤3 bar) | +22% | +38% | +199% | 0.811 | -19% | 2.669 | 0.0 |
| B | 2 | BTC/USDT | ichimoku_cloud | `cfg=(9, 26, 52)` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_fvg(≤3 bar) | +90% | +151% | +195% | 0.797 | -27% | 1.872 | 0.0 |
| B | 2 | LTC/USDT | williams_reversal | `n=21,lo=-95` | filtre=adx20 · çıkış=stop_atr=2.0,trail_atr=3.0 | +33% | +74% | +494% | 0.792 | -34% | 1.563 | 0.0 |
| B | 2 | UNI/USDT | down_days | `n=5,hold_exit=3` | filtre=trend_sma200 · çıkış=signal_only | +178% | +221% | +240% | 0.791 | -38% | 2.931 | 0.0 |
| B | 2 | ETH/USDT | volume_breakout | `n=20,rv=1.5` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_fvg(≤5 bar) | +69% | +86% | +168% | 0.782 | -28% | 2.528 | 0.0 |
| B | 2 | LINK/USDT | smc_ote | `k=8,fib_lo=0.5` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_fvg(≤0 bar) | +30% | +62% | +91% | 0.778 | -14% | 2.056 | 0.0 |
| B | 2 | MANA/USDT | bollinger_reversion | `n=30,k=3.0` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=pivot_bounce(≤5 bar) | +49% | +85% | +83% | 0.764 | -24% | 2.313 | 0.0 |
| B | 2 | SNX/USDT | rsi_divergence | `n=14,k=3,exit_level=70` | filtre=regime_bench200 · çıkış=stop_atr=2.0,max_hold=10 | +56% | +76% | +79% | 0.761 | -20% | 1.742 | 0.0 |
| B | 2 | LINK/USDT | atr_breakout | `n=10,k=2.0` | filtre=low_vol · çıkış=stop_atr=2.0,be_r=1.0 | +106% | +113% | +92% | 0.759 | -27% | 2.256 | 0.0 |
| B | 2 | MANA/USDT | hammer_star | `lookback_low=10` | çıkış=trail_atr=3.0 | +12% | +140% | +218% | 0.742 | -36% | 1.647 | 0.0 |
| B | 2 | SOL/USDT | smc_choch | `k=3` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=roc_breakout(≤3 bar) | +64% | +102% | +102% | 0.733 | -25% | 2.54 | 0.0 |
| B | 2 | ADA/USDT | cmf_flow | `n=20,th=0.2` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=donchian_breakout(≤3 bar) | +79% | veri yok | +107% | 0.732 | -35% | 2.055 | 0.0 |
| B | 2 | BTC/USDT | smc_bos | `k=8` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=ma_cross(≤5 bar) | +38% | +68% | +142% | 0.731 | -31% | 1.988 | 0.0 |
| B | 2 | SOL/USDT | bb_squeeze | `n=20,q=0.2,look=252` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_bos(≤0 bar) | +34% | +93% | +127% | 0.726 | -32% | 1.721 | 0.0 |
| B | 2 | BTC/USDT | rsi_midline | `n=28,level=60` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=donchian_breakout(≤0 bar) | +11% | +41% | +166% | 0.72 | -30% | 1.759 | 0.0 |
| B | 2 | SOL/USDT | aroon_cross | `n=14` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_ote(≤3 bar) | +80% | +114% | +114% | 0.7 | -29% | 2.044 | 0.0 |
| B | 2 | TRX/USDT | smc_order_block | `k=3,max_age=20` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_choch(≤5 bar) | +50% | +52% | +162% | 0.698 | -28% | 2.04 | 0.0 |
| B | 1 | BCH/USDT | down_days | `n=5,hold_exit=3` | çıkış=stop_atr=2.0,trail_atr=3.0 | +9% | +39% | +274% | 0.694 | -37% | 1.42 | 0.0 |
| B | 2 | DOGE/USDT | ultimate_reversal | `a=5,lo=30` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=pivot_bounce(≤3 bar) | +24% | +92% | +92% | 0.685 | -22% | 2.437 | 0.0 |
| B | 1 | SOL/USDT | volume_breakout | `n=50,rv=1.5` | çıkış=stop_atr=2.0,trail_atr=3.0 | +101% | +93% | +132% | 0.66 | -36% | 1.73 | 0.0 |
| B | 1 | ETH/USDT | high_52w_break | `n=126,exit_ma=50` | çıkış=stop_atr=2.0,trail_atr=3.0 | +44% | +29% | +244% | 0.658 | -31% | 1.642 | 0.0 |
| B | 2 | LTC/USDT | stoch_reversal | `k=21,d=5,smooth=1,lo=10` | filtre=regime_bench200 · çıkış=stop_atr=2.0,tp_r=3.0 | +17% | +63% | +197% | 0.653 | -30% | 1.586 | 0.0 |
| B | 2 | SOL/USDT | obv_trend | `n=20,price_n=50` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=donchian_breakout(≤3 bar) | +53% | +68% | +72% | 0.652 | -24% | 2.214 | 0.0 |
| B | 2 | BTC/USDT | cci_breakout | `n=40,level=100` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=ma_cross(≤0 bar) | +25% | +40% | +55% | 0.649 | -10% | 2.532 | 0.0 |
| B | 2 | NEAR/USDT | macd_cross | `cfg=(12, 26, 9),zero_filter=True` | filtre=regime_bench200 · çıkış=stop_atr=2.0,be_r=1.0 | +64% | +81% | +187% | 0.646 | -39% | 1.617 | 0.0 |
| B | 2 | UNI/USDT | ultimate_reversal | `a=7,lo=35` | filtre=htf_week_sma10 · çıkış=stop_atr=2.0,max_hold=10 | +51% | +90% | +93% | 0.639 | -32% | 1.638 | 0.0 |
| B | 2 | ADA/USDT | trix_cross | `n=21,signal=9` | filtre=low_vol · çıkış=trail_atr=3.0 | +12% | veri yok | +99% | 0.639 | -34% | 1.488 | 0.0 |
| B | 2 | AVAX/USDT | atr_breakout | `n=20,k=1.5` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=roc_breakout(≤3 bar) | +109% | +138% | +113% | 0.632 | -27% | 1.943 | 0.0 |
| B | 2 | DOT/USDT | bb_squeeze | `n=20,q=0.2,look=126` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_order_block(≤5 bar) | +82% | +46% | +97% | 0.628 | -40% | 2.105 | 0.0 |
| B | 2 | AVAX/USDT | macd_divergence | `k=3,fast=12,slow=26` | filtre=regime_bench200 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +130% | +109% | +89% | 0.627 | -33% | 1.6 | 0.0 |
| B | 1 | BTC/USDT | atr_breakout | `n=20,k=1.5` | çıkış=stop_atr=2.0,trail_atr=3.0 | +40% | +55% | +176% | 0.609 | -36% | 1.386 | 0.0 |
| B | 1 | TRX/USDT | wavetrend_reversal | `n1=9,n2=26,lo=-60` | çıkış=stop_atr=2.0,trail_atr=3.0 | +19% | +17% | +122% | 0.607 | -37% | 2.096 | 0.0 |
| B | 2 | BCH/USDT | down_days | `n=5,hold_exit=3` | filtre=adx20 · çıkış=stop_atr=2.0,trail_atr=3.0 | +12% | +10% | +175% | 0.607 | -28% | 1.435 | 0.0 |
| B | 1 | ETH/USDT | ma_cross | `kind=kama,pair=(50, 150)` | çıkış=stop_atr=2.0,trail_atr=3.0 | +36% | +35% | +109% | 0.594 | -19% | 1.826 | 0.0 |
| B | 2 | ETH/USDT | smc_liquidity_sweep | `k=3` | filtre=low_vol · çıkış=trail_atr=3.0 | +76% | +109% | +122% | 0.593 | -28% | 1.277 | 0.0 |
| B | 1 | ADA/USDT | adx_trend | `n=14,th=25` | çıkış=stop_atr=2.0,trail_atr=3.0 | +64% | veri yok | +81% | 0.585 | -39% | 1.772 | 0.0 |
| B | 1 | XRP/USDT | rsi_reversal | `n=7,lo=10,exit=50` | çıkış=stop_atr=2.0,trail_atr=3.0 | +54% | +80% | +101% | 0.582 | -24% | 2.047 | 0.0 |
| B | 1 | DOGE/USDT | ultimate_reversal | `a=5,lo=30` | çıkış=stop_atr=2.0,trail_atr=3.0 | +11% | +68% | +84% | 0.579 | -39% | 1.608 | 0.0 |
| B | 2 | TRX/USDT | wavetrend_reversal | `n1=9,n2=26,lo=-60` | çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +16% | +10% | +92% | 0.571 | -37% | 1.912 | 0.0 |
| B | 1 | BTC/USDT | aroon_cross | `n=50` | çıkış=stop_atr=2.0,trail_atr=3.0 | +72% | +80% | +134% | 0.567 | -33% | 1.449 | 0.0 |
| B | 2 | ADA/USDT | ichimoku_cloud | `cfg=(9, 26, 52)` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_fvg(≤0 bar) | +30% | veri yok | +46% | 0.567 | -27% | 2.03 | 0.0 |
| B | 2 | XRP/USDT | ultimate_reversal | `a=5,lo=30` | filtre=adx20 · çıkış=stop_atr=2.0,tp_r=3.0 | +30% | +53% | +74% | 0.564 | -26% | 1.695 | 0.0 |
| B | 2 | TRX/USDT | ma_cross | `kind=sma,pair=(5, 20)` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_fvg(≤3 bar) | +23% | +30% | +89% | 0.556 | -24% | 1.673 | 0.0 |
| B | 2 | TRX/USDT | volume_breakout | `n=50,rv=1.5` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_fvg(≤3 bar) | +2% | +2% | +81% | 0.549 | -21% | 3.004 | 0.0 |
| B | 1 | TRX/USDT | rsi_reversal | `n=28,lo=35,exit=50` | çıkış=stop_atr=2.0,trail_atr=3.0 | +12% | +67% | +110% | 0.547 | -36% | 1.551 | 0.0 |
| B | 2 | DOGE/USDT | ultimate_reversal | `a=5,lo=30` | filtre=adx20 · çıkış=stop_atr=2.0,trail_atr=3.0 | +6% | +52% | +66% | 0.517 | -37% | 1.613 | 0.0 |
| B | 1 | XRP/USDT | volume_breakout | `n=50,rv=1.5` | çıkış=stop_atr=2.0,trail_atr=3.0 | +53% | +97% | +146% | 0.516 | -38% | 1.645 | 0.0 |
| B | 2 | XRP/USDT | rsi_reversal | `n=7,lo=10,exit=50` | çıkış=signal_only | +29% | +46% | +74% | 0.44 | -31% | 2.308 | 0.0 |

## Coin coin özet (ajan günlüğü)

- **AAVE/USDT**: 78 aday denendi, 0 kaldı. En iyi aday rsi_reversal (`n=5,lo=10,exit=50`, çıkış=stop_atr=2.0,trail_atr=3.0): S7 — PSR 0.803.
- **ADA/USDT**: 108 aday denendi, 10 kaldı. En iyi aday cmf_flow (`n=20,th=0.2`, filtre=adx20 · çıkış=signal_only): OK — tüm adımlar geçti.
- **ALGO/USDT**: 66 aday denendi, 0 kaldı. En iyi aday adx_trend (`n=14,th=25`, filtre=trend_sma200 · çıkış=stop_atr=2.0,trail_atr=3.0): S4 — komşu ayarların %25'i kârlı.
- **APT/USDT**: 66 aday denendi, 0 kaldı. En iyi aday wavetrend_reversal (`n1=9,n2=26,lo=-60`, çıkış=stop_atr=2.0,trail_atr=3.0): S6 — yılların %25'i kârlı.
- **ARB/USDT**: 94 aday denendi, 5 kaldı. En iyi aday smc_choch (`k=8`, filtre=regime_bench200 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0): OK — tüm adımlar geçti.
- **ATOM/USDT**: 68 aday denendi, 0 kaldı. En iyi aday rsi_divergence (`n=14,k=3,exit_level=70`, çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_liquidity_sweep(≤3 bar)): S7 — PSR 0.875.
- **AVAX/USDT**: 66 aday denendi, 2 kaldı. En iyi aday atr_breakout (`n=20,k=1.5`, çıkış=stop_atr=2.0,trail_atr=3.0 · onay=roc_breakout(≤3 bar)): OK — tüm adımlar geçti.
- **AXS/USDT**: 62 aday denendi, 0 kaldı. En iyi aday rsi_reversal (`n=28,lo=20,exit=60`, çıkış=stop_atr=2.0,trail_atr=3.0): S1 — 3y +8%, 5y +8%, full +8%; 1 işlem.
- **BCH/USDT**: 70 aday denendi, 2 kaldı. En iyi aday down_days (`n=5,hold_exit=3`, çıkış=stop_atr=2.0,trail_atr=3.0): OK — tüm adımlar geçti.
- **BNB/USDT**: 100 aday denendi, 10 kaldı. En iyi aday macd_zero (`cfg=(12, 26, 9)`, çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_choch(≤5 bar)): OK — tüm adımlar geçti.
- **BTC/USDT**: 88 aday denendi, 19 kaldı. En iyi aday rsi_midline (`n=28,level=60`, filtre=low_vol · çıkış=stop_atr=2.0,be_r=1.0): OK — tüm adımlar geçti.
- **CRV/USDT**: 64 aday denendi, 0 kaldı. En iyi aday wavetrend_reversal (`n1=9,n2=18,lo=-60`, çıkış=stop_atr=2.0,trail_atr=3.0): S2 — PF 1.285, 1x maks. düşüş -58%.
- **DOGE/USDT**: 73 aday denendi, 3 kaldı. En iyi aday ultimate_reversal (`a=5,lo=30`, çıkış=stop_atr=2.0,trail_atr=3.0 · onay=pivot_bounce(≤3 bar)): OK — tüm adımlar geçti.
- **DOT/USDT**: 68 aday denendi, 2 kaldı. En iyi aday macd_divergence (`k=3,fast=12,slow=26`, filtre=regime_bench200 · çıkış=stop_atr=2.0,be_r=1.0): OK — tüm adımlar geçti.
- **ETC/USDT**: 66 aday denendi, 0 kaldı. En iyi aday coppock_turn (`scale=5`, filtre=trend_sma200 · çıkış=stop_atr=2.0,be_r=1.0): S6 — yılların %56'i kârlı.
- **ETH/USDT**: 84 aday denendi, 18 kaldı. En iyi aday price_ma (`kind=sma,n=150`, çıkış=stop_atr=2.0,trail_atr=3.0): OK — tüm adımlar geçti.
- **FIL/USDT**: 70 aday denendi, 0 kaldı. En iyi aday hammer_star (`lookback_low=10`, filtre=adx20 · çıkış=trail_atr=3.0): S5 — 1 bar geç girişte Sharpe'ın %36'i kalıyor.
- **IMX/USDT**: 74 aday denendi, 0 kaldı. En iyi aday smc_ote (`k=8,fib_lo=0.618`, çıkış=stop_atr=2.0,tp_r=3.0): S5 — 1 bar geç girişte Sharpe'ın %0'i kalıyor.
- **INJ/USDT**: 81 aday denendi, 8 kaldı. En iyi aday cmf_flow (`n=10,th=0.2`, filtre=regime_bench200 · çıkış=stop_atr=2.0,max_hold=10): OK — tüm adımlar geçti.
- **LINK/USDT**: 74 aday denendi, 2 kaldı. En iyi aday smc_ote (`k=8,fib_lo=0.5`, çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_fvg(≤0 bar)): OK — tüm adımlar geçti.
- **LTC/USDT**: 66 aday denendi, 2 kaldı. En iyi aday williams_reversal (`n=21,lo=-95`, filtre=adx20 · çıkış=stop_atr=2.0,trail_atr=3.0): OK — tüm adımlar geçti.
- **MANA/USDT**: 66 aday denendi, 3 kaldı. En iyi aday hammer_star (`lookback_low=10`, çıkış=stop_atr=2.0,trail_atr=3.0): OK — tüm adımlar geçti.
- **MINA/USDT**: 71 aday denendi, 1 kaldı. En iyi aday adx_trend (`n=20,th=20`, filtre=regime_bench200 · çıkış=stop_atr=2.0,be_r=1.0): OK — tüm adımlar geçti.
- **NEAR/USDT**: 80 aday denendi, 2 kaldı. En iyi aday macd_cross (`cfg=(12, 26, 9),zero_filter=True`, çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_order_block(≤5 bar)): OK — tüm adımlar geçti.
- **OP/USDT**: 64 aday denendi, 1 kaldı. En iyi aday trix_cross (`n=21,signal=7`, filtre=regime_bench200 · çıkış=stop_atr=2.0,max_hold=10): OK — tüm adımlar geçti.
- **PYTH/USDT**: elendi (S0: 2.9 yıl veri var, en az 3.0 yıl gerekli).
- **SAND/USDT**: 67 aday denendi, 0 kaldı. En iyi aday rsi_divergence (`n=14,k=3,exit_level=70`, çıkış=stop_atr=2.0,trail_atr=3.0 · onay=pivot_bounce(≤3 bar)): S7 — PSR 0.861.
- **SNX/USDT**: 64 aday denendi, 1 kaldı. En iyi aday rsi_divergence (`n=14,k=3,exit_level=70`, filtre=regime_bench200 · çıkış=stop_atr=2.0,max_hold=10): OK — tüm adımlar geçti.
- **SOL/USDT**: 103 aday denendi, 16 kaldı. En iyi aday adx_trend (`n=10,th=20`, filtre=regime_bench200 · çıkış=signal_only): OK — tüm adımlar geçti.
- **SUI/USDT**: 99 aday denendi, 9 kaldı. En iyi aday bollinger_reversion (`n=30,k=2.5`, filtre=adx20 · çıkış=stop_atr=2.0,max_hold=10): OK — tüm adımlar geçti.
- **THETA/USDT**: 65 aday denendi, 0 kaldı. En iyi aday wavetrend_reversal (`n1=9,n2=26,lo=-60`, çıkış=stop_atr=2.0,trail_atr=3.0): S4 — komşu ayarların %33'i kârlı.
- **TRX/USDT**: 79 aday denendi, 7 kaldı. En iyi aday ma_cross (`kind=sma,pair=(5, 20)`, filtre=trend_sma200 · çıkış=stop_atr=2.0,tp_r=3.0): OK — tüm adımlar geçti.
- **UNI/USDT**: 76 aday denendi, 3 kaldı. En iyi aday down_days (`n=5,hold_exit=3`, çıkış=stop_atr=2.0,trail_atr=3.0 · onay=pivot_bounce(≤3 bar)): OK — tüm adımlar geçti.
- **XLM/USDT**: 103 aday denendi, 11 kaldı. En iyi aday keltner_breakout (`n=20,k=2.0`, filtre=adx20 · çıkış=stop_atr=2.0,be_r=1.0): OK — tüm adımlar geçti.
- **XRP/USDT**: 77 aday denendi, 7 kaldı. En iyi aday high_52w_break (`n=126,exit_ma=50`, filtre=regime_bench200 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0): OK — tüm adımlar geçti.

## Zayıf yönler (dürüst liste)

- 40897 deneme yapıldı. Bu kadar çok denemede şans eseri iyi görünen strateji çıkar. DSR bunu düzeltir; tier A sadece DSR ≥ eşik olanlardır.
- Seçim ve test aynı geçmiş veride yapıldı. Gerçek test arenadaki ileri (paper) kayıttır.
- Survivorship: liste bugünün coinlerinden oluşur. Borsadan silinen coinler yok, bu sonucu iyimser yapar.
- Funding sabit yıllık oranla, likidasyon işlem bazında yaklaşık modellenir.
- Tek borsa verisi (Bitget, yoksa OKX/KuCoin). Emir defteri ve piyasa etkisi modellenmez.

## Arena

Arena: 100 aktif (eleme geçen), 0 kontrol (yakın aday, switcher kullanmaz), 100 yeni üye, 0 kontrolden aktife. Üst sınır 100.

## Switcher backtest kapısı

Geçti: **False** — kontroller: `{"beats_equal_weight_all_windows": false, "positive_at_cost_stress": true, "max_dd_ok": true}`

Pencereler: `{"3y": {"sharpe": 1.562, "ew_sharpe": 2.963}, "5y": {"sharpe": 1.049, "ew_sharpe": 2.35}, "full": {"sharpe": 1.4, "ew_sharpe": 2.266}}`
