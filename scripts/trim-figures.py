#!/usr/bin/env python3
"""縦長の図の上下にある空の背景を切り落とし、images/_trim/ に書き出す（元画像は変えない）。

  <scratchpad>/venv/bin/python3 scripts/trim-figures.py   # Pillow が要る

対象：版面（A5本文 120×178mm）で高さ上限（版面の85%）まで縮めたとき、横幅が版面の45%を
下回る図。背景色は左上の画素。縦に 24px の余白を残す。
"""
import unicodedata
from pathlib import Path
from PIL import Image, ImageChops

BOOK = Path(__file__).resolve().parent.parent / "books" / "uchi-no-mise"
OUT = BOOK / "images" / "_trim"
PAGE_W, PAGE_H = 120.0, 178.0
MAX_H = PAGE_H * 0.85
MIN_W = PAGE_W * 0.45
PAD = 24

OUT.mkdir(exist_ok=True)
for p in sorted((BOOK / "images").glob("fig*.png")):
    if "のコピー" in unicodedata.normalize("NFC", p.name):
        continue
    im = Image.open(p).convert("RGB")
    w, h = im.size
    scaled_w = MAX_H * w / h
    if scaled_w >= MIN_W:
        continue
    bg = Image.new("RGB", im.size, im.getpixel((0, 0)))
    diff = ImageChops.difference(im, bg).convert("L").point(lambda v: 255 if v > 12 else 0)
    box = diff.getbbox()
    if not box:
        continue
    top, bottom = max(0, box[1] - PAD), min(h, box[3] + PAD)
    new_h = bottom - top
    print(f"{p.name}: {w}x{h} -> {w}x{new_h}（縮小後の幅 {scaled_w:.0f}mm→{MAX_H * w / new_h:.0f}mm）")
    im.crop((0, top, w, bottom)).save(OUT / p.name)
