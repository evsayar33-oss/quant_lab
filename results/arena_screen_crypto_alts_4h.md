# Eleme motoru — crypto_alts 4h

Veri: 2018-01-11 → 2026-10-17. Coin: 34 uygun (toplam 35). Denenen varyant: 518 × coin = **25971 deneme**.
Her (coin, kural) için tek en iyi nokta değil, **en sağlam bölgenin merkezi** seçildi. Bu bir aday listesidir, karar değildir. Karar sadece doğrulama kapısında verilir.

## Huni

| Adım | Ne kontrol edilir | Elenen | Kalan |
|---|---|---|---|
| S0 | veri yetersiz | 53 | 1802 |
| S1 | her dönemde kârlı değil / az işlem | 1653 | 149 |
| S2 | kâr faktörü veya düşüş zayıf | 121 | 28 |
| S3 | yüksek maliyette zarar | 2 | 26 |
| S4 | plato yok (komşu ayarlar zararda) | 8 | 18 |
| S5 | 1 bar gecikmeye dayanıksız | 2 | 16 |
| S6 | yılların çoğunda kârlı değil | 3 | 13 |
| S7 | istatistiksel güven düşük (PSR) | 4 | 9 |

## 2. aşama: filtre × çıkış × kombo (sadece S1'i geçen adaylarda)

149 aday → 8359 ek deneme (DSR'a eklendi). Her aday için en sağlam filtre/çıkış hücresi ve en sağlam kombo seçildi; kombo sadece kuralı tek başına geçerse aday olur. Seçilenler aynı S1–S7 adımlarından geçti.

| Adım | Ne kontrol edilir | Elenen | Kalan |
|---|---|---|---|
| S0 | veri yetersiz | 0 | 240 |
| S1 | her dönemde kârlı değil / az işlem | 63 | 177 |
| S2 | kâr faktörü veya düşüş zayıf | 88 | 89 |
| S3 | yüksek maliyette zarar | 0 | 89 |
| S4 | plato yok (komşu ayarlar zararda) | 32 | 57 |
| S5 | 1 bar gecikmeye dayanıksız | 4 | 53 |
| S6 | yılların çoğunda kârlı değil | 6 | 47 |
| S7 | istatistiksel güven düşük (PSR) | 2 | 45 |

## Geçenler (54)

| Tier | Aşama | Coin | Kural | Ayar | Varyant | 3y | 5y | Tüm | Sharpe | 1x DD | PF | DSR |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| B | 2 | SUI/USDT | roc_breakout | `n=252,th=10` | filtre=adx20 · çıkış=stop_atr=2.0,tp_r=3.0 | +778% | veri yok | +1205% | 1.799 | -30% | 2.805 | 0.056 |
| B | 2 | ARB/USDT | price_ma | `kind=kama,n=200` | filtre=trend_sma200 · çıkış=trail_atr=3.0 | +921% | veri yok | +1016% | 1.537 | -32% | 2.104 | 0.013 |
| B | 2 | ARB/USDT | macd_zero | `cfg=(12, 26, 9)` | filtre=regime_bench200 · çıkış=stop_atr=2.0,tp_r=3.0 | +618% | veri yok | +659% | 1.464 | -40% | 1.779 | 0.011 |
| B | 2 | ARB/USDT | linreg_slope | `n=20,th=0.0005` | filtre=htf_week_sma10 · çıkış=stop_atr=2.0,tp_r=3.0 | +823% | veri yok | +672% | 1.324 | -35% | 1.635 | 0.005 |
| B | 2 | ARB/USDT | linreg_slope | `n=20,th=0.0005` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=cmf_flow(≤5 bar) | +806% | veri yok | +701% | 1.349 | -39% | 2.268 | 0.004 |
| B | 2 | ARB/USDT | bollinger_breakout | `n=50,k=2.5` | filtre=low_vol · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +110% | veri yok | +145% | 1.308 | -19% | 2.493 | 0.004 |
| B | 2 | ARB/USDT | bb_squeeze | `n=20,q=0.1,look=126` | filtre=low_vol · çıkış=stop_atr=2.0,max_hold=10 | +183% | veri yok | +214% | 1.307 | -23% | 2.035 | 0.004 |
| B | 2 | ARB/USDT | triple_ma | `set=(10, 50, 200),kind=ema` | filtre=htf_week_sma10 · çıkış=stop_atr=2.0,tp_r=3.0 | +433% | veri yok | +453% | 1.289 | -34% | 1.823 | 0.004 |
| B | 2 | OP/USDT | bollinger_breakout | `n=50,k=2.5` | filtre=trend_sma200 · çıkış=stop_atr=2.0,max_hold=10 | +306% | veri yok | +981% | 1.38 | -30% | 2.344 | 0.003 |
| B | 2 | SOL/USDT | high_52w_break | `n=126,exit_ma=50` | filtre=regime_bench200 · çıkış=stop_atr=2.0,be_r=1.0 | +251% | +398% | +1747% | 1.415 | -33% | 4.883 | 0.002 |
| B | 1 | XLM/USDT | high_52w_break | `n=126,exit_ma=50` | çıkış=stop_atr=2.0,trail_atr=3.0 | +244% | veri yok | +244% | 1.182 | -26% | 3.898 | 0.001 |
| B | 2 | ARB/USDT | ma_cross | `kind=sma,pair=(10, 30)` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=roc_breakout(≤3 bar) | +261% | veri yok | +212% | 1.039 | -31% | 2.938 | 0.001 |
| B | 2 | ETH/USDT | bollinger_breakout | `n=50,k=2.5` | filtre=regime_bench200 · çıkış=trail_atr=3.0 | +358% | +699% | +4439% | 1.307 | -32% | 2.405 | 0.0 |
| B | 2 | XRP/USDT | high_52w_break | `n=126,exit_ma=50` | filtre=regime_bench200 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +107% | +150% | +603% | 1.259 | -21% | 2.898 | 0.0 |
| B | 2 | SOL/USDT | cci_breakout | `n=40,level=150` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=ma_cross(≤3 bar) | +113% | +414% | +568% | 1.21 | -35% | 2.728 | 0.0 |
| B | 2 | SOL/USDT | high_52w_break | `n=126,exit_ma=50` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=chop_switch(≤0 bar) | +113% | +218% | +425% | 1.182 | -27% | 3.667 | 0.0 |
| B | 2 | FIL/USDT | linreg_slope | `n=20,th=0.001` | filtre=regime_bench200 · çıkış=stop_atr=2.0,max_hold=10 | +466% | +592% | +942% | 1.177 | -39% | 1.62 | 0.0 |
| B | 1 | ETH/USDT | bollinger_breakout | `n=50,k=2.5` | çıkış=stop_atr=2.0,trail_atr=3.0 | +322% | +408% | +2869% | 1.153 | -34% | 1.986 | 0.0 |
| B | 2 | SOL/USDT | donchian_breakout | `entry=100,exit=10` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=ma_cross(≤5 bar) | +122% | +228% | +425% | 1.1 | -33% | 2.61 | 0.0 |
| B | 2 | ADA/USDT | bollinger_breakout | `n=20,k=2.5` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=chop_switch(≤0 bar) | +117% | veri yok | +208% | 1.1 | -29% | 3.848 | 0.0 |
| B | 2 | OP/USDT | cmf_flow | `n=40,th=0.2` | filtre=low_vol · çıkış=stop_atr=2.0,tp_r=3.0 | +98% | veri yok | +175% | 1.098 | -39% | 2.137 | 0.0 |
| B | 2 | SAND/USDT | bollinger_breakout | `n=50,k=2.5` | filtre=adx20 · çıkış=stop_atr=2.0,max_hold=10 | +192% | veri yok | +778% | 1.067 | -39% | 2.01 | 0.0 |
| B | 2 | ETH/USDT | high_52w_break | `n=126,exit_ma=50` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=chop_switch(≤5 bar) | +93% | +80% | +552% | 1.047 | -23% | 2.765 | 0.0 |
| B | 2 | ARB/USDT | macd_zero | `cfg=(12, 26, 9)` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=roc_breakout(≤5 bar) | +148% | veri yok | +225% | 1.02 | -30% | 2.488 | 0.0 |
| B | 2 | ETH/USDT | high_52w_break | `n=126,exit_ma=50` | filtre=low_vol · çıkış=signal_only | +74% | +101% | +700% | 0.98 | -33% | 2.656 | 0.0 |
| B | 1 | ARB/USDT | hurst_switch | `n=200,fast=20,rsi_n=5` | çıkış=stop_atr=2.0,trail_atr=3.0 | +143% | veri yok | +135% | 0.959 | -31% | 2.171 | 0.0 |
| B | 1 | XRP/USDT | high_52w_break | `n=126,exit_ma=50` | çıkış=stop_atr=2.0,trail_atr=3.0 | +141% | +157% | +740% | 0.957 | -39% | 2.54 | 0.0 |
| B | 2 | ADA/USDT | high_52w_break | `n=126,exit_ma=50` | filtre=adx20 · çıkış=stop_atr=2.0,be_r=1.0 | +323% | veri yok | +239% | 0.923 | -38% | 3.504 | 0.0 |
| B | 2 | ADA/USDT | cci_breakout | `n=40,level=100` | filtre=low_vol · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +125% | veri yok | +190% | 0.887 | -37% | 1.406 | 0.0 |
| B | 2 | OP/USDT | bollinger_breakout | `n=50,k=2.5` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=roc_breakout(≤5 bar) | +164% | veri yok | +218% | 0.857 | -29% | 2.138 | 0.0 |
| B | 2 | INJ/USDT | volume_breakout | `n=50,rv=3.0` | filtre=htf_week_sma10 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +74% | veri yok | +127% | 0.831 | -36% | 1.979 | 0.0 |
| B | 2 | BNB/USDT | donchian_breakout | `entry=100,exit=10` | filtre=htf_week_sma10 · çıkış=trail_atr=3.0 | +89% | veri yok | +91% | 0.83 | -22% | 1.845 | 0.0 |
| B | 2 | BNB/USDT | donchian_breakout | `entry=100,exit=10` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=ma_cross(≤5 bar) | +73% | veri yok | +56% | 0.82 | -12% | 2.378 | 0.0 |
| B | 2 | ARB/USDT | keltner_breakout | `n=50,k=2.0` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=cmf_flow(≤0 bar) | +140% | veri yok | +122% | 0.813 | -22% | 1.938 | 0.0 |
| B | 2 | DOT/USDT | bb_squeeze | `n=20,q=0.1,look=252` | filtre=htf_week_sma10 · çıkış=stop_atr=2.0,tp_r=3.0 | +19% | +24% | +194% | 0.811 | -37% | 1.87 | 0.0 |
| B | 2 | DOT/USDT | bb_squeeze | `n=20,q=0.1,look=252` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=ma_cross(≤3 bar) | +23% | +47% | +172% | 0.794 | -33% | 3.184 | 0.0 |
| B | 1 | ETH/USDT | keltner_breakout | `n=20,k=2.5` | çıkış=stop_atr=2.0,trail_atr=3.0 | +75% | +91% | +674% | 0.785 | -38% | 1.601 | 0.0 |
| B | 2 | AXS/USDT | roc_breakout | `n=252,th=5` | filtre=trend_sma200 · çıkış=trail_atr=3.0 | +73% | +224% | +224% | 0.775 | -35% | 1.789 | 0.0 |
| B | 2 | XLM/USDT | keltner_breakout | `n=20,k=2.5` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=cmf_flow(≤3 bar) | +113% | veri yok | +100% | 0.748 | -31% | 1.897 | 0.0 |
| B | 2 | XLM/USDT | donchian_breakout | `entry=40,exit=20` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=chop_switch(≤0 bar) | +97% | veri yok | +93% | 0.736 | -33% | 2.019 | 0.0 |
| B | 2 | BTC/USDT | bollinger_breakout | `n=50,k=2.0` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=chop_switch(≤0 bar) | +65% | +70% | +140% | 0.717 | -22% | 1.976 | 0.0 |
| B | 2 | XLM/USDT | ma_cross | `kind=ema,pair=(20, 50)` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=cmf_flow(≤3 bar) | +74% | veri yok | +69% | 0.714 | -25% | 2.251 | 0.0 |
| B | 2 | ETH/USDT | volume_breakout | `n=50,rv=2.0` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=roc_breakout(≤5 bar) | +59% | +62% | +162% | 0.665 | -25% | 2.782 | 0.0 |
| B | 1 | SOL/USDT | volume_breakout | `n=50,rv=1.5` | çıkış=stop_atr=2.0,trail_atr=3.0 | +98% | +158% | +196% | 0.659 | -40% | 1.585 | 0.0 |
| B | 1 | ETH/USDT | high_52w_break | `n=126,exit_ma=50` | çıkış=stop_atr=2.0,trail_atr=3.0 | +44% | +26% | +244% | 0.658 | -31% | 1.642 | 0.0 |
| B | 1 | ETH/USDT | volume_breakout | `n=50,rv=2.0` | çıkış=stop_atr=2.0,trail_atr=3.0 | +111% | +102% | +207% | 0.642 | -30% | 1.921 | 0.0 |
| B | 2 | SAND/USDT | psar_flip | `cfg=(0.01, 0.1)` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=cmf_flow(≤0 bar) | +155% | veri yok | +97% | 0.629 | -34% | 2.283 | 0.0 |
| B | 2 | OP/USDT | adx_trend | `n=20,th=25` | filtre=adx20 · çıkış=trail_atr=3.0 | +9% | veri yok | +109% | 0.625 | -36% | 1.757 | 0.0 |
| B | 2 | MINA/USDT | ma_cross | `kind=ema,pair=(50, 150)` | filtre=regime_bench200 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +39% | +96% | +102% | 0.624 | -27% | 1.883 | 0.0 |
| B | 1 | OP/USDT | cmf_flow | `n=40,th=0.2` | çıkış=stop_atr=2.0,trail_atr=3.0 | +115% | veri yok | +110% | 0.609 | -39% | 1.549 | 0.0 |
| B | 2 | UNI/USDT | bollinger_breakout | `n=50,k=2.5` | filtre=low_vol · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +84% | +117% | +88% | 0.606 | -30% | 1.468 | 0.0 |
| B | 2 | BTC/USDT | keltner_breakout | `n=20,k=2.5` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=chop_switch(≤3 bar) | +46% | +77% | +125% | 0.603 | -30% | 1.64 | 0.0 |
| B | 2 | ADA/USDT | high_52w_break | `n=126,exit_ma=50` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=cmf_flow(≤5 bar) | +70% | veri yok | +68% | 0.568 | -33% | 1.884 | 0.0 |
| B | 2 | ALGO/USDT | bb_squeeze | `n=20,q=0.2,look=252` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=ma_cross(≤3 bar) | +71% | +59% | +96% | 0.482 | -34% | 1.909 | 0.0 |

## Coin coin özet (ajan günlüğü)

- **AAVE/USDT**: 54 aday denendi, 0 kaldı. En iyi aday coppock_turn (`scale=5`, çıkış=stop_atr=2.0,tp_r=3.0): S2 — PF 1.335, 1x maks. düşüş -63%.
- **ADA/USDT**: 77 aday denendi, 4 kaldı. En iyi aday bollinger_breakout (`n=20,k=2.5`, çıkış=stop_atr=2.0,trail_atr=3.0 · onay=chop_switch(≤0 bar)): OK — tüm adımlar geçti.
- **ALGO/USDT**: 55 aday denendi, 1 kaldı. En iyi aday bb_squeeze (`n=20,q=0.2,look=252`, çıkış=stop_atr=2.0,trail_atr=3.0 · onay=ma_cross(≤3 bar)): OK — tüm adımlar geçti.
- **APT/USDT**: 55 aday denendi, 0 kaldı. En iyi aday cmf_flow (`n=20,th=0.05`, çıkış=stop_atr=2.0,trail_atr=3.0 · onay=ma_cross(≤3 bar)): S4 — komşu ayarların %33'i kârlı.
- **ARB/USDT**: 82 aday denendi, 11 kaldı. En iyi aday price_ma (`kind=kama,n=200`, filtre=trend_sma200 · çıkış=trail_atr=3.0): OK — tüm adımlar geçti.
- **ATOM/USDT**: 57 aday denendi, 0 kaldı. En iyi aday chop_switch (`n=14,lo=38.2,hi=61.8`, filtre=low_vol · çıkış=stop_atr=2.0,max_hold=10): S4 — komşu ayar yok.
- **AVAX/USDT**: 56 aday denendi, 0 kaldı. En iyi aday roc_breakout (`n=63,th=5`, filtre=low_vol · çıkış=stop_atr=2.0,be_r=1.0): S2 — PF 2.558, 1x maks. düşüş -55%.
- **AXS/USDT**: 54 aday denendi, 1 kaldı. En iyi aday roc_breakout (`n=252,th=5`, filtre=trend_sma200 · çıkış=trail_atr=3.0): OK — tüm adımlar geçti.
- **BCH/USDT**: 54 aday denendi, 0 kaldı. En iyi aday coppock_turn (`scale=5`, filtre=low_vol · çıkış=stop_atr=2.0,be_r=1.0): S2 — PF 1.958, 1x maks. düşüş -47%.
- **BNB/USDT**: 64 aday denendi, 2 kaldı. En iyi aday donchian_breakout (`entry=100,exit=10`, filtre=htf_week_sma10 · çıkış=trail_atr=3.0): OK — tüm adımlar geçti.
- **BTC/USDT**: 64 aday denendi, 2 kaldı. En iyi aday bollinger_breakout (`n=50,k=2.0`, çıkış=stop_atr=2.0,trail_atr=3.0 · onay=chop_switch(≤0 bar)): OK — tüm adımlar geçti.
- **CRV/USDT**: 53 aday denendi, 0 kaldı. En iyi aday trix_cross (`n=12,signal=7`, çıkış=stop_atr=2.0,trail_atr=3.0): S1 — 3y -95%, 5y -89%, full -90%; 781 işlem (zararlı: 3y, 5y, full).
- **DOGE/USDT**: 57 aday denendi, 0 kaldı. En iyi aday hurst_switch (`n=200,fast=20,rsi_n=5`, çıkış=stop_atr=2.0,trail_atr=3.0): S5 — 1 bar geç girişte Sharpe'ın %0'i kalıyor.
- **DOT/USDT**: 55 aday denendi, 2 kaldı. En iyi aday bb_squeeze (`n=20,q=0.1,look=252`, filtre=htf_week_sma10 · çıkış=stop_atr=2.0,tp_r=3.0): OK — tüm adımlar geçti.
- **ETC/USDT**: 55 aday denendi, 0 kaldı. En iyi aday coppock_turn (`scale=5`, filtre=trend_sma200 · çıkış=stop_atr=2.0,be_r=1.0): S6 — yılların %56'i kârlı.
- **ETH/USDT**: 67 aday denendi, 8 kaldı. En iyi aday bollinger_breakout (`n=50,k=2.5`, filtre=regime_bench200 · çıkış=trail_atr=3.0): OK — tüm adımlar geçti.
- **FIL/USDT**: 61 aday denendi, 1 kaldı. En iyi aday linreg_slope (`n=20,th=0.001`, filtre=regime_bench200 · çıkış=stop_atr=2.0,max_hold=10): OK — tüm adımlar geçti.
- **IMX/USDT**: 55 aday denendi, 0 kaldı. En iyi aday hurst_switch (`n=200,fast=20,rsi_n=5`, çıkış=stop_atr=2.0,trail_atr=3.0): S2 — PF 1.423, 1x maks. düşüş -47%.
- **INJ/USDT**: 62 aday denendi, 1 kaldı. En iyi aday volume_breakout (`n=50,rv=3.0`, filtre=htf_week_sma10 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0): OK — tüm adımlar geçti.
- **LINK/USDT**: 53 aday denendi, 0 kaldı. En iyi aday gap_fade (`g=0.02`, çıkış=stop_atr=2.0,trail_atr=3.0): S1 — 3y +0%, 5y +0%, full +5%; 1 işlem (zararlı: 3y, 5y).
- **LTC/USDT**: 53 aday denendi, 0 kaldı. En iyi aday bb_squeeze (`n=20,q=0.1,look=126`, çıkış=stop_atr=2.0,trail_atr=3.0): S1 — 3y -34%, 5y -58%, full -2%; 270 işlem (zararlı: 3y, 5y, full).
- **MANA/USDT**: 58 aday denendi, 0 kaldı. En iyi aday price_ma (`kind=sma,n=100`, filtre=regime_bench200 · çıkış=stop_atr=2.0,tp_r=3.0): S2 — PF 1.551, 1x maks. düşüş -53%.
- **MINA/USDT**: 59 aday denendi, 1 kaldı. En iyi aday ma_cross (`kind=ema,pair=(50, 150)`, filtre=regime_bench200 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0): OK — tüm adımlar geçti.
- **NEAR/USDT**: 53 aday denendi, 0 kaldı. En iyi aday force_index (`n=2`, çıkış=stop_atr=2.0,trail_atr=3.0): S1 — 3y -33%, 5y -79%, full +71%; 1055 işlem (zararlı: 3y, 5y).
- **OP/USDT**: 58 aday denendi, 5 kaldı. En iyi aday bollinger_breakout (`n=50,k=2.5`, filtre=trend_sma200 · çıkış=stop_atr=2.0,max_hold=10): OK — tüm adımlar geçti.
- **PYTH/USDT**: elendi (S0: 2.9 yıl veri var, en az 3.0 yıl gerekli).
- **SAND/USDT**: 78 aday denendi, 2 kaldı. En iyi aday bollinger_breakout (`n=50,k=2.5`, filtre=adx20 · çıkış=stop_atr=2.0,max_hold=10): OK — tüm adımlar geçti.
- **SNX/USDT**: 54 aday denendi, 0 kaldı. En iyi aday bb_squeeze (`n=20,q=0.1,look=252`, filtre=low_vol · çıkış=stop_atr=2.0,tp_r=3.0): S2 — PF 1.43, 1x maks. düşüş -42%.
- **SOL/USDT**: 66 aday denendi, 5 kaldı. En iyi aday high_52w_break (`n=126,exit_ma=50`, filtre=regime_bench200 · çıkış=stop_atr=2.0,be_r=1.0): OK — tüm adımlar geçti.
- **SUI/USDT**: 67 aday denendi, 1 kaldı. En iyi aday roc_breakout (`n=252,th=10`, filtre=adx20 · çıkış=stop_atr=2.0,tp_r=3.0): OK — tüm adımlar geçti.
- **THETA/USDT**: 53 aday denendi, 0 kaldı. En iyi aday cci_breakout (`n=40,level=100`, çıkış=stop_atr=2.0,trail_atr=3.0): S1 — 3y -11%, 5y -56%, full -85%; 687 işlem (zararlı: 3y, 5y, full).
- **TRX/USDT**: 54 aday denendi, 0 kaldı. En iyi aday wavetrend_reversal (`n1=9,n2=26,lo=-60`, çıkış=stop_atr=2.0,trail_atr=3.0): S2 — PF 1.654, 1x maks. düşüş -49%.
- **UNI/USDT**: 57 aday denendi, 1 kaldı. En iyi aday bollinger_breakout (`n=50,k=2.5`, filtre=low_vol · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0): OK — tüm adımlar geçti.
- **XLM/USDT**: 84 aday denendi, 4 kaldı. En iyi aday high_52w_break (`n=126,exit_ma=50`, çıkış=stop_atr=2.0,trail_atr=3.0): OK — tüm adımlar geçti.
- **XRP/USDT**: 58 aday denendi, 2 kaldı. En iyi aday high_52w_break (`n=126,exit_ma=50`, filtre=regime_bench200 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0): OK — tüm adımlar geçti.

## Zayıf yönler (dürüst liste)

- 25971 deneme yapıldı. Bu kadar çok denemede şans eseri iyi görünen strateji çıkar. DSR bunu düzeltir; tier A sadece DSR ≥ eşik olanlardır.
- Seçim ve test aynı geçmiş veride yapıldı. Gerçek test arenadaki ileri (paper) kayıttır.
- Survivorship: liste bugünün coinlerinden oluşur. Borsadan silinen coinler yok, bu sonucu iyimser yapar.
- Funding sabit yıllık oranla, likidasyon işlem bazında yaklaşık modellenir.
- Tek borsa verisi (Bitget, yoksa OKX/KuCoin). Emir defteri ve piyasa etkisi modellenmez.

## Arena

Arena: 56 aktif (eleme geçen), 44 kontrol (yakın aday, switcher kullanmaz), 7 yeni üye, 0 kontrolden aktife. Üst sınır 100.

## Switcher backtest kapısı

Geçti: **False** — kontroller: `{"beats_equal_weight_all_windows": false, "positive_at_cost_stress": true, "max_dd_ok": true}`

Pencereler: `{"3y": {"sharpe": 1.191, "ew_sharpe": 2.92}, "5y": {"sharpe": 0.953, "ew_sharpe": 2.422}, "full": {"sharpe": 1.045, "ew_sharpe": 2.114}}`
