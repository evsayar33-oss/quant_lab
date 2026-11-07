# Zaman makinesi testi — 1d, kesim 2024-10-21

Her seçim **sadece 2024-10-21'e kadarki veriyle** yapıldı (eleme 15240 deneme, 18 coin). Sonra donmuş seçimlerin 2024-10-21 → 2026-10-20 arası gerçek sonucu ölçüldü. Kesimden sonra emekliye ayrılan üye: 10.

## Portföyler: backtest (kesime kadar) ↔ ileri (kesimden sonra)

| Portföy | Backtest yıllık | Backtest DD | **İleri: $1000 →** | İleri yıllık | İleri Sharpe | İleri maks. düşüş | Bant |
|---|---|---|---|---|---|---|---|
| A Hepsi eşit ağırlık, 1x | +47% | -13% | **886** | -6% | -0.75 | -14% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| B En iyi 10, 1x | +49% | -14% | **873** | -7% | -0.92 | -16% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| B2 En iyi 10, ters volatilite ağırlık, 1x | +47% | -27% | **800** | -11% | -1.15 | -25% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| C En iyi 5, 3x | +181% | -38% | **644** | -20% | -0.92 | -43% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| C2 En iyi 5, 3x + volatilite hedefi %35 | +78% | -32% | **748** | -14% | -1.07 | -30% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| K1 Çekirdek: BTC+ETH SMA200 + momentum + vol hedefi | +40% | -39% | **1,201** | +10% | 0.5 | -22% | beklenen aralıkta |
| K2 Çekirdek: BTC+ETH momentum + vol hedefi | +33% | -36% | **1,150** | +7% | 0.42 | -27% | beklenen aralıkta |
| BTC al-tut | – | – | **1,232** | +11% | 0.46 | -53% | – |

## Eleme motoru işe yarıyor mu? (kesimden sonra, eşit ağırlık, 1x)

| Grup | Strateji | $1000 → | Yıllık | Sharpe | Maks. düşüş | Kârlı strateji oranı | Medyan Sharpe |
|---|---|---|---|---|---|---|---|
| aktif | 10 | 679 | -18% | -0.7 | -35% | %0 | -0.35 |
| kontrol | 56 | 843 | -8% | -0.29 | -22% | %29 | -0.25 |

Backtest Sharpe sırası ile ileri Sharpe sırası arasındaki ilişki (Spearman): **-0.026** (1 = backtest'te iyi olan ileride de iyi; 0 = ilişki yok).

## En iyi / en kötü 10 / 5 üye (ileri getiri)

- ✅ AAVE/USDT down_days (kontrol): +112%, SR 0.93
- ✅ FIL/USDT smc_order_block (kontrol): +87%, SR 0.83
- ✅ FIL/USDT stoch_reversal (kontrol): +79%, SR 0.86
- ✅ SOL/USDT smc_liquidity_sweep (kontrol): +55%, SR 0.85
- ✅ UNI/USDT williams_reversal (kontrol): +47%, SR 0.67
- ✅ AXS/USDT mfi_reversal (kontrol): +36%, SR 0.55
- ✅ FIL/USDT ibs_reversion (kontrol): +34%, SR 0.6
- ✅ SOL/USDT price_ma (kontrol): +27%, SR 0.49
- ✅ UNI/USDT smc_ote (kontrol): +25%, SR 0.53
- ✅ FIL/USDT rsi_midline (kontrol): +19%, SR 0.43
- ❌ FIL/USDT smc_fvg (kontrol): -75%, SR -0.81
- ❌ AXS/USDT stochrsi_reversal (kontrol): -74%, SR -0.46
- ❌ FIL/USDT heikin_ashi (kontrol): -72%, SR -1.19
- ❌ AXS/USDT tsi_cross (kontrol): -69%, SR -0.7
- ❌ FIL/USDT chaikin_osc (aktif): -67%, SR -1.18

## Zayıf yönler

- Eşikler 2026'da yazıldı; araştırmacı (ben) kesimden sonraki dönemi biliyordu. Eleme motoru o veriyi görmedi, ama tamamen kör değil.
- Coin listesi bugünün listesidir: kesimden sonra borsadan silinen coinler yok (survivorship).
- Tek bir kesim tarihi = tek bir senaryo. Başka bir tarihte sonuç farklı olabilir.