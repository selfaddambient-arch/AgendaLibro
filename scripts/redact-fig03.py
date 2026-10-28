"""1冊目 図3（スタッフへの長文のLINE）の、相手の表示名とアイコンを不透明の黒い四角で塗りつぶす。
  python3 scripts/redact-fig03.py
元の画像（854×1917）の座標で指定し、縮小版（images/_web）には同じ割合で塗る。モザイク・ぼかしは使わない。
"""
from PIL import Image, ImageDraw
BOXES = [  # (左, 上, 右, 下) 元画像の座標
    (284, 436, 345, 498),   # 引用の返信：アイコン
    (348, 436, 430, 466),   # 引用の返信：表示名
    (8, 1712, 162, 1770),   # 画面の下：アイコンと表示名
]
W0, H0 = 854, 1917
for path in ['books/hitori-de-mise/images/fig-03.jpg', 'books/hitori-de-mise/images/_web/fig-03.jpg']:
    im = Image.open(path).convert('RGB')
    sx, sy = im.width / W0, im.height / H0
    d = ImageDraw.Draw(im)
    for l, t, r, b in BOXES:
        d.rectangle((l * sx, t * sy, r * sx, b * sy), fill=(0, 0, 0))
    im.save(path, quality=95)
    print(path, im.size)
