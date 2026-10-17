# Çekirdek çalışma — 4h

Sabit ayarlı 6 kural × 3 portföy = **18 deneme** (ayar taraması yok). Kabul kuralları sonuçlardan önce yazıldı (`config/core.yaml`): her ileri pencerede aynı varlığın al-tutuna göre düşüş ≥ 1/3 az, Sharpe en fazla 0.10 düşük, getiri pozitif.

## BTC

| Kural | Tüm geçmiş $1000 → | Yıllık | Sharpe | Maks. düşüş | 2022-10 → $ | 2023-10 → $ | 2024-10 → $ | 2022-10 DD | 2023-10 DD | 2024-10 DD | Onay |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Al-tut | 9,851 | +32% | 0.76 | -77% | 4,239 | 2,877 | 1,203 | -53% | -53% | -53% | – |
| Volatilite hedefi %40 | 10,175 | +33% | 0.9 | -66% | 3,543 | 2,612 | 1,147 | -52% | -52% | -52% | ❌ |
| Trend (SMA200) | 13,788 | +38% | 0.95 | -63% | 3,574 | 2,756 | 1,357 | -37% | -37% | -37% | ❌ |
| Zaman serisi momentumu (30/90/180g) | 15,839 | +40% | 1.04 | -55% | 3,488 | 2,788 | 1,429 | -26% | -26% | -26% | ✅ |
| Momentum + vol hedefi | 10,691 | +33% | 1.2 | -38% | 3,116 | 2,690 | 1,402 | -23% | -23% | -23% | ✅ |
| SMA200 + momentum + vol hedefi | 10,739 | +33% | 1.12 | -41% | 3,346 | 2,790 | 1,394 | -30% | -30% | -30% | ✅ |

## ETH

| Kural | Tüm geçmiş $1000 → | Yıllık | Sharpe | Maks. düşüş | 2022-10 → $ | 2023-10 → $ | 2024-10 → $ | 2022-10 DD | 2023-10 DD | 2024-10 DD | Onay |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Al-tut | 5,102 | +22% | 0.65 | -83% | 1,852 | 1,517 | 913 | -68% | -68% | -68% | – |
| Volatilite hedefi %40 | 4,866 | +21% | 0.67 | -60% | 1,921 | 1,576 | 920 | -60% | -60% | -60% | ❌ |
| Trend (SMA200) | 29,832 | +51% | 1.01 | -59% | 2,109 | 1,744 | 1,117 | -40% | -40% | -40% | ✅ |
| Zaman serisi momentumu (30/90/180g) | 20,500 | +44% | 0.96 | -55% | 1,668 | 1,743 | 1,134 | -43% | -43% | -42% | ✅ |
| Momentum + vol hedefi | 7,858 | +28% | 1.03 | -31% | 1,657 | 1,705 | 1,102 | -30% | -30% | -30% | ✅ |
| SMA200 + momentum + vol hedefi | 11,538 | +35% | 1.13 | -32% | 2,011 | 1,744 | 1,130 | -27% | -27% | -27% | ✅ |

## BTC+ETH

| Kural | Tüm geçmiş $1000 → | Yıllık | Sharpe | Maks. düşüş | 2022-10 → $ | 2023-10 → $ | 2024-10 → $ | 2022-10 DD | 2023-10 DD | 2024-10 DD | Onay |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Al-tut | 8,765 | +30% | 0.73 | -77% | 2,975 | 2,201 | 1,089 | -60% | -60% | -60% | – |
| Volatilite hedefi %40 | 7,520 | +28% | 0.82 | -61% | 2,681 | 2,076 | 1,042 | -56% | -56% | -56% | ❌ |
| Trend (SMA200) | 24,275 | +47% | 1.07 | -57% | 2,873 | 2,284 | 1,267 | -32% | -32% | -32% | ✅ |
| Zaman serisi momentumu (30/90/180g) | 20,657 | +44% | 1.07 | -53% | 2,495 | 2,269 | 1,297 | -33% | -33% | -33% | ✅ |
| Momentum + vol hedefi | 9,560 | +32% | 1.2 | -35% | 2,317 | 2,177 | 1,255 | -26% | -26% | -26% | ✅ |
| SMA200 + momentum + vol hedefi | 11,768 | +35% | 1.22 | -34% | 2,663 | 2,257 | 1,274 | -24% | -24% | -24% | ✅ |

## Zayıf yönler

- Kurallar literatürden; ama kriptoda bu literatür kısa (2014 sonrası). Ayarlar (200 gün, 30/90/180 gün, %40) standart değerlerdir, kriptoya göre seçilmedi.
- Sadece BTC/ETH: alt-coin getirisi yok; buna karşılık survivorship riski çok düşük.
- Spot varsayımı: perp ile yapılırsa funding maliyeti eklenir.
- Üç ileri pencere iç içedir (2022 penceresi 2023 ve 2024'ü de içerir); bağımsız üç test değildir.

## H052 varyantları (4 deneme, kabul kuralları önceden yazıldı)

Kabul: tüm geçmişte VE her ileri pencerede Sharpe temel kuraldan (H052) yüksek, maks. düşüş en fazla 5 puan derin. Karşılaştırma aynı zaman diliminde ve ortak dönemde; perp funding her ikisinde de düşüldü.

| Varyant | Sharpe (tüm) | Temel | Maks. düşüş | Temel | 2022-10 SR v/t | 2023-10 SR v/t | 2024-10 SR v/t | Onay |
|---|---|---|---|---|---|---|---|---|
| Daha fazla büyük coin (BTC, ETH, SOL, BNB, XRP) | 1.02 | 1.11 | -32% | -35% | 0.7/0.88 | 0.96/0.98 | 0.66/0.5 | ❌ |
| Düşüşte short (perp) | 0.88 | 1.11 | -47% | -35% | 0.71/0.88 | 0.87/0.98 | 0.55/0.5 | ❌ |
| İşlem yapmama bandı %10 | 1.14 | 1.11 | -35% | -35% | 0.91/0.88 | 1.01/0.98 | 0.54/0.5 | ✅ |
| 1h zaman dilimi | 1.0 | 1.11 | -37% | -35% | 0.78/0.88 | 0.9/0.98 | 0.56/0.5 | ❌ |

## H054 risk seviyeleri (kaldıraç yok; seçim kuralı önceden yazıldı)

Kural: tüm geçmişte ve her ileri pencerede maks. düşüş ≥ -40% kalan EN YÜKSEK hedef.

| Vol hedefi | $1000 → | Yıllık | Sharpe | Maks. düşüş | 2022-10 → $ / DD | 2023-10 → $ / DD | 2024-10 → $ / DD | Sınırda |
|---|---|---|---|---|---|---|---|---|
| %40 | 10,164 | +33% | 1.14 | -35% | 2,405 / -23% | 2,089 / -23% | 1,226 / -23% | ✅ |
| %60 | 14,078 | +38% | 1.05 | -47% | 2,489 / -32% | 2,088 / -32% | 1,209 / -32% | ❌ |
| %80 | 16,772 | +41% | 1.03 | -56% | 2,390 / -33% | 1,993 / -33% | 1,176 / -33% | ❌ |

**Seçilen:** %40

## Funding arbitrajı (spot long + perp short)

Veri (Binance, Bitget için vekil): {'BTCUSDT': ['2020-01-01', '2026-09-30'], 'ETHUSDT': ['2020-01-01', '2026-09-30']}

| Kural | $1000 → | Yıllık | Sharpe | Maks. düşüş | H054 ile korelasyon | 50/50 H054+arb Sharpe | H054 Sharpe | Onay |
|---|---|---|---|---|---|---|---|---|
| always_on | 1,538 | +7% | 10.38 | -0% | 0.081 | 1.42 | 1.21 | ✅ |
|  ↳ 2022-10 → | 1,149 | +4% | 15.54 | -0% | | 1.08 (DD -12%) | 0.96 (DD -23%) | |
|  ↳ 2023-10 → | 1,119 | +4% | 15.69 | -0% | | 1.2 (DD -12%) | 1.07 (DD -23%) | |
|  ↳ 2024-10 → | 1,051 | +3% | 17.21 | -0% | | 0.78 (DD -12%) | 0.68 (DD -23%) | |
| positive_only | 1,433 | +5% | 8.17 | -1% | 0.07 | 1.39 | 1.21 | ✅ |
|  ↳ 2022-10 → | 1,102 | +2% | 8.71 | -0% | | 1.04 (DD -12%) | 0.96 (DD -23%) | |
|  ↳ 2023-10 → | 1,084 | +3% | 9.31 | -0% | | 1.17 (DD -12%) | 1.07 (DD -23%) | |
|  ↳ 2024-10 → | 1,025 | +1% | 6.6 | -0% | | 0.73 (DD -12%) | 0.68 (DD -23%) | |

Sınırlar: spot–perp baz farkı ve Binance/Bitget farkı modellenmez; büyük yükselişte short perp için marjin eklemek gerekir.

## Boştaki nakitle funding arbitrajı (kriter: ileri dönemlerde en yüksek kâr)

H054'ün ortalama boştaki nakdi: %59. Kabul: her ileri pencerede H054'ten fazla kazanmalı, düşüşü en fazla 3 puan derin olmalı. Kabul edilenlerden ileri dönemlerde en çok kazanan seçilir.

| Seçenek | Tüm geçmiş → | Yıllık | Maks. düşüş | 2022-10 → | 2023-10 → | 2024-10 → | Onay |
|---|---|---|---|---|---|---|---|
| H054 tek başına | 8,506 | +37% | -26% | 2,577 | 2,234 | 1,316 | – |
| H054 + boştaki nakitle arbitraj (always_on) | 9,966 | +41% | -24% | 2,625 | 2,270 | 1,330 | ✅ |
| H054 + boştaki nakitle arbitraj (positive_only) | 9,645 | +40% | -26% | 2,593 | 2,253 | 1,322 | ✅ |

**Bot için seçilen:** `idle_always_on`