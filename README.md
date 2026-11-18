# Mineral Icon Pack

**Fayth · evoX Deck · v1.0.0**

Cilalı malakit üzerinde altın ve azurit üzerinde gümüş kabartma. Fayth’in evoX Deck için hazırladığı set, 72 özgün kontrol simgesini iki taş temasında sunuyor. Toplam **144 şeffaf PNG** ikonun her biri **128 × 128 piksel**.

**[Paketi indir](dist/mineral-icon-pack-1.0.0.evoxpack)** · [Tam boy ikon kataloğu](dist/mineral-onizleme.webp) · [Market kapağı](dist/mineral-kapak.webp)

![Malakit ve azurit temalarında 144 ikonun kataloğu](dist/mineral-onizleme.webp)

## İkonlar

| Grup | Örnekler | Her temada |
| --- | --- | ---: |
| Yayın | Canlı yayın, kayıt, kamera, ekran paylaşımı, sahne geçişi | 12 |
| Ses | Mikrofon, sessize alma, kulaklık, mikser, ses çıkışı | 12 |
| Medya | Oynat, duraklat, sonraki parça, tekrar, karışık çal | 12 |
| Çalışma | Klasör, tarayıcı, terminal, ekran görüntüsü, kopyala | 12 |
| Sistem | Güç, ekran kilidi, Wi-Fi, parlaklık, rahatsız etme | 12 |
| Kısayol | Yönler, onayla, iptal, ara, uygulamalar | 12 |

## evoX Deck’e ekleme

1. `mineral-icon-pack-1.0.0.evoxpack` dosyasını indir.
2. evoX masaüstünde **Market → İçe aktar** üzerinden paketi seç. Tek tek ikon eklemek için arşivdeki `assets/icons/` klasöründen istediğin PNG’leri çıkar ve **İkonlar → Ekle** üzerinden seç.
3. Bir tuş seçip ikon kütüphanesinden istediğin simgeyi ata. Dosya adları `malakit-` ve `azurit-` önekleriyle temayı gösterir.

[Paket içe aktarma](https://docs.evox.wraithesports.app/application/market-plugins#webden-indirilen-paketi-kurma) · [İkon kütüphanesi](https://docs.evox.wraithesports.app/application/icons-sounds)

## evoX Market gönderimi

| Alan | İçerik |
| --- | --- |
| Paket adı | Mineral Icon Pack |
| Yayıncı adı | Fayth |
| Sürüm | 1.0.0 |
| Açıklama | Cilalı malakit ve azurit üzerinde kabartma metal simgeler. Yayın, ses, medya, çalışma, sistem ve kısayollar için 72 özgün simge, iki temada 144 ikon. |
| Paket | [`mineral-icon-pack-1.0.0.evoxpack`](dist/mineral-icon-pack-1.0.0.evoxpack) |
| Kapak | [`mineral-kapak.webp`](dist/mineral-kapak.webp), 768 × 768 piksel |

Web Market’te **Yayınla** sayfasından `.evoxpack` dosyasını ve kapağı seç. Önce **Yükle ve tara**, ardından taslak hazır olduğunda **Moderasyona gönder** adımını kullan. [evoX yayınlama kılavuzu](https://docs.evox.wraithesports.app/application/publish-your-pack)

## Paketi yeniden üretme

Python 3.11+, Cairo ve DejaVu Sans/Serif yazı tipleri gerekir. Yazı tipleri farklı bir klasördeyse `MINERAL_FONT_DIR` ile belirt.

```sh
python -m pip install -r requirements.txt
python build.py
python validate.py
```

`glyphs.py` simgeleri, `materials.py` taş dokularını ve kabartmayı tanımlar. `build.py` paketi, kapağı ve kataloğu `dist/` altında üretir. `validate.py` arşiv bütünlüğünü, manifestteki dosya yollarını, 144 PNG’yi ve kapağı kontrol eder.
