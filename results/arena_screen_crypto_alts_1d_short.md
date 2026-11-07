# Eleme motoru — crypto_alts 1d_short (yön: short)

Veri: 2018-01-01 → 2026-11-01. Coin: 34 uygun (toplam 35). Denenen varyant: 592 × coin = **30466 deneme**.
Her (coin, kural) için tek en iyi nokta değil, **en sağlam bölgenin merkezi** seçildi. Bu bir aday listesidir, karar değildir. Karar sadece doğrulama kapısında verilir.

> ⚠️ **Zaman makinesi kontrolü önerilir.** Bu liste binlerce deneme arasından seçildi; seçim süreçleri backtest'te iyi görünüp ileride çökebilir (2026-10-17 ve 10-19 testleri). Gerçek paraya aday olmadan önce `Time machine test` workflow'unu aynı yön (side) ve zaman dilimiyle çalıştırın. Kural: CLAUDE.md / AGENTS.md.

## Huni

| Adım | Ne kontrol edilir | Elenen | Kalan |
|---|---|---|---|
| S0 | veri yetersiz | 68 | 2312 |
| S1 | her dönemde kârlı değil / az işlem | 2183 | 129 |
| S2 | kâr faktörü veya düşüş zayıf | 124 | 5 |
| S3 | yüksek maliyette zarar | 0 | 5 |
| S4 | plato yok (komşu ayarlar zararda) | 0 | 5 |
| S5 | 1 bar gecikmeye dayanıksız | 3 | 2 |
| S6 | yılların çoğunda kârlı değil | 2 | 0 |
| S7 | istatistiksel güven düşük (PSR) | 0 | 0 |

## 2. aşama: filtre × çıkış × kombo (sadece S1'i geçen adaylarda)

129 aday → 10338 ek deneme (DSR'a eklendi). Her aday için en sağlam filtre/çıkış hücresi ve en sağlam kombo seçildi; kombo sadece kuralı tek başına geçerse aday olur. Seçilenler aynı S1–S7 adımlarından geçti.

| Adım | Ne kontrol edilir | Elenen | Kalan |
|---|---|---|---|
| S0 | veri yetersiz | 0 | 229 |
| S1 | her dönemde kârlı değil / az işlem | 143 | 86 |
| S2 | kâr faktörü veya düşüş zayıf | 52 | 34 |
| S3 | yüksek maliyette zarar | 0 | 34 |
| S4 | plato yok (komşu ayarlar zararda) | 7 | 27 |
| S5 | 1 bar gecikmeye dayanıksız | 2 | 25 |
| S6 | yılların çoğunda kârlı değil | 5 | 20 |
| S7 | istatistiksel güven düşük (PSR) | 1 | 19 |

## Geçenler (19)

Kazanma oranı tek başına bir şey söylemez. Sistem sadece **kazanma oranı > başabaş oranı** olduğunda kârlıdır. Başabaş = 1 / (1 + ödeme oranı); ödeme oranı = ortalama kazanç / ortalama kayıp (maliyet sonrası). Pay = kazanma oranı − başabaş. Beklenen = işlem başına ortalama net getiri.

| Tier | Aşama | Coin | Kural | Ayar | Varyant | 3y | 5y | Tüm | Sharpe | 1x DD | PF | Kazanma | Ödeme | Başabaş | Pay | Beklenen | DSR |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| B | 2 | ARB/USDT | engulfing | `trend_n=0` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=vwap_cross(≤5 bar) | +446% | veri yok | +507% | 1.382 | -27% | 3.858 | 65% | 2.09 | 32% | +32% | +5.60% | 0.207 |
| B | 2 | IMX/USDT | cci_breakout | `n=14,level=100` | filtre=htf_week_sma10 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +343% | veri yok | +1004% | 1.178 | -36% | 3.515 | 61% | 2.213 | 31% | +30% | +7.12% | 0.087 |
| B | 2 | ARB/USDT | price_ma | `kind=sma,n=20` | çıkış=stop_atr=2.0,max_hold=10 | +271% | veri yok | +283% | 1.019 | -29% | 1.929 | 51% | 1.869 | 35% | +16% | +2.87% | 0.07 |
| B | 2 | IMX/USDT | triple_ma | `set=(5, 20, 50),kind=sma` | filtre=htf_week_sma10 · çıkış=stop_atr=2.0,max_hold=10 | +204% | veri yok | +529% | 1.112 | -29% | 5.603 | 68% | 2.668 | 27% | +40% | +7.68% | 0.069 |
| B | 2 | APT/USDT | cci_reversal | `n=14,lo=-100` | filtre=low_vol · çıkış=trail_atr=3.0 | +161% | veri yok | +220% | 1.066 | -36% | 2.776 | 82% | 0.607 | 62% | +20% | +3.59% | 0.057 |
| B | 2 | MINA/USDT | roc_breakout | `n=63,th=5` | çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +198% | +510% | +510% | 1.113 | -35% | 4.131 | 63% | 2.392 | 30% | +34% | +7.24% | 0.055 |
| B | 2 | MINA/USDT | rsi_midline | `n=28,level=50` | çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +270% | +597% | +582% | 1.045 | -39% | 2.138 | 45% | 2.647 | 27% | +17% | +4.13% | 0.046 |
| B | 2 | MINA/USDT | macd_cross | `cfg=(12, 26, 9),zero_filter=False` | filtre=trend_sma200 · çıkış=trail_atr=3.0 | +190% | +644% | +644% | 1.047 | -39% | 3.434 | 63% | 2.003 | 33% | +30% | +6.67% | 0.043 |
| B | 2 | OP/USDT | smc_liquidity_sweep | `k=3` | filtre=adx20 · çıkış=trail_atr=3.0 | +69% | veri yok | +218% | 0.925 | -40% | 2.169 | 50% | 2.169 | 32% | +18% | +4.10% | 0.036 |
| B | 2 | ARB/USDT | obv_trend | `n=50,price_n=50` | filtre=adx20 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +143% | veri yok | +127% | 0.859 | -39% | 2.17 | 40% | 3.255 | 24% | +16% | +3.28% | 0.035 |
| B | 2 | ARB/USDT | stochrsi_reversal | `n=9,lo=5` | filtre=htf_week_sma10 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +117% | veri yok | +121% | 0.808 | -34% | 1.971 | 73% | 0.717 | 58% | +15% | +3.49% | 0.03 |
| B | 2 | DOT/USDT | smc_liquidity_sweep | `k=3` | filtre=trend_sma200 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +153% | +283% | +352% | 1.0 | -38% | 2.232 | 60% | 1.514 | 40% | +20% | +3.68% | 0.024 |
| B | 2 | ARB/USDT | elder_impulse | `ema_n=13,macd_cfg=(12, 26, 9)` | filtre=htf_week_sma10 · çıkış=stop_atr=2.0,max_hold=10 | +145% | veri yok | +138% | 0.715 | -33% | 1.662 | 45% | 2.05 | 33% | +12% | +2.24% | 0.02 |
| B | 2 | DOT/USDT | smc_ote | `k=3,fib_lo=0.5` | filtre=trend_sma200 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +45% | +116% | +206% | 0.787 | -28% | 2.289 | 60% | 1.553 | 39% | +20% | +3.00% | 0.005 |
| B | 2 | DOT/USDT | rsi_reversal | `n=5,lo=35,exit=50` | filtre=htf_week_sma10 · çıkış=trail_atr=3.0 | +41% | +68% | +111% | 0.754 | -21% | 2.372 | 81% | 0.552 | 64% | +17% | +1.70% | 0.005 |
| B | 2 | AAVE/USDT | smc_ote | `k=5,fib_lo=0.5` | çıkış=stop_atr=2.0,max_hold=10 | +108% | +191% | +134% | 0.614 | -34% | 1.661 | 56% | 1.3 | 44% | +13% | +2.70% | 0.002 |
| B | 2 | FIL/USDT | williams_reversal | `n=10,lo=-80` | filtre=htf_week_sma10 · çıkış=stop_atr=2.0,trail_atr=3.0 | +73% | +168% | +119% | 0.552 | -37% | 1.667 | 71% | 0.691 | 59% | +12% | +2.12% | 0.001 |
| B | 2 | XLM/USDT | macd_cross | `cfg=(8, 21, 5),zero_filter=True` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_liquidity_sweep(≤5 bar) | +34% | +54% | +244% | 0.641 | -27% | 3.76 | 62% | 2.256 | 31% | +32% | +5.38% | 0.0 |
| B | 2 | XLM/USDT | smc_ote | `k=8,fib_lo=0.5` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=pivot_bounce(≤5 bar) | +102% | +207% | +127% | 0.563 | -28% | 2.128 | 47% | 2.432 | 29% | +18% | +3.43% | 0.0 |

## Coin coin özet (ajan günlüğü)

- **AAVE/USDT**: 70 aday denendi, 1 kaldı. En iyi aday smc_ote (`k=5,fib_lo=0.5`, çıkış=stop_atr=2.0,max_hold=10): OK — tüm adımlar geçti.
- **ADA/USDT**: 75 aday denendi, 0 kaldı. En iyi aday rsi_midline (`n=21,level=50`, filtre=low_vol · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0): S2 — PF 1.867, 1x maks. düşüş -46%.
- **ALGO/USDT**: 69 aday denendi, 0 kaldı. En iyi aday stochrsi_reversal (`n=14,lo=5`, filtre=low_vol · çıkış=stop_atr=2.0,max_hold=10): S2 — PF 1.697, 1x maks. düşüş -41%.
- **APT/USDT**: 91 aday denendi, 1 kaldı. En iyi aday cci_reversal (`n=14,lo=-100`, filtre=low_vol · çıkış=trail_atr=3.0): OK — tüm adımlar geçti.
- **ARB/USDT**: 101 aday denendi, 5 kaldı. En iyi aday engulfing (`trend_n=0`, çıkış=stop_atr=2.0,trail_atr=3.0 · onay=vwap_cross(≤5 bar)): OK — tüm adımlar geçti.
- **ATOM/USDT**: 68 aday denendi, 0 kaldı. En iyi aday rsi_divergence (`n=14,k=5,exit_level=50`, çıkış=stop_atr=2.0,trail_atr=3.0): S1 — 3y -0%, 5y +12%, full +96%; 18 işlem (zararlı: 3y).
- **AVAX/USDT**: 78 aday denendi, 0 kaldı. En iyi aday smc_fvg (`max_age=10,min_gap_atr=0.5`, çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0): S6 — yılların %57'i kârlı.
- **AXS/USDT**: 70 aday denendi, 0 kaldı. En iyi aday smc_ote (`k=3,fib_lo=0.618`, çıkış=stop_atr=2.0,trail_atr=3.0): S2 — PF 1.393, 1x maks. düşüş -63%.
- **BCH/USDT**: 71 aday denendi, 0 kaldı. En iyi aday williams_reversal (`n=14,lo=-95`, çıkış=stop_atr=2.0,trail_atr=3.0): S5 — 1 bar geç girişte Sharpe'ın %21'i kalıyor.
- **BNB/USDT**: 68 aday denendi, 0 kaldı. En iyi aday stoch_reversal (`k=5,d=5,smooth=3,lo=10`, çıkış=stop_atr=2.0,trail_atr=3.0): S1 — 3y -17%, 5y +1%, full +14%; 74 işlem (zararlı: 3y).
- **BTC/USDT**: 68 aday denendi, 0 kaldı. En iyi aday roc_breakout (`n=252,th=5`, çıkış=stop_atr=2.0,trail_atr=3.0): S1 — 3y +13%, 5y +32%, full +91%; 14 işlem.
- **CRV/USDT**: 68 aday denendi, 0 kaldı. En iyi aday down_days (`n=4,hold_exit=1`, çıkış=stop_atr=2.0,trail_atr=3.0): S5 — 1 bar geç girişte Sharpe'ın %0'i kalıyor.
- **DOGE/USDT**: 71 aday denendi, 0 kaldı. En iyi aday smc_fvg (`max_age=20,min_gap_atr=0.0`, filtre=adx20 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0): S2 — PF 1.826, 1x maks. düşüş -59%.
- **DOT/USDT**: 75 aday denendi, 3 kaldı. En iyi aday smc_liquidity_sweep (`k=3`, filtre=trend_sma200 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0): OK — tüm adımlar geçti.
- **ETC/USDT**: 78 aday denendi, 0 kaldı. En iyi aday stoch_reversal (`k=9,d=5,smooth=3,lo=10`, filtre=adx20 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0): S4 — komşu ayarların %40'i kârlı.
- **ETH/USDT**: 74 aday denendi, 0 kaldı. En iyi aday smc_liquidity_sweep (`k=3`, filtre=adx20 · çıkış=stop_atr=2.0,be_r=1.0): S2 — PF 1.379, 1x maks. düşüş -80%.
- **FIL/USDT**: 77 aday denendi, 1 kaldı. En iyi aday williams_reversal (`n=10,lo=-80`, filtre=htf_week_sma10 · çıkış=stop_atr=2.0,trail_atr=3.0): OK — tüm adımlar geçti.
- **IMX/USDT**: 94 aday denendi, 2 kaldı. En iyi aday cci_breakout (`n=14,level=100`, filtre=htf_week_sma10 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0): OK — tüm adımlar geçti.
- **INJ/USDT**: 68 aday denendi, 0 kaldı. En iyi aday smc_ote (`k=3,fib_lo=0.618`, çıkış=stop_atr=2.0,trail_atr=3.0): S1 — 3y -11%, 5y +38%, full +67%; 45 işlem (zararlı: 3y).
- **LINK/USDT**: 68 aday denendi, 0 kaldı. En iyi aday rsi_reversal (`n=28,lo=20,exit=60`, çıkış=stop_atr=2.0,trail_atr=3.0): S1 — 3y -5%, 5y -5%, full +66%; 5 işlem (zararlı: 3y, 5y).
- **LTC/USDT**: 70 aday denendi, 0 kaldı. En iyi aday cci_reversal (`n=14,lo=-200`, çıkış=stop_atr=2.0,trail_atr=3.0): S2 — PF 1.302, 1x maks. düşüş -60%.
- **MANA/USDT**: 70 aday denendi, 0 kaldı. En iyi aday awesome_zero (`fast=5,slow=34`, çıkış=stop_atr=2.0,trail_atr=3.0): S2 — PF 1.874, 1x maks. düşüş -65%.
- **MINA/USDT**: 114 aday denendi, 3 kaldı. En iyi aday roc_breakout (`n=63,th=5`, çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0): OK — tüm adımlar geçti.
- **NEAR/USDT**: 70 aday denendi, 0 kaldı. En iyi aday adx_trend (`n=14,th=20`, çıkış=stop_atr=2.0,trail_atr=3.0): S2 — PF 1.793, 1x maks. düşüş -62%.
- **OP/USDT**: 80 aday denendi, 1 kaldı. En iyi aday smc_liquidity_sweep (`k=3`, filtre=adx20 · çıkış=trail_atr=3.0): OK — tüm adımlar geçti.
- **PYTH/USDT**: elendi (S0: 2.9 yıl veri var, en az 3.0 yıl gerekli).
- **SAND/USDT**: 74 aday denendi, 0 kaldı. En iyi aday mfi_reversal (`n=10,lo=30`, filtre=trend_sma200 · çıkış=stop_atr=2.0,max_hold=10): S4 — komşu ayarların %0'i kârlı.
- **SNX/USDT**: 72 aday denendi, 0 kaldı. En iyi aday down_days (`n=4,hold_exit=1`, çıkış=stop_atr=2.0,trail_atr=3.0): S5 — 1 bar geç girişte Sharpe'ın %0'i kalıyor.
- **SOL/USDT**: 68 aday denendi, 0 kaldı. En iyi aday smc_liquidity_sweep (`k=3`, çıkış=stop_atr=2.0,trail_atr=3.0): S1 — 3y -18%, 5y +99%, full +77%; 70 işlem (zararlı: 3y).
- **SUI/USDT**: 70 aday denendi, 0 kaldı. En iyi aday stoch_reversal (`k=5,d=3,smooth=3,lo=10`, çıkış=stop_atr=2.0,trail_atr=3.0): S2 — PF 1.418, 1x maks. düşüş -67%.
- **THETA/USDT**: 68 aday denendi, 0 kaldı. En iyi aday triple_ma (`set=(20, 50, 100),kind=sma`, çıkış=stop_atr=2.0,trail_atr=3.0): S1 — 3y +70%, 5y +128%, full +106%; 24 işlem.
- **TRX/USDT**: 68 aday denendi, 0 kaldı. En iyi aday rsi_reversal (`n=14,lo=10,exit=50`, çıkış=stop_atr=2.0,trail_atr=3.0): S1 — 3y +21%, 5y +21%, full +21%; 1 işlem.
- **UNI/USDT**: 70 aday denendi, 0 kaldı. En iyi aday smc_ote (`k=3,fib_lo=0.5`, filtre=low_vol · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0): S5 — 1 bar geç girişte Sharpe'ın %38'i kalıyor.
- **XLM/USDT**: 75 aday denendi, 2 kaldı. En iyi aday macd_cross (`cfg=(8, 21, 5),zero_filter=True`, çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_liquidity_sweep(≤5 bar)): OK — tüm adımlar geçti.
- **XRP/USDT**: 70 aday denendi, 0 kaldı. En iyi aday roc_breakout (`n=252,th=5`, çıkış=stop_atr=2.0,trail_atr=3.0): S6 — yılların %56'i kârlı.

## Zayıf yönler (dürüst liste)

- 30466 deneme yapıldı. Bu kadar çok denemede şans eseri iyi görünen strateji çıkar. DSR bunu düzeltir; tier A sadece DSR ≥ eşik olanlardır.
- Seçim ve test aynı geçmiş veride yapıldı. Gerçek test arenadaki ileri (paper) kayıttır.
- Survivorship: liste bugünün coinlerinden oluşur. Borsadan silinen coinler yok, bu sonucu iyimser yapar.
- Funding sabit yıllık oranla, likidasyon işlem bazında yaklaşık modellenir.
- Tek borsa verisi (Bitget, yoksa OKX/KuCoin). Emir defteri ve piyasa etkisi modellenmez.

## Arena

Arena: 42 aktif (eleme geçen), 58 kontrol (yakın aday, switcher kullanmaz), 10 yeni üye, 0 kontrolden aktife. Üst sınır 100.

## Switcher backtest kapısı

Geçti: **False** — kontroller: `{"beats_equal_weight_all_windows": false, "positive_at_cost_stress": true, "max_dd_ok": true}`

Pencereler: `{"3y": {"sharpe": 1.116, "ew_sharpe": 1.926}, "5y": {"sharpe": 0.757, "ew_sharpe": 1.86}, "full": {"sharpe": 0.449, "ew_sharpe": 0.866}}`
