#!/usr/bin/env python3
"""原稿 Markdown を pandoc に渡せる形へ整える。

  python3 scripts/preprocess.py <epub|pdf> <出力.md>

- 【図X-Y】キャプション行を、図番号に対応する画像の figure へ置き換える
- 図番号と画像の対応は images/index.md のファイル名（figX-Y_*.png）から作る。
  合わない分は一覧にして終了コード 2 で止まる
- 先頭の書誌ブロック（題名〜3リンク）は metadata.yaml と奥付へ移す
- 強調記号（**／*）を落とす、URL を <> で括る、\\_ を _ に戻す
- pdf のときだけ「3つの出口」の直後に QR を3つ置く
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BOOK = ROOT / "books" / "uchi-no-mise"
MANUSCRIPT = BOOK / "bontaraku-02_uchi-no-mise_manuscript.md"
IMAGES = BOOK / "images"
BUILD = BOOK / "build"

MARK = re.compile(r"^【図(\d+-\d+[a-z]?)】(.*)$")

# 図番号 → 画像の明示指定（キャプションの意味に合う画像が複数あるとき。代表裁定 2026-10-26）
FILE_OVERRIDE = {"1-7": "fig1-7b_compare.png"}

# 指示と実際が違う図のキャプション。実画面に合わせる（index.md の備考が根拠）
CAPTION_OVERRIDE = {
    "1-4": "T-AI-MUROの会話の画面。最初の選択肢（「予約したいです」）を押すと、人数の質問が出る",
    "1-9": "マイページの来店回数（通算3回・次の特典まであと2回）（合成データ）",
    "2-2": "AIの試験の結果（36本中9本合格＝25.0％）と、間違いの原因の内訳",
}

QR_LINKS = [
    ("屯に行ってみる", "qr-tamuro.png"),
    ("自分の店で試してみる", "qr-agenda.png"),
    ("活動を追いかける（note）", "qr-note.png"),
]

COLOPHON = """## 奥付

- 題名：うちの店は、うちの仕様で
- 副題：19席のバー店主が、AIで予約システムから道具まで自分で作った記録
- 著者：本多楽（ぼんたらく）
- 発行：ボンタ合同会社
- 言語：日本語

屯のInstagram：https://www.instagram.com/tamuro.higashinakano/

屯の予約サイト：https://tamuroreservation.vercel.app/?src=book

Agendaシリーズ：https://bontallc.com/agenda?via=book

note：https://note.com/bontallc

X：https://x.com/tamuro_hnakano
"""


def figure_files():
    by_id = {}
    for p in sorted(IMAGES.glob("fig*.png")):
        m = re.match(r"fig(\d+-\d+[a-z]?)_", p.name)
        by_id.setdefault(m.group(1), []).append(p.name)
    return by_id


def main():
    mode, out = sys.argv[1], Path(sys.argv[2])
    lines = MANUSCRIPT.read_text(encoding="utf-8").split("\n")
    start = next(i for i, l in enumerate(lines) if l.startswith("## はじめに"))
    body = lines[start:]

    by_id = figure_files()
    problems, used, changes = [], [], []
    result = []
    for line in body:
        m = MARK.match(line)
        if not m:
            result.append(line)
            continue
        fig, caption = m.group(1), m.group(2).strip()
        cands = by_id.get(fig, [])
        fname = FILE_OVERRIDE.get(fig) or (cands[0] if len(cands) == 1 else None)
        if fname is None or not (IMAGES / fname).exists():
            problems.append(f"図{fig}: 画像が決まらない（候補 {cands}）")
            continue
        if fig in CAPTION_OVERRIDE:
            changes.append({"fig": fig, "before": caption, "after": CAPTION_OVERRIDE[fig]})
            caption = CAPTION_OVERRIDE[fig]
        used.append(fname)
        alt = f"図{fig}　{caption}".replace("[", "［").replace("]", "］")
        result.append(f"![{alt}](images/{fname})")

    marks = sum(1 for l in body if MARK.match(l))
    dup = sorted({f for f in used if used.count(f) > 1})
    if dup:
        problems.append(f"同じ画像が複数の印に使われた: {dup}")
    all_png = {p.name for p in IMAGES.glob("fig*.png")}
    unused = sorted(all_png - set(used))

    text = "\n".join(result)
    # 強調記号を落とす（原稿は現状 0 件。入ったときの保険）
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"(?<![*\w])\*([^*\s][^*]*?)\*(?![*\w])", r"\1", text)
    text = text.replace("\\_", "_")
    # URL を <> で括る（全角文字の手前で止まる）
    text = re.sub(r"(?<![<(\"])(https?://[A-Za-z0-9._~:/?#@!$&'*+,;=%\-]+)", r"<\1>", text)

    if mode == "pdf":
        qr = "\n".join(
            f'<figure><img src="images/_qr/{f}" alt=""><figcaption>{label}</figcaption></figure>'
            for label, f in QR_LINKS
        )
        block = f'\n```{{=html}}\n<div class="qr">\n{qr}\n</div>\n```\n'
        text = text.replace("\n## 第1章", block + "\n## 第1章", 1)

    text = text.rstrip("\n") + "\n\n" + re.sub(
        r"(?<![<(\"])(https?://[A-Za-z0-9._~:/?#@!$&'*+,;=%\-]+)", r"<\1>", COLOPHON
    )
    out.write_text(text, encoding="utf-8")

    BUILD.mkdir(parents=True, exist_ok=True)
    (BUILD / "figures.json").write_text(
        json.dumps(
            {"marks": marks, "used": used, "unused_png": unused, "caption_changes": changes, "problems": problems},
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"図の印 {marks} / 使った画像 {len(set(used))} / 未使用PNG {unused}")
    if problems:
        print("\n".join(problems))
        sys.exit(2)


if __name__ == "__main__":
    main()
