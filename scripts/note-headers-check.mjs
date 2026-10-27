// 8か所（下書き7本＋マガジン）の見出し画像が設定済みかを、開き直して実測する。
//   node scripts/note-headers-check.mjs <出力ディレクトリ>   （各ページの上部を <slug>.png に保存）
import { chromium } from 'playwright';
import { readFileSync } from 'node:fs';
const out = process.argv[2];
const drafts = JSON.parse(readFileSync('books/uchi-no-mise/note/drafts.json', 'utf8'));
const b = await chromium.launch({ headless: false, channel: 'chrome', ignoreDefaultArgs: ['--enable-automation'], args: ['--disable-blink-features=AutomationControlled'] });
const c = await b.newContext({ storageState: 'secrets/note-state.json', locale: 'ja-JP', viewport: { width: 1280, height: 900 } });
const p = await c.newPage();
let ok = 0;
for (const [slug, key] of Object.entries(drafts)) {
  await p.goto(`https://editor.note.com/notes/${key}/edit/`);
  await p.getByPlaceholder('記事タイトル').waitFor({ timeout: 60000 });
  await p.waitForTimeout(4500);
  const n = (await p.locator('img').count()) - (await p.locator('[contenteditable="true"] img').count());
  const size = await p.evaluate(() => { const i = [...document.images].find((x) => !x.closest('[contenteditable="true"]') && x.naturalWidth > 300); return i ? [i.naturalWidth, i.naturalHeight, i.src.split('?')[0].slice(-40)] : null; });
  console.log(slug, '見出し画像', n, JSON.stringify(size));
  if (n === 1 && size) ok++;
  await p.screenshot({ path: `${out}/${slug}.png`, clip: { x: 300, y: 90, width: 640, height: 340 } });
}
await p.goto('https://note.com/bontallc/m/m1576d0e10b0e/edit');
await p.waitForTimeout(5000);
const m = await p.evaluate(() => { const i = [...document.images].find((x) => x.naturalWidth > 300); return i ? [i.naturalWidth, i.naturalHeight, i.src.split('?')[0].slice(-40)] : null; });
console.log('magazine', JSON.stringify(m));
if (m) ok++;
await p.screenshot({ path: `${out}/magazine.png`, clip: { x: 440, y: 240, width: 640, height: 340 } });
console.log(`見出し画像あり ${ok}/8`);
await b.close();
