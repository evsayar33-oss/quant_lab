# Kasa koruma testi — crypto_alts 4h

Portföy: arenadaki **56 aktif üye**, eşit ağırlık, coin başı en fazla %20. Kabul kuralları sonuçlardan önce yazıldı (`config/arena.yaml` → `protection.accept`). Bir koruma sadece **komşu eşiklerin hepsinde** ve **her zaman diliminde** geçerse açılır.

## Korumasız portföy

Tüm geçmiş: CAGR +29.2%, Sharpe 2.322, maks. düşüş -6.8%, günlük CVaR95 -1.0%. Coin sınırı olmadan: maks. düşüş -11.2%.

Monte Carlo (1 yıl): P(düşüş ≤ −%50) = 0.0%, medyan +28%, kötü %5 +7%.

| Kriz | Getiri | Maks. düşüş |
|---|---|---|
| covid_2020 | +1.9% | -4.6% |
| may_2021 | +3.3% | -3.0% |
| luna_2022 | +7.2% | -2.9% |
| ftx_2022 | +2.8% | -4.4% |
| aug_2024 | +5.5% | -2.1% |
| oct_2025 | +3.3% | -1.5% |

## Kasa düşüş sigortası — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| (0.08, 0.16) | +29.2% | 2.322 | -6.8% | 0/6 | ✗✗✓✓ | kaldı |
|  | MC P(≤−%50): 0.0% (korumasız 0.0%) |  |  |  |  |  |
| (0.1, 0.2) | +29.2% | 2.322 | -6.8% | 0/6 | ✗✗✓✓ | kaldı |
|  | MC P(≤−%50): 0.0% (korumasız 0.0%) |  |  |  |  |  |
| (0.12, 0.25) | +29.2% | 2.322 | -6.8% | 0/6 | ✗✗✓✓ | kaldı |
|  | MC P(≤−%50): 0.0% (korumasız 0.0%) |  |  |  |  |  |

## Volatilite hedefi — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 0.25 | +29.2% | 2.322 | -6.8% | 0/6 | ✗✗✓✓ | kaldı |
| 0.35 | +29.2% | 2.322 | -6.8% | 0/6 | ✗✗✓✓ | kaldı |
| 0.5 | +29.2% | 2.322 | -6.8% | 0/6 | ✗✗✓✓ | kaldı |

## Kasa eğrisi filtresi — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 30 | +18.7% | 1.668 | -9.6% | 0/6 | ✗✗✗✗ | kaldı |
| 60 | +22.0% | 1.879 | -9.1% | 1/6 | ✗✗✗✓ | kaldı |
| 90 | +25.1% | 2.084 | -9.1% | 0/6 | ✗✗✗✓ | kaldı |

## Günlük kayıp limiti — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 0.04 | +29.2% | 2.322 | -6.8% | 0/6 | ✗✗✓✓ | kaldı |
| 0.05 | +29.2% | 2.322 | -6.8% | 0/6 | ✗✗✓✓ | kaldı |
| 0.07 | +29.2% | 2.322 | -6.8% | 0/6 | ✗✗✓✓ | kaldı |

## BTC çöküş bekçisi — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 0.08 | +28.9% | 2.303 | -6.8% | 0/6 | ✗✗✓✓ | kaldı |
| 0.1 | +28.9% | 2.307 | -6.8% | 0/6 | ✗✗✓✓ | kaldı |
| 0.15 | +29.2% | 2.322 | -6.8% | 0/6 | ✗✗✓✓ | kaldı |

## Felaket stopu — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 0.1 | +29.1% | 2.315 | -6.8% | 0/6 | ✗✗✓✓ | kaldı |
| 0.12 | +29.2% | 2.319 | -6.8% | 0/6 | ✗✗✓✓ | kaldı |
| 0.15 | +29.2% | 2.322 | -6.8% | 0/6 | ✗✗✓✓ | kaldı |

## Portföy seçenekleri ($1000 ile başlangıç, maliyet ve funding dahil)

| Portföy | Başlangıç | Bugün ($) | Yıllık | Sharpe | Maks. düşüş | En kötü yıl | Son 3y | Son 5y | En kötü kriz |
|---|---|---|---|---|---|---|---|---|---|
| Hepsi eşit ağırlık (56 strateji), 1x | 2018-07-31 | 9,458 | +31% | 2.4 | -7% | +6% (2018) | +195% | +327% | -5% |
| En iyi 10 (farklı coin), 1x | 2018-08-08 | 102,007 | +76% | 2.26 | -25% | +34% (2018) | +439% | +1076% | -12% |
| En iyi 5 (farklı coin), 1x | 2021-07-31 | 64,840 | +122% | 2.31 | -28% | +36% (2022) | +650% | +1649% | -9% |
| En iyi 5 (farklı coin), 2x | 2021-07-31 | 2,060,007 | +331% | 2.31 | -50% | +67% (2022) | +4597% | +20322% | -18% |
| En iyi 5 (farklı coin), 3x | 2021-07-31 | 32,460,104 | +631% | 2.31 | -66% | +83% (2022) | +24557% | +160481% | -27% |
| En iyi 5, 3x + düşüş sigortası (−%10 yarım / −%20 nakit) | 2021-07-31 | 54,102 | +115% | 1.46 | -65% | -29% (2022) | +2758% | +1926% | -17% |
| En iyi 5, 3x + volatilite hedefi %35 | 2021-07-31 | 266,290 | +191% | 2.69 | -29% | +54% (2022) | +3106% | +14063% | -9% |
| En iyi 10, ters volatilite ağırlık, 1x | 2018-08-08 | 89,790 | +73% | 2.17 | -17% | +11% (2018) | +336% | +685% | -8% |
| En iyi 10, HRP ağırlık, 1x | 2018-08-08 | 6,614 | +26% | 1.07 | -29% | +0% (2019) | +440% | +542% | -2% |
| En iyi 5, ters volatilite ağırlık, 1x | 2021-07-31 | 41,069 | +104% | 2.07 | -31% | -4% (2022) | +497% | +1062% | -10% |
| En iyi 5, HRP ağırlık, 1x | 2021-07-31 | 7,363 | +47% | 1.43 | -24% | +2% (2021) | +590% | +625% | -4% |
| Rastgele 5 strateji (300 deneme), 1x — medyan | – | 6,753 | – | 1.39 (p10–p90: 1.0–1.71) | -23% | – | – | – | – |
|  | En iyi 5'in Sharpe'ı 2.31: rastgele portföylerin %100'inden iyi |  |  |  |  |  |  |  |  |
| Karşılaştırma: BTC al-tut | 2018-07-26 | 10,014 | +32% | 0.77 | -77% | -64% (2022) | +178% | +29% | -55% |

## Likidasyon tamponu (matematik, test gerekmez)

Kural: likidasyon mesafesi ≥ 2.0 × felaket stop mesafesi → **en fazla 4.08x**.

| Kaldıraç | Likidasyon mesafesi | Kurala uygun | −%30 gap'te hayatta |
|---|---|---|---|
| 1x | %99.5 | ✓ | ✓ |
| 2x | %49.5 | ✓ | ✓ |
| 3x | %32.8 | ✓ | ✓ |
| 5x | %19.5 | ✗ | ✗ |
| 10x | %9.5 | ✗ | ✗ |
| 20x | %4.5 | ✗ | ✗ |

## Zayıf yönler

- Portföy, aynı geçmişte seçilmiş üyelerden oluşur; korumasız sonuç iyimserdir. Korumanın **farkı** daha güvenilirdir.
- Bar verisi kullanılır: bar içindeki ani iğneler (wick) ve borsa kesintileri modellenmez.
- Kriz sayısı az (en fazla 6). 'Krizlerin 2/3'ü' kuralı küçük örneklemle çalışır.
- Monte Carlo blokları geçmişten alınır; geçmişte hiç olmamış bir şok kapsanmaz.