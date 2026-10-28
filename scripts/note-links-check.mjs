// 公開した記事の「前の回／次の回」のリンクが、正しい記事に飛び、200 で開くかを確かめる（未ログイン）。
//   BOOK=hitori-de-mise node scripts/note-links-check.mjs
import { chromium } from 'playwright';
import { readFileSync } from 'node:fs';
const SLUG = process.env.BOOK || 'uchi-no-mise';
const drafts = JSON.parse(readFileSync(`books/${SLUG}/note/drafts.json`, 'utf8'));
const slugs = Object.keys(drafts);
const b = await chromium.launch();
const ctx = await b.newContext({ locale: 'ja-JP' });
const p = await ctx.newPage();
let bad = 0, n = 0;
for (const [i, s] of slugs.entries()) {
  await p.goto(`https://note.com/bontallc/n/${drafts[s]}`, { waitUntil: 'load' });
  await p.waitForTimeout(2000);
  const links = await p.$$eval('.note-common-styles__textnote-body a', (as) => as.map((a) => [a.textContent.trim(), a.href]));
  const prev = links.filter(([t]) => t.startsWith('◀ 前の章')), next = links.filter(([t]) => t.startsWith('次の章 ▶'));
  const exp = [];
  if (i > 0) exp.push([prev, drafts[slugs[i - 1]], '前']);
  else if (prev.length) { console.log(s, '先頭なのに前のリンクがある'); bad++; }
  if (i + 1 < slugs.length) exp.push([next, drafts[slugs[i + 1]], '次']);
  else if (next.length) { console.log(s, '最後なのに次のリンクがある'); bad++; }
  for (const [arr, key, kind] of exp) {
    n++;
    const href = arr[0]?.[1] || '';
    const r = href ? await ctx.request.get(href) : null;
    const ok = href.includes('/n/' + key) && r?.status() === 200;
    if (!ok) { bad++; console.log('NG', s, kind, href, r?.status()); }
  }
}
console.log(`${SLUG}: 前後のリンク ${n} 本を確認、不一致 ${bad}`);
await b.close();
process.exit(bad ? 1 : 0);
