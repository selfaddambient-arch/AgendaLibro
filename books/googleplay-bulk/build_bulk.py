#!/usr/bin/env python3
"""Google Play Books Partner Center 一括登録の準備を作る（冪等）。

出力（このフォルダ内のみ）:
  bulk_new.csv      新規の言語・本（Partner Center へ上げる表。列は Partner Center の列名）
  bulk_update.csv   上げ直し（1冊目の id・ms・bn）。Identifier に既存の GGKEY を入れる
  bulk_overview.csv 管理用の全件一覧（区分・ファイルの場所・検査用の長さ付き。Partner Center には上げない）
  files/epub|cover|pdf/<ID>.epub|_frontcover.png|.pdf   ファイルのコピー
  check_report.txt  検査結果
使い方: python3 build_bulk.py   （Google への接続は一切しない）
"""
import csv, json, re, shutil, sys, html
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
I18N = ROOT / "i18n"

LANGS = ["en", "id", "ms", "bn", "vi", "zh-CN", "zh-TW", "ko", "ne", "my", "th",
         "pt-BR", "es", "fr", "de", "hi", "fil", "it", "tr", "ru"]
BOOKS = [("01", "hitori-de-mise"), ("02", "uchi-no-mise")]
# 上げ直し（既存の Google Play 登録がある）= 1冊目の id・ms・bn
UPDATE = {("id", "01"), ("ms", "01"), ("bn", "01")}
# 既存の GGKEY（見つかったらここへ）。リポ内・AgendaHub を探したが見つからなかったので空
GGKEY = {("id", "01"): "", ("ms", "01"): "", ("bn", "01"): ""}
# ISO 639-2/B
ISO3 = {"en": "eng", "id": "ind", "ms": "may", "bn": "ben", "vi": "vie", "zh-CN": "chi",
        "zh-TW": "chi", "ko": "kor", "ne": "nep", "my": "bur", "th": "tha", "pt-BR": "por",
        "es": "spa", "fr": "fre", "de": "ger", "hi": "hin", "fil": "fil", "it": "ita",
        "tr": "tur", "ru": "rus"}

# 検査の上限（Google は公式に数値を出していない。保守的な目安）
TITLE_MAX = 255
SUBTITLE_MAX = 255
DESC_MAX = 4000
DESC_WARN = 3000  # 非公式情報の目安

COLS = ["Identifier", "Enable for Sale?", "Title", "Subtitle", "Book Format",
        "Contributor [Role]", "Language", "Description", "Publisher Name",
        "DRM Enabled?", "PDF Download Allowed?",
        "Price in USD", "Countries for USD Price"]


def read_yaml_flat(p):
    d = {}
    for line in p.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^(\w+):\s*(.*)$", line)
        if m:
            v = m.group(2).strip()
            if len(v) > 1 and v[0] == v[-1] and v[0] in "'\"":
                v = v[1:-1]
            d[m.group(1)] = v
    return d


def desc_of(lang, slug):
    w = I18N / lang / slug / "work"
    if (w / "store.json").exists():
        d = json.load(open(w / "store.json", encoding="utf-8"))
        return d["description"], d.get("gp_genres", []), d.get("keywords", [])
    d = json.load(open(w / "meta.json", encoding="utf-8"))  # en
    return d["store_description"], [], d.get("keywords", [])


def to_html(text):
    paras = [p.strip() for p in text.split("\n\n") if p.strip()]
    return "".join("<p>%s</p>" % html.escape(p, quote=False).replace("\n", "<br>") for p in paras)


def main():
    for sub in ("epub", "cover", "pdf"):
        d = HERE / "files" / sub
        if d.exists():
            for f in d.iterdir():
                if f.is_file():
                    f.unlink()  # このスクリプトが作った files/ 配下のみ作り直す
        d.mkdir(parents=True, exist_ok=True)

    new_rows, upd_rows, overview = [], [], []
    for lang in LANGS:
        mark = json.load(open(I18N / lang / "lang.json", encoding="utf-8")).get("mark", "")
        for no, slug in BOOKS:
            base = I18N / lang / slug
            meta = read_yaml_flat(base / "metadata.yaml")
            desc, genres, kws = desc_of(lang, slug)
            ident = f"bontaraku-{no}_{slug}_{lang}"
            src = {
                "epub": base / "build" / f"bontaraku-{no}_{slug}_{lang}_gp.epub",
                "pdf": base / "build" / f"bontaraku-{no}_{slug}_{lang}.pdf",
                "cover": base / "cover" / "cover.png",
            }
            dst = {
                "epub": HERE / "files" / "epub" / f"{ident}.epub",
                "pdf": HERE / "files" / "pdf" / f"{ident}.pdf",
                "cover": HERE / "files" / "cover" / f"{ident}_frontcover.png",
            }
            for k in src:
                if src[k].exists():
                    shutil.copy2(src[k], dst[k])
            is_upd = (lang, no) in UPDATE
            gg = GGKEY.get((lang, no), "")
            row = {
                "Identifier": gg if is_upd else ident,
                "Enable for Sale?": "Yes",
                "Title": meta["title"],
                "Subtitle": meta.get("subtitle", ""),
                "Book Format": "Digital",
                "Contributor [Role]": f"{meta['author']} [Author]",
                "Language": ISO3[lang],
                "Description": to_html(desc),
                "Publisher Name": meta.get("publisher", ""),
                "DRM Enabled?": "No",
                "PDF Download Allowed?": "Yes",
                "Price in USD": "0",
                "Countries for USD Price": "WORLD",
            }
            (upd_rows if is_upd else new_rows).append(row)
            overview.append({
                "区分": "上げ直し" if is_upd else "新規", "言語": lang, "本": no, "slug": slug,
                "リンクの印": mark, "ファイル名の基底": ident, "GGKEY": gg,
                "題名": meta["title"], "副題": meta.get("subtitle", ""),
                "説明文の長さ": len(desc), "ジャンル案(参考)": " / ".join(genres),
                "キーワード(参考)": " | ".join(kws),
                "epub": str(dst["epub"].relative_to(HERE)), "pdf": str(dst["pdf"].relative_to(HERE)),
                "cover": str(dst["cover"].relative_to(HERE)),
            })

    def write(name, rows, cols):
        with open(HERE / name, "w", encoding="utf-8-sig", newline="") as f:
            w = csv.DictWriter(f, fieldnames=cols)
            w.writeheader()
            w.writerows(rows)

    write("bulk_new.csv", new_rows, COLS)
    write("bulk_update.csv", upd_rows, COLS)
    write("bulk_overview.csv", overview, list(overview[0].keys()))
    return check(new_rows, upd_rows, overview)


def check(new_rows, upd_rows, overview):
    out, bad = [], 0

    def rep(ok, msg):
        nonlocal bad
        out.append(("OK  " if ok else "NG  ") + msg)
        bad += (not ok)

    rep(len(new_rows) + len(upd_rows) == 40, f"行数: 新規{len(new_rows)} + 上げ直し{len(upd_rows)} = {len(new_rows)+len(upd_rows)}（20言語×2冊=40）")
    rep(len(upd_rows) == 3, f"上げ直し {len(upd_rows)} 件（id・ms・bn の本1）")
    miss = [o["ファイル名の基底"] for o in overview
            for k in ("epub", "pdf", "cover") if not (HERE / o[k]).exists()]
    rep(not miss, f"ファイル存在（epub・pdf・表紙 各40）: 欠け {len(miss)} {miss[:5]}")
    zero = [o["epub"] for o in overview for k in ("epub", "pdf", "cover") if (HERE / o[k]).exists() and (HERE / o[k]).stat().st_size == 0]
    rep(not zero, f"0バイトのファイル {len(zero)}")
    allrows = new_rows + upd_rows
    rep(all(r["Price in USD"] == "0" and r["Countries for USD Price"] == "WORLD" for r in allrows), "価格 0・全世界（WORLD）")
    rep(all(r["DRM Enabled?"] == "No" for r in allrows), "DRM なし")
    req = ["Enable for Sale?", "Title", "Book Format", "Contributor [Role]", "Language", "Description", "Publisher Name"]
    empt = [(r["Title"], c) for r in allrows for c in req if not r[c].strip()]
    rep(not empt, f"必須列の空欄（Identifier 以外）: {empt[:3]}")
    emp_id = [r["Title"] for r in new_rows if not r["Identifier"].strip()]
    rep(not emp_id, f"新規の Identifier の空欄 {len(emp_id)}")
    rep(len({r["Identifier"] for r in new_rows}) == len(new_rows), "新規の Identifier に重複なし")
    gg_blank = sum(1 for r in upd_rows if not r["Identifier"].strip())
    out.append(f"WARN 上げ直しの GGKEY 空欄 {gg_blank}/3（代表がコピーして入れる）")
    tl = max(len(r["Title"]) for r in allrows)
    sl = max(len(r["Subtitle"]) for r in allrows)
    dl = max(o["説明文の長さ"] for o in overview)
    rep(tl <= TITLE_MAX, f"題名の最長 {tl}字（目安上限 {TITLE_MAX}）")
    rep(sl <= SUBTITLE_MAX, f"副題の最長 {sl}字（目安上限 {SUBTITLE_MAX}）")
    rep(dl <= DESC_MAX, f"説明文の最長 {dl}字（目安上限 {DESC_MAX}）")
    over = [o["ファイル名の基底"] for o in overview if o["説明文の長さ"] > DESC_WARN]
    out.append(f"INFO 説明文 {DESC_WARN}字超（非公式の目安）: {len(over)}件 {over[:6]}")
    out.append("NOTE Google は題名・説明文の字数上限を公式に公表していない。目安は保守的な仮置き")
    (HERE / "check_report.txt").write_text("\n".join(out) + "\n", encoding="utf-8")
    print("\n".join(out))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
