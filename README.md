# quant_lab — Strateji Laboratuvarı ve Karar Merkezi

Bu repo tüm al-sat botlarının **nihai karar merkezidir**. Bir bot bir stratejiyi ancak bu repoda
doğrulanmış ve `ACCEPT` kararı almışsa kullanır. LLM yok, ücretli API yok. Her şey GitHub Actions'ta çalışır.

## Kapsam (`python run.py --list`)

| Katman | İçerik |
|---|---|
| İndikatör kütüphanesi | 60+ fonksiyon: SMA/EMA/WMA/HMA/DEMA/TEMA/KAMA, RSI, Stoch, StochRSI, Williams %R, CCI, MFI, ROC, MACD, PPO, TRIX, TSI, Awesome, Ultimate, Coppock, DMI/ADX, Aroon, Vortex, WaveTrend, Supertrend, Parabolic SAR, Ichimoku, Heikin-Ashi, Bollinger, Keltner, Donchian, ATR, Choppiness, Z-score, Hurst, OBV, CMF, A/D, Chaikin, Force, VWAP, EOM, mum formasyonları |
| Giriş/çıkış kuralları | **53 kural, 518 parametre varyantı** (ör. RSI 2/3/5/7/9/14/21/28 × seviye 10/20/25/30/35 × çıkış 50/60/70). Long, short veya ikisi birden |
| Filtreler | trend (SMA 50/100/200), ADX 20/25, piyasa rejimi (endeks > SMA200), düşük volatilite, hacim onayı, temel kalite (ROE), temel değer (E/P) |
| Çıkış yönetimi | 17 çıkış ayarı: ATR veya % stop, ATR / % / R-katı hedef, ATR veya % trailing stop, zaman stopu, sinyal çıkışı |
| Ağırlık stratejileri | **41 strateji**: momentum (kesitsel, zaman serisi, residual, frog-in-pan, ivme, vol-yönetimli, trend kalitesi), düşük vol, idiosenkratik vol, MAX etkisi, BAB, mevsimsellik, ay dönümü, RSI rotasyonu, hacim şoku |
| Temel analiz faktörleri | E/P, B/P, S/P, CF/P, EBIT/EV, ROE, ROA, brüt kârlılık, accruals, varlık büyümesi, kaldıraç, net hisse ihracı, gelir/kâr büyümesi, küçük şirket, Piotroski F-skor, Magic Formula, QVM kompozit, değer+momentum, kalite+düşük vol |
| Veri (ücretsiz) | Fiyat: yfinance (BIST `.IS`, ABD), ccxt (Bitget → OKX → KuCoin). Temel: **İş Yatırım** (BIST, TTM, yayın gecikmeli) ve **SEC EDGAR** (ABD, gerçek dosyalama tarihi, ilk açıklanan değer) |
| Keşif motorları | `lab/adapters/vbt_adapter.py` (vectorbt ısı haritası), `lab/adapters/bt_adapter.py` (backtesting.py, bar içi stop/TP) |

## Karar akışı

```
Fikir → Discovery scan (her şeyi dener, dürüst sıralar) → hipotez (hypotheses/registry.yaml)
      → Karar kapısı (walk-forward + DSR + PBO + bootstrap + 2× maliyet + rejim + işlem sayısı)
      → decisions/registry.json (ACCEPT / WATCH / REJECT + hedef pozisyonlar / sinyaller)
      → Botlar lab/client.py ile okur, sadece ACCEPT'e göre işlem yapar
```

## Telefondan kullanım (GitHub → Actions)

| Workflow | Ne zaman | Ne yapar |
|---|---|---|
| **Discovery scan** | Her ayın 1'i + elle | Her evrende tüm kuralları × varyantları × filtreleri ve tüm stratejileri dener. `results/scan_*.md` liderlik tablosu ve önerilen hipotez YAML'ı üretir. Karar yazmaz. |
| **Validate hypotheses** | Her Cumartesi + elle (id ile) | Aktif hipotezleri karar kapısından geçirir, `decisions/registry.json` dosyasını günceller, Telegram'a özet gönderir. |
| **Ad-hoc backtest** | Elle | `strategy`, `rule`, `scan`, `vbt`, `bt` modları. Sonuç Telegram + artifact. Karar yazmaz. |

Secrets: `TELEGRAM_TOKEN`, `CHAT_ID` (diğer botlarla aynı), isteğe bağlı `SEC_USER_AGENT` (ör. `ad soyad eposta`; SEC iletişim bilgisi ister).
Settings → Actions → General → Workflow permissions → **Read and write permissions** seçili olmalı.

## Hipotez ekleme (GitHub web editöründe `hypotheses/registry.yaml`)

```yaml
- id: H030                     # asla tekrar kullanılmaz
  rule: wavetrend_reversal     # veya  strategy: qvm_composite
  universe: bist30
  for_system: bist_orderflow_quant
  start: "2012-01-01"
  filters: [none, trend_sma200, regime_bench200]   # veya all
  exits: all                   # veya [0, 1, 5]; boş = kademeli arama (tüm çıkışlar en iyi 3 varyanta)
  side: long                   # long | short | both
  status: active
  note: "neden test ediyoruz"
```

## Karar kapısı (`lab/validation.py` → `GATE`)

| Koşul | Eşik | Neden |
|---|---|---|
| OOS süresi | ≥ 3 yıl | Kısa örnek şans olabilir |
| Deflated Sharpe | ≥ 0.90 | Denenen **tüm** varyantların şişirdiği Sharpe'ı düzeltir |
| PBO (CSCV) | ≤ 0.50 | "En iyi backtesti seç" adımının kendisi aşırı uyum mu? |
| OOS Sharpe | ≥ 0.5 | Ekonomik anlam |
| OOS MaxDD | ≥ -45% | Dayanılabilir kayıp |
| Bootstrap P(Sharpe>0) | ≥ 0.85 | Tek döneme bağlı değil |
| Pozitif yıl oranı | ≥ 55% | Zamanda istikrar |
| 2× maliyetle eşit ağırlıklı benchmark'ı geçme | evet | Maliyete dayanıklı, beta değil |
| OOS işlem sayısı (kurallar) | ≥ 30 | İstatistiksel anlam |

`WATCH` = umut verici ama kanıt yetersiz, `REJECT` = kullanma. Eşikler gevşetilmez; her değişiklik
`hypotheses/CHANGELOG.md` dosyasına nedeniyle yazılır.

## Yürütme modeli (look-ahead yok)

- Ağırlık stratejileri: sinyal t kapanışı → pozisyon t+1. Maliyet = devir × (komisyon + slipaj).
- Kurallar: sinyal t kapanışı → işlem t+1 **açılışı**. Gün içinde stop ve hedef high/low ile kontrol edilir; ikisi aynı barda olursa stop kabul edilir (muhafazakâr). Boşlukta dolum açılış fiyatıdır.
- Temel veri: rapor sadece yayın tarihinden sonra görünür (BIST: dönem sonu + 75/100 gün; ABD: gerçek SEC dosyalama tarihi, sonraki düzeltmeler geçmişe sızmaz).
- Walk-forward: her varyant bir kez hesaplanır (nedensel), her eğitim penceresinde en iyi varyant seçilir, sonraki test penceresinde işlem yapılır.

## Botlara bağlama

`lab/client.py` dosyasını bot reposuna `quant_lab_client.py` adıyla kopyala:

```python
from quant_lab_client import approved
for h in approved(system="bist_orderflow_quant"):
    print(h["id"], h["kind"], h["targets"])
    # strategy: {"THYAO.IS": 0.2, ...}
    # rule:     {"positions": {...}, "entry_long_next_open": [...], "exit_long_next_open": [...]}
```

Kayıt alınamazsa veya 10 günden eskiyse `[]` döner; bot kendi varsayılanına geçer (fail-safe).

## Bilinen sınırlar

- **Survivorship bias:** Evrenler bugünkü üyelerdir. Geçmiş sonuçlar iyimserdir.
- Günlük bar. Ücretsiz gün içi veri kısa geçmişlidir (yfinance 15 dk ≈ 60 gün).
- ABD akış kalemleri (kâr, satış, CFO) yıllık 10-K'dan gelir. Bilanço kalemleri çeyrekliktir.
- Kripto açığa satışta funding maliyeti modellenmez (`Costs.borrow_annual` ile eklenebilir).

## Yerel test

```bash
pip install -r requirements.txt
python tests/test_core.py        # 12 test: look-ahead, dolum/stop, maliyet, gürültü reddi, edge bulma, DSR, PBO, temel veri zamanlaması
python run.py --synthetic --rule rsi_reversal
python run.py --scan --synthetic
```

## Dosya yapısı

```
lab/indicators.py        teknik indikatörler
lab/rules.py             giriş/çıkış kuralları + filtreler
lab/trade_engine.py      işlem motoru (stop, hedef, trailing, zaman, işlem kaydı)
lab/engine.py            ağırlık motoru
lab/strategies/          ağırlık stratejileri (fiyat ve temel faktörler)
lab/fundamentals.py      İş Yatırım + SEC EDGAR, zaman-noktası paneller
lab/candidates.py        varyant üretimi + paralel çalıştırma
lab/validation.py        karar kapısı
lab/scanner.py           keşif taraması
lab/metrics.py           Sharpe, Sortino, MaxDD, PSR, DSR, PBO, rejim analizi
lab/decision.py          decisions/registry.json
lab/client.py            botlar için okuyucu
```
