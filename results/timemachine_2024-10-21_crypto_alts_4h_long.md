# Zaman makinesi testi — 4h, kesim 2024-10-21

Her seçim **sadece 2024-10-21'e kadarki veriyle** yapıldı (eleme 26287 deneme, 23 coin). Sonra donmuş seçimlerin 2024-10-21 → 2026-10-21 arası gerçek sonucu ölçüldü. Kesimden sonra emekliye ayrılan üye: 52.

## Portföyler: backtest (kesime kadar) ↔ ileri (kesimden sonra)

| Portföy | Backtest yıllık | Backtest DD | **İleri: $1000 →** | İleri yıllık | İleri Sharpe | İleri maks. düşüş | Bant |
|---|---|---|---|---|---|---|---|
| A Hepsi eşit ağırlık, 1x | +33% | -6% | **1,017** | +1% | 0.16 | -9% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| B En iyi 10, 1x | +47% | -10% | **1,081** | +4% | 0.5 | -7% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| B2 En iyi 10, ters volatilite ağırlık, 1x | +78% | -19% | **1,087** | +4% | 0.54 | -8% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| C En iyi 5, 3x | +295% | -43% | **1,502** | +23% | 0.71 | -29% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| C2 En iyi 5, 3x + volatilite hedefi %35 | +105% | -30% | **1,371** | +17% | 0.69 | -24% | ⚠️ beklenen aralığın ALTINDA: backtest gibi davranmıyor olabilir |
| K1 Çekirdek: BTC+ETH SMA200 + momentum + vol hedefi | +45% | -35% | **1,211** | +10% | 0.51 | -24% | beklenen aralıkta |
| K2 Çekirdek: BTC+ETH momentum + vol hedefi | +35% | -36% | **1,174** | +8% | 0.47 | -27% | beklenen aralıkta |
| BTC al-tut | – | – | **1,207** | +10% | 0.43 | -53% | – |

## Eleme motoru işe yarıyor mu? (kesimden sonra, eşit ağırlık, 1x)

| Grup | Strateji | $1000 → | Yıllık | Sharpe | Maks. düşüş | Kârlı strateji oranı | Medyan Sharpe |
|---|---|---|---|---|---|---|---|
| aktif | 73 | 976 | -1% | -0.08 | -15% | %40 | -0.01 |
| kontrol | 27 | 1,032 | +2% | 0.23 | -15% | %52 | 0.14 |

Backtest Sharpe sırası ile ileri Sharpe sırası arasındaki ilişki (Spearman): **-0.056** (1 = backtest'te iyi olan ileride de iyi; 0 = ilişki yok).

## En iyi / en kötü 10 / 5 üye (ileri getiri)

- ✅ ETH/USDT price_ma (aktif): +71%, SR 1.01
- ✅ SOL/USDT adx_trend (kontrol): +57%, SR 0.88
- ✅ ETH/USDT roc_breakout (aktif): +54%, SR 0.84
- ✅ BTC/USDT price_ma (aktif): +53%, SR 0.98
- ✅ SOL/USDT ichimoku_cloud (aktif): +53%, SR 0.85
- ✅ BTC/USDT roc_breakout (kontrol): +52%, SR 0.96
- ✅ SOL/USDT chop_switch (kontrol): +48%, SR 0.9
- ✅ BTC/USDT triple_ma (kontrol): +47%, SR 1.29
- ✅ DOGE/USDT rsi_divergence (kontrol): +42%, SR 0.91
- ✅ ETH/USDT stoch_reversal (aktif): +41%, SR 0.93
- ❌ XRP/USDT stoch_reversal (aktif): -56%, SR -0.91
- ❌ FIL/USDT triple_ma (aktif): -53%, SR -1.93
- ❌ MINA/USDT down_days (kontrol): -50%, SR -1.94
- ❌ BCH/USDT volume_breakout (aktif): -48%, SR -1.06
- ❌ AVAX/USDT ppo_cross (aktif): -48%, SR -1.63

## Zayıf yönler

- Eşikler 2026'da yazıldı; araştırmacı (ben) kesimden sonraki dönemi biliyordu. Eleme motoru o veriyi görmedi, ama tamamen kör değil.
- Coin listesi bugünün listesidir: kesimden sonra borsadan silinen coinler yok (survivorship).
- Tek bir kesim tarihi = tek bir senaryo. Başka bir tarihte sonuç farklı olabilir.