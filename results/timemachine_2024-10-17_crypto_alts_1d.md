# Zaman makinesi testi — 1d, kesim 2024-10-17

Her seçim **sadece 2024-10-17'e kadarki veriyle** yapıldı (eleme 19763 deneme, 17 coin). Sonra donmuş seçimlerin 2024-10-17 → 2026-10-18 arası gerçek sonucu ölçüldü. Kesimden sonra emekliye ayrılan üye: 8.

## Portföyler: backtest (kesime kadar) ↔ ileri (kesimden sonra)

| Portföy | Backtest yıllık | Backtest DD | **İleri: $1000 →** | İleri yıllık | İleri Sharpe | İleri maks. düşüş | Bant |
|---|---|---|---|---|---|---|---|
| A Hepsi eşit ağırlık, 1x | +31% | -6% | **1,113** | +5% | 0.71 | -11% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| B En iyi 10, 1x | +37% | -8% | **929** | -4% | -0.39 | -12% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| B2 En iyi 10, ters volatilite ağırlık, 1x | +38% | -19% | **888** | -6% | -0.65 | -17% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| C En iyi 5, 3x | +154% | -26% | **719** | -15% | -0.39 | -39% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| C2 En iyi 5, 3x + volatilite hedefi %35 | +98% | -18% | **702** | -16% | -0.67 | -38% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| K1 Çekirdek: BTC+ETH SMA200 + momentum + vol hedefi | +40% | -39% | **1,185** | +9% | 0.47 | -22% | beklenen aralıkta |
| K2 Çekirdek: BTC+ETH momentum + vol hedefi | +33% | -36% | **1,141** | +7% | 0.41 | -27% | beklenen aralıkta |
| BTC al-tut | – | – | **1,218** | +10% | 0.44 | -53% | – |

## Eleme motoru işe yarıyor mu? (kesimden sonra, eşit ağırlık, 1x)

| Grup | Strateji | $1000 → | Yıllık | Sharpe | Maks. düşüş | Kârlı strateji oranı | Medyan Sharpe |
|---|---|---|---|---|---|---|---|
| aktif | 9 | 939 | -3% | -0.22 | -17% | %22 | -0.42 |
| kontrol | 91 | 798 | -11% | -0.55 | -31% | %24 | -0.21 |

Backtest Sharpe sırası ile ileri Sharpe sırası arasındaki ilişki (Spearman): **0.005** (1 = backtest'te iyi olan ileride de iyi; 0 = ilişki yok).

## En iyi / en kötü 10 / 5 üye (ileri getiri)

- ✅ SOL/USDT smc_fvg (kontrol): +209%, SR 1.38
- ✅ SOL/USDT ma_cross (kontrol): +202%, SR 1.25
- ✅ UNI/USDT williams_reversal (aktif): +137%, SR 1.13
- ✅ SOL/USDT supertrend_flip (kontrol): +94%, SR 0.91
- ✅ XRP/USDT vortex_cross (kontrol): +73%, SR 0.77
- ✅ ETH/USDT smc_bos (kontrol): +66%, SR 0.78
- ✅ AAVE/USDT hammer_star (kontrol): +56%, SR 0.94
- ✅ BTC/USDT vortex_cross (kontrol): +51%, SR 0.77
- ✅ ETH/USDT cci_breakout (kontrol): +44%, SR 0.66
- ✅ CRV/USDT force_index (kontrol): +34%, SR 0.57
- ❌ BCH/USDT heikin_ashi (kontrol): -92%, SR -1.25
- ❌ FIL/USDT obv_trend (kontrol): -89%, SR -1.13
- ❌ SNX/USDT ibs_reversion (kontrol): -88%, SR -1.1
- ❌ SNX/USDT mfi_reversal (kontrol): -86%, SR -0.95
- ❌ BCH/USDT ma_cross (kontrol): -84%, SR -1.47

## Zayıf yönler

- Eşikler 2026'da yazıldı; araştırmacı (ben) kesimden sonraki dönemi biliyordu. Eleme motoru o veriyi görmedi, ama tamamen kör değil.
- Coin listesi bugünün listesidir: kesimden sonra borsadan silinen coinler yok (survivorship).
- Tek bir kesim tarihi = tek bir senaryo. Başka bir tarihte sonuç farklı olabilir.