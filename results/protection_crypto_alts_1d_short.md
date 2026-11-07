# Kasa koruma testi — crypto_alts 1d

Portföy: arenadaki **42 aktif üye**, eşit ağırlık, coin başı en fazla %20. Kabul kuralları sonuçlardan önce yazıldı (`config/arena.yaml` → `protection.accept`). Bir koruma sadece **komşu eşiklerin hepsinde** ve **her zaman diliminde** geçerse açılır.

## Korumasız portföy

Tüm geçmiş: CAGR +15.5%, Sharpe 0.95, maks. düşüş -38.9%, günlük CVaR95 -1.8%. Coin sınırı olmadan: maks. düşüş -48.5%.

Monte Carlo (1 yıl): P(düşüş ≤ −%50) = 0.0%, medyan +14%, kötü %5 -10%.

| Kriz | Getiri | Maks. düşüş |
|---|---|---|
| covid_2020 | +2.3% | -9.1% |
| may_2021 | +13.2% | -9.7% |
| luna_2022 | +19.0% | -8.4% |
| ftx_2022 | +10.3% | -4.0% |
| aug_2024 | +6.0% | -3.6% |
| oct_2025 | +15.2% | -2.6% |

## Kasa düşüş sigortası — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| (0.08, 0.16) | +12.3% | 0.996 | -18.2% | 2/6 | ✗✓✓✓ | kaldı |
|  | MC P(≤−%50): 0.0% (korumasız 0.0%) |  |  |  |  |  |
| (0.1, 0.2) | +13.2% | 0.997 | -20.5% | 2/6 | ✗✓✓✓ | kaldı |
|  | MC P(≤−%50): 0.0% (korumasız 0.0%) |  |  |  |  |  |
| (0.12, 0.25) | +12.8% | 0.94 | -28.6% | 1/6 | ✗✓✓✓ | kaldı |
|  | MC P(≤−%50): 0.0% (korumasız 0.0%) |  |  |  |  |  |

## Volatilite hedefi — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 0.25 | +15.3% | 0.996 | -35.1% | 4/6 | ✗✓✓✓ | kaldı |
| 0.35 | +15.5% | 0.972 | -37.6% | 4/6 | ✗✓✓✓ | kaldı |
| 0.5 | +15.5% | 0.951 | -38.9% | 0/6 | ✗✗✓✓ | kaldı |

## Kasa eğrisi filtresi — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 30 | +12.6% | 0.866 | -24.6% | 1/6 | ✗✓✓✓ | kaldı |
| 60 | +11.7% | 0.816 | -28.4% | 0/6 | ✗✓✗✓ | kaldı |
| 90 | +13.3% | 0.905 | -21.9% | 0/6 | ✗✓✓✓ | kaldı |

## Günlük kayıp limiti — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 0.04 | +15.1% | 0.93 | -39.3% | 0/6 | ✗✗✓✓ | kaldı |
| 0.05 | +15.5% | 0.95 | -38.9% | 0/6 | ✗✗✓✓ | kaldı |
| 0.07 | +15.5% | 0.95 | -38.9% | 0/6 | ✗✗✓✓ | kaldı |

## BTC çöküş bekçisi — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 0.08 | +15.5% | 0.95 | -38.9% | 0/6 | ✗✗✓✓ | kaldı |
| 0.1 | +15.5% | 0.95 | -38.9% | 0/6 | ✗✗✓✓ | kaldı |
| 0.15 | +15.5% | 0.95 | -38.9% | 0/6 | ✗✗✓✓ | kaldı |

## Felaket stopu — ❌ GEÇMEDİ

| Eşik | CAGR | Sharpe | Maks. düşüş | Krizlerde daha az düşüş | Kriz/DD/Sharpe/CAGR | Sonuç |
|---|---|---|---|---|---|---|
| 0.1 | +14.6% | 0.913 | -39.7% | 3/6 | ✗✗✓✓ | kaldı |
| 0.12 | +14.2% | 0.89 | -40.7% | 3/6 | ✗✗✓✓ | kaldı |
| 0.15 | +15.3% | 0.943 | -38.1% | 3/6 | ✗✓✓✓ | kaldı |

## Portföy seçenekleri ($1000 ile başlangıç, maliyet ve funding dahil)

| Portföy | Başlangıç | Bugün ($) | Yıllık | Sharpe | Maks. düşüş | En kötü yıl | Son 3y | Son 5y | En kötü kriz |
|---|---|---|---|---|---|---|---|---|---|
| Hepsi eşit ağırlık (42 strateji), 1x | 2018-07-30 | 3,572 | +17% | 0.98 | -39% | -18% (2020) | +175% | +418% | -10% |
| En iyi 10 (farklı coin), 1x | 2018-09-25 | 2,043 | +9% | 0.46 | -86% | -48% (2021) | +256% | +833% | -13% |
| En iyi 5 (farklı coin), 1x | 2020-09-16 | 4,871 | +30% | 0.91 | -72% | -61% (2021) | +385% | +1518% | -22% |
| En iyi 5 (farklı coin), 2x | 2020-09-16 | 11,109 | +48% | 0.91 | -94% | -88% (2021) | +1762% | +15940% | -44% |
| En iyi 5 (farklı coin), 3x | 2020-09-16 | 11,670 | +49% | 0.91 | -99% | -97% (2021) | +5593% | +99478% | -63% |
| En iyi 5, 3x + düşüş sigortası (−%10 yarım / −%20 nakit) | 2020-09-16 | 1,922 | +11% | 0.47 | -32% | -23% (2020) | +151% | +151% | -13% |
| En iyi 5, 3x + volatilite hedefi %35 | 2020-09-16 | 12,980 | +52% | 1.15 | -69% | -44% (2020) | +784% | +4114% | -14% |
| En iyi 10, ters volatilite ağırlık, 1x | 2018-09-25 | 1,381 | +4% | 0.28 | -89% | -61% (2021) | +269% | +655% | -20% |
| En iyi 10, HRP ağırlık, 1x | 2018-09-25 | 3,610 | +17% | 1.14 | -21% | -4% (2021) | +193% | +280% | -6% |
| En iyi 5, ters volatilite ağırlık, 1x | 2020-09-16 | 2,063 | +13% | 0.49 | -88% | -82% (2021) | +424% | +1289% | -38% |
| En iyi 5, HRP ağırlık, 1x | 2020-09-16 | 3,201 | +21% | 1.11 | -20% | -7% (2021) | +207% | +288% | -12% |
| Rastgele 5 strateji (300 deneme), 1x — medyan | – | 2,927 | – | 0.73 (p10–p90: 0.35–1.14) | -51% | – | – | – | – |
|  | En iyi 5'in Sharpe'ı 0.91: rastgele portföylerin %69'inden iyi |  |  |  |  |  |  |  |  |
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