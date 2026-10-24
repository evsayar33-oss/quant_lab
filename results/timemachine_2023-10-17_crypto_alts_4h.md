# Zaman makinesi testi — 4h, kesim 2023-10-17

Her seçim **sadece 2023-10-17'e kadarki veriyle** yapıldı (eleme 11210 deneme, 12 coin). Sonra donmuş seçimlerin 2023-10-17 → 2026-10-19 arası gerçek sonucu ölçüldü. Kesimden sonra emekliye ayrılan üye: 11.

## Portföyler: backtest (kesime kadar) ↔ ileri (kesimden sonra)

| Portföy | Backtest yıllık | Backtest DD | **İleri: $1000 →** | İleri yıllık | İleri Sharpe | İleri maks. düşüş | Bant |
|---|---|---|---|---|---|---|---|
| A Hepsi eşit ağırlık, 1x | +35% | -9% | **1,147** | +5% | 0.65 | -8% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| B En iyi 10, 1x | +43% | -8% | **1,223** | +7% | 0.83 | -14% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| B2 En iyi 10, ters volatilite ağırlık, 1x | +47% | -14% | **1,229** | +7% | 1.0 | -7% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| C En iyi 5, 3x | +250% | -32% | **2,247** | +31% | 0.9 | -48% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| C2 En iyi 5, 3x + volatilite hedefi %35 | +120% | -26% | **2,244** | +31% | 1.01 | -41% | beklenen aralıkta |
| K1 Çekirdek: BTC+ETH SMA200 + momentum + vol hedefi | +40% | -35% | **2,041** | +27% | 0.99 | -24% | beklenen aralıkta |
| K2 Çekirdek: BTC+ETH momentum + vol hedefi | +30% | -36% | **1,957** | +25% | 1.0 | -27% | beklenen aralıkta |
| BTC al-tut | – | – | **2,919** | +43% | 1.01 | -53% | – |

## Eleme motoru işe yarıyor mu? (kesimden sonra, eşit ağırlık, 1x)

| Grup | Strateji | $1000 → | Yıllık | Sharpe | Maks. düşüş | Kârlı strateji oranı | Medyan Sharpe |
|---|---|---|---|---|---|---|---|
| aktif | 17 | 1,039 | +1% | 0.18 | -20% | %47 | 0.02 |
| kontrol | 38 | 873 | -4% | -0.19 | -32% | %34 | -0.12 |

Backtest Sharpe sırası ile ileri Sharpe sırası arasındaki ilişki (Spearman): **0.352** (1 = backtest'te iyi olan ileride de iyi; 0 = ilişki yok).

## En iyi / en kötü 10 / 5 üye (ileri getiri)

- ✅ ETH/USDT bollinger_breakout (aktif): +138%, SR 1.14
- ✅ XRP/USDT high_52w_break (aktif): +107%, SR 1.25
- ✅ DOT/USDT macd_divergence (kontrol): +102%, SR 0.92
- ✅ AVAX/USDT keltner_breakout (kontrol): +101%, SR 0.72
- ✅ BTC/USDT chop_switch (kontrol): +98%, SR 1.66
- ✅ AVAX/USDT bollinger_breakout (kontrol): +81%, SR 0.64
- ✅ ETC/USDT high_52w_break (kontrol): +80%, SR 0.71
- ✅ ETH/USDT high_52w_break (aktif): +74%, SR 0.91
- ✅ BTC/USDT bb_squeeze (aktif): +30%, SR 0.57
- ✅ ETH/USDT triple_ma (kontrol): +28%, SR 0.4
- ❌ AVAX/USDT smc_fvg (kontrol): -86%, SR -0.71
- ❌ ETC/USDT triple_ma (kontrol): -85%, SR -0.78
- ❌ ALGO/USDT williams_reversal (kontrol): -78%, SR -0.9
- ❌ BCH/USDT donchian_breakout (kontrol): -73%, SR -0.97
- ❌ ETC/USDT donchian_breakout (aktif): -72%, SR -1.0

## Zayıf yönler

- Eşikler 2026'da yazıldı; araştırmacı (ben) kesimden sonraki dönemi biliyordu. Eleme motoru o veriyi görmedi, ama tamamen kör değil.
- Coin listesi bugünün listesidir: kesimden sonra borsadan silinen coinler yok (survivorship).
- Tek bir kesim tarihi = tek bir senaryo. Başka bir tarihte sonuç farklı olabilir.