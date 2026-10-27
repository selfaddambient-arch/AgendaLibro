#!/usr/bin/env python3
"""note 記事 a：原稿の「はじめに」全文（3つの出口まで）を書き出す（前後リンク・案内は note-split.py が付ける）。
原稿から機械的に抜くので、本文は手で写さない。"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "books/uchi-no-mise/bontaraku-02_uchi-no-mise_manuscript.md"
OUT = ROOT / "books/uchi-no-mise/note/a-hajimeni.md"

lines = SRC.read_text(encoding="utf-8").split("\n")
s = next(i for i, l in enumerate(lines) if l.startswith("## はじめに"))
e = next(i for i, l in enumerate(lines) if l.startswith("## 第1章"))
body = "\n".join(lines[s + 1 : e]).strip()
body = re.sub(r"^### ", "## ", body, flags=re.M).replace("\\_", "_")
cover = "![表紙](../build/cover.png)"
OUT.write_text("# 『うちの店は、うちの仕様で』はじめに\n\n" + body + "\n\n" + cover + "\n", encoding="utf-8")
print(len(body), "字（はじめに本文）")
