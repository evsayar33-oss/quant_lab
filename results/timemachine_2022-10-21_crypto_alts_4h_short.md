# Zaman makinesi testi — 4h, kesim 2022-10-21

Her seçim **sadece 2022-10-21'e kadarki veriyle** yapıldı (eleme 7678 deneme, 9 coin). Sonra donmuş seçimlerin 2022-10-21 → 2026-10-21 arası gerçek sonucu ölçüldü. Kesimden sonra emekliye ayrılan üye: 14.

## Portföyler: backtest (kesime kadar) ↔ ileri (kesimden sonra)

| Portföy | Backtest yıllık | Backtest DD | **İleri: $1000 →** | İleri yıllık | İleri Sharpe | İleri maks. düşüş | Bant |
|---|---|---|---|---|---|---|---|
| A Hepsi eşit ağırlık, 1x | +30% | -8% | **927** | -2% | -0.52 | -8% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| B En iyi 10, 1x | +32% | -9% | **881** | -3% | -0.67 | -13% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| B2 En iyi 10, ters volatilite ağırlık, 1x | +38% | -15% | **879** | -3% | -0.76 | -12% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| C En iyi 5, 3x | +156% | -38% | **694** | -9% | -0.4 | -39% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| C2 En iyi 5, 3x + volatilite hedefi %35 | +97% | -28% | **743** | -7% | -0.35 | -33% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| K1 Çekirdek: BTC+ETH SMA200 + momentum + vol hedefi | +48% | -35% | **2,332** | +24% | 0.89 | -24% | beklenen aralıkta |
| K2 Çekirdek: BTC+ETH momentum + vol hedefi | +37% | -33% | **2,023** | +19% | 0.82 | -27% | beklenen aralıkta |
| BTC al-tut | – | – | **4,364** | +45% | 1.04 | -53% | – |

## Eleme motoru işe yarıyor mu? (kesimden sonra, eşit ağırlık, 1x)

| Grup | Strateji | $1000 → | Yıllık | Sharpe | Maks. düşüş | Kârlı strateji oranı | Medyan Sharpe |
|---|---|---|---|---|---|---|---|
| aktif | 14 | 944 | -1% | -0.12 | -12% | %36 | -0.07 |
| kontrol | 21 | 726 | -8% | -0.86 | -30% | %10 | -0.4 |

Backtest Sharpe sırası ile ileri Sharpe sırası arasındaki ilişki (Spearman): **0.169** (1 = backtest'te iyi olan ileride de iyi; 0 = ilişki yok).

## En iyi / en kötü 10 / 5 üye (ileri getiri)

- ✅ ETH/USDT bollinger_breakout (kontrol): +137%, SR 0.98
- ✅ ETH/USDT adx_trend (kontrol): +39%, SR 0.63
- ✅ ETC/USDT roc_breakout (aktif): +32%, SR 0.53
- ✅ BCH/USDT aroon_cross (aktif): +27%, SR 0.36
- ✅ XRP/USDT bb_squeeze (aktif): +20%, SR 0.43
- ✅ BCH/USDT bollinger_breakout (aktif): +11%, SR 0.22
- ✅ ALGO/USDT bb_squeeze (aktif): +1%, SR 0.08
- ✅ ALGO/USDT hammer_star (kontrol): -7%, SR 0.04
- ✅ ETC/USDT hammer_star (kontrol): -7%, SR -0.13
- ✅ LTC/USDT bb_squeeze (aktif): -10%, SR -0.09
- ❌ BCH/USDT smc_order_block (kontrol): -74%, SR -1.04
- ❌ BCH/USDT atr_breakout (kontrol): -74%, SR -1.18
- ❌ LTC/USDT triple_ma (kontrol): -65%, SR -0.91
- ❌ ETC/USDT triple_ma (kontrol): -58%, SR -0.61
- ❌ ALGO/USDT williams_reversal (kontrol): -48%, SR -0.6

## Zayıf yönler

- Eşikler 2026'da yazıldı; araştırmacı (ben) kesimden sonraki dönemi biliyordu. Eleme motoru o veriyi görmedi, ama tamamen kör değil.
- Coin listesi bugünün listesidir: kesimden sonra borsadan silinen coinler yok (survivorship).
- Tek bir kesim tarihi = tek bir senaryo. Başka bir tarihte sonuç farklı olabilir.