#!/usr/bin/env bash
# レビューを agy -p（Gemini）に出す：章ごとの i18n/<言語>/<slug>/review/<名前>.md を渡し、返事を <名前>.gemini.md に置く。
#   I18N_LANG=id bash scripts/i18n/review-agy.sh [slug]
# 枠が尽きたら（エラーの文字が返ったら）止まる。そのとき窓が Gemini API に切り替える。
cd "$(dirname "$0")/../.."
LG="${I18N_LANG:-en}"
MODEL="${AGY_MODEL:-gemini-3.8-flash-high}"
NAME=$(python3 -c "import json;print(json.load(open('i18n/$LG/lang.json'))['name'])")
PRE="You are a careful bilingual reviewer (Japanese and $NAME). The text below is one part of a Japanese nonfiction book (a solo bar owner using AI) and its $NAME translation, made by AI. Review the translation. Reply in Japanese, as a numbered list only. Each item: the type (① 意味の取り違え ② 不自然な表現 ③ その言語の読者に伝わらない箇所), the exact quoted passage of the translation, the problem in one line, and a suggested fix in $NAME. Also report any heading/number mismatch, changed fact or number, lost sentence, or leftover Japanese. Do not rewrite the whole text. If there is nothing to report in a category, say so briefly. Do not report the yen-to-US-dollar estimates in parentheses, the translator's short notes in italics, or the title choice: those are decided by the author. Do not use any tools; just read and answer."
for slug in ${1:-hitori-de-mise uchi-no-mise}; do
  for f in i18n/$LG/$slug/review/[0-9]*.md; do
    case "$f" in *.gemini.md|*.chatgpt.md) continue;; esac
    out="${f%.md}.gemini.md"
    if [ -s "$out" ]; then echo "skip $out"; continue; fi
    echo "== $f"
    agy -p "$PRE

$(cat "$f")" --model "$MODEL" --mode plan > "$out.tmp" 2>"$out.err"
    rc=$?
    if [ $rc -ne 0 ] || [ ! -s "$out.tmp" ] || grep -qi "quota\|error:" "$out.tmp" "$out.err" 2>/dev/null && [ $(wc -c < "$out.tmp") -lt 400 ]; then
      echo "NG rc=$rc $(head -c 200 "$out.err" "$out.tmp" | tr '\n' ' ')"; rm -f "$out.tmp"; exit 3
    fi
    mv "$out.tmp" "$out"; rm -f "$out.err"
    echo "ok $(wc -c < "$out") bytes"
  done
done
echo ALLDONE
