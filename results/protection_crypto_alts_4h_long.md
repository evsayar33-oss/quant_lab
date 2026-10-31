# Kasa koruma testi — crypto_alts 4h

Portföy: arenadaki **100 aktif üye**, eşit ağırlık, coin başı en fazla %20. Kabul kuralları sonuçlardan önce yazıldı (`config/arena.yaml` → `protection.accept`). Bir koruma sadece **komşu eşiklerin hepsinde** ve **her zaman diliminde** geçerse açılır.

## Korumasız portföy

Tüm geçmiş: CAGR +27.8%, Sharpe 2.643, maks. düşüş -6.5%, günlük CVaR95 -0.9%. Coin sınırı olmadan: maks. düşüş -17.8%.

Monte Carlo (1 yıl): P(düşüş ≤ −%50) = 0.0%, medyan +26%, kötü %5 +7%.

| Kriz | Getiri | Maks. düşüş |
|---|---|---|
| covid_2020 | -0.4% | -0.9% |
| may_2021 | -0.5% | -3.8% |
| luna_2022 | -0.1% | -2.6% |
| ftx_2022 | -2.3% | -3.3% |
| aug_2024 | +0.1% | -2.1% |
| oct_2025 | -0.0% | -1.1% |

## Kasa düşüş sigortası — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| (0.08, 0.16) | +27.8% | 2.643 | -6.5% | 0/6 | ✗✗✓✓ | kaldı |
|  | MC P(≤−%50): 0.0% (korumasız 0.0%) |  |  |  |  |  |
| (0.1, 0.2) | +27.8% | 2.643 | -6.5% | 0/6 | ✗✗✓✓ | kaldı |
|  | MC P(≤−%50): 0.0% (korumasız 0.0%) |  |  |  |  |  |
| (0.12, 0.25) | +27.8% | 2.643 | -6.5% | 0/6 | ✗✗✓✓ | kaldı |
|  | MC P(≤−%50): 0.0% (korumasız 0.0%) |  |  |  |  |  |

## Volatilite hedefi — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 0.25 | +27.8% | 2.643 | -6.5% | 0/6 | ✗✗✓✓ | kaldı |
| 0.35 | +27.8% | 2.643 | -6.5% | 0/6 | ✗✗✓✓ | kaldı |
| 0.5 | +27.8% | 2.643 | -6.5% | 0/6 | ✗✗✓✓ | kaldı |

## Kasa eğrisi filtresi — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 30 | +22.3% | 2.271 | -7.2% | 4/6 | ✗✗✗✓ | kaldı |
| 60 | +23.2% | 2.35 | -8.2% | 3/6 | ✗✗✗✓ | kaldı |
| 90 | +24.6% | 2.467 | -7.8% | 3/6 | ✗✗✓✓ | kaldı |

## Günlük kayıp limiti — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 0.04 | +27.8% | 2.643 | -6.5% | 0/6 | ✗✗✓✓ | kaldı |
| 0.05 | +27.8% | 2.643 | -6.5% | 0/6 | ✗✗✓✓ | kaldı |
| 0.07 | +27.8% | 2.643 | -6.5% | 0/6 | ✗✗✓✓ | kaldı |

## BTC çöküş bekçisi — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 0.08 | +26.2% | 2.536 | -6.9% | 4/6 | ✗✗✓✓ | kaldı |
| 0.1 | +26.6% | 2.559 | -6.9% | 3/6 | ✗✗✓✓ | kaldı |
| 0.15 | +27.4% | 2.611 | -6.9% | 1/6 | ✗✗✓✓ | kaldı |

## Felaket stopu — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 0.1 | +27.6% | 2.628 | -6.5% | 1/6 | ✗✗✓✓ | kaldı |
| 0.12 | +27.6% | 2.624 | -6.5% | 0/6 | ✗✗✓✓ | kaldı |
| 0.15 | +27.7% | 2.637 | -6.5% | 0/6 | ✗✗✓✓ | kaldı |

## Portföy seçenekleri ($1000 ile başlangıç, maliyet ve funding dahil)

| Portföy | Başlangıç | Bugün ($) | Yıllık | Sharpe | Maks. düşüş | En kötü yıl | Son 3y | Son 5y | En kötü kriz |
|---|---|---|---|---|---|---|---|---|---|
| Hepsi eşit ağırlık (100 strateji), 1x | 2018-01-16 | 8,598 | +28% | 2.65 | -7% | +3% (2022) | +138% | +200% | -4% |
| En iyi 10 (farklı coin), 1x | 2018-08-28 | 34,512 | +54% | 2.53 | -15% | -1% (2022) | +224% | +318% | -6% |
| En iyi 5 (farklı coin), 1x | 2020-10-16 | 48,508 | +91% | 2.45 | -17% | -5% (2022) | +329% | +638% | -6% |
| En iyi 5 (farklı coin), 2x | 2020-10-16 | 1,511,417 | +238% | 2.45 | -32% | -13% (2022) | +1541% | +4329% | -11% |
| En iyi 5 (farklı coin), 3x | 2020-10-16 | 30,847,177 | +459% | 2.45 | -45% | -22% (2022) | +5507% | +21547% | -16% |
| En iyi 5, 3x + düşüş sigortası (−%10 yarım / −%20 nakit) | 2020-10-16 | 366,215 | +167% | 1.84 | -43% | -8% (2022) | +1398% | +1599% | -8% |
| En iyi 5, 3x + volatilite hedefi %35 | 2020-10-16 | 83,550 | +109% | 2.15 | -32% | -14% (2022) | +1075% | +2522% | -16% |
| En iyi 10, ters volatilite ağırlık, 1x | 2018-08-28 | 56,679 | +64% | 2.61 | -14% | -7% (2022) | +242% | +346% | -5% |
| En iyi 10, HRP ağırlık, 1x | 2018-08-28 | 4,221 | +19% | 1.54 | -11% | -4% (2021) | +290% | +340% | -7% |
| En iyi 5, ters volatilite ağırlık, 1x | 2020-10-16 | 66,605 | +101% | 2.4 | -15% | -6% (2022) | +352% | +601% | -10% |
| En iyi 5, HRP ağırlık, 1x | 2020-10-16 | 5,518 | +33% | 1.6 | -16% | -5% (2021) | +476% | +481% | -4% |
| Rastgele 5 strateji (300 deneme), 1x — medyan | – | 7,476 | – | 1.44 (p10–p90: 1.16–1.71) | -21% | – | – | – | – |
|  | En iyi 5'in Sharpe'ı 2.45: rastgele portföylerin %100'inden iyi |  |  |  |  |  |  |  |  |
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