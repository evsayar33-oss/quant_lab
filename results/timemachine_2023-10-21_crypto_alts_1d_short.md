# Zaman makinesi testi — 1d, kesim 2023-10-21

Her seçim **sadece 2023-10-21'e kadarki veriyle** yapıldı (eleme 4900 deneme, 8 coin). Sonra donmuş seçimlerin 2023-10-21 → 2026-10-20 arası gerçek sonucu ölçüldü. Kesimden sonra emekliye ayrılan üye: 0.

## Portföyler: backtest (kesime kadar) ↔ ileri (kesimden sonra)

| Portföy | Backtest yıllık | Backtest DD | **İleri: $1000 →** | İleri yıllık | İleri Sharpe | İleri maks. düşüş | Bant |
|---|---|---|---|---|---|---|---|
| A Hepsi eşit ağırlık, 1x | – | – | **1,000** | +0% | 0.0 | +0% | çok erken (< 1 hafta) |
| B En iyi 10, 1x | – | – | **1,000** | +0% | 0.0 | +0% | çok erken (< 1 hafta) |
| B2 En iyi 10, ters volatilite ağırlık, 1x | – | – | **1,000** | +0% | 0.0 | +0% | çok erken (< 1 hafta) |
| C En iyi 5, 3x | – | – | **1,000** | +0% | 0.0 | +0% | çok erken (< 1 hafta) |
| C2 En iyi 5, 3x + volatilite hedefi %35 | – | – | **1,000** | +0% | 0.0 | +0% | çok erken (< 1 hafta) |
| K1 Çekirdek: BTC+ETH SMA200 + momentum + vol hedefi | +34% | -39% | **2,046** | +27% | 0.99 | -22% | beklenen aralıkta |
| K2 Çekirdek: BTC+ETH momentum + vol hedefi | +28% | -36% | **1,874** | +23% | 0.93 | -27% | beklenen aralıkta |
| BTC al-tut | – | – | **2,776** | +41% | 0.96 | -53% | – |

## Eleme motoru işe yarıyor mu? (kesimden sonra, eşit ağırlık, 1x)

| Grup | Strateji | $1000 → | Yıllık | Sharpe | Maks. düşüş | Kârlı strateji oranı | Medyan Sharpe |
|---|---|---|---|---|---|---|---|
| aktif | 0 | 0 | – | None | – | – | None |
| kontrol | 7 | 850 | -5% | -0.23 | -35% | %43 | 0.05 |

Backtest Sharpe sırası ile ileri Sharpe sırası arasındaki ilişki (Spearman): **-0.036** (1 = backtest'te iyi olan ileride de iyi; 0 = ilişki yok).

## En iyi / en kötü 10 / 5 üye (ileri getiri)

- ✅ BCH/USDT williams_reversal (kontrol): +42%, SR 0.56
- ✅ BTC/USDT rsi_reversal (kontrol): +11%, SR 0.41
- ✅ BCH/USDT cci_reversal (kontrol): +3%, SR 0.17
- ✅ LTC/USDT smc_ote (kontrol): -17%, SR -0.2
- ✅ BCH/USDT stoch_reversal (kontrol): -20%, SR 0.05
- ✅ XRP/USDT smc_ote (kontrol): -56%, SR -0.98
- ✅ BCH/USDT rsi_reversal (kontrol): -65%, SR -0.55
- ❌ BCH/USDT rsi_reversal (kontrol): -65%, SR -0.55
- ❌ XRP/USDT smc_ote (kontrol): -56%, SR -0.98
- ❌ BCH/USDT stoch_reversal (kontrol): -20%, SR 0.05
- ❌ LTC/USDT smc_ote (kontrol): -17%, SR -0.2
- ❌ BCH/USDT cci_reversal (kontrol): +3%, SR 0.17

## Zayıf yönler

- Eşikler 2026'da yazıldı; araştırmacı (ben) kesimden sonraki dönemi biliyordu. Eleme motoru o veriyi görmedi, ama tamamen kör değil.
- Coin listesi bugünün listesidir: kesimden sonra borsadan silinen coinler yok (survivorship).
- Tek bir kesim tarihi = tek bir senaryo. Başka bir tarihte sonuç farklı olabilir.