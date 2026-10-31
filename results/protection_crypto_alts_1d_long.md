# Kasa koruma testi — crypto_alts 1d

Portföy: arenadaki **47 aktif üye**, eşit ağırlık, coin başı en fazla %20. Kabul kuralları sonuçlardan önce yazıldı (`config/arena.yaml` → `protection.accept`). Bir koruma sadece **komşu eşiklerin hepsinde** ve **her zaman diliminde** geçerse açılır.

## Korumasız portföy

Tüm geçmiş: CAGR +31.1%, Sharpe 2.34, maks. düşüş -5.9%, günlük CVaR95 -1.2%. Coin sınırı olmadan: maks. düşüş -7.2%.

Monte Carlo (1 yıl): P(düşüş ≤ −%50) = 0.0%, medyan +30%, kötü %5 +7%.

| Kriz | Getiri | Maks. düşüş |
|---|---|---|
| covid_2020 | +3.7% | -1.0% |
| may_2021 | +1.1% | -2.5% |
| luna_2022 | +2.0% | -3.2% |
| ftx_2022 | -4.7% | -5.0% |
| aug_2024 | -1.4% | -2.3% |
| oct_2025 | -1.7% | -3.1% |

## Kasa düşüş sigortası — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| (0.08, 0.16) | +31.1% | 2.34 | -5.9% | 0/6 | ✗✗✓✓ | kaldı |
|  | MC P(≤−%50): 0.0% (korumasız 0.0%) |  |  |  |  |  |
| (0.1, 0.2) | +31.1% | 2.34 | -5.9% | 0/6 | ✗✗✓✓ | kaldı |
|  | MC P(≤−%50): 0.0% (korumasız 0.0%) |  |  |  |  |  |
| (0.12, 0.25) | +31.1% | 2.34 | -5.9% | 0/6 | ✗✗✓✓ | kaldı |
|  | MC P(≤−%50): 0.0% (korumasız 0.0%) |  |  |  |  |  |

## Volatilite hedefi — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 0.25 | +31.1% | 2.348 | -5.9% | 0/6 | ✗✗✓✓ | kaldı |
| 0.35 | +31.1% | 2.34 | -5.9% | 0/6 | ✗✗✓✓ | kaldı |
| 0.5 | +31.1% | 2.34 | -5.9% | 0/6 | ✗✗✓✓ | kaldı |

## Kasa eğrisi filtresi — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 30 | +20.3% | 1.755 | -15.5% | 2/6 | ✗✗✗✗ | kaldı |
| 60 | +22.7% | 1.89 | -12.5% | 1/6 | ✗✗✗✗ | kaldı |
| 90 | +24.4% | 1.981 | -17.4% | 0/6 | ✗✗✗✓ | kaldı |

## Günlük kayıp limiti — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 0.04 | +31.1% | 2.34 | -5.9% | 0/6 | ✗✗✓✓ | kaldı |
| 0.05 | +31.1% | 2.34 | -5.9% | 0/6 | ✗✗✓✓ | kaldı |
| 0.07 | +31.1% | 2.34 | -5.9% | 0/6 | ✗✗✓✓ | kaldı |

## BTC çöküş bekçisi — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 0.08 | +30.5% | 2.306 | -6.6% | 1/6 | ✗✗✓✓ | kaldı |
| 0.1 | +31.0% | 2.336 | -6.4% | 1/6 | ✗✗✓✓ | kaldı |
| 0.15 | +31.1% | 2.34 | -5.9% | 0/6 | ✗✗✓✓ | kaldı |

## Felaket stopu — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 0.1 | +28.5% | 2.21 | -7.8% | 2/6 | ✗✗✓✓ | kaldı |
| 0.12 | +29.6% | 2.255 | -6.7% | 2/6 | ✗✗✓✓ | kaldı |
| 0.15 | +29.4% | 2.232 | -7.0% | 1/6 | ✗✗✓✓ | kaldı |

## Portföy seçenekleri ($1000 ile başlangıç, maliyet ve funding dahil)

| Portföy | Başlangıç | Bugün ($) | Yıllık | Sharpe | Maks. düşüş | En kötü yıl | Son 3y | Son 5y | En kötü kriz |
|---|---|---|---|---|---|---|---|---|---|
| Hepsi eşit ağırlık (47 strateji), 1x | 2018-10-04 | 9,328 | +32% | 2.37 | -6% | +1% (2018) | +143% | +194% | -5% |
| En iyi 10 (farklı coin), 1x | 2019-02-09 | 44,433 | +64% | 2.27 | -15% | +3% (2022) | +292% | +384% | -8% |
| En iyi 5 (farklı coin), 1x | 2019-02-12 | 103,935 | +83% | 2.02 | -20% | -10% (2022) | +588% | +630% | -8% |
| En iyi 5 (farklı coin), 2x | 2019-02-12 | 5,127,126 | +204% | 2.02 | -38% | -23% (2022) | +3732% | +3878% | -15% |
| En iyi 5 (farklı coin), 3x | 2019-02-12 | 125,536,212 | +361% | 2.02 | -53% | -36% (2022) | +17412% | +16302% | -23% |
| En iyi 5, 3x + düşüş sigortası (−%10 yarım / −%20 nakit) | 2019-02-12 | 222,695 | +102% | 1.34 | -62% | -32% (2022) | +1896% | +1041% | -12% |
| En iyi 5, 3x + volatilite hedefi %35 | 2019-02-12 | 421,689 | +120% | 1.94 | -36% | -8% (2022) | +1295% | +1986% | -17% |
| En iyi 10, ters volatilite ağırlık, 1x | 2019-02-09 | 50,096 | +66% | 2.27 | -13% | +7% (2022) | +266% | +430% | -10% |
| En iyi 10, HRP ağırlık, 1x | 2019-02-09 | 3,849 | +19% | 1.18 | -17% | -2% (2022) | +144% | +150% | -0% |
| En iyi 5, ters volatilite ağırlık, 1x | 2019-02-12 | 155,633 | +93% | 1.97 | -21% | -1% (2022) | +873% | +929% | -10% |
| En iyi 5, HRP ağırlık, 1x | 2019-02-12 | 5,714 | +25% | 1.11 | -17% | -5% (2022) | +248% | +246% | -5% |
| Rastgele 5 strateji (300 deneme), 1x — medyan | – | 8,807 | – | 1.41 (p10–p90: 1.09–1.66) | -22% | – | – | – | – |
|  | En iyi 5'in Sharpe'ı 2.02: rastgele portföylerin %100'inden iyi |  |  |  |  |  |  |  |  |
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