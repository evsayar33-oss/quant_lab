# Eleme motoru — crypto_alts 4h

Veri: 2018-01-11 → 2026-10-20. Coin: 34 uygun (toplam 35). Denenen varyant: 553 × coin = **34426 deneme**.
Her (coin, kural) için tek en iyi nokta değil, **en sağlam bölgenin merkezi** seçildi. Bu bir aday listesidir, karar değildir. Karar sadece doğrulama kapısında verilir.

## Huni

| Adım | Ne kontrol edilir | Elenen | Kalan |
|---|---|---|---|
| S0 | veri yetersiz | 62 | 2108 |
| S1 | her dönemde kârlı değil / az işlem | 1913 | 195 |
| S2 | kâr faktörü veya düşüş zayıf | 162 | 33 |
| S3 | yüksek maliyette zarar | 6 | 27 |
| S4 | plato yok (komşu ayarlar zararda) | 3 | 24 |
| S5 | 1 bar gecikmeye dayanıksız | 3 | 21 |
| S6 | yılların çoğunda kârlı değil | 9 | 12 |
| S7 | istatistiksel güven düşük (PSR) | 3 | 9 |

## 2. aşama: filtre × çıkış × kombo (sadece S1'i geçen adaylarda)

195 aday → 15624 ek deneme (DSR'a eklendi). Her aday için en sağlam filtre/çıkış hücresi ve en sağlam kombo seçildi; kombo sadece kuralı tek başına geçerse aday olur. Seçilenler aynı S1–S7 adımlarından geçti.

| Adım | Ne kontrol edilir | Elenen | Kalan |
|---|---|---|---|
| S0 | veri yetersiz | 0 | 336 |
| S1 | her dönemde kârlı değil / az işlem | 82 | 254 |
| S2 | kâr faktörü veya düşüş zayıf | 67 | 187 |
| S3 | yüksek maliyette zarar | 0 | 187 |
| S4 | plato yok (komşu ayarlar zararda) | 40 | 147 |
| S5 | 1 bar gecikmeye dayanıksız | 9 | 138 |
| S6 | yılların çoğunda kârlı değil | 13 | 125 |
| S7 | istatistiksel güven düşük (PSR) | 10 | 115 |

## Geçenler (124)

| Tier | Aşama | Coin | Kural | Ayar | Varyant | 3y | 5y | Tüm | Sharpe | 1x DD | PF | DSR |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| B | 2 | ARB/USDT | price_ma | `kind=kama,n=200` | filtre=trend_sma200 · çıkış=stop_atr=2.0,tp_r=3.0 | +720% | veri yok | +802% | 1.944 | -39% | 2.432 | 0.23 |
| B | 2 | ARB/USDT | smc_bos | `k=2` | filtre=low_vol · çıkış=stop_atr=2.0,tp_r=3.0 | +634% | veri yok | +910% | 1.836 | -35% | 2.113 | 0.166 |
| B | 2 | ARB/USDT | roc_breakout | `n=63,th=0` | filtre=trend_sma200 · çıkış=stop_atr=2.0,tp_r=3.0 | +440% | veri yok | +591% | 1.689 | -23% | 2.394 | 0.107 |
| B | 2 | ARB/USDT | ppo_cross | `cfg=(12, 26, 9)` | filtre=low_vol · çıkış=stop_atr=2.0,tp_r=3.0 | +413% | veri yok | +698% | 1.669 | -36% | 1.896 | 0.104 |
| B | 2 | ARB/USDT | cci_breakout | `n=14,level=100` | filtre=low_vol · çıkış=stop_atr=2.0,tp_r=3.0 | +600% | veri yok | +613% | 1.585 | -29% | 1.804 | 0.076 |
| B | 2 | ARB/USDT | keltner_breakout | `n=50,k=2.0` | filtre=low_vol · çıkış=stop_atr=2.0,max_hold=10 | +389% | veri yok | +455% | 1.629 | -27% | 2.421 | 0.071 |
| B | 2 | ARB/USDT | macd_cross | `cfg=(12, 26, 9),zero_filter=True` | filtre=low_vol · çıkış=stop_atr=2.0,tp_r=3.0 | +162% | veri yok | +283% | 1.344 | -34% | 2.121 | 0.032 |
| B | 2 | ARB/USDT | macd_cross | `cfg=(12, 26, 9),zero_filter=True` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_order_block(≤3 bar) | +208% | veri yok | +206% | 1.422 | -16% | 3.844 | 0.03 |
| B | 2 | ARB/USDT | vwap_cross | `n=50` | filtre=low_vol · çıkış=stop_atr=2.0,tp_r=3.0 | +228% | veri yok | +295% | 1.301 | -36% | 1.676 | 0.025 |
| B | 2 | ARB/USDT | inside_bar | `trend_n=50` | filtre=low_vol · çıkış=stop_atr=2.0,tp_r=3.0 | +280% | veri yok | +295% | 1.307 | -27% | 2.182 | 0.024 |
| B | 2 | ARB/USDT | trix_cross | `n=15,signal=7` | filtre=trend_sma200 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +190% | veri yok | +240% | 1.245 | -24% | 1.769 | 0.017 |
| B | 2 | ARB/USDT | awesome_zero | `fast=5,slow=34` | filtre=htf_week_sma10 · çıkış=stop_atr=2.0,tp_r=3.0 | +270% | veri yok | +322% | 1.209 | -32% | 1.799 | 0.016 |
| B | 2 | XLM/USDT | smc_bos | `k=2` | filtre=low_vol · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +126% | veri yok | +136% | 1.15 | -20% | 1.754 | 0.016 |
| B | 2 | ARB/USDT | aroon_cross | `n=14` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=roc_breakout(≤5 bar) | +223% | veri yok | +244% | 1.266 | -20% | 3.575 | 0.015 |
| B | 2 | APT/USDT | macd_zero | `cfg=(12, 26, 9)` | filtre=htf_week_sma10 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +87% | veri yok | +230% | 1.234 | -22% | 2.047 | 0.014 |
| B | 2 | ARB/USDT | smc_order_block | `k=3,max_age=50` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_liquidity_sweep(≤3 bar) | +169% | veri yok | +265% | 1.222 | -34% | 2.0 | 0.013 |
| B | 2 | ARB/USDT | donchian_breakout | `entry=40,exit=10` | filtre=low_vol · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +107% | veri yok | +129% | 1.212 | -14% | 3.169 | 0.012 |
| B | 2 | ARB/USDT | ppo_cross | `cfg=(12, 26, 9)` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_order_block(≤3 bar) | +255% | veri yok | +312% | 1.226 | -25% | 1.965 | 0.011 |
| B | 2 | ARB/USDT | ichimoku_cloud | `cfg=(7, 22, 44)` | filtre=low_vol · çıkış=stop_atr=2.0,tp_r=3.0 | +161% | veri yok | +199% | 1.159 | -26% | 1.743 | 0.011 |
| B | 2 | ARB/USDT | ma_cross | `kind=hma,pair=(20, 100)` | filtre=htf_week_sma10 · çıkış=stop_atr=2.0,tp_r=3.0 | +221% | veri yok | +280% | 1.141 | -40% | 1.784 | 0.011 |
| B | 2 | ARB/USDT | smc_choch | `k=3` | filtre=low_vol · çıkış=stop_atr=2.0,trail_atr=3.0 | +235% | veri yok | +266% | 1.175 | -24% | 2.231 | 0.01 |
| B | 2 | ARB/USDT | psar_flip | `cfg=(0.01, 0.1)` | filtre=low_vol · çıkış=trail_atr=3.0 | +268% | veri yok | +287% | 1.11 | -39% | 1.893 | 0.009 |
| B | 2 | XLM/USDT | roc_breakout | `n=126,th=0` | filtre=trend_sma200 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +70% | veri yok | +70% | 1.014 | -19% | 1.827 | 0.009 |
| B | 2 | AXS/USDT | macd_zero | `cfg=(5, 35, 5)` | filtre=low_vol · çıkış=stop_atr=2.0,tp_r=3.0 | +83% | +603% | +603% | 1.271 | -37% | 1.875 | 0.008 |
| B | 2 | ARB/USDT | smc_order_block | `k=3,max_age=50` | filtre=low_vol · çıkış=trail_atr=3.0 | +279% | veri yok | +360% | 1.107 | -38% | 1.528 | 0.008 |
| B | 2 | ARB/USDT | cmf_flow | `n=20,th=0.05` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_order_block(≤3 bar) | +122% | veri yok | +199% | 1.072 | -30% | 1.96 | 0.008 |
| B | 2 | XLM/USDT | macd_zero | `cfg=(5, 35, 5)` | filtre=low_vol · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +85% | veri yok | +82% | 0.984 | -13% | 1.783 | 0.008 |
| B | 2 | SAND/USDT | tsi_cross | `cfg=(25, 13, 7)` | filtre=low_vol · çıkış=stop_atr=2.0,max_hold=10 | +268% | +550% | +550% | 1.256 | -33% | 1.649 | 0.007 |
| B | 2 | OP/USDT | bb_squeeze | `n=20,q=0.2,look=252` | filtre=low_vol · çıkış=stop_atr=2.0,max_hold=10 | +103% | veri yok | +244% | 1.196 | -22% | 2.126 | 0.007 |
| B | 2 | OP/USDT | aroon_cross | `n=14` | filtre=low_vol · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +148% | veri yok | +370% | 1.16 | -32% | 1.602 | 0.007 |
| B | 2 | XLM/USDT | trix_cross | `n=21,signal=9` | filtre=low_vol · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +86% | veri yok | +75% | 0.963 | -22% | 1.834 | 0.007 |
| B | 2 | OP/USDT | vortex_cross | `n=28` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_ote(≤5 bar) | +217% | veri yok | +506% | 1.179 | -31% | 2.534 | 0.006 |
| B | 2 | ARB/USDT | linreg_slope | `n=20,th=0.001` | filtre=trend_sma200 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +200% | veri yok | +180% | 1.019 | -30% | 1.572 | 0.006 |
| B | 2 | XLM/USDT | awesome_zero | `fast=5,slow=34` | filtre=low_vol · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +80% | veri yok | +77% | 0.933 | -19% | 1.707 | 0.006 |
| B | 2 | AXS/USDT | trix_cross | `n=9,signal=7` | filtre=low_vol · çıkış=stop_atr=2.0,tp_r=3.0 | +127% | +602% | +602% | 1.181 | -38% | 1.595 | 0.005 |
| B | 2 | ADA/USDT | rsi_divergence | `n=14,k=3,exit_level=70` | filtre=htf_week_sma10 · çıkış=stop_atr=2.0,be_r=1.0 | +128% | veri yok | +213% | 1.151 | -31% | 2.116 | 0.005 |
| B | 2 | OP/USDT | ma_cross | `kind=dema,pair=(20, 50)` | filtre=low_vol · çıkış=stop_atr=2.0,tp_r=3.0 | +154% | veri yok | +335% | 1.103 | -32% | 1.847 | 0.005 |
| B | 2 | ARB/USDT | triple_ma | `set=(10, 50, 200),kind=ema` | filtre=adx20 · çıkış=stop_atr=2.0,tp_r=3.0 | +133% | veri yok | +129% | 0.965 | -21% | 2.195 | 0.005 |
| B | 2 | FIL/USDT | trix_cross | `n=9,signal=9` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_ote(≤5 bar) | +187% | +487% | +474% | 1.269 | -20% | 2.88 | 0.004 |
| B | 2 | SAND/USDT | ma_cross | `kind=dema,pair=(10, 50)` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=roc_breakout(≤3 bar) | +75% | +337% | +337% | 1.231 | -26% | 3.339 | 0.004 |
| B | 2 | DOGE/USDT | linreg_slope | `n=100,th=0.0005` | filtre=low_vol · çıkış=stop_atr=2.0,tp_r=3.0 | +133% | +207% | +337% | 1.22 | -29% | 2.886 | 0.004 |
| B | 2 | SAND/USDT | aroon_cross | `n=14` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=roc_breakout(≤3 bar) | +126% | +309% | +309% | 1.183 | -28% | 2.803 | 0.004 |
| B | 2 | ADA/USDT | trix_cross | `n=21,signal=9` | filtre=low_vol · çıkış=stop_atr=2.0,tp_r=3.0 | +56% | veri yok | +233% | 1.113 | -25% | 1.873 | 0.004 |
| B | 2 | APT/USDT | cmf_flow | `n=20,th=0.05` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_order_block(≤0 bar) | +71% | veri yok | +182% | 1.067 | -25% | 2.244 | 0.004 |
| B | 1 | ARB/USDT | donchian_breakout | `entry=40,exit=10` | çıkış=stop_atr=2.0,trail_atr=3.0 | +220% | veri yok | +263% | 1.008 | -25% | 2.213 | 0.004 |
| B | 2 | ARB/USDT | linreg_slope | `n=20,th=0.001` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=cmf_flow(≤5 bar) | +212% | veri yok | +186% | 0.984 | -25% | 2.385 | 0.004 |
| B | 2 | ARB/USDT | obv_trend | `n=20,price_n=50` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_order_block(≤3 bar) | +164% | veri yok | +190% | 0.944 | -37% | 1.596 | 0.004 |
| B | 2 | ARB/USDT | macd_zero | `cfg=(12, 26, 9)` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=cmf_flow(≤5 bar) | +124% | veri yok | +133% | 0.914 | -18% | 3.241 | 0.004 |
| B | 2 | UNI/USDT | supertrend_flip | `cfg=(14, 3.0)` | filtre=trend_sma200 · çıkış=stop_atr=2.0,tp_r=3.0 | +145% | +324% | +834% | 1.204 | -37% | 2.065 | 0.003 |
| B | 2 | SAND/USDT | ppo_cross | `cfg=(12, 26, 9)` | filtre=low_vol · çıkış=stop_atr=2.0,max_hold=10 | +283% | +400% | +400% | 1.123 | -35% | 1.558 | 0.003 |
| B | 2 | SAND/USDT | cci_breakout | `n=14,level=100` | filtre=low_vol · çıkış=stop_atr=2.0,tp_r=3.0 | +403% | +491% | +491% | 1.096 | -36% | 1.635 | 0.003 |
| B | 2 | ARB/USDT | vwap_cross | `n=50` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_liquidity_sweep(≤5 bar) | +152% | veri yok | +164% | 1.022 | -27% | 2.199 | 0.003 |
| B | 2 | ARB/USDT | bollinger_breakout | `n=50,k=2.5` | çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +106% | veri yok | +119% | 0.935 | -24% | 2.32 | 0.003 |
| B | 2 | XLM/USDT | smc_bos | `k=2` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_ote(≤5 bar) | +42% | veri yok | +55% | 0.772 | -17% | 2.512 | 0.003 |
| B | 2 | SAND/USDT | volume_breakout | `n=50,rv=1.5` | filtre=trend_sma200 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +122% | +234% | +234% | 1.092 | -17% | 2.999 | 0.002 |
| B | 2 | FIL/USDT | wavetrend_reversal | `n1=12,n2=21,lo=-40` | filtre=adx20 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +397% | +602% | +479% | 1.084 | -31% | 1.583 | 0.002 |
| B | 2 | SAND/USDT | aroon_cross | `n=14` | filtre=low_vol · çıkış=stop_atr=2.0,tp_r=3.0 | +144% | +375% | +375% | 0.981 | -39% | 1.576 | 0.002 |
| B | 2 | ARB/USDT | supertrend_flip | `cfg=(7, 2.0)` | filtre=htf_week_sma10 · çıkış=trail_atr=3.0 | +220% | veri yok | +184% | 0.853 | -30% | 1.615 | 0.002 |
| B | 2 | ARB/USDT | trix_cross | `n=15,signal=7` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=cmf_flow(≤5 bar) | +91% | veri yok | +117% | 0.832 | -30% | 2.163 | 0.002 |
| B | 2 | ARB/USDT | roc_breakout | `n=63,th=0` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_order_block(≤0 bar) | +81% | veri yok | +75% | 0.815 | -19% | 2.077 | 0.002 |
| B | 2 | ARB/USDT | vortex_cross | `n=28` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=cmf_flow(≤5 bar) | +195% | veri yok | +122% | 0.783 | -32% | 1.765 | 0.002 |
| B | 2 | FIL/USDT | macd_cross | `cfg=(8, 21, 5),zero_filter=False` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_ote(≤5 bar) | +84% | +444% | +421% | 1.114 | -22% | 2.016 | 0.001 |
| B | 2 | UNI/USDT | donchian_breakout | `entry=20,exit=20` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_order_block(≤5 bar) | +180% | +412% | +490% | 0.977 | -38% | 2.441 | 0.001 |
| B | 2 | DOGE/USDT | roc_breakout | `n=126,th=5` | filtre=low_vol · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +90% | +99% | +174% | 0.97 | -31% | 1.781 | 0.001 |
| B | 2 | SAND/USDT | vwap_cross | `n=50` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=roc_breakout(≤0 bar) | +53% | +139% | +139% | 0.969 | -21% | 3.06 | 0.001 |
| B | 2 | SAND/USDT | triple_ma | `set=(5, 20, 50),kind=ema` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=roc_breakout(≤5 bar) | +139% | +219% | +219% | 0.95 | -37% | 2.146 | 0.001 |
| B | 2 | SAND/USDT | psar_flip | `cfg=(0.01, 0.1)` | filtre=low_vol · çıkış=stop_atr=2.0,tp_r=3.0 | +175% | +328% | +328% | 0.941 | -36% | 1.602 | 0.001 |
| B | 2 | SAND/USDT | smc_choch | `k=3` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=roc_breakout(≤5 bar) | +100% | +223% | +223% | 0.922 | -28% | 2.653 | 0.001 |
| B | 2 | SAND/USDT | triple_ma | `set=(5, 20, 50),kind=ema` | filtre=low_vol · çıkış=stop_atr=2.0,tp_r=3.0 | +54% | +231% | +231% | 0.884 | -34% | 1.573 | 0.001 |
| B | 2 | OP/USDT | trix_cross | `n=21,signal=9` | filtre=low_vol · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +134% | veri yok | +148% | 0.869 | -32% | 1.593 | 0.001 |
| B | 2 | OP/USDT | ma_cross | `kind=dema,pair=(20, 50)` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=bb_squeeze(≤5 bar) | +67% | veri yok | +147% | 0.867 | -27% | 2.351 | 0.001 |
| B | 1 | ARB/USDT | bollinger_breakout | `n=50,k=2.5` | çıkış=stop_atr=2.0,trail_atr=3.0 | +119% | veri yok | +137% | 0.831 | -29% | 2.519 | 0.001 |
| B | 2 | ARB/USDT | rsi_midline | `n=21,level=60` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_order_block(≤5 bar) | +136% | veri yok | +147% | 0.812 | -34% | 1.926 | 0.001 |
| B | 2 | ARB/USDT | ichimoku_cloud | `cfg=(7, 22, 44)` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_order_block(≤3 bar) | +127% | veri yok | +127% | 0.808 | -26% | 1.927 | 0.001 |
| B | 2 | INJ/USDT | roc_breakout | `n=252,th=5` | filtre=low_vol · çıkış=stop_atr=2.0,trail_atr=3.0 | +110% | veri yok | +134% | 0.798 | -36% | 1.855 | 0.001 |
| B | 2 | ARB/USDT | rsi_midline | `n=21,level=60` | filtre=htf_week_sma10 · çıkış=stop_atr=2.0,max_hold=10 | +114% | veri yok | +127% | 0.764 | -28% | 1.563 | 0.001 |
| B | 2 | APT/USDT | triple_ma | `set=(5, 20, 50),kind=ema` | filtre=low_vol · çıkış=stop_atr=2.0,max_hold=10 | +47% | veri yok | +78% | 0.753 | -21% | 1.562 | 0.001 |
| B | 2 | ARB/USDT | cci_breakout | `n=14,level=100` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_liquidity_sweep(≤5 bar) | +47% | veri yok | +87% | 0.748 | -38% | 1.701 | 0.001 |
| B | 1 | SUI/USDT | linreg_slope | `n=100,th=0.0005` | çıkış=stop_atr=2.0,trail_atr=3.0 | +91% | veri yok | +94% | 0.728 | -35% | 1.897 | 0.001 |
| B | 1 | ARB/USDT | rsi_midline | `n=21,level=60` | çıkış=stop_atr=2.0,trail_atr=3.0 | +151% | veri yok | +126% | 0.69 | -37% | 1.521 | 0.001 |
| B | 2 | ETH/USDT | bollinger_breakout | `n=50,k=2.5` | filtre=htf_week_sma10 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +54% | +138% | +268% | 1.137 | -17% | 3.455 | 0.0 |
| B | 2 | XRP/USDT | ma_cross | `kind=sma,pair=(20, 50)` | filtre=low_vol · çıkış=stop_atr=2.0,tp_r=3.0 | +29% | +158% | +452% | 0.965 | -21% | 2.109 | 0.0 |
| B | 2 | FIL/USDT | ppo_cross | `cfg=(12, 26, 9)` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_order_block(≤0 bar) | +96% | +191% | +192% | 0.954 | -23% | 2.364 | 0.0 |
| B | 1 | FIL/USDT | rsi_reversal | `n=14,lo=30,exit=50` | çıkış=stop_atr=2.0,trail_atr=3.0 | +37% | +176% | +271% | 0.934 | -29% | 1.562 | 0.0 |
| B | 2 | FIL/USDT | tsi_cross | `cfg=(25, 13, 7)` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_order_block(≤5 bar) | +122% | +275% | +289% | 0.9 | -33% | 1.678 | 0.0 |
| B | 2 | ETH/USDT | bollinger_breakout | `n=50,k=2.5` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_bos(≤0 bar) | +57% | +159% | +308% | 0.898 | -24% | 3.356 | 0.0 |
| B | 2 | DOT/USDT | bb_squeeze | `n=20,q=0.2,look=252` | filtre=low_vol · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +67% | +216% | +173% | 0.874 | -38% | 1.805 | 0.0 |
| B | 2 | ETH/USDT | price_ma | `kind=sma,n=150` | filtre=htf_week_sma10 · çıkış=stop_atr=2.0,max_hold=10 | +32% | +61% | +138% | 0.872 | -22% | 2.265 | 0.0 |
| B | 2 | SAND/USDT | macd_divergence | `k=3,fast=12,slow=26` | filtre=low_vol · çıkış=stop_atr=2.0,max_hold=10 | +78% | +113% | +113% | 0.854 | -25% | 1.754 | 0.0 |
| B | 2 | MANA/USDT | price_ma | `kind=sma,n=100` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=pivot_bounce(≤5 bar) | +88% | +173% | +182% | 0.847 | -23% | 2.035 | 0.0 |
| B | 2 | UNI/USDT | bollinger_breakout | `n=50,k=2.5` | filtre=low_vol · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +33% | +75% | +91% | 0.84 | -19% | 2.415 | 0.0 |
| B | 2 | SAND/USDT | ichimoku_cloud | `cfg=(9, 26, 52)` | filtre=low_vol · çıkış=trail_atr=3.0 | +21% | +249% | +249% | 0.837 | -40% | 1.732 | 0.0 |
| B | 2 | SAND/USDT | price_ma | `kind=sma,n=50` | filtre=low_vol · çıkış=stop_atr=2.0,tp_r=3.0 | +115% | +220% | +220% | 0.833 | -37% | 1.504 | 0.0 |
| B | 2 | SAND/USDT | rsi_divergence | `n=14,k=5,exit_level=50` | filtre=adx20 · çıkış=signal_only | +20% | +81% | +81% | 0.827 | -18% | 4.614 | 0.0 |
| B | 2 | FIL/USDT | bollinger_reversion | `n=30,k=2.0` | filtre=regime_bench200 · çıkış=stop_atr=2.0,tp_r=3.0 | +65% | +104% | +104% | 0.819 | -25% | 1.683 | 0.0 |
| B | 2 | SAND/USDT | awesome_zero | `fast=5,slow=34` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_fvg(≤5 bar) | +54% | +181% | +181% | 0.811 | -29% | 1.903 | 0.0 |
| B | 2 | NEAR/USDT | bb_squeeze | `n=20,q=0.2,look=252` | filtre=low_vol · çıkış=stop_atr=2.0,tp_r=3.0 | +53% | +207% | +226% | 0.809 | -39% | 1.691 | 0.0 |
| B | 2 | DOGE/USDT | roc_breakout | `n=126,th=5` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_liquidity_sweep(≤3 bar) | +46% | +73% | +110% | 0.808 | -28% | 2.82 | 0.0 |
| B | 2 | SNX/USDT | donchian_breakout | `entry=100,exit=10` | filtre=low_vol · çıkış=stop_atr=2.0,tp_r=3.0 | +39% | +205% | +195% | 0.799 | -33% | 2.349 | 0.0 |
| B | 2 | NEAR/USDT | bb_squeeze | `n=20,q=0.2,look=252` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=cmf_flow(≤3 bar) | +79% | +230% | +250% | 0.795 | -30% | 2.383 | 0.0 |
| B | 2 | ETC/USDT | roc_breakout | `n=252,th=10` | filtre=regime_bench200 · çıkış=stop_atr=2.0,tp_r=3.0 | +97% | +314% | +344% | 0.784 | -28% | 2.206 | 0.0 |
| B | 2 | IMX/USDT | donchian_breakout | `entry=100,exit=10` | filtre=htf_week_sma10 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +111% | veri yok | +140% | 0.75 | -37% | 1.799 | 0.0 |
| B | 2 | ADA/USDT | hammer_star | `lookback_low=10` | filtre=htf_week_sma10 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +15% | veri yok | +45% | 0.747 | -13% | 1.681 | 0.0 |
| B | 2 | SAND/USDT | cmf_flow | `n=10,th=0.05` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=bb_squeeze(≤3 bar) | +97% | +92% | +92% | 0.739 | -24% | 1.957 | 0.0 |
| B | 2 | XRP/USDT | bb_squeeze | `n=20,q=0.1,look=252` | çıkış=stop_atr=2.0,tp_r=3.0 | +42% | +35% | +203% | 0.737 | -39% | 1.726 | 0.0 |
| B | 2 | MANA/USDT | volume_breakout | `n=50,rv=1.5` | çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +72% | +91% | +129% | 0.734 | -35% | 2.005 | 0.0 |
| B | 2 | SAND/USDT | awesome_zero | `fast=5,slow=34` | filtre=low_vol · çıkış=stop_atr=2.0,tp_r=3.0 | +69% | +164% | +164% | 0.726 | -32% | 1.54 | 0.0 |
| B | 2 | MANA/USDT | rsi_divergence | `n=14,k=5,exit_level=50` | filtre=adx20 · çıkış=stop_atr=2.0,max_hold=10 | +15% | +36% | +46% | 0.713 | -12% | 1.996 | 0.0 |
| B | 1 | SAND/USDT | volume_breakout | `n=50,rv=1.5` | çıkış=stop_atr=2.0,trail_atr=3.0 | +120% | +159% | +159% | 0.697 | -28% | 2.371 | 0.0 |
| B | 2 | OP/USDT | donchian_breakout | `entry=20,exit=10` | filtre=low_vol · çıkış=trail_atr=3.0 | +108% | veri yok | +142% | 0.697 | -40% | 1.643 | 0.0 |
| B | 2 | AVAX/USDT | roc_breakout | `n=252,th=10` | filtre=regime_bench200 · çıkış=stop_atr=2.0,max_hold=10 | +58% | +116% | +109% | 0.677 | -26% | 2.781 | 0.0 |
| B | 1 | SAND/USDT | donchian_breakout | `entry=100,exit=20` | çıkış=stop_atr=2.0,trail_atr=3.0 | +49% | +163% | +163% | 0.674 | -38% | 1.787 | 0.0 |
| B | 2 | OP/USDT | smc_order_block | `k=3,max_age=20` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_liquidity_sweep(≤5 bar) | +6% | veri yok | +106% | 0.666 | -39% | 1.779 | 0.0 |
| B | 2 | SAND/USDT | bb_squeeze | `n=20,q=0.2,look=126` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_order_block(≤5 bar) | +51% | +105% | +105% | 0.661 | -26% | 1.941 | 0.0 |
| B | 1 | ARB/USDT | volume_breakout | `n=50,rv=2.0` | çıkış=stop_atr=2.0,trail_atr=3.0 | +72% | veri yok | +93% | 0.66 | -31% | 1.9 | 0.0 |
| B | 2 | MANA/USDT | price_ma | `kind=sma,n=100` | filtre=trend_sma200 · çıkış=stop_atr=2.0,tp_r=3.0 | +127% | +162% | +172% | 0.646 | -35% | 1.641 | 0.0 |
| B | 2 | SAND/USDT | smc_order_block | `k=5,max_age=50` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=bb_squeeze(≤3 bar) | +7% | +68% | +68% | 0.642 | -21% | 2.258 | 0.0 |
| B | 2 | MINA/USDT | bb_squeeze | `n=20,q=0.1,look=252` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_choch(≤3 bar) | +44% | +86% | +99% | 0.636 | -34% | 1.942 | 0.0 |
| B | 2 | MINA/USDT | bb_squeeze | `n=20,q=0.1,look=252` | çıkış=signal_only | +101% | +126% | +128% | 0.631 | -33% | 1.772 | 0.0 |
| B | 2 | UNI/USDT | supertrend_flip | `cfg=(14, 3.0)` | çıkış=stop_atr=2.0,trail_atr=3.0 · onay=bb_squeeze(≤5 bar) | +69% | +159% | +113% | 0.622 | -27% | 2.112 | 0.0 |
| B | 2 | SAND/USDT | trix_cross | `n=21,signal=7` | filtre=low_vol · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0 | +77% | +92% | +92% | 0.61 | -31% | 1.413 | 0.0 |
| B | 1 | SAND/USDT | rsi_divergence | `n=14,k=5,exit_level=50` | çıkış=stop_atr=2.0,trail_atr=3.0 | +7% | +47% | +47% | 0.581 | -25% | 1.758 | 0.0 |
| B | 2 | BTC/USDT | donchian_breakout | `entry=100,exit=10` | filtre=htf_week_sma10 · çıkış=stop_atr=2.0,tp_r=3.0 | +28% | +36% | +101% | 0.552 | -31% | 1.536 | 0.0 |
| B | 2 | UNI/USDT | donchian_breakout | `entry=20,exit=20` | filtre=low_vol · çıkış=stop_atr=2.0,trail_atr=3.0 | +72% | +111% | +107% | 0.541 | -37% | 1.536 | 0.0 |

## Coin coin özet (ajan günlüğü)

- **AAVE/USDT**: 62 aday denendi, 0 kaldı. En iyi aday triple_ma (`set=(10, 50, 200),kind=ema`, çıkış=stop_atr=2.0,trail_atr=3.0): S1 — 3y -10%, 5y +53%, full +6%; 104 işlem (zararlı: 3y).
- **ADA/USDT**: 78 aday denendi, 3 kaldı. En iyi aday rsi_divergence (`n=14,k=3,exit_level=70`, filtre=htf_week_sma10 · çıkış=stop_atr=2.0,be_r=1.0): OK — tüm adımlar geçti.
- **ALGO/USDT**: 68 aday denendi, 0 kaldı. En iyi aday rsi_divergence (`n=14,k=5,exit_level=50`, filtre=regime_bench200 · çıkış=signal_only): S7 — PSR 0.878.
- **APT/USDT**: 71 aday denendi, 3 kaldı. En iyi aday macd_zero (`cfg=(12, 26, 9)`, filtre=htf_week_sma10 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0): OK — tüm adımlar geçti.
- **ARB/USDT**: 118 aday denendi, 41 kaldı. En iyi aday price_ma (`kind=kama,n=200`, filtre=trend_sma200 · çıkış=stop_atr=2.0,tp_r=3.0): OK — tüm adımlar geçti.
- **ATOM/USDT**: 72 aday denendi, 0 kaldı. En iyi aday bb_squeeze (`n=20,q=0.1,look=252`, filtre=low_vol · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0): S7 — PSR 0.807.
- **AVAX/USDT**: 65 aday denendi, 1 kaldı. En iyi aday roc_breakout (`n=252,th=10`, filtre=regime_bench200 · çıkış=stop_atr=2.0,max_hold=10): OK — tüm adımlar geçti.
- **AXS/USDT**: 69 aday denendi, 2 kaldı. En iyi aday macd_zero (`cfg=(5, 35, 5)`, filtre=low_vol · çıkış=stop_atr=2.0,tp_r=3.0): OK — tüm adımlar geçti.
- **BCH/USDT**: 64 aday denendi, 0 kaldı. En iyi aday volume_breakout (`n=50,rv=2.0`, filtre=low_vol · çıkış=trail_atr=3.0): S4 — komşu ayarların %33'i kârlı.
- **BNB/USDT**: 65 aday denendi, 0 kaldı. En iyi aday donchian_breakout (`entry=100,exit=10`, çıkış=stop_atr=2.0,trail_atr=3.0): S7 — PSR 0.829.
- **BTC/USDT**: 64 aday denendi, 1 kaldı. En iyi aday donchian_breakout (`entry=100,exit=10`, filtre=htf_week_sma10 · çıkış=stop_atr=2.0,tp_r=3.0): OK — tüm adımlar geçti.
- **CRV/USDT**: 64 aday denendi, 0 kaldı. En iyi aday roc_breakout (`n=252,th=0`, filtre=adx20 · çıkış=stop_atr=2.0,tp_r=3.0): S2 — PF 1.357, 1x maks. düşüş -52%.
- **DOGE/USDT**: 67 aday denendi, 3 kaldı. En iyi aday linreg_slope (`n=100,th=0.0005`, filtre=low_vol · çıkış=stop_atr=2.0,tp_r=3.0): OK — tüm adımlar geçti.
- **DOT/USDT**: 69 aday denendi, 1 kaldı. En iyi aday bb_squeeze (`n=20,q=0.2,look=252`, filtre=low_vol · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0): OK — tüm adımlar geçti.
- **ETC/USDT**: 64 aday denendi, 1 kaldı. En iyi aday roc_breakout (`n=252,th=10`, filtre=regime_bench200 · çıkış=stop_atr=2.0,tp_r=3.0): OK — tüm adımlar geçti.
- **ETH/USDT**: 70 aday denendi, 3 kaldı. En iyi aday bollinger_breakout (`n=50,k=2.5`, filtre=htf_week_sma10 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0): OK — tüm adımlar geçti.
- **FIL/USDT**: 85 aday denendi, 7 kaldı. En iyi aday trix_cross (`n=9,signal=9`, çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_ote(≤5 bar)): OK — tüm adımlar geçti.
- **IMX/USDT**: 69 aday denendi, 1 kaldı. En iyi aday donchian_breakout (`entry=100,exit=10`, filtre=htf_week_sma10 · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0): OK — tüm adımlar geçti.
- **INJ/USDT**: 65 aday denendi, 1 kaldı. En iyi aday roc_breakout (`n=252,th=5`, filtre=low_vol · çıkış=stop_atr=2.0,trail_atr=3.0): OK — tüm adımlar geçti.
- **LINK/USDT**: 64 aday denendi, 0 kaldı. En iyi aday smc_order_block (`k=5,max_age=50`, çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_liquidity_sweep(≤0 bar)): S4 — komşu ayarların %0'i kârlı.
- **LTC/USDT**: 62 aday denendi, 0 kaldı. En iyi aday bb_squeeze (`n=20,q=0.1,look=126`, çıkış=stop_atr=2.0,trail_atr=3.0): S1 — 3y -16%, 5y -27%, full +13%; 134 işlem (zararlı: 3y, 5y).
- **MANA/USDT**: 76 aday denendi, 4 kaldı. En iyi aday price_ma (`kind=sma,n=100`, çıkış=stop_atr=2.0,trail_atr=3.0 · onay=pivot_bounce(≤5 bar)): OK — tüm adımlar geçti.
- **MINA/USDT**: 70 aday denendi, 2 kaldı. En iyi aday bb_squeeze (`n=20,q=0.1,look=252`, çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_choch(≤3 bar)): OK — tüm adımlar geçti.
- **NEAR/USDT**: 64 aday denendi, 2 kaldı. En iyi aday bb_squeeze (`n=20,q=0.2,look=252`, filtre=low_vol · çıkış=stop_atr=2.0,tp_r=3.0): OK — tüm adımlar geçti.
- **OP/USDT**: 86 aday denendi, 8 kaldı. En iyi aday bb_squeeze (`n=20,q=0.2,look=252`, filtre=low_vol · çıkış=stop_atr=2.0,max_hold=10): OK — tüm adımlar geçti.
- **PYTH/USDT**: elendi (S0: 2.9 yıl veri var, en az 3.0 yıl gerekli).
- **SAND/USDT**: 114 aday denendi, 25 kaldı. En iyi aday tsi_cross (`cfg=(25, 13, 7)`, filtre=low_vol · çıkış=stop_atr=2.0,max_hold=10): OK — tüm adımlar geçti.
- **SNX/USDT**: 72 aday denendi, 1 kaldı. En iyi aday donchian_breakout (`entry=100,exit=10`, filtre=low_vol · çıkış=stop_atr=2.0,tp_r=3.0): OK — tüm adımlar geçti.
- **SOL/USDT**: 62 aday denendi, 0 kaldı. En iyi aday volume_breakout (`n=50,rv=3.0`, çıkış=stop_atr=2.0,trail_atr=3.0): S1 — 3y +31%, 5y +34%, full +34%; 26 işlem.
- **SUI/USDT**: 65 aday denendi, 1 kaldı. En iyi aday linreg_slope (`n=100,th=0.0005`, çıkış=stop_atr=2.0,trail_atr=3.0): OK — tüm adımlar geçti.
- **THETA/USDT**: 64 aday denendi, 0 kaldı. En iyi aday roc_breakout (`n=252,th=10`, çıkış=stop_atr=2.0,trail_atr=3.0 · onay=smc_order_block(≤3 bar)): S2 — PF 2.11, 1x maks. düşüş -47%.
- **TRX/USDT**: 63 aday denendi, 0 kaldı. En iyi aday wavetrend_reversal (`n1=9,n2=26,lo=-60`, çıkış=stop_atr=2.0,trail_atr=3.0): S2 — PF 1.332, 1x maks. düşüş -47%.
- **UNI/USDT**: 81 aday denendi, 5 kaldı. En iyi aday supertrend_flip (`cfg=(14, 3.0)`, filtre=trend_sma200 · çıkış=stop_atr=2.0,tp_r=3.0): OK — tüm adımlar geçti.
- **XLM/USDT**: 86 aday denendi, 6 kaldı. En iyi aday smc_bos (`k=2`, filtre=low_vol · çıkış=stop_atr=2.0,partial_r=1.0,partial_frac=0.5,partial_to_be=True,trail_atr=3.0): OK — tüm adımlar geçti.
- **XRP/USDT**: 66 aday denendi, 2 kaldı. En iyi aday ma_cross (`kind=sma,pair=(20, 50)`, filtre=low_vol · çıkış=stop_atr=2.0,tp_r=3.0): OK — tüm adımlar geçti.

## Zayıf yönler (dürüst liste)

- 34426 deneme yapıldı. Bu kadar çok denemede şans eseri iyi görünen strateji çıkar. DSR bunu düzeltir; tier A sadece DSR ≥ eşik olanlardır.
- Seçim ve test aynı geçmiş veride yapıldı. Gerçek test arenadaki ileri (paper) kayıttır.
- Survivorship: liste bugünün coinlerinden oluşur. Borsadan silinen coinler yok, bu sonucu iyimser yapar.
- Funding sabit yıllık oranla, likidasyon işlem bazında yaklaşık modellenir.
- Tek borsa verisi (Bitget, yoksa OKX/KuCoin). Emir defteri ve piyasa etkisi modellenmez.

## Arena

Arena: 97 aktif (eleme geçen), 3 kontrol (yakın aday, switcher kullanmaz), 100 yeni üye, 0 kontrolden aktife. Üst sınır 100.

## Switcher backtest kapısı

Geçti: **False** — kontroller: `{"beats_equal_weight_all_windows": false, "positive_at_cost_stress": true, "max_dd_ok": true}`

Pencereler: `{"3y": {"sharpe": 1.461, "ew_sharpe": 2.131}, "5y": {"sharpe": 1.449, "ew_sharpe": 2.211}, "full": {"sharpe": 1.048, "ew_sharpe": 1.953}}`
