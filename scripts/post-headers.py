#!/usr/bin/env python3
"""生成した見出し画像の仕上げ：16:9 の原画を 1360×765 に切り、中央を 1280×670 に切り出す（どちらも実体は PNG）。

  <venv>/bin/python3 scripts/post-headers.py <略名> [slug ...]   # Pillow が要る
16x9/<slug>.png（モデルの出力 1376×768 など）を 1360×765 に上書きし、note/<slug>.png を作る。
"""
import sys
from pathlib import Path
from PIL import Image

book = sys.argv[1]
H = Path("books") / book / "note-headers"
slugs = sys.argv[2:] or [p.stem for p in sorted((H / "16x9").glob("*.png"))]
for s in slugs:
    p = H / "16x9" / f"{s}.png"
    im = Image.open(p).convert("RGB")
    if im.size != (1360, 765):
        x, y = (im.width - 1360) // 2, (im.height - 765) // 2
        im = im.crop((x, y, x + 1360, y + 765))
    im.save(p, "PNG")
    w = im.resize((1280, round(im.height * 1280 / im.width)), Image.LANCZOS)
    off = (w.height - 670) // 2
    w.crop((0, off, 1280, off + 670)).save(H / "note" / f"{s}.png", "PNG")
    print(s, im.size, "→ 1280x670")
