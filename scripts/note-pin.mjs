// note の記事をクリエイターページに固定する（代表承認 2026-10-28）。
//   KEY=<記事の鍵> node scripts/note-pin.mjs
import { chromium } from 'playwright';
const key = process.env.KEY;
const b = await chromium.launch({ headless: false, channel: 'chrome', ignoreDefaultArgs: ['--enable-automation'], args: ['--disable-blink-features=AutomationControlled'] });
const c = await b.newContext({ storageState: 'secrets/note-state.json', locale: 'ja-JP', viewport: { width: 1280, height: 1000 } });
const p = await c.newPage();
await p.goto(`https://note.com/bontallc/n/${key}`);
await p.waitForTimeout(5000);
await p.mouse.click(931, 624); // 記事の著者行の「…」
await p.waitForTimeout(1500);
console.log('MENU', await p.evaluate(() => [...document.querySelectorAll('[role="menuitem"],[role="menu"] button,[role="menu"] a,[role="dialog"] button')].map((e) => e.textContent.trim()).filter(Boolean).join(' / ')));
const pin = p.getByText(/クリエイターページに固定表示/).first();
if (process.argv.includes('--go') && (await pin.count())) { await pin.click(); await p.waitForTimeout(1500); await p.getByRole('button', { name: 'OK', exact: true }).click(); await p.waitForTimeout(4000); }
await p.screenshot({ path: '/private/tmp/claude-502/-Users-keikawaguchi-AntiGravity-AgendaLibro/441d50a6-9423-46bd-b06c-f8a7a50a3bef/scratchpad/pin.png' });
await b.close();
