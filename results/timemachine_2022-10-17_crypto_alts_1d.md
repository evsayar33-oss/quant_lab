# Zaman makinesi testi — 1d, kesim 2022-10-17

Her seçim **sadece 2022-10-17'e kadarki veriyle** yapıldı (eleme 9969 deneme, 7 coin). Sonra donmuş seçimlerin 2022-10-17 → 2026-10-16 arası gerçek sonucu ölçüldü. Kesimden sonra emekliye ayrılan üye: 12.

## Portföyler: backtest (kesime kadar) ↔ ileri (kesimden sonra)

| Portföy | Backtest yıllık | Backtest DD | **İleri: $1000 →** | İleri yıllık | İleri Sharpe | İleri maks. düşüş | Bant |
|---|---|---|---|---|---|---|---|
| A Hepsi eşit ağırlık, 1x | +58% | -15% | **890** | -3% | -0.48 | -12% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| B En iyi 10, 1x | +81% | -17% | **881** | -3% | -0.29 | -16% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| B2 En iyi 10, ters volatilite ağırlık, 1x | +83% | -24% | **947** | -1% | -0.05 | -17% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| C En iyi 5, 3x | +341% | -44% | **609** | -12% | -0.29 | -44% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| C2 En iyi 5, 3x + volatilite hedefi %35 | +113% | -26% | **736** | -7% | -0.26 | -33% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| BTC al-tut | – | – | **4,175** | +43% | 1.0 | -53% | – |

## Eleme motoru işe yarıyor mu? (kesimden sonra, eşit ağırlık, 1x)

| Grup | Strateji | $1000 → | Yıllık | Sharpe | Maks. düşüş | Kârlı strateji oranı | Medyan Sharpe |
|---|---|---|---|---|---|---|---|
| aktif | 12 | 1,042 | +1% | 0.14 | -21% | %33 | -0.08 |
| kontrol | 88 | 738 | -7% | -0.24 | -37% | %27 | -0.09 |

Backtest Sharpe sırası ile ileri Sharpe sırası arasındaki ilişki (Spearman): **-0.191** (1 = backtest'te iyi olan ileride de iyi; 0 = ilişki yok).

## En iyi / en kötü 10 / 5 üye (ileri getiri)

- ✅ XRP/USDT tsi_cross (kontrol): +649%, SR 1.06
- ✅ XRP/USDT vortex_cross (kontrol): +371%, SR 0.87
- ✅ XRP/USDT elder_impulse (kontrol): +217%, SR 0.73
- ✅ BCH/USDT hurst_switch (kontrol): +111%, SR 0.7
- ✅ XRP/USDT ppo_cross (aktif): +101%, SR 0.71
- ✅ BTC/USDT vortex_cross (kontrol): +95%, SR 0.65
- ✅ ETH/USDT vwap_cross (kontrol): +89%, SR 0.57
- ✅ BTC/USDT atr_breakout (kontrol): +86%, SR 0.8
- ✅ LTC/USDT rsi_reversal (kontrol): +72%, SR 0.69
- ✅ ETH/USDT cci_breakout (kontrol): +57%, SR 0.47
- ❌ ETC/USDT tsi_cross (kontrol): -98%, SR -0.94
- ❌ ETC/USDT ppo_cross (kontrol): -97%, SR -0.84
- ❌ ETC/USDT ma_cross (kontrol): -96%, SR -0.75
- ❌ BCH/USDT psar_flip (kontrol): -95%, SR -0.67
- ❌ ETC/USDT roc_breakout (kontrol): -93%, SR -1.32

## Zayıf yönler

- Eşikler 2026'da yazıldı; araştırmacı (ben) kesimden sonraki dönemi biliyordu. Eleme motoru o veriyi görmedi, ama tamamen kör değil.
- Coin listesi bugünün listesidir: kesimden sonra borsadan silinen coinler yok (survivorship).
- Tek bir kesim tarihi = tek bir senaryo. Başka bir tarihte sonuç farklı olabilir.