# Çekirdek çalışma — 1d

Sabit ayarlı 6 kural × 3 portföy = **18 deneme** (ayar taraması yok). Kabul kuralları sonuçlardan önce yazıldı (`config/core.yaml`): her ileri pencerede aynı varlığın al-tutuna göre düşüş ≥ 1/3 az, Sharpe en fazla 0.10 düşük, getiri pozitif.

## BTC

| Kural | Tüm geçmiş $1000 → | Yıllık | Sharpe | Maks. düşüş | 2022-10 → $ | 2023-10 → $ | 2024-10 → $ | 2022-10 DD | 2023-10 DD | 2024-10 DD | Onay |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Al-tut | 9,883 | +32% | 0.76 | -77% | 4,175 | 2,874 | 1,211 | -53% | -53% | -53% | – |
| Volatilite hedefi %40 | 7,814 | +28% | 0.8 | -65% | 3,413 | 2,630 | 1,129 | -52% | -52% | -52% | ❌ |
| Trend (SMA200) | 11,572 | +35% | 0.9 | -64% | 3,440 | 2,639 | 1,353 | -32% | -32% | -32% | ✅ |
| Zaman serisi momentumu (30/90/180g) | 15,003 | +39% | 1.02 | -51% | 3,222 | 2,680 | 1,426 | -26% | -26% | -26% | ✅ |
| Momentum + vol hedefi | 8,176 | +29% | 1.05 | -39% | 2,717 | 2,494 | 1,339 | -25% | -25% | -25% | ✅ |
| SMA200 + momentum + vol hedefi | 7,639 | +28% | 0.96 | -45% | 3,038 | 2,600 | 1,364 | -25% | -25% | -25% | ✅ |

## ETH

| Kural | Tüm geçmiş $1000 → | Yıllık | Sharpe | Maks. düşüş | 2022-10 → $ | 2023-10 → $ | 2024-10 → $ | 2022-10 DD | 2023-10 DD | 2024-10 DD | Onay |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Al-tut | 5,129 | +22% | 0.66 | -83% | 1,820 | 1,549 | 930 | -68% | -68% | -68% | – |
| Volatilite hedefi %40 | 6,383 | +25% | 0.73 | -57% | 2,162 | 1,779 | 946 | -56% | -56% | -56% | ❌ |
| Trend (SMA200) | 17,762 | +42% | 0.89 | -74% | 2,333 | 1,969 | 1,179 | -38% | -38% | -38% | ✅ |
| Zaman serisi momentumu (30/90/180g) | 15,359 | +39% | 0.88 | -64% | 1,655 | 1,744 | 1,203 | -40% | -40% | -37% | ✅ |
| Momentum + vol hedefi | 7,818 | +28% | 0.99 | -31% | 1,673 | 1,711 | 1,089 | -27% | -27% | -27% | ✅ |
| SMA200 + momentum + vol hedefi | 10,672 | +33% | 1.07 | -38% | 2,184 | 1,941 | 1,123 | -23% | -23% | -23% | ✅ |

## BTC+ETH

| Kural | Tüm geçmiş $1000 → | Yıllık | Sharpe | Maks. düşüş | 2022-10 → $ | 2023-10 → $ | 2024-10 → $ | 2022-10 DD | 2023-10 DD | 2024-10 DD | Onay |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Al-tut | 8,909 | +30% | 0.74 | -76% | 2,942 | 2,233 | 1,105 | -60% | -60% | -60% | – |
| Volatilite hedefi %40 | 7,568 | +28% | 0.8 | -59% | 2,799 | 2,219 | 1,050 | -53% | -53% | -53% | ❌ |
| Trend (SMA200) | 18,030 | +42% | 0.99 | -62% | 2,973 | 2,382 | 1,300 | -29% | -29% | -29% | ✅ |
| Zaman serisi momentumu (30/90/180g) | 17,771 | +42% | 1.02 | -56% | 2,396 | 2,232 | 1,335 | -30% | -30% | -30% | ✅ |
| Momentum + vol hedefi | 8,387 | +29% | 1.11 | -35% | 2,178 | 2,104 | 1,218 | -26% | -26% | -26% | ✅ |
| SMA200 + momentum + vol hedefi | 9,637 | +32% | 1.11 | -38% | 2,650 | 2,305 | 1,256 | -21% | -21% | -21% | ✅ |

## Zayıf yönler

- Kurallar literatürden; ama kriptoda bu literatür kısa (2014 sonrası). Ayarlar (200 gün, 30/90/180 gün, %40) standart değerlerdir, kriptoya göre seçilmedi.
- Sadece BTC/ETH: alt-coin getirisi yok; buna karşılık survivorship riski çok düşük.
- Spot varsayımı: perp ile yapılırsa funding maliyeti eklenir.
- Üç ileri pencere iç içedir (2022 penceresi 2023 ve 2024'ü de içerir); bağımsız üç test değildir.