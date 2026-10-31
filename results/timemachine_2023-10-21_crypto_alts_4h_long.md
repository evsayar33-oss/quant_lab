# Zaman makinesi testi — 4h, kesim 2023-10-21

Her seçim **sadece 2023-10-21'e kadarki veriyle** yapıldı (eleme 19730 deneme, 12 coin). Sonra donmuş seçimlerin 2023-10-21 → 2026-10-21 arası gerçek sonucu ölçüldü. Kesimden sonra emekliye ayrılan üye: 40.

## Portföyler: backtest (kesime kadar) ↔ ileri (kesimden sonra)

| Portföy | Backtest yıllık | Backtest DD | **İleri: $1000 →** | İleri yıllık | İleri Sharpe | İleri maks. düşüş | Bant |
|---|---|---|---|---|---|---|---|
| A Hepsi eşit ağırlık, 1x | +31% | -6% | **1,171** | +5% | 0.94 | -8% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| B En iyi 10, 1x | +38% | -8% | **1,103** | +3% | 0.54 | -9% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| B2 En iyi 10, ters volatilite ağırlık, 1x | +39% | -24% | **1,103** | +3% | 0.58 | -9% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| C En iyi 5, 3x | +186% | -38% | **2,157** | +29% | 0.9 | -42% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| C2 En iyi 5, 3x + volatilite hedefi %35 | +118% | -31% | **1,771** | +21% | 0.78 | -40% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| K1 Çekirdek: BTC+ETH SMA200 + momentum + vol hedefi | +40% | -35% | **2,013** | +26% | 0.98 | -24% | beklenen aralıkta |
| K2 Çekirdek: BTC+ETH momentum + vol hedefi | +30% | -36% | **1,943** | +25% | 0.99 | -27% | beklenen aralıkta |
| BTC al-tut | – | – | **2,809** | +41% | 0.98 | -53% | – |

## Eleme motoru işe yarıyor mu? (kesimden sonra, eşit ağırlık, 1x)

| Grup | Strateji | $1000 → | Yıllık | Sharpe | Maks. düşüş | Kârlı strateji oranı | Medyan Sharpe |
|---|---|---|---|---|---|---|---|
| aktif | 68 | 1,167 | +5% | 0.68 | -14% | %60 | 0.28 |
| kontrol | 32 | 1,072 | +2% | 0.35 | -15% | %34 | -0.1 |

Backtest Sharpe sırası ile ileri Sharpe sırası arasındaki ilişki (Spearman): **0.188** (1 = backtest'te iyi olan ileride de iyi; 0 = ilişki yok).

## En iyi / en kötü 10 / 5 üye (ileri getiri)

- ✅ AVAX/USDT inside_bar (kontrol): +284%, SR 1.12
- ✅ BTC/USDT price_ma (aktif): +202%, SR 1.46
- ✅ ETH/USDT smc_choch (aktif): +138%, SR 1.2
- ✅ BTC/USDT triple_ma (kontrol): +118%, SR 1.61
- ✅ ETH/USDT keltner_breakout (aktif): +118%, SR 1.01
- ✅ ETH/USDT price_ma (aktif): +114%, SR 1.12
- ✅ ETH/USDT bollinger_breakout (aktif): +110%, SR 1.17
- ✅ XRP/USDT high_52w_break (aktif): +107%, SR 1.25
- ✅ BTC/USDT rsi_midline (aktif): +87%, SR 1.12
- ✅ XRP/USDT keltner_breakout (aktif): +87%, SR 0.8
- ❌ BCH/USDT donchian_breakout (aktif): -80%, SR -1.55
- ❌ ETH/USDT engulfing (kontrol): -58%, SR -1.04
- ❌ BCH/USDT high_52w_break (aktif): -57%, SR -1.06
- ❌ XRP/USDT stoch_reversal (aktif): -51%, SR -1.19
- ❌ BCH/USDT ma_cross (aktif): -45%, SR -1.19

## Zayıf yönler

- Eşikler 2026'da yazıldı; araştırmacı (ben) kesimden sonraki dönemi biliyordu. Eleme motoru o veriyi görmedi, ama tamamen kör değil.
- Coin listesi bugünün listesidir: kesimden sonra borsadan silinen coinler yok (survivorship).
- Tek bir kesim tarihi = tek bir senaryo. Başka bir tarihte sonuç farklı olabilir.