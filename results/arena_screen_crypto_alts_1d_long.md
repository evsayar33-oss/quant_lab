# Eleme motoru — crypto_alts 1d

Veri: 2018-07-24 → 2026-10-19. Coin: 32 uygun (toplam 35). Denenen varyant: 553 × coin = **39312 deneme**.
Her (coin, kural) için tek en iyi nokta değil, **en sağlam bölgenin merkezi** seçildi. Bu bir aday listesidir, karar değildir. Karar sadece doğrulama kapısında verilir.

## Huni

| Adım | Ne kontrol edilir | Elenen | Kalan |
|---|---|---|---|
| S0 | veri yetersiz | 186 | 1984 |
| S1 | her dönemde kârlı değil / az işlem | 1715 | 269 |
| S2 | kâr faktörü veya düşüş zayıf | 230 | 39 |
| S3 | yüksek maliyette zarar | 1 | 38 |
| S4 | plato yok (komşu ayarlar zararda) | 3 | 35 |
| S5 | 1 bar gecikmeye dayanıksız | 11 | 24 |
| S6 | yılların çoğunda kârlı değil | 5 | 19 |
| S7 | istatistiksel güven düşük (PSR) | 6 | 13 |

## 2. aşama: filtre × çıkış × kombo (sadece S1'i geçen adaylarda)

269 aday → 21616 ek deneme (DSR'a eklendi). Her aday için en sağlam filtre/çıkış hücresi ve en sağlam kombo seçildi; kombo sadece kuralı tek başına geçerse aday olur. Seçilenler aynı S1–S7 adımlarından geçti.

| Adım | Ne kontrol edilir | Elenen | Kalan |
|---|---|---|---|
| S0 | veri yetersiz | 0 | 446 |
| S1 | her dönemde kârlı değil / az işlem | 282 | 164 |
| S2 | kâr faktörü veya düşüş zayıf | 100 | 64 |
| S3 | yüksek maliyette zarar | 0 | 64 |
| S4 | plato yok (komşu ayarlar zararda) | 9 | 55 |
| S5 | 1 bar gecikmeye dayanıksız | 7 | 48 |
| S6 | yılların çoğunda kârlı değil | 5 | 43 |
| S7 | istatistiksel güven düşük (PSR) | 4 | 39 |

## Geçenler (52)

| Tier | Aşama | Coin | Kural | Ayar | Varyant | 3y | 5y | Tüm | Sharpe | 1x DD | PF | DSR |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| B | 2 | SUI/USDT | price_ma | `kind=sma,n=20` | filtre=low_vol · çıkış=stop_atr=2.0,tp_r=3.0 | +900% | veri yok | +890% | 1.581 | -28% | 4.369 | 0.342 |
| B | 2 | XLM/USDT | nr7_breakout | `n=4` | filtre=low_vol · çıkış=signal_only | +667% | veri yok | +667% | 1.303 | -38% | 5.808 | 0.121 |
| B | 1 | XLM/USDT | stoch_reversal | `k=9,d=3,smooth=3,lo=10` | çıkış=stop_atr=2.0,trail_atr=3.0 | +234% | veri yok | +216% | 1.086 | -30% | 2.344 | 0.088 |
| B | 2 | SOL/USDT | vwap_cross | `n=10` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=price_ma(≤5 bar) | +564% | +609% | +609% | 1.221 | -35% | 3.522 | 0.086 |
| B | 2 | BTC/USDT | awesome_zero | `fast=5,slow=34` | filtre=low_vol · çıkış=stop_atr=2.0,be_r=1.0 | +90% | +62% | +1676% | 1.301 | -36% | 7.425 | 0.078 |
| B | 2 | BNB/USDT | obv_trend | `n=20,price_n=20` | filtre=htf_week_sma10 · çıkış=stop_atr=2.0,tp_r=3.0 | +138% | veri yok | +133% | 1.097 | -16% | 2.492 | 0.076 |
| B | 2 | SUI/USDT | elder_impulse | `ema_n=13,macd_cfg=(12, 26, 9)` | filtre=low_vol · çıkış=stop_atr=2.0,tp_r=3.0 | +285% | veri yok | +281% | 1.009 | -36% | 2.078 | 0.066 |
| B | 2 | XRP/USDT | cci_breakout | `n=14,level=100` | filtre=low_vol · çıkış=signal_only | +475% | +570% | +8005% | 1.302 | -38% | 5.916 | 0.064 |
| B | 2 | BNB/USDT | smc_order_block | `k=3,max_age=50` | filtre=htf_week_sma10 · çıkış=signal_only | +206% | veri yok | +191% | 0.942 | -38% | 3.887 | 0.046 |
| B | 2 | BNB/USDT | smc_fvg | `max_age=40,min_gap_atr=0.5` | çıkış=signal_only | +164% | veri yok | +165% | 0.869 | -25% | 2.725 | 0.035 |
| B | 2 | BNB/USDT | tsi_cross | `cfg=(25, 13, 7)` | filtre=trend_sma200 · çıkış=stop_atr=2.0,tp_r=3.0 | +103% | veri yok | +103% | 0.878 | -22% | 2.541 | 0.032 |
| B | 2 | BTC/USDT | trix_cross | `n=12,signal=7` | filtre=trend_sma200 · çıkış=stop_atr=2.0,be_r=1.0 | +74% | +99% | +922% | 1.143 | -39% | 3.828 | 0.028 |
| B | 2 | AXS/USDT | rsi_reversal | `n=2,lo=10,exit=50` | filtre=adx20 · çıkış=signal_only | +112% | +329% | +329% | 1.022 | -27% | 2.966 | 0.025 |
| B | 2 | BNB/USDT | stoch_reversal | `k=21,d=5,smooth=1,lo=25` | çıkış=trail_atr=3.0 | +85% | veri yok | +87% | 0.781 | -36% | 1.925 | 0.025 |
| B | 2 | BNB/USDT | elder_impulse | `ema_n=13,macd_cfg=(12, 26, 9)` | filtre=htf_week_sma10 · çıkış=stop_atr=2.0,max_hold=10 | +115% | veri yok | +103% | 0.759 | -32% | 1.787 | 0.021 |
| B | 2 | IMX/USDT | price_ma | `kind=kama,n=100` | filtre=low_vol · çıkış=stop_atr=2.0,max_hold=10 | +226% | veri yok | +186% | 0.866 | -36% | 2.567 | 0.017 |
| B | 2 | CRV/USDT | force_index | `n=2` | filtre=regime_bench200 · çıkış=signal_only | +82% | +224% | +318% | 0.881 | -40% | 1.969 | 0.015 |
| B | 2 | ARB/USDT | down_days | `n=3,hold_exit=1` | çıkış=trail_atr=3.0 | +45% | veri yok | +91% | 0.694 | -40% | 1.576 | 0.015 |
| B | 2 | DOT/USDT | rsi_reversal | `n=5,lo=20,exit=50` | filtre=adx20 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +98% | veri yok | +124% | 0.726 | -25% | 2.56 | 0.011 |
| B | 2 | XRP/USDT | heikin_ashi | `confirm=3` | filtre=low_vol · çıkış=signal_only | +182% | +309% | +1525% | 1.059 | -33% | 3.06 | 0.01 |
| B | 1 | DOGE/USDT | smc_ote | `k=3,fib_lo=0.5` | çıkış=stop_atr=2.0,trail_atr=3.0 | +144% | +187% | +243% | 0.838 | -36% | 1.857 | 0.01 |
| B | 2 | ETH/USDT | tsi_cross | `cfg=(25, 13, 7)` | filtre=low_vol · çıkış=signal_only | +120% | +59% | +984% | 0.958 | -38% | 2.614 | 0.009 |
| B | 1 | TRX/USDT | down_days | `n=3,hold_exit=1` | çıkış=stop_atr=2.0,trail_atr=3.0 | +34% | +58% | +356% | 0.945 | -26% | 2.19 | 0.009 |
| B | 2 | BTC/USDT | cci_breakout | `n=40,level=100` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_bos(≤5 bar) | +49% | +29% | +636% | 0.954 | -29% | 3.291 | 0.008 |
| B | 1 | ETH/USDT | ma_cross | `kind=dema,pair=(20, 50)` | çıkış=stop_atr=2.0,trail_atr=3.0 | +98% | +141% | +876% | 0.948 | -32% | 3.72 | 0.007 |
| B | 2 | BTC/USDT | tsi_cross | `cfg=(25, 13, 7)` | filtre=low_vol · çıkış=stop_atr=2.0,be_r=1.0 | +58% | +39% | +446% | 0.943 | -37% | 2.612 | 0.006 |
| B | 1 | ETH/USDT | trix_cross | `n=21,signal=7` | çıkış=stop_atr=2.0,trail_atr=3.0 | +79% | +147% | +1071% | 0.919 | -36% | 2.812 | 0.006 |
| B | 2 | AAVE/USDT | stoch_reversal | `k=5,d=5,smooth=1,lo=10` | filtre=adx20 · çıkış=stop_atr=2.0,trail_atr=3.0 | +30% | +76% | +126% | 0.697 | -32% | 2.893 | 0.006 |
| B | 1 | DOT/USDT | rsi_reversal | `n=5,lo=20,exit=50` | çıkış=stop_atr=2.0,trail_atr=3.0 | +74% | veri yok | +109% | 0.652 | -26% | 2.064 | 0.006 |
| B | 2 | OP/USDT | force_index | `n=2` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_fvg(≤5 bar) | +70% | veri yok | +114% | 0.646 | -31% | 1.818 | 0.006 |
| B | 2 | UNI/USDT | stoch_reversal | `k=5,d=3,smooth=1,lo=10` | filtre=low_vol · çıkış=signal_only | +154% | +195% | +195% | 0.763 | -29% | 2.953 | 0.005 |
| B | 2 | UNI/USDT | force_index | `n=2` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=cci_breakout(≤3 bar) | +74% | +89% | +136% | 0.825 | -17% | 3.095 | 0.004 |
| B | 2 | BTC/USDT | wavetrend_reversal | `n1=9,n2=18,lo=-40` | çıkış=stop_atr=2.0,max_hold=10 | +25% | +55% | +281% | 0.852 | -22% | 3.228 | 0.003 |
| B | 2 | AAVE/USDT | bollinger_reversion | `n=30,k=1.5` | filtre=adx20 · çıkış=stop_atr=2.0,max_hold=10 | +80% | +139% | +152% | 0.61 | -39% | 1.756 | 0.003 |
| B | 1 | ETH/USDT | roc_breakout | `n=63,th=5` | çıkış=stop_atr=2.0,trail_atr=3.0 | +75% | +21% | +415% | 0.805 | -40% | 3.101 | 0.002 |
| B | 2 | LTC/USDT | hurst_switch | `n=100,fast=20,rsi_n=2` | filtre=htf_week_sma10 · çıkış=signal_only | +81% | +119% | +318% | 0.803 | -24% | 3.406 | 0.002 |
| B | 1 | BTC/USDT | keltner_breakout | `n=50,k=2.0` | çıkış=stop_atr=2.0,trail_atr=3.0 | +27% | +28% | +420% | 0.772 | -37% | 2.496 | 0.002 |
| B | 1 | BTC/USDT | cci_breakout | `n=40,level=100` | çıkış=stop_atr=2.0,trail_atr=3.0 | +46% | +39% | +421% | 0.756 | -37% | 2.156 | 0.002 |
| B | 2 | SNX/USDT | rsi_reversal | `n=2,lo=10,exit=50` | filtre=regime_bench200 · çıkış=signal_only | +164% | +152% | +162% | 0.742 | -29% | 2.518 | 0.002 |
| B | 2 | CRV/USDT | zscore_reversion | `n=20,z=1.5` | filtre=low_vol · çıkış=trail_atr=3.0 | +47% | +85% | +85% | 0.554 | -31% | 1.965 | 0.002 |
| B | 2 | CRV/USDT | bollinger_reversion | `n=20,k=1.5` | filtre=low_vol · çıkış=trail_atr=3.0 | +47% | +85% | +85% | 0.554 | -31% | 1.965 | 0.002 |
| B | 2 | LTC/USDT | down_days | `n=4,hold_exit=3` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=pivot_bounce(≤5 bar) | +14% | +69% | +330% | 0.758 | -35% | 2.264 | 0.001 |
| B | 1 | BTC/USDT | awesome_zero | `fast=5,slow=34` | çıkış=stop_atr=2.0,trail_atr=3.0 | +39% | +26% | +306% | 0.705 | -36% | 2.227 | 0.001 |
| B | 2 | ADA/USDT | cci_reversal | `n=14,lo=-150` | filtre=adx20 · çıkış=trail_atr=3.0 | +143% | veri yok | +180% | 0.674 | -34% | 2.662 | 0.001 |
| B | 2 | TRX/USDT | hurst_switch | `n=100,fast=20,rsi_n=2` | filtre=regime_bench200 · çıkış=trail_atr=3.0 | +76% | +92% | +134% | 0.632 | -35% | 2.14 | 0.001 |
| B | 2 | TRX/USDT | smc_ote | `k=3,fib_lo=0.618` | çıkış=signal_only | +140% | +133% | +666% | 0.785 | -35% | 3.225 | 0.0 |
| B | 1 | TRX/USDT | smc_ote | `k=3,fib_lo=0.618` | çıkış=stop_atr=2.0,trail_atr=3.0 | +145% | +137% | +543% | 0.731 | -35% | 2.819 | 0.0 |
| B | 2 | BTC/USDT | ibs_reversion | `lo=0.3,hi=0.8` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_liquidity_sweep(≤3 bar) | +27% | +49% | +132% | 0.684 | -23% | 2.062 | 0.0 |
| B | 1 | TRX/USDT | stoch_reversal | `k=5,d=5,smooth=3,lo=10` | çıkış=stop_atr=2.0,trail_atr=3.0 | +19% | +36% | +135% | 0.612 | -30% | 2.678 | 0.0 |
| B | 2 | LTC/USDT | hurst_switch | `n=100,fast=20,rsi_n=2` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_order_block(≤5 bar) | +79% | +62% | +176% | 0.597 | -29% | 2.034 | 0.0 |
| B | 2 | BCH/USDT | cmf_flow | `n=20,th=0.2` | filtre=low_vol · çıkış=stop_atr=2.0,max_hold=10 | +41% | +63% | +304% | 0.593 | -38% | 2.747 | 0.0 |
| B | 1 | BTC/USDT | bollinger_reversion | `n=20,k=2.0` | çıkış=stop_atr=2.0,trail_atr=3.0 | +15% | +31% | +118% | 0.504 | -35% | 1.765 | 0.0 |

## Coin coin özet (ajan günlüğü)

- **AAVE/USDT**: 80 aday denendi, 2 kaldı. En iyi aday stoch_reversal (`k=5,d=5,smooth=1,lo=10`, filtre=adx20 · çıkış=stop_atr=2.0,trail_atr=3.0): OK — tüm adımlar geçti.
- **ADA/USDT**: 70 aday denendi, 1 kaldı. En iyi aday cci_reversal (`n=14,lo=-150`, filtre=adx20 · çıkış=trail_atr=3.0): OK — tüm adımlar geçti.
- **ALGO/USDT**: elendi (S0: 1.8 yıl veri var, en az 3.0 yıl gerekli).
- **APT/USDT**: 65 aday denendi, 0 kaldı. En iyi aday ultimate_reversal (`a=5,lo=35`, çıkış=stop_atr=2.0,trail_atr=3.0): S2 — PF 1.548, 1x maks. düşüş -45%.
- **ARB/USDT**: 76 aday denendi, 1 kaldı. En iyi aday down_days (`n=3,hold_exit=1`, çıkış=trail_atr=3.0): OK — tüm adımlar geçti.
- **ATOM/USDT**: 66 aday denendi, 0 kaldı. En iyi aday hurst_switch (`n=200,fast=20,rsi_n=2`, çıkış=stop_atr=2.0,trail_atr=3.0 · onay=pivot_bounce(≤3 bar)): S5 — 1 bar geç girişte Sharpe'ın %37'i kalıyor.
- **AVAX/USDT**: 67 aday denendi, 0 kaldı. En iyi aday smc_fvg (`max_age=40,min_gap_atr=0.0`, filtre=trend_sma200 · çıkış=signal_only): S2 — PF 2.286, 1x maks. düşüş -55%.
- **AXS/USDT**: 69 aday denendi, 1 kaldı. En iyi aday rsi_reversal (`n=2,lo=10,exit=50`, filtre=adx20 · çıkış=signal_only): OK — tüm adımlar geçti.
- **BCH/USDT**: 79 aday denendi, 1 kaldı. En iyi aday cmf_flow (`n=20,th=0.2`, filtre=low_vol · çıkış=stop_atr=2.0,max_hold=10): OK — tüm adımlar geçti.
- **BNB/USDT**: 102 aday denendi, 6 kaldı. En iyi aday obv_trend (`n=20,price_n=20`, filtre=htf_week_sma10 · çıkış=stop_atr=2.0,tp_r=3.0): OK — tüm adımlar geçti.
- **BTC/USDT**: 89 aday denendi, 10 kaldı. En iyi aday awesome_zero (`fast=5,slow=34`, filtre=low_vol · çıkış=stop_atr=2.0,be_r=1.0): OK — tüm adımlar geçti.
- **CRV/USDT**: 84 aday denendi, 3 kaldı. En iyi aday force_index (`n=2`, filtre=regime_bench200 · çıkış=signal_only): OK — tüm adımlar geçti.
- **DOGE/USDT**: 63 aday denendi, 1 kaldı. En iyi aday smc_ote (`k=3,fib_lo=0.5`, çıkış=stop_atr=2.0,trail_atr=3.0): OK — tüm adımlar geçti.
- **DOT/USDT**: 66 aday denendi, 2 kaldı. En iyi aday rsi_reversal (`n=5,lo=20,exit=50`, filtre=adx20 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0): OK — tüm adımlar geçti.
- **ETC/USDT**: 67 aday denendi, 0 kaldı. En iyi aday ma_cross (`kind=sma,pair=(10, 50)`, çıkış=stop_atr=2.0,trail_atr=3.0): S2 — PF 2.885, 1x maks. düşüş -46%.
- **ETH/USDT**: 84 aday denendi, 4 kaldı. En iyi aday tsi_cross (`cfg=(25, 13, 7)`, filtre=low_vol · çıkış=signal_only): OK — tüm adımlar geçti.
- **FIL/USDT**: 70 aday denendi, 0 kaldı. En iyi aday rsi_reversal (`n=5,lo=25,exit=50`, çıkış=stop_atr=2.0,trail_atr=3.0 · onay=pivot_bounce(≤3 bar)): S4 — komşu ayarların %40'i kârlı.
- **IMX/USDT**: 74 aday denendi, 1 kaldı. En iyi aday price_ma (`kind=kama,n=100`, filtre=low_vol · çıkış=stop_atr=2.0,max_hold=10): OK — tüm adımlar geçti.
- **INJ/USDT**: elendi (S0: 2.9 yıl veri var, en az 3.0 yıl gerekli).
- **LINK/USDT**: 75 aday denendi, 0 kaldı. En iyi aday obv_trend (`n=20,price_n=50`, filtre=htf_week_sma10 · çıkış=stop_atr=2.0,max_hold=10): S7 — PSR 0.846.
- **LTC/USDT**: 77 aday denendi, 3 kaldı. En iyi aday hurst_switch (`n=100,fast=20,rsi_n=2`, filtre=htf_week_sma10 · çıkış=signal_only): OK — tüm adımlar geçti.
- **MANA/USDT**: 64 aday denendi, 0 kaldı. En iyi aday obv_trend (`n=20,price_n=50`, filtre=low_vol · çıkış=stop_atr=2.0,max_hold=10): S2 — PF 3.605, 1x maks. düşüş -45%.
- **MINA/USDT**: 78 aday denendi, 0 kaldı. En iyi aday atr_breakout (`n=10,k=1.0`, filtre=regime_bench200 · çıkış=signal_only): S2 — PF 2.683, 1x maks. düşüş -51%.
- **NEAR/USDT**: 95 aday denendi, 0 kaldı. En iyi aday ppo_cross (`cfg=(12, 26, 9)`, filtre=low_vol · çıkış=stop_atr=2.0,be_r=1.0): S2 — PF 3.722, 1x maks. düşüş -45%.
- **OP/USDT**: 69 aday denendi, 1 kaldı. En iyi aday force_index (`n=2`, çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_fvg(≤5 bar)): OK — tüm adımlar geçti.
- **PYTH/USDT**: elendi (S0: 2.9 yıl veri var, en az 3.0 yıl gerekli).
- **SAND/USDT**: 62 aday denendi, 0 kaldı. En iyi aday mfi_reversal (`n=21,lo=20`, çıkış=stop_atr=2.0,trail_atr=3.0): S1 — 3y +21%, full +72%; 5 işlem.
- **SNX/USDT**: 64 aday denendi, 1 kaldı. En iyi aday rsi_reversal (`n=2,lo=10,exit=50`, filtre=regime_bench200 · çıkış=signal_only): OK — tüm adımlar geçti.
- **SOL/USDT**: 93 aday denendi, 1 kaldı. En iyi aday vwap_cross (`n=10`, çıkış=stop_atr=2.0,trail_atr=3.0 · onay=price_ma(≤5 bar)): OK — tüm adımlar geçti.
- **SUI/USDT**: 87 aday denendi, 2 kaldı. En iyi aday price_ma (`kind=sma,n=20`, filtre=low_vol · çıkış=stop_atr=2.0,tp_r=3.0): OK — tüm adımlar geçti.
- **THETA/USDT**: 65 aday denendi, 0 kaldı. En iyi aday hammer_star (`lookback_low=10`, çıkış=stop_atr=2.0,trail_atr=3.0): S6 — yılların %57'i kârlı.
- **TRX/USDT**: 103 aday denendi, 5 kaldı. En iyi aday down_days (`n=3,hold_exit=1`, çıkış=stop_atr=2.0,trail_atr=3.0): OK — tüm adımlar geçti.
- **UNI/USDT**: 74 aday denendi, 2 kaldı. En iyi aday stoch_reversal (`k=5,d=3,smooth=1,lo=10`, filtre=low_vol · çıkış=signal_only): OK — tüm adımlar geçti.
- **XLM/USDT**: 74 aday denendi, 2 kaldı. En iyi aday nr7_breakout (`n=4`, filtre=low_vol · çıkış=signal_only): OK — tüm adımlar geçti.
- **XRP/USDT**: 79 aday denendi, 2 kaldı. En iyi aday cci_breakout (`n=14,level=100`, filtre=low_vol · çıkış=signal_only): OK — tüm adımlar geçti.

## Zayıf yönler (dürüst liste)

- 39312 deneme yapıldı. Bu kadar çok denemede şans eseri iyi görünen strateji çıkar. DSR bunu düzeltir; tier A sadece DSR ≥ eşik olanlardır.
- Seçim ve test aynı geçmiş veride yapıldı. Gerçek test arenadaki ileri (paper) kayıttır.
- Survivorship: liste bugünün coinlerinden oluşur. Borsadan silinen coinler yok, bu sonucu iyimser yapar.
- Funding sabit yıllık oranla, likidasyon işlem bazında yaklaşık modellenir.
- Tek borsa verisi (Bitget, yoksa OKX/KuCoin). Emir defteri ve piyasa etkisi modellenmez.

## Arena

Arena: 47 aktif (eleme geçen), 53 kontrol (yakın aday, switcher kullanmaz), 100 yeni üye, 0 kontrolden aktife. Üst sınır 100.

## Switcher backtest kapısı

Geçti: **False** — kontroller: `{"beats_equal_weight_all_windows": false, "positive_at_cost_stress": true, "max_dd_ok": true}`

Pencereler: `{"3y": {"sharpe": 1.368, "ew_sharpe": 2.639}, "5y": {"sharpe": 0.773, "ew_sharpe": 2.029}, "full": {"sharpe": 1.081, "ew_sharpe": 2.346}}`
