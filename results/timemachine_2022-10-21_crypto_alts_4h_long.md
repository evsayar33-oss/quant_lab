# Zaman makinesi testi — 4h, kesim 2022-10-21

Her seçim **sadece 2022-10-21'e kadarki veriyle** yapıldı (eleme 19022 deneme, 9 coin). Sonra donmuş seçimlerin 2022-10-21 → 2026-10-21 arası gerçek sonucu ölçüldü. Kesimden sonra emekliye ayrılan üye: 57.

## Portföyler: backtest (kesime kadar) ↔ ileri (kesimden sonra)

| Portföy | Backtest yıllık | Backtest DD | **İleri: $1000 →** | İleri yıllık | İleri Sharpe | İleri maks. düşüş | Bant |
|---|---|---|---|---|---|---|---|
| A Hepsi eşit ağırlık, 1x | +48% | -8% | **1,158** | +4% | 0.73 | -8% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| B En iyi 10, 1x | +73% | -12% | **1,000** | +0% | 0.02 | -8% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| B2 En iyi 10, ters volatilite ağırlık, 1x | +66% | -19% | **1,034** | +1% | 0.2 | -8% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| C En iyi 5, 3x | +430% | -34% | **1,000** | +0% | 0.09 | -24% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| C2 En iyi 5, 3x + volatilite hedefi %35 | +172% | -27% | **1,015** | +0% | 0.11 | -24% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| K1 Çekirdek: BTC+ETH SMA200 + momentum + vol hedefi | +48% | -35% | **2,332** | +24% | 0.89 | -24% | beklenen aralıkta |
| K2 Çekirdek: BTC+ETH momentum + vol hedefi | +37% | -33% | **2,023** | +19% | 0.82 | -27% | beklenen aralıkta |
| BTC al-tut | – | – | **4,364** | +45% | 1.04 | -53% | – |

## Eleme motoru işe yarıyor mu? (kesimden sonra, eşit ağırlık, 1x)

| Grup | Strateji | $1000 → | Yıllık | Sharpe | Maks. düşüş | Kârlı strateji oranı | Medyan Sharpe |
|---|---|---|---|---|---|---|---|
| aktif | 79 | 1,253 | +6% | 0.57 | -20% | %58 | 0.37 |
| kontrol | 21 | 1,056 | +1% | 0.23 | -18% | %57 | 0.16 |

Backtest Sharpe sırası ile ileri Sharpe sırası arasındaki ilişki (Spearman): **0.014** (1 = backtest'te iyi olan ileride de iyi; 0 = ilişki yok).

## En iyi / en kötü 10 / 5 üye (ileri getiri)

- ✅ BTC/USDT rsi_midline (aktif): +182%, SR 1.35
- ✅ ETH/USDT smc_choch (aktif): +182%, SR 1.09
- ✅ BTC/USDT trix_cross (aktif): +156%, SR 1.33
- ✅ ETH/USDT smc_bos (aktif): +142%, SR 0.88
- ✅ BTC/USDT aroon_cross (aktif): +139%, SR 1.16
- ✅ XRP/USDT donchian_breakout (aktif): +134%, SR 0.8
- ✅ BTC/USDT linreg_slope (aktif): +122%, SR 1.14
- ✅ ETH/USDT keltner_breakout (aktif): +117%, SR 0.82
- ✅ ETH/USDT high_52w_break (aktif): +108%, SR 0.92
- ✅ ETH/USDT bollinger_breakout (aktif): +103%, SR 0.9
- ❌ XRP/USDT stoch_reversal (aktif): -60%, SR -0.65
- ❌ ETH/USDT engulfing (aktif): -60%, SR -0.78
- ❌ BCH/USDT stochrsi_reversal (aktif): -58%, SR -0.5
- ❌ ETC/USDT bollinger_breakout (aktif): -49%, SR -0.26
- ❌ ETC/USDT bb_squeeze (aktif): -48%, SR -0.64

## Zayıf yönler

- Eşikler 2026'da yazıldı; araştırmacı (ben) kesimden sonraki dönemi biliyordu. Eleme motoru o veriyi görmedi, ama tamamen kör değil.
- Coin listesi bugünün listesidir: kesimden sonra borsadan silinen coinler yok (survivorship).
- Tek bir kesim tarihi = tek bir senaryo. Başka bir tarihte sonuç farklı olabilir.