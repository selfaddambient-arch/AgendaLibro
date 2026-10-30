"""英訳の機械ゲート（日本語版との構造の一致・リンクの印・円→ドル・用語の揺れ）。
  python3 scripts/i18n/gate.py [slug…]     終了コード 0＝すべて合格
"""
import sys, re, json, pathlib, yaml
import os
LG = os.environ.get('I18N_LANG', 'en')   # 言語コード（2文字）。i18n/<言語>/ を使う
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from common import load_glossary, load_lang
GLOSS = load_glossary(LG)
LANG = load_lang(LG)
FIG = LANG.get('fig_label', 'Figure')
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


def num(s, style):
    s = s.strip().replace('\u00a0', ' ').replace('\u202f', ' ')
    if style == 'en':
        return float(s.replace(',', '').replace(' ', ''))
    if style == 'dot':
        return float(s.replace('.', '').replace(' ', '').replace(',', '.'))
    return float(s.replace(' ', '').replace('.', '').replace(',', '.'))  # space


YEN = r'¥\s?(\d{1,3}(?:[.,\u00a0\u202f ]\d{3})+(?:[.,]\d+)?|\d+(?:[.,]\d+)?)(?!\d|[.,]\d)'


def currency_checks(slug, text):
    """円の金額：すべて ¥ で書き、直後の括弧に $ の概算がある。金額の並びと米ドルの並びは英語版と一致（数値で比べる）。"""
    style = LANG.get('number_style', 'en'); res = {}
    en = (ROOT / f'i18n/en/{slug}/manuscript.md').read_text()
    def seqs(t, st):
        yens = [num(m.group(1), st) for m in re.finditer(YEN, t)]
        usds = [num(m.group(1), st) for m in re.finditer(r'\$\s?(\d{1,3}(?:[.,\u00a0\u202f ]\d{3})+(?:[.,]\d+)?|\d+(?:[.,]\d+)?)', t)]
        return yens, usds
    ey, eu = seqs(en, 'en'); ty, tu = seqs(text, style)
    close = lambda a, b: len(a) == len(b) and all(abs(x - y) <= 1e-6 * max(1, abs(x)) for x, y in zip(a, b))
    res['円の金額の並びが英語版と一致'] = close(ty, ey) or (len(ty), len(ey))
    res['米ドルの概算の並びが英語版と一致'] = close(tu, eu) or (len(tu), len(eu))
    lone = [m.group(0) for m in re.finditer(YEN + r'(?:\s*[–—-]\s*¥\s?[\d.,]*\d(?![\d.,]*\d))?(?!\s*[–—-]\s*¥)(?!\s*\([^)]*\$)', text)]
    res['円の金額すべてに米ドルの括弧'] = (not lone) or lone[:5]
    res['円の金額の数（参考）'] = len(ty)
    return res


def check(slug):
    d = ROOT / f'i18n/{LG}/{slug}'
    ja = (d / 'work/source.ja.md').read_text(); en = (d / 'manuscript.md').read_text()
    code = CODE[slug]; res = {}
    res['見出し数が一致'] = heads(ja) == heads(en) or (heads(ja), heads(en))
    res['画像行の数が一致'] = len(re.findall(r'^!\[', ja, flags=re.M)) == len(re.findall(r'^!\[', en, flags=re.M)) or (len(re.findall(r'^!\[', ja, flags=re.M)), len(re.findall(r'^!\[', en, flags=re.M)))
    jf = len(re.findall(r'^【図', ja, flags=re.M)); ef = len(re.findall(r'^【', en, flags=re.M))
    res['図の印の数が一致'] = jf == ef or (jf, ef)
    jc = len(re.findall(r'^図\d', ja, flags=re.M)); ec = len(re.findall(r'^' + re.escape(FIG) + r'\s?\d', en, flags=re.M))
    res['図の行の数が一致'] = jc == ec or (jc, ec)
    jt = len(re.findall(r'^\|', ja, flags=re.M)); et = len(re.findall(r'^\|', en, flags=re.M))
    res['表の行の数が一致'] = jt == et or (jt, et)
    ju, eu = urls(ja), urls(en)
    res['リンクの数が一致'] = len(ju) == len(eu) or (len(ju), len(eu))
    res['リンクの中身が一致'] = ([u.rstrip('.,;') for u in ju] == [u.rstrip('.,;') for u in eu]) or sorted(set(ju) ^ set(eu))[:6]
    marks = re.findall(r'[?&](?:src|via)=([^\s&)）]+)', en)
    bad = [m for m in marks if m != f"{code}-{LANG.get('mark', LG)}-{{{{FMT}}}}"]
    res['リンクの印が本-言語-形式'] = (not bad and len(marks) == len(re.findall(r'[?&](?:src|via)=', ja))) or bad
    res['{{FMT}} の数が一致'] = ja.count('{{FMT}}') == en.count('{{FMT}}') or (ja.count('{{FMT}}'), en.count('{{FMT}}'))
    res.update(currency_checks(slug, en))
    res['補足の印が残っていない'] = ('⟦' not in en and '⟧' not in en) or 'あり'
    res['日本語の文字が残っていない（図の注を除く）'] = True
    cjk = [ln.strip()[:60] for ln in en.split('\n') if re.search(r'[ぁ-ヺー々一-鿿]', ln.replace('屯', ''))]
    res['日本語の文字が残っていない（図の注を除く）'] = True if LANG.get('cjk') else ((len(cjk) == 0) or {'行数': len(cjk), '例': cjk[:4]})
    # 用語の揺れ
    fb = []
    for f in GLOSS['forbid']:
        for b in f['bad']:
            if re.search(r'(?<![\w])' + re.escape(b) + r'(?![\w])', en):
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


def file_text_urls(path):
    """仕上がったファイル（PDF・EPUB）の本文と、リンク先の URL を全部読む。"""
    import zipfile
    if path.suffix == '.epub':
        z = zipfile.ZipFile(path)
        txt = ''.join(z.read(n).decode('utf8', 'ignore') for n in z.namelist() if n.endswith(('.xhtml', '.html', '.opf', '.ncx')))
        return txt
    import pymupdf
    d = pymupdf.open(path)
    return ''.join(p.get_text().replace('\n', '') for p in d) + ' ' + ' '.join(str(l.get('uri', '')) for p in d for l in p.get_links())


def cover_check(slug):
    """表紙の画像を Apple Vision で読み、題名・副題・著者名が文字化けなく出ているか照合する。"""
    import subprocess, difflib, unicodedata
    res = {}
    cover = ROOT / f'i18n/{LG}/{slug}/cover/cover.png'
    if not cover.exists():
        return {'表紙の画像がある': False}
    langs = LANG.get('ocr_langs')
    if not langs:
        res['表紙の文字（Vision 非対応の言語：目視で確認）'] = True
        return res
    out = subprocess.run(['swift', str(ROOT / 'scripts/i18n/ocr-cover.swift'), str(cover), ','.join(langs)], capture_output=True, text=True).stdout
    norm = lambda s: ''.join(c for c in unicodedata.normalize('NFKC', s).lower() if c.isalnum()).replace('l', 'i').replace('1', 'i').replace('0', 'o')  # AI を Al と読む等の取り違えは同じ字とみなす
    got = norm(out)
    cj = json.load(open(ROOT / f'i18n/{LG}/{slug}/cover/cover.json'))
    md = {k: v.strip().strip('"') for k, v in (l.split(':', 1) for l in open(ROOT / f'i18n/{LG}/{slug}/metadata.yaml').read().splitlines() if ':' in l)}
    for label, exp in (('題名', ''.join(cj['lines'])), ('副題', md['subtitle']), ('著者名', cj.get('author') or md['author'])):
        e = norm(exp)
        m = difflib.SequenceMatcher(None, e, got).find_longest_match(0, len(e), 0, len(got))
        ratio = m.size / max(1, len(e))
        res[f'表紙の{label}が読める（一致 {ratio:.0%}）'] = ratio >= 0.85 or f'読めた文字: {out[:120]!r}'
    return res


def build_checks(slug):
    """組版の機械ゲート：epubcheck・リンクの印・{{FMT}}・図の数・見出しの数（日本語版の EPUB と比べる）。"""
    import subprocess, zipfile
    code = CODE[slug]; res = {}
    ja_epub = next(iter(sorted((ROOT / f'books/{slug}/build').glob('*.epub'))), None)
    def counts(epub):
        z = zipfile.ZipFile(epub); x = ''.join(z.read(n).decode('utf8', 'ignore') for n in z.namelist() if n.endswith('.xhtml') and 'nav' not in n)
        return dict(img=len(re.findall(r'<img ', x)), h=len(re.findall(r'<h[1-6][ >]', x)))
    jc = counts(ja_epub) if ja_epub else None
    for f in build_files(slug):
        fmt = 'pdf' if f.suffix == '.pdf' else ('kindle' if f.stem.endswith('_kindle') else 'gp')
        txt = file_text_urls(f)
        P = r'b\d-[a-z]{2,3}-(?:pdf|kindle|gp)'
        marks = re.findall(r'[?&](?:src|via)=(' + P + ')', txt)
        malformed = re.findall(r'[?&](?:src|via)=(?!' + P + r')[^\s]{0,24}', txt)
        want = f"{code}-{LANG.get('mark', LG)}-{fmt}"
        bad = sorted({m for m in marks if m != want} | set(malformed))
        res[f'{f.name}：リンクの印がすべて {want}（{len(marks)}件）'] = (not bad and len(marks) >= 2) or bad or '印が見つからない'
        res[f'{f.name} に {{{{FMT}}}} が0件'] = (txt.count('{{FMT}}') + txt.count('%7B%7BFMT%7D%7D')) == 0 or '残っている'
        if f.suffix == '.epub':
            r = subprocess.run(['epubcheck', str(f)], capture_output=True, text=True)
            m = re.search(r'(\d+) 件の致命的エラー / (\d+) 件のエラー', r.stdout + r.stderr) or re.search(r'(\d+) fatal error\(s\) / (\d+) error\(s\)', r.stdout + r.stderr)
            res[f'{f.name}：epubcheck エラー0'] = (m and m.group(1) == '0' and m.group(2) == '0') or (m.groups() if m else r.stdout[-200:])
            c = counts(f)
            if jc:
                res[f'{f.name}：図の数が日本語版の EPUB と一致（{c["img"]}／{jc["img"]}）'] = c['img'] == jc['img'] or (c['img'], jc['img'])
                res[f'{f.name}：見出しの数が日本語版の EPUB と一致（{c["h"]}／{jc["h"]}）'] = abs(c['h'] - jc['h']) <= 2 or (c['h'], jc['h'])
    res.update(cover_check(slug))
    return res


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
        r.update(build_checks(s))
        for k, v in r.items():
            ok = v is True or k.endswith('（参考）') or isinstance(v, int)
            if not ok: fail += 1
            print(('OK  ' if ok else 'NG  ') + k, '' if v is True else v)
    sys.exit(1 if fail else 0)
