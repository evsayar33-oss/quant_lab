# Zaman makinesi testi — 1d, kesim 2024-10-21

Her seçim **sadece 2024-10-21'e kadarki veriyle** yapıldı (eleme 22799 deneme, 18 coin). Sonra donmuş seçimlerin 2024-10-21 → 2026-10-20 arası gerçek sonucu ölçüldü. Kesimden sonra emekliye ayrılan üye: 14.

## Portföyler: backtest (kesime kadar) ↔ ileri (kesimden sonra)

| Portföy | Backtest yıllık | Backtest DD | **İleri: $1000 →** | İleri yıllık | İleri Sharpe | İleri maks. düşüş | Bant |
|---|---|---|---|---|---|---|---|
| A Hepsi eşit ağırlık, 1x | +33% | -13% | **1,155** | +8% | 0.75 | -14% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| B En iyi 10, 1x | +35% | -15% | **1,269** | +13% | 0.91 | -20% | beklenen aralıkta |
| B2 En iyi 10, ters volatilite ağırlık, 1x | +55% | -21% | **1,713** | +31% | 1.04 | -17% | beklenen aralıkta |
| C En iyi 5, 3x | +146% | -49% | **3,493** | +87% | 1.32 | -43% | beklenen aralıkta |
| C2 En iyi 5, 3x + volatilite hedefi %35 | +91% | -41% | **2,778** | +67% | 1.48 | -31% | beklenen aralıkta |
| K1 Çekirdek: BTC+ETH SMA200 + momentum + vol hedefi | +40% | -39% | **1,201** | +10% | 0.5 | -22% | beklenen aralıkta |
| K2 Çekirdek: BTC+ETH momentum + vol hedefi | +33% | -36% | **1,150** | +7% | 0.42 | -27% | beklenen aralıkta |
| BTC al-tut | – | – | **1,232** | +11% | 0.46 | -53% | – |

## Eleme motoru işe yarıyor mu? (kesimden sonra, eşit ağırlık, 1x)

| Grup | Strateji | $1000 → | Yıllık | Sharpe | Maks. düşüş | Kârlı strateji oranı | Medyan Sharpe |
|---|---|---|---|---|---|---|---|
| aktif | 21 | 1,177 | +9% | 0.63 | -18% | %43 | 0.11 |
| kontrol | 79 | 862 | -7% | -0.29 | -36% | %28 | -0.06 |

Backtest Sharpe sırası ile ileri Sharpe sırası arasındaki ilişki (Spearman): **0.044** (1 = backtest'te iyi olan ileride de iyi; 0 = ilişki yok).

## En iyi / en kötü 10 / 5 üye (ileri getiri)

- ✅ ETH/USDT ma_cross (aktif): +172%, SR 1.42
- ✅ TRX/USDT smc_ote (aktif): +136%, SR 0.84
- ✅ UNI/USDT smc_liquidity_sweep (kontrol): +115%, SR 0.96
- ✅ ETH/USDT vwap_cross (kontrol): +82%, SR 0.96
- ✅ ETH/USDT smc_bos (aktif): +63%, SR 0.81
- ✅ TRX/USDT awesome_zero (kontrol): +57%, SR 0.57
- ✅ BTC/USDT chaikin_osc (kontrol): +50%, SR 0.91
- ✅ ETH/USDT supertrend_flip (aktif): +49%, SR 0.67
- ✅ TRX/USDT vortex_cross (kontrol): +38%, SR 0.48
- ✅ BTC/USDT ichimoku_cloud (kontrol): +38%, SR 0.81
- ❌ SNX/USDT stoch_reversal (kontrol): -88%, SR -1.51
- ❌ BCH/USDT cci_breakout (kontrol): -78%, SR -1.95
- ❌ SOL/USDT chaikin_osc (kontrol): -70%, SR -0.88
- ❌ THETA/USDT cmf_flow (kontrol): -68%, SR -1.05
- ❌ SOL/USDT stoch_reversal (kontrol): -66%, SR -0.78

## Zayıf yönler

- Eşikler 2026'da yazıldı; araştırmacı (ben) kesimden sonraki dönemi biliyordu. Eleme motoru o veriyi görmedi, ama tamamen kör değil.
- Coin listesi bugünün listesidir: kesimden sonra borsadan silinen coinler yok (survivorship).
- Tek bir kesim tarihi = tek bir senaryo. Başka bir tarihte sonuç farklı olabilir.