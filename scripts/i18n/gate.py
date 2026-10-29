"""英訳の機械ゲート（日本語版との構造の一致・リンクの印・円→ドル・用語の揺れ）。
  python3 scripts/i18n/gate.py [slug…]     終了コード 0＝すべて合格
"""
import sys, re, json, pathlib, yaml
import os
LG = os.environ.get('I18N_LANG', 'en')   # 言語コード（2文字）。i18n/<言語>/ を使う
ROOT = pathlib.Path(__file__).resolve().parents[2]
GLOSS = yaml.safe_load(open(ROOT / f'i18n/{LG}/glossary.yaml'))
CODE = {'hitori-de-mise': 'b1', 'uchi-no-mise': 'b2'}


def strip_fences(t):
    return re.sub(r'```.*?```', '', t, flags=re.S)


def heads(t):
    t = strip_fences(t); out = {}
    for ln in t.split('\n'):
        m = re.match(r'^(#{1,6}) ', ln)
        if m: out[len(m.group(1))] = out.get(len(m.group(1)), 0) + 1
    return out


def urls(t):
    return sorted(u.rstrip(').,;') for u in re.findall(r"https?://[A-Za-z0-9._~:/?#\[\]@!$&'()*+,;=%{}-]+", t))


def check(slug):
    d = ROOT / f'i18n/{LG}/{slug}'
    ja = (d / 'work/source.ja.md').read_text(); en = (d / 'manuscript.md').read_text()
    code = CODE[slug]; res = {}
    res['見出し数が一致'] = heads(ja) == heads(en) or (heads(ja), heads(en))
    res['画像行の数が一致'] = len(re.findall(r'^!\[', ja, flags=re.M)) == len(re.findall(r'^!\[', en, flags=re.M)) or (len(re.findall(r'^!\[', ja, flags=re.M)), len(re.findall(r'^!\[', en, flags=re.M)))
    jf = len(re.findall(r'^【図', ja, flags=re.M)); ef = len(re.findall(r'^【Figure ', en, flags=re.M))
    res['図の印の数が一致'] = jf == ef or (jf, ef)
    jc = len(re.findall(r'^図\d', ja, flags=re.M)); ec = len(re.findall(r'^Figure \d', en, flags=re.M))
    res['図の行の数が一致'] = jc == ec or (jc, ec)
    jt = len(re.findall(r'^\|', ja, flags=re.M)); et = len(re.findall(r'^\|', en, flags=re.M))
    res['表の行の数が一致'] = jt == et or (jt, et)
    ju, eu = urls(ja), urls(en)
    res['リンクの数が一致'] = len(ju) == len(eu) or (len(ju), len(eu))
    res['リンクの中身が一致'] = ([u.rstrip('.,;') for u in ju] == [u.rstrip('.,;') for u in eu]) or sorted(set(ju) ^ set(eu))[:6]
    marks = re.findall(r'[?&](?:src|via)=([^\s&)）]+)', en)
    bad = [m for m in marks if m != f'{code}-{LG}-{{{{FMT}}}}']
    res['リンクの印が本-言語-形式'] = (not bad and len(marks) == len(re.findall(r'[?&](?:src|via)=', ja))) or bad
    res['{{FMT}} の数が一致'] = ja.count('{{FMT}}') == en.count('{{FMT}}') or (ja.count('{{FMT}}'), en.count('{{FMT}}'))
    plain = re.sub(r'\(about \$[\d.,]+(?:–\$[\d.,]+)?\)', '', en)
    amounts = re.findall(r'¥[\d,]+(?:\.\d+)?', en)
    n = r'(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?(?![\d,]*\d)'
    noUSD = [m.group(0) for m in re.finditer(r'¥' + n + r'(?:\s*[–—-]\s*¥' + n + r')?(?! \(about \$)(?!\s*[–—-]\s*¥)', en)]
    res['円の金額すべてに米ドルの概算'] = (not noUSD) or noUSD[:5]
    res['円の金額の数（参考）'] = len(amounts)
    res['補足の印が残っていない'] = ('⟦' not in en and '⟧' not in en) or 'あり'
    res['日本語の文字が残っていない（図の注を除く）'] = True
    cjk = [ln.strip()[:60] for ln in en.split('\n') if re.search(r'[ぁ-ヺー々一-鿿]', ln.replace('屯', ''))]
    res['日本語の文字が残っていない（図の注を除く）'] = (len(cjk) == 0) or {'行数': len(cjk), '例': cjk[:4]}
    # 用語の揺れ
    fb = []
    for f in GLOSS['forbid']:
        for b in f['bad']:
            if re.search(r'(?<![A-Za-z])' + re.escape(b) + r'(?![A-Za-z])', en):
                fb.append(b)
    res['用語の揺れ0'] = (not fb) or fb
    miss = []
    for g in GLOSS['terms']:
        if g['ja'] in ('第N章', '図', '手帳', 'MCP', '2軒目手帳') : continue
        if g['ja'] in ja and g['to'].lower() not in en.lower():
            miss.append(g['ja'] + '→' + g['to'])
    res['用語集の語が訳文にある'] = (not miss) or miss
    # 数字（日本語にあって訳文に無い数）。万・漢数字を使う箇所は目で見る参考値
    jn = set(re.findall(r'\d[\d,.]*\d|\d', re.sub(r'https?://\S+', '', ja)))
    en_plain = re.sub(r'https?://\S+', '', en).replace(',', '')
    miss_n = sorted(n for n in jn if n.replace(',', '') not in en_plain)
    res['日本語の数字が訳文にない（参考）'] = miss_n[:40]
    return res


def build_files(slug):
    d = ROOT / f'i18n/{LG}/{slug}/build'
    return sorted(f for f in d.glob('*') if f.suffix in ('.pdf', '.epub')) if d.exists() else []


def fmt_leftover(path):
    """仕上がったファイル（PDF・EPUB）の全文を読み、{{FMT}} が残っていないか数える。"""
    import zipfile
    if path.suffix == '.epub':
        z = zipfile.ZipFile(path)
        txt = ''.join(z.read(n).decode('utf8', 'ignore') for n in z.namelist() if n.endswith(('.xhtml', '.html', '.opf', '.ncx', '.css', '.txt')))
    else:
        import pymupdf
        d = pymupdf.open(path); txt = ''.join(p.get_text() for p in d)
        txt += ''.join(str(l.get('uri', '')) for p in d for l in p.get_links())
    return txt.count('{{FMT}}') + txt.count('%7B%7BFMT%7D%7D')


if __name__ == '__main__':
    slugs = sys.argv[1:] or list(CODE)
    fail = 0
    for s in slugs:
        r = check(s); print('==', s)
        for f in build_files(s):
            n = fmt_leftover(f); r[f'{f.name} に {{{{FMT}}}} が0件'] = (n == 0) or n
        for k, v in r.items():
            ok = v is True or k.endswith('（参考）') or isinstance(v, int)
            if not ok: fail += 1
            print(('OK  ' if ok else 'NG  ') + k, '' if v is True else v)
    sys.exit(1 if fail else 0)
