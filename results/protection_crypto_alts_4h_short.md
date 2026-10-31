# Kasa koruma testi — crypto_alts 4h

Portföy: arenadaki **97 aktif üye**, eşit ağırlık, coin başı en fazla %20. Kabul kuralları sonuçlardan önce yazıldı (`config/arena.yaml` → `protection.accept`). Bir koruma sadece **komşu eşiklerin hepsinde** ve **her zaman diliminde** geçerse açılır.

## Korumasız portföy

Tüm geçmiş: CAGR +21.5%, Sharpe 1.894, maks. düşüş -8.1%, günlük CVaR95 -0.9%. Coin sınırı olmadan: maks. düşüş -8.9%.

Monte Carlo (1 yıl): P(düşüş ≤ −%50) = 0.0%, medyan +21%, kötü %5 +2%.

| Kriz | Getiri | Maks. düşüş |
|---|---|---|
| covid_2020 | +2.6% | -0.5% |
| may_2021 | +15.4% | -4.6% |
| luna_2022 | +12.9% | -2.7% |
| ftx_2022 | +5.1% | -4.8% |
| aug_2024 | +7.4% | -3.0% |
| oct_2025 | +3.3% | -0.8% |

## Kasa düşüş sigortası — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| (0.08, 0.16) | +21.2% | 1.876 | -8.0% | 0/6 | ✗✓✓✓ | kaldı |
|  | MC P(≤−%50): 0.0% (korumasız 0.0%) |  |  |  |  |  |
| (0.1, 0.2) | +21.5% | 1.894 | -8.1% | 0/6 | ✗✗✓✓ | kaldı |
|  | MC P(≤−%50): 0.0% (korumasız 0.0%) |  |  |  |  |  |
| (0.12, 0.25) | +21.5% | 1.894 | -8.1% | 0/6 | ✗✗✓✓ | kaldı |
|  | MC P(≤−%50): 0.0% (korumasız 0.0%) |  |  |  |  |  |

## Volatilite hedefi — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 0.25 | +21.5% | 1.899 | -8.1% | 0/6 | ✗✗✓✓ | kaldı |
| 0.35 | +21.5% | 1.894 | -8.1% | 0/6 | ✗✗✓✓ | kaldı |
| 0.5 | +21.5% | 1.894 | -8.1% | 0/6 | ✗✗✓✓ | kaldı |

## Kasa eğrisi filtresi — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 30 | +14.5% | 1.435 | -7.5% | 2/6 | ✗✓✗✗ | kaldı |
| 60 | +14.4% | 1.408 | -8.2% | 2/6 | ✗✗✗✗ | kaldı |
| 90 | +16.9% | 1.582 | -8.3% | 1/6 | ✗✗✗✓ | kaldı |

## Günlük kayıp limiti — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 0.04 | +21.5% | 1.894 | -8.1% | 0/6 | ✗✗✓✓ | kaldı |
| 0.05 | +21.5% | 1.894 | -8.1% | 0/6 | ✗✗✓✓ | kaldı |
| 0.07 | +21.5% | 1.894 | -8.1% | 0/6 | ✗✗✓✓ | kaldı |

## BTC çöküş bekçisi — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 0.08 | +21.5% | 1.894 | -8.1% | 0/6 | ✗✗✓✓ | kaldı |
| 0.1 | +21.5% | 1.894 | -8.1% | 0/6 | ✗✗✓✓ | kaldı |
| 0.15 | +21.5% | 1.894 | -8.1% | 0/6 | ✗✗✓✓ | kaldı |

## Felaket stopu — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 0.1 | +21.4% | 1.891 | -8.1% | 0/6 | ✗✗✓✓ | kaldı |
| 0.12 | +21.5% | 1.891 | -8.1% | 0/6 | ✗✗✓✓ | kaldı |
| 0.15 | +21.5% | 1.893 | -8.1% | 0/6 | ✗✗✓✓ | kaldı |

## Portföy seçenekleri ($1000 ile başlangıç, maliyet ve funding dahil)

| Portföy | Başlangıç | Bugün ($) | Yıllık | Sharpe | Maks. düşüş | En kötü yıl | Son 3y | Son 5y | En kötü kriz |
|---|---|---|---|---|---|---|---|---|---|
| Hepsi eşit ağırlık (97 strateji), 1x | 2018-08-08 | 5,517 | +23% | 1.96 | -8% | +5% (2020) | +118% | +262% | -5% |
| En iyi 10 (farklı coin), 1x | 2021-06-08 | 10,671 | +55% | 2.37 | -10% | +8% (2023) | +192% | +572% | -9% |
| En iyi 5 (farklı coin), 1x | 2021-08-12 | 9,314 | +54% | 2.07 | -14% | +8% (2023) | +244% | +853% | -9% |
| En iyi 5 (farklı coin), 2x | 2021-08-12 | 68,045 | +126% | 2.07 | -27% | +14% (2023) | +948% | +7158% | -18% |
| En iyi 5 (farklı coin), 3x | 2021-08-12 | 392,229 | +216% | 2.07 | -38% | +18% (2021) | +2742% | +44382% | -25% |
| En iyi 5, 3x + düşüş sigortası (−%10 yarım / −%20 nakit) | 2021-08-12 | 13,584 | +65% | 1.32 | -37% | -28% (2021) | +642% | +1689% | -19% |
| En iyi 5, 3x + volatilite hedefi %35 | 2021-08-12 | 47,330 | +110% | 2.12 | -28% | +14% (2023) | +692% | +5529% | -15% |
| En iyi 10, ters volatilite ağırlık, 1x | 2021-06-08 | 11,259 | +57% | 2.37 | -11% | +13% (2023) | +175% | +662% | -11% |
| En iyi 10, HRP ağırlık, 1x | 2021-06-08 | 2,089 | +15% | 1.06 | -15% | -3% (2023) | +88% | +109% | -1% |
| En iyi 5, ters volatilite ağırlık, 1x | 2021-08-12 | 14,387 | +67% | 2.29 | -14% | +11% (2023) | +279% | +1234% | -11% |
| En iyi 5, HRP ağırlık, 1x | 2021-08-12 | 2,968 | +23% | 1.28 | -18% | -8% (2021) | +180% | +206% | -4% |
| Rastgele 5 strateji (300 deneme), 1x — medyan | – | 4,352 | – | 1.3 (p10–p90: 1.05–1.55) | -18% | – | – | – | – |
|  | En iyi 5'in Sharpe'ı 2.07: rastgele portföylerin %100'inden iyi |  |  |  |  |  |  |  |  |
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