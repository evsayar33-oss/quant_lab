# Eleme motoru — crypto_alts 4h (yön: both)

Veri: 2018-01-01 → 2026-11-02. Coin: 34 uygun (toplam 35). Denenen varyant: 592 × coin = **29193 deneme**.
Her (coin, kural) için tek en iyi nokta değil, **en sağlam bölgenin merkezi** seçildi. Bu bir aday listesidir, karar değildir. Karar sadece doğrulama kapısında verilir.

> ⚠️ **Zaman makinesi kontrolü önerilir.** Bu liste binlerce deneme arasından seçildi; seçim süreçleri backtest'te iyi görünüp ileride çökebilir (2026-10-17 ve 10-19 testleri). Gerçek paraya aday olmadan önce `Time machine test` workflow'unu aynı yön (side) ve zaman dilimiyle çalıştırın. Kural: CLAUDE.md / AGENTS.md.

## Huni

| Adım | Ne kontrol edilir | Elenen | Kalan |
|---|---|---|---|
| S0 | veri yetersiz | 68 | 2312 |
| S1 | her dönemde kârlı değil / az işlem | 2203 | 109 |
| S2 | kâr faktörü veya düşüş zayıf | 94 | 15 |
| S3 | yüksek maliyette zarar | 1 | 14 |
| S4 | plato yok (komşu ayarlar zararda) | 3 | 11 |
| S5 | 1 bar gecikmeye dayanıksız | 1 | 10 |
| S6 | yılların çoğunda kârlı değil | 2 | 8 |
| S7 | istatistiksel güven düşük (PSR) | 3 | 5 |

## 2. aşama: filtre × çıkış × kombo (sadece S1'i geçen adaylarda)

109 aday → 9065 ek deneme (DSR'a eklendi). Her aday için en sağlam filtre/çıkış hücresi ve en sağlam kombo seçildi; kombo sadece kuralı tek başına geçerse aday olur. Seçilenler aynı S1–S7 adımlarından geçti.

| Adım | Ne kontrol edilir | Elenen | Kalan |
|---|---|---|---|
| S0 | veri yetersiz | 0 | 194 |
| S1 | her dönemde kârlı değil / az işlem | 54 | 140 |
| S2 | kâr faktörü veya düşüş zayıf | 75 | 65 |
| S3 | yüksek maliyette zarar | 0 | 65 |
| S4 | plato yok (komşu ayarlar zararda) | 19 | 46 |
| S5 | 1 bar gecikmeye dayanıksız | 1 | 45 |
| S6 | yılların çoğunda kârlı değil | 11 | 34 |
| S7 | istatistiksel güven düşük (PSR) | 0 | 34 |

## Geçenler (39)

Kazanma oranı tek başına bir şey söylemez. Sistem sadece **kazanma oranı > başabaş oranı** olduğunda kârlıdır. Başabaş = 1 / (1 + ödeme oranı); ödeme oranı = ortalama kazanç / ortalama kayıp (maliyet sonrası). Pay = kazanma oranı − başabaş. Beklenen = işlem başına ortalama net getiri.

| Tier | Aşama | Coin | Kural | Ayar | Varyant | 3y | 5y | Tüm | Sharpe | 1x DD | PF | Kazanma | Ödeme | Başabaş | Pay | Beklenen | DSR |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| B | 2 | SUI/USDT | roc_breakout | `n=252,th=10` | filtre=adx20 · çıkış=stop_atr=2.0,tp_r=3.0 | +812% | veri yok | +1201% | 1.785 | -30% | 2.799 | 44% | 3.615 | 22% | +22% | +5.22% | 0.089 |
| B | 2 | ARB/USDT | price_ma | `kind=kama,n=200` | filtre=trend_sma200 · çıkış=trail_atr=3.0 | +978% | veri yok | +1063% | 1.54 | -32% | 2.135 | 30% | 5.107 | 16% | +13% | +1.71% | 0.026 |
| B | 2 | ARB/USDT | macd_zero | `cfg=(12, 26, 9)` | filtre=regime_bench200 · çıkış=stop_atr=2.0,tp_r=3.0 | +584% | veri yok | +673% | 1.446 | -40% | 1.743 | 37% | 2.97 | 25% | +12% | +1.99% | 0.02 |
| B | 2 | ARB/USDT | smc_choch | `k=8` | filtre=trend_sma200 · çıkış=stop_atr=2.0,tp_r=3.0 | +465% | veri yok | +530% | 1.309 | -32% | 1.903 | 42% | 2.643 | 27% | +14% | +2.68% | 0.01 |
| B | 2 | ARB/USDT | bollinger_breakout | `n=50,k=2.5` | filtre=low_vol · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +107% | veri yok | +145% | 1.3 | -19% | 2.493 | 65% | 1.36 | 42% | +22% | +1.93% | 0.008 |
| B | 2 | ARB/USDT | triple_ma | `set=(10, 50, 200),kind=ema` | filtre=htf_week_sma10 · çıkış=stop_atr=2.0,tp_r=3.0 | +363% | veri yok | +403% | 1.217 | -34% | 1.729 | 35% | 3.234 | 24% | +11% | +2.14% | 0.006 |
| B | 2 | OP/USDT | bollinger_breakout | `n=50,k=2.5` | filtre=trend_sma200 · çıkış=stop_atr=2.0,max_hold=10 | +262% | veri yok | +894% | 1.331 | -30% | 2.258 | 59% | 1.584 | 39% | +20% | +2.53% | 0.005 |
| B | 2 | ARB/USDT | bb_squeeze | `n=20,q=0.1,look=126` | filtre=low_vol · çıkış=stop_atr=2.0,max_hold=10 | +151% | veri yok | +179% | 1.173 | -26% | 1.861 | 49% | 1.908 | 34% | +15% | +1.45% | 0.005 |
| B | 2 | ARB/USDT | ma_cross | `kind=sma,pair=(10, 30)` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=roc_breakout(≤5 bar) | +284% | veri yok | +241% | 1.022 | -36% | 2.429 | 48% | 2.597 | 28% | +20% | +2.66% | 0.002 |
| B | 2 | OP/USDT | cmf_flow | `n=40,th=0.2` | filtre=low_vol · çıkış=stop_atr=2.0,tp_r=3.0 | +98% | veri yok | +175% | 1.093 | -39% | 2.137 | 49% | 2.244 | 31% | +18% | +2.85% | 0.001 |
| B | 2 | ARB/USDT | macd_divergence | `k=3,fast=12,slow=26` | filtre=regime_bench200 · çıkış=stop_atr=2.0,trail_atr=3.0 | +245% | veri yok | +229% | 1.019 | -30% | 1.874 | 34% | 3.683 | 21% | +12% | +1.95% | 0.001 |
| B | 1 | ARB/USDT | hurst_switch | `n=200,fast=20,rsi_n=5` | çıkış=stop_atr=2.0,trail_atr=3.0 | +143% | veri yok | +135% | 0.953 | -31% | 2.171 | 41% | 3.121 | 24% | +17% | +2.76% | 0.001 |
| B | 2 | ARB/USDT | macd_zero | `cfg=(12, 26, 9)` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=roc_breakout(≤5 bar) | +123% | veri yok | +192% | 0.929 | -30% | 2.251 | 44% | 2.908 | 26% | +18% | +2.57% | 0.001 |
| B | 2 | XRP/USDT | high_52w_break | `n=126,exit_ma=50` | filtre=adx20 · çıkış=stop_atr=2.0,max_hold=10 | +259% | +303% | +3232% | 1.306 | -32% | 3.072 | 53% | 2.718 | 27% | +26% | +4.43% | 0.0 |
| B | 2 | ETH/USDT | price_ma | `kind=sma,n=150` | filtre=low_vol · çıkış=trail_atr=3.0 | +175% | +313% | +2043% | 1.185 | -31% | 2.038 | 29% | 5.015 | 17% | +12% | +1.12% | 0.0 |
| B | 2 | ETH/USDT | high_52w_break | `n=126,exit_ma=50` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=chop_switch(≤5 bar) | +88% | +81% | +548% | 0.993 | -23% | 2.677 | 47% | 2.966 | 25% | +22% | +2.89% | 0.0 |
| B | 2 | IMX/USDT | smc_ote | `k=8,fib_lo=0.5` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=roc_breakout(≤3 bar) | +63% | veri yok | +156% | 0.967 | -28% | 2.047 | 44% | 2.654 | 27% | +16% | +1.72% | 0.0 |
| B | 2 | ETH/USDT | high_52w_break | `n=126,exit_ma=50` | filtre=low_vol · çıkış=signal_only | +74% | +103% | +766% | 0.957 | -33% | 2.634 | 44% | 3.361 | 23% | +21% | +4.27% | 0.0 |
| B | 2 | BTC/USDT | triple_ma | `set=(10, 50, 200),kind=ema` | filtre=low_vol · çıkış=trail_atr=3.0 | +31% | +102% | +522% | 0.943 | -31% | 1.973 | 43% | 2.599 | 28% | +15% | +1.16% | 0.0 |
| B | 1 | XRP/USDT | high_52w_break | `n=126,exit_ma=50` | çıkış=stop_atr=2.0,trail_atr=3.0 | +136% | +157% | +884% | 0.932 | -39% | 2.496 | 43% | 3.307 | 23% | +20% | +3.06% | 0.0 |
| B | 2 | FIL/USDT | mfi_reversal | `n=14,lo=10` | çıkış=stop_atr=2.0,tp_r=3.0 | +234% | +185% | +307% | 0.929 | -24% | 2.427 | 64% | 1.378 | 42% | +22% | +2.82% | 0.0 |
| B | 2 | FIL/USDT | ma_cross | `kind=dema,pair=(20, 100)` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_order_block(≤3 bar) | +170% | +341% | +400% | 0.928 | -33% | 2.446 | 43% | 3.235 | 24% | +19% | +2.85% | 0.0 |
| B | 2 | BTC/USDT | bollinger_breakout | `n=50,k=2.0` | filtre=low_vol · çıkış=trail_atr=3.0 | +23% | +106% | +599% | 0.906 | -39% | 1.877 | 41% | 2.696 | 27% | +14% | +1.11% | 0.0 |
| B | 1 | FIL/USDT | mfi_reversal | `n=14,lo=10` | çıkış=stop_atr=2.0,trail_atr=3.0 | +202% | +158% | +257% | 0.884 | -26% | 2.299 | 60% | 1.511 | 40% | +20% | +2.60% | 0.0 |
| B | 2 | DOT/USDT | rsi_divergence | `n=14,k=3,exit_level=70` | filtre=trend_sma200 · çıkış=stop_atr=2.0,max_hold=10 | +88% | +88% | +121% | 0.87 | -19% | 1.935 | 57% | 1.464 | 41% | +16% | +1.35% | 0.0 |
| B | 2 | DOGE/USDT | high_52w_break | `n=252,exit_ma=50` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=chop_switch(≤0 bar) | +46% | +60% | +1979% | 0.865 | -35% | 5.486 | 56% | 4.294 | 19% | +37% | +11.33% | 0.0 |
| B | 2 | OP/USDT | bollinger_breakout | `n=50,k=2.5` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=roc_breakout(≤5 bar) | +158% | veri yok | +218% | 0.853 | -29% | 2.138 | 53% | 1.87 | 35% | +18% | +2.49% | 0.0 |
| B | 2 | DOT/USDT | rsi_divergence | `n=14,k=3,exit_level=70` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_order_block(≤5 bar) | +68% | +104% | +130% | 0.822 | -29% | 2.035 | 44% | 2.543 | 28% | +16% | +2.04% | 0.0 |
| B | 2 | ARB/USDT | cci_breakout | `n=40,level=150` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_choch(≤3 bar) | +226% | veri yok | +178% | 0.817 | -32% | 1.644 | 38% | 2.739 | 27% | +11% | +1.58% | 0.0 |
| B | 2 | DOT/USDT | bb_squeeze | `n=20,q=0.1,look=252` | filtre=htf_week_sma10 · çıkış=stop_atr=2.0,tp_r=3.0 | +19% | +14% | +194% | 0.808 | -37% | 1.87 | 43% | 2.494 | 29% | +14% | +1.57% | 0.0 |
| B | 2 | DOT/USDT | bb_squeeze | `n=20,q=0.1,look=252` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=ma_cross(≤3 bar) | +23% | +44% | +172% | 0.791 | -33% | 3.184 | 57% | 2.42 | 29% | +28% | +2.84% | 0.0 |
| B | 2 | ADA/USDT | high_52w_break | `n=126,exit_ma=50` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_bos(≤5 bar) | +75% | +46% | +485% | 0.773 | -39% | 2.012 | 37% | 3.492 | 22% | +14% | +2.61% | 0.0 |
| B | 2 | OP/USDT | trix_cross | `n=21,signal=7` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=macd_divergence(≤3 bar) | +90% | veri yok | +104% | 0.704 | -28% | 2.277 | 55% | 1.843 | 35% | +20% | +2.30% | 0.0 |
| B | 2 | BTC/USDT | keltner_breakout | `n=20,k=2.5` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=chop_switch(≤3 bar) | +32% | +88% | +177% | 0.686 | -30% | 1.774 | 43% | 2.317 | 30% | +13% | +1.12% | 0.0 |
| B | 1 | ETH/USDT | high_52w_break | `n=126,exit_ma=50` | çıkış=stop_atr=2.0,trail_atr=3.0 | +40% | +36% | +293% | 0.682 | -31% | 1.684 | 41% | 2.461 | 29% | +12% | +1.53% | 0.0 |
| B | 2 | ETH/USDT | volume_breakout | `n=20,rv=1.5` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_choch(≤0 bar) | +113% | +132% | +248% | 0.639 | -37% | 2.088 | 49% | 2.173 | 32% | +18% | +1.74% | 0.0 |
| B | 2 | OP/USDT | adx_trend | `n=20,th=25` | filtre=adx20 · çıkış=trail_atr=3.0 | +10% | veri yok | +109% | 0.621 | -36% | 1.757 | 36% | 3.138 | 24% | +12% | +1.49% | 0.0 |
| B | 1 | OP/USDT | cmf_flow | `n=40,th=0.2` | çıkış=stop_atr=2.0,trail_atr=3.0 | +118% | veri yok | +113% | 0.614 | -39% | 1.558 | 44% | 1.991 | 33% | +10% | +1.38% | 0.0 |
| B | 2 | ETH/USDT | volume_breakout | `n=20,rv=1.5` | filtre=low_vol · çıkış=trail_atr=3.0 | +30% | +55% | +218% | 0.591 | -39% | 1.664 | 42% | 2.334 | 30% | +12% | +1.01% | 0.0 |

## Coin coin özet (ajan günlüğü)

- **AAVE/USDT**: 70 aday denendi, 0 kaldı. En iyi aday coppock_turn (`scale=5`, çıkış=stop_atr=2.0,trail_atr=3.0 · onay=pivot_bounce(≤3 bar)): S4 — komşu ayarların %0'i kârlı.
- **ADA/USDT**: 79 aday denendi, 1 kaldı. En iyi aday high_52w_break (`n=126,exit_ma=50`, çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_bos(≤5 bar)): OK — tüm adımlar geçti.
- **ALGO/USDT**: 70 aday denendi, 0 kaldı. En iyi aday rsi_divergence (`n=14,k=3,exit_level=70`, filtre=regime_bench200 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0): S2 — PF 1.631, 1x maks. düşüş -41%.
- **APT/USDT**: 70 aday denendi, 0 kaldı. En iyi aday funding_extreme (`n=90,th=1.5`, çıkış=stop_atr=2.0,trail_atr=3.0 · onay=pivot_bounce(≤3 bar)): S6 — yılların %50'i kârlı.
- **ARB/USDT**: 101 aday denendi, 11 kaldı. En iyi aday price_ma (`kind=kama,n=200`, filtre=trend_sma200 · çıkış=trail_atr=3.0): OK — tüm adımlar geçti.
- **ATOM/USDT**: 68 aday denendi, 0 kaldı. En iyi aday rsi_reversal (`n=28,lo=20,exit=50`, çıkış=stop_atr=2.0,trail_atr=3.0): S1 — 3y +14%, 5y +16%, full +12%; 4 işlem.
- **AVAX/USDT**: 72 aday denendi, 0 kaldı. En iyi aday roc_breakout (`n=63,th=5`, filtre=low_vol · çıkış=stop_atr=2.0,be_r=1.0): S2 — PF 2.533, 1x maks. düşüş -55%.
- **AXS/USDT**: 68 aday denendi, 0 kaldı. En iyi aday high_52w_break (`n=126,exit_ma=50`, çıkış=stop_atr=2.0,trail_atr=3.0): S1 — 3y -28%, 5y -27%, full +550%; 67 işlem (zararlı: 3y, 5y).
- **BCH/USDT**: 74 aday denendi, 0 kaldı. En iyi aday coppock_turn (`scale=5`, filtre=low_vol · çıkış=stop_atr=2.0,be_r=1.0): S2 — PF 1.926, 1x maks. düşüş -47%.
- **BNB/USDT**: 76 aday denendi, 0 kaldı. En iyi aday high_52w_break (`n=252,exit_ma=50`, çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_bos(≤5 bar)): S6 — yılların %56'i kârlı.
- **BTC/USDT**: 82 aday denendi, 3 kaldı. En iyi aday triple_ma (`set=(10, 50, 200),kind=ema`, filtre=low_vol · çıkış=trail_atr=3.0): OK — tüm adımlar geçti.
- **CRV/USDT**: 70 aday denendi, 0 kaldı. En iyi aday funding_extreme (`n=90,th=1.5`, filtre=regime_bench200 · çıkış=signal_only): S2 — PF 1.815, 1x maks. düşüş -73%.
- **DOGE/USDT**: 78 aday denendi, 1 kaldı. En iyi aday high_52w_break (`n=252,exit_ma=50`, çıkış=stop_atr=2.0,trail_atr=3.0 · onay=chop_switch(≤0 bar)): OK — tüm adımlar geçti.
- **DOT/USDT**: 74 aday denendi, 4 kaldı. En iyi aday rsi_divergence (`n=14,k=3,exit_level=70`, filtre=trend_sma200 · çıkış=stop_atr=2.0,max_hold=10): OK — tüm adımlar geçti.
- **ETC/USDT**: 72 aday denendi, 0 kaldı. En iyi aday coppock_turn (`scale=5`, filtre=trend_sma200 · çıkış=stop_atr=2.0,be_r=1.0): S6 — yılların %56'i kârlı.
- **ETH/USDT**: 80 aday denendi, 6 kaldı. En iyi aday price_ma (`kind=sma,n=150`, filtre=low_vol · çıkış=trail_atr=3.0): OK — tüm adımlar geçti.
- **FIL/USDT**: 75 aday denendi, 3 kaldı. En iyi aday mfi_reversal (`n=14,lo=10`, çıkış=stop_atr=2.0,tp_r=3.0): OK — tüm adımlar geçti.
- **IMX/USDT**: 76 aday denendi, 1 kaldı. En iyi aday smc_ote (`k=8,fib_lo=0.5`, çıkış=stop_atr=2.0,trail_atr=3.0 · onay=roc_breakout(≤3 bar)): OK — tüm adımlar geçti.
- **INJ/USDT**: 71 aday denendi, 0 kaldı. En iyi aday funding_extreme (`n=90,th=2.0`, filtre=regime_bench200 · çıkış=stop_atr=2.0,trail_atr=3.0): S6 — yılların %33'i kârlı.
- **LINK/USDT**: 68 aday denendi, 0 kaldı. En iyi aday gap_fade (`g=0.02`, çıkış=stop_atr=2.0,trail_atr=3.0): S1 — 3y +0%, 5y +0%, full +5%; 1 işlem (zararlı: 3y, 5y).
- **LTC/USDT**: 68 aday denendi, 0 kaldı. En iyi aday bb_squeeze (`n=20,q=0.1,look=126`, çıkış=stop_atr=2.0,trail_atr=3.0): S1 — 3y -35%, 5y -57%, full -4%; 271 işlem (zararlı: 3y, 5y, full).
- **MANA/USDT**: 71 aday denendi, 0 kaldı. En iyi aday hammer_star (`lookback_low=10`, filtre=trend_sma200 · çıkış=stop_atr=2.0,tp_r=3.0): S2 — PF 1.647, 1x maks. düşüş -43%.
- **MINA/USDT**: 72 aday denendi, 0 kaldı. En iyi aday atr_breakout (`n=20,k=2.0`, çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_liquidity_sweep(≤3 bar)): S4 — komşu ayarların %0'i kârlı.
- **NEAR/USDT**: 68 aday denendi, 0 kaldı. En iyi aday force_index (`n=2`, çıkış=stop_atr=2.0,trail_atr=3.0): S1 — 3y -44%, 5y -79%, full +10%; 1086 işlem (zararlı: 3y, 5y).
- **OP/USDT**: 78 aday denendi, 6 kaldı. En iyi aday bollinger_breakout (`n=50,k=2.5`, filtre=trend_sma200 · çıkış=stop_atr=2.0,max_hold=10): OK — tüm adımlar geçti.
- **PYTH/USDT**: elendi (S0: 2.9 yıl veri var, en az 3.0 yıl gerekli).
- **SAND/USDT**: 74 aday denendi, 0 kaldı. En iyi aday roc_breakout (`n=252,th=10`, filtre=trend_sma200 · çıkış=stop_atr=2.0,be_r=1.0): S2 — PF 4.672, 1x maks. düşüş -75%.
- **SNX/USDT**: 70 aday denendi, 0 kaldı. En iyi aday funding_extreme (`n=90,th=1.5`, filtre=adx20 · çıkış=signal_only): S2 — PF 1.773, 1x maks. düşüş -73%.
- **SOL/USDT**: 74 aday denendi, 0 kaldı. En iyi aday high_52w_break (`n=126,exit_ma=50`, filtre=regime_bench200 · çıkış=signal_only): S6 — yılların %57'i kârlı.
- **SUI/USDT**: 83 aday denendi, 1 kaldı. En iyi aday roc_breakout (`n=252,th=10`, filtre=adx20 · çıkış=stop_atr=2.0,tp_r=3.0): OK — tüm adımlar geçti.
- **THETA/USDT**: 68 aday denendi, 0 kaldı. En iyi aday cci_breakout (`n=40,level=100`, çıkış=stop_atr=2.0,trail_atr=3.0): S1 — 3y -15%, 5y -56%, full -84%; 689 işlem (zararlı: 3y, 5y, full).
- **TRX/USDT**: 71 aday denendi, 0 kaldı. En iyi aday wavetrend_reversal (`n1=9,n2=26,lo=-60`, çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0): S2 — PF 1.764, 1x maks. düşüş -43%.
- **UNI/USDT**: 70 aday denendi, 0 kaldı. En iyi aday volume_breakout (`n=50,rv=3.0`, çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_order_block(≤5 bar)): S5 — 1 bar geç girişte Sharpe'ın %23'i kalıyor.
- **XLM/USDT**: 74 aday denendi, 0 kaldı. En iyi aday chop_switch (`n=14,lo=38.2,hi=61.8`, filtre=adx20 · çıkış=signal_only): S2 — PF 2.883, 1x maks. düşüş -54%.
- **XRP/USDT**: 71 aday denendi, 2 kaldı. En iyi aday high_52w_break (`n=126,exit_ma=50`, filtre=adx20 · çıkış=stop_atr=2.0,max_hold=10): OK — tüm adımlar geçti.

## Zayıf yönler (dürüst liste)

- 29193 deneme yapıldı. Bu kadar çok denemede şans eseri iyi görünen strateji çıkar. DSR bunu düzeltir; tier A sadece DSR ≥ eşik olanlardır.
- Seçim ve test aynı geçmiş veride yapıldı. Gerçek test arenadaki ileri (paper) kayıttır.
- Survivorship: liste bugünün coinlerinden oluşur. Borsadan silinen coinler yok, bu sonucu iyimser yapar.
- Funding sabit yıllık oranla, likidasyon işlem bazında yaklaşık modellenir.
- Tek borsa verisi (Bitget, yoksa OKX/KuCoin). Emir defteri ve piyasa etkisi modellenmez.

## Arena

Arena: 71 aktif (eleme geçen), 29 kontrol (yakın aday, switcher kullanmaz), 15 yeni üye, 0 kontrolden aktife. Üst sınır 100.

## Switcher backtest kapısı

Geçti: **False** — kontroller: `{"beats_equal_weight_all_windows": false, "positive_at_cost_stress": true, "max_dd_ok": true}`

Pencereler: `{"3y": {"sharpe": 0.134, "ew_sharpe": 2.881}, "5y": {"sharpe": 0.412, "ew_sharpe": 2.494}, "full": {"sharpe": 0.692, "ew_sharpe": 1.925}}`
