# Zaman makinesi testi — 1d, kesim 2023-10-21

Her seçim **sadece 2023-10-21'e kadarki veriyle** yapıldı (eleme 21592 deneme, 8 coin). Sonra donmuş seçimlerin 2023-10-21 → 2026-10-20 arası gerçek sonucu ölçüldü. Kesimden sonra emekliye ayrılan üye: 19.

## Portföyler: backtest (kesime kadar) ↔ ileri (kesimden sonra)

| Portföy | Backtest yıllık | Backtest DD | **İleri: $1000 →** | İleri yıllık | İleri Sharpe | İleri maks. düşüş | Bant |
|---|---|---|---|---|---|---|---|
| A Hepsi eşit ağırlık, 1x | +42% | -10% | **1,348** | +10% | 1.11 | -11% | beklenen aralıkta |
| B En iyi 10, 1x | +60% | -21% | **1,890** | +24% | 1.46 | -11% | beklenen aralıkta |
| B2 En iyi 10, ters volatilite ağırlık, 1x | +69% | -18% | **2,305** | +32% | 1.08 | -12% | beklenen aralıkta |
| C En iyi 5, 3x | +260% | -55% | **7,846** | +99% | 1.52 | -37% | beklenen aralıkta |
| C2 En iyi 5, 3x + volatilite hedefi %35 | +114% | -29% | **3,291** | +49% | 1.35 | -28% | beklenen aralıkta |
| K1 Çekirdek: BTC+ETH SMA200 + momentum + vol hedefi | +34% | -39% | **2,046** | +27% | 0.99 | -22% | beklenen aralıkta |
| K2 Çekirdek: BTC+ETH momentum + vol hedefi | +28% | -36% | **1,874** | +23% | 0.93 | -27% | beklenen aralıkta |
| BTC al-tut | – | – | **2,776** | +41% | 0.96 | -53% | – |

## Eleme motoru işe yarıyor mu? (kesimden sonra, eşit ağırlık, 1x)

| Grup | Strateji | $1000 → | Yıllık | Sharpe | Maks. düşüş | Kârlı strateji oranı | Medyan Sharpe |
|---|---|---|---|---|---|---|---|
| aktif | 33 | 1,353 | +11% | 0.81 | -20% | %58 | 0.29 |
| kontrol | 67 | 998 | -0% | 0.09 | -42% | %36 | -0.01 |

Backtest Sharpe sırası ile ileri Sharpe sırası arasındaki ilişki (Spearman): **0.151** (1 = backtest'te iyi olan ileride de iyi; 0 = ilişki yok).

## En iyi / en kötü 10 / 5 üye (ileri getiri)

- ✅ XRP/USDT macd_cross (kontrol): +889%, SR 1.92
- ✅ XRP/USDT ppo_cross (aktif): +701%, SR 1.69
- ✅ XRP/USDT elder_impulse (aktif): +542%, SR 1.52
- ✅ XRP/USDT tsi_cross (kontrol): +438%, SR 1.55
- ✅ THETA/USDT obv_trend (kontrol): +265%, SR 1.03
- ✅ XRP/USDT engulfing (kontrol): +237%, SR 1.07
- ✅ ETH/USDT vwap_cross (kontrol): +203%, SR 1.2
- ✅ XRP/USDT heikin_ashi (aktif): +182%, SR 1.11
- ✅ TRX/USDT smc_ote (aktif): +153%, SR 0.73
- ✅ XRP/USDT vortex_cross (kontrol): +121%, SR 0.88
- ❌ ETC/USDT ppo_cross (kontrol): -83%, SR -0.79
- ❌ ETC/USDT ma_cross (kontrol): -82%, SR -0.8
- ❌ ETC/USDT tsi_cross (kontrol): -82%, SR -0.81
- ❌ THETA/USDT roc_breakout (kontrol): -80%, SR -0.97
- ❌ ETC/USDT atr_breakout (kontrol): -75%, SR -0.83

## Zayıf yönler

- Eşikler 2026'da yazıldı; araştırmacı (ben) kesimden sonraki dönemi biliyordu. Eleme motoru o veriyi görmedi, ama tamamen kör değil.
- Coin listesi bugünün listesidir: kesimden sonra borsadan silinen coinler yok (survivorship).
- Tek bir kesim tarihi = tek bir senaryo. Başka bir tarihte sonuç farklı olabilir.