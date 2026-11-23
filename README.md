<div align="center">
  <img src="dist/mineral-kapak.webp" alt="Mineral Icon Pack Cover" width="128" height="128">
  <h1>Mineral Icon Pack</h1>
  <p><strong>Polished Malachite with Gold Embossing &amp; Deep Azurite with Silver Embossing — 144 Retina 128×128 PNG Icons for evoX Deck &amp; Stream Deck.</strong></p>

  <p>
    <a href="dist/mineral-icon-pack-1.0.0.evoxpack">
      <img src="https://img.shields.io/badge/Download-.evoxpack%20v1.0.0-1B6B4A?style=for-the-badge&logo=icloud&logoColor=F5E6A8" alt="Download .evoxpack v1.0.0">
    </a>
    <a href="dist/mineral-onizleme.webp">
      <img src="https://img.shields.io/badge/Preview-Full%20Catalog-1D3F73?style=for-the-badge&logo=images&logoColor=E2E8F0" alt="Full Icon Catalog">
    </a>
    <a href="#installation">
      <img src="https://img.shields.io/badge/Guide-Installation-2E4053?style=for-the-badge&logo=readthedocs&logoColor=white" alt="Installation Guide">
    </a>
    <a href="README.tr.md">
      <img src="https://img.shields.io/badge/Language-T%C3%BCrk%C3%A7e-D4AF37?style=for-the-badge&logo=googletranslate&logoColor=101A20" alt="Türkçe README">
    </a>
  </p>

  <p>
    <img src="https://img.shields.io/badge/Total%20Icons-144%20(72%20%C3%97%202)-1B6B4A?style=flat-square" alt="144 Icons">
    <img src="https://img.shields.io/badge/Themes-Malachite%20%26%20Azurite-1D3F73?style=flat-square" alt="Malachite & Azurite">
    <img src="https://img.shields.io/badge/Format-128%C3%97128%20Transparent%20PNG-10B981?style=flat-square" alt="128x128 PNG">
    <img src="https://img.shields.io/badge/Platforms-evoX%20Deck%20%7C%20Stream%20Deck-0078D6?style=flat-square" alt="evoX Deck & Stream Deck">
    <img src="https://img.shields.io/badge/Publisher-Fayth-C9A227?style=flat-square" alt="Publisher Fayth">
    <img src="https://hits.sh/github.com/hfatih/mineral-icon-pack.svg?style=flat-square&label=views&color=1B6B4A" alt="Views">
  </p>
</div>

---

## Visual Showcase

<p align="center">
  <img src="dist/mineral-onizleme.webp" alt="Full catalog of 144 icons in Malachite and Azurite mineral themes" width="100%">
</p>

<details>
  <summary>View 768×768 Market Cover Artwork</summary>
  <p align="center">
    <img src="dist/mineral-kapak.webp" alt="Mineral Icon Pack Market Cover" width="384">
  </p>
</details>

---

## Mineral Themes

Crafted by **Fayth** for **evoX Deck** and **Stream Deck**, the pack renders **72 original vector control glyphs** at 3× supersampling (`384×384` downsampled to crisp `128×128` transparent PNGs) across two natural stone finishes:

| Theme | Stone Surface | Embossed Metal | Filename Prefix | Icons |
| :--- | :--- | :--- | :--- | ---: |
| **Malachite** | Banded polished emerald-malachite | Warm brushed gold relief | `malakit-` | 72 |
| **Azurite** | Deep sapphire-azurite mineral | Cool polished silver relief | `azurit-` | 72 |

---

## Icon Categories

| Category | Included Controls | Per Theme | Total |
| :--- | :--- | ---: | ---: |
| **Streaming** | Go live, record, camera, screen share, scene transition, overlays | 12 | 24 |
| **Audio** | Microphone, mute, headphones, mixer, audio output, volume | 12 | 24 |
| **Media** | Play, pause, next track, repeat, shuffle, playback controls | 12 | 24 |
| **Workflow** | Folder, browser, terminal, screenshot, copy, productivity actions | 12 | 24 |
| **System** | Power, lock screen, Wi-Fi, brightness, do not disturb, settings | 12 | 24 |
| **Shortcuts** | Directional arrows, confirm, cancel, search, app launcher | 12 | 24 |
| **Total** | **72 unique glyphs across 2 gemstone finishes** | **72** | **144** |

---

## Installation

### Method 1: evoX Deck (`.evoxpack` — Recommended)

1. Download [`mineral-icon-pack-1.0.0.evoxpack`](dist/mineral-icon-pack-1.0.0.evoxpack).
2. Open the **evoX** desktop app and navigate to **Market → Import** to load the pack in one click.
3. Select any deck key and pick an icon from your library — filenames start with `malakit-` or `azurit-` for instant theme filtering.

### Method 2: Manual PNG Import (evoX Deck / Elgato Stream Deck)

1. Extract the PNGs from `assets/icons/` inside `mineral-icon-pack-1.0.0.evoxpack` (standard ZIP archive).
2. In **evoX Deck**, go to **Icons → Add** and select the extracted PNGs; or in **Elgato Stream Deck**, choose **Set from File** on any key.

> [!TIP]
> Official evoX documentation: [Installing a Downloaded Pack](https://docs.evox.wraithesports.app/application/market-plugins#webden-indirilen-paketi-kurma) · [Icon Library](https://docs.evox.wraithesports.app/application/icons-sounds) · [Publishing Guide](https://docs.evox.wraithesports.app/application/publish-your-pack)

---

## evoX Market Metadata

<details>
  <summary>Show package submission fields for evoX Web Market</summary>

| Field | Value |
| :--- | :--- |
| **Pack Name** | Mineral Icon Pack |
| **Publisher** | Fayth |
| **Version** | `1.0.0` |
| **Description** | Polished malachite and azurite tiles with embossed metallic glyphs. 72 original icons for streaming, audio, media, workflow, system, and shortcuts — 144 icons across two themes. |
| **Package** | [`dist/mineral-icon-pack-1.0.0.evoxpack`](dist/mineral-icon-pack-1.0.0.evoxpack) |
| **Cover** | [`dist/mineral-kapak.webp`](dist/mineral-kapak.webp) (`768 × 768 px`) |

</details>

---

## Rebuilding From Source

Every icon, stone texture, metallic bevel, cover, and catalog preview is generated procedurally from Python.

**Requirements:** Python 3.11+, Cairo, and DejaVu Sans/Serif fonts (set `MINERAL_FONT_DIR` if your fonts live outside `/usr/share/fonts/truetype/dejavu`).

```bash
python -m pip install -r requirements.txt
python build.py
python validate.py
```

```text
mineral-icon-pack/
├── glyphs.py          # 72 SVG vector glyph definitions grouped by category
├── materials.py       # Procedural malachite & azurite stone shaders + metallic relief
├── build.py           # 3× supersampled renderer, .evoxpack packager & preview generator
├── validate.py        # Archive integrity, manifest paths, 144 PNGs & cover validator
├── requirements.txt   # Python dependencies
└── dist/
    ├── mineral-icon-pack-1.0.0.evoxpack
    ├── mineral-kapak.webp
    └── mineral-onizleme.webp
```

## License

Project-owned code and original material in this revision are licensed under [GNU GPL v3.0](LICENSE) (GPL-3.0-only). Third-party code, fonts, imagery, data, and brand assets retain their own terms and attributions.
