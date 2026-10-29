// 英語版の表紙：文字なしの絵（nano.mjs cover）に、英題・副題・著者名を HTML で重ねて 1600×2560 で撮る。
//   node scripts/i18n/cover.mjs [slug…]   → i18n/en/<slug>/cover/cover.html・cover.png（文字は画像生成に描かせない）
import { chromium } from 'playwright';
import { readFileSync, writeFileSync } from 'node:fs';
import { resolve } from 'node:path';
import { pathToFileURL } from 'node:url';

const LOOK = {
  'hitori-de-mise': { lines: ['Running the Shop Alone,', 'with AI Beside Me'], size: 104, tag: 'A SOLO SHOP OWNER × AI', scrim: 'rgba(40,22,10,.78)', ink: '#fff6e6', sub: '#f6e3c4' },
  'uchi-no-mise': { lines: ['Our Bar,', 'Our Specs'], size: 190, tag: 'A SOLO SHOP OWNER × AI', scrim: 'rgba(6,18,46,.80)', ink: '#ffffff', sub: '#d6e4ff' },
};
const meta = (s) => Object.fromEntries(readFileSync(`i18n/en/${s}/metadata.yaml`, 'utf8').split('\n').filter(Boolean).map((l) => [l.split(':')[0], l.slice(l.indexOf(':') + 1).trim()]));

const slugs = process.argv.slice(2).length ? process.argv.slice(2) : Object.keys(LOOK);
const b = await chromium.launch();
for (const s of slugs) {
  const L = LOOK[s], m = meta(s);
  const html = `<!doctype html><meta charset="utf-8"><style>
  html,body{margin:0;width:1600px;height:2560px;overflow:hidden}
  .c{position:relative;width:1600px;height:2560px;background:url(art.png) center/cover no-repeat;font-family:'Baskerville','Georgia','Times New Roman',serif}
  .scrim{position:absolute;inset:0 0 auto 0;height:1250px;background:linear-gradient(180deg,${L.scrim} 0%,${L.scrim} 55%,rgba(0,0,0,0) 100%)}
  .t{position:absolute;left:110px;right:110px;top:150px;color:${L.ink};text-shadow:0 3px 18px rgba(0,0,0,.45)}
  h1{margin:0;font-weight:700;font-size:${L.size}px;line-height:1.06;letter-spacing:-1px}
  .sub{margin:56px 0 0;font-size:62px;line-height:1.28;color:${L.sub};font-style:italic;max-width:1300px}
  .au{margin:70px 0 0;font-size:72px;letter-spacing:6px;color:${L.ink};font-weight:600}
  .tag{position:absolute;left:110px;bottom:120px;font-family:'Helvetica Neue',Arial,sans-serif;font-size:46px;letter-spacing:10px;color:#fff;text-shadow:0 2px 14px rgba(0,0,0,.6)}
  </style><div class="c"><div class="scrim"></div><div class="t"><h1>${L.lines.join('<br>')}</h1><p class="sub">${m.subtitle}</p><p class="au">${m.author.toUpperCase()}</p></div><div class="tag">${L.tag}</div></div>`;
  const f = `i18n/en/${s}/cover/cover.html`;
  writeFileSync(f, html);
  const p = await b.newPage({ viewport: { width: 1600, height: 2560 } });
  await p.goto(pathToFileURL(resolve(f)).href);
  await p.waitForTimeout(500);
  await p.screenshot({ path: `i18n/en/${s}/cover/cover.png` });
  await p.close();
  console.log('ok', s);
}
await b.close();
