// マガジンの記事が、回の順（1回目が先頭）に並んでいるかを確かめる。公開状態も表示する。
//   BOOK=hitori-de-mise node scripts/note-magazine-check.mjs
import { chromium } from 'playwright';
import { readFileSync } from 'node:fs';
const SLUG = process.env.BOOK || 'uchi-no-mise';
const drafts = JSON.parse(readFileSync(`books/${SLUG}/note/drafts.json`, 'utf8'));
const mag = JSON.parse(readFileSync(`books/${SLUG}/note/magazine.json`, 'utf8')).url;
const want = Object.values(drafts);
const b = await chromium.launch({ headless: false, channel: 'chrome', ignoreDefaultArgs: ['--enable-automation'], args: ['--disable-blink-features=AutomationControlled'] });
const ctx = await b.newContext({ storageState: 'secrets/note-state.json', locale: 'ja-JP', viewport: { width: 1280, height: 1000 } });
const p = await ctx.newPage();
await p.goto(mag); await p.waitForTimeout(6000);
for (let i = 0; i < 5; i++) { await p.mouse.wheel(0, 3000); await p.waitForTimeout(600); }
const head = (await p.locator('body').innerText()).replace(/\s+/g, ' ').match(/(非公開|公開中)?\s*(\d+)本/);
const keys = [...new Set(await p.$$eval('a', (as) => as.map((a) => (a.getAttribute('href') || '').match(/\/bontallc\/n\/(n[0-9a-f]+)/)?.[1]).filter(Boolean)))];
const ok = JSON.stringify(keys) === JSON.stringify(want);
console.log(mag, '| 記事', keys.length, '本 | 回の順:', ok, '| 表示:', head?.[0]);
if (!ok) console.log(' 実際:', keys.join(','), '\n 期待:', want.join(','));
await b.close();
process.exit(ok ? 0 : 1);
