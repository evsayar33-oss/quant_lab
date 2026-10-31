# Zaman makinesi testi — 4h, kesim 2024-10-17

Her seçim **sadece 2024-10-17'e kadarki veriyle** yapıldı (eleme 19437 deneme, 22 coin). Sonra donmuş seçimlerin 2024-10-17 → 2026-10-19 arası gerçek sonucu ölçüldü. Kesimden sonra emekliye ayrılan üye: 22.

## Portföyler: backtest (kesime kadar) ↔ ileri (kesimden sonra)

| Portföy | Backtest yıllık | Backtest DD | **İleri: $1000 →** | İleri yıllık | İleri Sharpe | İleri maks. düşüş | Bant |
|---|---|---|---|---|---|---|---|
| A Hepsi eşit ağırlık, 1x | +30% | -6% | **1,094** | +5% | 0.65 | -5% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| B En iyi 10, 1x | +34% | -9% | **1,110** | +5% | 0.73 | -8% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| B2 En iyi 10, ters volatilite ağırlık, 1x | +50% | -16% | **1,091** | +4% | 0.76 | -8% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| C En iyi 5, 3x | +191% | -32% | **1,753** | +32% | 1.1 | -26% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| C2 En iyi 5, 3x + volatilite hedefi %35 | +118% | -19% | **1,776** | +33% | 1.16 | -26% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| K1 Çekirdek: BTC+ETH SMA200 + momentum + vol hedefi | +44% | -35% | **1,211** | +10% | 0.51 | -24% | beklenen aralıkta |
| K2 Çekirdek: BTC+ETH momentum + vol hedefi | +35% | -36% | **1,181** | +9% | 0.49 | -27% | beklenen aralıkta |
| BTC al-tut | – | – | **1,221** | +10% | 0.45 | -53% | – |

## Eleme motoru işe yarıyor mu? (kesimden sonra, eşit ağırlık, 1x)

| Grup | Strateji | $1000 → | Yıllık | Sharpe | Maks. düşüş | Kârlı strateji oranı | Medyan Sharpe |
|---|---|---|---|---|---|---|---|
| aktif | 31 | 976 | -1% | -0.07 | -14% | %36 | -0.13 |
| kontrol | 63 | 861 | -7% | -0.36 | -27% | %32 | -0.01 |

Backtest Sharpe sırası ile ileri Sharpe sırası arasındaki ilişki (Spearman): **0.115** (1 = backtest'te iyi olan ileride de iyi; 0 = ilişki yok).

## En iyi / en kötü 10 / 5 üye (ileri getiri)

- ✅ FIL/USDT linreg_slope (aktif): +225%, SR 1.42
- ✅ FIL/USDT ppo_cross (kontrol): +161%, SR 1.16
- ✅ FIL/USDT macd_cross (kontrol): +160%, SR 1.17
- ✅ ETH/USDT bollinger_breakout (aktif): +117%, SR 1.32
- ✅ SOL/USDT ma_cross (kontrol): +74%, SR 0.95
- ✅ FIL/USDT smc_choch (aktif): +68%, SR 0.75
- ✅ MANA/USDT macd_zero (kontrol): +58%, SR 0.71
- ✅ ETH/USDT volume_breakout (kontrol): +52%, SR 0.79
- ✅ MANA/USDT volume_breakout (kontrol): +50%, SR 0.67
- ✅ SOL/USDT donchian_breakout (aktif): +50%, SR 0.92
- ❌ FIL/USDT macd_zero (kontrol): -96%, SR -1.07
- ❌ FIL/USDT awesome_zero (kontrol): -93%, SR -1.81
- ❌ FIL/USDT ichimoku_cloud (kontrol): -81%, SR -1.0
- ❌ FIL/USDT donchian_breakout (kontrol): -80%, SR -1.11
- ❌ AVAX/USDT bollinger_breakout (kontrol): -77%, SR -1.02

## Zayıf yönler

- Eşikler 2026'da yazıldı; araştırmacı (ben) kesimden sonraki dönemi biliyordu. Eleme motoru o veriyi görmedi, ama tamamen kör değil.
- Coin listesi bugünün listesidir: kesimden sonra borsadan silinen coinler yok (survivorship).
- Tek bir kesim tarihi = tek bir senaryo. Başka bir tarihte sonuç farklı olabilir.