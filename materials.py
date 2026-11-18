"""Procedural polished stone and relief metal, lit from the upper left."""

from dataclasses import dataclass
from io import BytesIO

import cairosvg
import numpy as np
from PIL import Image, ImageColor
from scipy.ndimage import distance_transform_edt, gaussian_filter, shift


@dataclass(frozen=True)
class Finish:
    name: str
    stone: tuple[str, ...]
    edge: str
    metal: tuple[str, ...]
    seed: int
    offset: float


FINISHES = {
    "malakit": Finish(
        "Malakit",
        ("#05211D", "#074639", "#10755B", "#2BAA79", "#86DCA7"),
        "#C3F0AC",
        ("#946036", "#EAB76C", "#FFF0BC", "#FFFAE0"),
        49,
        -0.11,
    ),
    "azurit": Finish(
        "Azurit",
        ("#090D29", "#102854", "#24478E", "#5679C8", "#A4C4ED"),
        "#BBDBFF",
        ("#717EAF", "#B3C2E7", "#E6F3FF", "#FAFDFF"),
        75,
        0.23,
    ),
}


def rgb(hex_color):
    return np.array(ImageColor.getrgb(hex_color), dtype=np.float32) / 255


def palette(values, colors):
    steps = np.linspace(0, 1, len(colors))
    matrix = np.array([rgb(color) for color in colors])
    return np.stack([np.interp(values, steps, matrix[:, i]) for i in range(3)], axis=-1)


def coordinates(size):
    offset = np.linspace(-1, 1, size)
    return np.meshgrid(offset, offset)


def smooth(low, high, values):
    fraction = np.clip((values - low) / (high - low), 0, 1)
    return fraction * fraction * (3 - 2 * fraction)


def rgba(colors, mask):
    pixels = np.concatenate([colors, mask[..., None]], axis=-1)
    return Image.fromarray(np.uint8(np.clip(pixels, 0, 1) * 255 + 0.5))


def normal_dot(height, pixel_step, direction):
    dy, dx = np.gradient(height, pixel_step)
    norm = np.sqrt(1 + dx * dx + dy * dy)
    vector = np.array(direction)
    vector = vector / np.linalg.norm(vector)
    return (vector[2] - dx * vector[0] - dy * vector[1]) / norm


def stone(size, finish):
    x, y = coordinates(size)
    radius = ((abs(x) / 0.94) ** 4.55 + (abs(y) / 0.94) ** 4.55) ** (1 / 4.55)
    step = 2 / (size - 1)
    mask = np.clip((1 - radius) / step + 0.5, 0, 1)
    surface = 0.13 * np.sqrt(np.maximum(0, 1 - radius ** 2))
    rng = np.random.default_rng(finish.seed)
    noise = rng.standard_normal(x.shape)

    # Offset, warped lobes make the bands bend around mineral growth centers.
    offset = finish.offset
    flow_x = 0.80 * x + 0.47 * y + 0.14 * np.sin(y * 5.2 + offset)
    flow_y = 0.93 * y - 0.4 * x + 0.13 * np.sin(x * 4.9 + offset)
    lobe_a = np.sqrt((flow_x + 0.63 + offset) ** 2 + 0.32 * (flow_y + 0.68) ** 2)
    lobe_b = np.sqrt((flow_x - 0.44) ** 2 + 0.77 * (flow_y - 0.98 + offset) ** 2)
    bedding = 0.54 * lobe_a + 0.46 * lobe_b
    bedding += 0.11 * np.sin(4.8 * flow_x + 3.1 * flow_y) + 0.024 * np.sin(11 * flow_y + 5 * flow_x)
    bands = np.sin(57 * bedding + 2.5 * np.sin(10 * lobe_a))
    fine_bands = (0.5 + 0.5 * np.sin(153 * bedding + 6 * flow_y)) ** 11
    vein = (0.5 + 0.5 * np.sin(33 * bedding + 4.2 * flow_x)) ** 25
    pools = np.sin(10.6 * lobe_b + 3.14 * np.sin(2.6 * lobe_a))
    depth = 0.41 + 0.24 * bands + 0.105 * pools + 0.09 * fine_bands + 0.078 * vein
    base = palette(np.clip(depth, 0, 0.86), finish.stone)

    key = np.clip(normal_dot(surface, step, (-0.52, -0.58, 0.7)), 0, 1)
    face = 0.76 + 0.25 * key + 0.11 * (-y) - 0.11 * x
    base *= face[..., None]
    softbox = np.exp(-((x + 0.48 - 0.20 * y) / 0.72) ** 2 - ((y + 0.67) / 0.44) ** 2)
    caustic = np.exp(-((x - 0.82 + 0.45 * y) / 0.39) ** 2 - ((y - 0.44) / 0.58) ** 2)
    bevel = np.exp(-((radius - 0.962) / 0.017) ** 2)
    rim = bevel * (0.10 + 0.59 * np.clip(0.36 - 0.48 * x - 0.57 * y, 0, 1))
    sheen = 0.17 * softbox + 0.15 * caustic + rim
    base = base * (1 - sheen[..., None]) + rgb(finish.edge) * sheen[..., None]
    base += (0.011 * noise + 0.013 * gaussian_filter(noise, 2))[..., None]
    return rgba(base, mask)


def emblem_mask(markup, size, fraction):
    glyph_size = round(size * fraction)
    xml = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{glyph_size}" height="{glyph_size}"
        viewBox="0 0 24 24">
        <style>.solid {{ fill: white; stroke: none; }}</style>
        <g fill="none" stroke="white" stroke-width="2.1" stroke-linecap="round"
        stroke-linejoin="round">{markup}</g>
        </svg>"""
    with Image.open(BytesIO(cairosvg.svg2png(bytestring=xml.encode("utf-8")))) as glyph:
        alpha = glyph.convert("RGBA").getchannel("A")
    mask = Image.new("L", (size, size))
    inset = (size - glyph_size) // 2
    mask.paste(alpha, (inset, inset - round(size * 0.012)))
    return np.asarray(mask, dtype=np.float32) / 255


def relief(stone_image, finish, markup, fraction=0.67):
    size = stone_image.width
    x, y = coordinates(size)
    mask = emblem_mask(markup, size, fraction)
    thickness = size * 0.0095
    inside = distance_transform_edt(mask > 0.5)
    surface = smooth(0, thickness * 1.4, inside) * thickness
    key = normal_dot(gaussian_filter(surface, size * 0.0009), 1, (-0.58, -0.65, 0.72))
    reflect = smooth(0.58, 1.07, -y - 0.54 * x)
    value = np.clip(0.38 + 0.46 * key + 0.27 * reflect - 0.09 * y, 0, 1)
    metal = palette(value, finish.metal)

    backing = stone_image.copy()
    dark = np.tile(rgb("#090C10"), (size, size, 1))
    shade = gaussian_filter(shift(mask, (size * 0.025, size * 0.010)), size * 0.011) * 0.69
    backing.alpha_composite(rgba(dark, shade))
    wall = shift(mask, (size * 0.015, size * 0.004))
    riser = np.tile(rgb(finish.metal[0]), (size, size, 1))
    backing.alpha_composite(rgba(riser, wall))
    backing.alpha_composite(rgba(metal, mask))
    return backing
