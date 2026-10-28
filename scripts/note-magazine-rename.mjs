// note のマガジンの名前を変える（非公開のまま）。
//   BOOK=hitori-de-mise node scripts/note-magazine-rename.mjs "<新しい名前>"
import { chromium } from 'playwright';
import { readFileSync } from 'node:fs';
const slug = process.env.BOOK || 'uchi-no-mise';
const name = process.argv[2];
const url = JSON.parse(readFileSync(`books/${slug}/note/magazine.json`, 'utf8')).url;
const b = await chromium.launch({ headless: false, channel: 'chrome', ignoreDefaultArgs: ['--enable-automation'], args: ['--disable-blink-features=AutomationControlled'] });
const ctx = await b.newContext({ storageState: 'secrets/note-state.json', locale: 'ja-JP', viewport: { width: 1280, height: 1000 } });
const p = await ctx.newPage();
await p.goto(url + '/edit');
const field = () => p.locator('input[type="text"]').filter({ hasNot: p.locator('nothing') }).nth(0);
await p.waitForTimeout(6000);
await field().fill(name);
await p.getByText('更新', { exact: true }).last().click();
await p.waitForTimeout(8000);
await p.goto(url + '/edit');
await p.waitForTimeout(6000);
console.log('マガジン名:', await field().inputValue());
await b.close();
