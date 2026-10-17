# Zaman makinesi testi — 4h, kesim 2022-10-17

Her seçim **sadece 2022-10-17'e kadarki veriyle** yapıldı (eleme 8146 deneme, 9 coin). Sonra donmuş seçimlerin 2022-10-17 → 2026-10-17 arası gerçek sonucu ölçüldü. Kesimden sonra emekliye ayrılan üye: 21.

## Portföyler: backtest (kesime kadar) ↔ ileri (kesimden sonra)

| Portföy | Backtest yıllık | Backtest DD | **İleri: $1000 →** | İleri yıllık | İleri Sharpe | İleri maks. düşüş | Bant |
|---|---|---|---|---|---|---|---|
| A Hepsi eşit ağırlık, 1x | +46% | -14% | **1,024** | +1% | 0.15 | -7% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| B En iyi 10, 1x | +56% | -12% | **926** | -2% | -0.47 | -11% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| B2 En iyi 10, ters volatilite ağırlık, 1x | +55% | -16% | **949** | -1% | -0.38 | -8% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| C En iyi 5, 3x | +310% | -38% | **747** | -7% | -0.4 | -39% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| C2 En iyi 5, 3x + volatilite hedefi %35 | +149% | -33% | **840** | -4% | -0.27 | -29% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| K1 Çekirdek: BTC+ETH SMA200 + momentum + vol hedefi | +48% | -35% | **2,289** | +23% | 0.88 | -24% | beklenen aralıkta |
| K2 Çekirdek: BTC+ETH momentum + vol hedefi | +38% | -33% | **1,992** | +19% | 0.8 | -27% | beklenen aralıkta |
| BTC al-tut | – | – | **4,239** | +43% | 1.03 | -53% | – |

## Eleme motoru işe yarıyor mu? (kesimden sonra, eşit ağırlık, 1x)

| Grup | Strateji | $1000 → | Yıllık | Sharpe | Maks. düşüş | Kârlı strateji oranı | Medyan Sharpe |
|---|---|---|---|---|---|---|---|
| aktif | 25 | 1,148 | +4% | 0.36 | -19% | %60 | 0.17 |
| kontrol | 37 | 598 | -12% | -0.76 | -44% | %16 | -0.37 |

Backtest Sharpe sırası ile ileri Sharpe sırası arasındaki ilişki (Spearman): **0.114** (1 = backtest'te iyi olan ileride de iyi; 0 = ilişki yok).

## En iyi / en kötü 10 / 5 üye (ileri getiri)

- ✅ ETH/USDT bollinger_breakout (aktif): +120%, SR 0.81
- ✅ ETH/USDT high_52w_break (aktif): +108%, SR 0.92
- ✅ XRP/USDT donchian_breakout (aktif): +98%, SR 0.61
- ✅ BCH/USDT bollinger_breakout (kontrol): +90%, SR 0.69
- ✅ BTC/USDT roc_breakout (kontrol): +56%, SR 0.74
- ✅ BTC/USDT keltner_breakout (aktif): +52%, SR 0.52
- ✅ BTC/USDT atr_breakout (aktif): +51%, SR 0.68
- ✅ ETH/USDT rsi_midline (aktif): +46%, SR 0.47
- ✅ ETH/USDT chop_switch (kontrol): +38%, SR 0.51
- ✅ ETH/USDT roc_breakout (aktif): +34%, SR 0.43
- ❌ ETC/USDT linreg_slope (kontrol): -93%, SR -0.72
- ❌ ETC/USDT roc_breakout (kontrol): -92%, SR -0.98
- ❌ ETC/USDT donchian_breakout (kontrol): -84%, SR -0.68
- ❌ BCH/USDT roc_breakout (kontrol): -84%, SR -0.9
- ❌ ALGO/USDT williams_reversal (kontrol): -84%, SR -0.84

## Zayıf yönler

- Eşikler 2026'da yazıldı; araştırmacı (ben) kesimden sonraki dönemi biliyordu. Eleme motoru o veriyi görmedi, ama tamamen kör değil.
- Coin listesi bugünün listesidir: kesimden sonra borsadan silinen coinler yok (survivorship).
- Tek bir kesim tarihi = tek bir senaryo. Başka bir tarihte sonuç farklı olabilir.