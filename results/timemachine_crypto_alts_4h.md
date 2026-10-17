# Zaman makinesi testi — 4h, kesim 2024-10-17

Her seçim **sadece 2024-10-17'e kadarki veriyle** yapıldı (eleme 16056 deneme, 22 coin). Sonra donmuş seçimlerin 2024-10-17 → 2026-10-17 arası gerçek sonucu ölçüldü. Kesimden sonra emekliye ayrılan üye: 16.

## Portföyler: backtest (kesime kadar) ↔ ileri (kesimden sonra)

| Portföy | Backtest yıllık | Backtest DD | **İleri: $1000 →** | İleri yıllık | İleri Sharpe | İleri maks. düşüş | Bant |
|---|---|---|---|---|---|---|---|
| A Hepsi eşit ağırlık, 1x | +31% | -8% | **1,115** | +6% | 0.73 | -7% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| B En iyi 10, 1x | +35% | -9% | **1,065** | +3% | 0.38 | -8% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| B2 En iyi 10, ters volatilite ağırlık, 1x | +61% | -17% | **1,063** | +3% | 0.41 | -7% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| C En iyi 5, 3x | +179% | -33% | **1,507** | +23% | 0.82 | -28% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| C2 En iyi 5, 3x + volatilite hedefi %35 | +110% | -23% | **1,517** | +23% | 0.89 | -21% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| BTC al-tut | – | – | **1,207** | +10% | 0.43 | -53% | – |

## Eleme motoru işe yarıyor mu? (kesimden sonra, eşit ağırlık, 1x)

| Grup | Strateji | $1000 → | Yıllık | Sharpe | Maks. düşüş | Kârlı strateji oranı | Medyan Sharpe |
|---|---|---|---|---|---|---|---|
| aktif | 23 | 1,012 | +1% | 0.11 | -15% | %35 | -0.1 |
| kontrol | 60 | 765 | -13% | -0.66 | -35% | %32 | -0.2 |

Backtest Sharpe sırası ile ileri Sharpe sırası arasındaki ilişki (Spearman): **-0.018** (1 = backtest'te iyi olan ileride de iyi; 0 = ilişki yok).

## En iyi / en kötü 10 / 5 üye (ileri getiri)

- ✅ FIL/USDT linreg_slope (aktif): +219%, SR 1.4
- ✅ ETH/USDT bollinger_breakout (aktif): +104%, SR 1.34
- ✅ FIL/USDT ppo_cross (kontrol): +93%, SR 1.03
- ✅ FIL/USDT macd_cross (kontrol): +84%, SR 0.95
- ✅ SOL/USDT ma_cross (kontrol): +74%, SR 0.95
- ✅ ETH/USDT keltner_breakout (aktif): +59%, SR 0.84
- ✅ ETH/USDT volume_breakout (kontrol): +52%, SR 0.79
- ✅ MANA/USDT volume_breakout (kontrol): +50%, SR 0.67
- ✅ MANA/USDT macd_zero (kontrol): +49%, SR 0.65
- ✅ SOL/USDT chop_switch (kontrol): +48%, SR 0.89
- ❌ FIL/USDT macd_zero (kontrol): -96%, SR -1.08
- ❌ FIL/USDT awesome_zero (kontrol): -93%, SR -1.81
- ❌ FIL/USDT vortex_cross (kontrol): -93%, SR -1.58
- ❌ FIL/USDT ichimoku_cloud (kontrol): -81%, SR -0.97
- ❌ FIL/USDT donchian_breakout (kontrol): -79%, SR -1.07

## Zayıf yönler

- Eşikler 2026'da yazıldı; araştırmacı (ben) kesimden sonraki dönemi biliyordu. Eleme motoru o veriyi görmedi, ama tamamen kör değil.
- Coin listesi bugünün listesidir: kesimden sonra borsadan silinen coinler yok (survivorship).
- Tek bir kesim tarihi = tek bir senaryo. Başka bir tarihte sonuç farklı olabilir.