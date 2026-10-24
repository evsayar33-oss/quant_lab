# Kasa koruma testi — crypto_alts 1d

Portföy: arenadaki **32 aktif üye**, eşit ağırlık, coin başı en fazla %20. Kabul kuralları sonuçlardan önce yazıldı (`config/arena.yaml` → `protection.accept`). Bir koruma sadece **komşu eşiklerin hepsinde** ve **her zaman diliminde** geçerse açılır.

## Korumasız portföy

Tüm geçmiş: CAGR +23.5%, Sharpe 1.475, maks. düşüş -11.9%, günlük CVaR95 -1.6%. Coin sınırı olmadan: maks. düşüş -12.3%.

Monte Carlo (1 yıl): P(düşüş ≤ −%50) = 0.0%, medyan +22%, kötü %5 -2%.

| Kriz | Getiri | Maks. düşüş |
|---|---|---|
| covid_2020 | +0.0% | 0.0% |
| may_2021 | +10.4% | -6.2% |
| luna_2022 | +18.2% | -8.8% |
| ftx_2022 | +11.8% | -3.7% |
| aug_2024 | +7.0% | -4.3% |
| oct_2025 | +15.7% | -2.1% |

## Kasa düşüş sigortası — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| (0.08, 0.16) | +20.9% | 1.413 | -10.7% | 1/6 | ✗✓✓✓ | kaldı |
|  | MC P(≤−%50): 0.0% (korumasız 0.0%) |  |  |  |  |  |
| (0.1, 0.2) | +21.9% | 1.445 | -11.0% | 0/6 | ✗✓✓✓ | kaldı |
|  | MC P(≤−%50): 0.0% (korumasız 0.0%) |  |  |  |  |  |
| (0.12, 0.25) | +23.5% | 1.475 | -11.9% | 0/6 | ✗✗✓✓ | kaldı |
|  | MC P(≤−%50): 0.0% (korumasız 0.0%) |  |  |  |  |  |

## Volatilite hedefi — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 0.25 | +22.3% | 1.492 | -10.1% | 4/6 | ✗✓✓✓ | kaldı |
| 0.35 | +23.2% | 1.483 | -11.8% | 2/6 | ✗✓✓✓ | kaldı |
| 0.5 | +23.5% | 1.477 | -11.9% | 0/6 | ✗✗✓✓ | kaldı |

## Kasa eğrisi filtresi — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 30 | +16.7% | 1.17 | -9.3% | 0/6 | ✗✓✗✗ | kaldı |
| 60 | +17.6% | 1.202 | -11.6% | 0/6 | ✗✓✗✗ | kaldı |
| 90 | +18.9% | 1.269 | -11.3% | 0/6 | ✗✓✗✓ | kaldı |

## Günlük kayıp limiti — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 0.04 | +23.0% | 1.454 | -11.9% | 0/6 | ✗✗✓✓ | kaldı |
| 0.05 | +23.5% | 1.475 | -11.9% | 0/6 | ✗✗✓✓ | kaldı |
| 0.07 | +23.5% | 1.475 | -11.9% | 0/6 | ✗✗✓✓ | kaldı |

## BTC çöküş bekçisi — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 0.08 | +23.5% | 1.475 | -11.9% | 0/6 | ✗✗✓✓ | kaldı |
| 0.1 | +23.5% | 1.475 | -11.9% | 0/6 | ✗✗✓✓ | kaldı |
| 0.15 | +23.5% | 1.475 | -11.9% | 0/6 | ✗✗✓✓ | kaldı |

## Felaket stopu — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 0.1 | +22.8% | 1.444 | -12.6% | 0/6 | ✗✗✓✓ | kaldı |
| 0.12 | +22.6% | 1.433 | -12.6% | 0/6 | ✗✗✓✓ | kaldı |
| 0.15 | +23.0% | 1.453 | -12.3% | 0/6 | ✗✗✓✓ | kaldı |

## Portföy seçenekleri ($1000 ile başlangıç, maliyet ve funding dahil)

| Portföy | Başlangıç | Bugün ($) | Yıllık | Sharpe | Maks. düşüş | En kötü yıl | Son 3y | Son 5y | En kötü kriz |
|---|---|---|---|---|---|---|---|---|---|
| Hepsi eşit ağırlık (32 strateji), 1x | 2021-06-01 | 5,682 | +38% | 1.83 | -12% | +2% (2023) | +161% | +411% | -9% |
| En iyi 10 (farklı coin), 1x | 2021-06-01 | 10,102 | +54% | 1.9 | -15% | +3% (2023) | +229% | +752% | -15% |
| En iyi 5 (farklı coin), 1x | 2021-11-25 | 11,813 | +66% | 1.99 | -16% | +6% (2023) | +279% | – | -10% |
| En iyi 5 (farklı coin), 2x | 2021-11-25 | 98,126 | +155% | 1.99 | -31% | +10% (2023) | +1111% | – | -19% |
| En iyi 5 (farklı coin), 3x | 2021-11-25 | 578,698 | +266% | 1.99 | -44% | +10% (2023) | +3165% | – | -27% |
| En iyi 5, 3x + düşüş sigortası (−%10 yarım / −%20 nakit) | 2021-11-25 | 4,410 | +35% | 0.82 | -64% | -32% (2024) | +76% | – | -28% |
| En iyi 5, 3x + volatilite hedefi %35 | 2021-11-25 | 36,972 | +109% | 1.94 | -28% | +16% (2023) | +569% | – | -9% |
| En iyi 10, ters volatilite ağırlık, 1x | 2021-06-01 | 15,824 | +67% | 2.02 | -16% | +2% (2023) | +366% | +1024% | -11% |
| En iyi 10, HRP ağırlık, 1x | 2021-06-01 | 4,492 | +32% | 1.75 | -17% | +3% (2021) | +224% | +349% | -4% |
| En iyi 5, ters volatilite ağırlık, 1x | 2021-11-25 | 15,214 | +74% | 2.01 | -18% | +2% (2021) | +342% | – | -11% |
| En iyi 5, HRP ağırlık, 1x | 2021-11-25 | 3,012 | +25% | 1.37 | -14% | -5% (2023) | +180% | – | -12% |
| Rastgele 5 strateji (300 deneme), 1x — medyan | – | 5,791 | – | 1.52 (p10–p90: 1.31–1.77) | -18% | – | – | – | – |
|  | En iyi 5'in Sharpe'ı 1.99: rastgele portföylerin %100'inden iyi |  |  |  |  |  |  |  |  |
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