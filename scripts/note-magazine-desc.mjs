// note のマガジンの説明文の末尾に1行足す（代表承認 2026-10-28）。すでに入っていれば足さない。
//   BOOK=hitori-de-mise node scripts/note-magazine-desc.mjs
import { chromium } from 'playwright';
import { readFileSync } from 'node:fs';
const slug = process.env.BOOK || 'uchi-no-mise';
const url = JSON.parse(readFileSync(`books/${slug}/note/magazine.json`, 'utf8')).url;
const LINE = 'PDF版（無料・再配布自由）・Kindle版・Google Play版はこちら：https://bontallc.com/books?via=note';
const b = await chromium.launch({ headless: false, channel: 'chrome', ignoreDefaultArgs: ['--enable-automation'], args: ['--disable-blink-features=AutomationControlled'] });
const ctx = await b.newContext({ storageState: 'secrets/note-state.json', locale: 'ja-JP', viewport: { width: 1280, height: 1000 } });
const p = await ctx.newPage();
await p.goto(url + '/edit');
const ta = p.locator('textarea').first();
await ta.waitFor({ timeout: 60000 });
await p.waitForTimeout(2000);
const cur = await ta.inputValue();
if (!cur.includes(LINE)) await ta.fill(cur.replace(/\s+$/, '') + '\n' + LINE);
await p.getByRole('button', { name: '更新', exact: true }).click();
await p.waitForTimeout(6000);
await p.goto(url + '/edit');
await p.locator('textarea').first().waitFor({ timeout: 60000 });
await p.waitForTimeout(2000);
const after = await p.locator('textarea').first().inputValue();
console.log(JSON.stringify({ slug, 説明文: after, 入った: after.endsWith(LINE) }));
await b.close();
