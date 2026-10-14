# quant_lab — Strateji Laboratuvarı ve Karar Merkezi

Bu repo tüm al-sat botlarının **nihai karar merkezidir**. Bir bot bir stratejiyi ancak burada doğrulanmış ve
`ACCEPT` almışsa kullanır. LLM yok, ücretli API yok. Her şey GitHub Actions'ta çalışır.

## Akış

```
Fikir → Discovery scan (her şeyi dener, dürüst sıralar)
      → Hipotez (hypotheses/registry.yaml)
      → Karar kapısı: walk-forward + DSR + PBO + Reality Check + gecikme + rastgele giriş + parametre komşuluğu + ...
      → decisions/registry.json (ACCEPT / WATCH / REJECT / DEGRADED + hedefler + bot başına HRP sermaye dağılımı)
      → Canlı (paper) takip: bozulan strateji otomatik DEGRADED olur
      → Botlar lab/client.py ile okur, sadece ACCEPT'e göre işlem yapar
```

## Kapsam (`python run.py --list`)

| Katman | İçerik |
|---|---|
| **Zaman dilimleri** | `1h`, `4h`, `1d`, `1w`, `1mo`. Haftalık/aylık barlar günlükten üretilir. Hisse 1h verisi ~2 yıl (Yahoo sınırı), kripto 1h/4h uzun geçmiş. Bütün metrikler bar/yıl ölçülerek yıllıklandırılır |
| **Çoklu zaman dilimi** | Üst zaman dilimi trend filtreleri (`htf_week_sma10/30`, `htf_month_sma10`), sadece **tamamlanmış** üst barlarla |
| **İndikatörler** | 60+: 7 hareketli ortalama tipi, RSI, Stoch, StochRSI, %R, CCI, MFI, ROC, MACD, PPO, TRIX, TSI, AO, UO, Coppock, DMI/ADX, Aroon, Vortex, WaveTrend, Supertrend, PSAR, Ichimoku, Heikin-Ashi, Bollinger, Keltner, Donchian, ATR, Choppiness, Z-skor, Hurst, OBV, CMF, A/D, Chaikin, Force, VWAP, EOM, mum formasyonları |
| **Giriş kuralları** | 53 kural / **518 parametre varyantı** (ör. RSI 2,3,5,7,9,14,21,28 × seviye × çıkış). Long, short, ikisi |
| **Filtreler (19)** | Trend SMA50/100/200, ADX, endeks rejimi, düşük vol, hacim, temel kalite/değer, üst zaman dilimi trendi, VIX, VIX-spike, USDTRY stresi, faiz eğrisi, endeks üyeliği |
| **Stop-loss** | ATR (1.5/2/3), yüzde (3/5/8/12), swing-low (5/10/20 bar), breakeven, ATR/yüzde trailing (chandelier), MA trailing, zaman stopu |
| **Kâr alma** | ATR hedef, yüzde hedef, R-katı (1.5/2/3), **kısmi kâr alma** (1R/2R'de %50 + kalan trailing + stop başabaş), sabit tutma süresi |
| **44 çıkış ayarı** | Yukarıdakilerin seçilmiş kombinasyonları (`run.py --list`) |
| **Pozisyon boyutu** | Eşit, ATR-risk (%0.5/%1/%2 risk), pozisyon başı vol hedefi; brüt kaldıraç sınırı; Kelly oranı raporu |
| **Ağırlık stratejileri (47)** | Momentum (kesitsel, zaman serisi, residual, frog-in-pan, ivme, vol-yönetimli, trend kalitesi), düşük vol, idiosenkratik vol, MAX, BAB, mevsimsellik, ay dönümü, RSI rotasyonu, hacim şoku, **pairs trading**, **walk-forward ML (ridge)**, **bilanço sonrası drift**, **makro risk anahtarı**, breadth, USDTRY korunma |
| **Temel faktörler (21)** | E/P, B/P, S/P, CF/P, EBIT/EV, ROE, ROA, brüt kârlılık, accruals, varlık büyümesi, kaldıraç, net hisse ihracı, büyüme, küçük şirket, Piotroski F, Magic Formula, QVM, değer+momentum, kalite+düşük vol |
| **Veri (ücretsiz)** | yfinance, ccxt (Bitget/OKX/KuCoin), İş Yatırım (BIST bilanço, TTM, yayın gecikmeli), SEC EDGAR (ABD, gerçek dosyalama tarihi), makro (^VIX, ^TNX, ^IRX, USDTRY=X), S&P 500 geçmiş üyelik |

## Karar kapısı (`lab/validation.py` → `GATE`)

| Kontrol | Eşik | Neden |
|---|---|---|
| OOS süresi | ≥ 3 yıl | Kısa örnek şans olabilir |
| Deflated Sharpe | ≥ 0.90 | Denenen **tüm** varyantların şişirdiği Sharpe'ı düzeltir |
| PBO (CSCV) | ≤ 0.50 | "En iyi backtesti seçme" adımı aşırı uyum mu? |
| White Reality Check p | ≤ 0.10 | En iyi sonuç veri madenciliği mi? |
| OOS Sharpe | ≥ 0.5 | **Risksiz faizin üstünde** ölçülür; TL piyasada **USD'ye çevrilerek** ölçülür |
| OOS MaxDD | ≥ -45% | Dayanılabilir kayıp |
| Bootstrap P(Sharpe>0) | ≥ 0.85 | Tek döneme bağlı değil |
| Pozitif yıl oranı | ≥ 55% | Zamanda istikrar |
| 2× maliyet | eşit ağırlıklı benchmark'ı geçmeli | Maliyete dayanıklı, beta değil |
| İşlem sayısı (kurallar) | ≥ 30 | İstatistik anlam |
| 1 bar gecikme | Sharpe'ın ≥ %40'ı kalmalı | Gecikmeye dayanıklı |
| Rastgele giriş testi | p ≤ 0.10 | Kâr çıkışlardan değil sinyalden gelmeli (işlem sayısı ve maruziyet eşlenir) |
| Parametre komşuluğu | komşuların ≥ %50'si kârlı | Tepe değil plato |

Raporda ayrıca: gürültü testi, Monte Carlo işlem karıştırma, walk-forward verimliliği, rejim analizi (boğa/ayı,
sakin/stresli, VIX bantları, faiz eğrisi), haftanın günü / ay / saat profili, VaR/CVaR, Ulcer, Omega, tail ratio,
up/down capture, aylık getiri ısı haritası ve grafikler.

## Zamanlama ve kâr maksimizasyonu çalışmaları (her rapor)

- **Event study:** Sinyalden sonra 1, 2, 3, 5, 10, 15, 20, 40, 60 bar ileri getiri, isabet oranı ve t-istatistiği. En iyi tutma süresini verir.
- **Stop × hedef × süre ızgarası:** Gerçek high/low yollarıyla stop %2–12, hedef %3–25, süre 3–40 bar. Isı haritası olarak verilir.
- **Portföy katmanları:** Vol hedefleme, drawdown freni, equity-curve filtresi. Calmar oranına göre en iyisi önerilir.
- **MFE/MAE:** Her işlemde en iyi ve en kötü fiyat hareketi, edge ratio, R-katı, SQN, Kelly.

Bunlar örneklem içi teşhislerdir. Daha iyi bir çıkış bulunursa hipoteze `exits: [...]` olarak eklenir ve kapıdan geçmesi beklenir.

## Gerçekçilik

- Sinyal t kapanışında, işlem t+1 açılışında. Gün içi stop ve hedef high/low ile kontrol edilir; ikisi aynı barda olursa stop sayılır. Boşlukta dolum açılış fiyatıdır.
- BIST ±%10 tavan/taban: kilitli açılışta emir dolmaz, bir sonraki bara bekler.
- Likidite: `min_adv` altındaki hissede pozisyon açılmaz.
- Maliyet: komisyon + slipaj, açığa satış borç maliyeti, kripto funding.
- Temel veri yayın tarihinden önce görünmez. SEC'de ilk açıklanan değer kullanılır (sonradan yapılan düzeltme geçmişe sızmaz).
- Intraday barlarda günlük makro veri bir gün sonra görünür.
- S&P evrenlerinde geçmiş üyelik maskesi uygulanır (survivorship kontrolü).

## Telefondan kullanım (GitHub → Actions)

| Workflow | Ne zaman | Ne yapar |
|---|---|---|
| **Discovery scan** | Her ayın 1'i + elle | Evren × zaman dilimi matrisi. Tüm kuralları, varyantları ve stratejileri dener. `results/scan_*.md` + önerilen YAML |
| **Validate hypotheses** | Cumartesi + elle (id veya id listesi) | Her hipotez **paralel** bir işte doğrulanır. Sonra kayıt birleştirilir, commit edilir, Telegram'a gönderilir |
| **Live tracking** | Hafta içi 21:47 | ACCEPT stratejileri dondurulmuş varyantla paper takip edilir. Bozulma olursa DEGRADED yapılır |
| **Ad-hoc backtest** | Elle | `strategy`, `rule`, `scan`, `vbt`, `bt` modları; zaman dilimi seçilir. Karar yazmaz |

Secrets: `TELEGRAM_TOKEN`, `CHAT_ID`. İsteğe bağlı: `SEC_USER_AGENT` ("ad eposta").
Settings → Actions → General → Workflow permissions → **Read and write**.

## Hipotez ekleme (`hypotheses/registry.yaml`)

```yaml
- id: H040                      # asla tekrar kullanılmaz
  rule: wavetrend_reversal      # veya  strategy: qvm_composite
  universe: bist30
  timeframe: 4h                 # 1h | 4h | 1d | 1w | 1mo
  for_system: bist_orderflow_quant
  start: "2012-01-01"
  filters: [none, trend_sma200, htf_week_sma10]   # veya all
  exits: all                    # veya [0, 18, 22]; boş = kademeli arama (tüm çıkışlar en iyi 3 varyanta)
  sizes: all                    # pozisyon boyutu modları (kademe 3)
  side: long                    # long | short | both
  max_positions: 10
  status: active
  note: "neden test ediyoruz"
```

## Botlara bağlama

`lab/client.py` dosyasını bot reposuna `quant_lab_client.py` adıyla kopyala:

```python
from quant_lab_client import approved, allocation
for h in approved(system="bist_orderflow_quant"):
    print(h["id"], h["timeframe"], h["targets"])
print(allocation("bist_orderflow_quant"))   # {"H001": 0.6, "H013": 0.4}
```

Kayıt alınamazsa veya 10 günden eskiyse boş döner; bot kendi varsayılanına geçer (fail-safe).

## Bilinen sınırlar (dürüst liste)

- BIST için ücretsiz geçmiş endeks üyeliği yok. Survivorship bias BIST'te kalır. ABD'de maske var ama borsadan çıkmış şirketlerin fiyatı ücretsiz kaynaklarda yok.
- Hisse 1h verisi ~2 yıl. Intraday hisse sonuçları bu yüzden kısa OOS ile sınırlı; kapı ACCEPT vermez, WATCH verebilir.
- ABD akış kalemleri yıllık 10-K'dan gelir. BIST bilanço yayın tarihi tahmini bir gecikmeyle (75/100 gün) modellenir. Bu yüzden bilanço sonrası drift bir yaklaşıktır.
- Kripto funding sabit yıllık oranla yaklaşıklanır (gerçek funding değişkendir).
- Emir defteri, kısmi dolum ve piyasa etkisi modellenmez. Slipaj sabit orandır.

## Yerel test

```bash
pip install -r requirements.txt
python tests/test_core.py      # 22 test
python run.py --synthetic --rule rsi_reversal
python run.py --scan --synthetic
```

## Dosya yapısı

```
lab/data.py            veri (çoklu zaman dilimi, makro, risksiz faiz, kur, önbellek)
lab/panel.py           Panel (OHLCV + temel + makro + üyelik + bar/yıl)
lab/indicators.py      teknik indikatörler
lab/rules.py           giriş/çıkış kuralları + 19 filtre (çoklu zaman dilimi, makro)
lab/trade_engine.py    işlem motoru: stop/hedef/kısmi/breakeven/trailing/MA/zaman, boyutlandırma, limitler, MFE/MAE
lab/engine.py          ağırlık motoru (maliyet, borç, funding, üyelik)
lab/strategies/        ağırlık stratejileri: fiyat, temel, gelişmiş (pairs, ML, drift, makro)
lab/fundamentals.py    İş Yatırım + SEC EDGAR
lab/membership.py      geçmiş endeks üyeliği
lab/candidates.py      varyant üretimi (kademe 1-3) + paralel çalıştırma
lab/validation.py      karar kapısı
lab/robustness.py      sağlamlık + zamanlama + kâr maksimizasyonu çalışmaları
lab/scanner.py         keşif taraması (+ Reality Check)
lab/metrics.py         performans, risk, anlamlılık (PSR, DSR, PBO, Reality Check)
lab/charts.py          grafikler
lab/decision.py        karar kaydı + HRP dağılımı
lab/live.py            canlı takip + bozulma tespiti
lab/client.py          botlar için okuyucu
```
