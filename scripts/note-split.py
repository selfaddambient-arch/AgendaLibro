#!/usr/bin/env python3
"""原稿を章ごとの note 記事（Markdown）に分け、前後リンクを付ける。

  python3 scripts/note-split.py

出力：books/uchi-no-mise/note/ch1.md … ch5.md, ep.md（おわりに）。
「はじめに」は note-article-a.py が作る a-hajimeni.md を使い、末尾にリンクだけ足す。
下書きの ID は note/drafts.json（slug → note の記事キー）。ID が無い記事へのリンクは付けない。
note は表に対応しないため、表は note-draft.mjs が「見出し：値」の箇条書きにする。
"""
import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NOTE = ROOT / "books/uchi-no-mise/note"
spec = importlib.util.spec_from_file_location("preprocess", ROOT / "scripts/preprocess.py")
pre = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pre)

BOOK_TITLE = "『うちの店は、うちの仕様で』"
PUBLIC = "https://note.com/bontallc/n/"

# slug, 原稿の見出し（先頭一致）
CHAPTERS = [
    ("intro", "はじめに"),
    ("ch1", "第1章"),
    ("ch2", "第2章"),
    ("ch3", "第3章"),
    ("ch4", "第4章"),
    ("ch5", "第5章"),
    ("ep", "おわりに"),
]


def split_manuscript():
    lines = pre.MANUSCRIPT.read_text(encoding="utf-8").split("\n")
    heads = [i for i, l in enumerate(lines) if l.startswith("## ")]
    out = {}
    for n, i in enumerate(heads):
        end = heads[n + 1] if n + 1 < len(heads) else len(lines)
        title = lines[i][3:].strip()
        for slug, key in CHAPTERS:
            if title.startswith(key):
                out[slug] = (title, lines[i + 1 : end])
    return out


def convert_headings(body_lines):
    by_id = pre.figure_files()
    res = []
    for line in body_lines:
        m = pre.MARK.match(line)
        if m:
            fig, cap = m.group(1), m.group(2).strip()
            fname = pre.FILE_OVERRIDE.get(fig) or by_id[fig][0]
            cap = pre.CAPTION_OVERRIDE.get(fig, cap)
            res += [f"![図{fig}](../images/{fname})", "", f"図{fig}　{cap}"]
        elif line.startswith("#### "):
            res.append("### " + line[5:])
        elif line.startswith("### "):
            res.append("## " + line[4:])
        else:
            res.append(line)
    return "\n".join(res).strip("\n").replace("\\_", "_")


# 全記事の末尾に付ける共通の案内。note 経由は ?src=note / ?via=note で、本の中（?src=book / ?via=book）と分けて数える
FOOTER = """## この本の、ほかの読み方

屯の予約サイト：[https://tamuroreservation.vercel.app/?src=note](https://tamuroreservation.vercel.app/?src=note)

Agendaシリーズ：[https://bontallc.com/agenda?via=note](https://bontallc.com/agenda?via=note)

note：[https://note.com/bontallc](https://note.com/bontallc)

X：[https://x.com/tamuro_hnakano](https://x.com/tamuro_hnakano)"""


def main():
    chapters = split_manuscript()
    drafts_path = NOTE / "drafts.json"
    drafts = json.loads(drafts_path.read_text()) if drafts_path.exists() else {}
    order = [s for s, _ in CHAPTERS]

    def link(slug, label):
        if slug not in drafts:
            return None
        short = chapters[slug][0]
        return f"[{label}　{short}]({PUBLIC}{drafts[slug]})"

    subprocess.run([sys.executable, str(ROOT / "scripts/note-article-a.py")], check=True)
    for i, slug in enumerate(order):
        prev_l = link(order[i - 1], "◀ 前の章") if i > 0 else None
        next_l = link(order[i + 1], "次の章 ▶") if i + 1 < len(order) else None
        if slug == "intro":
            path = NOTE / "a-hajimeni.md"
            text = path.read_text(encoding="utf-8").rstrip("\n")
            head, rest = text.split("\n\n", 1)
            parts = [head, f"全7回の{i + 1}回目", rest]
            if next_l:
                parts.append(next_l)
            parts.append(FOOTER)
            path.write_text("\n\n".join(parts) + "\n", encoding="utf-8")
            continue
        title, body = chapters[slug]
        parts = [f"# {BOOK_TITLE}{title}", f"全7回の{i + 1}回目"]
        if prev_l:
            parts.append(prev_l)
        parts.append(convert_headings(body))
        if next_l:
            parts.append(next_l)
        parts.append(FOOTER)
        (NOTE / f"{slug}.md").write_text("\n\n".join(parts) + "\n", encoding="utf-8")
        print(slug, len("\n".join(body)), "字", "prev" if prev_l else "-", "next" if next_l else "-")


main()
