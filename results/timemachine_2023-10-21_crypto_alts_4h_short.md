# Zaman makinesi testi — 4h, kesim 2023-10-21

Her seçim **sadece 2023-10-21'e kadarki veriyle** yapıldı (eleme 9199 deneme, 12 coin). Sonra donmuş seçimlerin 2023-10-21 → 2026-10-21 arası gerçek sonucu ölçüldü. Kesimden sonra emekliye ayrılan üye: 9.

## Portföyler: backtest (kesime kadar) ↔ ileri (kesimden sonra)

| Portföy | Backtest yıllık | Backtest DD | **İleri: $1000 →** | İleri yıllık | İleri Sharpe | İleri maks. düşüş | Bant |
|---|---|---|---|---|---|---|---|
| A Hepsi eşit ağırlık, 1x | +30% | -7% | **1,014** | +0% | 0.17 | -6% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| B En iyi 10, 1x | +29% | -9% | **1,048** | +2% | 0.47 | -6% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| B2 En iyi 10, ters volatilite ağırlık, 1x | +33% | -14% | **1,143** | +5% | 1.1 | -3% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| C En iyi 5, 3x | +136% | -33% | **1,228** | +7% | 0.55 | -22% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| C2 En iyi 5, 3x + volatilite hedefi %35 | +88% | -28% | **1,231** | +7% | 0.55 | -22% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| K1 Çekirdek: BTC+ETH SMA200 + momentum + vol hedefi | +40% | -35% | **2,013** | +26% | 0.98 | -24% | beklenen aralıkta |
| K2 Çekirdek: BTC+ETH momentum + vol hedefi | +30% | -36% | **1,943** | +25% | 0.99 | -27% | beklenen aralıkta |
| BTC al-tut | – | – | **2,809** | +41% | 0.98 | -53% | – |

## Eleme motoru işe yarıyor mu? (kesimden sonra, eşit ağırlık, 1x)

| Grup | Strateji | $1000 → | Yıllık | Sharpe | Maks. düşüş | Kârlı strateji oranı | Medyan Sharpe |
|---|---|---|---|---|---|---|---|
| aktif | 10 | 903 | -3% | -0.27 | -13% | %20 | -0.18 |
| kontrol | 22 | 812 | -7% | -0.78 | -19% | %18 | -0.38 |

Backtest Sharpe sırası ile ileri Sharpe sırası arasındaki ilişki (Spearman): **0.116** (1 = backtest'te iyi olan ileride de iyi; 0 = ilişki yok).

## En iyi / en kötü 10 / 5 üye (ileri getiri)

- ✅ DOT/USDT bb_squeeze (aktif): +97%, SR 1.27
- ✅ ETH/USDT bollinger_breakout (aktif): +83%, SR 0.99
- ✅ CRV/USDT roc_breakout (kontrol): +52%, SR 0.62
- ✅ DOT/USDT roc_breakout (kontrol): +32%, SR 0.46
- ✅ AVAX/USDT macd_divergence (kontrol): +7%, SR 0.22
- ✅ ALGO/USDT bb_squeeze (kontrol): +4%, SR 0.21
- ✅ BCH/USDT aroon_cross (aktif): -0%, SR 0.14
- ✅ BCH/USDT bollinger_breakout (aktif): -5%, SR 0.04
- ✅ BCH/USDT ichimoku_cloud (kontrol): -8%, SR 0.01
- ✅ ETH/USDT ma_cross (kontrol): -11%, SR -0.46
- ❌ CRV/USDT linreg_slope (kontrol): -63%, SR -0.7
- ❌ CRV/USDT donchian_breakout (aktif): -58%, SR -1.12
- ❌ ALGO/USDT williams_reversal (kontrol): -54%, SR -0.96
- ❌ CRV/USDT ichimoku_cloud (aktif): -50%, SR -0.58
- ❌ ETC/USDT triple_ma (kontrol): -48%, SR -0.6

## Zayıf yönler

- Eşikler 2026'da yazıldı; araştırmacı (ben) kesimden sonraki dönemi biliyordu. Eleme motoru o veriyi görmedi, ama tamamen kör değil.
- Coin listesi bugünün listesidir: kesimden sonra borsadan silinen coinler yok (survivorship).
- Tek bir kesim tarihi = tek bir senaryo. Başka bir tarihte sonuç farklı olabilir.