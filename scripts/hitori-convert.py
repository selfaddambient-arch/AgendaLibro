#!/usr/bin/env python3
"""1冊目『1人で店を回す、その横にAIが来た』の docx を、原稿 Markdown と画像（images/fig-01〜）に変換する。

  python3 scripts/hitori-convert.py

- pandoc で docx → gfm（画像は work/media に取り出す）
- 直すのは体裁だけ：強調記号・目次・空の見出し・区切り線・見出しID・【 】の記号を落とし、見出しの階層を整える。本文の言葉は変えない
- 画像は出現順に fig-01〜（同じ画像が複数箇所にあれば、その数だけ複製）。画像の下の（…）はキャプションにする
- 冒頭に「再公開にあたって」、巻末に「3つの出口」を足す（代表指示 2026-10-28）
"""
import re
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BOOK = ROOT / "books" / "hitori-de-mise"
SRC = next((BOOK / "source").glob("*.docx"))
WORK = BOOK / "work"
OUT = BOOK / "bontaraku-01_hitori-de-mise_manuscript.md"
IMAGES = BOOK / "images"

REPUBLISH = "本書は2026年1月時点の記録です。店の営業のしかたや、AIの道具の名前・仕様は、その後変わっているものがあります。続きは2冊目『うちの店は、うちの仕様で』に書きました。"

EXITS = """### この本の、3つの出口

この本は、PDFとnoteとGoogle Playで無料で読めます（Kindleだけは、ストアの決まりで最低価格を付けています）。代わりに、読み終えたあとに行ける場所を3つ用意しました。どれか一つでも使ってもらえたら、この本を書いた甲斐があります。

1. 屯に行ってみる。東中野駅東口から1分。予約なしでも入れます。予約サイト https://tamuroreservation.vercel.app/?src=book1
2. 自分の店で試してみる。Agendaシリーズは無料の手帳から始められます。https://bontallc.com/agenda?via=book1
3. 活動を追いかける。次に作る道具や、店の日々は、noteとXで書いています。note https://note.com/bontallc／X https://x.com/tamuro\\_hnakano

本を読んで来てくださった方へ。予約のときに、クーポンコード「BOOK」を入れてください。初回のお飲み物を一杯、お出しします。予約なしで来られた方は、最初の注文のときに「本を見た」と一言ください。同じ一杯をお出しします。本から来てくださった方が何人いたか、わたしが数えられるようにするための、小さな仕掛けです。
"""

LABEL = re.compile(r"^\**【(.+?)】\**\s*(.*)$")


def main():
    WORK.mkdir(exist_ok=True)
    subprocess.run(["pandoc", str(SRC), "-f", "docx", "-t", "gfm", "--wrap=none", f"--extract-media={WORK / 'media'}", "-o", str(WORK / "raw.md")], check=True)
    L = (WORK / "raw.md").read_text(encoding="utf-8").split("\n")
    start = next(i for i, l in enumerate(L) if l == "# はじめに")
    L = L[start:]

    # 区切り線（「\」と「=」の組）を落とす
    out = []
    i = 0
    while i < len(L):
        if L[i] == "\\" and i + 1 < len(L) and L[i + 1] == "=":
            i += 2
            continue
        out.append(L[i])
        i += 1
    L = out

    res, figs = [], []
    i = 0
    n_img = 0
    while i < len(L):
        l = L[i]
        # --- 画像
        m = re.match(r'<img src="([^"]+)"', l)
        if m:
            n_img += 1
            src = WORK / m.group(1).replace("media/media/", "media/media/", 1)
            ext = src.suffix.lower()
            name = f"fig-{n_img:02d}{ext}"
            IMAGES.mkdir(exist_ok=True)
            shutil.copy(src, IMAGES / name)
            # 下の（…）／(…) をキャプションに
            j = i + 1
            while j < len(L) and not L[j].strip():
                j += 1
            cap = ""
            if j < len(L) and re.match(r"^[（(].*[）)]$", L[j].strip()):
                cap = L[j].strip()[1:-1].strip()
                i = j  # キャプション行を消費
            else:
                # 写真に説明が無い場合は、直前の「▼ …」の見出しをキャプションにする
                for k in range(len(res) - 1, max(len(res) - 8, 0), -1):
                    if res[k].startswith("▼ "):
                        cap = res[k][2:].strip()
                        break
                if not cap:
                    # それも無ければ、直前の見出しの文言（すでに本文にある言葉）をキャプションにする
                    for k in range(len(res) - 1, -1, -1):
                        mm = re.match(r"^\**【(.+?)】\**", res[k])
                        if mm:
                            cap = mm.group(1).strip()
                            break
                        if res[k].startswith("#"):
                            cap = res[k].lstrip("#").strip()
                            break
                if not cap:
                    pass
            res.append(f"![{cap}](images/{name})")
            figs.append((name, cap))
            i += 1
            continue
        res.append(l)
        i += 1
    L = res

    res = []
    i = 0
    while i < len(L):
        l = L[i]
        # --- 見出しの整理
        if l == "# はじめに":
            res.append("## はじめに")
        elif l.startswith("## 元システム屋"):
            res.append("### " + l[3:])
        elif re.match(r"^# 第\d章$", l):
            # 次の「## 〇〇編 - …」と1行にまとめる
            j = i + 1
            while not L[j].startswith("## "):
                j += 1
            res.append(f"## {l[2:]}　{L[j][3:].strip()}")
            i = j + 1
            continue
        elif l == "# おわりに":
            j = i + 1
            while not L[j].startswith("## "):
                j += 1
            res.append(f"## おわりに　{L[j][3:].strip()}")
            i = j + 1
            continue
        elif l == "# 【著者プロフィール】":
            res.append(EXITS)
            res.append("### 著者プロフィール")
        elif re.match(r"^### +$", l) or l.strip() == "###":
            pass  # 空の見出し
        elif re.match(r"^### (?!\d-\d)", l):
            # 本文が見出しになっているもの（6章冒頭の案内）は段落に戻す
            res.append(l[4:])
        else:
            res.append(l)
        i += 1
    L = res

    text = "\n".join(L)
    # --- 記号の整理
    text = re.sub(r"\[<u>(.*?)</u>\]\((.*?)\)", r"\1", text)  # リンクは URL の文字だけ残す
    text = text.replace("\\*\\*", "").replace("**", "")
    text = re.sub(r"\\\*([^*\n]+?)\\\*", r"\1", text)  # \*強調\*
    text = re.sub(r"\*([^*\n]+?)\*", r"\1", text)  # *強調*
    # 【 】：行全体が見出し的なものは小見出しに、行の中のものは記号だけ落とす
    lines = []
    for l in text.split("\n"):
        m = LABEL.match(l.strip()) if l.strip().startswith(("【", "**【")) else None
        if m:
            lines.append("#### " + m.group(1))
            if m.group(2).strip():
                lines += ["", m.group(2).strip()]
        else:
            lines.append(l.replace("【", "").replace("】", ""))
    text = "\n".join(lines)
    text = re.sub(r"^(#{2,4} .*?)\\$", r"\1", text, flags=re.M)  # 見出し末尾の改行記号
    text = re.sub(r"\n{3,}", "\n\n", text).strip("\n")

    body = f"{REPUBLISH}\n\n" + text if False else text
    # 「再公開にあたって」：はじめにの見出しの直後に1段落
    text = text.replace("## はじめに\n", f"## はじめに\n\n{REPUBLISH}\n", 1)
    OUT.write_text(text.strip("\n") + "\n", encoding="utf-8")
    print("画像", n_img, "→ images/fig-01〜", f"{n_img:02d}")
    print("原稿", OUT.name, len(text), "字")


main()
