# Mineral Icon Pack

Fayth’in evoX Deck için hazırladığı **144 ikonluk** koleksiyon. Cilalı malakit üzerinde altın ve azurit üzerinde gümüş kabartmayla işlenen 72 özgün simge, iki temada sunuluyor. Yayın, ses, medya, çalışma, sistem ve kısayol gruplarındaki ikonlar 128 × 128 şeffaf PNG.

![Malakit ve azurit ikonlarının önizlemesi](dist/mineral-onizleme.webp)

## Dosyalar

- [evoX paketi](dist/mineral-icon-pack-1.0.0.evoxpack)
- [Market kapağı](dist/mineral-kapak.webp)
- [İkon kataloğu](dist/mineral-onizleme.webp)

Paketi evoX masaüstündeki **Market → İçe aktar** üzerinden seçebilirsin. İkonları tek tek kullanmak için arşivin `assets/icons/` klasöründeki PNG’leri **İkonlar → Ekle** üzerinden seç. Market gönderiminde WEBP kapağı ayrı yükleme alanına eklenebilir. [İkon kütüphanesi](https://docs.evox.wraithesports.app/application/icons-sounds) · [Yayınlama kılavuzu](https://docs.evox.wraithesports.app/application/publish-your-pack)

## Yeniden üretme

Python 3.11+, Cairo ve DejaVu Sans/Serif yazı tipleri gerekir. Yazı tipleri farklı bir klasördeyse `MINERAL_FONT_DIR` ile belirt.

```sh
python -m pip install -r requirements.txt
python build.py
python validate.py
```

`glyphs.py` simgeleri, `materials.py` taş dokularını ve kabartmayı tanımlar. Yapı betiği Market arşivine yalnız manifesti ve PNG görselleri ekler. Paket doğrulaması arşiv bütünlüğünü, dosya yollarını, PNG’leri ve kapak boyutunu kontrol eder.
