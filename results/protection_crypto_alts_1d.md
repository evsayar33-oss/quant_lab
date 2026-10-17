# Kasa koruma testi — crypto_alts 1d

Portföy: arenadaki **24 aktif üye**, eşit ağırlık, coin başı en fazla %20. Kabul kuralları sonuçlardan önce yazıldı (`config/arena.yaml` → `protection.accept`). Bir koruma sadece **komşu eşiklerin hepsinde** ve **her zaman diliminde** geçerse açılır.

## Korumasız portföy

Tüm geçmiş: CAGR +35.2%, Sharpe 2.759, maks. düşüş -6.9%, günlük CVaR95 -1.1%. Coin sınırı olmadan: maks. düşüş -10.5%.

Monte Carlo (1 yıl): P(düşüş ≤ −%50) = 0.0%, medyan +34%, kötü %5 +12%.

| Kriz | Getiri | Maks. düşüş |
|---|---|---|
| covid_2020 | +9.1% | -0.9% |
| may_2021 | +4.8% | -3.5% |
| luna_2022 | +17.7% | -2.1% |
| ftx_2022 | +4.0% | -2.8% |
| aug_2024 | -0.9% | -1.3% |
| oct_2025 | +3.6% | -1.7% |

## Kasa düşüş sigortası — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| (0.08, 0.16) | +35.2% | 2.759 | -6.9% | 0/6 | ✗✗✓✓ | kaldı |
|  | MC P(≤−%50): 0.0% (korumasız 0.0%) |  |  |  |  |  |
| (0.1, 0.2) | +35.2% | 2.759 | -6.9% | 0/6 | ✗✗✓✓ | kaldı |
|  | MC P(≤−%50): 0.0% (korumasız 0.0%) |  |  |  |  |  |
| (0.12, 0.25) | +35.2% | 2.759 | -6.9% | 0/6 | ✗✗✓✓ | kaldı |
|  | MC P(≤−%50): 0.0% (korumasız 0.0%) |  |  |  |  |  |

## Volatilite hedefi — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 0.25 | +35.2% | 2.76 | -6.9% | 0/6 | ✗✗✓✓ | kaldı |
| 0.35 | +35.2% | 2.759 | -6.9% | 0/6 | ✗✗✓✓ | kaldı |
| 0.5 | +35.2% | 2.759 | -6.9% | 0/6 | ✗✗✓✓ | kaldı |

## Kasa eğrisi filtresi — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 30 | +27.2% | 2.369 | -6.0% | 2/6 | ✗✓✗✓ | kaldı |
| 60 | +28.6% | 2.435 | -8.5% | 0/6 | ✗✗✗✓ | kaldı |
| 90 | +29.5% | 2.476 | -8.3% | 0/6 | ✗✗✗✓ | kaldı |

## Günlük kayıp limiti — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 0.04 | +35.2% | 2.759 | -6.9% | 0/6 | ✗✗✓✓ | kaldı |
| 0.05 | +35.2% | 2.759 | -6.9% | 0/6 | ✗✗✓✓ | kaldı |
| 0.07 | +35.2% | 2.759 | -6.9% | 0/6 | ✗✗✓✓ | kaldı |

## BTC çöküş bekçisi — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 0.08 | +34.2% | 2.693 | -6.9% | 0/6 | ✗✗✓✓ | kaldı |
| 0.1 | +34.7% | 2.721 | -6.9% | 0/6 | ✗✗✓✓ | kaldı |
| 0.15 | +35.2% | 2.759 | -6.9% | 0/6 | ✗✗✓✓ | kaldı |

## Felaket stopu — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 0.1 | +32.8% | 2.598 | -7.3% | 0/6 | ✗✗✓✓ | kaldı |
| 0.12 | +32.6% | 2.572 | -7.4% | 0/6 | ✗✗✓✓ | kaldı |
| 0.15 | +32.6% | 2.568 | -8.3% | 0/6 | ✗✗✓✓ | kaldı |

## Portföy seçenekleri ($1000 ile başlangıç, maliyet ve funding dahil)

| Portföy | Başlangıç | Bugün ($) | Yıllık | Sharpe | Maks. düşüş | En kötü yıl | Son 3y | Son 5y | En kötü kriz |
|---|---|---|---|---|---|---|---|---|---|
| Hepsi eşit ağırlık (24 strateji), 1x | 2019-02-09 | 11,955 | +38% | 2.86 | -7% | +6% (2019) | +185% | +334% | -3% |
| En iyi 10 (farklı coin), 1x | 2019-02-23 | 26,521 | +54% | 2.14 | -20% | -12% (2019) | +256% | +475% | -10% |
| En iyi 5 (farklı coin), 1x | 2021-08-11 | 16,779 | +72% | 1.93 | -32% | +24% (2023) | +403% | +679% | -19% |
| En iyi 5 (farklı coin), 2x | 2021-08-11 | 177,631 | +172% | 1.93 | -56% | +50% (2023) | +2148% | +4027% | -36% |
| En iyi 5 (farklı coin), 3x | 2021-08-11 | 1,203,155 | +293% | 1.93 | -73% | +77% (2023) | +8873% | +14853% | -51% |
| En iyi 5, 3x + düşüş sigortası (−%10 yarım / −%20 nakit) | 2021-08-11 | 81,927 | +134% | 1.73 | -63% | -27% (2022) | +1736% | +961% | -32% |
| En iyi 5, 3x + volatilite hedefi %35 | 2021-08-11 | 126,651 | +155% | 2.18 | -36% | +62% (2021) | +1939% | +6454% | -11% |
| Karşılaştırma: BTC al-tut | 2018-07-26 | 9,894 | +32% | 0.77 | -77% | -64% (2022) | +186% | +32% | -52% |

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