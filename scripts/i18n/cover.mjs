// 多言語版の表紙：英語版で作った文字なしの絵（i18n/en/<slug>/cover/art.png）に、その言語の題名・副題・著者名を HTML で重ねて 1600×2560 で撮る。
//   I18N_LANG=id node scripts/i18n/cover.mjs [slug…]   → i18n/<言語>/<slug>/cover/cover.html・cover.png
// 文字は画像生成に描かせない（HTML の文字なので、書体が合えば文字化けしない）。
// 題名の行分けと大きさは i18n/<言語>/<slug>/cover/cover.json：{"lines":["…","…"],"size":104,"tag":"…","subsize":62}
import { chromium } from 'playwright';
import { readFileSync, writeFileSync, existsSync } from 'node:fs';
import { resolve } from 'node:path';
import { pathToFileURL } from 'node:url';

const LG = process.env.I18N_LANG || 'en'; // 言語コード（2文字）。i18n/<言語>/ を使う
const LOOK = {
  'hitori-de-mise': { scrim: 'rgba(40,22,10,.78)', ink: '#fff6e6', sub: '#f6e3c4' },
  'uchi-no-mise': { scrim: 'rgba(6,18,46,.80)', ink: '#ffffff', sub: '#d6e4ff' },
};
const lang = JSON.parse(readFileSync(`i18n/${LG}/lang.json`, 'utf8'));
const meta = (s) => Object.fromEntries(readFileSync(`i18n/${LG}/${s}/metadata.yaml`, 'utf8').split('\n').filter((l) => l.includes(':')).map((l) => [l.split(':')[0], l.slice(l.indexOf(':') + 1).trim().replace(/^"|"$/g, '')]));

const slugs = process.argv.slice(2).length ? process.argv.slice(2) : Object.keys(LOOK);
const b = await chromium.launch();
for (const s of slugs) {
  const L = LOOK[s], m = meta(s);
  const cj = JSON.parse(readFileSync(`i18n/${LG}/${s}/cover/cover.json`, 'utf8'));
  const art = pathToFileURL(resolve(`i18n/en/${s}/cover/art.png`)).href;
  const html = `<!doctype html><meta charset="utf-8"><style>
  html,body{margin:0;width:1600px;height:2560px;overflow:hidden}
  .c{position:relative;width:1600px;height:2560px;background:url(${art}) center/cover no-repeat;font-family:${lang.font}}
  .scrim{position:absolute;inset:0 0 auto 0;height:1250px;background:linear-gradient(180deg,${L.scrim} 0%,${L.scrim} 55%,rgba(0,0,0,0) 100%)}
  .t{position:absolute;left:110px;right:110px;top:150px;color:${L.ink};text-shadow:0 3px 18px rgba(0,0,0,.45)}
  h1{margin:0;font-weight:700;font-size:${cj.size}px;line-height:${cj.lh || 1.1};letter-spacing:${cj.ls ?? -1}px}
  .sub{margin:56px 0 0;font-size:${cj.subsize || 62}px;line-height:1.35;color:${L.sub};${cj.italic === false ? '' : 'font-style:italic;'}max-width:1300px}
  .au{margin:70px 0 0;font-size:${cj.ausize || 72}px;letter-spacing:6px;color:${L.ink};font-weight:600}
  .tag{position:absolute;left:110px;bottom:120px;font-size:46px;letter-spacing:${cj.tagls ?? 10}px;color:#fff;text-shadow:0 2px 14px rgba(0,0,0,.6)}
  </style><div class="c"><div class="scrim"></div><div class="t"><h1>${cj.lines.join('<br>')}</h1><p class="sub">${m.subtitle}</p><p class="au">${cj.author || m.author.toUpperCase()}</p></div><div class="tag">${cj.tag}</div></div>`;
  const f = `i18n/${LG}/${s}/cover/cover.html`;
  writeFileSync(f, html);
  const p = await b.newPage({ viewport: { width: 1600, height: 2560 } });
  await p.goto(pathToFileURL(resolve(f)).href);
  await p.waitForTimeout(600);
  await p.screenshot({ path: `i18n/${LG}/${s}/cover/cover.png` });
  await p.close();
  console.log('ok', LG, s);
}
await b.close();
