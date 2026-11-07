# Çekirdek çalışma — 4h

Sabit ayarlı 6 kural × 3 portföy = **18 deneme** (ayar taraması yok). Kabul kuralları sonuçlardan önce yazıldı (`config/core.yaml`): her ileri pencerede aynı varlığın al-tutuna göre düşüş ≥ 1/3 az, Sharpe en fazla 0.10 düşük, getiri pozitif.

## BTC

| Kural | Tüm geçmiş $1000 → | Yıllık | Sharpe | Maks. düşüş | 2022-10 → $ | 2023-10 → $ | 2024-10 → $ | 2022-10 DD | 2023-10 DD | 2024-10 DD | Onay |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Al-tut | 5,744 | +22% | 0.63 | -81% | 4,018 | 2,727 | 1,141 | -53% | -53% | -53% | – |
| Volatilite hedefi %40 | 7,055 | +25% | 0.75 | -66% | 3,358 | 2,476 | 1,087 | -52% | -52% | -52% | ❌ |
| Trend (SMA200) | 13,465 | +34% | 0.91 | -63% | 3,428 | 2,644 | 1,292 | -37% | -37% | -37% | ❌ |
| Zaman serisi momentumu (30/90/180g) | 11,685 | +32% | 0.91 | -55% | 3,320 | 2,658 | 1,398 | -26% | -26% | -26% | ✅ |
| Momentum + vol hedefi | 8,874 | +28% | 1.07 | -37% | 2,979 | 2,581 | 1,371 | -23% | -23% | -23% | ✅ |
| SMA200 + momentum + vol hedefi | 10,316 | +30% | 1.07 | -41% | 3,195 | 2,664 | 1,325 | -30% | -30% | -30% | ✅ |

## ETH

| Kural | Tüm geçmiş $1000 → | Yıllık | Sharpe | Maks. düşüş | 2022-10 → $ | 2023-10 → $ | 2024-10 → $ | 2022-10 DD | 2023-10 DD | 2024-10 DD | Onay |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Al-tut | 3,083 | +14% | 0.57 | -94% | 1,741 | 1,427 | 859 | -68% | -68% | -68% | – |
| Volatilite hedefi %40 | 2,969 | +13% | 0.5 | -72% | 1,819 | 1,493 | 871 | -60% | -60% | -60% | ❌ |
| Trend (SMA200) | 27,024 | +45% | 0.96 | -59% | 1,910 | 1,580 | 1,012 | -41% | -41% | -41% | ✅ |
| Zaman serisi momentumu (30/90/180g) | 17,660 | +38% | 0.89 | -55% | 1,623 | 1,721 | 1,102 | -40% | -40% | -40% | ✅ |
| Momentum + vol hedefi | 7,333 | +25% | 0.96 | -32% | 1,588 | 1,657 | 1,061 | -30% | -30% | -30% | ✅ |
| SMA200 + momentum + vol hedefi | 10,704 | +31% | 1.06 | -32% | 1,865 | 1,617 | 1,048 | -29% | -29% | -29% | ✅ |

## BTC+ETH

| Kural | Tüm geçmiş $1000 → | Yıllık | Sharpe | Maks. düşüş | 2022-10 → $ | 2023-10 → $ | 2024-10 → $ | 2022-10 DD | 2023-10 DD | 2024-10 DD | Onay |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Al-tut | 5,376 | +21% | 0.62 | -88% | 2,810 | 2,079 | 1,029 | -60% | -60% | -60% | – |
| Volatilite hedefi %40 | 4,905 | +20% | 0.66 | -65% | 2,540 | 1,968 | 988 | -56% | -56% | -56% | ❌ |
| Trend (SMA200) | 22,836 | +42% | 1.02 | -57% | 2,679 | 2,130 | 1,177 | -32% | -32% | -32% | ✅ |
| Zaman serisi momentumu (30/90/180g) | 16,507 | +37% | 0.97 | -52% | 2,401 | 2,202 | 1,265 | -32% | -32% | -32% | ✅ |
| Momentum + vol hedefi | 8,420 | +27% | 1.09 | -35% | 2,218 | 2,103 | 1,218 | -26% | -26% | -26% | ✅ |
| SMA200 + momentum + vol hedefi | 11,112 | +31% | 1.15 | -34% | 2,507 | 2,124 | 1,196 | -24% | -24% | -24% | ✅ |

## Zayıf yönler

- Kurallar literatürden; ama kriptoda bu literatür kısa (2014 sonrası). Ayarlar (200 gün, 30/90/180 gün, %40) standart değerlerdir, kriptoya göre seçilmedi.
- Sadece BTC/ETH: alt-coin getirisi yok; buna karşılık survivorship riski çok düşük.
- Spot varsayımı: perp ile yapılırsa funding maliyeti eklenir.
- Üç ileri pencere iç içedir (2022 penceresi 2023 ve 2024'ü de içerir); bağımsız üç test değildir.

## H052 varyantları (4 deneme, kabul kuralları önceden yazıldı)

Kabul: tüm geçmişte VE her ileri pencerede Sharpe temel kuraldan (H052) yüksek, maks. düşüş en fazla 5 puan derin. Karşılaştırma aynı zaman diliminde ve ortak dönemde; perp funding her ikisinde de düşüldü.

| Varyant | Sharpe (tüm) | Temel | Maks. düşüş | Temel | 2022-10 SR v/t | 2023-10 SR v/t | 2024-10 SR v/t | Onay |
|---|---|---|---|---|---|---|---|---|
| Daha fazla büyük coin (BTC, ETH, SOL, BNB, XRP) | 0.94 | 1.05 | -35% | -35% | 0.56/0.81 | 0.85/0.89 | 0.51/0.35 | ❌ |
| Düşüşte short (perp) | 0.93 | 1.05 | -46% | -35% | 0.67/0.81 | 0.81/0.89 | 0.47/0.35 | ❌ |
| İşlem yapmama bandı %10 | 1.07 | 1.05 | -35% | -35% | 0.84/0.81 | 0.92/0.89 | 0.39/0.35 | ✅ |
| 1h zaman dilimi | 0.94 | 1.05 | -37% | -35% | 0.73/0.81 | 0.83/0.89 | 0.44/0.35 | ❌ |

## H054 risk seviyeleri (kaldıraç yok; seçim kuralı önceden yazıldı)

Kural: tüm geçmişte ve her ileri pencerede maks. düşüş ≥ -40% kalan EN YÜKSEK hedef.

| Vol hedefi | $1000 → | Yıllık | Sharpe | Maks. düşüş | 2022-10 → $ / DD | 2023-10 → $ / DD | 2024-10 → $ / DD | Sınırda |
|---|---|---|---|---|---|---|---|---|
| %40 | 9,537 | +29% | 1.07 | -35% | 2,249 / -24% | 1,954 / -24% | 1,144 / -24% | ✅ |
| %60 | 13,184 | +34% | 0.99 | -47% | 2,318 / -32% | 1,945 / -32% | 1,122 / -32% | ❌ |
| %80 | 15,670 | +37% | 0.97 | -56% | 2,220 / -33% | 1,851 / -33% | 1,089 / -33% | ❌ |

**Seçilen:** %40

## Funding arbitrajı (spot long + perp short)

Veri (Binance, Bitget için vekil): {'BTCUSDT': ['2020-01-01', '2026-10-31'], 'ETHUSDT': ['2020-01-01', '2026-10-31']}

| Kural | $1000 → | Yıllık | Sharpe | Maks. düşüş | H054 ile korelasyon | 50/50 H054+arb Sharpe | H054 Sharpe | Onay |
|---|---|---|---|---|---|---|---|---|
| always_on | 1,540 | +7% | 10.35 | -0% | 0.082 | 1.34 | 1.13 | ✅ |
|  ↳ 2022-10 → | 1,151 | +4% | 15.52 | -0% | | 0.95 (DD -12%) | 0.83 (DD -23%) | |
|  ↳ 2023-10 → | 1,121 | +4% | 15.64 | -0% | | 1.02 (DD -12%) | 0.9 (DD -23%) | |
|  ↳ 2024-10 → | 1,052 | +3% | 17.29 | -0% | | 0.49 (DD -12%) | 0.39 (DD -23%) | |
| positive_only | 1,432 | +5% | 8.1 | -1% | 0.071 | 1.31 | 1.13 | ✅ |
|  ↳ 2022-10 → | 1,101 | +2% | 8.51 | -0% | | 0.91 (DD -12%) | 0.83 (DD -23%) | |
|  ↳ 2023-10 → | 1,084 | +3% | 9.03 | -0% | | 0.98 (DD -12%) | 0.9 (DD -23%) | |
|  ↳ 2024-10 → | 1,025 | +1% | 6.2 | -0% | | 0.44 (DD -12%) | 0.39 (DD -23%) | |

Sınırlar: spot–perp baz farkı ve Binance/Bitget farkı modellenmez; büyük yükselişte short perp için marjin eklemek gerekir.

## Boştaki nakitle funding arbitrajı (kriter: ileri dönemlerde en yüksek kâr)

H054'ün ortalama boştaki nakdi: %58. Kabul: her ileri pencerede H054'ten fazla kazanmalı, düşüşü en fazla 3 puan derin olmalı. Kabul edilenlerden ileri dönemlerde en çok kazanan seçilir.

| Seçenek | Tüm geçmiş → | Yıllık | Maks. düşüş | 2022-10 → | 2023-10 → | 2024-10 → | Onay |
|---|---|---|---|---|---|---|---|
| H054 tek başına | 7,457 | +34% | -26% | 2,252 | 1,952 | 1,147 | – |
| H054 + boştaki nakitle arbitraj (always_on) | 8,737 | +37% | -24% | 2,294 | 1,984 | 1,159 | ✅ |
| H054 + boştaki nakitle arbitraj (positive_only) | 8,454 | +37% | -26% | 2,265 | 1,969 | 1,153 | ✅ |

**Bot için seçilen:** `idle_always_on`