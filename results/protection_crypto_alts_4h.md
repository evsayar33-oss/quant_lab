# Kasa koruma testi — crypto_alts 4h

Portföy: arenadaki **71 aktif üye**, eşit ağırlık, coin başı en fazla %20. Kabul kuralları sonuçlardan önce yazıldı (`config/arena.yaml` → `protection.accept`). Bir koruma sadece **komşu eşiklerin hepsinde** ve **her zaman diliminde** geçerse açılır.

## Korumasız portföy

Tüm geçmiş: CAGR +32.1%, Sharpe 2.23, maks. düşüş -10.4%, günlük CVaR95 -1.1%. Coin sınırı olmadan: maks. düşüş -22.9%.

Monte Carlo (1 yıl): P(düşüş ≤ −%50) = 0.0%, medyan +31%, kötü %5 +8%.

| Kriz | Getiri | Maks. düşüş |
|---|---|---|
| covid_2020 | +4.4% | -5.8% |
| may_2021 | -0.4% | -4.8% |
| luna_2022 | +6.3% | -2.6% |
| ftx_2022 | +2.1% | -3.6% |
| aug_2024 | +5.3% | -2.2% |
| oct_2025 | +3.4% | -1.4% |

## Kasa düşüş sigortası — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| (0.08, 0.16) | +31.8% | 2.228 | -9.2% | 0/6 | ✗✓✓✓ | kaldı |
|  | MC P(≤−%50): 0.0% (korumasız 0.0%) |  |  |  |  |  |
| (0.1, 0.2) | +31.6% | 2.215 | -10.3% | 0/6 | ✗✓✓✓ | kaldı |
|  | MC P(≤−%50): 0.0% (korumasız 0.0%) |  |  |  |  |  |
| (0.12, 0.25) | +32.1% | 2.23 | -10.4% | 0/6 | ✗✗✓✓ | kaldı |
|  | MC P(≤−%50): 0.0% (korumasız 0.0%) |  |  |  |  |  |

## Volatilite hedefi — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 0.25 | +32.3% | 2.252 | -8.6% | 1/6 | ✗✓✓✓ | kaldı |
| 0.35 | +32.1% | 2.23 | -10.4% | 0/6 | ✗✗✓✓ | kaldı |
| 0.5 | +32.1% | 2.23 | -10.4% | 0/6 | ✗✗✓✓ | kaldı |

## Kasa eğrisi filtresi — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 30 | +21.2% | 1.649 | -10.7% | 0/6 | ✗✗✗✗ | kaldı |
| 60 | +24.5% | 1.846 | -11.1% | 1/6 | ✗✗✗✓ | kaldı |
| 90 | +26.4% | 2.016 | -9.7% | 0/6 | ✗✓✓✓ | kaldı |

## Günlük kayıp limiti — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 0.04 | +32.1% | 2.23 | -10.4% | 0/6 | ✗✗✓✓ | kaldı |
| 0.05 | +32.1% | 2.23 | -10.4% | 0/6 | ✗✗✓✓ | kaldı |
| 0.07 | +32.1% | 2.23 | -10.4% | 0/6 | ✗✗✓✓ | kaldı |

## BTC çöküş bekçisi — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 0.08 | +31.2% | 2.181 | -10.4% | 1/6 | ✗✗✓✓ | kaldı |
| 0.1 | +31.4% | 2.194 | -10.4% | 0/6 | ✗✗✓✓ | kaldı |
| 0.15 | +32.0% | 2.227 | -10.4% | 0/6 | ✗✗✓✓ | kaldı |

## Felaket stopu — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 0.1 | +31.9% | 2.23 | -10.2% | 2/6 | ✗✓✓✓ | kaldı |
| 0.12 | +31.9% | 2.221 | -10.3% | 2/6 | ✗✓✓✓ | kaldı |
| 0.15 | +32.0% | 2.224 | -10.4% | 1/6 | ✗✗✓✓ | kaldı |

## Portföy seçenekleri ($1000 ile başlangıç, maliyet ve funding dahil)

| Portföy | Başlangıç | Bugün ($) | Yıllık | Sharpe | Maks. düşüş | En kötü yıl | Son 3y | Son 5y | En kötü kriz |
|---|---|---|---|---|---|---|---|---|---|
| Hepsi eşit ağırlık (71 strateji), 1x | 2018-01-08 | 11,699 | +32% | 2.23 | -10% | +16% (2019) | +179% | +294% | -6% |
| En iyi 10 (farklı coin), 1x | 2018-01-16 | 51,497 | +57% | 1.73 | -38% | +9% (2019) | +439% | +848% | -13% |
| En iyi 5 (farklı coin), 1x | 2018-07-16 | 82,138 | +70% | 1.69 | -44% | -5% (2018) | +598% | +1131% | -6% |
| En iyi 5 (farklı coin), 2x | 2018-07-16 | 2,518,222 | +157% | 1.69 | -71% | -16% (2018) | +3980% | +11358% | -13% |
| En iyi 5 (farklı coin), 3x | 2018-07-16 | 29,158,907 | +245% | 1.69 | -86% | -30% (2018) | +19925% | +80788% | -18% |
| En iyi 5, 3x + düşüş sigortası (−%10 yarım / −%20 nakit) | 2018-07-16 | 38,313 | +55% | 1.08 | -67% | +0% (2019) | +2251% | +2811% | -17% |
| En iyi 5, 3x + volatilite hedefi %35 | 2018-07-16 | 438,285 | +108% | 1.85 | -56% | -4% (2018) | +2626% | +8998% | -9% |
| En iyi 10, ters volatilite ağırlık, 1x | 2018-01-16 | 43,392 | +54% | 1.73 | -36% | -1% (2019) | +349% | +662% | -10% |
| En iyi 10, HRP ağırlık, 1x | 2018-01-16 | 9,430 | +29% | 1.15 | -26% | +0% (2021) | +532% | +667% | -1% |
| En iyi 5, ters volatilite ağırlık, 1x | 2018-07-16 | 57,265 | +63% | 1.53 | -38% | -16% (2018) | +455% | +749% | -8% |
| En iyi 5, HRP ağırlık, 1x | 2018-07-16 | 8,547 | +30% | 1.16 | -24% | -10% (2020) | +608% | +779% | -4% |
| Rastgele 5 strateji (300 deneme), 1x — medyan | – | 8,256 | – | 1.24 (p10–p90: 0.84–1.59) | -31% | – | – | – | – |
|  | En iyi 5'in Sharpe'ı 1.69: rastgele portföylerin %95'inden iyi |  |  |  |  |  |  |  |  |
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