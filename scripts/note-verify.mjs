// note の記事管理画面を開き、下書きの一覧を撮る（公開状態でないことの確認用）。
//   node scripts/note-verify.mjs <保存先.png>
import { chromium } from 'playwright';
const browser = await chromium.launch({
  headless: false, channel: 'chrome',
  ignoreDefaultArgs: ['--enable-automation'],
  args: ['--disable-blink-features=AutomationControlled'],
});
const context = await browser.newContext({ storageState: 'secrets/note-state.json', locale: 'ja-JP', viewport: { width: 1280, height: 900 } });
const page = await context.newPage();
await page.goto('https://note.com/notes?status=draft', { waitUntil: 'domcontentloaded' });
await page.waitForTimeout(8000);
console.log(page.url());
console.log((await page.locator('body').innerText()).slice(0, 900));
await page.screenshot({ path: process.argv[2] });
await browser.close();
