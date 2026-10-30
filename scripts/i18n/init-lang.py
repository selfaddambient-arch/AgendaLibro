#!/usr/bin/env python3
"""新しい言語の置き場を作る（サブエージェントが最初に1回だけ流す）。
  python3 scripts/i18n/init-lang.py <言語コード> <リンクの印の言語（2文字）>
作るもの（すべて i18n/<言語>/ の中）：
  lang.json（雛形・TODO を埋める）、glossary.add.yaml（雛形）、<slug>/{work,cover,review,build}/、
  <slug>/work/source.ja.md（英語版の前処理済みの日本語。リンクの印だけ b?-<印>-{{FMT}} に置き換え）
"""
import sys, json, re, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
lg, mark = sys.argv[1], sys.argv[2]
assert re.fullmatch(r'[a-z]{2}', mark), '印の言語は英小文字2文字'
d = ROOT / f'i18n/{lg}'
d.mkdir(exist_ok=True)
for slug, code in (('hitori-de-mise', 'b1'), ('uchi-no-mise', 'b2')):
    for sub in ('work', 'cover', 'review', 'build'):
        (d / slug / sub).mkdir(parents=True, exist_ok=True)
    src = (ROOT / f'i18n/en/{slug}/work/source.ja.md').read_text(encoding='utf-8')
    (d / slug / 'work/source.ja.md').write_text(src.replace(f'{code}-en-', f'{code}-{mark}-'), encoding='utf-8')
if not (d / 'lang.json').exists():
    tpl = json.loads((ROOT / 'i18n/id/lang.json').read_text(encoding='utf-8'))
    tpl.update(code=lg, bcp47='TODO', name='TODO（その言語の自称）', ja_name='TODO（日本語での言語名）', mark=mark, kindle='TODO（KDP 対応なら true）',
               fig_label='TODO', number_style='TODO（en／dot／space）', cjk=False, ocr_langs=['TODO（Vision 対応なら。無ければこの行を消す）'], font='TODO（その文字が正しく出る書体）',
               toc_title='TODO', qr_labels=['TODO', 'TODO', 'TODO'], colophon='TODO（id/lang.json の colophon を、その言語に訳す）')
    (d / 'lang.json').write_text(json.dumps(tpl, ensure_ascii=False, indent=1), encoding='utf-8')
if not (d / 'glossary.add.yaml').exists():
    base = (ROOT / 'i18n/id/glossary.yaml').read_text(encoding='utf-8')
    base = re.sub(r'to: "[^"]*"', 'to: "TODO"', base)
    base = re.sub(r'(usd_per_jpy_rate|rate_date):.*\n', '', base)
    (d / 'glossary.add.yaml').write_text('# TODO：to を埋める（手帳の名前は AgendaHub の辞書の hub.product.*.nick に合わせる）。forbid も、その言語で揺れやすい綴りに直す\n' + base, encoding='utf-8')
print('作った：', d)
