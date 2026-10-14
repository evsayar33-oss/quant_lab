# quant_lab — Strateji Laboratuvarı ve Karar Merkezi

Bu repo tüm al-sat botlarının **nihai karar merkezidir**. Bir bot, bir stratejiyi ancak bu repoda
doğrulanmış ve `ACCEPT` kararı almış ise kullanır. LLM yok, ücretli API yok. Her şey GitHub Actions'ta çalışır.

## Akış

```
Fikir (makale / awesome-systematic-trading)
   → hypotheses/registry.yaml  (H0xx)
   → Walk-forward + Deflated Sharpe + bootstrap + 2× maliyet testi
   → decisions/registry.json   (ACCEPT / WATCH / REJECT + hedef ağırlıklar)
   → Botlar lab/client.py ile okur, sadece ACCEPT'e göre işlem yapar
```

## Telefondan kullanım

| İş | Nasıl |
|---|---|
| Hızlı deneme | Actions → **Ad-hoc backtest** → Run workflow. Motor: `lab`, `vbt` veya `bt`. Sonuç Telegram'a ve artifact'e gelir. Karar kaydını değiştirmez. |
| Resmi test | `hypotheses/registry.yaml` dosyasına yeni bir kayıt ekle (GitHub web editörü) → Actions → **Validate hypotheses** → id gir. |
| Haftalık kontrol | Her Cumartesi 07:17 TR: tüm aktif hipotezler yeniden doğrulanır, sonuç commit edilir ve Telegram'a gönderilir. |
| Sonuçları görme | `results/H0xx_*.md` raporları ve `decisions/registry.json`. |

Gerekli secret'lar: `TELEGRAM_TOKEN`, `CHAT_ID` (diğer botlarla aynı).
Settings → Actions → General → Workflow permissions → **Read and write** açık olmalı.

## Karar kapısı (validation.GATE)

Bir hipotezin `ACCEPT` alması için tüm koşullar sağlanmalı:

| Koşul | Eşik | Neden |
|---|---|---|
| Out-of-sample süresi | ≥ 3 yıl | Kısa örnek şans olabilir |
| Deflated Sharpe (olasılık) | ≥ 0.90 | Çok parametre denemesinin şişirdiği Sharpe'ı düzeltir |
| OOS Sharpe | ≥ 0.5 | Minimum ekonomik anlam |
| OOS MaxDD | ≥ -45% | Dayanılabilir kayıp |
| Bootstrap P(Sharpe>0) | ≥ 0.85 | Sonuç tek bir döneme bağlı değil |
| Pozitif yıl oranı | ≥ 55% | Zaman içinde istikrar |
| 2× maliyet ile eşit ağırlıklı benchmark'ı geçme | evet | Getiri maliyete dayanıklı ve beta değil |

`WATCH` = umut verici ama kanıt yetersiz. `REJECT` = kullanma. Eşikleri gevşetmek yasak; değişiklik
nedeniyle `hypotheses/CHANGELOG.md` dosyasına yazılır.

## Strateji kataloğu (`python run.py --list`)

| Ad | Fikir | Kaynak |
|---|---|---|
| `xs_momentum` | Kesitsel 12-1 momentum | Jegadeesh & Titman 1993 |
| `ts_momentum` | Zaman serisi momentum, volatilite hedefli | Moskowitz, Ooi & Pedersen 2012 |
| `ma_cross` | Hareketli ortalama kesişimi | Faber 2007 |
| `st_reversal` | Kısa vadeli dönüş | Lehmann 1990 |
| `low_vol` | Düşük volatilite anomalisi | Ang et al. 2006 |
| `high_52w` | 52 hafta zirvesine yakınlık | George & Hwang 2004 |
| `dual_momentum` | Göreli + mutlak momentum | Antonacci 2014 |
| `turn_of_month` | Ay dönümü etkisi | Ariel 1987 |
| `rsi_reversion` | RSI(2) trend içi dip alımı | Connors 2009 |
| `equal_weight` | 1/N benchmark | DeMiguel et al. 2009 |

Yeni strateji: `lab/strategies/__init__.py` dosyasına `@strategy(...)` ile bir fonksiyon ekle.
Fonksiyon t günü kapanışına kadar olan veriyle hedef ağırlık döndürür; motor ağırlığı t+1'de uygular.

## Evrenler (`config/universes.yaml`)

`bist30`, `bist_index`, `sp_megacap`, `us_sectors`, `global_assets`, `crypto_major`.
Veri: yfinance (BIST `.IS`, ABD), ccxt public uç noktaları (Bitget → OKX → KuCoin). Hepsi ücretsiz.

**Uyarı (survivorship bias):** Evrenler bugünkü üyelerdir. Endeksten çıkan hisseler yoktur, bu yüzden
geçmiş sonuçlar iyimserdir.

## Botlara bağlama

`lab/client.py` dosyasını bot reposuna `quant_lab_client.py` adıyla kopyala:

```python
from quant_lab_client import approved
for h in approved(system="bist_orderflow_quant"):
    targets = h["targets"]   # {"THYAO.IS": 0.2, ...}
```

Kayıt alınamazsa veya 10 günden eskiyse `[]` döner: bot kendi varsayılanına geçer (fail-safe).

## Yerel test

```bash
pip install -r requirements.txt
python tests/test_core.py          # look-ahead, maliyet, sahte edge, DSR testleri
python run.py --synthetic          # internetsiz duman testi
python run.py --hypothesis H001
```

## Dosya yapısı

```
lab/data.py          ücretsiz veri + önbellek
lab/engine.py        vektörel motor (t+1 uygulama, maliyet, borç maliyeti)
lab/metrics.py       Sharpe, Sortino, MaxDD, PSR, DSR
lab/validation.py    sweep, walk-forward, bootstrap, karar kapısı
lab/decision.py      decisions/registry.json yazımı
lab/client.py        botlar için okuyucu
lab/adapters/        vectorbt ve backtesting.py (keşif amaçlı, karar vermez)
```
