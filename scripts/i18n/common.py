"""多言語の共通部品：言語設定と用語集の読み込み。"""
import json, pathlib, yaml
ROOT = pathlib.Path(__file__).resolve().parents[2]


def load_lang(lg):
    return json.loads((ROOT / f'i18n/{lg}/lang.json').read_text(encoding='utf-8'))


def load_glossary(lg):
    """為替は i18n/_common/glossary.base.yaml。terms／forbid は i18n/<言語>/glossary.yaml と glossary.add.yaml をまとめる（同じ ja の語は後のファイルが勝つ）。"""
    g = yaml.safe_load((ROOT / 'i18n/_common/glossary.base.yaml').read_text(encoding='utf-8'))
    terms, forbid = {}, []
    for name in ('glossary.yaml', 'glossary.add.yaml'):
        p = ROOT / f'i18n/{lg}/{name}'
        if not p.exists():
            continue
        y = yaml.safe_load(p.read_text(encoding='utf-8')) or {}
        for t in y.get('terms', []) or []:
            terms[t['ja']] = t
        forbid += y.get('forbid', []) or []
    g['terms'] = list(terms.values()); g['forbid'] = forbid
    return g
