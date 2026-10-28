#!/usr/bin/env python3
"""輪郭線の検査（v2）：色の境目に、周りの2色のどちらとも違う濃い色が細く挟まっている画素を数える。

  <venv>/bin/python3 scripts/outline-check.py <画像>...   # Pillow・numpy が要る

画像を幅 1280px にそろえ、各画素について、縦・横それぞれ両側 K px 離れた画素（周りの2色）と比べる。
次の3つをすべて満たす画素を「輪郭線の画素」として数え、画像全体の LIMIT 未満なら合格（終了コード 0）。
  1) 輝度が、両側の画素のどちらよりも T 以上暗い（濃い色である）
  2) 両側の画素との色の距離（RGB）が、どちらも D 以上（周りの2色のどちらとも違う）
  3) 両側の画素の間の距離は 2K px（4px）以内（＝挟まっている線の幅が 3px 以下の細さ）
設定値（K=2, T=25, D=40, 基準 0.5%）は、前回版の2枚（2冊目のマガジン 0.53%・1冊目の第5章 0.97%）が不合格に、
輪郭線のない他の画像（最大 0.44%）が合格になる境目に合わせた（余白は小さい）。
v1（細い濃色の画素の割合）は `--v1` で使える。
"""
import sys
import numpy as np
from PIL import Image, ImageFilter

K, T, D, LIMIT = 2, 25, 40, 0.005


def load(path, width=1280):
    im = Image.open(path).convert("RGB")
    return im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)


def v2(path):
    a = np.asarray(load(path)).astype(np.int32)
    luma = (a[..., 0] * 299 + a[..., 1] * 587 + a[..., 2] * 114) // 1000
    flagged = np.zeros(luma.shape, dtype=bool)
    for axis in (0, 1):
        pa, pb = np.roll(a, K, axis=axis), np.roll(a, -K, axis=axis)
        la, lb = np.roll(luma, K, axis=axis), np.roll(luma, -K, axis=axis)
        da = np.sqrt(((a - pa) ** 2).sum(-1))
        db = np.sqrt(((a - pb) ** 2).sum(-1))
        f = (luma < la - T) & (luma < lb - T) & (da >= D) & (db >= D)
        flagged |= f
    flagged[:K] = flagged[-K:] = False
    flagged[:, :K] = flagged[:, -K:] = False
    return flagged.sum() / flagged.size


def v1(path):
    im = load(path, 640)
    luma = np.asarray(im.convert("L")).astype(np.int16)
    dark = Image.fromarray(((luma < 100) * 255).astype("uint8"))
    opened = dark.filter(ImageFilter.MinFilter(3)).filter(ImageFilter.MaxFilter(3))
    thin = (np.asarray(dark) > 0) & ~(np.asarray(opened) > 0)
    return thin.sum() / thin.size


if __name__ == "__main__":
    args = sys.argv[1:]
    old = "--v1" in args
    paths = [x for x in args if not x.startswith("--")]
    limit = 0.01 if old else LIMIT
    bad = 0
    for p in paths:
        r = (v1 if old else v2)(p)
        ok = r < limit
        bad += 0 if ok else 1
        print(f"{p.split('/')[-1]}: 輪郭線の画素 {r * 100:.2f}% {'OK' if ok else 'NG'}")
    sys.exit(1 if bad else 0)
