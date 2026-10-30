"""ストアに貼る文言のページ books/store-copy.html を作る（外部通信なし・1枚の HTML）。
  python3 scripts/i18n/store-copy.py
材料：
  日本語の紹介文…いまストアに出ている文（2026-10-29 に Kindle・Google Play の公開ページから取得して books/store-copy.src.json に保存）
  英語の説明文・キーワード…i18n/en/<slug>/work/meta.json の窓の推敲版（下の EN_FIX で書き直した所だけ差し替え）
"""
import json, pathlib, html
import os
LG = os.environ.get('I18N_LANG', 'en')   # 言語コード（2文字）。i18n/<言語>/ を使う
ROOT = pathlib.Path(__file__).resolve().parents[2]
src = json.loads((ROOT / 'books/store-copy.src.json').read_text())
EN = {s: json.loads((ROOT / f'i18n/{LG}/{s}/work/meta.json').read_text()) for s in ('hitori-de-mise', 'uchi-no-mise')}
MD = {s: {k: v.strip() for k, v in (l.split(':', 1) for l in (ROOT / f'i18n/{LG}/{s}/metadata.yaml').read_text().splitlines() if ':' in l)} for s in EN}

JA = {
  'hitori-de-mise': dict(title='一人で店を回す、その横にAIが来た。', sub='話すと、やってくれる。想像以上に。', author='本多楽',
      kw=['個人店 AI活用', '飲食店 生成AI', '一人経営 仕事術', 'バイブコーディング', 'ChatGPT Gemini 実践', '飲食店 業務効率化', '個人事業主 AI入門'],
      kcat=['（いまの登録）Kindle本 › ビジネス・経済 › ビジネスライフ › 個人の成功論', '（ランキングに出ている）タイムマネジメント', '（候補・KDPの選択肢で名前を確認）コンピュータ・IT › 人工知能'],
      gcat=['ビジネス／経済', 'コンピュータ／人工知能']),
  'uchi-no-mise': dict(title='うちの店は、うちの仕様で', sub='19席のバー店主が、AIで予約システムから道具まで自分で作った記録', author='本多楽',
      kw=['飲食店 予約システム', 'MCPサーバー', 'バー 経営', 'AIで自作', '個人店 DX', '東中野 屯', 'Agendaシリーズ'],
      kcat=['（いまの登録）Kindle本 › ビジネス・経済 › 実践経営・リーダーシップ › 経営学', '（候補・KDPの選択肢で名前を確認）コンピュータ・IT › 人工知能', '（候補）ビジネス・経済 › 起業・開業'],
      gcat=['ビジネス／経済', 'コンピュータ／人工知能']),
}
# 英語の説明文の書き直し（前作・続編の題名を英題にそろえ、無料の言い方をストアごとに正しくする）
SEQ = {'hitori-de-mise': 'A sequel, *Built for Our Bar*, follows the building of a reservation system that customers\' own AIs can book through.'.replace('*', '')}
def en_desc(slug, store):
    d = EN[slug]['store_description'].strip()
    if slug == 'hitori-de-mise':
        d = d.replace('The book is free to read and free to share.\n\nA sequel, Uchi no mise wa, uchi no shiyō de, follows the building of a reservation system that customers\' own AIs can book through.',
                      '@@FREE@@\n\n' + SEQ[slug])
    else:
        d = d.replace('The book is free to read and free to redistribute. You can read it as a PDF, on note, or on Google Play.', '@@FREE@@')
    free = ('You can read this book for free as a PDF, on note, and on Google Play, and you are welcome to share the PDF. The Kindle edition carries the minimum price that the store requires.'
            if store == 'kindle' else
            'This book is free to read, and you are welcome to share it. It is also free as a PDF and on note.')
    assert '@@FREE@@' in d
    return d.replace('@@FREE@@', free)

EN_CAT = {
  'hitori-de-mise': dict(kcat=['Business & Money › Small Business & Entrepreneurship', 'Business & Money › Skills › Time Management', 'Computers & Technology › Artificial Intelligence & Semantics'],
                         gcat=['Business & Economics / Small Business', 'Computers / Artificial Intelligence']),
  'uchi-no-mise': dict(kcat=['Business & Money › Management & Leadership', 'Computers & Technology › Artificial Intelligence & Semantics', 'Business & Money › Small Business & Entrepreneurship'],
                       gcat=['Business & Economics / Small Business', 'Computers / Artificial Intelligence']),
}

def gp_clip(t):
    """Google Play の公開ページの説明文は、要約が続けて繰り返される。最初の本文だけを取る。"""
    first = t.split('\n', 1)[0]
    i = t.find(first, len(first))
    return (t[:i] if i > 0 else t).strip()

def fields(slug, lang, store):
    ja = JA[slug]; k = {'hitori-de-mise': ('k1', 'g1'), 'uchi-no-mise': ('k2', 'g2')}[slug]
    if lang == 'ja':
        title, sub, author = ja['title'], ja['sub'], ja['author']
        desc = src[k[0]] if store == 'kindle' else gp_clip(src[k[1]])
        kw = ja['kw']; cat = ja['kcat'] if store == 'kindle' else ja['gcat']
    else:
        title, sub, author = MD[slug]['title'], MD[slug]['subtitle'], MD[slug]['author']
        desc = en_desc(slug, store); kw = EN[slug]['keywords']; cat = EN_CAT[slug]['kcat'] if store == 'kindle' else EN_CAT[slug]['gcat']
    f = [dict(label='題名', text=title), dict(label='副題', text=sub), dict(label='著者', text=author)]
    f.append(dict(label='紹介文' if store == 'kindle' else '説明文', text=desc, multiline=True, limit=4000 if store == 'kindle' else None))
    if store == 'kindle':
        for i, w in enumerate(kw, 1):
            f.append(dict(label=f'キーワード {i}', text=w, limit=50, cand=(lang == 'ja')))
        f.append(dict(label='キーワード（7つを1行ずつ）', text='\n'.join(kw), multiline=True))
    f.append(dict(label='カテゴリの候補' if store == 'kindle' else 'ジャンルの候補', items=cat))
    return f

books = []
for slug, name in (('hitori-de-mise', '1冊目'), ('uchi-no-mise', '2冊目')):
    sec = []
    for lang, ln in (('ja', '日本語'), ('en', '英語')):
        for store, sn in (('kindle', 'Kindle'), ('gplay', 'Google Play')):
            sec.append(dict(id=f'{slug}-{lang}-{store}', lang=ln, store=sn, fields=fields(slug, lang, store)))
    books.append(dict(slug=slug, name=name, title=JA[slug]['title'], en=MD[slug]['title'], sections=sec))

PAGE = r'''<!doctype html>
<html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>ストアに貼る文言</title>
<style>
:root{--bg:#f6f4ef;--card:#fff;--ink:#1f2328;--mut:#6b7280;--line:#e5e1d8;--acc:#1f5eff;--ok:#0a7d33;--warn:#b45309}
@media (prefers-color-scheme:dark){:root{--bg:#15171a;--card:#1d2024;--ink:#e8e8e8;--mut:#9aa1ab;--line:#2d3138;--acc:#7aa2ff;--ok:#4cc27a;--warn:#f0a35e}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.7 -apple-system,"Hiragino Sans","Yu Gothic",system-ui,sans-serif}
header{padding:28px 20px 8px;max-width:960px;margin:0 auto}h1{margin:0 0 6px;font-size:22px}p.lead{margin:0;color:var(--mut)}
nav{position:sticky;top:0;background:var(--bg);border-bottom:1px solid var(--line);padding:10px 20px;z-index:2}
nav .in{max-width:960px;margin:0 auto;display:flex;flex-wrap:wrap;gap:6px 14px;align-items:center}nav b{font-size:13px}
nav a{color:var(--acc);text-decoration:none;font-size:13px;border:1px solid var(--line);border-radius:999px;padding:3px 10px;background:var(--card)}
main{max-width:960px;margin:0 auto;padding:8px 20px 80px}
h2.book{margin:34px 0 4px;font-size:19px}.en{color:var(--mut);font-size:13px;margin:0 0 6px}
section{background:var(--card);border:1px solid var(--line);border-radius:14px;margin:14px 0;padding:6px 18px 12px}
section h3{margin:12px 0 4px;font-size:16px}
.row{display:grid;grid-template-columns:150px 1fr auto;gap:6px 14px;padding:10px 0;border-top:1px solid var(--line);align-items:start}
.row:first-of-type{border-top:0}
.lab{font-size:13px;color:var(--mut)}.lab small{display:block;color:var(--warn)}
.txt{white-space:pre-wrap;word-break:break-word;margin:0}
.side{display:flex;flex-direction:column;align-items:flex-end;gap:4px;min-width:96px}
.cnt{font-size:12px;color:var(--mut);font-variant-numeric:tabular-nums}.cnt.over{color:#d92d20;font-weight:600}
button{font:inherit;font-size:13px;border:1px solid var(--acc);color:var(--acc);background:transparent;border-radius:8px;padding:5px 14px;cursor:pointer;min-height:34px}
button:hover{background:var(--acc);color:#fff}button.done{border-color:var(--ok);color:var(--ok)}button.done:hover{background:transparent}
ul.items{margin:0;padding:0;list-style:none}ul.items li{display:flex;gap:10px;justify-content:space-between;align-items:center;padding:3px 0}
.note{font-size:13px;color:var(--mut);margin:6px 0 0}
@media (max-width:640px){.row{grid-template-columns:1fr}.side{flex-direction:row;align-items:center;justify-content:space-between}}
</style></head><body>
<header><h1>ストアに貼る文言</h1>
<p class="lead">項目ごとの「コピー」を押して、KDP と Google Play Books の入力欄に貼ります。改行はそのまま残ります。このページは外部と通信しません。日本語の紹介文は、2026-10-29 時点でストアに出ている文と同じです（Kindle の日本語キーワード7つは、ストアの画面に出ないので窓の候補）。英語は窓の推敲版です。</p></header>
<nav><div class="in"><b>移動</b>__NAV__</div></nav>
<main>__BODY__
<p class="note">文字数は改行も1字に数えています。Kindle の上限（題名＋副題 200字・紹介文 4,000字・キーワード1つ 50字）は KDP の案内に基づく目安で、超えると赤くなります。カテゴリ・ジャンルの候補は、各ストアの選択肢の名前に合わせて選んでください。</p>
</main>
<script>
const DATA=__DATA__;
const esc=s=>s.replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));
const cnt=s=>Array.from(s).length;
async function copy(text,btn){
  try{await navigator.clipboard.writeText(text)}catch(e){const t=document.createElement('textarea');t.value=text;t.style.position='fixed';t.style.opacity='0';document.body.appendChild(t);t.select();document.execCommand('copy');t.remove()}
  const o=btn.textContent;btn.textContent='コピーしました';btn.classList.add('done');setTimeout(()=>{btn.textContent=o;btn.classList.remove('done')},1600)}
const nav=document.querySelector('nav .in'),main=document.querySelector('main');
let body='';
DATA.forEach(b=>{
  nav.insertAdjacentHTML('beforeend',`<a href="#${b.sections[0].id}">${b.name}</a>`);
  body+=`<h2 class="book">${b.name}　${esc(b.title)}</h2><p class="en">${esc(b.en)}</p>`;
  b.sections.forEach(s=>{
    nav.insertAdjacentHTML('beforeend',`<a href="#${s.id}">${s.lang}・${s.store}</a>`);
    body+=`<section id="${s.id}"><h3>${s.lang}　${s.store}</h3>`;
    s.fields.forEach((f,i)=>{
      if(f.items){body+=`<div class="row"><div class="lab">${f.label}</div><ul class="items">${f.items.map((t,j)=>`<li><span>${esc(t)}</span><button data-c="${s.id}|${i}|${j}">コピー</button></li>`).join('')}</ul><div></div></div>`;return}
      const n=cnt(f.text),over=f.limit&&n>f.limit;
      body+=`<div class="row"><div class="lab">${f.label}${f.cand?'<small>候補</small>':''}</div><p class="txt">${esc(f.text)}</p><div class="side"><span class="cnt${over?' over':''}">${n}字${f.limit?' / '+f.limit:''}</span><button data-c="${s.id}|${i}">コピー</button></div></div>`});
    body+='</section>'})});
main.insertAdjacentHTML('afterbegin',body);
const find=id=>DATA.flatMap(b=>b.sections).find(s=>s.id===id);
document.addEventListener('click',e=>{const b=e.target.closest('button[data-c]');if(!b)return;const [id,i,j]=b.dataset.c.split('|');const f=find(id).fields[+i];copy(j===undefined?f.text:f.items[+j].replace(/^（[^）]*）/,''),b)});
</script></body></html>'''
PAGE = PAGE.replace('__NAV__', '').replace('__BODY__', '').replace('__DATA__', json.dumps(books, ensure_ascii=False))
(ROOT / 'books/store-copy.html').write_text(PAGE)
print('ok', len(PAGE))
