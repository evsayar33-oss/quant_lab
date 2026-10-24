# Kasa koruma testi — crypto_alts 1d

Portföy: arenadaki **32 aktif üye**, eşit ağırlık, coin başı en fazla %20. Kabul kuralları sonuçlardan önce yazıldı (`config/arena.yaml` → `protection.accept`). Bir koruma sadece **komşu eşiklerin hepsinde** ve **her zaman diliminde** geçerse açılır.

## Korumasız portföy

Tüm geçmiş: CAGR +32.5%, Sharpe 2.888, maks. düşüş -6.9%, günlük CVaR95 -1.0%. Coin sınırı olmadan: maks. düşüş -9.1%.

Monte Carlo (1 yıl): P(düşüş ≤ −%50) = 0.0%, medyan +32%, kötü %5 +13%.

| Kriz | Getiri | Maks. düşüş |
|---|---|---|
| covid_2020 | +7.5% | -1.2% |
| may_2021 | +5.0% | -2.9% |
| luna_2022 | +13.5% | -1.8% |
| ftx_2022 | +4.2% | -3.2% |
| aug_2024 | -1.3% | -1.5% |
| oct_2025 | +4.2% | -0.8% |

## Kasa düşüş sigortası — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| (0.08, 0.16) | +32.5% | 2.888 | -6.9% | 0/6 | ✗✗✓✓ | kaldı |
|  | MC P(≤−%50): 0.0% (korumasız 0.0%) |  |  |  |  |  |
| (0.1, 0.2) | +32.5% | 2.888 | -6.9% | 0/6 | ✗✗✓✓ | kaldı |
|  | MC P(≤−%50): 0.0% (korumasız 0.0%) |  |  |  |  |  |
| (0.12, 0.25) | +32.5% | 2.888 | -6.9% | 0/6 | ✗✗✓✓ | kaldı |
|  | MC P(≤−%50): 0.0% (korumasız 0.0%) |  |  |  |  |  |

## Volatilite hedefi — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 0.25 | +32.5% | 2.888 | -6.9% | 0/6 | ✗✗✓✓ | kaldı |
| 0.35 | +32.5% | 2.888 | -6.9% | 0/6 | ✗✗✓✓ | kaldı |
| 0.5 | +32.5% | 2.888 | -6.9% | 0/6 | ✗✗✓✓ | kaldı |

## Kasa eğrisi filtresi — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 30 | +25.7% | 2.527 | -5.7% | 2/6 | ✗✓✗✓ | kaldı |
| 60 | +27.7% | 2.606 | -7.5% | 2/6 | ✗✗✓✓ | kaldı |
| 90 | +29.0% | 2.713 | -6.4% | 1/6 | ✗✓✓✓ | kaldı |

## Günlük kayıp limiti — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 0.04 | +32.5% | 2.89 | -6.9% | 0/6 | ✗✗✓✓ | kaldı |
| 0.05 | +32.5% | 2.888 | -6.9% | 0/6 | ✗✗✓✓ | kaldı |
| 0.07 | +32.5% | 2.888 | -6.9% | 0/6 | ✗✗✓✓ | kaldı |

## BTC çöküş bekçisi — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 0.08 | +31.7% | 2.828 | -7.0% | 0/6 | ✗✗✓✓ | kaldı |
| 0.1 | +32.1% | 2.857 | -7.0% | 0/6 | ✗✗✓✓ | kaldı |
| 0.15 | +32.5% | 2.888 | -6.9% | 0/6 | ✗✗✓✓ | kaldı |

## Felaket stopu — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 0.1 | +30.8% | 2.754 | -5.7% | 0/6 | ✗✓✓✓ | kaldı |
| 0.12 | +30.8% | 2.74 | -6.4% | 0/6 | ✗✓✓✓ | kaldı |
| 0.15 | +30.8% | 2.736 | -5.7% | 0/6 | ✗✓✓✓ | kaldı |

## Portföy seçenekleri ($1000 ile başlangıç, maliyet ve funding dahil)

| Portföy | Başlangıç | Bugün ($) | Yıllık | Sharpe | Maks. düşüş | En kötü yıl | Son 3y | Son 5y | En kötü kriz |
|---|---|---|---|---|---|---|---|---|---|
| Hepsi eşit ağırlık (32 strateji), 1x | 2018-09-06 | 10,162 | +33% | 2.91 | -7% | +1% (2018) | +179% | +326% | -3% |
| En iyi 10 (farklı coin), 1x | 2019-02-23 | 27,902 | +54% | 2.14 | -20% | -12% (2019) | +294% | +576% | -9% |
| En iyi 5 (farklı coin), 1x | 2021-08-11 | 18,472 | +75% | 1.98 | -32% | +31% (2024) | +438% | +757% | -19% |
| En iyi 5 (farklı coin), 2x | 2021-08-11 | 215,091 | +182% | 1.98 | -56% | +68% (2024) | +2474% | +4898% | -36% |
| En iyi 5 (farklı coin), 3x | 2021-08-11 | 1,606,498 | +315% | 1.98 | -73% | +111% (2024) | +10954% | +19865% | -51% |
| En iyi 5, 3x + düşüş sigortası (−%10 yarım / −%20 nakit) | 2021-08-11 | 150,779 | +163% | 1.89 | -57% | -27% (2022) | +3279% | +1852% | -32% |
| En iyi 5, 3x + volatilite hedefi %35 | 2021-08-11 | 130,808 | +156% | 2.21 | -36% | +62% (2021) | +1892% | +6669% | -11% |
| En iyi 10, ters volatilite ağırlık, 1x | 2019-02-23 | 22,610 | +50% | 1.72 | -17% | -7% (2019) | +215% | +521% | -10% |
| En iyi 10, HRP ağırlık, 1x | 2019-02-23 | 2,869 | +15% | 1.3 | -9% | -2% (2019) | +126% | +145% | -1% |
| En iyi 5, ters volatilite ağırlık, 1x | 2021-08-11 | 14,360 | +67% | 1.66 | -32% | +19% (2021) | +404% | +953% | -19% |
| En iyi 5, HRP ağırlık, 1x | 2021-08-11 | 3,926 | +30% | 1.52 | -21% | +0% (2022) | +241% | +264% | -1% |
| Rastgele 5 strateji (300 deneme), 1x — medyan | – | 8,489 | – | 1.54 (p10–p90: 1.09–1.92) | -21% | – | – | – | – |
|  | En iyi 5'in Sharpe'ı 1.98: rastgele portföylerin %93'inden iyi |  |  |  |  |  |  |  |  |
| Karşılaştırma: BTC al-tut | 2018-07-26 | 9,934 | +32% | 0.77 | -77% | -64% (2022) | +185% | +32% | -52% |

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