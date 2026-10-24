# Eleme motoru — crypto_alts 1d

Veri: 2018-07-24 → 2026-10-17. Coin: 32 uygun (toplam 35). Denenen varyant: 553 × coin = **36257 deneme**.
Her (coin, kural) için tek en iyi nokta değil, **en sağlam bölgenin merkezi** seçildi. Bu bir aday listesidir, karar değildir. Karar sadece doğrulama kapısında verilir.

## Huni

| Adım | Ne kontrol edilir | Elenen | Kalan |
|---|---|---|---|
| S0 | veri yetersiz | 186 | 1984 |
| S1 | her dönemde kârlı değil / az işlem | 1753 | 231 |
| S2 | kâr faktörü veya düşüş zayıf | 212 | 19 |
| S3 | yüksek maliyette zarar | 1 | 18 |
| S4 | plato yok (komşu ayarlar zararda) | 7 | 11 |
| S5 | 1 bar gecikmeye dayanıksız | 6 | 5 |
| S6 | yılların çoğunda kârlı değil | 1 | 4 |
| S7 | istatistiksel güven düşük (PSR) | 3 | 1 |

## 2. aşama: filtre × çıkış × kombo (sadece S1'i geçen adaylarda)

231 aday → 18561 ek deneme (DSR'a eklendi). Her aday için en sağlam filtre/çıkış hücresi ve en sağlam kombo seçildi; kombo sadece kuralı tek başına geçerse aday olur. Seçilenler aynı S1–S7 adımlarından geçti.

| Adım | Ne kontrol edilir | Elenen | Kalan |
|---|---|---|---|
| S0 | veri yetersiz | 0 | 400 |
| S1 | her dönemde kârlı değil / az işlem | 217 | 183 |
| S2 | kâr faktörü veya düşüş zayıf | 133 | 50 |
| S3 | yüksek maliyette zarar | 0 | 50 |
| S4 | plato yok (komşu ayarlar zararda) | 16 | 34 |
| S5 | 1 bar gecikmeye dayanıksız | 6 | 28 |
| S6 | yılların çoğunda kârlı değil | 2 | 26 |
| S7 | istatistiksel güven düşük (PSR) | 2 | 24 |

## Geçenler (25)

| Tier | Aşama | Coin | Kural | Ayar | Varyant | 3y | 5y | Tüm | Sharpe | 1x DD | PF | DSR |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| B | 2 | ARB/USDT | atr_breakout | `n=20,k=1.0` | filtre=low_vol · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +657% | veri yok | +791% | 1.6 | -24% | 4.979 | 0.322 |
| B | 2 | SOL/USDT | cci_breakout | `n=40,level=150` | filtre=regime_bench200 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +250% | +667% | +1553% | 1.45 | -32% | 5.867 | 0.179 |
| B | 2 | XLM/USDT | stoch_reversal | `k=9,d=5,smooth=3,lo=20` | filtre=low_vol · çıkış=stop_atr=2.0,be_r=1.0 | +240% | veri yok | +240% | 1.151 | -27% | 2.28 | 0.096 |
| B | 2 | MINA/USDT | rsi_midline | `n=28,level=50` | filtre=low_vol · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +258% | veri yok | +362% | 1.22 | -33% | 2.882 | 0.095 |
| B | 2 | ARB/USDT | engulfing | `trend_n=200` | filtre=adx20 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +354% | veri yok | +371% | 1.104 | -36% | 2.097 | 0.079 |
| B | 2 | SOL/USDT | donchian_breakout | `entry=40,exit=10` | filtre=regime_bench200 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +133% | +334% | +836% | 1.187 | -39% | 4.057 | 0.058 |
| B | 2 | BNB/USDT | price_ma | `kind=sma,n=50` | filtre=htf_week_sma10 · çıkış=signal_only | +215% | veri yok | +209% | 0.978 | -28% | 4.778 | 0.045 |
| B | 2 | ARB/USDT | rsi_reversal | `n=2,lo=10,exit=50` | filtre=regime_bench200 · çıkış=signal_only | +129% | veri yok | +129% | 0.96 | -30% | 2.203 | 0.044 |
| B | 2 | XLM/USDT | rsi_reversal | `n=9,lo=30,exit=50` | filtre=adx20 · çıkış=trail_atr=3.0 | +108% | veri yok | +95% | 0.852 | -34% | 1.961 | 0.04 |
| B | 2 | ARB/USDT | rsi_midline | `n=21,level=50` | filtre=regime_bench200 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +270% | veri yok | +176% | 0.895 | -33% | 2.042 | 0.036 |
| B | 2 | IMX/USDT | smc_ote | `k=3,fib_lo=0.5` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_fvg(≤3 bar) | +202% | veri yok | +281% | 1.028 | -40% | 2.817 | 0.026 |
| B | 2 | APT/USDT | force_index | `n=2` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_order_block(≤3 bar) | +89% | veri yok | +89% | 0.828 | -34% | 2.331 | 0.015 |
| B | 2 | SAND/USDT | mfi_reversal | `n=10,lo=30` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_liquidity_sweep(≤3 bar) | +63% | veri yok | +205% | 0.864 | -37% | 2.101 | 0.013 |
| B | 2 | AXS/USDT | williams_reversal | `n=7,lo=-80` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_order_block(≤3 bar) | +124% | +292% | +292% | 0.848 | -35% | 2.103 | 0.013 |
| B | 2 | CRV/USDT | force_index | `n=2` | filtre=regime_bench200 · çıkış=signal_only | +79% | +209% | +311% | 0.874 | -40% | 1.959 | 0.011 |
| B | 2 | ADA/USDT | trix_cross | `n=21,signal=9` | filtre=low_vol · çıkış=stop_atr=2.0,max_hold=10 | +102% | veri yok | +133% | 0.752 | -32% | 2.101 | 0.008 |
| B | 2 | LINK/USDT | stoch_reversal | `k=5,d=3,smooth=3,lo=10` | filtre=trend_sma200 · çıkış=stop_atr=2.0,trail_atr=3.0 | +107% | +170% | +170% | 0.774 | -31% | 2.043 | 0.006 |
| B | 2 | ETH/USDT | ma_cross | `kind=sma,pair=(20, 50)` | filtre=low_vol · çıkış=trail_atr=3.0 | +76% | +194% | +730% | 0.935 | -38% | 4.075 | 0.005 |
| B | 2 | AXS/USDT | stoch_reversal | `k=5,d=3,smooth=1,lo=10` | filtre=adx20 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +63% | +206% | +206% | 0.691 | -38% | 1.601 | 0.005 |
| B | 2 | OP/USDT | force_index | `n=2` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_fvg(≤5 bar) | +76% | veri yok | +122% | 0.669 | -31% | 1.818 | 0.005 |
| B | 2 | ETC/USDT | ma_cross | `kind=sma,pair=(10, 50)` | filtre=low_vol · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +51% | +99% | +651% | 0.928 | -27% | 2.699 | 0.004 |
| B | 2 | FIL/USDT | stoch_reversal | `k=5,d=3,smooth=3,lo=10` | filtre=low_vol · çıkış=stop_atr=2.0,trail_atr=3.0 | +76% | +214% | +214% | 0.726 | -38% | 1.874 | 0.004 |
| B | 2 | LTC/USDT | hurst_switch | `n=100,fast=20,rsi_n=2` | filtre=htf_week_sma10 · çıkış=signal_only | +81% | +119% | +318% | 0.803 | -24% | 3.406 | 0.001 |
| B | 2 | TRX/USDT | hurst_switch | `n=100,fast=20,rsi_n=2` | filtre=regime_bench200 · çıkış=trail_atr=3.0 | +76% | +92% | +134% | 0.632 | -35% | 2.14 | 0.001 |
| B | 1 | BTC/USDT | atr_breakout | `n=10,k=2.0` | çıkış=stop_atr=2.0,trail_atr=3.0 | +45% | +65% | +230% | 0.602 | -31% | 2.694 | 0.0 |

## Coin coin özet (ajan günlüğü)

- **AAVE/USDT**: 68 aday denendi, 0 kaldı. En iyi aday hammer_star (`lookback_low=10`, filtre=adx20 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0): S5 — 1 bar geç girişte Sharpe'ın %31'i kalıyor.
- **ADA/USDT**: 88 aday denendi, 1 kaldı. En iyi aday trix_cross (`n=21,signal=9`, filtre=low_vol · çıkış=stop_atr=2.0,max_hold=10): OK — tüm adımlar geçti.
- **ALGO/USDT**: elendi (S0: 1.8 yıl veri var, en az 3.0 yıl gerekli).
- **APT/USDT**: 74 aday denendi, 1 kaldı. En iyi aday force_index (`n=2`, çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_order_block(≤3 bar)): OK — tüm adımlar geçti.
- **ARB/USDT**: 92 aday denendi, 4 kaldı. En iyi aday atr_breakout (`n=20,k=1.0`, filtre=low_vol · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0): OK — tüm adımlar geçti.
- **ATOM/USDT**: 68 aday denendi, 0 kaldı. En iyi aday hurst_switch (`n=200,fast=20,rsi_n=2`, çıkış=stop_atr=2.0,trail_atr=3.0 · onay=pivot_bounce(≤3 bar)): S5 — 1 bar geç girişte Sharpe'ın %37'i kalıyor.
- **AVAX/USDT**: 80 aday denendi, 0 kaldı. En iyi aday hammer_star (`lookback_low=10`, çıkış=stop_atr=2.0,trail_atr=3.0): S5 — 1 bar geç girişte Sharpe'ın %3'i kalıyor.
- **AXS/USDT**: 68 aday denendi, 2 kaldı. En iyi aday williams_reversal (`n=7,lo=-80`, çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_order_block(≤3 bar)): OK — tüm adımlar geçti.
- **BCH/USDT**: 72 aday denendi, 0 kaldı. En iyi aday hurst_switch (`n=100,fast=20,rsi_n=2`, çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0): S2 — PF 1.952, 1x maks. düşüş -57%.
- **BNB/USDT**: 77 aday denendi, 1 kaldı. En iyi aday price_ma (`kind=sma,n=50`, filtre=htf_week_sma10 · çıkış=signal_only): OK — tüm adımlar geçti.
- **BTC/USDT**: 74 aday denendi, 1 kaldı. En iyi aday atr_breakout (`n=10,k=2.0`, çıkış=stop_atr=2.0,trail_atr=3.0): OK — tüm adımlar geçti.
- **CRV/USDT**: 72 aday denendi, 1 kaldı. En iyi aday force_index (`n=2`, filtre=regime_bench200 · çıkış=signal_only): OK — tüm adımlar geçti.
- **DOGE/USDT**: 66 aday denendi, 0 kaldı. En iyi aday rsi_divergence (`n=14,k=3,exit_level=50`, çıkış=stop_atr=2.0,trail_atr=3.0): S5 — 1 bar geç girişte Sharpe'ın %0'i kalıyor.
- **DOT/USDT**: 75 aday denendi, 0 kaldı. En iyi aday williams_reversal (`n=7,lo=-90`, filtre=htf_week_sma10 · çıkış=trail_atr=3.0): S4 — komşu ayarların %33'i kârlı.
- **ETC/USDT**: 69 aday denendi, 1 kaldı. En iyi aday ma_cross (`kind=sma,pair=(10, 50)`, filtre=low_vol · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0): OK — tüm adımlar geçti.
- **ETH/USDT**: 87 aday denendi, 1 kaldı. En iyi aday ma_cross (`kind=sma,pair=(20, 50)`, filtre=low_vol · çıkış=trail_atr=3.0): OK — tüm adımlar geçti.
- **FIL/USDT**: 68 aday denendi, 1 kaldı. En iyi aday stoch_reversal (`k=5,d=3,smooth=3,lo=10`, filtre=low_vol · çıkış=stop_atr=2.0,trail_atr=3.0): OK — tüm adımlar geçti.
- **IMX/USDT**: 74 aday denendi, 1 kaldı. En iyi aday smc_ote (`k=3,fib_lo=0.5`, çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_fvg(≤3 bar)): OK — tüm adımlar geçti.
- **INJ/USDT**: elendi (S0: 2.9 yıl veri var, en az 3.0 yıl gerekli).
- **LINK/USDT**: 68 aday denendi, 1 kaldı. En iyi aday stoch_reversal (`k=5,d=3,smooth=3,lo=10`, filtre=trend_sma200 · çıkış=stop_atr=2.0,trail_atr=3.0): OK — tüm adımlar geçti.
- **LTC/USDT**: 67 aday denendi, 1 kaldı. En iyi aday hurst_switch (`n=100,fast=20,rsi_n=2`, filtre=htf_week_sma10 · çıkış=signal_only): OK — tüm adımlar geçti.
- **MANA/USDT**: 64 aday denendi, 0 kaldı. En iyi aday triple_ma (`set=(5, 20, 50),kind=sma`, filtre=regime_bench200 · çıkış=stop_atr=2.0,max_hold=10): S2 — PF 2.552, 1x maks. düşüş -60%.
- **MINA/USDT**: 95 aday denendi, 1 kaldı. En iyi aday rsi_midline (`n=28,level=50`, filtre=low_vol · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0): OK — tüm adımlar geçti.
- **NEAR/USDT**: 93 aday denendi, 0 kaldı. En iyi aday vwap_cross (`n=50`, filtre=regime_bench200 · çıkış=stop_atr=2.0,max_hold=10): S5 — 1 bar geç girişte Sharpe'ın %35'i kalıyor.
- **OP/USDT**: 73 aday denendi, 1 kaldı. En iyi aday force_index (`n=2`, çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_fvg(≤5 bar)): OK — tüm adımlar geçti.
- **PYTH/USDT**: elendi (S0: 2.9 yıl veri var, en az 3.0 yıl gerekli).
- **SAND/USDT**: 69 aday denendi, 1 kaldı. En iyi aday mfi_reversal (`n=10,lo=30`, çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_liquidity_sweep(≤3 bar)): OK — tüm adımlar geçti.
- **SNX/USDT**: 67 aday denendi, 0 kaldı. En iyi aday down_days (`n=4,hold_exit=1`, filtre=adx20 · çıkış=signal_only): S4 — komşu ayarların %33'i kârlı.
- **SOL/USDT**: 77 aday denendi, 2 kaldı. En iyi aday cci_breakout (`n=40,level=150`, filtre=regime_bench200 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0): OK — tüm adımlar geçti.
- **SUI/USDT**: 81 aday denendi, 0 kaldı. En iyi aday price_ma (`kind=sma,n=20`, filtre=low_vol · çıkış=stop_atr=2.0,max_hold=10): S5 — 1 bar geç girişte Sharpe'ın %20'i kalıyor.
- **THETA/USDT**: 65 aday denendi, 0 kaldı. En iyi aday ichimoku_cloud (`cfg=(20, 60, 120)`, çıkış=stop_atr=2.0,trail_atr=3.0): S2 — PF 2.415, 1x maks. düşüş -81%.
- **TRX/USDT**: 68 aday denendi, 1 kaldı. En iyi aday hurst_switch (`n=100,fast=20,rsi_n=2`, filtre=regime_bench200 · çıkış=trail_atr=3.0): OK — tüm adımlar geçti.
- **UNI/USDT**: 75 aday denendi, 0 kaldı. En iyi aday hammer_star (`lookback_low=10`, çıkış=stop_atr=2.0,trail_atr=3.0): S7 — PSR 0.752.
- **XLM/USDT**: 86 aday denendi, 2 kaldı. En iyi aday stoch_reversal (`k=9,d=5,smooth=3,lo=20`, filtre=low_vol · çıkış=stop_atr=2.0,be_r=1.0): OK — tüm adımlar geçti.
- **XRP/USDT**: 64 aday denendi, 0 kaldı. En iyi aday macd_cross (`cfg=(5, 35, 5),zero_filter=True`, filtre=low_vol · çıkış=signal_only): S2 — PF 4.202, 1x maks. düşüş -47%.

## Zayıf yönler (dürüst liste)

- 36257 deneme yapıldı. Bu kadar çok denemede şans eseri iyi görünen strateji çıkar. DSR bunu düzeltir; tier A sadece DSR ≥ eşik olanlardır.
- Seçim ve test aynı geçmiş veride yapıldı. Gerçek test arenadaki ileri (paper) kayıttır.
- Survivorship: liste bugünün coinlerinden oluşur. Borsadan silinen coinler yok, bu sonucu iyimser yapar.
- Funding sabit yıllık oranla, likidasyon işlem bazında yaklaşık modellenir.
- Tek borsa verisi (Bitget, yoksa OKX/KuCoin). Emir defteri ve piyasa etkisi modellenmez.

## Arena

Arena: 32 aktif (eleme geçen), 68 kontrol (yakın aday, switcher kullanmaz), 7 yeni üye, 1 kontrolden aktife. Üst sınır 100.

## Switcher backtest kapısı

Geçti: **False** — kontroller: `{"beats_equal_weight_all_windows": false, "positive_at_cost_stress": true, "max_dd_ok": true}`

Pencereler: `{"3y": {"sharpe": 0.79, "ew_sharpe": 3.605}, "5y": {"sharpe": 0.892, "ew_sharpe": 3.077}, "full": {"sharpe": 1.144, "ew_sharpe": 2.583}}`
