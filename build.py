"""Build Fayth's Mineral Icon Pack and its two preview images."""

from io import BytesIO
import json
import os
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

from PIL import Image, ImageDraw, ImageFont

from glyphs import GROUPS
from materials import FINISHES, relief, stone

ROOT = Path(__file__).resolve().parent
DIST = ROOT / "dist"
FONT_DIR = Path(os.environ.get("MINERAL_FONT_DIR", "/usr/share/fonts/truetype/dejavu"))
VERSION = "1.0.0"
DATE = (2026, 11, 18, 0, 0, 0)
SIZE = 128
RENDER_SIZE = SIZE * 3
PACK = "Mineral Icon Pack"
COVER_PATH = "preview/cover.png"
EMBLEM = """
<path d="M12 2.8 21 9l-3.4 9.1L12 22l-5.6-3.9L3 9z"/>
<path d="m3 9 9 2.5L21 9M12 2.8v8.7L6.4 18.1M12 11.5l5.6 6.6m-5.6-6.6V22"/>
"""
DESCRIPTION = (
    "Cilalı malakit ve azurit üzerinde kabartma metal simgeler. "
    "Yayın, ses, medya, çalışma, sistem ve kısayollar için 72 özgün simge, iki temada 144 ikon."
)


def png_bytes(image):
    buffer = BytesIO()
    image.save(buffer, format="PNG", optimize=True)
    return buffer.getvalue()


def font(size, filename="DejaVuSans.ttf"):
    return ImageFont.truetype(str(FONT_DIR / filename), size)


def catalog(art):
    image = Image.new("RGBA", (2496, 1552), "#101A20")
    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle((26, 26, 2469, 1525), radius=34, outline="#30454E", width=2)
    draw.text((76, 63), "Mineral Icon Pack", font=font(94, "DejaVuSerif.ttf"), fill="#F5F4EA", anchor="lt")
    draw.text((80, 174), "FAYTH   /   144 İKON   /   128 × 128 PNG",
              font=font(29, "DejaVuSansMono.ttf"), fill="#BBD0CC", anchor="lt")

    slots = list(FINISHES.items())
    for column, (_, finish) in enumerate(slots):
        left = 72 + column * 1200
        draw.rounded_rectangle((left, 258, left + 1152, 1482), radius=28,
                               fill="#17242C", outline="#3B525B", width=2)
        draw.text((left + 31, 286), finish.name, font=font(44, "DejaVuSerif.ttf"),
                  fill=finish.edge, anchor="lt")
        for index, shade in enumerate(finish.stone[1:]):
            x = left + 939 + index * 38
            draw.ellipse((x, 299, x + 22, 321), fill=shade, outline="#88A1A9")

    for row, (group_key, (label, entries)) in enumerate(GROUPS.items()):
        y = 369 + row * 183
        for column, (finish_key, _) in enumerate(slots):
            left = 72 + column * 1200
            draw.line((left + 28, y, left + 1124, y), fill="#334650")
            draw.text((left + 30, y + 16), label, font=font(24, "DejaVuSans-Bold.ttf"),
                      fill="#E0EBEC", anchor="lt")
            for number, (slug, name, _) in enumerate(entries):
                x = left + 20 + number * 93
                icon = art[finish_key, group_key, slug].resize((82, 82), Image.Resampling.LANCZOS)
                image.alpha_composite(icon, (x + 5, y + 53))
                face = font(12)
                box = 91
                if draw.textlength(name, font=face) > box and " " in name:
                    first, last = name.rsplit(" ", 1)
                    name = f"{first}\n{last}"
                draw.multiline_text((x + 46, y + 143), name, font=face, fill="#BBD0CC",
                                    anchor="ma", align="center", spacing=4)
    return image.convert("RGB")


def write_member(archive, name, payload):
    member = ZipInfo(name, date_time=DATE)
    member.compress_type = ZIP_DEFLATED
    member.create_system = 3
    member.external_attr = 0o100644 << 16
    archive.writestr(member, payload, compresslevel=6)


def build():
    DIST.mkdir(exist_ok=True)
    assets = []
    art = {}
    for finish_key, finish in FINISHES.items():
        tile = stone(RENDER_SIZE, finish)
        for group_key, (group_name, entries) in GROUPS.items():
            for slug, name, markup in entries:
                identifier = f"{finish_key}-{group_key}-{slug}"
                art[finish_key, group_key, slug] = relief(tile, finish, markup).resize(
                    (SIZE, SIZE), Image.Resampling.LANCZOS
                )
                assets.append({
                    "id": f"icons-mineral-{identifier}",
                    "path": f"assets/icons/{identifier}.png",
                    "name": f"{finish.name} · {group_name} · {name}",
                })

    finish = FINISHES["malakit"]
    cover = relief(stone(768, finish), finish, EMBLEM, fraction=0.72)
    cover.save(DIST / "mineral-kapak.webp", format="WEBP", quality=94, method=6)
    catalog(art).save(DIST / "mineral-onizleme.webp", format="WEBP", quality=94, method=6)
    embedded_cover = cover.resize((480, 480), Image.Resampling.LANCZOS)
    manifest = {
        "schemaVersion": 1,
        "packageType": "icon_pack",
        "name": PACK,
        "description": DESCRIPTION,
        "version": VERSION,
        "author": {"id": "desktop-local-user", "name": "Fayth"},
        "requiredActions": [],
        "requiredIntegrations": [],
        "assets": {"icons": assets, "sounds": []},
        "createdWith": "evox-deck-v2",
        "createdAt": "2026-11-18T00:00:00.000Z",
        "coverImage": COVER_PATH,
    }
    with ZipFile(DIST / f"mineral-icon-pack-{VERSION}.evoxpack", "w") as archive:
        write_member(archive, "manifest.json", (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))
        for asset, icon in zip(assets, art.values(), strict=True):
            write_member(archive, asset["path"], png_bytes(icon))
        write_member(archive, COVER_PATH, png_bytes(embedded_cover))


if __name__ == "__main__":
    build()
