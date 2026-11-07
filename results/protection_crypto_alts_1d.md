# Kasa koruma testi — crypto_alts 1d

Portföy: arenadaki **41 aktif üye**, eşit ağırlık, coin başı en fazla %20. Kabul kuralları sonuçlardan önce yazıldı (`config/arena.yaml` → `protection.accept`). Bir koruma sadece **komşu eşiklerin hepsinde** ve **her zaman diliminde** geçerse açılır.

## Korumasız portföy

Tüm geçmiş: CAGR +24.6%, Sharpe 2.312, maks. düşüş -12.7%, günlük CVaR95 -1.0%. Coin sınırı olmadan: maks. düşüş -13.1%.

Monte Carlo (1 yıl): P(düşüş ≤ −%50) = 0.0%, medyan +24%, kötü %5 +6%.

| Kriz | Getiri | Maks. düşüş |
|---|---|---|
| covid_2020 | +3.6% | -2.6% |
| may_2021 | -3.6% | -5.5% |
| luna_2022 | +11.4% | -1.6% |
| ftx_2022 | +2.3% | -3.3% |
| aug_2024 | -1.2% | -1.2% |
| oct_2025 | +3.2% | -0.6% |

## Kasa düşüş sigortası — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| (0.08, 0.16) | +24.3% | 2.329 | -10.4% | 0/6 | ✗✓✓✓ | kaldı |
|  | MC P(≤−%50): 0.0% (korumasız 0.0%) |  |  |  |  |  |
| (0.1, 0.2) | +24.2% | 2.307 | -11.4% | 0/6 | ✗✓✓✓ | kaldı |
|  | MC P(≤−%50): 0.0% (korumasız 0.0%) |  |  |  |  |  |
| (0.12, 0.25) | +24.1% | 2.294 | -12.7% | 0/6 | ✗✓✓✓ | kaldı |
|  | MC P(≤−%50): 0.0% (korumasız 0.0%) |  |  |  |  |  |

## Volatilite hedefi — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 0.25 | +24.6% | 2.312 | -12.7% | 0/6 | ✗✗✓✓ | kaldı |
| 0.35 | +24.6% | 2.312 | -12.7% | 0/6 | ✗✗✓✓ | kaldı |
| 0.5 | +24.6% | 2.312 | -12.7% | 0/6 | ✗✗✓✓ | kaldı |

## Kasa eğrisi filtresi — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 30 | +17.3% | 1.947 | -13.0% | 2/6 | ✗✗✗✗ | kaldı |
| 60 | +20.9% | 2.144 | -7.2% | 2/6 | ✗✓✓✓ | kaldı |
| 90 | +20.5% | 2.122 | -7.1% | 2/6 | ✗✓✓✓ | kaldı |

## Günlük kayıp limiti — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 0.04 | +24.6% | 2.312 | -12.7% | 0/6 | ✗✗✓✓ | kaldı |
| 0.05 | +24.6% | 2.312 | -12.7% | 0/6 | ✗✗✓✓ | kaldı |
| 0.07 | +24.6% | 2.312 | -12.7% | 0/6 | ✗✗✓✓ | kaldı |

## BTC çöküş bekçisi — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 0.08 | +24.0% | 2.257 | -12.9% | 0/6 | ✗✗✓✓ | kaldı |
| 0.1 | +24.4% | 2.29 | -12.7% | 0/6 | ✗✗✓✓ | kaldı |
| 0.15 | +24.6% | 2.312 | -12.7% | 0/6 | ✗✗✓✓ | kaldı |

## Felaket stopu — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 0.1 | +23.0% | 2.18 | -11.9% | 1/6 | ✗✓✓✓ | kaldı |
| 0.12 | +23.4% | 2.208 | -12.3% | 1/6 | ✗✓✓✓ | kaldı |
| 0.15 | +23.6% | 2.234 | -12.3% | 1/6 | ✗✓✓✓ | kaldı |

## Portföy seçenekleri ($1000 ile başlangıç, maliyet ve funding dahil)

| Portföy | Başlangıç | Bugün ($) | Yıllık | Sharpe | Maks. düşüş | En kötü yıl | Son 3y | Son 5y | En kötü kriz |
|---|---|---|---|---|---|---|---|---|---|
| Hepsi eşit ağırlık (41 strateji), 1x | 2018-03-15 | 6,995 | +25% | 2.34 | -13% | +5% (2018) | +140% | +233% | -5% |
| En iyi 10 (farklı coin), 1x | 2018-06-28 | 14,260 | +38% | 1.92 | -21% | -6% (2018) | +236% | +452% | -12% |
| En iyi 5 (farklı coin), 1x | 2021-01-05 | 20,155 | +68% | 1.61 | -45% | +26% (2024) | +308% | +974% | -41% |
| En iyi 5 (farklı coin), 2x | 2021-01-05 | 182,493 | +145% | 1.61 | -77% | +56% (2024) | +1394% | +8477% | -73% |
| En iyi 5 (farklı coin), 3x | 2021-01-05 | 590,265 | +199% | 1.61 | -95% | -6% (2021) | +4844% | +51539% | -93% |
| En iyi 5, 3x + düşüş sigortası (−%10 yarım / −%20 nakit) | 2021-01-05 | 7,057 | +40% | 0.88 | -81% | -70% (2021) | +1865% | +2260% | -62% |
| En iyi 5, 3x + volatilite hedefi %35 | 2021-01-05 | 128,343 | +130% | 2.12 | -29% | +53% (2024) | +1238% | +5335% | -18% |
| En iyi 10, ters volatilite ağırlık, 1x | 2018-06-28 | 14,065 | +37% | 1.5 | -31% | -4% (2019) | +162% | +308% | -12% |
| En iyi 10, HRP ağırlık, 1x | 2018-06-28 | 3,539 | +16% | 0.93 | -19% | -1% (2018) | +193% | +216% | -10% |
| En iyi 5, ters volatilite ağırlık, 1x | 2021-01-05 | 28,338 | +78% | 1.72 | -43% | +24% (2024) | +304% | +1077% | -38% |
| En iyi 5, HRP ağırlık, 1x | 2021-01-05 | 3,853 | +26% | 1.36 | -16% | +1% (2024) | +196% | +240% | -1% |
| Rastgele 5 strateji (300 deneme), 1x — medyan | – | 6,002 | – | 1.19 (p10–p90: 0.73–1.62) | -28% | – | – | – | – |
|  | En iyi 5'in Sharpe'ı 1.61: rastgele portföylerin %89'inden iyi |  |  |  |  |  |  |  |  |
| Karşılaştırma: BTC al-tut | 2018-01-02 | 5,855 | +22% | 0.64 | -81% | -72% (2018) | +121% | +28% | -52% |

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