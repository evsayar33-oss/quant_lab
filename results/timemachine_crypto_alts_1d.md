# Zaman makinesi testi — 1d, kesim 2024-10-17

Her seçim **sadece 2024-10-17'e kadarki veriyle** yapıldı (eleme 15149 deneme, 17 coin). Sonra donmuş seçimlerin 2024-10-17 → 2026-10-16 arası gerçek sonucu ölçüldü. Kesimden sonra emekliye ayrılan üye: 4.

## Portföyler: backtest (kesime kadar) ↔ ileri (kesimden sonra)

| Portföy | Backtest yıllık | Backtest DD | **İleri: $1000 →** | İleri yıllık | İleri Sharpe | İleri maks. düşüş | Bant |
|---|---|---|---|---|---|---|---|
| A Hepsi eşit ağırlık, 1x | +41% | -12% | **955** | -2% | -0.12 | -19% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| B En iyi 10, 1x | +48% | -14% | **914** | -4% | -0.23 | -22% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| B2 En iyi 10, ters volatilite ağırlık, 1x | +37% | -20% | **822** | -9% | -0.4 | -28% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| C En iyi 5, 3x | +173% | -39% | **670** | -18% | -0.23 | -56% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| C2 En iyi 5, 3x + volatilite hedefi %35 | +93% | -30% | **608** | -22% | -0.79 | -47% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| BTC al-tut | – | – | **1,211** | +10% | 0.44 | -53% | – |

## Eleme motoru işe yarıyor mu? (kesimden sonra, eşit ağırlık, 1x)

| Grup | Strateji | $1000 → | Yıllık | Sharpe | Maks. düşüş | Kârlı strateji oranı | Medyan Sharpe |
|---|---|---|---|---|---|---|---|
| aktif | 5 | 889 | -6% | -0.26 | -28% | %20 | -0.02 |
| kontrol | 95 | 778 | -12% | -0.64 | -31% | %22 | -0.21 |

Backtest Sharpe sırası ile ileri Sharpe sırası arasındaki ilişki (Spearman): **-0.008** (1 = backtest'te iyi olan ileride de iyi; 0 = ilişki yok).

## En iyi / en kötü 10 / 5 üye (ileri getiri)

- ✅ SOL/USDT ma_cross (kontrol): +201%, SR 1.25
- ✅ ETH/USDT bollinger_breakout (kontrol): +178%, SR 1.2
- ✅ UNI/USDT williams_reversal (kontrol): +108%, SR 1.23
- ✅ SOL/USDT supertrend_flip (kontrol): +93%, SR 0.91
- ✅ CRV/USDT price_ma (kontrol): +87%, SR 0.78
- ✅ XRP/USDT vortex_cross (kontrol): +73%, SR 0.77
- ✅ ETH/USDT cci_breakout (kontrol): +62%, SR 0.79
- ✅ AAVE/USDT hammer_star (kontrol): +60%, SR 0.98
- ✅ BTC/USDT vortex_cross (kontrol): +52%, SR 0.78
- ✅ SOL/USDT obv_trend (kontrol): +33%, SR 0.53
- ❌ BCH/USDT heikin_ashi (kontrol): -92%, SR -1.25
- ❌ SNX/USDT ibs_reversion (kontrol): -88%, SR -1.1
- ❌ FIL/USDT obv_trend (kontrol): -88%, SR -1.07
- ❌ SNX/USDT mfi_reversal (kontrol): -87%, SR -1.0
- ❌ FIL/USDT inside_bar (kontrol): -85%, SR -1.16

## Zayıf yönler

- Eşikler 2026'da yazıldı; araştırmacı (ben) kesimden sonraki dönemi biliyordu. Eleme motoru o veriyi görmedi, ama tamamen kör değil.
- Coin listesi bugünün listesidir: kesimden sonra borsadan silinen coinler yok (survivorship).
- Tek bir kesim tarihi = tek bir senaryo. Başka bir tarihte sonuç farklı olabilir.