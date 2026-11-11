// カレンダー紹介シリーズの見出し画像（1280×670）を、その回の見本画像から作る。
//   node scripts/note-series-header.mjs <記事フォルダ NN>
import { chromium } from 'playwright';
import { readdirSync } from 'node:fs';
import { resolve } from 'node:path';
const nn = process.argv[2];
const dir = resolve(`articles/2026-11-calendar-series/${nn}`);
const imgs = readdirSync(`${dir}/images`).filter((f) => f.endsWith('.jpg')).sort();
const w = Math.floor((1280 - 80 - 24 * (imgs.length - 1)) / imgs.length);
const html = `<body style="margin:0;width:1280px;height:670px;background:#ece8e0;display:flex;gap:24px;padding:40px;box-sizing:border-box">${imgs.map((f) => `<div style="width:${w}px;height:590px;overflow:hidden;box-shadow:0 6px 18px rgba(0,0,0,.25);background:#fff"><img src="file://${dir}/images/${f}" style="width:100%;height:100%;object-fit:cover;object-position:left top;display:block"></div>`).join('')}</body>`;
const { writeFileSync } = await import('node:fs');
writeFileSync(`${dir}/header.html`, html);
const b = await chromium.launch({ channel: 'chrome' });
const p = await b.newPage({ viewport: { width: 1280, height: 670 } });
await p.goto(`file://${dir}/header.html`);
await p.waitForTimeout(1500);
await p.screenshot({ path: `${dir}/header.png` });
await b.close();
console.log(`${dir}/header.png`);
