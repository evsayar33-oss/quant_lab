# Kasa koruma testi — crypto_alts 1d

Portföy: arenadaki **65 aktif üye**, eşit ağırlık, coin başı en fazla %20. Kabul kuralları sonuçlardan önce yazıldı (`config/arena.yaml` → `protection.accept`). Bir koruma sadece **komşu eşiklerin hepsinde** ve **her zaman diliminde** geçerse açılır.

## Korumasız portföy

Tüm geçmiş: CAGR +27.5%, Sharpe 2.099, maks. düşüş -12.3%, günlük CVaR95 -1.3%. Coin sınırı olmadan: maks. düşüş -14.8%.

Monte Carlo (1 yıl): P(düşüş ≤ −%50) = 0.0%, medyan +28%, kötü %5 +5%.

| Kriz | Getiri | Maks. düşüş |
|---|---|---|
| covid_2020 | +1.7% | -3.9% |
| may_2021 | -0.1% | -4.9% |
| luna_2022 | +2.7% | -3.0% |
| ftx_2022 | -3.7% | -4.2% |
| aug_2024 | -1.1% | -2.2% |
| oct_2025 | -1.6% | -3.1% |

## Kasa düşüş sigortası — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| (0.08, 0.16) | +26.8% | 2.109 | -10.2% | 0/6 | ✗✓✓✓ | kaldı |
|  | MC P(≤−%50): 0.0% (korumasız 0.0%) |  |  |  |  |  |
| (0.1, 0.2) | +26.7% | 2.068 | -11.3% | 0/6 | ✗✓✓✓ | kaldı |
|  | MC P(≤−%50): 0.0% (korumasız 0.0%) |  |  |  |  |  |
| (0.12, 0.25) | +27.0% | 2.081 | -12.2% | 0/6 | ✗✓✓✓ | kaldı |
|  | MC P(≤−%50): 0.0% (korumasız 0.0%) |  |  |  |  |  |

## Volatilite hedefi — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 0.25 | +27.5% | 2.099 | -12.3% | 0/6 | ✗✗✓✓ | kaldı |
| 0.35 | +27.5% | 2.099 | -12.3% | 0/6 | ✗✗✓✓ | kaldı |
| 0.5 | +27.5% | 2.099 | -12.3% | 0/6 | ✗✗✓✓ | kaldı |

## Kasa eğrisi filtresi — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 30 | +17.8% | 1.625 | -14.5% | 4/6 | ✗✗✗✗ | kaldı |
| 60 | +20.3% | 1.769 | -11.8% | 1/6 | ✗✓✗✗ | kaldı |
| 90 | +22.6% | 1.909 | -15.7% | 1/6 | ✗✗✓✓ | kaldı |

## Günlük kayıp limiti — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 0.04 | +27.5% | 2.099 | -12.3% | 0/6 | ✗✗✓✓ | kaldı |
| 0.05 | +27.5% | 2.099 | -12.3% | 0/6 | ✗✗✓✓ | kaldı |
| 0.07 | +27.5% | 2.099 | -12.3% | 0/6 | ✗✗✓✓ | kaldı |

## BTC çöküş bekçisi — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 0.08 | +27.1% | 2.078 | -11.8% | 1/6 | ✗✓✓✓ | kaldı |
| 0.1 | +27.5% | 2.103 | -11.8% | 0/6 | ✗✓✓✓ | kaldı |
| 0.15 | +27.5% | 2.099 | -12.3% | 0/6 | ✗✗✓✓ | kaldı |

## Felaket stopu — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 0.1 | +24.9% | 1.997 | -12.6% | 4/6 | ✗✗✓✓ | kaldı |
| 0.12 | +25.6% | 2.019 | -12.2% | 4/6 | ✗✓✓✓ | kaldı |
| 0.15 | +25.6% | 2.005 | -12.3% | 3/6 | ✗✗✓✓ | kaldı |

## Portföy seçenekleri ($1000 ile başlangıç, maliyet ve funding dahil)

| Portföy | Başlangıç | Bugün ($) | Yıllık | Sharpe | Maks. düşüş | En kötü yıl | Son 3y | Son 5y | En kötü kriz |
|---|---|---|---|---|---|---|---|---|---|
| Hepsi eşit ağırlık (65 strateji), 1x | 2018-01-29 | 8,564 | +28% | 2.11 | -12% | -2% (2018) | +112% | +156% | -5% |
| En iyi 10 (farklı coin), 1x | 2018-06-28 | 23,912 | +46% | 2.13 | -23% | -10% (2018) | +292% | +413% | -6% |
| En iyi 5 (farklı coin), 1x | 2018-07-18 | 24,584 | +47% | 1.82 | -21% | -8% (2022) | +306% | +331% | -6% |
| En iyi 5 (farklı coin), 2x | 2018-07-18 | 398,496 | +106% | 1.82 | -38% | -17% (2022) | +1341% | +1471% | -11% |
| En iyi 5 (farklı coin), 3x | 2018-07-18 | 4,274,691 | +174% | 1.82 | -53% | -25% (2022) | +4394% | +4765% | -17% |
| En iyi 5, 3x + düşüş sigortası (−%10 yarım / −%20 nakit) | 2018-07-18 | 38,054 | +55% | 1.12 | -49% | -5% (2018) | +678% | +586% | -17% |
| En iyi 5, 3x + volatilite hedefi %35 | 2018-07-18 | 82,454 | +70% | 1.63 | -39% | -22% (2018) | +773% | +914% | -8% |
| En iyi 10, ters volatilite ağırlık, 1x | 2018-06-28 | 33,756 | +52% | 2.03 | -28% | -17% (2018) | +414% | +664% | -6% |
| En iyi 10, HRP ağırlık, 1x | 2018-06-28 | 1,307 | +3% | 0.3 | -30% | -9% (2022) | +14% | -8% | -8% |
| En iyi 5, ters volatilite ağırlık, 1x | 2018-07-18 | 29,343 | +50% | 1.72 | -30% | -11% (2018) | +466% | +507% | -3% |
| En iyi 5, HRP ağırlık, 1x | 2018-07-18 | 2,096 | +9% | 0.74 | -21% | -7% (2019) | +73% | +72% | -0% |
| Rastgele 5 strateji (300 deneme), 1x — medyan | – | 7,591 | – | 1.18 (p10–p90: 0.79–1.48) | -31% | – | – | – | – |
|  | En iyi 5'in Sharpe'ı 1.82: rastgele portföylerin %100'inden iyi |  |  |  |  |  |  |  |  |
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