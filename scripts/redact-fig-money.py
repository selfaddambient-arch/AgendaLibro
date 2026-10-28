"""1冊目の図21・23（Wi-Fi のパスワード）、図25（キャッシュフローのメモ）、図26（CF管理の画面）を、不透明の黒い四角で塗りつぶす。
  python3 scripts/redact-fig-money.py
Apple Vision（scripts/ocr-chars.swift）で文字の位置を出し、次を塗る（代表承認 2026-10-28）：
  図21・23：pass: で始まるパスワード
  図25：金額の数字すべて（項目名・日付は残す）
  図26：ローマ字の氏名（kawaguchi）、銀行ごとの残高・給与・合計などの金額すべて
縮小版（images/_web）には同じ割合で塗る。モザイク・ぼかしは使わない。塗った位置の文字列は保存しない。
"""
import json, re, subprocess, sys
from PIL import Image, ImageDraw
D = 'books/hitori-de-mise/images/'
TARGETS = {'fig-21.png': 'pass', 'fig-23.png': 'pass', 'fig-25.png': 'money', 'fig-26.png': 'money+name'}
DATE = re.compile(r'\d{4}/\d{1,2}/\d{1,2}')
NUM = re.compile(r'[¥￥]?\s*\d[\d,，.]*')

def ocr(path):
    return json.loads(subprocess.run(['swift', 'scripts/ocr-chars.swift', path], capture_output=True, text=True, check=True).stdout)

def spans(text, mode):
    out = []
    if 'pass' in mode:
        m = re.search(r'pass', text, re.I)
        if m: out.append((m.start(), len(text)))
        elif re.search(r'be[l1i]oo', text, re.I): out.append((0, len(text)))
    if 'money' in mode:
        dates = [m.span() for m in DATE.finditer(text)]
        for m in NUM.finditer(text):
            s, e = m.span()
            if any(a <= s < b for a, b in dates): continue
            digits = len(re.findall(r'\d', m.group()))
            if m.group().lstrip()[:1] in '¥￥' or digits >= 3:
                out.append((s, e))
    if 'name' in mode and re.search(r'k[a-z]{1,3}guchi|guchi|kaw', text, re.I):
        out.append((0, len(text)))
    return out

for name, mode in TARGETS.items():
    path = D + name
    im = Image.open(path).convert('RGB')
    W, H = im.size
    rects = []
    for ob in ocr(path):
        for s, e in spans(ob['text'], mode):
            bs = [b for b in ob['boxes'][s:e] if b[2] > 0]
            if not bs: continue
            x0 = min(b[0] for b in bs); y0 = min(b[1] for b in bs)
            x1 = max(b[0] + b[2] for b in bs); y1 = max(b[1] + b[3] for b in bs)
            rects.append((x0, y0, x1, y1))
    pad = 0.002
    if name == 'fig-26.png':  # 入力欄の金額（OCRが読み落とす分も含め、数字の入る欄を位置で塗る。802×1001の画面）
        for cy in (135, 185, 233, 283, 331, 494, 543, 705, 754, 803, 965):
            rects.append((385 / 802, (cy - 11) / 1001, 484 / 802, (cy + 11) / 1001))
    for p in (path, D + '_web/' + name):
        t = Image.open(p).convert('RGB')
        d = ImageDraw.Draw(t)
        for x0, y0, x1, y1 in rects:
            d.rectangle(((x0 - pad) * t.width, (y0 - pad) * t.height, (x1 + pad) * t.width, (y1 + pad) * t.height), fill=(0, 0, 0))
        t.save(p)
    print(name, '塗った箇所', len(rects))
