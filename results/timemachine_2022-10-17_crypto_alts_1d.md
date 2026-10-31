# Zaman makinesi testi — 1d, kesim 2022-10-17

Her seçim **sadece 2022-10-17'e kadarki veriyle** yapıldı (eleme 14301 deneme, 7 coin). Sonra donmuş seçimlerin 2022-10-17 → 2026-10-18 arası gerçek sonucu ölçüldü. Kesimden sonra emekliye ayrılan üye: 12.

## Portföyler: backtest (kesime kadar) ↔ ileri (kesimden sonra)

| Portföy | Backtest yıllık | Backtest DD | **İleri: $1000 →** | İleri yıllık | İleri Sharpe | İleri maks. düşüş | Bant |
|---|---|---|---|---|---|---|---|
| A Hepsi eşit ağırlık, 1x | +57% | -11% | **999** | -0% | 0.02 | -10% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| B En iyi 10, 1x | +72% | -16% | **1,235** | +5% | 0.43 | -9% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| B2 En iyi 10, ters volatilite ağırlık, 1x | +72% | -17% | **1,844** | +17% | 0.56 | -9% | beklenen aralıkta |
| C En iyi 5, 3x | +320% | -44% | **1,568** | +12% | 0.43 | -26% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| C2 En iyi 5, 3x + volatilite hedefi %35 | +148% | -28% | **1,747** | +15% | 0.5 | -23% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| K1 Çekirdek: BTC+ETH SMA200 + momentum + vol hedefi | +40% | -39% | **2,288** | +23% | 0.86 | -22% | beklenen aralıkta |
| K2 Çekirdek: BTC+ETH momentum + vol hedefi | +35% | -33% | **1,879** | +17% | 0.74 | -27% | beklenen aralıkta |
| BTC al-tut | – | – | **4,201** | +43% | 1.0 | -53% | – |

## Eleme motoru işe yarıyor mu? (kesimden sonra, eşit ağırlık, 1x)

| Grup | Strateji | $1000 → | Yıllık | Sharpe | Maks. düşüş | Kârlı strateji oranı | Medyan Sharpe |
|---|---|---|---|---|---|---|---|
| aktif | 13 | 1,218 | +5% | 0.45 | -19% | %38 | -0.04 |
| kontrol | 87 | 644 | -10% | -0.39 | -43% | %21 | -0.15 |

Backtest Sharpe sırası ile ileri Sharpe sırası arasındaki ilişki (Spearman): **-0.105** (1 = backtest'te iyi olan ileride de iyi; 0 = ilişki yok).

## En iyi / en kötü 10 / 5 üye (ileri getiri)

- ✅ XRP/USDT tsi_cross (kontrol): +649%, SR 1.06
- ✅ XRP/USDT vortex_cross (kontrol): +371%, SR 0.87
- ✅ XRP/USDT elder_impulse (kontrol): +217%, SR 0.73
- ✅ TRX/USDT smc_ote (aktif): +133%, SR 0.59
- ✅ XRP/USDT ppo_cross (aktif): +101%, SR 0.71
- ✅ BTC/USDT vortex_cross (kontrol): +94%, SR 0.64
- ✅ ETH/USDT vwap_cross (kontrol): +90%, SR 0.57
- ✅ BTC/USDT atr_breakout (kontrol): +86%, SR 0.8
- ✅ LTC/USDT rsi_reversal (kontrol): +72%, SR 0.69
- ✅ ETH/USDT bollinger_breakout (kontrol): +54%, SR 0.47
- ❌ ETC/USDT smc_fvg (kontrol): -100%, SR -1.65
- ❌ ETC/USDT tsi_cross (kontrol): -98%, SR -0.93
- ❌ ETC/USDT ppo_cross (kontrol): -96%, SR -0.83
- ❌ ETC/USDT ma_cross (kontrol): -96%, SR -0.74
- ❌ BCH/USDT psar_flip (kontrol): -95%, SR -0.67

## Zayıf yönler

- Eşikler 2026'da yazıldı; araştırmacı (ben) kesimden sonraki dönemi biliyordu. Eleme motoru o veriyi görmedi, ama tamamen kör değil.
- Coin listesi bugünün listesidir: kesimden sonra borsadan silinen coinler yok (survivorship).
- Tek bir kesim tarihi = tek bir senaryo. Başka bir tarihte sonuç farklı olabilir.