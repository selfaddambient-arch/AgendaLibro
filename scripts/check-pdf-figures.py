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
# 第2引数に原稿 .md を渡すと、原稿の画像の説明文（![説明](…)）をキャプションとして照合する（図番号が無い本用）
captions = []
if len(sys.argv) > 2:
    captions = [m.group(1) for m in re.finditer(r"^!\[(.*)\]\(", open(sys.argv[2], encoding="utf-8").read(), re.M)]
norm = lambda t: re.sub(r"\s+", "", t)
mm = 25.4 / 72
bad, figs, tall = [], 0, []
for i, page in enumerate(doc, 1):
    if i == 1:
        continue  # 表紙
    imgs = [r for img in page.get_images(full=True) for r in page.get_image_rects(img[0])]
    imgs = [r for r in imgs if not (abs(r.width / r.height - 1) < 0.05 and r.width * mm < 50)]  # 正方形の小さな画像（QR）を除く
    if captions:
        # 画像の直下（40pt 以内）に、原稿のキャプションで始まる文字のかたまりがあること
        blocks = [(b[0], b[1], b[3], norm(b[4])) for b in page.get_text("blocks")]
        caps = []
        for r in imgs:
            hit = next((bk for bk in blocks if -4 <= bk[1] - r.y1 <= 40 and any(norm(c)[:10] and bk[3].startswith(norm(c)[:10]) for c in captions)), None)
            if hit:
                caps.append(hit[3][:12])
    else:
        caps = [l for l in page.get_text().split("\n") if cap.match(l)]
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
