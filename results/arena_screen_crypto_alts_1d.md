# Eleme motoru — crypto_alts 1d

Veri: 2018-01-11 → 2026-10-16. Coin: 33 uygun (toplam 35). Denenen varyant: 518 × coin = **28115 deneme**.
Her (coin, kural) için tek en iyi nokta değil, **en sağlam bölgenin merkezi** seçildi. Bu bir aday listesidir, karar değildir. Karar sadece doğrulama kapısında verilir.

## Huni

| Adım | Ne kontrol edilir | Elenen | Kalan |
|---|---|---|---|
| S0 | veri yetersiz | 106 | 1749 |
| S1 | her dönemde kârlı değil / az işlem | 1553 | 196 |
| S2 | kâr faktörü veya düşüş zayıf | 182 | 14 |
| S3 | yüksek maliyette zarar | 1 | 13 |
| S4 | plato yok (komşu ayarlar zararda) | 6 | 7 |
| S5 | 1 bar gecikmeye dayanıksız | 2 | 5 |
| S6 | yılların çoğunda kârlı değil | 2 | 3 |
| S7 | istatistiksel güven düşük (PSR) | 2 | 1 |

## 2. aşama: filtre × çıkış × kombo (sadece S1'i geçen adaylarda)

196 aday → 11021 ek deneme (DSR'a eklendi). Her aday için en sağlam filtre/çıkış hücresi ve en sağlam kombo seçildi; kombo sadece kuralı tek başına geçerse aday olur. Seçilenler aynı S1–S7 adımlarından geçti.

| Adım | Ne kontrol edilir | Elenen | Kalan |
|---|---|---|---|
| S0 | veri yetersiz | 0 | 278 |
| S1 | her dönemde kârlı değil / az işlem | 140 | 138 |
| S2 | kâr faktörü veya düşüş zayıf | 103 | 35 |
| S3 | yüksek maliyette zarar | 0 | 35 |
| S4 | plato yok (komşu ayarlar zararda) | 9 | 26 |
| S5 | 1 bar gecikmeye dayanıksız | 3 | 23 |
| S6 | yılların çoğunda kârlı değil | 1 | 22 |
| S7 | istatistiksel güven düşük (PSR) | 0 | 22 |

## Geçenler (23)

| Tier | Aşama | Coin | Kural | Ayar | Varyant | 3y | 5y | Tüm | Sharpe | 1x DD | PF | DSR |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| B | 2 | SOL/USDT | cci_breakout | `n=40,level=150` | filtre=regime_bench200 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +250% | +667% | +1553% | 1.45 | -32% | 5.867 | 0.167 |
| B | 2 | APT/USDT | stoch_reversal | `k=9,d=5,smooth=3,lo=10` | filtre=low_vol · çıkış=stop_atr=2.0,trail_atr=3.0 | +614% | veri yok | +514% | 1.404 | -31% | 4.021 | 0.164 |
| B | 2 | XLM/USDT | stoch_reversal | `k=9,d=5,smooth=3,lo=20` | filtre=low_vol · çıkış=stop_atr=2.0,be_r=1.0 | +240% | veri yok | +240% | 1.152 | -27% | 2.28 | 0.09 |
| B | 2 | MINA/USDT | rsi_midline | `n=28,level=50` | filtre=low_vol · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +256% | veri yok | +362% | 1.22 | -33% | 2.882 | 0.088 |
| B | 2 | ARB/USDT | engulfing | `trend_n=200` | filtre=adx20 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +401% | veri yok | +397% | 1.136 | -36% | 2.097 | 0.082 |
| B | 2 | SOL/USDT | donchian_breakout | `entry=40,exit=10` | filtre=regime_bench200 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +133% | +334% | +836% | 1.187 | -39% | 4.057 | 0.053 |
| B | 2 | BNB/USDT | price_ma | `kind=sma,n=50` | filtre=htf_week_sma10 · çıkış=signal_only | +214% | veri yok | +209% | 0.978 | -28% | 4.778 | 0.042 |
| B | 2 | ARB/USDT | rsi_reversal | `n=2,lo=10,exit=50` | filtre=regime_bench200 · çıkış=signal_only | +129% | veri yok | +129% | 0.96 | -30% | 2.203 | 0.04 |
| B | 2 | ARB/USDT | rsi_midline | `n=21,level=50` | filtre=regime_bench200 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +299% | veri yok | +192% | 0.934 | -33% | 2.042 | 0.039 |
| B | 2 | XLM/USDT | rsi_reversal | `n=9,lo=30,exit=50` | filtre=adx20 · çıkış=trail_atr=3.0 | +99% | veri yok | +95% | 0.852 | -34% | 1.961 | 0.037 |
| B | 2 | AAVE/USDT | hammer_star | `lookback_low=10` | filtre=adx20 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +92% | +129% | +445% | 0.954 | -38% | 3.607 | 0.01 |
| B | 2 | CRV/USDT | force_index | `n=2` | filtre=regime_bench200 · çıkış=signal_only | +79% | +209% | +311% | 0.874 | -40% | 1.959 | 0.01 |
| B | 2 | ADA/USDT | trix_cross | `n=21,signal=9` | filtre=low_vol · çıkış=stop_atr=2.0,max_hold=10 | +102% | veri yok | +133% | 0.752 | -32% | 2.101 | 0.007 |
| B | 2 | LINK/USDT | stoch_reversal | `k=5,d=3,smooth=3,lo=10` | filtre=trend_sma200 · çıkış=stop_atr=2.0,trail_atr=3.0 | +107% | +170% | +170% | 0.774 | -31% | 2.043 | 0.005 |
| B | 2 | AXS/USDT | stoch_reversal | `k=5,d=3,smooth=1,lo=10` | filtre=adx20 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +66% | +211% | +211% | 0.698 | -38% | 1.601 | 0.005 |
| B | 2 | ETH/USDT | ma_cross | `kind=sma,pair=(20, 50)` | filtre=low_vol · çıkış=trail_atr=3.0 | +76% | +194% | +730% | 0.936 | -38% | 4.075 | 0.004 |
| B | 2 | ETC/USDT | ma_cross | `kind=sma,pair=(10, 50)` | filtre=low_vol · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +54% | +99% | +651% | 0.928 | -27% | 2.699 | 0.003 |
| B | 2 | FIL/USDT | stoch_reversal | `k=5,d=3,smooth=3,lo=10` | filtre=low_vol · çıkış=stop_atr=2.0,trail_atr=3.0 | +76% | +214% | +214% | 0.726 | -38% | 1.874 | 0.003 |
| B | 2 | LTC/USDT | hurst_switch | `n=100,fast=20,rsi_n=2` | filtre=htf_week_sma10 · çıkış=signal_only | +81% | +119% | +318% | 0.803 | -24% | 3.406 | 0.001 |
| B | 2 | BTC/USDT | ma_cross | `kind=kama,pair=(10, 50)` | filtre=trend_sma200 · çıkış=stop_atr=2.0,max_hold=10 | +50% | +43% | +225% | 0.79 | -26% | 2.884 | 0.001 |
| B | 2 | BTC/USDT | obv_trend | `n=50,price_n=50` | filtre=low_vol · çıkış=stop_atr=2.0,be_r=1.0 | +65% | +129% | +827% | 0.778 | -39% | 2.995 | 0.001 |
| B | 2 | BTC/USDT | atr_breakout | `n=10,k=2.0` | filtre=low_vol · çıkış=stop_atr=2.0,max_hold=10 | +75% | +143% | +411% | 0.883 | -16% | 5.879 | 0.0 |
| B | 1 | BTC/USDT | atr_breakout | `n=10,k=2.0` | çıkış=stop_atr=2.0,trail_atr=3.0 | +25% | +42% | +227% | 0.573 | -32% | 2.595 | 0.0 |

## Coin coin özet (ajan günlüğü)

- **AAVE/USDT**: 58 aday denendi, 1 kaldı. En iyi aday hammer_star (`lookback_low=10`, filtre=adx20 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0): OK — tüm adımlar geçti.
- **ADA/USDT**: 70 aday denendi, 1 kaldı. En iyi aday trix_cross (`n=21,signal=9`, filtre=low_vol · çıkış=stop_atr=2.0,max_hold=10): OK — tüm adımlar geçti.
- **ALGO/USDT**: elendi (S0: 1.8 yıl veri var, en az 3.0 yıl gerekli).
- **APT/USDT**: 58 aday denendi, 1 kaldı. En iyi aday stoch_reversal (`k=9,d=5,smooth=3,lo=10`, filtre=low_vol · çıkış=stop_atr=2.0,trail_atr=3.0): OK — tüm adımlar geçti.
- **ARB/USDT**: 78 aday denendi, 3 kaldı. En iyi aday engulfing (`trend_n=200`, filtre=adx20 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0): OK — tüm adımlar geçti.
- **ATOM/USDT**: 55 aday denendi, 0 kaldı. En iyi aday hurst_switch (`n=200,fast=20,rsi_n=2`, filtre=adx20 · çıkış=signal_only): S2 — PF 1.856, 1x maks. düşüş -46%.
- **AVAX/USDT**: 66 aday denendi, 0 kaldı. En iyi aday hammer_star (`lookback_low=10`, çıkış=stop_atr=2.0,trail_atr=3.0): S5 — 1 bar geç girişte Sharpe'ın %7'i kalıyor.
- **AXS/USDT**: 58 aday denendi, 1 kaldı. En iyi aday stoch_reversal (`k=5,d=3,smooth=1,lo=10`, filtre=adx20 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0): OK — tüm adımlar geçti.
- **BCH/USDT**: 60 aday denendi, 0 kaldı. En iyi aday zscore_reversion (`n=10,z=2.5`, çıkış=stop_atr=2.0,trail_atr=3.0): S4 — komşu ayarların %0'i kârlı.
- **BNB/USDT**: 63 aday denendi, 1 kaldı. En iyi aday price_ma (`kind=sma,n=50`, filtre=htf_week_sma10 · çıkış=signal_only): OK — tüm adımlar geçti.
- **BTC/USDT**: 67 aday denendi, 4 kaldı. En iyi aday ma_cross (`kind=kama,pair=(10, 50)`, filtre=trend_sma200 · çıkış=stop_atr=2.0,max_hold=10): OK — tüm adımlar geçti.
- **CRV/USDT**: 59 aday denendi, 1 kaldı. En iyi aday force_index (`n=2`, filtre=regime_bench200 · çıkış=signal_only): OK — tüm adımlar geçti.
- **DOGE/USDT**: 53 aday denendi, 0 kaldı. En iyi aday rsi_reversal (`n=7,lo=10,exit=60`, çıkış=stop_atr=2.0,trail_atr=3.0): S1 — 3y -33%, 5y +39%, full +68%; 14 işlem (zararlı: 3y).
- **DOT/USDT**: 60 aday denendi, 0 kaldı. En iyi aday williams_reversal (`n=7,lo=-90`, filtre=htf_week_sma10 · çıkış=trail_atr=3.0): S4 — komşu ayarların %33'i kârlı.
- **ETC/USDT**: 57 aday denendi, 1 kaldı. En iyi aday ma_cross (`kind=sma,pair=(10, 50)`, filtre=low_vol · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0): OK — tüm adımlar geçti.
- **ETH/USDT**: 72 aday denendi, 1 kaldı. En iyi aday ma_cross (`kind=sma,pair=(20, 50)`, filtre=low_vol · çıkış=trail_atr=3.0): OK — tüm adımlar geçti.
- **FIL/USDT**: 56 aday denendi, 1 kaldı. En iyi aday stoch_reversal (`k=5,d=3,smooth=3,lo=10`, filtre=low_vol · çıkış=stop_atr=2.0,trail_atr=3.0): OK — tüm adımlar geçti.
- **IMX/USDT**: 62 aday denendi, 0 kaldı. En iyi aday vortex_cross (`n=14`, çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0): S2 — PF 1.695, 1x maks. düşüş -64%.
- **INJ/USDT**: 58 aday denendi, 0 kaldı. En iyi aday hammer_star (`lookback_low=10`, çıkış=stop_atr=2.0,trail_atr=3.0): S4 — komşu ayarların %0'i kârlı.
- **LINK/USDT**: 57 aday denendi, 1 kaldı. En iyi aday stoch_reversal (`k=5,d=3,smooth=3,lo=10`, filtre=trend_sma200 · çıkış=stop_atr=2.0,trail_atr=3.0): OK — tüm adımlar geçti.
- **LTC/USDT**: 58 aday denendi, 1 kaldı. En iyi aday hurst_switch (`n=100,fast=20,rsi_n=2`, filtre=htf_week_sma10 · çıkış=signal_only): OK — tüm adımlar geçti.
- **MANA/USDT**: 56 aday denendi, 0 kaldı. En iyi aday awesome_zero (`fast=5,slow=34`, filtre=low_vol · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0): S2 — PF 2.202, 1x maks. düşüş -63%.
- **MINA/USDT**: 78 aday denendi, 1 kaldı. En iyi aday rsi_midline (`n=28,level=50`, filtre=low_vol · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0): OK — tüm adımlar geçti.
- **NEAR/USDT**: 72 aday denendi, 0 kaldı. En iyi aday rsi_midline (`n=9,level=50`, filtre=low_vol · çıkış=stop_atr=2.0,be_r=1.0): S2 — PF 2.929, 1x maks. düşüş -62%.
- **OP/USDT**: 57 aday denendi, 0 kaldı. En iyi aday force_index (`n=2`, çıkış=stop_atr=2.0,trail_atr=3.0 · onay=bollinger_breakout(≤5 bar)): S5 — 1 bar geç girişte Sharpe'ın %35'i kalıyor.
- **PYTH/USDT**: elendi (S0: 2.9 yıl veri var, en az 3.0 yıl gerekli).
- **SAND/USDT**: 56 aday denendi, 0 kaldı. En iyi aday engulfing (`trend_n=200`, filtre=adx20 · çıkış=stop_atr=2.0,max_hold=10): S2 — PF 2.191, 1x maks. düşüş -55%.
- **SNX/USDT**: 58 aday denendi, 0 kaldı. En iyi aday down_days (`n=4,hold_exit=1`, filtre=adx20 · çıkış=signal_only): S4 — komşu ayarların %33'i kârlı.
- **SOL/USDT**: 62 aday denendi, 2 kaldı. En iyi aday cci_breakout (`n=40,level=150`, filtre=regime_bench200 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0): OK — tüm adımlar geçti.
- **SUI/USDT**: 68 aday denendi, 0 kaldı. En iyi aday price_ma (`kind=sma,n=20`, filtre=low_vol · çıkış=stop_atr=2.0,max_hold=10): S5 — 1 bar geç girişte Sharpe'ın %20'i kalıyor.
- **THETA/USDT**: 55 aday denendi, 0 kaldı. En iyi aday ichimoku_cloud (`cfg=(20, 60, 120)`, çıkış=stop_atr=2.0,trail_atr=3.0): S2 — PF 2.415, 1x maks. düşüş -81%.
- **TRX/USDT**: 55 aday denendi, 0 kaldı. En iyi aday hurst_switch (`n=100,fast=20,rsi_n=2`, filtre=regime_bench200 · çıkış=trail_atr=3.0): S6 — yılların %57'i kârlı.
- **UNI/USDT**: 62 aday denendi, 0 kaldı. En iyi aday hammer_star (`lookback_low=10`, çıkış=stop_atr=2.0,trail_atr=3.0): S7 — PSR 0.752.
- **XLM/USDT**: 69 aday denendi, 2 kaldı. En iyi aday stoch_reversal (`k=9,d=5,smooth=3,lo=20`, filtre=low_vol · çıkış=stop_atr=2.0,be_r=1.0): OK — tüm adımlar geçti.
- **XRP/USDT**: 54 aday denendi, 0 kaldı. En iyi aday macd_cross (`cfg=(5, 35, 5),zero_filter=True`, filtre=low_vol · çıkış=signal_only): S2 — PF 4.202, 1x maks. düşüş -47%.

## Zayıf yönler (dürüst liste)

- 28115 deneme yapıldı. Bu kadar çok denemede şans eseri iyi görünen strateji çıkar. DSR bunu düzeltir; tier A sadece DSR ≥ eşik olanlardır.
- Seçim ve test aynı geçmiş veride yapıldı. Gerçek test arenadaki ileri (paper) kayıttır.
- Survivorship: liste bugünün coinlerinden oluşur. Borsadan silinen coinler yok, bu sonucu iyimser yapar.
- Funding sabit yıllık oranla, likidasyon işlem bazında yaklaşık modellenir.
- Tek borsa verisi (Bitget, yoksa OKX/KuCoin). Emir defteri ve piyasa etkisi modellenmez.

## Arena

Arena: 24 aktif (eleme geçen), 76 kontrol (yakın aday, switcher kullanmaz), 0 yeni üye, 0 kontrolden aktife. Üst sınır 100.

## Switcher backtest kapısı

Geçti: **False** — kontroller: `{"beats_equal_weight_all_windows": false, "positive_at_cost_stress": true, "max_dd_ok": true}`

Pencereler: `{"3y": {"sharpe": 1.375, "ew_sharpe": 3.312}, "5y": {"sharpe": 1.168, "ew_sharpe": 2.787}, "full": {"sharpe": 1.275, "ew_sharpe": 2.332}}`
