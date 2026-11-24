#!/usr/bin/env python3
"""Render the 23 November 2026 world-news image (1024x1024 PNG).

Render-time only: main.py never imports this file.
Requires Pillow.
"""

import hashlib
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "asset", "entry.png")

W, H = 1024, 1024
INK = (24, 24, 28)
PAPER = (250, 247, 238)
RED = (178, 34, 34)
GOLD = (176, 141, 60)
GREY = (96, 96, 100)
LINE = (210, 204, 190)
FOOT = (52, 52, 58)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


def wrap(draw, text, face, width):
    words = text.split()
    lines, current = [], ""
    for word in words:
        trial = f"{current} {word}".strip()
        if draw.textlength(trial, font=face) <= width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


STORIES = [
    ("NVIDIA", "Huang returns as CEO",
     "Nvidia brings back Jensen Huang as chief executive; shares jump about 30% on the news."),
    ("UKRAINE", "Sea drones sink Russian warship",
     "Seven Ukrainian naval drones sink a Russian warship off Libya and hit the cargo ship Angara."),
    ("CLIMATE", "COP31 ends with no deal",
     "Climate talks in Antalya collapse without agreement after fossil-fuel language is stripped out."),
    ("BELGIUM", "National strike grounds flights",
     "A nationwide strike cancels nearly all flights at Brussels and Charleroi airports."),
    ("RED SEA", "Houthis claim refinery attack",
     "Yemen's Houthis say they struck an oil refinery on Saudi Arabia's Red Sea coast."),
    ("INDONESIA", "Factory fire kills 24",
     "A fire at a candy factory in Banten kills 24 people; 34 more are reported missing."),
]


def draw_story(draw, story, top, index):
    tag, head, body = story
    y = top
    draw.ellipse([64, y + 2, 100, y + 38], fill=RED)
    num = font("DejaVuSans-Bold.ttf", 20)
    label = str(index + 1)
    tw = draw.textlength(label, font=num)
    draw.text((82 - tw / 2, y + 7), label, font=num, fill=(255, 255, 255))
    title = f"{tag}  —  {head}"
    draw.text((120, y + 2), title, font=font("DejaVuSans-Bold.ttf", 27), fill=INK)
    lines = wrap(draw, body, font("DejaVuSans.ttf", 22), 1024 - 120 - 64)
    by = y + 42
    for line in lines:
        draw.text((120, by), line, font=font("DejaVuSans.ttf", 22), fill=(60, 60, 66))
        by += 30
    return by


def main():
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, W, 148], fill=INK)
    draw.rectangle([0, 148, W, 154], fill=GOLD)
    draw.text((64, 22), "THE WORLD IN ONE DAY", font=font("DejaVuSans-Bold.ttf", 44), fill=(250, 247, 238))
    draw.text((64, 84), "23 NOVEMBER 2026  ·  MONDAY", font=font("DejaVuSans-Bold.ttf", 28), fill=GOLD)
    draw.text((64, 118), "Six stories that shaped the day", font=font("DejaVuSans.ttf", 22), fill=(180, 180, 190))
    y = 186
    for i, story in enumerate(STORIES):
        y = draw_story(draw, story, y, i)
        if i < len(STORIES) - 1:
            draw.line([(64, y + 10), (W - 64, y + 10)], fill=LINE, width=2)
            y += 22
    if y > H - 64:
        raise SystemExit(f"layout overflow: last story ends at y={y}, footer starts at {H - 56}")
    draw.rectangle([0, H - 56, W, H], fill=FOOT)
    note = "Sources: public news coverage of 23 November 2026  ·  Built by an AI agent for make.fun"
    draw.text((64, H - 44), note, font=font("DejaVuSans.ttf", 19), fill=(200, 200, 208))
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    img.save(OUT, format="PNG")
    with open(OUT, "rb") as handle:
        digest = hashlib.sha256(handle.read()).hexdigest()
    print(f"wrote {OUT} ({os.path.getsize(OUT)} bytes, sha256 {digest})")


if __name__ == "__main__":
    main()
