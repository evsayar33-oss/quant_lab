# Eleme motoru — crypto_alts 1d

Veri: 2018-07-24 → 2026-10-19. Coin: 32 uygun (toplam 35). Denenen varyant: 553 × coin = **31240 deneme**.
Her (coin, kural) için tek en iyi nokta değil, **en sağlam bölgenin merkezi** seçildi. Bu bir aday listesidir, karar değildir. Karar sadece doğrulama kapısında verilir.

## Huni

| Adım | Ne kontrol edilir | Elenen | Kalan |
|---|---|---|---|
| S0 | veri yetersiz | 186 | 1984 |
| S1 | her dönemde kârlı değil / az işlem | 1815 | 169 |
| S2 | kâr faktörü veya düşüş zayıf | 149 | 20 |
| S3 | yüksek maliyette zarar | 2 | 18 |
| S4 | plato yok (komşu ayarlar zararda) | 3 | 15 |
| S5 | 1 bar gecikmeye dayanıksız | 4 | 11 |
| S6 | yılların çoğunda kârlı değil | 4 | 7 |
| S7 | istatistiksel güven düşük (PSR) | 3 | 4 |

## 2. aşama: filtre × çıkış × kombo (sadece S1'i geçen adaylarda)

169 aday → 13544 ek deneme (DSR'a eklendi). Her aday için en sağlam filtre/çıkış hücresi ve en sağlam kombo seçildi; kombo sadece kuralı tek başına geçerse aday olur. Seçilenler aynı S1–S7 adımlarından geçti.

| Adım | Ne kontrol edilir | Elenen | Kalan |
|---|---|---|---|
| S0 | veri yetersiz | 0 | 303 |
| S1 | her dönemde kârlı değil / az işlem | 194 | 109 |
| S2 | kâr faktörü veya düşüş zayıf | 49 | 60 |
| S3 | yüksek maliyette zarar | 0 | 60 |
| S4 | plato yok (komşu ayarlar zararda) | 11 | 49 |
| S5 | 1 bar gecikmeye dayanıksız | 9 | 40 |
| S6 | yılların çoğunda kârlı değil | 4 | 36 |
| S7 | istatistiksel güven düşük (PSR) | 4 | 32 |

## Geçenler (36)

| Tier | Aşama | Coin | Kural | Ayar | Varyant | 3y | 5y | Tüm | Sharpe | 1x DD | PF | DSR |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| B | 2 | SAND/USDT | macd_cross | `cfg=(8, 21, 5),zero_filter=False` | çıkış=stop_atr=2.0,max_hold=10 | +206% | veri yok | +2256% | 1.374 | -33% | 2.7 | 0.169 |
| B | 2 | MINA/USDT | linreg_slope | `n=20,th=0.001` | çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +514% | veri yok | +626% | 1.305 | -33% | 3.581 | 0.155 |
| B | 2 | DOT/USDT | smc_liquidity_sweep | `k=3` | filtre=trend_sma200 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +153% | veri yok | +305% | 1.293 | -31% | 2.74 | 0.131 |
| B | 1 | DOT/USDT | smc_liquidity_sweep | `k=3` | çıkış=stop_atr=2.0,trail_atr=3.0 | +220% | veri yok | +413% | 1.157 | -32% | 2.1 | 0.075 |
| B | 2 | IMX/USDT | cci_breakout | `n=14,level=100` | filtre=htf_week_sma10 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +253% | veri yok | +853% | 1.128 | -36% | 3.515 | 0.068 |
| B | 2 | IMX/USDT | triple_ma | `set=(5, 20, 50),kind=sma` | filtre=htf_week_sma10 · çıkış=stop_atr=2.0,max_hold=10 | +158% | veri yok | +510% | 1.102 | -29% | 5.603 | 0.063 |
| B | 2 | ARB/USDT | smc_fvg | `max_age=20,min_gap_atr=0.0` | filtre=htf_week_sma10 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +130% | veri yok | +229% | 0.998 | -26% | 2.162 | 0.061 |
| B | 2 | UNI/USDT | williams_reversal | `n=7,lo=-90` | filtre=trend_sma200 · çıkış=trail_atr=3.0 | +120% | +267% | +267% | 1.106 | -25% | 3.902 | 0.058 |
| B | 1 | SAND/USDT | macd_cross | `cfg=(8, 21, 5),zero_filter=False` | çıkış=stop_atr=2.0,trail_atr=3.0 | +159% | veri yok | +1113% | 1.094 | -37% | 2.498 | 0.057 |
| B | 2 | APT/USDT | cci_reversal | `n=14,lo=-100` | filtre=low_vol · çıkış=trail_atr=3.0 | +140% | veri yok | +220% | 1.071 | -36% | 2.776 | 0.056 |
| B | 2 | ARB/USDT | price_ma | `kind=sma,n=20` | çıkış=stop_atr=2.0,max_hold=10 | +230% | veri yok | +241% | 0.961 | -29% | 1.863 | 0.055 |
| B | 2 | ARB/USDT | rsi_reversal | `n=2,lo=10,exit=50` | filtre=htf_week_sma10 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +48% | veri yok | +61% | 0.95 | -14% | 3.543 | 0.048 |
| B | 2 | SAND/USDT | elder_impulse | `ema_n=13,macd_cfg=(12, 26, 9)` | çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +171% | veri yok | +737% | 1.044 | -38% | 2.111 | 0.046 |
| B | 2 | ADA/USDT | stochrsi_reversal | `n=9,lo=10` | filtre=low_vol · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +86% | veri yok | +140% | 0.98 | -34% | 2.674 | 0.04 |
| B | 2 | ARB/USDT | elder_impulse | `ema_n=13,macd_cfg=(12, 26, 9)` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=engulfing(≤5 bar) | +207% | veri yok | +224% | 0.883 | -36% | 2.564 | 0.04 |
| B | 2 | DOT/USDT | stoch_reversal | `k=9,d=3,smooth=1,lo=25` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=pivot_bounce(≤5 bar) | +99% | veri yok | +312% | 1.009 | -36% | 2.009 | 0.038 |
| B | 2 | OP/USDT | smc_liquidity_sweep | `k=3` | filtre=adx20 · çıkış=trail_atr=3.0 | +69% | veri yok | +218% | 0.928 | -40% | 2.169 | 0.036 |
| B | 2 | ARB/USDT | obv_trend | `n=50,price_n=50` | filtre=adx20 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +128% | veri yok | +127% | 0.864 | -39% | 2.17 | 0.035 |
| B | 2 | DOGE/USDT | smc_fvg | `max_age=20,min_gap_atr=0.0` | filtre=adx20 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +169% | +406% | +571% | 1.009 | -38% | 2.022 | 0.031 |
| B | 2 | ARB/USDT | stochrsi_reversal | `n=9,lo=5` | filtre=htf_week_sma10 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +117% | veri yok | +121% | 0.812 | -34% | 1.971 | 0.03 |
| B | 2 | AVAX/USDT | smc_fvg | `max_age=10,min_gap_atr=0.5` | çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +239% | veri yok | +319% | 0.967 | -35% | 2.916 | 0.028 |
| B | 2 | AVAX/USDT | smc_liquidity_sweep | `k=3` | filtre=adx20 · çıkış=stop_atr=2.0,tp_r=3.0 | +189% | veri yok | +258% | 0.948 | -35% | 2.336 | 0.023 |
| B | 2 | DOT/USDT | stochrsi_reversal | `n=9,lo=5` | filtre=htf_week_sma10 · çıkış=trail_atr=3.0 | +59% | veri yok | +203% | 0.9 | -32% | 2.588 | 0.02 |
| B | 2 | ARB/USDT | elder_impulse | `ema_n=13,macd_cfg=(12, 26, 9)` | filtre=htf_week_sma10 · çıkış=stop_atr=2.0,max_hold=10 | +125% | veri yok | +138% | 0.718 | -33% | 1.662 | 0.02 |
| B | 2 | SAND/USDT | mfi_reversal | `n=10,lo=30` | filtre=trend_sma200 · çıkış=stop_atr=2.0,tp_r=3.0 | +160% | veri yok | +278% | 0.93 | -29% | 2.483 | 0.017 |
| B | 2 | SAND/USDT | triple_ma | `set=(5, 20, 50),kind=sma` | çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +41% | veri yok | +298% | 0.837 | -39% | 2.35 | 0.016 |
| B | 1 | AXS/USDT | smc_ote | `k=3,fib_lo=0.618` | çıkış=stop_atr=2.0,trail_atr=3.0 | +29% | +184% | +184% | 0.822 | -39% | 1.859 | 0.015 |
| B | 2 | DOT/USDT | smc_ote | `k=3,fib_lo=0.618` | çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +59% | veri yok | +127% | 0.766 | -28% | 1.944 | 0.01 |
| B | 2 | DOT/USDT | rsi_reversal | `n=3,lo=35,exit=70` | filtre=htf_week_sma10 · çıkış=trail_atr=3.0 | +77% | veri yok | +157% | 0.752 | -26% | 1.942 | 0.01 |
| B | 2 | SAND/USDT | engulfing | `trend_n=0` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_fvg(≤3 bar) | +152% | veri yok | +245% | 0.779 | -40% | 2.704 | 0.009 |
| B | 2 | ATOM/USDT | smc_fvg | `max_age=20,min_gap_atr=0.5` | filtre=adx20 · çıkış=stop_atr=2.0,trail_atr=3.0 | +49% | veri yok | +219% | 0.747 | -33% | 3.45 | 0.008 |
| B | 2 | ADA/USDT | bollinger_reversion | `n=10,k=1.5` | filtre=trend_sma200 · çıkış=trail_atr=3.0 | +52% | veri yok | +64% | 0.658 | -26% | 1.87 | 0.008 |
| B | 2 | AAVE/USDT | smc_ote | `k=5,fib_lo=0.5` | çıkış=stop_atr=2.0,max_hold=10 | +108% | +137% | +176% | 0.769 | -33% | 1.848 | 0.007 |
| B | 1 | DOT/USDT | smc_ote | `k=3,fib_lo=0.618` | çıkış=stop_atr=2.0,trail_atr=3.0 | +42% | veri yok | +108% | 0.689 | -28% | 1.871 | 0.007 |
| B | 2 | DOT/USDT | rsi_midline | `n=14,level=50` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=macd_cross(≤3 bar) | +61% | veri yok | +163% | 0.688 | -36% | 3.033 | 0.005 |
| B | 2 | AVAX/USDT | smc_ote | `k=3,fib_lo=0.5` | çıkış=stop_atr=2.0,tp_r=3.0 | +150% | veri yok | +107% | 0.588 | -38% | 1.564 | 0.004 |

## Coin coin özet (ajan günlüğü)

- **AAVE/USDT**: 67 aday denendi, 1 kaldı. En iyi aday smc_ote (`k=5,fib_lo=0.5`, çıkış=stop_atr=2.0,max_hold=10): OK — tüm adımlar geçti.
- **ADA/USDT**: 74 aday denendi, 2 kaldı. En iyi aday stochrsi_reversal (`n=9,lo=10`, filtre=low_vol · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0): OK — tüm adımlar geçti.
- **ALGO/USDT**: elendi (S0: 1.8 yıl veri var, en az 3.0 yıl gerekli).
- **APT/USDT**: 84 aday denendi, 1 kaldı. En iyi aday cci_reversal (`n=14,lo=-100`, filtre=low_vol · çıkış=trail_atr=3.0): OK — tüm adımlar geçti.
- **ARB/USDT**: 93 aday denendi, 7 kaldı. En iyi aday smc_fvg (`max_age=20,min_gap_atr=0.0`, filtre=htf_week_sma10 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0): OK — tüm adımlar geçti.
- **ATOM/USDT**: 73 aday denendi, 1 kaldı. En iyi aday smc_fvg (`max_age=20,min_gap_atr=0.5`, filtre=adx20 · çıkış=stop_atr=2.0,trail_atr=3.0): OK — tüm adımlar geçti.
- **AVAX/USDT**: 74 aday denendi, 3 kaldı. En iyi aday smc_fvg (`max_age=10,min_gap_atr=0.5`, çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0): OK — tüm adımlar geçti.
- **AXS/USDT**: 71 aday denendi, 1 kaldı. En iyi aday smc_ote (`k=3,fib_lo=0.618`, çıkış=stop_atr=2.0,trail_atr=3.0): OK — tüm adımlar geçti.
- **BCH/USDT**: 68 aday denendi, 0 kaldı. En iyi aday williams_reversal (`n=14,lo=-95`, çıkış=stop_atr=2.0,trail_atr=3.0): S5 — 1 bar geç girişte Sharpe'ın %26'i kalıyor.
- **BNB/USDT**: 64 aday denendi, 0 kaldı. En iyi aday williams_reversal (`n=7,lo=-95`, çıkış=stop_atr=2.0,trail_atr=3.0): S7 — PSR 0.781.
- **BTC/USDT**: 62 aday denendi, 0 kaldı. En iyi aday bb_squeeze (`n=20,q=0.2,look=126`, çıkış=stop_atr=2.0,trail_atr=3.0): S1 — 3y -16%, 5y +3%, full +44%; 26 işlem (zararlı: 3y).
- **CRV/USDT**: 65 aday denendi, 0 kaldı. En iyi aday smc_ote (`k=3,fib_lo=0.5`, filtre=htf_week_sma10 · çıkış=stop_atr=2.0,trail_atr=3.0): S6 — yılların %33'i kârlı.
- **DOGE/USDT**: 66 aday denendi, 1 kaldı. En iyi aday smc_fvg (`max_age=20,min_gap_atr=0.0`, filtre=adx20 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0): OK — tüm adımlar geçti.
- **DOT/USDT**: 92 aday denendi, 8 kaldı. En iyi aday smc_liquidity_sweep (`k=3`, filtre=trend_sma200 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0): OK — tüm adımlar geçti.
- **ETC/USDT**: 72 aday denendi, 0 kaldı. En iyi aday cci_reversal (`n=20,lo=-100`, çıkış=stop_atr=2.0,trail_atr=3.0 · onay=pivot_bounce(≤5 bar)): S4 — komşu ayarların %0'i kârlı.
- **ETH/USDT**: 66 aday denendi, 0 kaldı. En iyi aday smc_ote (`k=8,fib_lo=0.618`, çıkış=stop_atr=2.0,trail_atr=3.0): S2 — PF 1.462, 1x maks. düşüş -45%.
- **FIL/USDT**: 67 aday denendi, 0 kaldı. En iyi aday williams_reversal (`n=7,lo=-80`, filtre=trend_sma200 · çıkış=stop_atr=2.0,be_r=1.0): S2 — PF 1.857, 1x maks. düşüş -46%.
- **IMX/USDT**: 84 aday denendi, 2 kaldı. En iyi aday cci_breakout (`n=14,level=100`, filtre=htf_week_sma10 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0): OK — tüm adımlar geçti.
- **INJ/USDT**: elendi (S0: 2.9 yıl veri var, en az 3.0 yıl gerekli).
- **LINK/USDT**: 67 aday denendi, 0 kaldı. En iyi aday ultimate_reversal (`a=5,lo=35`, filtre=trend_sma200 · çıkış=stop_atr=2.0,tp_r=3.0): S4 — komşu ayarların %0'i kârlı.
- **LTC/USDT**: 62 aday denendi, 0 kaldı. En iyi aday rsi_reversal (`n=7,lo=10,exit=50`, çıkış=stop_atr=2.0,trail_atr=3.0): S1 — 3y +13%, 5y +13%, full +29%; 4 işlem.
- **MANA/USDT**: 69 aday denendi, 0 kaldı. En iyi aday rsi_reversal (`n=2,lo=10,exit=50`, filtre=low_vol · çıkış=trail_atr=3.0): S5 — 1 bar geç girişte Sharpe'ın %0'i kalıyor.
- **MINA/USDT**: 88 aday denendi, 1 kaldı. En iyi aday linreg_slope (`n=20,th=0.001`, çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0): OK — tüm adımlar geçti.
- **NEAR/USDT**: 66 aday denendi, 0 kaldı. En iyi aday rsi_reversal (`n=3,lo=35,exit=50`, filtre=low_vol · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0): S5 — 1 bar geç girişte Sharpe'ın %28'i kalıyor.
- **OP/USDT**: 74 aday denendi, 1 kaldı. En iyi aday smc_liquidity_sweep (`k=3`, filtre=adx20 · çıkış=trail_atr=3.0): OK — tüm adımlar geçti.
- **PYTH/USDT**: elendi (S0: 2.9 yıl veri var, en az 3.0 yıl gerekli).
- **SAND/USDT**: 89 aday denendi, 6 kaldı. En iyi aday macd_cross (`cfg=(8, 21, 5),zero_filter=False`, çıkış=stop_atr=2.0,max_hold=10): OK — tüm adımlar geçti.
- **SNX/USDT**: 74 aday denendi, 0 kaldı. En iyi aday down_days (`n=4,hold_exit=1`, filtre=adx20 · çıkış=signal_only): S5 — 1 bar geç girişte Sharpe'ın %4'i kalıyor.
- **SOL/USDT**: 62 aday denendi, 0 kaldı. En iyi aday smc_liquidity_sweep (`k=3`, çıkış=stop_atr=2.0,trail_atr=3.0): S1 — 3y -18%, 5y +99%, full +141%; 61 işlem (zararlı: 3y).
- **SUI/USDT**: 64 aday denendi, 0 kaldı. En iyi aday stoch_reversal (`k=5,d=3,smooth=3,lo=10`, çıkış=stop_atr=2.0,trail_atr=3.0): S2 — PF 1.418, 1x maks. düşüş -67%.
- **THETA/USDT**: 62 aday denendi, 0 kaldı. En iyi aday triple_ma (`set=(20, 50, 100),kind=sma`, çıkış=stop_atr=2.0,trail_atr=3.0): S1 — 3y +52%, 5y +102%, full +139%; 21 işlem.
- **TRX/USDT**: 66 aday denendi, 0 kaldı. En iyi aday rsi_divergence (`n=14,k=3,exit_level=50`, çıkış=stop_atr=2.0,trail_atr=3.0): S4 — komşu ayarların %0'i kârlı.
- **UNI/USDT**: 68 aday denendi, 1 kaldı. En iyi aday williams_reversal (`n=7,lo=-90`, filtre=trend_sma200 · çıkış=trail_atr=3.0): OK — tüm adımlar geçti.
- **XLM/USDT**: 72 aday denendi, 0 kaldı. En iyi aday smc_liquidity_sweep (`k=3`, çıkış=stop_atr=2.0,trail_atr=3.0): S6 — yılların %50'i kârlı.
- **XRP/USDT**: 62 aday denendi, 0 kaldı. En iyi aday roc_breakout (`n=252,th=5`, çıkış=stop_atr=2.0,trail_atr=3.0): S1 — 3y +8%, 5y +25%, full +22%; 29 işlem.

## Zayıf yönler (dürüst liste)

- 31240 deneme yapıldı. Bu kadar çok denemede şans eseri iyi görünen strateji çıkar. DSR bunu düzeltir; tier A sadece DSR ≥ eşik olanlardır.
- Seçim ve test aynı geçmiş veride yapıldı. Gerçek test arenadaki ileri (paper) kayıttır.
- Survivorship: liste bugünün coinlerinden oluşur. Borsadan silinen coinler yok, bu sonucu iyimser yapar.
- Funding sabit yıllık oranla, likidasyon işlem bazında yaklaşık modellenir.
- Tek borsa verisi (Bitget, yoksa OKX/KuCoin). Emir defteri ve piyasa etkisi modellenmez.

## Arena

Arena: 32 aktif (eleme geçen), 68 kontrol (yakın aday, switcher kullanmaz), 100 yeni üye, 0 kontrolden aktife. Üst sınır 100.

## Switcher backtest kapısı

Geçti: **False** — kontroller: `{"beats_equal_weight_all_windows": false, "positive_at_cost_stress": true, "max_dd_ok": true}`

Pencereler: `{"3y": {"sharpe": 0.659, "ew_sharpe": 1.807}, "5y": {"sharpe": 0.392, "ew_sharpe": 1.85}, "full": {"sharpe": 0.305, "ew_sharpe": 1.457}}`
