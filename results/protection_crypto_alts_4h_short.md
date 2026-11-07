# Kasa koruma testi — crypto_alts 4h

Portföy: arenadaki **100 aktif üye**, eşit ağırlık, coin başı en fazla %20. Kabul kuralları sonuçlardan önce yazıldı (`config/arena.yaml` → `protection.accept`). Bir koruma sadece **komşu eşiklerin hepsinde** ve **her zaman diliminde** geçerse açılır.

## Korumasız portföy

Tüm geçmiş: CAGR +17.0%, Sharpe 1.437, maks. düşüş -17.1%, günlük CVaR95 -1.0%. Coin sınırı olmadan: maks. düşüş -23.6%.

Monte Carlo (1 yıl): P(düşüş ≤ −%50) = 0.0%, medyan +16%, kötü %5 -2%.

| Kriz | Getiri | Maks. düşüş |
|---|---|---|
| covid_2020 | +3.1% | -2.3% |
| may_2021 | +11.8% | -5.2% |
| luna_2022 | +12.5% | -2.9% |
| ftx_2022 | +5.2% | -4.5% |
| aug_2024 | +7.3% | -2.9% |
| oct_2025 | +3.1% | -0.7% |

## Kasa düşüş sigortası — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| (0.08, 0.16) | +15.4% | 1.428 | -14.2% | 1/6 | ✗✓✓✓ | kaldı |
|  | MC P(≤−%50): 0.0% (korumasız 0.0%) |  |  |  |  |  |
| (0.1, 0.2) | +16.2% | 1.447 | -13.7% | 1/6 | ✗✓✓✓ | kaldı |
|  | MC P(≤−%50): 0.0% (korumasız 0.0%) |  |  |  |  |  |
| (0.12, 0.25) | +16.5% | 1.438 | -14.7% | 1/6 | ✗✓✓✓ | kaldı |
|  | MC P(≤−%50): 0.0% (korumasız 0.0%) |  |  |  |  |  |

## Volatilite hedefi — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 0.25 | +17.2% | 1.455 | -17.1% | 0/6 | ✗✗✓✓ | kaldı |
| 0.35 | +17.0% | 1.437 | -17.1% | 0/6 | ✗✗✓✓ | kaldı |
| 0.5 | +17.0% | 1.437 | -17.1% | 0/6 | ✗✗✓✓ | kaldı |

## Kasa eğrisi filtresi — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 30 | +11.1% | 1.072 | -15.0% | 1/6 | ✗✓✗✗ | kaldı |
| 60 | +11.9% | 1.134 | -13.7% | 1/6 | ✗✓✗✗ | kaldı |
| 90 | +11.6% | 1.136 | -13.3% | 0/6 | ✗✓✗✗ | kaldı |

## Günlük kayıp limiti — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 0.04 | +17.0% | 1.437 | -17.1% | 0/6 | ✗✗✓✓ | kaldı |
| 0.05 | +17.0% | 1.437 | -17.1% | 0/6 | ✗✗✓✓ | kaldı |
| 0.07 | +17.0% | 1.437 | -17.1% | 0/6 | ✗✗✓✓ | kaldı |

## BTC çöküş bekçisi — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 0.08 | +17.0% | 1.437 | -17.1% | 0/6 | ✗✗✓✓ | kaldı |
| 0.1 | +17.0% | 1.437 | -17.1% | 0/6 | ✗✗✓✓ | kaldı |
| 0.15 | +17.0% | 1.437 | -17.1% | 0/6 | ✗✗✓✓ | kaldı |

## Felaket stopu — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 0.1 | +17.2% | 1.449 | -16.5% | 0/6 | ✗✓✓✓ | kaldı |
| 0.12 | +17.2% | 1.45 | -16.5% | 0/6 | ✗✓✓✓ | kaldı |
| 0.15 | +17.2% | 1.451 | -16.5% | 0/6 | ✗✓✓✓ | kaldı |

## Portföy seçenekleri ($1000 ile başlangıç, maliyet ve funding dahil)

| Portföy | Başlangıç | Bugün ($) | Yıllık | Sharpe | Maks. düşüş | En kötü yıl | Son 3y | Son 5y | En kötü kriz |
|---|---|---|---|---|---|---|---|---|---|
| Hepsi eşit ağırlık (100 strateji), 1x | 2018-01-16 | 4,006 | +17% | 1.44 | -17% | -3% (2020) | +117% | +245% | -5% |
| En iyi 10 (farklı coin), 1x | 2018-01-16 | 6,091 | +23% | 1.11 | -34% | -11% (2020) | +185% | +461% | -10% |
| En iyi 5 (farklı coin), 1x | 2020-09-11 | 7,126 | +38% | 1.3 | -41% | -23% (2021) | +270% | +886% | -16% |
| En iyi 5 (farklı coin), 2x | 2020-09-11 | 32,085 | +76% | 1.3 | -69% | -49% (2021) | +1115% | +7625% | -30% |
| En iyi 5 (farklı coin), 3x | 2020-09-11 | 91,540 | +109% | 1.3 | -86% | -71% (2021) | +3434% | +48292% | -43% |
| En iyi 5, 3x + düşüş sigortası (−%10 yarım / −%20 nakit) | 2020-09-11 | 4,934 | +30% | 0.87 | -62% | -57% (2020) | +811% | +1050% | -17% |
| En iyi 5, 3x + volatilite hedefi %35 | 2020-09-11 | 24,097 | +68% | 1.5 | -60% | -38% (2020) | +869% | +5305% | -15% |
| En iyi 10, ters volatilite ağırlık, 1x | 2018-01-16 | 6,313 | +23% | 1.12 | -34% | -4% (2020) | +176% | +448% | -7% |
| En iyi 10, HRP ağırlık, 1x | 2018-01-16 | 1,521 | +5% | 0.48 | -15% | -9% (2021) | +62% | +72% | -5% |
| En iyi 5, ters volatilite ağırlık, 1x | 2020-09-11 | 12,518 | +51% | 1.71 | -24% | -11% (2021) | +311% | +1092% | -13% |
| En iyi 5, HRP ağırlık, 1x | 2020-09-11 | 2,857 | +19% | 1.07 | -23% | -16% (2020) | +208% | +240% | -4% |
| Rastgele 5 strateji (300 deneme), 1x — medyan | – | 3,676 | – | 0.94 (p10–p90: 0.65–1.23) | -34% | – | – | – | – |
|  | En iyi 5'in Sharpe'ı 1.3: rastgele portföylerin %96'inden iyi |  |  |  |  |  |  |  |  |
| Karşılaştırma: BTC al-tut | 2018-01-01 | 5,808 | +22% | 0.63 | -81% | -72% (2018) | +123% | +27% | -55% |

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