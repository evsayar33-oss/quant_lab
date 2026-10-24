# Zaman makinesi testi — 4h, kesim 2022-10-17

Her seçim **sadece 2022-10-17'e kadarki veriyle** yapıldı (eleme 10467 deneme, 9 coin). Sonra donmuş seçimlerin 2022-10-17 → 2026-10-19 arası gerçek sonucu ölçüldü. Kesimden sonra emekliye ayrılan üye: 20.

## Portföyler: backtest (kesime kadar) ↔ ileri (kesimden sonra)

| Portföy | Backtest yıllık | Backtest DD | **İleri: $1000 →** | İleri yıllık | İleri Sharpe | İleri maks. düşüş | Bant |
|---|---|---|---|---|---|---|---|
| A Hepsi eşit ağırlık, 1x | +49% | -12% | **1,016** | +0% | 0.11 | -7% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| B En iyi 10, 1x | +60% | -11% | **898** | -3% | -0.65 | -16% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| B2 En iyi 10, ters volatilite ağırlık, 1x | +56% | -16% | **885** | -3% | -0.7 | -16% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| C En iyi 5, 3x | +329% | -30% | **648** | -10% | -0.6 | -50% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| C2 En iyi 5, 3x + volatilite hedefi %35 | +154% | -26% | **775** | -6% | -0.41 | -38% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| K1 Çekirdek: BTC+ETH SMA200 + momentum + vol hedefi | +48% | -35% | **2,311** | +23% | 0.88 | -24% | beklenen aralıkta |
| K2 Çekirdek: BTC+ETH momentum + vol hedefi | +38% | -33% | **2,004** | +19% | 0.81 | -27% | beklenen aralıkta |
| BTC al-tut | – | – | **4,300** | +44% | 1.03 | -53% | – |

## Eleme motoru işe yarıyor mu? (kesimden sonra, eşit ağırlık, 1x)

| Grup | Strateji | $1000 → | Yıllık | Sharpe | Maks. düşüş | Kârlı strateji oranı | Medyan Sharpe |
|---|---|---|---|---|---|---|---|
| aktif | 24 | 1,152 | +4% | 0.37 | -17% | %62 | 0.14 |
| kontrol | 42 | 623 | -11% | -0.8 | -41% | %17 | -0.3 |

Backtest Sharpe sırası ile ileri Sharpe sırası arasındaki ilişki (Spearman): **0.096** (1 = backtest'te iyi olan ileride de iyi; 0 = ilişki yok).

## En iyi / en kötü 10 / 5 üye (ileri getiri)

- ✅ ETH/USDT bollinger_breakout (aktif): +120%, SR 0.81
- ✅ ETH/USDT high_52w_break (aktif): +108%, SR 0.92
- ✅ XRP/USDT donchian_breakout (aktif): +91%, SR 0.59
- ✅ BCH/USDT bollinger_breakout (kontrol): +90%, SR 0.69
- ✅ BTC/USDT roc_breakout (kontrol): +56%, SR 0.74
- ✅ ETH/USDT rsi_midline (aktif): +52%, SR 0.48
- ✅ BTC/USDT keltner_breakout (aktif): +52%, SR 0.52
- ✅ BTC/USDT atr_breakout (aktif): +51%, SR 0.68
- ✅ ETH/USDT chop_switch (kontrol): +38%, SR 0.51
- ✅ ETH/USDT atr_breakout (aktif): +27%, SR 0.34
- ❌ ETC/USDT linreg_slope (kontrol): -93%, SR -0.72
- ❌ ETC/USDT roc_breakout (kontrol): -92%, SR -0.98
- ❌ BCH/USDT roc_breakout (kontrol): -85%, SR -0.92
- ❌ ETC/USDT donchian_breakout (kontrol): -84%, SR -0.68
- ❌ ALGO/USDT williams_reversal (kontrol): -84%, SR -0.84

## Zayıf yönler

- Eşikler 2026'da yazıldı; araştırmacı (ben) kesimden sonraki dönemi biliyordu. Eleme motoru o veriyi görmedi, ama tamamen kör değil.
- Coin listesi bugünün listesidir: kesimden sonra borsadan silinen coinler yok (survivorship).
- Tek bir kesim tarihi = tek bir senaryo. Başka bir tarihte sonuç farklı olabilir.