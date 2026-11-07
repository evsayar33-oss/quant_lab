# Zaman makinesi testi — 1d, kesim 2023-10-17

Her seçim **sadece 2023-10-17'e kadarki veriyle** yapıldı (eleme 13642 deneme, 8 coin). Sonra donmuş seçimlerin 2023-10-17 → 2026-10-18 arası gerçek sonucu ölçüldü. Kesimden sonra emekliye ayrılan üye: 8.

## Portföyler: backtest (kesime kadar) ↔ ileri (kesimden sonra)

| Portföy | Backtest yıllık | Backtest DD | **İleri: $1000 →** | İleri yıllık | İleri Sharpe | İleri maks. düşüş | Bant |
|---|---|---|---|---|---|---|---|
| A Hepsi eşit ağırlık, 1x | +28% | -9% | **1,042** | +1% | 0.23 | -11% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| B En iyi 10, 1x | +34% | -15% | **869** | -5% | -0.8 | -18% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| B2 En iyi 10, ters volatilite ağırlık, 1x | +32% | -15% | **881** | -4% | -0.98 | -13% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| C En iyi 5, 3x | +112% | -42% | **639** | -14% | -0.8 | -47% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| C2 En iyi 5, 3x + volatilite hedefi %35 | +70% | -36% | **705** | -11% | -0.68 | -41% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| K1 Çekirdek: BTC+ETH SMA200 + momentum + vol hedefi | +33% | -39% | **2,073** | +27% | 1.0 | -22% | beklenen aralıkta |
| K2 Çekirdek: BTC+ETH momentum + vol hedefi | +28% | -36% | **1,886** | +24% | 0.94 | -27% | beklenen aralıkta |
| BTC al-tut | – | – | **2,892** | +42% | 0.99 | -53% | – |

## Eleme motoru işe yarıyor mu? (kesimden sonra, eşit ağırlık, 1x)

| Grup | Strateji | $1000 → | Yıllık | Sharpe | Maks. düşüş | Kârlı strateji oranı | Medyan Sharpe |
|---|---|---|---|---|---|---|---|
| aktif | 12 | 1,097 | +3% | 0.33 | -16% | %33 | 0.01 |
| kontrol | 88 | 798 | -7% | -0.27 | -43% | %26 | -0.15 |

Backtest Sharpe sırası ile ileri Sharpe sırası arasındaki ilişki (Spearman): **-0.107** (1 = backtest'te iyi olan ileride de iyi; 0 = ilişki yok).

## En iyi / en kötü 10 / 5 üye (ileri getiri)

- ✅ XRP/USDT macd_cross (kontrol): +1007%, SR 1.84
- ✅ XRP/USDT ppo_cross (kontrol): +667%, SR 1.45
- ✅ ETH/USDT keltner_breakout (kontrol): +338%, SR 1.84
- ✅ XRP/USDT vortex_cross (kontrol): +209%, SR 0.92
- ✅ XRP/USDT ma_cross (kontrol): +192%, SR 1.0
- ✅ ETH/USDT vwap_cross (kontrol): +189%, SR 0.96
- ✅ BTC/USDT rsi_midline (kontrol): +140%, SR 1.12
- ✅ ETH/USDT cci_breakout (kontrol): +112%, SR 0.78
- ✅ BTC/USDT vortex_cross (kontrol): +98%, SR 0.84
- ✅ BTC/USDT ma_cross (kontrol): +69%, SR 0.74
- ❌ ETC/USDT tsi_cross (kontrol): -97%, SR -1.18
- ❌ ETC/USDT ppo_cross (kontrol): -96%, SR -1.14
- ❌ ETC/USDT ma_cross (kontrol): -94%, SR -0.89
- ❌ ETC/USDT roc_breakout (kontrol): -91%, SR -1.55
- ❌ BCH/USDT ma_cross (kontrol): -88%, SR -0.95

## Zayıf yönler

- Eşikler 2026'da yazıldı; araştırmacı (ben) kesimden sonraki dönemi biliyordu. Eleme motoru o veriyi görmedi, ama tamamen kör değil.
- Coin listesi bugünün listesidir: kesimden sonra borsadan silinen coinler yok (survivorship).
- Tek bir kesim tarihi = tek bir senaryo. Başka bir tarihte sonuç farklı olabilir.