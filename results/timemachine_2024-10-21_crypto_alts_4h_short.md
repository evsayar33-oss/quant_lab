# Zaman makinesi testi — 4h, kesim 2024-10-21

Her seçim **sadece 2024-10-21'e kadarki veriyle** yapıldı (eleme 25309 deneme, 23 coin). Sonra donmuş seçimlerin 2024-10-21 → 2026-10-21 arası gerçek sonucu ölçüldü. Kesimden sonra emekliye ayrılan üye: 62.

## Portföyler: backtest (kesime kadar) ↔ ileri (kesimden sonra)

| Portföy | Backtest yıllık | Backtest DD | **İleri: $1000 →** | İleri yıllık | İleri Sharpe | İleri maks. düşüş | Bant |
|---|---|---|---|---|---|---|---|
| A Hepsi eşit ağırlık, 1x | +22% | -8% | **1,027** | +1% | 0.17 | -10% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| B En iyi 10, 1x | +28% | -8% | **962** | -2% | -0.13 | -12% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| B2 En iyi 10, ters volatilite ağırlık, 1x | +38% | -18% | **979** | -1% | -0.06 | -9% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| C En iyi 5, 3x | +118% | -28% | **715** | -15% | -0.18 | -45% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| C2 En iyi 5, 3x + volatilite hedefi %35 | +86% | -21% | **734** | -14% | -0.38 | -41% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| K1 Çekirdek: BTC+ETH SMA200 + momentum + vol hedefi | +45% | -35% | **1,211** | +10% | 0.51 | -24% | beklenen aralıkta |
| K2 Çekirdek: BTC+ETH momentum + vol hedefi | +35% | -36% | **1,174** | +8% | 0.47 | -27% | beklenen aralıkta |
| BTC al-tut | – | – | **1,207** | +10% | 0.43 | -53% | – |

## Eleme motoru işe yarıyor mu? (kesimden sonra, eşit ağırlık, 1x)

| Grup | Strateji | $1000 → | Yıllık | Sharpe | Maks. düşüş | Kârlı strateji oranı | Medyan Sharpe |
|---|---|---|---|---|---|---|---|
| aktif | 78 | 902 | -5% | -0.28 | -23% | %31 | -0.17 |
| kontrol | 22 | 951 | -2% | -0.17 | -13% | %46 | 0.04 |

Backtest Sharpe sırası ile ileri Sharpe sırası arasındaki ilişki (Spearman): **0.203** (1 = backtest'te iyi olan ileride de iyi; 0 = ilişki yok).

## En iyi / en kötü 10 / 5 üye (ileri getiri)

- ✅ FIL/USDT macd_cross (aktif): +124%, SR 1.35
- ✅ ETC/USDT roc_breakout (aktif): +91%, SR 1.29
- ✅ UNI/USDT supertrend_flip (aktif): +67%, SR 0.84
- ✅ AXS/USDT supertrend_flip (aktif): +60%, SR 0.95
- ✅ ETH/USDT bollinger_breakout (aktif): +34%, SR 0.95
- ✅ UNI/USDT ichimoku_cloud (aktif): +32%, SR 0.58
- ✅ DOGE/USDT awesome_zero (kontrol): +29%, SR 0.54
- ✅ BCH/USDT bollinger_breakout (aktif): +28%, SR 0.83
- ✅ DOT/USDT bb_squeeze (aktif): +24%, SR 0.49
- ✅ AXS/USDT trix_cross (aktif): +21%, SR 0.44
- ❌ FIL/USDT bollinger_breakout (aktif): -78%, SR -1.34
- ❌ FIL/USDT ichimoku_cloud (aktif): -74%, SR -1.11
- ❌ FIL/USDT macd_zero (aktif): -68%, SR -0.66
- ❌ FIL/USDT rsi_midline (aktif): -64%, SR -0.97
- ❌ FIL/USDT donchian_breakout (aktif): -62%, SR -0.85

## Zayıf yönler

- Eşikler 2026'da yazıldı; araştırmacı (ben) kesimden sonraki dönemi biliyordu. Eleme motoru o veriyi görmedi, ama tamamen kör değil.
- Coin listesi bugünün listesidir: kesimden sonra borsadan silinen coinler yok (survivorship).
- Tek bir kesim tarihi = tek bir senaryo. Başka bir tarihte sonuç farklı olabilir.