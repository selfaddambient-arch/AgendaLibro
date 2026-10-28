#!/usr/bin/env python3
"""1冊目『一人で店を回す、その横にAIが来た。』の原稿を、章ごとの note 記事（Markdown）8本に分ける。

  python3 scripts/note-split-book1.py

出力：books/hitori-de-mise/note/intro.md, ch1.md … ch6.md, ep.md（おわりに）。
各記事：題名／「全8回の◯回目」／前の章へのリンク／本文／次の章へのリンク／共通の案内。
下書きの鍵は note/drafts.json。公開前の記事はリンク先が開かない（公開すると開く）。
note は表に対応しないが、この本の原稿に表は無い。
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BOOK = ROOT / "books" / "hitori-de-mise"
NOTE = BOOK / "note"
MANUSCRIPT = BOOK / "bontaraku-01_hitori-de-mise_manuscript.md"
BOOK_TITLE = "『一人で店を回す、その横にAIが来た。』"
PUBLIC = "https://note.com/bontallc/n/"
SLUGS = ["intro", "ch1", "ch2", "ch3", "ch4", "ch5", "ch6", "ep"]

# 共通の案内：note 経由は ?src=note1 / ?via=note1 で、本の中（?src=book1 / ?via=book1）と分けて数える
FOOTER = """## この本の、ほかの読み方

Kindle：[https://www.amazon.co.jp/dp/B0GFY4WW4Y](https://www.amazon.co.jp/dp/B0GFY4WW4Y)

屯の予約サイト：[https://tamuroreservation.vercel.app/?src=note1](https://tamuroreservation.vercel.app/?src=note1)

Agendaシリーズ：[https://bontallc.com/agenda?via=note1](https://bontallc.com/agenda?via=note1)

note：[https://note.com/bontallc](https://note.com/bontallc)

X：[https://x.com/tamuro_hnakano](https://x.com/tamuro_hnakano)"""


def web_image(name):
    for cand in (name, Path(name).stem + ".jpg"):
        if (BOOK / "images" / "_web" / cand).exists():
            return f"../images/_web/{cand}"
    return f"../images/{name}"


def convert(body_lines):
    res = []
    for line in body_lines:
        m = re.match(r"^!\[(.*)\]\(images/([^)]+)\)$", line)
        if m:
            cap, name = m.group(1), m.group(2)
            res += [f"![{cap}]({web_image(name)})", ""]
            if cap:
                res += [cap, ""]
            continue
        if line.startswith("#### "):
            line = "### " + line[5:]
        elif line.startswith("### "):
            line = "## " + line[4:]
        line = re.sub(r"\\$", "", line)  # 行末の改行記号（note では段落内の改行にする）
        line = re.sub(r"\\([\[\]_])", r"\1", line)
        res.append(line)
    # 項目の間の空行を詰める（空行で分かれると、note では番号が毎回 1 に戻る）
    item = re.compile(r"^(\d+\.\s|- )")
    out = []
    for k, line in enumerate(res):
        if line == "" and out and item.match(out[-1]):
            nxt = next((x for x in res[k + 1 :] if x != ""), "")
            if item.match(nxt):
                continue
        out.append(line)
    return "\n".join(out).strip("\n")


def main():
    lines = MANUSCRIPT.read_text(encoding="utf-8").split("\n")
    heads = [i for i, l in enumerate(lines) if l.startswith("## ")]
    secs = []
    for n, i in enumerate(heads):
        end = heads[n + 1] if n + 1 < len(heads) else len(lines)
        secs.append((lines[i][3:].strip(), lines[i + 1 : end]))
    assert len(secs) == len(SLUGS), len(secs)
    drafts = json.loads((NOTE / "drafts.json").read_text())
    total = len(SLUGS)

    def link(idx, label):
        return f"[{label}　{secs[idx][0]}]({PUBLIC}{drafts[SLUGS[idx]]})"

    for i, slug in enumerate(SLUGS):
        title, body = secs[i]
        parts = [f"# {BOOK_TITLE}{title}", f"全{total}回の{i + 1}回目"]
        if i > 0:
            parts.append(link(i - 1, "◀ 前の章"))
        parts.append(convert(body))
        if i + 1 < total:
            parts.append(link(i + 1, "次の章 ▶"))
        parts.append(FOOTER)
        name = "ep" if slug == "ep" else slug
        (NOTE / f"{name}.md").write_text("\n\n".join(parts) + "\n", encoding="utf-8")
        print(slug, len("\n".join(body)), "字", "prev" if i > 0 else "-", "next" if i + 1 < total else "-")


main()
