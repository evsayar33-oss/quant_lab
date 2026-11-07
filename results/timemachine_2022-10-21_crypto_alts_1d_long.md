# Zaman makinesi testi — 1d, kesim 2022-10-21

Her seçim **sadece 2022-10-21'e kadarki veriyle** yapıldı (eleme 16485 deneme, 7 coin). Sonra donmuş seçimlerin 2022-10-21 → 2026-10-20 arası gerçek sonucu ölçüldü. Kesimden sonra emekliye ayrılan üye: 24.

## Portföyler: backtest (kesime kadar) ↔ ileri (kesimden sonra)

| Portföy | Backtest yıllık | Backtest DD | **İleri: $1000 →** | İleri yıllık | İleri Sharpe | İleri maks. düşüş | Bant |
|---|---|---|---|---|---|---|---|
| A Hepsi eşit ağırlık, 1x | +58% | -11% | **1,090** | +2% | 0.36 | -10% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| B En iyi 10, 1x | +83% | -20% | **1,327** | +7% | 0.67 | -13% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| B2 En iyi 10, ters volatilite ağırlık, 1x | +82% | -21% | **1,163** | +4% | 0.42 | -13% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| C En iyi 5, 3x | +393% | -54% | **2,300** | +23% | 0.71 | -35% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| C2 En iyi 5, 3x + volatilite hedefi %35 | +132% | -26% | **2,226** | +22% | 0.77 | -31% | beklenen aralıkta |
| K1 Çekirdek: BTC+ETH SMA200 + momentum + vol hedefi | +40% | -39% | **2,318** | +23% | 0.88 | -22% | beklenen aralıkta |
| K2 Çekirdek: BTC+ETH momentum + vol hedefi | +35% | -33% | **1,897** | +17% | 0.75 | -27% | beklenen aralıkta |
| BTC al-tut | – | – | **4,333** | +44% | 1.02 | -53% | – |

## Eleme motoru işe yarıyor mu? (kesimden sonra, eşit ağırlık, 1x)

| Grup | Strateji | $1000 → | Yıllık | Sharpe | Maks. düşüş | Kârlı strateji oranı | Medyan Sharpe |
|---|---|---|---|---|---|---|---|
| aktif | 29 | 1,194 | +5% | 0.38 | -25% | %52 | 0.2 |
| kontrol | 71 | 847 | -4% | -0.08 | -45% | %35 | 0.02 |

Backtest Sharpe sırası ile ileri Sharpe sırası arasındaki ilişki (Spearman): **-0.045** (1 = backtest'te iyi olan ileride de iyi; 0 = ilişki yok).

## En iyi / en kötü 10 / 5 üye (ileri getiri)

- ✅ XRP/USDT elder_impulse (aktif): +706%, SR 1.14
- ✅ XRP/USDT vortex_cross (kontrol): +670%, SR 1.1
- ✅ XRP/USDT price_ma (aktif): +247%, SR 0.9
- ✅ XRP/USDT heikin_ashi (aktif): +240%, SR 1.0
- ✅ TRX/USDT smc_ote (aktif): +216%, SR 0.74
- ✅ ETH/USDT rsi_midline (aktif): +197%, SR 0.89
- ✅ XRP/USDT engulfing (kontrol): +185%, SR 0.69
- ✅ TRX/USDT elder_impulse (kontrol): +113%, SR 0.9
- ✅ LTC/USDT price_ma (aktif): +101%, SR 0.66
- ✅ ETH/USDT macd_cross (kontrol): +88%, SR 0.59
- ❌ ETC/USDT smc_fvg (aktif): -91%, SR -1.3
- ❌ ETC/USDT heikin_ashi (kontrol): -89%, SR -0.8
- ❌ BCH/USDT cci_breakout (kontrol): -85%, SR -1.0
- ❌ ETC/USDT ma_cross (kontrol): -85%, SR -0.86
- ❌ ETC/USDT cci_breakout (kontrol): -84%, SR -0.79

## Zayıf yönler

- Eşikler 2026'da yazıldı; araştırmacı (ben) kesimden sonraki dönemi biliyordu. Eleme motoru o veriyi görmedi, ama tamamen kör değil.
- Coin listesi bugünün listesidir: kesimden sonra borsadan silinen coinler yok (survivorship).
- Tek bir kesim tarihi = tek bir senaryo. Başka bir tarihte sonuç farklı olabilir.