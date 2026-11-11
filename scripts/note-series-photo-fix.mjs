// note-series-photo.mjs の試行で本文が崩れた段落を、原稿どおりの内容で貼り直して一時保存する（公開は note-publish.mjs --update）。
import { chromium } from 'playwright';
const [editUrl, startsWith, html] = process.argv.slice(2);
const browser = await chromium.launch({ headless: false, channel: 'chrome', ignoreDefaultArgs: ['--enable-automation'], args: ['--disable-blink-features=AutomationControlled'] });
const ctx = await browser.newContext({ storageState: 'secrets/note-state.json', locale: 'ja-JP', viewport: { width: 1280, height: 900 } });
const page = await ctx.newPage();
await page.goto(editUrl);
await page.getByPlaceholder('記事タイトル').waitFor({ timeout: 60000 });
await page.waitForTimeout(4000);
const body = page.locator('[contenteditable="true"]').first();
await body.locator('p', { hasText: startsWith }).first().click({ clickCount: 3 });
await page.waitForTimeout(500);
await body.evaluate((el, h) => {
  const dt = new DataTransfer();
  dt.setData('text/html', h);
  dt.setData('text/plain', h.replace(/<[^>]+>/g, ''));
  el.dispatchEvent(new ClipboardEvent('paste', { clipboardData: dt, bubbles: true, cancelable: true }));
}, html);
await page.waitForTimeout(1200);
console.log('STRUCT', await body.evaluate((el) => [...el.children].map((x) => x.tagName + (x.tagName === 'FIGURE' ? (x.hasAttribute('embedded-service') ? '(card)' : '') : '') + ':' + (x.tagName === 'FIGURE' ? (x.querySelector('figcaption')?.innerText || '') : x.innerText).slice(0, 14).split('\n').join('/')).join(' | ')));
await page.getByRole('button', { name: '一時保存' }).click();
await page.getByText('保存しました').first().waitFor({ timeout: 30000 }).catch(() => {});
await page.waitForTimeout(1500);
await browser.close();
