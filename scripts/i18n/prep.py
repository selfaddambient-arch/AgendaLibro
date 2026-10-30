#!/usr/bin/env python3
"""多言語版の原稿を、pandoc に渡せる形へ整える（scripts/preprocess.py の言語対応版）。

  I18N_LANG=en python3 scripts/i18n/prep.py <slug> <pdf|kindle|gp> <出力.md>

- {{FMT}} を形式（pdf／kindle／gp）に置き換える（pdf と kindle と gp の中身は同じで、印だけ違う）
- 【Figure X-Y】キャプション（見出しの語は言語ごとに違ってよい）を、図番号に対応する画像の figure へ置き換える
- 原稿に直接書かれた画像は、縮小版（images/_web/）があればそれを使う
- 先頭の書誌ブロック（題名〜リンク）は metadata.yaml と奥付へ移す（最初の「## 」から本文）
- URL を <> で括る。強調記号は残す（訳文の注 *(…)* のため）
- pdf のときだけ「3つの出口」の直後に QR を3つ置く（QR のリンクは同じ印）
- 奥付：i18n/<言語>/lang.json の colophon 雛形に、題名・日付・為替などを入れて末尾へ
"""
import json, os, re, sys, datetime, unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LG = os.environ.get("I18N_LANG", "en")
CODE = {"hitori-de-mise": "b1", "uchi-no-mise": "b2"}
MARK = re.compile(r"^【([^\d】]*?)\s*(\d+-\d+[a-z]?)】(.*)$")
FILE_OVERRIDE = {"1-7": "fig1-7b_compare.png"}   # 日本語版と同じ（代表裁定 2026-10-26）


def is_copy(name):
    return "のコピー" in unicodedata.normalize("NFC", name)


def figure_files(images):
    by_id = {}
    for p in sorted(images.glob("fig*.png")):
        if is_copy(p.name):
            continue
        m = re.match(r"fig(\d+-\d+[a-z]?)_", p.name)
        if m:
            by_id.setdefault(m.group(1), []).append(p.name)
    return by_id


URL = r"(https?://[A-Za-z0-9._~:/?#@!$&'*+,;=%\-]+)"


def main():
    slug, fmt, out = sys.argv[1], sys.argv[2], Path(sys.argv[3])
    d = ROOT / f"i18n/{LG}/{slug}"
    lang = json.loads((ROOT / f"i18n/{LG}/lang.json").read_text(encoding="utf-8"))
    meta = {k: v.strip().strip('"') for k, v in (l.split(":", 1) for l in (d / "metadata.yaml").read_text(encoding="utf-8").splitlines() if ":" in l)}
    base = (ROOT / "i18n/_common/glossary.base.yaml").read_text(encoding="utf-8")
    gloss_rate = re.search(r"usd_per_jpy_rate:\s*(\d+)", base).group(1)
    rate_date = re.search(r'rate_date:\s*"([^"]+)"', base).group(1)
    images = ROOT / "books" / slug / "images"
    text0 = (d / "manuscript.md").read_text(encoding="utf-8").replace("{{FMT}}", fmt)
    lines = text0.split("\n")
    start = next(i for i, l in enumerate(lines) if l.startswith("## "))
    body = lines[start:]

    by_id = figure_files(images)
    problems, used, result, fig_idx = [], [], [], set()
    for line in body:
        m = MARK.match(line)
        if not m:
            result.append(line); continue
        label, fig, caption = m.group(1).strip(), m.group(2), m.group(3).strip()
        cands = by_id.get(fig, [])
        fname = FILE_OVERRIDE.get(fig) or (cands[0] if len(cands) == 1 else None)
        if fname is None or not (images / fname).exists():
            problems.append(f"{label} {fig}: 画像が決まらない（候補 {cands}）"); continue
        used.append(fname)
        alt = f"{label} {fig}: {caption}".replace("[", "［").replace("]", "］")
        src = f"images/_trim/{fname}" if (images / "_trim" / fname).exists() else f"images/{fname}"
        fig_idx.add(len(result)); result.append(f"![{alt}]({src})")
    marks = sum(1 for l in body if MARK.match(l))
    inline = 0
    for k, line in enumerate(result):
        if k in fig_idx:
            continue
        m2 = re.match(r"^!\[(.*)\]\(images/([^)_][^)]*)\)$", line)
        if m2:
            inline += 1
            if not (images / m2.group(2)).exists():
                problems.append(f"画像がない: {m2.group(2)}")
            stem = Path(m2.group(2)).stem
            for cand in (m2.group(2), stem + ".jpg"):
                if (images / "_web" / cand).exists():
                    result[k] = f"![{m2.group(1)}](images/_web/{cand})"; break
    text = "\n".join(result)
    text = text.replace("\\_", "_")
    text = re.sub(r"(?<![<(\"])" + URL, r"<\1>", text)

    exits = {}
    if fmt == "pdf":
        # 3つの出口：「1. …agenda?via=」で始まる番号付きの3項目と、その直前の ### 見出しを探す
        m1 = re.search(r"^1\. [^\n]*bontallc\.com/agenda\?via=[^\n]*$", text, flags=re.M)
        if not m1:
            problems.append("3つの出口が見つからない")
        else:
            h = text.rfind("\n### ", 0, m1.start()) + 1
            m3 = re.compile(r"\n3\. [^\n]*\n").search(text, m1.start())
            block_lines = text[m1.start():m3.end()].strip().split("\n")
            urls = []
            for bl in block_lines:
                us = re.findall(r"<(https?://[^>]+)>", bl)
                urls.append(us[0])
            files = ["qr-1.png", "qr-2.png", "qr-3.png"]
            exits = dict(zip(files, urls))
            qr = "\n".join(f'<figure><img src="_qr/{f}" alt=""><figcaption>{lab}</figcaption></figure>' for lab, f in zip(lang["qr_labels"], files))
            blk = f'\n```{{=html}}\n<div class="qr">\n{qr}\n</div>\n```\n'
            text = text[:h] + "::: exits\n\n" + text[h:m3.end()] + blk + "\n:::\n" + text[m3.end():]

    today = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))).date().isoformat()
    code = CODE[slug]
    mk = lang.get("mark", LG)
    agenda = f"https://bontallc.com/agenda?via={code}-{mk}-{fmt}"
    tamuro = f"https://tamuroreservation.vercel.app/?src={code}-{mk}-{fmt}"
    col = lang["colophon"].format(title=meta["title"], subtitle=meta["subtitle"], author=meta["author"], publisher=meta["publisher"],
                                   date=today, rate=gloss_rate, rate_date=rate_date, agenda=agenda, tamuro=tamuro)
    col = re.sub(r"(?<![<(\"])" + URL, r"<\1>", col)
    text = text.rstrip("\n") + "\n\n" + col
    out.write_text(text, encoding="utf-8")
    (out.parent / f"{fmt}.exits.json").write_text(json.dumps(exits, ensure_ascii=False))
    (out.parent / "figures.json").write_text(json.dumps({"marks": marks, "inline_images": inline, "used": used, "problems": problems}, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{LG}/{slug}/{fmt}: 図の印 {marks} / 原稿の画像 {inline} / 使った画像 {len(set(used))}")
    if problems:
        print("\n".join(problems)); sys.exit(2)


if __name__ == "__main__":
    main()
