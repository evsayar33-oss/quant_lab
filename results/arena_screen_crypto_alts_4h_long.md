# Eleme motoru — crypto_alts 4h_long (yön: long)

Veri: 2018-01-01 → 2026-11-02. Coin: 34 uygun (toplam 35). Denenen varyant: 592 × coin = **40067 deneme**.
Her (coin, kural) için tek en iyi nokta değil, **en sağlam bölgenin merkezi** seçildi. Bu bir aday listesidir, karar değildir. Karar sadece doğrulama kapısında verilir.

> ⚠️ **Zaman makinesi kontrolü önerilir.** Bu liste binlerce deneme arasından seçildi; seçim süreçleri backtest'te iyi görünüp ileride çökebilir (2026-10-17 ve 10-19 testleri). Gerçek paraya aday olmadan önce `Time machine test` workflow'unu aynı yön (side) ve zaman dilimiyle çalıştırın. Kural: CLAUDE.md / AGENTS.md.

## Huni

| Adım | Ne kontrol edilir | Elenen | Kalan |
|---|---|---|---|
| S0 | veri yetersiz | 68 | 2312 |
| S1 | her dönemde kârlı değil / az işlem | 2064 | 248 |
| S2 | kâr faktörü veya düşüş zayıf | 183 | 65 |
| S3 | yüksek maliyette zarar | 4 | 61 |
| S4 | plato yok (komşu ayarlar zararda) | 10 | 51 |
| S5 | 1 bar gecikmeye dayanıksız | 4 | 47 |
| S6 | yılların çoğunda kârlı değil | 14 | 33 |
| S7 | istatistiksel güven düşük (PSR) | 7 | 26 |

## 2. aşama: filtre × çıkış × kombo (sadece S1'i geçen adaylarda)

248 aday → 19939 ek deneme (DSR'a eklendi). Her aday için en sağlam filtre/çıkış hücresi ve en sağlam kombo seçildi; kombo sadece kuralı tek başına geçerse aday olur. Seçilenler aynı S1–S7 adımlarından geçti.

| Adım | Ne kontrol edilir | Elenen | Kalan |
|---|---|---|---|
| S0 | veri yetersiz | 0 | 421 |
| S1 | her dönemde kârlı değil / az işlem | 139 | 282 |
| S2 | kâr faktörü veya düşüş zayıf | 119 | 163 |
| S3 | yüksek maliyette zarar | 4 | 159 |
| S4 | plato yok (komşu ayarlar zararda) | 36 | 123 |
| S5 | 1 bar gecikmeye dayanıksız | 6 | 117 |
| S6 | yılların çoğunda kârlı değil | 22 | 95 |
| S7 | istatistiksel güven düşük (PSR) | 1 | 94 |

## Geçenler (120)

Kazanma oranı tek başına bir şey söylemez. Sistem sadece **kazanma oranı > başabaş oranı** olduğunda kârlıdır. Başabaş = 1 / (1 + ödeme oranı); ödeme oranı = ortalama kazanç / ortalama kayıp (maliyet sonrası). Pay = kazanma oranı − başabaş. Beklenen = işlem başına ortalama net getiri.

| Tier | Aşama | Coin | Kural | Ayar | Varyant | 3y | 5y | Tüm | Sharpe | 1x DD | PF | Kazanma | Ödeme | Başabaş | Pay | Beklenen | DSR |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| B | 2 | SOL/USDT | smc_choch | `k=8` | filtre=regime_bench200 · çıkış=stop_atr=2.0,be_r=1.0 | +129% | +1471% | +23551% | 1.826 | -37% | 8.316 | 39% | 12.82 | 7% | +32% | +13.45% | 0.32 |
| B | 2 | ARB/USDT | ma_cross | `kind=sma,pair=(20, 50)` | filtre=regime_bench200 · çıkış=stop_atr=2.0,max_hold=10 | +112% | veri yok | +262% | 1.352 | -31% | 2.755 | 51% | 2.64 | 28% | +24% | +3.26% | 0.067 |
| B | 2 | SUI/USDT | bollinger_reversion | `n=30,k=2.5` | filtre=adx20 · çıkış=stop_atr=2.0,max_hold=10 | +270% | veri yok | +234% | 1.238 | -22% | 2.25 | 57% | 1.688 | 37% | +20% | +1.99% | 0.064 |
| B | 2 | ARB/USDT | smc_choch | `k=8` | filtre=regime_bench200 · çıkış=stop_atr=2.0,tp_r=3.0 | +195% | veri yok | +249% | 1.206 | -33% | 2.199 | 43% | 2.894 | 26% | +18% | +3.45% | 0.061 |
| B | 2 | INJ/USDT | wavetrend_reversal | `n1=12,n2=21,lo=-53` | filtre=low_vol · çıkış=stop_atr=2.0,tp_r=3.0 | +138% | +391% | +840% | 1.41 | -30% | 2.922 | 58% | 2.11 | 32% | +26% | +4.24% | 0.058 |
| B | 2 | ARB/USDT | macd_divergence | `k=3,fast=12,slow=26` | filtre=regime_bench200 · çıkış=stop_atr=2.0,be_r=1.0 | +326% | veri yok | +282% | 1.209 | -30% | 2.587 | 26% | 7.164 | 12% | +14% | +3.72% | 0.047 |
| B | 2 | ARB/USDT | atr_breakout | `n=10,k=2.0` | filtre=regime_bench200 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +83% | veri yok | +124% | 1.085 | -26% | 2.347 | 57% | 1.788 | 36% | +21% | +2.44% | 0.03 |
| B | 2 | OP/USDT | keltner_breakout | `n=20,k=2.5` | filtre=trend_sma200 · çıkış=stop_atr=2.0,max_hold=10 | +72% | veri yok | +359% | 1.179 | -27% | 2.383 | 62% | 1.466 | 40% | +21% | +2.99% | 0.029 |
| B | 2 | SUI/USDT | atr_breakout | `n=20,k=2.0` | filtre=regime_bench200 · çıkış=stop_atr=2.0,max_hold=10 | +120% | veri yok | +108% | 0.979 | -17% | 2.311 | 58% | 1.651 | 38% | +21% | +2.39% | 0.021 |
| B | 1 | SUI/USDT | wavetrend_reversal | `n1=9,n2=26,lo=-60` | çıkış=stop_atr=2.0,trail_atr=3.0 | +109% | veri yok | +138% | 0.953 | -31% | 2.335 | 52% | 2.189 | 31% | +20% | +3.65% | 0.02 |
| B | 2 | SOL/USDT | smc_fvg | `max_age=20,min_gap_atr=0.0` | filtre=regime_bench200 · çıkış=signal_only | +98% | +414% | +3062% | 1.198 | -38% | 1.6 | 33% | 3.256 | 24% | +10% | +0.93% | 0.019 |
| B | 2 | BTC/USDT | rsi_midline | `n=28,level=60` | filtre=low_vol · çıkış=stop_atr=2.0,be_r=1.0 | +57% | +95% | +2112% | 1.322 | -38% | 3.295 | 29% | 7.964 | 11% | +18% | +3.29% | 0.018 |
| B | 2 | ETH/USDT | roc_breakout | `n=126,th=5` | filtre=trend_sma200 · çıkış=trail_atr=3.0 | +73% | +54% | +1670% | 1.318 | -29% | 2.93 | 46% | 3.458 | 22% | +23% | +2.71% | 0.017 |
| B | 2 | SUI/USDT | bollinger_breakout | `n=20,k=2.5` | filtre=trend_sma200 · çıkış=stop_atr=2.0,max_hold=10 | +168% | veri yok | +142% | 0.893 | -26% | 1.717 | 50% | 1.717 | 37% | +13% | +1.61% | 0.016 |
| B | 2 | SUI/USDT | keltner_breakout | `n=50,k=2.5` | filtre=trend_sma200 · çıkış=stop_atr=2.0,max_hold=10 | +251% | veri yok | +161% | 0.891 | -32% | 1.612 | 48% | 1.727 | 37% | +12% | +1.47% | 0.016 |
| B | 1 | ARB/USDT | hurst_switch | `n=200,fast=20,rsi_n=5` | çıkış=stop_atr=2.0,trail_atr=3.0 | +143% | veri yok | +135% | 0.953 | -31% | 2.171 | 41% | 3.121 | 24% | +17% | +2.76% | 0.014 |
| B | 2 | SUI/USDT | wavetrend_reversal | `n1=9,n2=26,lo=-60` | çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +60% | veri yok | +94% | 0.854 | -34% | 2.033 | 58% | 1.468 | 40% | +18% | +2.67% | 0.013 |
| B | 2 | XRP/USDT | donchian_breakout | `entry=100,exit=10` | filtre=adx20 · çıkış=stop_atr=2.0,max_hold=10 | +241% | +308% | +3511% | 1.324 | -32% | 2.953 | 54% | 2.545 | 28% | +26% | +4.11% | 0.012 |
| B | 2 | ADA/USDT | volume_breakout | `n=50,rv=2.0` | filtre=htf_week_sma10 · çıkış=stop_atr=2.0,max_hold=10 | +90% | +83% | +1226% | 1.271 | -23% | 3.009 | 63% | 1.793 | 36% | +27% | +3.94% | 0.012 |
| B | 2 | ADA/USDT | bollinger_breakout | `n=50,k=2.5` | filtre=htf_week_sma10 · çıkış=stop_atr=2.0,be_r=1.0 | +306% | +241% | +3548% | 1.229 | -37% | 6.21 | 32% | 13.151 | 7% | +25% | +10.39% | 0.011 |
| B | 1 | SUI/USDT | bollinger_reversion | `n=30,k=2.5` | çıkış=stop_atr=2.0,trail_atr=3.0 | +141% | veri yok | +138% | 0.819 | -36% | 1.536 | 53% | 1.365 | 42% | +11% | +1.36% | 0.011 |
| B | 2 | XRP/USDT | high_52w_break | `n=126,exit_ma=50` | filtre=adx20 · çıkış=stop_atr=2.0,max_hold=10 | +259% | +303% | +3232% | 1.306 | -32% | 3.072 | 53% | 2.718 | 27% | +26% | +4.43% | 0.01 |
| B | 2 | SUI/USDT | volume_breakout | `n=50,rv=2.0` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=chop_switch(≤0 bar) | +115% | veri yok | +116% | 0.809 | -23% | 2.121 | 42% | 2.936 | 25% | +16% | +3.25% | 0.01 |
| B | 2 | BTC/USDT | atr_breakout | `n=20,k=1.5` | filtre=low_vol · çıkış=signal_only | +58% | +114% | +741% | 1.197 | -24% | 2.283 | 44% | 2.959 | 25% | +18% | +1.56% | 0.007 |
| B | 2 | BTC/USDT | price_ma | `kind=ema,n=150` | filtre=low_vol · çıkış=stop_atr=2.0,be_r=1.0 | +154% | +182% | +2433% | 1.185 | -38% | 2.881 | 14% | 17.807 | 5% | +9% | +2.02% | 0.007 |
| B | 2 | ADA/USDT | atr_breakout | `n=10,k=2.0` | filtre=htf_week_sma10 · çıkış=stop_atr=2.0,be_r=1.0 | +98% | +72% | +978% | 1.189 | -39% | 3.836 | 49% | 3.968 | 20% | +29% | +5.26% | 0.006 |
| B | 2 | ADA/USDT | donchian_breakout | `entry=100,exit=10` | çıkış=stop_atr=2.0,max_hold=10 | +92% | +92% | +1957% | 1.165 | -33% | 2.14 | 55% | 1.742 | 36% | +19% | +2.32% | 0.006 |
| B | 2 | MINA/USDT | adx_trend | `n=20,th=20` | filtre=regime_bench200 · çıkış=stop_atr=2.0,be_r=1.0 | +184% | +223% | +504% | 0.968 | -33% | 3.802 | 26% | 10.772 | 8% | +18% | +5.84% | 0.006 |
| B | 2 | BTC/USDT | linreg_slope | `n=20,th=0.0005` | filtre=low_vol · çıkış=stop_atr=2.0,be_r=1.0 | +31% | +68% | +1195% | 1.149 | -36% | 2.052 | 31% | 4.576 | 18% | +13% | +1.41% | 0.005 |
| B | 2 | BTC/USDT | bollinger_breakout | `n=50,k=2.0` | filtre=trend_sma200 · çıkış=signal_only | +68% | +116% | +1320% | 1.133 | -32% | 2.41 | 40% | 3.661 | 22% | +18% | +2.72% | 0.004 |
| B | 2 | ETH/USDT | rsi_midline | `n=28,level=60` | filtre=low_vol · çıkış=signal_only | +109% | +118% | +2217% | 1.131 | -33% | 2.757 | 41% | 3.975 | 20% | +21% | +4.00% | 0.004 |
| B | 2 | BNB/USDT | macd_cross | `cfg=(19, 39, 9),zero_filter=False` | filtre=trend_sma200 · çıkış=stop_atr=2.0,tp_r=3.0 | +46% | +67% | +1409% | 1.117 | -31% | 1.768 | 38% | 2.952 | 25% | +12% | +1.13% | 0.004 |
| B | 1 | ETH/USDT | price_ma | `kind=sma,n=150` | çıkış=stop_atr=2.0,trail_atr=3.0 | +99% | +113% | +1123% | 1.123 | -40% | 2.046 | 26% | 5.927 | 14% | +11% | +1.30% | 0.003 |
| B | 2 | BNB/USDT | ma_cross | `kind=dema,pair=(10, 50)` | filtre=regime_bench200 · çıkış=signal_only | +82% | +61% | +1767% | 1.11 | -32% | 2.157 | 37% | 3.604 | 22% | +16% | +1.59% | 0.003 |
| B | 2 | NEAR/USDT | macd_cross | `cfg=(12, 26, 9),zero_filter=True` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_order_block(≤5 bar) | +109% | +178% | +345% | 0.969 | -36% | 2.347 | 37% | 4.037 | 20% | +17% | +2.85% | 0.003 |
| B | 2 | FIL/USDT | ichimoku_cloud | `cfg=(9, 26, 52)` | filtre=trend_sma200 · çıkış=stop_atr=2.0,trail_atr=3.0 | +114% | +183% | +604% | 0.96 | -36% | 2.231 | 32% | 4.639 | 18% | +15% | +2.60% | 0.003 |
| B | 2 | UNI/USDT | down_days | `n=5,hold_exit=3` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=pivot_bounce(≤3 bar) | +51% | +137% | +316% | 0.941 | -23% | 1.74 | 61% | 1.105 | 48% | +14% | +1.44% | 0.003 |
| B | 2 | INJ/USDT | mfi_reversal | `n=10,lo=10` | filtre=adx20 · çıkış=stop_atr=2.0,max_hold=10 | +108% | +121% | +221% | 0.921 | -27% | 2.174 | 62% | 1.346 | 43% | +19% | +1.95% | 0.003 |
| B | 2 | BTC/USDT | ma_cross | `kind=tema,pair=(20, 50)` | filtre=low_vol · çıkış=signal_only | +52% | +80% | +892% | 1.107 | -39% | 1.856 | 41% | 2.666 | 27% | +14% | +1.28% | 0.002 |
| B | 2 | ADA/USDT | keltner_breakout | `n=20,k=2.5` | filtre=htf_week_sma10 · çıkış=stop_atr=2.0,tp_r=3.0 | +129% | +87% | +673% | 1.05 | -35% | 2.369 | 48% | 2.517 | 28% | +20% | +3.78% | 0.002 |
| B | 2 | ETH/USDT | bollinger_breakout | `n=50,k=2.5` | filtre=regime_bench200 · çıkış=trail_atr=3.0 | +116% | +161% | +874% | 1.033 | -28% | 2.354 | 51% | 2.24 | 31% | +20% | +2.32% | 0.002 |
| B | 2 | BTC/USDT | ichimoku_cloud | `cfg=(9, 26, 52)` | filtre=low_vol · çıkış=stop_atr=2.0,be_r=1.0 | +55% | +84% | +612% | 1.024 | -33% | 1.938 | 33% | 3.955 | 20% | +13% | +1.14% | 0.002 |
| B | 2 | UNI/USDT | macd_divergence | `k=3,fast=12,slow=26` | filtre=htf_week_sma10 · çıkış=stop_atr=2.0,max_hold=10 | +52% | +113% | +211% | 0.897 | -23% | 1.963 | 53% | 1.723 | 37% | +16% | +1.77% | 0.002 |
| B | 2 | INJ/USDT | cmf_flow | `n=10,th=0.2` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=macd_divergence(≤5 bar) | +108% | +116% | +175% | 0.859 | -32% | 2.683 | 52% | 2.45 | 29% | +23% | +2.72% | 0.002 |
| B | 2 | UNI/USDT | down_days | `n=5,hold_exit=3` | filtre=trend_sma200 · çıkış=signal_only | +178% | +214% | +679% | 1.074 | -38% | 4.019 | 71% | 1.667 | 38% | +33% | +4.28% | 0.001 |
| B | 2 | ETH/USDT | donchian_breakout | `entry=100,exit=20` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=chop_switch(≤5 bar) | +96% | +80% | +595% | 0.998 | -30% | 2.531 | 44% | 3.245 | 24% | +20% | +2.67% | 0.001 |
| B | 2 | ETH/USDT | high_52w_break | `n=126,exit_ma=50` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=chop_switch(≤5 bar) | +88% | +81% | +548% | 0.993 | -23% | 2.677 | 47% | 2.966 | 25% | +22% | +2.89% | 0.001 |
| B | 2 | ADA/USDT | keltner_breakout | `n=20,k=2.5` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_bos(≤0 bar) | +38% | +97% | +480% | 0.979 | -31% | 4.266 | 50% | 4.266 | 19% | +31% | +5.24% | 0.001 |
| B | 2 | ETH/USDT | bollinger_breakout | `n=50,k=2.5` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_bos(≤3 bar) | +87% | +89% | +545% | 0.961 | -22% | 2.352 | 49% | 2.485 | 29% | +20% | +2.09% | 0.001 |
| B | 2 | ETH/USDT | high_52w_break | `n=126,exit_ma=50` | filtre=low_vol · çıkış=signal_only | +74% | +103% | +766% | 0.957 | -33% | 2.634 | 44% | 3.361 | 23% | +21% | +4.27% | 0.001 |
| B | 2 | TRX/USDT | ma_cross | `kind=sma,pair=(5, 20)` | filtre=trend_sma200 · çıkış=stop_atr=2.0,tp_r=3.0 | +40% | +90% | +847% | 0.933 | -34% | 1.616 | 37% | 2.715 | 27% | +10% | +0.92% | 0.001 |
| B | 2 | ATOM/USDT | macd_divergence | `k=3,fast=12,slow=26` | filtre=adx20 · çıkış=stop_atr=2.0,max_hold=10 | +11% | +109% | +343% | 0.865 | -37% | 1.685 | 55% | 1.404 | 42% | +13% | +1.09% | 0.001 |
| B | 1 | FIL/USDT | ma_cross | `kind=kama,pair=(50, 150)` | çıkış=stop_atr=2.0,trail_atr=3.0 | +14% | +55% | +296% | 0.834 | -35% | 2.46 | 41% | 3.568 | 22% | +19% | +3.78% | 0.001 |
| B | 2 | SNX/USDT | rsi_divergence | `n=14,k=3,exit_level=70` | filtre=regime_bench200 · çıkış=stop_atr=2.0,max_hold=10 | +56% | +86% | +108% | 0.802 | -20% | 1.842 | 55% | 1.501 | 40% | +15% | +1.80% | 0.001 |
| B | 2 | SOL/USDT | ma_cross | `kind=dema,pair=(10, 50)` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=rsi_midline(≤0 bar) | +88% | +332% | +239% | 0.791 | -37% | 2.328 | 49% | 2.425 | 29% | +20% | +3.21% | 0.001 |
| B | 2 | UNI/USDT | ultimate_reversal | `a=7,lo=35` | filtre=adx20 · çıkış=stop_atr=2.0,max_hold=10 | +56% | +102% | +276% | 0.784 | -31% | 1.603 | 53% | 1.425 | 41% | +12% | +1.39% | 0.001 |
| B | 2 | AAVE/USDT | rsi_reversal | `n=5,lo=10,exit=50` | filtre=adx20 · çıkış=signal_only | +99% | +144% | +160% | 0.77 | -34% | 2.322 | 77% | 0.693 | 59% | +18% | +1.49% | 0.001 |
| B | 2 | BTC/USDT | atr_breakout | `n=20,k=1.5` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=ma_cross(≤0 bar) | +47% | +87% | +138% | 1.006 | -9% | 4.349 | 66% | 2.269 | 31% | +35% | +2.71% | 0.0 |
| B | 2 | XLM/USDT | ma_cross | `kind=ema,pair=(20, 100)` | çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +65% | +135% | +391% | 0.96 | -22% | 2.08 | 55% | 1.715 | 37% | +18% | +1.87% | 0.0 |
| B | 2 | SNX/USDT | adx_trend | `n=14,th=30` | çıkış=stop_atr=2.0,max_hold=10 | +97% | +298% | +337% | 0.959 | -18% | 4.041 | 52% | 3.69 | 21% | +31% | +4.05% | 0.0 |
| B | 2 | XRP/USDT | volume_breakout | `n=50,rv=1.5` | filtre=adx20 · çıkış=stop_atr=2.0,max_hold=10 | +95% | +108% | +883% | 0.944 | -31% | 2.521 | 53% | 2.269 | 31% | +22% | +3.04% | 0.0 |
| B | 2 | XLM/USDT | atr_breakout | `n=10,k=2.0` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=rsi_midline(≤5 bar) | +25% | +99% | +657% | 0.94 | -32% | 3.392 | 46% | 4.071 | 20% | +26% | +4.16% | 0.0 |
| B | 1 | XRP/USDT | high_52w_break | `n=126,exit_ma=50` | çıkış=stop_atr=2.0,trail_atr=3.0 | +136% | +157% | +884% | 0.932 | -39% | 2.496 | 43% | 3.307 | 23% | +20% | +3.06% | 0.0 |
| B | 1 | XLM/USDT | ma_cross | `kind=ema,pair=(20, 100)` | çıkış=stop_atr=2.0,trail_atr=3.0 | +80% | +199% | +763% | 0.915 | -31% | 2.384 | 38% | 3.973 | 20% | +17% | +2.77% | 0.0 |
| B | 2 | BTC/USDT | bb_squeeze | `n=20,q=0.2,look=252` | filtre=htf_week_sma10 · çıkış=stop_atr=2.0,be_r=1.0 | +28% | +58% | +246% | 0.911 | -20% | 2.257 | 32% | 4.856 | 17% | +15% | +1.43% | 0.0 |
| B | 1 | BTC/USDT | bb_squeeze | `n=20,q=0.2,look=252` | çıkış=stop_atr=2.0,trail_atr=3.0 | +49% | +71% | +344% | 0.902 | -29% | 1.717 | 39% | 2.669 | 27% | +12% | +0.88% | 0.0 |
| B | 2 | ADA/USDT | donchian_breakout | `entry=100,exit=10` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_bos(≤5 bar) | +87% | +60% | +840% | 0.9 | -39% | 2.237 | 43% | 2.918 | 26% | +18% | +2.75% | 0.0 |
| B | 2 | DOGE/USDT | inside_bar | `trend_n=50` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=chop_switch(≤3 bar) | +82% | +109% | +2291% | 0.897 | -33% | 5.836 | 49% | 6.127 | 14% | +35% | +12.09% | 0.0 |
| B | 2 | ADA/USDT | roc_breakout | `n=10,th=10` | filtre=low_vol · çıkış=stop_atr=2.0,max_hold=10 | +48% | +55% | +398% | 0.882 | -29% | 2.072 | 53% | 1.857 | 35% | +18% | +2.09% | 0.0 |
| B | 1 | ETH/USDT | bollinger_breakout | `n=50,k=2.5` | çıkış=stop_atr=2.0,trail_atr=3.0 | +66% | +58% | +584% | 0.881 | -29% | 1.942 | 45% | 2.383 | 30% | +15% | +1.70% | 0.0 |
| B | 2 | ETH/USDT | linreg_slope | `n=100,th=0.0005` | filtre=regime_bench200 · çıkış=trail_atr=3.0 | +66% | +44% | +249% | 0.877 | -26% | 2.572 | 46% | 3.049 | 25% | +21% | +2.66% | 0.0 |
| B | 2 | DOGE/USDT | high_52w_break | `n=252,exit_ma=50` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=chop_switch(≤0 bar) | +46% | +60% | +1979% | 0.865 | -35% | 5.486 | 56% | 4.294 | 19% | +37% | +11.33% | 0.0 |
| B | 1 | MANA/USDT | hammer_star | `lookback_low=10` | çıkış=stop_atr=2.0,trail_atr=3.0 | +31% | +151% | +374% | 0.854 | -34% | 1.751 | 67% | 0.847 | 54% | +13% | +1.02% | 0.0 |
| B | 2 | LTC/USDT | atr_breakout | `n=20,k=2.0` | filtre=regime_bench200 · çıkış=stop_atr=2.0,tp_r=3.0 | +90% | +109% | +440% | 0.845 | -28% | 1.843 | 48% | 1.954 | 34% | +15% | +2.01% | 0.0 |
| B | 1 | BTC/USDT | bollinger_breakout | `n=50,k=2.0` | çıkış=stop_atr=2.0,trail_atr=3.0 | +81% | +128% | +360% | 0.827 | -27% | 1.7 | 41% | 2.477 | 29% | +12% | +0.98% | 0.0 |
| B | 1 | ADA/USDT | keltner_breakout | `n=20,k=2.5` | çıkış=stop_atr=2.0,trail_atr=3.0 | +182% | +291% | +656% | 0.821 | -39% | 1.937 | 46% | 2.324 | 30% | +15% | +2.03% | 0.0 |
| B | 2 | ADA/USDT | rsi_midline | `n=28,level=60` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=chop_switch(≤5 bar) | +85% | +81% | +401% | 0.819 | -35% | 2.422 | 47% | 2.707 | 27% | +20% | +2.82% | 0.0 |
| B | 2 | ADA/USDT | cci_breakout | `n=20,level=150` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=chop_switch(≤5 bar) | +130% | +268% | +389% | 0.811 | -39% | 2.37 | 45% | 2.923 | 26% | +19% | +3.04% | 0.0 |
| B | 2 | TRX/USDT | smc_choch | `k=3` | filtre=regime_bench200 · çıkış=stop_atr=2.0,tp_r=3.0 | +65% | +101% | +425% | 0.809 | -40% | 1.639 | 41% | 2.389 | 30% | +11% | +1.30% | 0.0 |
| B | 1 | SNX/USDT | adx_trend | `n=14,th=30` | çıkış=stop_atr=2.0,trail_atr=3.0 | +72% | +217% | +278% | 0.791 | -28% | 3.081 | 41% | 4.45 | 18% | +23% | +3.72% | 0.0 |
| B | 2 | LTC/USDT | williams_reversal | `n=21,lo=-95` | filtre=adx20 · çıkış=stop_atr=2.0,trail_atr=3.0 | +33% | +74% | +494% | 0.79 | -34% | 1.563 | 55% | 1.286 | 44% | +11% | +1.32% | 0.0 |
| B | 1 | BTC/USDT | triple_ma | `set=(10, 50, 200),kind=ema` | çıkış=stop_atr=2.0,trail_atr=3.0 | +116% | +141% | +230% | 0.773 | -40% | 1.804 | 46% | 2.114 | 32% | +14% | +1.07% | 0.0 |
| B | 2 | ADA/USDT | high_52w_break | `n=126,exit_ma=50` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_bos(≤5 bar) | +75% | +46% | +485% | 0.773 | -39% | 2.012 | 37% | 3.492 | 22% | +14% | +2.61% | 0.0 |
| B | 2 | TRX/USDT | ichimoku_cloud | `cfg=(9, 26, 52)` | filtre=htf_week_sma10 · çıkış=stop_atr=2.0,tp_r=3.0 | +40% | +90% | +341% | 0.772 | -30% | 1.697 | 38% | 2.724 | 27% | +12% | +1.06% | 0.0 |
| B | 2 | TRX/USDT | smc_order_block | `k=3,max_age=20` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_choch(≤5 bar) | +49% | +53% | +235% | 0.768 | -28% | 2.157 | 40% | 3.21 | 24% | +16% | +1.34% | 0.0 |
| B | 2 | MANA/USDT | hammer_star | `lookback_low=10` | çıkış=trail_atr=3.0 | +8% | +124% | +299% | 0.764 | -36% | 1.693 | 67% | 0.833 | 55% | +12% | +0.96% | 0.0 |
| B | 2 | BTC/USDT | ma_cross | `kind=tema,pair=(20, 50)` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_bos(≤5 bar) | +29% | +16% | +199% | 0.761 | -33% | 1.747 | 44% | 2.233 | 31% | +13% | +0.98% | 0.0 |
| B | 2 | ETH/USDT | volume_breakout | `n=20,rv=1.5` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_fvg(≤5 bar) | +53% | +86% | +188% | 0.758 | -28% | 2.526 | 42% | 3.515 | 22% | +20% | +2.32% | 0.0 |
| B | 1 | AXS/USDT | ma_cross | `kind=sma,pair=(50, 200)` | çıkış=stop_atr=2.0,trail_atr=3.0 | +3% | +61% | +152% | 0.748 | -36% | 2.587 | 39% | 4.097 | 20% | +19% | +3.90% | 0.0 |
| B | 1 | ETH/USDT | linreg_slope | `n=100,th=0.0005` | çıkış=stop_atr=2.0,trail_atr=3.0 | +59% | +39% | +230% | 0.738 | -39% | 1.95 | 37% | 3.27 | 23% | +14% | +1.94% | 0.0 |
| B | 2 | ADA/USDT | ichimoku_cloud | `cfg=(9, 26, 52)` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_order_block(≤3 bar) | +64% | +103% | +349% | 0.725 | -37% | 1.782 | 35% | 3.267 | 23% | +12% | +1.63% | 0.0 |
| B | 1 | ETH/USDT | donchian_breakout | `entry=100,exit=20` | çıkış=stop_atr=2.0,trail_atr=3.0 | +46% | +33% | +357% | 0.724 | -37% | 1.706 | 39% | 2.718 | 27% | +12% | +1.54% | 0.0 |
| B | 2 | MANA/USDT | bollinger_reversion | `n=30,k=3.0` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=pivot_bounce(≤5 bar) | +53% | +90% | +99% | 0.713 | -24% | 2.201 | 62% | 1.362 | 42% | +19% | +2.24% | 0.0 |
| B | 1 | TRX/USDT | wavetrend_reversal | `n1=9,n2=26,lo=-60` | çıkış=stop_atr=2.0,trail_atr=3.0 | +19% | +17% | +211% | 0.7 | -37% | 2.258 | 54% | 1.923 | 34% | +20% | +2.81% | 0.0 |
| B | 2 | BTC/USDT | linreg_slope | `n=20,th=0.0005` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_bos(≤5 bar) | +28% | +66% | +254% | 0.695 | -40% | 1.549 | 39% | 2.386 | 30% | +10% | +0.77% | 0.0 |
| B | 1 | BCH/USDT | down_days | `n=5,hold_exit=3` | çıkış=stop_atr=2.0,trail_atr=3.0 | +9% | +39% | +274% | 0.692 | -37% | 1.42 | 58% | 1.024 | 49% | +9% | +0.79% | 0.0 |
| B | 2 | NEAR/USDT | rsi_divergence | `n=14,k=3,exit_level=70` | filtre=htf_week_sma10 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +84% | +53% | +124% | 0.691 | -37% | 1.855 | 52% | 1.694 | 37% | +15% | +2.27% | 0.0 |
| B | 2 | UNI/USDT | mfi_reversal | `n=14,lo=20` | filtre=trend_sma200 · çıkış=signal_only | +104% | +90% | +200% | 0.685 | -19% | 4.749 | 61% | 2.999 | 25% | +36% | +4.12% | 0.0 |
| B | 2 | BTC/USDT | ichimoku_cloud | `cfg=(9, 26, 52)` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_fvg(≤5 bar) | +92% | +155% | +165% | 0.684 | -40% | 1.712 | 38% | 2.768 | 26% | +12% | +0.80% | 0.0 |
| B | 1 | ETH/USDT | high_52w_break | `n=126,exit_ma=50` | çıkış=stop_atr=2.0,trail_atr=3.0 | +40% | +36% | +293% | 0.682 | -31% | 1.684 | 41% | 2.461 | 29% | +12% | +1.53% | 0.0 |
| B | 2 | BTC/USDT | volume_breakout | `n=20,rv=1.5` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=chop_switch(≤0 bar) | +37% | +73% | +110% | 0.681 | -24% | 1.937 | 38% | 3.182 | 24% | +14% | +1.23% | 0.0 |
| B | 2 | BTC/USDT | donchian_breakout | `entry=55,exit=20` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=chop_switch(≤0 bar) | +39% | +63% | +185% | 0.68 | -27% | 1.775 | 42% | 2.45 | 29% | +13% | +1.10% | 0.0 |
| B | 2 | LINK/USDT | atr_breakout | `n=10,k=2.0` | filtre=low_vol · çıkış=signal_only | +49% | +83% | +192% | 0.674 | -33% | 2.107 | 48% | 2.239 | 31% | +18% | +2.00% | 0.0 |
| B | 2 | TRX/USDT | wavetrend_reversal | `n1=9,n2=26,lo=-60` | çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +16% | +10% | +152% | 0.667 | -37% | 2.032 | 58% | 1.471 | 40% | +18% | +2.24% | 0.0 |
| B | 2 | BTC/USDT | volume_breakout | `n=20,rv=1.5` | filtre=low_vol · çıkış=stop_atr=2.0,trail_atr=3.0 | +23% | +31% | +112% | 0.667 | -20% | 1.897 | 37% | 3.181 | 24% | +13% | +1.03% | 0.0 |
| B | 1 | BNB/USDT | triple_ma | `set=(10, 50, 200),kind=ema` | çıkış=stop_atr=2.0,trail_atr=3.0 | +12% | +27% | +288% | 0.663 | -40% | 1.684 | 43% | 2.246 | 31% | +12% | +1.24% | 0.0 |
| B | 1 | BTC/USDT | atr_breakout | `n=20,k=1.5` | çıkış=stop_atr=2.0,trail_atr=3.0 | +23% | +67% | +232% | 0.654 | -36% | 1.415 | 36% | 2.48 | 29% | +8% | +0.56% | 0.0 |
| B | 2 | BTC/USDT | cci_breakout | `n=40,level=100` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=ma_cross(≤0 bar) | +25% | +40% | +55% | 0.627 | -10% | 2.532 | 50% | 2.532 | 28% | +22% | +1.66% | 0.0 |
| B | 2 | AVAX/USDT | macd_divergence | `k=3,fast=12,slow=26` | filtre=regime_bench200 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +130% | +109% | +89% | 0.625 | -33% | 1.6 | 49% | 1.646 | 38% | +12% | +1.14% | 0.0 |
| B | 2 | BCH/USDT | down_days | `n=5,hold_exit=3` | filtre=adx20 · çıkış=stop_atr=2.0,trail_atr=3.0 | +12% | +10% | +175% | 0.605 | -28% | 1.435 | 59% | 0.998 | 50% | +9% | +0.86% | 0.0 |
| B | 1 | ETH/USDT | ma_cross | `kind=kama,pair=(50, 150)` | çıkış=stop_atr=2.0,trail_atr=3.0 | +31% | +35% | +130% | 0.602 | -20% | 1.835 | 46% | 2.141 | 32% | +14% | +1.40% | 0.0 |
| B | 2 | TRX/USDT | trix_cross | `n=21,signal=7` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_order_block(≤3 bar) | +36% | +75% | +124% | 0.591 | -34% | 1.853 | 46% | 2.186 | 31% | +14% | +1.18% | 0.0 |
| B | 2 | BNB/USDT | atr_breakout | `n=20,k=1.5` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_choch(≤0 bar) | +9% | +56% | +133% | 0.587 | -24% | 2.099 | 50% | 2.099 | 32% | +18% | +1.48% | 0.0 |
| B | 1 | XRP/USDT | volume_breakout | `n=50,rv=1.5` | çıkış=stop_atr=2.0,trail_atr=3.0 | +38% | +91% | +220% | 0.567 | -38% | 1.693 | 34% | 3.24 | 24% | +11% | +1.58% | 0.0 |
| B | 2 | BTC/USDT | smc_bos | `k=8` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=rsi_midline(≤5 bar) | +57% | +52% | +152% | 0.56 | -32% | 1.437 | 42% | 1.983 | 34% | +8% | +0.66% | 0.0 |
| B | 1 | DOGE/USDT | rsi_divergence | `n=14,k=5,exit_level=70` | çıkış=stop_atr=2.0,trail_atr=3.0 | +69% | +76% | +109% | 0.545 | -35% | 1.691 | 43% | 2.238 | 31% | +12% | +1.27% | 0.0 |
| B | 2 | LTC/USDT | atr_breakout | `n=20,k=2.0` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=rsi_midline(≤0 bar) | +11% | +20% | +114% | 0.528 | -27% | 2.018 | 50% | 2.018 | 33% | +17% | +1.67% | 0.0 |
| B | 1 | XRP/USDT | rsi_reversal | `n=7,lo=10,exit=50` | çıkış=stop_atr=2.0,trail_atr=3.0 | +54% | +80% | +100% | 0.52 | -24% | 1.848 | 63% | 1.083 | 48% | +15% | +1.83% | 0.0 |
| B | 2 | LTC/USDT | stoch_reversal | `k=21,d=5,smooth=1,lo=10` | filtre=regime_bench200 · çıkış=stop_atr=2.0,tp_r=3.0 | +17% | +58% | +129% | 0.512 | -34% | 1.409 | 62% | 0.876 | 53% | +8% | +0.83% | 0.0 |
| B | 2 | ADA/USDT | aroon_cross | `n=50` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_choch(≤3 bar) | +38% | +37% | +98% | 0.474 | -31% | 1.977 | 47% | 2.26 | 31% | +16% | +1.87% | 0.0 |

## Coin coin özet (ajan günlüğü)

- **AAVE/USDT**: 79 aday denendi, 1 kaldı. En iyi aday rsi_reversal (`n=5,lo=10,exit=50`, filtre=adx20 · çıkış=signal_only): OK — tüm adımlar geçti.
- **ADA/USDT**: 99 aday denendi, 14 kaldı. En iyi aday volume_breakout (`n=50,rv=2.0`, filtre=htf_week_sma10 · çıkış=stop_atr=2.0,max_hold=10): OK — tüm adımlar geçti.
- **ALGO/USDT**: 72 aday denendi, 0 kaldı. En iyi aday adx_trend (`n=14,th=25`, filtre=trend_sma200 · çıkış=stop_atr=2.0,trail_atr=3.0): S4 — komşu ayarların %25'i kârlı.
- **APT/USDT**: 73 aday denendi, 0 kaldı. En iyi aday funding_extreme (`n=365,th=2.0`, çıkış=stop_atr=2.0,trail_atr=3.0): S6 — yılların %50'i kârlı.
- **ARB/USDT**: 94 aday denendi, 5 kaldı. En iyi aday ma_cross (`kind=sma,pair=(20, 50)`, filtre=regime_bench200 · çıkış=stop_atr=2.0,max_hold=10): OK — tüm adımlar geçti.
- **ATOM/USDT**: 72 aday denendi, 1 kaldı. En iyi aday macd_divergence (`k=3,fast=12,slow=26`, filtre=adx20 · çıkış=stop_atr=2.0,max_hold=10): OK — tüm adımlar geçti.
- **AVAX/USDT**: 72 aday denendi, 1 kaldı. En iyi aday macd_divergence (`k=3,fast=12,slow=26`, filtre=regime_bench200 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0): OK — tüm adımlar geçti.
- **AXS/USDT**: 72 aday denendi, 1 kaldı. En iyi aday ma_cross (`kind=sma,pair=(50, 200)`, çıkış=stop_atr=2.0,trail_atr=3.0): OK — tüm adımlar geçti.
- **BCH/USDT**: 77 aday denendi, 2 kaldı. En iyi aday down_days (`n=5,hold_exit=3`, çıkış=stop_atr=2.0,trail_atr=3.0): OK — tüm adımlar geçti.
- **BNB/USDT**: 93 aday denendi, 4 kaldı. En iyi aday macd_cross (`cfg=(19, 39, 9),zero_filter=False`, filtre=trend_sma200 · çıkış=stop_atr=2.0,tp_r=3.0): OK — tüm adımlar geçti.
- **BTC/USDT**: 96 aday denendi, 21 kaldı. En iyi aday rsi_midline (`n=28,level=60`, filtre=low_vol · çıkış=stop_atr=2.0,be_r=1.0): OK — tüm adımlar geçti.
- **CRV/USDT**: 71 aday denendi, 0 kaldı. En iyi aday funding_extreme (`n=90,th=1.5`, filtre=adx20 · çıkış=signal_only): S2 — PF 2.576, 1x maks. düşüş -65%.
- **DOGE/USDT**: 79 aday denendi, 3 kaldı. En iyi aday inside_bar (`trend_n=50`, çıkış=stop_atr=2.0,trail_atr=3.0 · onay=chop_switch(≤3 bar)): OK — tüm adımlar geçti.
- **DOT/USDT**: 70 aday denendi, 0 kaldı. En iyi aday macd_divergence (`k=3,fast=12,slow=26`, filtre=regime_bench200 · çıkış=stop_atr=2.0,be_r=1.0): S4 — komşu ayarların %0'i kârlı.
- **ETC/USDT**: 72 aday denendi, 0 kaldı. En iyi aday coppock_turn (`scale=5`, filtre=trend_sma200 · çıkış=stop_atr=2.0,be_r=1.0): S6 — yılların %56'i kârlı.
- **ETH/USDT**: 85 aday denendi, 15 kaldı. En iyi aday roc_breakout (`n=126,th=5`, filtre=trend_sma200 · çıkış=trail_atr=3.0): OK — tüm adımlar geçti.
- **FIL/USDT**: 75 aday denendi, 2 kaldı. En iyi aday ichimoku_cloud (`cfg=(9, 26, 52)`, filtre=trend_sma200 · çıkış=stop_atr=2.0,trail_atr=3.0): OK — tüm adımlar geçti.
- **IMX/USDT**: 82 aday denendi, 0 kaldı. En iyi aday smc_ote (`k=8,fib_lo=0.618`, çıkış=stop_atr=2.0,tp_r=3.0): S5 — 1 bar geç girişte Sharpe'ın %0'i kalıyor.
- **INJ/USDT**: 79 aday denendi, 3 kaldı. En iyi aday wavetrend_reversal (`n1=12,n2=21,lo=-53`, filtre=low_vol · çıkış=stop_atr=2.0,tp_r=3.0): OK — tüm adımlar geçti.
- **LINK/USDT**: 79 aday denendi, 1 kaldı. En iyi aday atr_breakout (`n=10,k=2.0`, filtre=low_vol · çıkış=signal_only): OK — tüm adımlar geçti.
- **LTC/USDT**: 74 aday denendi, 4 kaldı. En iyi aday atr_breakout (`n=20,k=2.0`, filtre=regime_bench200 · çıkış=stop_atr=2.0,tp_r=3.0): OK — tüm adımlar geçti.
- **MANA/USDT**: 71 aday denendi, 3 kaldı. En iyi aday hammer_star (`lookback_low=10`, çıkış=stop_atr=2.0,trail_atr=3.0): OK — tüm adımlar geçti.
- **MINA/USDT**: 78 aday denendi, 1 kaldı. En iyi aday adx_trend (`n=20,th=20`, filtre=regime_bench200 · çıkış=stop_atr=2.0,be_r=1.0): OK — tüm adımlar geçti.
- **NEAR/USDT**: 81 aday denendi, 2 kaldı. En iyi aday macd_cross (`cfg=(12, 26, 9),zero_filter=True`, çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_order_block(≤5 bar)): OK — tüm adımlar geçti.
- **OP/USDT**: 72 aday denendi, 1 kaldı. En iyi aday keltner_breakout (`n=20,k=2.5`, filtre=trend_sma200 · çıkış=stop_atr=2.0,max_hold=10): OK — tüm adımlar geçti.
- **PYTH/USDT**: elendi (S0: 2.9 yıl veri var, en az 3.0 yıl gerekli).
- **SAND/USDT**: 71 aday denendi, 0 kaldı. En iyi aday mfi_reversal (`n=14,lo=10`, çıkış=stop_atr=2.0,trail_atr=3.0): S7 — PSR 0.771.
- **SNX/USDT**: 74 aday denendi, 3 kaldı. En iyi aday rsi_divergence (`n=14,k=3,exit_level=70`, filtre=regime_bench200 · çıkış=stop_atr=2.0,max_hold=10): OK — tüm adımlar geçti.
- **SOL/USDT**: 92 aday denendi, 3 kaldı. En iyi aday smc_choch (`k=8`, filtre=regime_bench200 · çıkış=stop_atr=2.0,be_r=1.0): OK — tüm adımlar geçti.
- **SUI/USDT**: 105 aday denendi, 8 kaldı. En iyi aday bollinger_reversion (`n=30,k=2.5`, filtre=adx20 · çıkış=stop_atr=2.0,max_hold=10): OK — tüm adımlar geçti.
- **THETA/USDT**: 72 aday denendi, 0 kaldı. En iyi aday stochrsi_reversal (`n=21,lo=20`, çıkış=stop_atr=2.0,trail_atr=3.0 · onay=rsi_midline(≤5 bar)): S6 — yılların %44'i kârlı.
- **TRX/USDT**: 92 aday denendi, 7 kaldı. En iyi aday ma_cross (`kind=sma,pair=(5, 20)`, filtre=trend_sma200 · çıkış=stop_atr=2.0,tp_r=3.0): OK — tüm adımlar geçti.
- **UNI/USDT**: 85 aday denendi, 5 kaldı. En iyi aday down_days (`n=5,hold_exit=3`, çıkış=stop_atr=2.0,trail_atr=3.0 · onay=pivot_bounce(≤3 bar)): OK — tüm adımlar geçti.
- **XLM/USDT**: 93 aday denendi, 3 kaldı. En iyi aday ma_cross (`kind=ema,pair=(20, 100)`, çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0): OK — tüm adımlar geçti.
- **XRP/USDT**: 82 aday denendi, 6 kaldı. En iyi aday donchian_breakout (`entry=100,exit=10`, filtre=adx20 · çıkış=stop_atr=2.0,max_hold=10): OK — tüm adımlar geçti.

## Zayıf yönler (dürüst liste)

- 40067 deneme yapıldı. Bu kadar çok denemede şans eseri iyi görünen strateji çıkar. DSR bunu düzeltir; tier A sadece DSR ≥ eşik olanlardır.
- Seçim ve test aynı geçmiş veride yapıldı. Gerçek test arenadaki ileri (paper) kayıttır.
- Survivorship: liste bugünün coinlerinden oluşur. Borsadan silinen coinler yok, bu sonucu iyimser yapar.
- Funding sabit yıllık oranla, likidasyon işlem bazında yaklaşık modellenir.
- Tek borsa verisi (Bitget, yoksa OKX/KuCoin). Emir defteri ve piyasa etkisi modellenmez.

## Arena

Arena: 100 aktif (eleme geçen), 0 kontrol (yakın aday, switcher kullanmaz), 0 yeni üye, 0 kontrolden aktife. Üst sınır 100.

## Switcher backtest kapısı

Geçti: **False** — kontroller: `{"beats_equal_weight_all_windows": false, "positive_at_cost_stress": true, "max_dd_ok": true}`

Pencereler: `{"3y": {"sharpe": 1.355, "ew_sharpe": 2.729}, "5y": {"sharpe": 1.276, "ew_sharpe": 2.262}, "full": {"sharpe": 1.11, "ew_sharpe": 2.207}}`
