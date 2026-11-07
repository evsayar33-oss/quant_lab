# Eleme motoru — crypto_alts 4h_short (yön: short)

Veri: 2018-01-01 → 2026-11-02. Coin: 34 uygun (toplam 35). Denenen varyant: 592 × coin = **31032 deneme**.
Her (coin, kural) için tek en iyi nokta değil, **en sağlam bölgenin merkezi** seçildi. Bu bir aday listesidir, karar değildir. Karar sadece doğrulama kapısında verilir.

> ⚠️ **Zaman makinesi kontrolü önerilir.** Bu liste binlerce deneme arasından seçildi; seçim süreçleri backtest'te iyi görünüp ileride çökebilir (2026-10-17 ve 10-19 testleri). Gerçek paraya aday olmadan önce `Time machine test` workflow'unu aynı yön (side) ve zaman dilimiyle çalıştırın. Kural: CLAUDE.md / AGENTS.md.

## Huni

| Adım | Ne kontrol edilir | Elenen | Kalan |
|---|---|---|---|
| S0 | veri yetersiz | 68 | 2312 |
| S1 | her dönemde kârlı değil / az işlem | 2176 | 136 |
| S2 | kâr faktörü veya düşüş zayıf | 117 | 19 |
| S3 | yüksek maliyette zarar | 6 | 13 |
| S4 | plato yok (komşu ayarlar zararda) | 1 | 12 |
| S5 | 1 bar gecikmeye dayanıksız | 3 | 9 |
| S6 | yılların çoğunda kârlı değil | 4 | 5 |
| S7 | istatistiksel güven düşük (PSR) | 1 | 4 |

## 2. aşama: filtre × çıkış × kombo (sadece S1'i geçen adaylarda)

136 aday → 10904 ek deneme (DSR'a eklendi). Her aday için en sağlam filtre/çıkış hücresi ve en sağlam kombo seçildi; kombo sadece kuralı tek başına geçerse aday olur. Seçilenler aynı S1–S7 adımlarından geçti.

| Adım | Ne kontrol edilir | Elenen | Kalan |
|---|---|---|---|
| S0 | veri yetersiz | 0 | 243 |
| S1 | her dönemde kârlı değil / az işlem | 72 | 171 |
| S2 | kâr faktörü veya düşüş zayıf | 57 | 114 |
| S3 | yüksek maliyette zarar | 1 | 113 |
| S4 | plato yok (komşu ayarlar zararda) | 25 | 88 |
| S5 | 1 bar gecikmeye dayanıksız | 3 | 85 |
| S6 | yılların çoğunda kârlı değil | 11 | 74 |
| S7 | istatistiksel güven düşük (PSR) | 6 | 68 |

## Geçenler (72)

Kazanma oranı tek başına bir şey söylemez. Sistem sadece **kazanma oranı > başabaş oranı** olduğunda kârlıdır. Başabaş = 1 / (1 + ödeme oranı); ödeme oranı = ortalama kazanç / ortalama kayıp (maliyet sonrası). Pay = kazanma oranı − başabaş. Beklenen = işlem başına ortalama net getiri.

| Tier | Aşama | Coin | Kural | Ayar | Varyant | 3y | 5y | Tüm | Sharpe | 1x DD | PF | Kazanma | Ödeme | Başabaş | Pay | Beklenen | DSR |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| B | 2 | ARB/USDT | price_ma | `kind=kama,n=200` | filtre=trend_sma200 · çıkış=stop_atr=2.0,tp_r=3.0 | +961% | veri yok | +1003% | 2.049 | -39% | 2.57 | 27% | 7.069 | 12% | +14% | +2.36% | 0.347 |
| B | 2 | ARB/USDT | smc_bos | `k=2` | filtre=low_vol · çıkış=stop_atr=2.0,tp_r=3.0 | +674% | veri yok | +935% | 1.831 | -38% | 2.096 | 45% | 2.599 | 28% | +17% | +2.25% | 0.201 |
| B | 2 | ARB/USDT | roc_breakout | `n=63,th=0` | filtre=trend_sma200 · çıkış=stop_atr=2.0,tp_r=3.0 | +511% | veri yok | +681% | 1.738 | -23% | 2.419 | 39% | 3.769 | 21% | +18% | +1.94% | 0.157 |
| B | 2 | ARB/USDT | ppo_cross | `cfg=(12, 26, 9)` | filtre=low_vol · çıkış=stop_atr=2.0,tp_r=3.0 | +443% | veri yok | +744% | 1.693 | -36% | 1.903 | 42% | 2.682 | 27% | +14% | +1.49% | 0.14 |
| B | 2 | ARB/USDT | keltner_breakout | `n=50,k=2.0` | filtre=low_vol · çıkış=stop_atr=2.0,max_hold=10 | +398% | veri yok | +465% | 1.633 | -28% | 2.433 | 54% | 2.093 | 32% | +21% | +2.05% | 0.095 |
| B | 2 | ARB/USDT | cci_breakout | `n=14,level=100` | filtre=low_vol · çıkış=stop_atr=2.0,tp_r=3.0 | +584% | veri yok | +596% | 1.551 | -29% | 1.767 | 40% | 2.637 | 28% | +13% | +1.33% | 0.086 |
| B | 2 | ARB/USDT | macd_cross | `cfg=(12, 26, 9),zero_filter=True` | filtre=low_vol · çıkış=stop_atr=2.0,tp_r=3.0 | +175% | veri yok | +303% | 1.373 | -34% | 2.124 | 48% | 2.284 | 30% | +18% | +1.90% | 0.047 |
| B | 2 | ARB/USDT | macd_cross | `cfg=(12, 26, 9),zero_filter=True` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_order_block(≤3 bar) | +208% | veri yok | +206% | 1.415 | -16% | 3.844 | 56% | 2.989 | 25% | +31% | +3.76% | 0.04 |
| B | 2 | ARB/USDT | vwap_cross | `n=50` | filtre=low_vol · çıkış=stop_atr=2.0,tp_r=3.0 | +259% | veri yok | +332% | 1.337 | -36% | 1.717 | 24% | 5.395 | 16% | +8% | +1.09% | 0.039 |
| B | 2 | ARB/USDT | inside_bar | `trend_n=50` | filtre=low_vol · çıkış=stop_atr=2.0,tp_r=3.0 | +302% | veri yok | +318% | 1.332 | -27% | 2.234 | 41% | 3.17 | 24% | +17% | +2.19% | 0.037 |
| B | 2 | ARB/USDT | aroon_cross | `n=14` | filtre=low_vol · çıkış=stop_atr=2.0,tp_r=3.0 | +553% | veri yok | +458% | 1.329 | -40% | 1.671 | 40% | 2.506 | 28% | +12% | +1.29% | 0.036 |
| B | 2 | ARB/USDT | trix_cross | `n=15,signal=7` | filtre=trend_sma200 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +214% | veri yok | +268% | 1.302 | -24% | 1.813 | 54% | 1.521 | 40% | +15% | +1.33% | 0.031 |
| B | 2 | ARB/USDT | psar_flip | `cfg=(0.01, 0.1)` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=roc_breakout(≤5 bar) | +155% | veri yok | +199% | 1.306 | -17% | 4.522 | 70% | 1.938 | 34% | +36% | +4.13% | 0.025 |
| B | 2 | ARB/USDT | supertrend_flip | `cfg=(7, 2.0)` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_order_block(≤3 bar) | +308% | veri yok | +313% | 1.281 | -34% | 2.709 | 51% | 2.608 | 28% | +23% | +3.13% | 0.025 |
| B | 2 | ARB/USDT | awesome_zero | `fast=5,slow=34` | filtre=htf_week_sma10 · çıkış=stop_atr=2.0,tp_r=3.0 | +271% | veri yok | +322% | 1.203 | -32% | 1.799 | 40% | 2.699 | 27% | +13% | +1.63% | 0.021 |
| B | 2 | APT/USDT | macd_zero | `cfg=(12, 26, 9)` | filtre=htf_week_sma10 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +87% | veri yok | +230% | 1.229 | -22% | 2.047 | 57% | 1.535 | 39% | +18% | +1.63% | 0.019 |
| B | 2 | ARB/USDT | ichimoku_cloud | `cfg=(7, 22, 44)` | filtre=low_vol · çıkış=stop_atr=2.0,tp_r=3.0 | +175% | veri yok | +214% | 1.191 | -26% | 1.771 | 36% | 3.137 | 24% | +12% | +1.32% | 0.018 |
| B | 2 | ARB/USDT | smc_order_block | `k=3,max_age=50` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_liquidity_sweep(≤3 bar) | +169% | veri yok | +264% | 1.201 | -34% | 2.008 | 35% | 3.72 | 21% | +14% | +1.51% | 0.017 |
| B | 2 | ARB/USDT | smc_choch | `k=3` | filtre=low_vol · çıkış=stop_atr=2.0,trail_atr=3.0 | +252% | veri yok | +285% | 1.2 | -24% | 2.277 | 46% | 2.691 | 27% | +19% | +2.22% | 0.017 |
| B | 2 | ARB/USDT | aroon_cross | `n=14` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=roc_breakout(≤5 bar) | +203% | veri yok | +223% | 1.2 | -20% | 3.202 | 55% | 2.646 | 27% | +27% | +3.21% | 0.015 |
| B | 2 | ARB/USDT | ppo_cross | `cfg=(12, 26, 9)` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_order_block(≤3 bar) | +228% | veri yok | +281% | 1.16 | -25% | 1.881 | 39% | 2.962 | 25% | +14% | +1.54% | 0.012 |
| B | 2 | ARB/USDT | smc_order_block | `k=3,max_age=50` | filtre=low_vol · çıkış=trail_atr=3.0 | +269% | veri yok | +347% | 1.08 | -38% | 1.523 | 29% | 3.785 | 21% | +8% | +0.77% | 0.011 |
| B | 2 | ARB/USDT | cmf_flow | `n=20,th=0.05` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_order_block(≤3 bar) | +116% | veri yok | +191% | 1.044 | -30% | 1.923 | 47% | 2.198 | 31% | +15% | +1.27% | 0.009 |
| B | 2 | ARB/USDT | linreg_slope | `n=20,th=0.0005` | filtre=low_vol · çıkış=stop_atr=2.0,tp_r=3.0 | +252% | veri yok | +214% | 1.031 | -37% | 1.559 | 44% | 1.958 | 34% | +10% | +1.39% | 0.008 |
| B | 2 | OP/USDT | vortex_cross | `n=28` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_ote(≤5 bar) | +200% | veri yok | +473% | 1.144 | -31% | 2.433 | 46% | 2.807 | 26% | +20% | +2.33% | 0.007 |
| B | 2 | OP/USDT | aroon_cross | `n=14` | filtre=low_vol · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +131% | veri yok | +339% | 1.109 | -32% | 1.568 | 52% | 1.424 | 41% | +11% | +0.98% | 0.007 |
| B | 2 | OP/USDT | ma_cross | `kind=dema,pair=(20, 50)` | filtre=low_vol · çıkış=stop_atr=2.0,tp_r=3.0 | +154% | veri yok | +335% | 1.098 | -32% | 1.847 | 40% | 2.709 | 27% | +14% | +2.28% | 0.007 |
| B | 2 | ARB/USDT | triple_ma | `set=(10, 50, 200),kind=ema` | filtre=adx20 · çıkış=stop_atr=2.0,tp_r=3.0 | +139% | veri yok | +135% | 0.959 | -21% | 2.195 | 41% | 3.136 | 24% | +17% | +2.86% | 0.006 |
| B | 2 | ARB/USDT | ma_cross | `kind=hma,pair=(20, 100)` | filtre=low_vol · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +115% | veri yok | +111% | 0.944 | -21% | 1.692 | 53% | 1.475 | 40% | +13% | +1.23% | 0.006 |
| B | 2 | ARB/USDT | vwap_cross | `n=50` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_liquidity_sweep(≤5 bar) | +152% | veri yok | +164% | 1.017 | -27% | 2.199 | 31% | 4.839 | 17% | +14% | +1.76% | 0.005 |
| B | 2 | ARB/USDT | obv_trend | `n=20,price_n=50` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_order_block(≤3 bar) | +163% | veri yok | +188% | 0.93 | -37% | 1.587 | 33% | 3.266 | 23% | +9% | +0.87% | 0.005 |
| B | 2 | ARB/USDT | macd_zero | `cfg=(12, 26, 9)` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=cmf_flow(≤5 bar) | +128% | veri yok | +138% | 0.922 | -18% | 3.302 | 56% | 2.552 | 28% | +28% | +2.92% | 0.005 |
| B | 2 | ARB/USDT | bollinger_breakout | `n=50,k=2.5` | çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +106% | veri yok | +119% | 0.931 | -24% | 2.32 | 57% | 1.763 | 36% | +21% | +2.24% | 0.004 |
| B | 2 | ARB/USDT | donchian_breakout | `entry=40,exit=10` | filtre=low_vol · çıkış=trail_atr=3.0 | +106% | veri yok | +147% | 0.92 | -25% | 3.151 | 60% | 2.101 | 32% | +28% | +2.96% | 0.004 |
| B | 1 | ARB/USDT | donchian_breakout | `entry=40,exit=10` | çıkış=stop_atr=2.0,trail_atr=3.0 | +177% | veri yok | +214% | 0.914 | -29% | 2.018 | 53% | 1.777 | 36% | +17% | +2.06% | 0.004 |
| B | 2 | APT/USDT | ma_cross | `kind=sma,pair=(5, 20)` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_order_block(≤3 bar) | +144% | veri yok | +193% | 0.911 | -32% | 2.033 | 53% | 1.835 | 35% | +17% | +1.81% | 0.003 |
| B | 2 | ARB/USDT | supertrend_flip | `cfg=(7, 2.0)` | filtre=htf_week_sma10 · çıkış=trail_atr=3.0 | +220% | veri yok | +184% | 0.849 | -30% | 1.615 | 40% | 2.384 | 30% | +11% | +1.43% | 0.003 |
| B | 2 | ARB/USDT | roc_breakout | `n=63,th=0` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_order_block(≤0 bar) | +81% | veri yok | +75% | 0.811 | -19% | 2.077 | 47% | 2.374 | 30% | +17% | +1.48% | 0.003 |
| B | 2 | OP/USDT | smc_order_block | `k=3,max_age=50` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_ote(≤3 bar) | +103% | veri yok | +323% | 0.928 | -32% | 1.692 | 32% | 3.515 | 22% | +10% | +1.43% | 0.002 |
| B | 2 | OP/USDT | trix_cross | `n=21,signal=9` | filtre=low_vol · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +152% | veri yok | +167% | 0.924 | -32% | 1.633 | 56% | 1.274 | 44% | +12% | +1.32% | 0.002 |
| B | 2 | ARB/USDT | ma_cross | `kind=hma,pair=(20, 100)` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_bos(≤3 bar) | +150% | veri yok | +142% | 0.841 | -36% | 1.955 | 48% | 2.106 | 32% | +16% | +2.15% | 0.002 |
| B | 1 | ARB/USDT | bollinger_breakout | `n=50,k=2.5` | çıkış=stop_atr=2.0,trail_atr=3.0 | +119% | veri yok | +137% | 0.827 | -29% | 2.519 | 52% | 2.3 | 30% | +22% | +2.73% | 0.002 |
| B | 2 | ARB/USDT | smc_choch | `k=3` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=pivot_bounce(≤5 bar) | +118% | veri yok | +113% | 0.821 | -30% | 1.988 | 51% | 1.894 | 35% | +17% | +2.34% | 0.002 |
| B | 2 | APT/USDT | triple_ma | `set=(5, 20, 50),kind=ema` | filtre=low_vol · çıkış=stop_atr=2.0,max_hold=10 | +55% | veri yok | +88% | 0.807 | -21% | 1.605 | 51% | 1.541 | 39% | +12% | +0.78% | 0.002 |
| B | 2 | ARB/USDT | adx_trend | `n=10,th=20` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_order_block(≤3 bar) | +78% | veri yok | +92% | 0.779 | -25% | 1.721 | 34% | 3.279 | 23% | +11% | +1.27% | 0.002 |
| B | 2 | ARB/USDT | ichimoku_cloud | `cfg=(7, 22, 44)` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_order_block(≤3 bar) | +117% | veri yok | +116% | 0.767 | -26% | 1.856 | 38% | 3.049 | 25% | +13% | +1.44% | 0.002 |
| B | 1 | SUI/USDT | linreg_slope | `n=100,th=0.0005` | çıkış=stop_atr=2.0,trail_atr=3.0 | +91% | veri yok | +94% | 0.724 | -35% | 1.897 | 40% | 2.908 | 26% | +14% | +2.28% | 0.002 |
| B | 1 | FIL/USDT | rsi_reversal | `n=14,lo=30,exit=50` | çıkış=stop_atr=2.0,trail_atr=3.0 | +47% | +176% | +448% | 0.997 | -29% | 1.631 | 59% | 1.147 | 47% | +12% | +1.34% | 0.001 |
| B | 2 | ARB/USDT | rsi_midline | `n=21,level=60` | filtre=htf_week_sma10 · çıkış=stop_atr=2.0,max_hold=10 | +114% | veri yok | +127% | 0.76 | -28% | 1.563 | 48% | 1.731 | 37% | +11% | +1.01% | 0.001 |
| B | 2 | FIL/USDT | ppo_cross | `cfg=(12, 26, 9)` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_order_block(≤5 bar) | +131% | +282% | +414% | 0.934 | -35% | 1.811 | 42% | 2.547 | 28% | +13% | +1.32% | 0.0 |
| B | 2 | FIL/USDT | tsi_cross | `cfg=(25, 13, 7)` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_order_block(≤5 bar) | +131% | +271% | +408% | 0.932 | -33% | 1.704 | 39% | 2.697 | 27% | +12% | +1.15% | 0.0 |
| B | 2 | DOGE/USDT | linreg_slope | `n=100,th=0.0005` | filtre=low_vol · çıkış=stop_atr=2.0,tp_r=3.0 | +133% | +207% | +386% | 0.922 | -36% | 2.549 | 44% | 3.314 | 23% | +20% | +3.93% | 0.0 |
| B | 2 | ETH/USDT | bollinger_breakout | `n=50,k=2.5` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=ma_cross(≤3 bar) | +39% | +114% | +505% | 0.917 | -28% | 4.17 | 51% | 3.989 | 20% | +31% | +4.58% | 0.0 |
| B | 2 | FIL/USDT | ma_cross | `kind=sma,pair=(10, 30)` | filtre=low_vol · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +41% | +113% | +202% | 0.861 | -28% | 1.684 | 51% | 1.606 | 38% | +13% | +1.06% | 0.0 |
| B | 2 | FIL/USDT | macd_cross | `cfg=(8, 21, 5),zero_filter=False` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_ote(≤5 bar) | +71% | +357% | +296% | 0.851 | -32% | 1.729 | 40% | 2.579 | 28% | +12% | +1.10% | 0.0 |
| B | 2 | DOT/USDT | bb_squeeze | `n=20,q=0.2,look=252` | filtre=low_vol · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +59% | +216% | +159% | 0.831 | -38% | 1.746 | 59% | 1.202 | 45% | +14% | +1.13% | 0.0 |
| B | 2 | ETC/USDT | roc_breakout | `n=252,th=10` | filtre=regime_bench200 · çıkış=stop_atr=2.0,tp_r=3.0 | +101% | +321% | +474% | 0.821 | -31% | 2.423 | 47% | 2.702 | 27% | +20% | +3.97% | 0.0 |
| B | 2 | MANA/USDT | volume_breakout | `n=50,rv=1.5` | filtre=htf_week_sma10 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +25% | +87% | +133% | 0.794 | -27% | 2.6 | 68% | 1.2 | 46% | +23% | +2.68% | 0.0 |
| B | 2 | DOGE/USDT | roc_breakout | `n=126,th=5` | filtre=regime_bench200 · çıkış=stop_atr=2.0,max_hold=10 | +74% | +88% | +182% | 0.767 | -25% | 1.8 | 52% | 1.68 | 37% | +14% | +1.06% | 0.0 |
| B | 2 | MANA/USDT | rsi_divergence | `n=14,k=5,exit_level=50` | filtre=adx20 · çıkış=stop_atr=2.0,max_hold=10 | +18% | +36% | +72% | 0.752 | -16% | 2.173 | 62% | 1.328 | 43% | +19% | +1.04% | 0.0 |
| B | 2 | XRP/USDT | bb_squeeze | `n=20,q=0.1,look=252` | çıkış=stop_atr=2.0,tp_r=3.0 | +42% | +35% | +246% | 0.738 | -39% | 1.695 | 40% | 2.496 | 29% | +12% | +1.09% | 0.0 |
| B | 2 | ADA/USDT | smc_ote | `k=3,fib_lo=0.5` | filtre=htf_week_sma10 · çıkış=stop_atr=2.0,tp_r=3.0 | +86% | +104% | +282% | 0.735 | -35% | 1.404 | 44% | 1.747 | 36% | +8% | +0.52% | 0.0 |
| B | 2 | UNI/USDT | bollinger_breakout | `n=50,k=2.5` | filtre=low_vol · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +25% | +64% | +92% | 0.733 | -19% | 2.175 | 65% | 1.171 | 46% | +19% | +1.90% | 0.0 |
| B | 2 | DOGE/USDT | roc_breakout | `n=126,th=5` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_liquidity_sweep(≤3 bar) | +51% | +80% | +124% | 0.731 | -28% | 2.742 | 45% | 3.352 | 23% | +22% | +2.27% | 0.0 |
| B | 2 | ETH/USDT | keltner_breakout | `n=20,k=2.5` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=ma_cross(≤5 bar) | +9% | +61% | +321% | 0.729 | -32% | 2.974 | 53% | 2.676 | 27% | +25% | +3.16% | 0.0 |
| B | 2 | IMX/USDT | donchian_breakout | `entry=100,exit=10` | filtre=htf_week_sma10 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +105% | veri yok | +133% | 0.72 | -37% | 1.749 | 61% | 1.137 | 47% | +14% | +1.76% | 0.0 |
| B | 2 | AVAX/USDT | roc_breakout | `n=252,th=10` | filtre=regime_bench200 · çıkış=stop_atr=2.0,max_hold=10 | +54% | +111% | +103% | 0.653 | -26% | 2.542 | 65% | 1.362 | 42% | +23% | +2.03% | 0.0 |
| B | 2 | MINA/USDT | bb_squeeze | `n=20,q=0.1,look=252` | çıkış=signal_only | +105% | +142% | +132% | 0.639 | -33% | 1.772 | 45% | 2.177 | 32% | +13% | +1.45% | 0.0 |
| B | 2 | ETH/USDT | price_ma | `kind=ema,n=150` | filtre=htf_week_sma10 · çıkış=stop_atr=2.0,tp_r=3.0 | +38% | +57% | +175% | 0.636 | -29% | 1.813 | 28% | 4.779 | 17% | +10% | +1.05% | 0.0 |
| B | 2 | DOT/USDT | bb_squeeze | `n=20,q=0.2,look=252` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=ma_cross(≤0 bar) | +10% | +54% | +90% | 0.611 | -22% | 3.202 | 61% | 2.022 | 33% | +28% | +2.71% | 0.0 |
| B | 2 | ETH/USDT | keltner_breakout | `n=20,k=2.5` | filtre=low_vol · çıkış=stop_atr=2.0,tp_r=3.0 | +42% | +62% | +116% | 0.592 | -34% | 2.127 | 47% | 2.372 | 30% | +18% | +1.73% | 0.0 |
| B | 2 | XLM/USDT | ma_cross | `kind=sma,pair=(10, 50)` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_order_block(≤5 bar) | +24% | +32% | +187% | 0.576 | -32% | 1.826 | 41% | 2.628 | 28% | +13% | +1.50% | 0.0 |

## Coin coin özet (ajan günlüğü)

- **AAVE/USDT**: 68 aday denendi, 0 kaldı. En iyi aday triple_ma (`set=(10, 50, 200),kind=ema`, çıkış=stop_atr=2.0,trail_atr=3.0): S1 — 3y -5%, 5y +69%, full +12%; 105 işlem (zararlı: 3y).
- **ADA/USDT**: 72 aday denendi, 1 kaldı. En iyi aday smc_ote (`k=3,fib_lo=0.5`, filtre=htf_week_sma10 · çıkış=stop_atr=2.0,tp_r=3.0): OK — tüm adımlar geçti.
- **ALGO/USDT**: 72 aday denendi, 0 kaldı. En iyi aday rsi_divergence (`n=14,k=5,exit_level=50`, filtre=regime_bench200 · çıkış=signal_only): S7 — PSR 0.878.
- **APT/USDT**: 83 aday denendi, 3 kaldı. En iyi aday macd_zero (`cfg=(12, 26, 9)`, filtre=htf_week_sma10 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0): OK — tüm adımlar geçti.
- **ARB/USDT**: 125 aday denendi, 39 kaldı. En iyi aday price_ma (`kind=kama,n=200`, filtre=trend_sma200 · çıkış=stop_atr=2.0,tp_r=3.0): OK — tüm adımlar geçti.
- **ATOM/USDT**: 68 aday denendi, 0 kaldı. En iyi aday rsi_reversal (`n=28,lo=20,exit=50`, çıkış=stop_atr=2.0,trail_atr=3.0): S1 — 3y +8%, 5y +8%, full +4%; 2 işlem.
- **AVAX/USDT**: 71 aday denendi, 1 kaldı. En iyi aday roc_breakout (`n=252,th=10`, filtre=regime_bench200 · çıkış=stop_atr=2.0,max_hold=10): OK — tüm adımlar geçti.
- **AXS/USDT**: 71 aday denendi, 0 kaldı. En iyi aday roc_breakout (`n=252,th=5`, filtre=low_vol · çıkış=trail_atr=3.0): S4 — komşu ayarların %33'i kârlı.
- **BCH/USDT**: 70 aday denendi, 0 kaldı. En iyi aday volume_breakout (`n=50,rv=2.0`, filtre=low_vol · çıkış=trail_atr=3.0): S4 — komşu ayarların %33'i kârlı.
- **BNB/USDT**: 70 aday denendi, 0 kaldı. En iyi aday rsi_divergence (`n=14,k=3,exit_level=70`, çıkış=stop_atr=2.0,trail_atr=3.0): S2 — PF 1.205, 1x maks. düşüş -43%.
- **BTC/USDT**: 70 aday denendi, 0 kaldı. En iyi aday donchian_breakout (`entry=100,exit=10`, filtre=htf_week_sma10 · çıkış=stop_atr=2.0,tp_r=3.0): S2 — PF 1.347, 1x maks. düşüş -47%.
- **CRV/USDT**: 74 aday denendi, 0 kaldı. En iyi aday roc_breakout (`n=252,th=0`, filtre=adx20 · çıkış=stop_atr=2.0,tp_r=3.0): S2 — PF 1.408, 1x maks. düşüş -52%.
- **DOGE/USDT**: 74 aday denendi, 3 kaldı. En iyi aday linreg_slope (`n=100,th=0.0005`, filtre=low_vol · çıkış=stop_atr=2.0,tp_r=3.0): OK — tüm adımlar geçti.
- **DOT/USDT**: 79 aday denendi, 2 kaldı. En iyi aday bb_squeeze (`n=20,q=0.2,look=252`, filtre=low_vol · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0): OK — tüm adımlar geçti.
- **ETC/USDT**: 69 aday denendi, 1 kaldı. En iyi aday roc_breakout (`n=252,th=10`, filtre=regime_bench200 · çıkış=stop_atr=2.0,tp_r=3.0): OK — tüm adımlar geçti.
- **ETH/USDT**: 86 aday denendi, 4 kaldı. En iyi aday bollinger_breakout (`n=50,k=2.5`, çıkış=stop_atr=2.0,trail_atr=3.0 · onay=ma_cross(≤3 bar)): OK — tüm adımlar geçti.
- **FIL/USDT**: 90 aday denendi, 5 kaldı. En iyi aday rsi_reversal (`n=14,lo=30,exit=50`, çıkış=stop_atr=2.0,trail_atr=3.0): OK — tüm adımlar geçti.
- **IMX/USDT**: 77 aday denendi, 1 kaldı. En iyi aday donchian_breakout (`entry=100,exit=10`, filtre=htf_week_sma10 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0): OK — tüm adımlar geçti.
- **INJ/USDT**: 70 aday denendi, 0 kaldı. En iyi aday funding_extreme (`n=90,th=2.0`, çıkış=stop_atr=2.0,trail_atr=3.0): S5 — 1 bar geç girişte Sharpe'ın %7'i kalıyor.
- **LINK/USDT**: 68 aday denendi, 0 kaldı. En iyi aday gap_fade (`g=0.02`, çıkış=stop_atr=2.0,trail_atr=3.0): S1 — 3y +0%, 5y +0%, full +5%; 1 işlem (zararlı: 3y, 5y).
- **LTC/USDT**: 68 aday denendi, 0 kaldı. En iyi aday bb_squeeze (`n=20,q=0.1,look=126`, çıkış=stop_atr=2.0,trail_atr=3.0): S1 — 3y -16%, 5y -27%, full +13%; 134 işlem (zararlı: 3y, 5y).
- **MANA/USDT**: 74 aday denendi, 2 kaldı. En iyi aday volume_breakout (`n=50,rv=1.5`, filtre=htf_week_sma10 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0): OK — tüm adımlar geçti.
- **MINA/USDT**: 80 aday denendi, 1 kaldı. En iyi aday bb_squeeze (`n=20,q=0.1,look=252`, çıkış=signal_only): OK — tüm adımlar geçti.
- **NEAR/USDT**: 68 aday denendi, 0 kaldı. En iyi aday ma_cross (`kind=kama,pair=(50, 200)`, çıkış=stop_atr=2.0,trail_atr=3.0): S1 — 3y -15%, 5y +82%, full +55%; 41 işlem (zararlı: 3y).
- **OP/USDT**: 87 aday denendi, 5 kaldı. En iyi aday vortex_cross (`n=28`, çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_ote(≤5 bar)): OK — tüm adımlar geçti.
- **PYTH/USDT**: elendi (S0: 2.9 yıl veri var, en az 3.0 yıl gerekli).
- **SAND/USDT**: 78 aday denendi, 0 kaldı. En iyi aday rsi_divergence (`n=14,k=5,exit_level=50`, çıkış=stop_atr=2.0,trail_atr=3.0 · onay=macd_divergence(≤0 bar)): S7 — PSR 0.81.
- **SNX/USDT**: 69 aday denendi, 0 kaldı. En iyi aday pivot_bounce (`window=20`, filtre=regime_bench200 · çıkış=stop_atr=2.0,trail_atr=3.0): S4 — komşu ayarların %0'i kârlı.
- **SOL/USDT**: 68 aday denendi, 0 kaldı. En iyi aday triple_ma (`set=(5, 20, 50),kind=sma`, çıkış=stop_atr=2.0,trail_atr=3.0): S1 — 3y -20%, 5y +38%, full -52%; 274 işlem (zararlı: 3y, full).
- **SUI/USDT**: 72 aday denendi, 1 kaldı. En iyi aday linreg_slope (`n=100,th=0.0005`, çıkış=stop_atr=2.0,trail_atr=3.0): OK — tüm adımlar geçti.
- **THETA/USDT**: 70 aday denendi, 0 kaldı. En iyi aday roc_breakout (`n=252,th=10`, çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_order_block(≤3 bar)): S2 — PF 2.11, 1x maks. düşüş -47%.
- **TRX/USDT**: 70 aday denendi, 0 kaldı. En iyi aday bb_squeeze (`n=20,q=0.1,look=252`, çıkış=stop_atr=2.0,trail_atr=3.0): S3 — 2.0x maliyette getiri -14%.
- **UNI/USDT**: 78 aday denendi, 1 kaldı. En iyi aday bollinger_breakout (`n=50,k=2.5`, filtre=low_vol · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0): OK — tüm adımlar geçti.
- **XLM/USDT**: 74 aday denendi, 1 kaldı. En iyi aday ma_cross (`kind=sma,pair=(10, 50)`, çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_order_block(≤5 bar)): OK — tüm adımlar geçti.
- **XRP/USDT**: 72 aday denendi, 1 kaldı. En iyi aday bb_squeeze (`n=20,q=0.1,look=252`, çıkış=stop_atr=2.0,tp_r=3.0): OK — tüm adımlar geçti.

## Zayıf yönler (dürüst liste)

- 31032 deneme yapıldı. Bu kadar çok denemede şans eseri iyi görünen strateji çıkar. DSR bunu düzeltir; tier A sadece DSR ≥ eşik olanlardır.
- Seçim ve test aynı geçmiş veride yapıldı. Gerçek test arenadaki ileri (paper) kayıttır.
- Survivorship: liste bugünün coinlerinden oluşur. Borsadan silinen coinler yok, bu sonucu iyimser yapar.
- Funding sabit yıllık oranla, likidasyon işlem bazında yaklaşık modellenir.
- Tek borsa verisi (Bitget, yoksa OKX/KuCoin). Emir defteri ve piyasa etkisi modellenmez.

## Arena

Arena: 100 aktif (eleme geçen), 0 kontrol (yakın aday, switcher kullanmaz), 3 yeni üye, 0 kontrolden aktife. Üst sınır 100.

## Switcher backtest kapısı

Geçti: **False** — kontroller: `{"beats_equal_weight_all_windows": false, "positive_at_cost_stress": true, "max_dd_ok": true}`

Pencereler: `{"3y": {"sharpe": 1.375, "ew_sharpe": 2.146}, "5y": {"sharpe": 1.511, "ew_sharpe": 2.175}, "full": {"sharpe": 0.844, "ew_sharpe": 1.239}}`
