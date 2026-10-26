#!/usr/bin/env python3
"""PDF の各図が1ページ内に収まっているかを、画像とキャプションの位置で確認する。

  <venv>/bin/python3 scripts/check-pdf-figures.py <PDF>   # PyMuPDF が要る

- キャプション（「図X-Y　…」で始まる行）と同じページに画像があること
- 画像の高さが版面（178mm）の85%以下であること
"""
import re
import sys
import pymupdf as fitz

doc = fitz.open(sys.argv[1])
cap = re.compile(r"^図\d+-\d+[a-z]?\s")
mm = 25.4 / 72
bad, figs, tall = [], 0, []
for i, page in enumerate(doc, 1):
    if i == 1:
        continue  # 表紙
    caps = [l for l in page.get_text().split("\n") if cap.match(l)]
    imgs = [r for img in page.get_images(full=True) for r in page.get_image_rects(img[0])]
    imgs = [r for r in imgs if not (abs(r.width / r.height - 1) < 0.05 and r.width * mm < 50)]  # 正方形の小さな画像（QR）を除く
    figs += len(caps)
    if len(caps) != len(imgs):
        bad.append((i, caps, len(imgs)))
    for r in imgs:
        if r.height * mm > 178 * 0.85 + 0.5:
            tall.append((i, round(r.height * mm, 1)))
print(f"ページ数 {len(doc)} / 図のキャプション {figs} / 分割の疑い {len(bad)} / 高さ超過 {len(tall)}")
for b in bad:
    print("  分割:", b)
for t in tall:
    print("  超過:", t)
sys.exit(1 if bad or tall else 0)
