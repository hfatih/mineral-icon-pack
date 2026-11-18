"""Check the archive, manifest references, PNG contents, and Market cover."""

from collections import Counter
import hashlib
from io import BytesIO
import json
from pathlib import Path
import re
from zipfile import ZipFile

from PIL import Image

DIST = Path(__file__).resolve().parent / "dist"
PACK = DIST / "mineral-icon-pack-1.0.0.evoxpack"


def check_image(data, expected_size):
    with Image.open(BytesIO(data)) as image:
        assert image.format == "PNG", image.format
        assert image.mode == "RGBA", image.mode
        assert image.size == expected_size, image.size
        image.verify()
    with Image.open(BytesIO(data)) as image:
        assert image.getchannel("A").getextrema() == (0, 255)


def validate():
    with ZipFile(PACK) as archive:
        manifest = json.loads(archive.read("manifest.json"))
        icons = manifest["assets"]["icons"]
        assert archive.testzip() is None
        assert manifest["schemaVersion"] == 1 and manifest["packageType"] == "icon_pack"
        assert manifest["version"] == "1.0.0" and manifest["author"]["name"] == "Fayth"
        assert not (manifest["requiredActions"] or manifest["requiredIntegrations"] or manifest["assets"]["sounds"])
        assert Counter(x["path"].split("/")[2].split("-")[0] for x in icons) == {"malakit": 72, "azurit": 72}
        assert len({icon["id"] for icon in icons}) == len({icon["name"] for icon in icons}) == 144
        paths = [icon["path"] for icon in icons]
        assert len(set(paths)) == 144
        assert set(archive.namelist()) == {"manifest.json", manifest["coverImage"], *paths}
        assert len(archive.namelist()) == 146 and not any(member.flag_bits & 1 for member in archive.infolist())
        checksums = set()
        for icon in icons:
            path = icon["path"]
            assert re.fullmatch(r"assets/icons/[a-z0-9-]+\.png", path), path
            png = archive.read(path)
            check_image(png, (128, 128))
            checksums.add(hashlib.sha256(png).hexdigest())
        assert len(checksums) == 144
        assert manifest["coverImage"] == "preview/cover.png"
        check_image(archive.read(manifest["coverImage"]), (480, 480))

    cover = DIST / "mineral-kapak.webp"
    assert cover.stat().st_size < 2_000_000
    with Image.open(cover) as image:
        assert image.format == "WEBP" and image.size == (768, 768)
        image.verify()
    with Image.open(DIST / "mineral-onizleme.webp") as image:
        assert image.format == "WEBP" and image.size == (2496, 1552)
        image.verify()
    print("144 benzersiz RGBA PNG, manifest, ZIP ve kapak doğrulandı.")
    print(f"SHA-256  {hashlib.sha256(PACK.read_bytes()).hexdigest()}")


if __name__ == "__main__":
    validate()
