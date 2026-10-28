#!/usr/bin/env python3
"""表紙画像を 1600×2560 に収める（縦横比を保って拡縮し、足りない上下は画像の端の行を延ばして埋める。文字は足さない）。

  <venv>/bin/python3 scripts/make-cover.py <元画像> <出力.jpg>   # Pillow が要る
"""
import sys
from PIL import Image

W, H = 1600, 2560
src, out = sys.argv[1], sys.argv[2]
im = Image.open(src).convert("RGB")
s = min(W / im.width, H / im.height)
nw, nh = round(im.width * s), round(im.height * s)
im = im.resize((nw, nh), Image.LANCZOS)
canvas = Image.new("RGB", (W, H))
x, y = (W - nw) // 2, (H - nh) // 2
canvas.paste(im, (x, y))
if y > 0:  # 上下の余白：端の1行をそのまま延ばす
    canvas.paste(im.crop((0, 0, nw, 1)).resize((nw, y)), (x, 0))
    canvas.paste(im.crop((0, nh - 1, nw, nh)).resize((nw, H - y - nh)), (x, y + nh))
if x > 0:  # 左右の余白（縦長に収まらない画像の場合）
    canvas.paste(canvas.crop((x, 0, x + 1, H)).resize((x, H)), (0, 0))
    canvas.paste(canvas.crop((x + nw - 1, 0, x + nw, H)).resize((W - x - nw, H)), (x + nw, 0))
canvas.save(out, quality=92)
print(f"{im.width}x{im.height} → {W}x{H}（余白 上下 {y}px／左右 {x}px）")
