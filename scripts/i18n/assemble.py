#!/usr/bin/env python3
"""章ごとに書いた部品（work/part-NN.md）を、manuscript.md に組む。
  I18N_LANG=id python3 scripts/i18n/assemble.py <slug>…
窓が自分で訳すとき（API を使わないとき）の組み立て。部品は番号順に、空行1つでつなぐ。
"""
import os, sys, glob, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
LG = os.environ.get('I18N_LANG', 'en')
for slug in sys.argv[1:] or ['hitori-de-mise', 'uchi-no-mise']:
    d = ROOT / f'i18n/{LG}/{slug}'
    parts = sorted(glob.glob(str(d / 'work/part-*.md')))
    if not parts:
        continue
    text = '\n\n'.join(pathlib.Path(p).read_text(encoding='utf-8').strip('\n') for p in parts) + '\n'
    (d / 'manuscript.md').write_text(text, encoding='utf-8')
    print(LG, slug, len(parts), '部品 →', len(text), '字')
