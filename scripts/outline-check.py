#!/usr/bin/env python3
"""輪郭線の検査：フラットデザインに黒や濃い色の細い線が入っていないかを数える。

  <venv>/bin/python3 scripts/outline-check.py <画像>...   # Pillow・numpy が要る

画像を幅 640px に縮小し、濃色（輝度 100 未満）の画素のうち、3×3 の開き（収縮→膨張）で消える
＝幅 2px 以下の細い構造の画素を数える。全体の 1% 未満なら合格（終了コード 0）。
"""
import sys
import numpy as np
from PIL import Image, ImageFilter

LIMIT = 0.01
DARK = 100
bad = 0
for path in sys.argv[1:]:
    im = Image.open(path).convert("RGB")
    im = im.resize((640, round(im.height * 640 / im.width)), Image.LANCZOS)
    luma = np.asarray(im.convert("L")).astype(np.int16)
    dark = Image.fromarray(((luma < DARK) * 255).astype("uint8"))
    opened = dark.filter(ImageFilter.MinFilter(3)).filter(ImageFilter.MaxFilter(3))
    thin = (np.asarray(dark) > 0) & ~(np.asarray(opened) > 0)
    r = thin.sum() / thin.size
    ok = r < LIMIT
    bad += 0 if ok else 1
    print(f"{path.split('/')[-1]}: 細い濃色 {r * 100:.2f}% {'OK' if ok else 'NG'}")
sys.exit(1 if bad else 0)
