# Eleme motoru — crypto_alts 4h

Veri: 2018-01-11 → 2026-10-18. Coin: 34 uygun (toplam 35). Denenen varyant: 553 × coin = **31798 deneme**.
Her (coin, kural) için tek en iyi nokta değil, **en sağlam bölgenin merkezi** seçildi. Bu bir aday listesidir, karar değildir. Karar sadece doğrulama kapısında verilir.

## Huni

| Adım | Ne kontrol edilir | Elenen | Kalan |
|---|---|---|---|
| S0 | veri yetersiz | 62 | 2108 |
| S1 | her dönemde kârlı değil / az işlem | 1946 | 162 |
| S2 | kâr faktörü veya düşüş zayıf | 134 | 28 |
| S3 | yüksek maliyette zarar | 2 | 26 |
| S4 | plato yok (komşu ayarlar zararda) | 8 | 18 |
| S5 | 1 bar gecikmeye dayanıksız | 2 | 16 |
| S6 | yılların çoğunda kârlı değil | 3 | 13 |
| S7 | istatistiksel güven düşük (PSR) | 4 | 9 |

## 2. aşama: filtre × çıkış × kombo (sadece S1'i geçen adaylarda)

162 aday → 12996 ek deneme (DSR'a eklendi). Her aday için en sağlam filtre/çıkış hücresi ve en sağlam kombo seçildi; kombo sadece kuralı tek başına geçerse aday olur. Seçilenler aynı S1–S7 adımlarından geçti.

| Adım | Ne kontrol edilir | Elenen | Kalan |
|---|---|---|---|
| S0 | veri yetersiz | 0 | 293 |
| S1 | her dönemde kârlı değil / az işlem | 77 | 216 |
| S2 | kâr faktörü veya düşüş zayıf | 99 | 117 |
| S3 | yüksek maliyette zarar | 0 | 117 |
| S4 | plato yok (komşu ayarlar zararda) | 39 | 78 |
| S5 | 1 bar gecikmeye dayanıksız | 7 | 71 |
| S6 | yılların çoğunda kârlı değil | 9 | 62 |
| S7 | istatistiksel güven düşük (PSR) | 2 | 60 |

## Geçenler (69)

| Tier | Aşama | Coin | Kural | Ayar | Varyant | 3y | 5y | Tüm | Sharpe | 1x DD | PF | DSR |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| B | 2 | SUI/USDT | roc_breakout | `n=252,th=10` | filtre=adx20 · çıkış=stop_atr=2.0,tp_r=3.0 | +767% | veri yok | +1205% | 1.798 | -30% | 2.805 | 0.055 |
| B | 2 | ARB/USDT | price_ma | `kind=kama,n=200` | filtre=trend_sma200 · çıkış=trail_atr=3.0 | +993% | veri yok | +1095% | 1.572 | -32% | 2.104 | 0.015 |
| B | 2 | ARB/USDT | macd_zero | `cfg=(12, 26, 9)` | filtre=regime_bench200 · çıkış=stop_atr=2.0,tp_r=3.0 | +663% | veri yok | +690% | 1.487 | -40% | 1.779 | 0.012 |
| B | 2 | ARB/USDT | smc_bos | `k=8` | filtre=trend_sma200 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +543% | veri yok | +571% | 1.472 | -36% | 1.793 | 0.011 |
| B | 2 | ARB/USDT | bollinger_breakout | `n=50,k=2.5` | filtre=low_vol · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +109% | veri yok | +145% | 1.307 | -19% | 2.493 | 0.004 |
| B | 2 | ARB/USDT | bb_squeeze | `n=20,q=0.1,look=126` | filtre=low_vol · çıkış=stop_atr=2.0,max_hold=10 | +183% | veri yok | +214% | 1.307 | -23% | 2.035 | 0.004 |
| B | 2 | ARB/USDT | linreg_slope | `n=20,th=0.0005` | filtre=htf_week_sma10 · çıkış=stop_atr=2.0,tp_r=3.0 | +770% | veri yok | +632% | 1.296 | -35% | 1.607 | 0.004 |
| B | 2 | ARB/USDT | smc_choch | `k=8` | filtre=trend_sma200 · çıkış=stop_atr=2.0,tp_r=3.0 | +423% | veri yok | +500% | 1.291 | -32% | 1.88 | 0.004 |
| B | 2 | ARB/USDT | triple_ma | `set=(10, 50, 200),kind=ema` | filtre=htf_week_sma10 · çıkış=stop_atr=2.0,tp_r=3.0 | +403% | veri yok | +439% | 1.272 | -34% | 1.775 | 0.004 |
| B | 2 | SOL/USDT | high_52w_break | `n=126,exit_ma=50` | filtre=regime_bench200 · çıkış=stop_atr=2.0,be_r=1.0 | +251% | +398% | +1747% | 1.414 | -33% | 4.883 | 0.002 |
| B | 2 | OP/USDT | bollinger_breakout | `n=50,k=2.5` | filtre=trend_sma200 · çıkış=stop_atr=2.0,max_hold=10 | +306% | veri yok | +981% | 1.379 | -30% | 2.344 | 0.002 |
| B | 1 | XLM/USDT | high_52w_break | `n=126,exit_ma=50` | çıkış=stop_atr=2.0,trail_atr=3.0 | +244% | veri yok | +244% | 1.181 | -26% | 3.898 | 0.001 |
| B | 2 | ARB/USDT | macd_divergence | `k=3,fast=12,slow=26` | filtre=regime_bench200 · çıkış=stop_atr=2.0,trail_atr=3.0 | +260% | veri yok | +243% | 1.055 | -30% | 1.916 | 0.001 |
| B | 2 | ARB/USDT | macd_zero | `cfg=(12, 26, 9)` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=roc_breakout(≤5 bar) | +159% | veri yok | +239% | 1.046 | -30% | 2.488 | 0.001 |
| B | 2 | ARB/USDT | ma_cross | `kind=sma,pair=(10, 30)` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=roc_breakout(≤3 bar) | +261% | veri yok | +212% | 1.039 | -31% | 2.938 | 0.001 |
| B | 2 | XLM/USDT | ma_cross | `kind=ema,pair=(20, 50)` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_fvg(≤3 bar) | +134% | veri yok | +128% | 1.023 | -22% | 2.709 | 0.001 |
| B | 2 | ETH/USDT | bollinger_breakout | `n=50,k=2.5` | filtre=regime_bench200 · çıkış=trail_atr=3.0 | +358% | +718% | +4439% | 1.307 | -32% | 2.405 | 0.0 |
| B | 2 | ETH/USDT | bollinger_breakout | `n=50,k=2.5` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_bos(≤5 bar) | +286% | +482% | +3642% | 1.284 | -31% | 2.317 | 0.0 |
| B | 2 | XRP/USDT | high_52w_break | `n=126,exit_ma=50` | filtre=regime_bench200 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +107% | +150% | +603% | 1.259 | -21% | 2.898 | 0.0 |
| B | 2 | SOL/USDT | cci_breakout | `n=40,level=150` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=ma_cross(≤3 bar) | +113% | +414% | +568% | 1.21 | -35% | 2.728 | 0.0 |
| B | 2 | FIL/USDT | linreg_slope | `n=20,th=0.001` | filtre=regime_bench200 · çıkış=stop_atr=2.0,max_hold=10 | +501% | +635% | +1007% | 1.2 | -39% | 1.62 | 0.0 |
| B | 2 | SOL/USDT | high_52w_break | `n=126,exit_ma=50` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=chop_switch(≤0 bar) | +113% | +218% | +425% | 1.181 | -27% | 3.667 | 0.0 |
| B | 2 | ETH/USDT | rsi_midline | `n=28,level=60` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=bollinger_breakout(≤3 bar) | +307% | +284% | +2116% | 1.154 | -38% | 2.053 | 0.0 |
| B | 1 | ETH/USDT | bollinger_breakout | `n=50,k=2.5` | çıkış=stop_atr=2.0,trail_atr=3.0 | +322% | +421% | +2869% | 1.153 | -34% | 1.986 | 0.0 |
| B | 2 | SOL/USDT | donchian_breakout | `entry=100,exit=10` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=ma_cross(≤5 bar) | +122% | +228% | +425% | 1.1 | -33% | 2.61 | 0.0 |
| B | 2 | ADA/USDT | bollinger_breakout | `n=20,k=2.5` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=chop_switch(≤0 bar) | +117% | veri yok | +208% | 1.1 | -29% | 3.848 | 0.0 |
| B | 2 | OP/USDT | cmf_flow | `n=40,th=0.2` | filtre=low_vol · çıkış=stop_atr=2.0,tp_r=3.0 | +98% | veri yok | +175% | 1.098 | -39% | 2.137 | 0.0 |
| B | 2 | SAND/USDT | bollinger_breakout | `n=50,k=2.5` | filtre=adx20 · çıkış=stop_atr=2.0,max_hold=10 | +192% | veri yok | +778% | 1.067 | -39% | 2.01 | 0.0 |
| B | 2 | ETH/USDT | high_52w_break | `n=126,exit_ma=50` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=chop_switch(≤5 bar) | +93% | +80% | +552% | 1.047 | -23% | 2.765 | 0.0 |
| B | 2 | ETH/USDT | high_52w_break | `n=126,exit_ma=50` | filtre=low_vol · çıkış=signal_only | +74% | +106% | +700% | 0.979 | -33% | 2.656 | 0.0 |
| B | 1 | ARB/USDT | hurst_switch | `n=200,fast=20,rsi_n=5` | çıkış=stop_atr=2.0,trail_atr=3.0 | +143% | veri yok | +135% | 0.959 | -31% | 2.171 | 0.0 |
| B | 1 | XRP/USDT | high_52w_break | `n=126,exit_ma=50` | çıkış=stop_atr=2.0,trail_atr=3.0 | +141% | +157% | +740% | 0.957 | -39% | 2.54 | 0.0 |
| B | 2 | FIL/USDT | ma_cross | `kind=dema,pair=(20, 100)` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_order_block(≤3 bar) | +206% | +360% | +346% | 0.953 | -33% | 2.353 | 0.0 |
| B | 2 | ADA/USDT | smc_choch | `k=8` | filtre=htf_week_sma10 · çıkış=stop_atr=2.0,tp_r=3.0 | +114% | veri yok | +237% | 0.93 | -37% | 1.796 | 0.0 |
| B | 2 | ADA/USDT | high_52w_break | `n=126,exit_ma=50` | filtre=adx20 · çıkış=stop_atr=2.0,be_r=1.0 | +323% | veri yok | +239% | 0.922 | -38% | 3.504 | 0.0 |
| B | 2 | ADA/USDT | cci_breakout | `n=40,level=100` | filtre=low_vol · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +132% | veri yok | +200% | 0.909 | -37% | 1.406 | 0.0 |
| B | 2 | SAND/USDT | ichimoku_cloud | `cfg=(20, 60, 120)` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_fvg(≤0 bar) | +85% | veri yok | +146% | 0.899 | -34% | 2.785 | 0.0 |
| B | 2 | ADA/USDT | roc_breakout | `n=252,th=5` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_bos(≤3 bar) | +121% | veri yok | +111% | 0.892 | -38% | 2.31 | 0.0 |
| B | 2 | DOT/USDT | rsi_divergence | `n=14,k=3,exit_level=70` | filtre=trend_sma200 · çıkış=stop_atr=2.0,max_hold=10 | +88% | +88% | +121% | 0.873 | -19% | 1.935 | 0.0 |
| B | 2 | ARB/USDT | cci_breakout | `n=40,level=150` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_choch(≤3 bar) | +244% | veri yok | +201% | 0.867 | -32% | 1.705 | 0.0 |
| B | 2 | OP/USDT | bollinger_breakout | `n=50,k=2.5` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=roc_breakout(≤5 bar) | +164% | veri yok | +218% | 0.857 | -29% | 2.138 | 0.0 |
| B | 2 | INJ/USDT | roc_breakout | `n=252,th=5` | filtre=htf_week_sma10 · çıkış=stop_atr=2.0,max_hold=10 | +63% | veri yok | +121% | 0.85 | -33% | 1.515 | 0.0 |
| B | 2 | SAND/USDT | rsi_midline | `n=28,level=55` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_choch(≤0 bar) | +74% | veri yok | +229% | 0.835 | -39% | 1.832 | 0.0 |
| B | 2 | INJ/USDT | volume_breakout | `n=50,rv=3.0` | filtre=htf_week_sma10 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +74% | veri yok | +127% | 0.83 | -36% | 1.979 | 0.0 |
| B | 2 | BNB/USDT | donchian_breakout | `entry=100,exit=10` | filtre=htf_week_sma10 · çıkış=trail_atr=3.0 | +89% | veri yok | +91% | 0.829 | -22% | 1.845 | 0.0 |
| B | 2 | DOT/USDT | rsi_divergence | `n=14,k=3,exit_level=70` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_order_block(≤5 bar) | +68% | +104% | +130% | 0.825 | -29% | 2.035 | 0.0 |
| B | 2 | BNB/USDT | donchian_breakout | `entry=100,exit=10` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=ma_cross(≤5 bar) | +73% | veri yok | +56% | 0.819 | -12% | 2.378 | 0.0 |
| B | 2 | DOT/USDT | bb_squeeze | `n=20,q=0.1,look=252` | filtre=htf_week_sma10 · çıkış=stop_atr=2.0,tp_r=3.0 | +19% | +24% | +194% | 0.811 | -37% | 1.87 | 0.0 |
| B | 2 | SAND/USDT | macd_divergence | `k=3,fast=12,slow=26` | filtre=regime_bench200 · çıkış=stop_atr=2.0,max_hold=10 | +140% | veri yok | +196% | 0.8 | -27% | 1.791 | 0.0 |
| B | 2 | DOT/USDT | bb_squeeze | `n=20,q=0.1,look=252` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=ma_cross(≤3 bar) | +23% | +47% | +172% | 0.794 | -33% | 3.184 | 0.0 |
| B | 2 | SAND/USDT | ppo_cross | `cfg=(12, 26, 9)` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=bollinger_breakout(≤5 bar) | +40% | veri yok | +178% | 0.789 | -34% | 2.046 | 0.0 |
| B | 1 | ETH/USDT | keltner_breakout | `n=20,k=2.5` | çıkış=stop_atr=2.0,trail_atr=3.0 | +75% | +93% | +674% | 0.785 | -38% | 1.601 | 0.0 |
| B | 2 | AXS/USDT | roc_breakout | `n=252,th=5` | filtre=trend_sma200 · çıkış=trail_atr=3.0 | +67% | +224% | +224% | 0.775 | -35% | 1.789 | 0.0 |
| B | 2 | XLM/USDT | cci_breakout | `n=40,level=100` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=ma_cross(≤3 bar) | +57% | veri yok | +74% | 0.733 | -27% | 1.759 | 0.0 |
| B | 2 | SAND/USDT | rsi_divergence | `n=14,k=3,exit_level=70` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_ote(≤3 bar) | +169% | veri yok | +104% | 0.73 | -34% | 2.137 | 0.0 |
| B | 2 | BTC/USDT | bollinger_breakout | `n=50,k=2.0` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=chop_switch(≤0 bar) | +66% | +70% | +140% | 0.717 | -22% | 1.976 | 0.0 |
| B | 2 | OP/USDT | trix_cross | `n=21,signal=7` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=macd_divergence(≤3 bar) | +84% | veri yok | +104% | 0.707 | -28% | 2.277 | 0.0 |
| B | 2 | ETH/USDT | volume_breakout | `n=50,rv=2.0` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=roc_breakout(≤5 bar) | +59% | +62% | +162% | 0.665 | -25% | 2.782 | 0.0 |
| B | 1 | SOL/USDT | volume_breakout | `n=50,rv=1.5` | çıkış=stop_atr=2.0,trail_atr=3.0 | +98% | +158% | +196% | 0.659 | -40% | 1.585 | 0.0 |
| B | 1 | ETH/USDT | high_52w_break | `n=126,exit_ma=50` | çıkış=stop_atr=2.0,trail_atr=3.0 | +44% | +29% | +244% | 0.658 | -31% | 1.642 | 0.0 |
| B | 1 | ETH/USDT | volume_breakout | `n=50,rv=2.0` | çıkış=stop_atr=2.0,trail_atr=3.0 | +111% | +102% | +207% | 0.641 | -30% | 1.921 | 0.0 |
| B | 2 | SAND/USDT | rsi_divergence | `n=14,k=3,exit_level=70` | filtre=low_vol · çıkış=stop_atr=2.0,max_hold=10 | +45% | veri yok | +76% | 0.626 | -35% | 1.474 | 0.0 |
| B | 2 | OP/USDT | adx_trend | `n=20,th=25` | filtre=adx20 · çıkış=trail_atr=3.0 | +10% | veri yok | +109% | 0.624 | -36% | 1.757 | 0.0 |
| B | 2 | BTC/USDT | keltner_breakout | `n=20,k=2.5` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_fvg(≤5 bar) | +101% | +129% | +163% | 0.614 | -37% | 1.621 | 0.0 |
| B | 2 | LINK/USDT | bb_squeeze | `n=20,q=0.1,look=252` | filtre=low_vol · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +2% | +86% | +91% | 0.61 | -36% | 1.379 | 0.0 |
| B | 1 | OP/USDT | cmf_flow | `n=40,th=0.2` | çıkış=stop_atr=2.0,trail_atr=3.0 | +115% | veri yok | +110% | 0.609 | -39% | 1.549 | 0.0 |
| B | 2 | UNI/USDT | bollinger_breakout | `n=50,k=2.5` | filtre=low_vol · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +84% | +117% | +88% | 0.606 | -30% | 1.468 | 0.0 |
| B | 2 | DOGE/USDT | macd_divergence | `k=3,fast=12,slow=26` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=wavetrend_reversal(≤3 bar) | +61% | +94% | +103% | 0.595 | -38% | 2.09 | 0.0 |
| B | 2 | ALGO/USDT | bb_squeeze | `n=20,q=0.2,look=252` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=ma_cross(≤3 bar) | +67% | +59% | +96% | 0.482 | -34% | 1.909 | 0.0 |

## Coin coin özet (ajan günlüğü)

- **AAVE/USDT**: 64 aday denendi, 0 kaldı. En iyi aday coppock_turn (`scale=5`, çıkış=stop_atr=2.0,tp_r=3.0): S2 — PF 1.335, 1x maks. düşüş -63%.
- **ADA/USDT**: 94 aday denendi, 5 kaldı. En iyi aday bollinger_breakout (`n=20,k=2.5`, çıkış=stop_atr=2.0,trail_atr=3.0 · onay=chop_switch(≤0 bar)): OK — tüm adımlar geçti.
- **ALGO/USDT**: 66 aday denendi, 1 kaldı. En iyi aday bb_squeeze (`n=20,q=0.2,look=252`, çıkış=stop_atr=2.0,trail_atr=3.0 · onay=ma_cross(≤3 bar)): OK — tüm adımlar geçti.
- **APT/USDT**: 64 aday denendi, 0 kaldı. En iyi aday cmf_flow (`n=20,th=0.05`, çıkış=stop_atr=2.0,trail_atr=3.0 · onay=bollinger_breakout(≤3 bar)): S4 — komşu ayarların %33'i kârlı.
- **ARB/USDT**: 97 aday denendi, 13 kaldı. En iyi aday price_ma (`kind=kama,n=200`, filtre=trend_sma200 · çıkış=trail_atr=3.0): OK — tüm adımlar geçti.
- **ATOM/USDT**: 66 aday denendi, 0 kaldı. En iyi aday chop_switch (`n=14,lo=38.2,hi=61.8`, filtre=low_vol · çıkış=stop_atr=2.0,max_hold=10): S4 — komşu ayar yok.
- **AVAX/USDT**: 64 aday denendi, 0 kaldı. En iyi aday roc_breakout (`n=63,th=5`, filtre=low_vol · çıkış=stop_atr=2.0,be_r=1.0): S2 — PF 2.558, 1x maks. düşüş -55%.
- **AXS/USDT**: 64 aday denendi, 1 kaldı. En iyi aday roc_breakout (`n=252,th=5`, filtre=trend_sma200 · çıkış=trail_atr=3.0): OK — tüm adımlar geçti.
- **BCH/USDT**: 64 aday denendi, 0 kaldı. En iyi aday coppock_turn (`scale=5`, filtre=low_vol · çıkış=stop_atr=2.0,be_r=1.0): S2 — PF 1.926, 1x maks. düşüş -47%.
- **BNB/USDT**: 76 aday denendi, 2 kaldı. En iyi aday donchian_breakout (`entry=100,exit=10`, filtre=htf_week_sma10 · çıkış=trail_atr=3.0): OK — tüm adımlar geçti.
- **BTC/USDT**: 73 aday denendi, 2 kaldı. En iyi aday bollinger_breakout (`n=50,k=2.0`, çıkış=stop_atr=2.0,trail_atr=3.0 · onay=chop_switch(≤0 bar)): OK — tüm adımlar geçti.
- **CRV/USDT**: 62 aday denendi, 0 kaldı. En iyi aday trix_cross (`n=12,signal=7`, çıkış=stop_atr=2.0,trail_atr=3.0): S1 — 3y -95%, 5y -90%, full -90%; 782 işlem (zararlı: 3y, 5y, full).
- **DOGE/USDT**: 69 aday denendi, 1 kaldı. En iyi aday macd_divergence (`k=3,fast=12,slow=26`, çıkış=stop_atr=2.0,trail_atr=3.0 · onay=wavetrend_reversal(≤3 bar)): OK — tüm adımlar geçti.
- **DOT/USDT**: 68 aday denendi, 4 kaldı. En iyi aday rsi_divergence (`n=14,k=3,exit_level=70`, filtre=trend_sma200 · çıkış=stop_atr=2.0,max_hold=10): OK — tüm adımlar geçti.
- **ETC/USDT**: 64 aday denendi, 0 kaldı. En iyi aday coppock_turn (`scale=5`, filtre=trend_sma200 · çıkış=stop_atr=2.0,be_r=1.0): S6 — yılların %56'i kârlı.
- **ETH/USDT**: 77 aday denendi, 10 kaldı. En iyi aday bollinger_breakout (`n=50,k=2.5`, filtre=regime_bench200 · çıkış=trail_atr=3.0): OK — tüm adımlar geçti.
- **FIL/USDT**: 72 aday denendi, 2 kaldı. En iyi aday linreg_slope (`n=20,th=0.001`, filtre=regime_bench200 · çıkış=stop_atr=2.0,max_hold=10): OK — tüm adımlar geçti.
- **IMX/USDT**: 64 aday denendi, 0 kaldı. En iyi aday hurst_switch (`n=200,fast=20,rsi_n=5`, çıkış=stop_atr=2.0,trail_atr=3.0): S2 — PF 1.423, 1x maks. düşüş -47%.
- **INJ/USDT**: 70 aday denendi, 2 kaldı. En iyi aday roc_breakout (`n=252,th=5`, filtre=htf_week_sma10 · çıkış=stop_atr=2.0,max_hold=10): OK — tüm adımlar geçti.
- **LINK/USDT**: 64 aday denendi, 1 kaldı. En iyi aday bb_squeeze (`n=20,q=0.1,look=252`, filtre=low_vol · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0): OK — tüm adımlar geçti.
- **LTC/USDT**: 62 aday denendi, 0 kaldı. En iyi aday bb_squeeze (`n=20,q=0.1,look=126`, çıkış=stop_atr=2.0,trail_atr=3.0): S1 — 3y -34%, 5y -58%, full -2%; 270 işlem (zararlı: 3y, 5y, full).
- **MANA/USDT**: 69 aday denendi, 0 kaldı. En iyi aday price_ma (`kind=sma,n=100`, filtre=regime_bench200 · çıkış=stop_atr=2.0,tp_r=3.0): S2 — PF 1.551, 1x maks. düşüş -53%.
- **MINA/USDT**: 66 aday denendi, 0 kaldı. En iyi aday atr_breakout (`n=20,k=2.0`, çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_liquidity_sweep(≤3 bar)): S4 — komşu ayarların %0'i kârlı.
- **NEAR/USDT**: 62 aday denendi, 0 kaldı. En iyi aday force_index (`n=2`, çıkış=stop_atr=2.0,trail_atr=3.0): S1 — 3y -33%, 5y -79%, full +71%; 1055 işlem (zararlı: 3y, 5y).
- **OP/USDT**: 70 aday denendi, 6 kaldı. En iyi aday bollinger_breakout (`n=50,k=2.5`, filtre=trend_sma200 · çıkış=stop_atr=2.0,max_hold=10): OK — tüm adımlar geçti.
- **PYTH/USDT**: elendi (S0: 2.9 yıl veri var, en az 3.0 yıl gerekli).
- **SAND/USDT**: 92 aday denendi, 7 kaldı. En iyi aday bollinger_breakout (`n=50,k=2.5`, filtre=adx20 · çıkış=stop_atr=2.0,max_hold=10): OK — tüm adımlar geçti.
- **SNX/USDT**: 64 aday denendi, 0 kaldı. En iyi aday bb_squeeze (`n=20,q=0.1,look=252`, filtre=low_vol · çıkış=stop_atr=2.0,tp_r=3.0): S2 — PF 1.43, 1x maks. düşüş -42%.
- **SOL/USDT**: 77 aday denendi, 5 kaldı. En iyi aday high_52w_break (`n=126,exit_ma=50`, filtre=regime_bench200 · çıkış=stop_atr=2.0,be_r=1.0): OK — tüm adımlar geçti.
- **SUI/USDT**: 77 aday denendi, 1 kaldı. En iyi aday roc_breakout (`n=252,th=10`, filtre=adx20 · çıkış=stop_atr=2.0,tp_r=3.0): OK — tüm adımlar geçti.
- **THETA/USDT**: 62 aday denendi, 0 kaldı. En iyi aday cci_breakout (`n=40,level=100`, çıkış=stop_atr=2.0,trail_atr=3.0): S1 — 3y -6%, 5y -54%, full -84%; 687 işlem (zararlı: 3y, 5y, full).
- **TRX/USDT**: 63 aday denendi, 0 kaldı. En iyi aday wavetrend_reversal (`n1=9,n2=26,lo=-60`, çıkış=stop_atr=2.0,trail_atr=3.0): S2 — PF 1.654, 1x maks. düşüş -49%.
- **UNI/USDT**: 68 aday denendi, 1 kaldı. En iyi aday bollinger_breakout (`n=50,k=2.5`, filtre=low_vol · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0): OK — tüm adımlar geçti.
- **XLM/USDT**: 100 aday denendi, 3 kaldı. En iyi aday high_52w_break (`n=126,exit_ma=50`, çıkış=stop_atr=2.0,trail_atr=3.0): OK — tüm adımlar geçti.
- **XRP/USDT**: 67 aday denendi, 2 kaldı. En iyi aday high_52w_break (`n=126,exit_ma=50`, filtre=regime_bench200 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0): OK — tüm adımlar geçti.

## Zayıf yönler (dürüst liste)

- 31798 deneme yapıldı. Bu kadar çok denemede şans eseri iyi görünen strateji çıkar. DSR bunu düzeltir; tier A sadece DSR ≥ eşik olanlardır.
- Seçim ve test aynı geçmiş veride yapıldı. Gerçek test arenadaki ileri (paper) kayıttır.
- Survivorship: liste bugünün coinlerinden oluşur. Borsadan silinen coinler yok, bu sonucu iyimser yapar.
- Funding sabit yıllık oranla, likidasyon işlem bazında yaklaşık modellenir.
- Tek borsa verisi (Bitget, yoksa OKX/KuCoin). Emir defteri ve piyasa etkisi modellenmez.

## Arena

Arena: 77 aktif (eleme geçen), 23 kontrol (yakın aday, switcher kullanmaz), 21 yeni üye, 0 kontrolden aktife. Üst sınır 100.

## Switcher backtest kapısı

Geçti: **False** — kontroller: `{"beats_equal_weight_all_windows": false, "positive_at_cost_stress": true, "max_dd_ok": true}`

Pencereler: `{"3y": {"sharpe": 1.049, "ew_sharpe": 3.022}, "5y": {"sharpe": 0.847, "ew_sharpe": 2.57}, "full": {"sharpe": 0.975, "ew_sharpe": 2.142}}`
