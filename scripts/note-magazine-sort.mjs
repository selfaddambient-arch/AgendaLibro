// マガジンの並びを「日付昇順」（＝1回目が先頭）にして保存する。
//   node scripts/note-magazine-sort.mjs <マガジンURL>
import { chromium } from 'playwright';
const url = process.argv[2];
const b = await chromium.launch({ headless: false, channel: 'chrome', ignoreDefaultArgs: ['--enable-automation'], args: ['--disable-blink-features=AutomationControlled'] });
const ctx = await b.newContext({ storageState: 'secrets/note-state.json', locale: 'ja-JP', viewport: { width: 1280, height: 1000 } });
const p = await ctx.newPage();
await p.goto(url);
await p.waitForTimeout(5000);
await p.getByText('並び替え・削除').first().click();
await p.waitForTimeout(2000);
if (await p.getByText('追加日順').count()) await p.getByText('追加日順').first().click();
await p.waitForTimeout(1500);
await p.getByRole('button', { name: '保存' }).click();
await p.waitForTimeout(4000);
await p.goto(url);
await p.waitForTimeout(5000);
for (let i = 0; i < 5; i++) { await p.mouse.wheel(0, 3000); await p.waitForTimeout(600); }
const titles = await p.$$eval('a[href*="/n/n"]', (as) => { const seen = new Set(); return as.map((a) => a.innerText.replace(/\s+/g, ' ').trim()).filter((t) => t.includes('』') && !seen.has(t.slice(0, 40)) && seen.add(t.slice(0, 40))); });
console.log(titles.map((t, i) => `${i + 1} ${t.slice(0, 70)}`).join('\n'));
await b.close();
