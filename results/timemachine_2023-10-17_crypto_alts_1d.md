# Zaman makinesi testi — 1d, kesim 2023-10-17

Her seçim **sadece 2023-10-17'e kadarki veriyle** yapıldı (eleme 9750 deneme, 8 coin). Sonra donmuş seçimlerin 2023-10-17 → 2026-10-16 arası gerçek sonucu ölçüldü. Kesimden sonra emekliye ayrılan üye: 7.

## Portföyler: backtest (kesime kadar) ↔ ileri (kesimden sonra)

| Portföy | Backtest yıllık | Backtest DD | **İleri: $1000 →** | İleri yıllık | İleri Sharpe | İleri maks. düşüş | Bant |
|---|---|---|---|---|---|---|---|
| A Hepsi eşit ağırlık, 1x | +29% | -10% | **1,052** | +2% | 0.26 | -11% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| B En iyi 10, 1x | +41% | -20% | **846** | -5% | -0.72 | -22% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| B2 En iyi 10, ters volatilite ağırlık, 1x | +36% | -31% | **883** | -4% | -0.45 | -20% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| C En iyi 5, 3x | +124% | -53% | **577** | -17% | -0.72 | -54% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| C2 En iyi 5, 3x + volatilite hedefi %35 | +62% | -39% | **708** | -11% | -0.55 | -42% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| BTC al-tut | – | – | **2,874** | +42% | 0.98 | -53% | – |

## Eleme motoru işe yarıyor mu? (kesimden sonra, eşit ağırlık, 1x)

| Grup | Strateji | $1000 → | Yıllık | Sharpe | Maks. düşüş | Kârlı strateji oranı | Medyan Sharpe |
|---|---|---|---|---|---|---|---|
| aktif | 11 | 1,109 | +4% | 0.35 | -17% | %36 | 0.04 |
| kontrol | 89 | 895 | -4% | -0.05 | -44% | %35 | 0.05 |

Backtest Sharpe sırası ile ileri Sharpe sırası arasındaki ilişki (Spearman): **-0.213** (1 = backtest'te iyi olan ileride de iyi; 0 = ilişki yok).

## En iyi / en kötü 10 / 5 üye (ileri getiri)

- ✅ XRP/USDT macd_cross (kontrol): +1007%, SR 1.84
- ✅ XRP/USDT ppo_cross (kontrol): +667%, SR 1.45
- ✅ ETH/USDT keltner_breakout (kontrol): +338%, SR 1.84
- ✅ XRP/USDT vortex_cross (kontrol): +209%, SR 0.92
- ✅ XRP/USDT ma_cross (kontrol): +192%, SR 1.0
- ✅ ETH/USDT vwap_cross (kontrol): +188%, SR 0.96
- ✅ BTC/USDT rsi_midline (kontrol): +140%, SR 1.12
- ✅ ETH/USDT bollinger_breakout (kontrol): +131%, SR 0.8
- ✅ ETH/USDT cci_breakout (kontrol): +111%, SR 0.78
- ✅ BTC/USDT vortex_cross (kontrol): +100%, SR 0.85
- ❌ ETC/USDT tsi_cross (kontrol): -97%, SR -1.19
- ❌ ETC/USDT ppo_cross (kontrol): -96%, SR -1.16
- ❌ ETC/USDT ma_cross (kontrol): -94%, SR -0.91
- ❌ ETC/USDT roc_breakout (kontrol): -91%, SR -1.57
- ❌ BCH/USDT ma_cross (kontrol): -88%, SR -0.96

## Zayıf yönler

- Eşikler 2026'da yazıldı; araştırmacı (ben) kesimden sonraki dönemi biliyordu. Eleme motoru o veriyi görmedi, ama tamamen kör değil.
- Coin listesi bugünün listesidir: kesimden sonra borsadan silinen coinler yok (survivorship).
- Tek bir kesim tarihi = tek bir senaryo. Başka bir tarihte sonuç farklı olabilir.