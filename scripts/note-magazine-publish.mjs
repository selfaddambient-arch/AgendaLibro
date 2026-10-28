// マガジンを「公開」にする（代表承認 2026-10-28）。
//   BOOK=hitori-de-mise node scripts/note-magazine-publish.mjs
import { chromium } from 'playwright';
import { readFileSync } from 'node:fs';
const SLUG = process.env.BOOK || 'uchi-no-mise';
const url = JSON.parse(readFileSync(`books/${SLUG}/note/magazine.json`, 'utf8')).url;
const b = await chromium.launch({ headless: false, channel: 'chrome', ignoreDefaultArgs: ['--enable-automation'], args: ['--disable-blink-features=AutomationControlled'] });
const ctx = await b.newContext({ storageState: 'secrets/note-state.json', locale: 'ja-JP', viewport: { width: 1280, height: 1000 } });
const p = await ctx.newPage();
await p.goto(url + '/edit');
await p.waitForTimeout(6000);
const sw = p.getByRole('switch');
const n = await sw.count();
console.log('switch count', n);
const state = async () => (n ? await sw.first().getAttribute('aria-checked') : null);
console.log('before', await state());
if ((await state()) !== 'true') await sw.first().click();
await p.waitForTimeout(800);
console.log('toggled', await state());
await p.getByText('更新', { exact: true }).last().click();
await p.waitForTimeout(8000);
await p.goto(url);
await p.waitForTimeout(5000);
console.log('表示:', (await p.locator('body').innerText()).replace(/\s+/g, ' ').match(/(非公開|公開中)?\s*\d+本/)?.[0]);
await b.close();
