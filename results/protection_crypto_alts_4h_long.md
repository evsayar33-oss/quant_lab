# Kasa koruma testi — crypto_alts 4h

Portföy: arenadaki **100 aktif üye**, eşit ağırlık, coin başı en fazla %20. Kabul kuralları sonuçlardan önce yazıldı (`config/arena.yaml` → `protection.accept`). Bir koruma sadece **komşu eşiklerin hepsinde** ve **her zaman diliminde** geçerse açılır.

## Korumasız portföy

Tüm geçmiş: CAGR +27.8%, Sharpe 2.223, maks. düşüş -8.0%, günlük CVaR95 -1.0%. Coin sınırı olmadan: maks. düşüş -8.2%.

Monte Carlo (1 yıl): P(düşüş ≤ −%50) = 0.0%, medyan +27%, kötü %5 +5%.

| Kriz | Getiri | Maks. düşüş |
|---|---|---|
| covid_2020 | -1.3% | -2.5% |
| may_2021 | -5.6% | -6.9% |
| luna_2022 | -1.7% | -3.4% |
| ftx_2022 | -2.3% | -3.2% |
| aug_2024 | +0.1% | -2.1% |
| oct_2025 | -0.0% | -1.1% |

## Kasa düşüş sigortası — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| (0.08, 0.16) | +27.8% | 2.223 | -8.0% | 0/6 | ✗✗✓✓ | kaldı |
|  | MC P(≤−%50): 0.0% (korumasız 0.0%) |  |  |  |  |  |
| (0.1, 0.2) | +27.8% | 2.223 | -8.0% | 0/6 | ✗✗✓✓ | kaldı |
|  | MC P(≤−%50): 0.0% (korumasız 0.0%) |  |  |  |  |  |
| (0.12, 0.25) | +27.8% | 2.223 | -8.0% | 0/6 | ✗✗✓✓ | kaldı |
|  | MC P(≤−%50): 0.0% (korumasız 0.0%) |  |  |  |  |  |

## Volatilite hedefi — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 0.25 | +27.7% | 2.227 | -8.0% | 0/6 | ✗✗✓✓ | kaldı |
| 0.35 | +27.8% | 2.223 | -8.0% | 0/6 | ✗✗✓✓ | kaldı |
| 0.5 | +27.8% | 2.223 | -8.0% | 0/6 | ✗✗✓✓ | kaldı |

## Kasa eğrisi filtresi — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 30 | +21.2% | 1.834 | -9.0% | 5/6 | ✓✗✗✓ | kaldı |
| 60 | +22.3% | 1.899 | -11.5% | 5/6 | ✓✗✗✓ | kaldı |
| 90 | +22.5% | 1.923 | -15.6% | 4/6 | ✗✗✗✓ | kaldı |

## Günlük kayıp limiti — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 0.04 | +27.8% | 2.223 | -8.0% | 0/6 | ✗✗✓✓ | kaldı |
| 0.05 | +27.8% | 2.223 | -8.0% | 0/6 | ✗✗✓✓ | kaldı |
| 0.07 | +27.8% | 2.223 | -8.0% | 0/6 | ✗✗✓✓ | kaldı |

## BTC çöküş bekçisi — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 0.08 | +25.0% | 2.058 | -8.5% | 2/6 | ✗✗✓✓ | kaldı |
| 0.1 | +25.6% | 2.093 | -8.7% | 2/6 | ✗✗✓✓ | kaldı |
| 0.15 | +27.2% | 2.185 | -8.7% | 1/6 | ✗✗✓✓ | kaldı |

## Felaket stopu — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 0.1 | +27.1% | 2.185 | -7.6% | 1/6 | ✗✓✓✓ | kaldı |
| 0.12 | +27.1% | 2.18 | -7.8% | 0/6 | ✗✓✓✓ | kaldı |
| 0.15 | +27.4% | 2.203 | -7.8% | 0/6 | ✗✓✓✓ | kaldı |

## Portföy seçenekleri ($1000 ile başlangıç, maliyet ve funding dahil)

| Portföy | Başlangıç | Bugün ($) | Yıllık | Sharpe | Maks. düşüş | En kötü yıl | Son 3y | Son 5y | En kötü kriz |
|---|---|---|---|---|---|---|---|---|---|
| Hepsi eşit ağırlık (100 strateji), 1x | 2018-01-04 | 8,728 | +28% | 2.22 | -8% | +1% (2022) | +121% | +188% | -7% |
| En iyi 10 (farklı coin), 1x | 2018-01-27 | 20,310 | +41% | 2.11 | -15% | -2% (2022) | +198% | +315% | -9% |
| En iyi 5 (farklı coin), 1x | 2018-07-02 | 19,547 | +43% | 1.31 | -50% | -25% (2019) | +279% | +522% | -10% |
| En iyi 5 (farklı coin), 2x | 2018-07-02 | 173,859 | +86% | 1.31 | -80% | -52% (2019) | +1185% | +3089% | -19% |
| En iyi 5 (farklı coin), 3x | 2018-07-02 | 695,264 | +119% | 1.31 | -94% | -74% (2019) | +3806% | +13406% | -28% |
| En iyi 5, 3x + düşüş sigortası (−%10 yarım / −%20 nakit) | 2018-07-02 | 29,723 | +50% | 1.19 | -43% | +0% (2019) | +944% | +1676% | -4% |
| En iyi 5, 3x + volatilite hedefi %35 | 2018-07-02 | 33,910 | +53% | 1.22 | -51% | -37% (2019) | +799% | +2169% | -26% |
| En iyi 10, ters volatilite ağırlık, 1x | 2018-01-27 | 26,053 | +45% | 2.27 | -21% | -1% (2018) | +217% | +347% | -7% |
| En iyi 10, HRP ağırlık, 1x | 2018-01-27 | 5,504 | +21% | 1.65 | -11% | -2% (2020) | +257% | +446% | -7% |
| En iyi 5, ters volatilite ağırlık, 1x | 2018-07-02 | 29,121 | +50% | 1.5 | -41% | -25% (2019) | +320% | +552% | -10% |
| En iyi 5, HRP ağırlık, 1x | 2018-07-02 | 7,912 | +28% | 1.51 | -16% | -5% (2022) | +450% | +688% | -4% |
| Rastgele 5 strateji (300 deneme), 1x — medyan | – | 6,388 | – | 1.28 (p10–p90: 0.98–1.57) | -23% | – | – | – | – |
|  | En iyi 5'in Sharpe'ı 1.31: rastgele portföylerin %55'inden iyi |  |  |  |  |  |  |  |  |
| Karşılaştırma: BTC al-tut | 2018-01-01 | 5,808 | +22% | 0.63 | -81% | -72% (2018) | +125% | +28% | -55% |

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