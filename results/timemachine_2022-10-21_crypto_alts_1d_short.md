# Zaman makinesi testi — 1d, kesim 2022-10-21

Her seçim **sadece 2022-10-21'e kadarki veriyle** yapıldı (eleme 4389 deneme, 7 coin). Sonra donmuş seçimlerin 2022-10-21 → 2026-10-20 arası gerçek sonucu ölçüldü. Kesimden sonra emekliye ayrılan üye: 1.

## Portföyler: backtest (kesime kadar) ↔ ileri (kesimden sonra)

| Portföy | Backtest yıllık | Backtest DD | **İleri: $1000 →** | İleri yıllık | İleri Sharpe | İleri maks. düşüş | Bant |
|---|---|---|---|---|---|---|---|
| A Hepsi eşit ağırlık, 1x | +11% | -13% | **993** | -0% | -0.02 | -8% | beklenen aralıkta |
| B En iyi 10, 1x | +11% | -13% | **993** | -0% | -0.02 | -8% | beklenen aralıkta |
| B2 En iyi 10, ters volatilite ağırlık, 1x | +11% | -13% | **993** | -0% | -0.02 | -8% | beklenen aralıkta |
| C En iyi 5, 3x | +29% | -39% | **961** | -1% | -0.02 | -22% | beklenen aralıkta |
| C2 En iyi 5, 3x + volatilite hedefi %35 | +20% | -25% | **955** | -1% | -0.06 | -19% | beklenen aralıkta |
| K1 Çekirdek: BTC+ETH SMA200 + momentum + vol hedefi | +40% | -39% | **2,318** | +23% | 0.88 | -22% | beklenen aralıkta |
| K2 Çekirdek: BTC+ETH momentum + vol hedefi | +35% | -33% | **1,897** | +17% | 0.75 | -27% | beklenen aralıkta |
| BTC al-tut | – | – | **4,333** | +44% | 1.02 | -53% | – |

## Eleme motoru işe yarıyor mu? (kesimden sonra, eşit ağırlık, 1x)

| Grup | Strateji | $1000 → | Yıllık | Sharpe | Maks. düşüş | Kârlı strateji oranı | Medyan Sharpe |
|---|---|---|---|---|---|---|---|
| aktif | 1 | 1,101 | +2% | 0.3 | -14% | %100 | 0.3 |
| kontrol | 6 | 458 | -18% | -0.9 | -60% | %0 | -0.51 |

Backtest Sharpe sırası ile ileri Sharpe sırası arasındaki ilişki (Spearman): **0.071** (1 = backtest'te iyi olan ileride de iyi; 0 = ilişki yok).

## En iyi / en kötü 10 / 5 üye (ileri getiri)

- ✅ BTC/USDT rsi_reversal (aktif): +10%, SR 0.3
- ✅ LTC/USDT ibs_reversion (kontrol): -31%, SR -0.47
- ✅ BCH/USDT rsi_reversal (kontrol): -34%, SR -0.03
- ✅ XRP/USDT smc_ote (kontrol): -40%, SR -0.29
- ✅ BCH/USDT trix_cross (kontrol): -59%, SR -0.55
- ✅ LTC/USDT stochrsi_reversal (kontrol): -77%, SR -0.88
- ✅ BCH/USDT adx_trend (kontrol): -86%, SR -1.03
- ❌ BCH/USDT adx_trend (kontrol): -86%, SR -1.03
- ❌ LTC/USDT stochrsi_reversal (kontrol): -77%, SR -0.88
- ❌ BCH/USDT trix_cross (kontrol): -59%, SR -0.55
- ❌ XRP/USDT smc_ote (kontrol): -40%, SR -0.29
- ❌ BCH/USDT rsi_reversal (kontrol): -34%, SR -0.03

## Zayıf yönler

- Eşikler 2026'da yazıldı; araştırmacı (ben) kesimden sonraki dönemi biliyordu. Eleme motoru o veriyi görmedi, ama tamamen kör değil.
- Coin listesi bugünün listesidir: kesimden sonra borsadan silinen coinler yok (survivorship).
- Tek bir kesim tarihi = tek bir senaryo. Başka bir tarihte sonuç farklı olabilir.