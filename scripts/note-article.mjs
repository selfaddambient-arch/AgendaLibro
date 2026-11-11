// note に記事の下書きを作る（題名・見出し画像・本文・本文の画像とキャプション）。公開はしない。
//   node scripts/note-article.mjs --article <article.md> --header <見出し画像> [--url <editor.note.com/notes/…/edit/>] [--shot <保存先.png>]
// note-calendar.mjs の汎用版。画像は article.md の ![キャプション](相対パス) で指定する。
import { chromium } from 'playwright';
import { readFileSync } from 'node:fs';
import { basename, resolve, dirname } from 'node:path';

const argv = process.argv.slice(2);
const opt = (k) => (argv.includes(k) ? argv[argv.indexOf(k) + 1] : undefined);
const file = opt('--article') ?? 'articles/2026-11-calendar/article.md';
const header = opt('--header') ?? 'articles/2026-11-calendar/note-header/note/calendar.png';
const editUrl = opt('--url') ?? 'https://editor.note.com/new';
const shot = opt('--shot');

const blocks = readFileSync(file, 'utf8').trim().split(/\n{2,}/);
const title = blocks.shift().replace(/^# /, '');

const browser = await chromium.launch({ headless: false, channel: 'chrome', ignoreDefaultArgs: ['--enable-automation'], args: ['--disable-blink-features=AutomationControlled'] });
const context = await browser.newContext({ storageState: 'secrets/note-state.json', locale: 'ja-JP', viewport: { width: 1280, height: 900 } });
const page = await context.newPage();
await page.goto(editUrl);
const titleBox = page.getByPlaceholder('記事タイトル');
await titleBox.waitFor({ timeout: 60000 });
await page.waitForTimeout(3000);

// 見出し画像（本文の外にある img の数で、入っているかを判定）
const hasEyecatch = (await page.locator('img').count()) - (await page.locator('[contenteditable="true"] img').count()) > 0;
if (!hasEyecatch) {
  const r = await page.evaluate(() => { const e = [...document.querySelectorAll('button')].find((b) => { const q = b.getBoundingClientRect(); return !b.textContent.trim() && !b.getAttribute('aria-label') && Math.round(q.width) === 40 && Math.round(q.height) === 40 && q.top > 60 && q.top < 200; }); const q = e.getBoundingClientRect(); return [q.x + 20, q.y + 20]; });
  await page.mouse.click(r[0], r[1]);
  const [chooser] = await Promise.all([page.waitForEvent('filechooser'), page.getByText('画像をアップロード').click()]);
  await chooser.setFiles(resolve(header));
  await page.waitForTimeout(3500); // 切り抜き画面が出そろうのを待つ
  await page.getByRole('button', { name: '保存', exact: true }).click({ timeout: 30000 });
  await page.waitForTimeout(4000);
}

await titleBox.fill(title);
const body = page.locator('[contenteditable="true"]').first();
await body.click();

const esc = (t) => t.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const inline = (t) => esc(t).replace(/\[([^\]]+)\]\((https?:[^)\s]+)\)/g, '<a href="$2">$1</a>');
const images = [];
const toHtml = (block) => {
  const im = block.match(/^!\[(.*)\]\((.+)\)$/);
  if (im) { images.push({ alt: im[1], path: resolve(dirname(file), im[2]) }); return `<p>[[IMG${images.length - 1}]]</p>`; }
  if (block.startsWith('## ')) return `<h2>${inline(block.slice(3))}</h2>`;
  return `<p>${inline(block).split('\n').join('<br>')}</p>`;
};
const html = blocks.map(toHtml).join('');
await page.keyboard.press('Meta+A');
await body.evaluate((el, h) => {
  const dt = new DataTransfer();
  dt.setData('text/html', h);
  dt.setData('text/plain', el.innerText);
  el.dispatchEvent(new ClipboardEvent('paste', { clipboardData: dt, bubbles: true, cancelable: true }));
}, html);
await page.waitForTimeout(1500);

// 本文中の画像：目印の段落を消して、画像ファイルを貼り付ける（note が自動でアップロードする）。そのあとキャプションを入れる
for (let i = 0; i < images.length; i++) {
  const { alt, path } = images[i];
  const before = await page.locator('[contenteditable="true"] img').count();
  await page.getByText(`[[IMG${i}]]`, { exact: true }).click({ clickCount: 3 });
  await page.waitForTimeout(600);
  await page.keyboard.press('Backspace');
  await page.waitForTimeout(600);
  const b64 = readFileSync(path).toString('base64');
  await body.evaluate((el, [name, data]) => {
    const bin = Uint8Array.from(atob(data), (c) => c.charCodeAt(0));
    const dt = new DataTransfer();
    dt.items.add(new File([bin], name, { type: 'image/jpeg' }));
    el.dispatchEvent(new ClipboardEvent('paste', { clipboardData: dt, bubbles: true, cancelable: true }));
  }, [basename(path), b64]);
  await page.waitForFunction((n) => document.querySelectorAll('[contenteditable="true"] img').length > n, before, { timeout: 60000 });
  await page.waitForTimeout(2500);
  const fig = body.locator('figure').nth(i);
  if (i === 0) console.log('FIGURE_HTML', (await fig.evaluate((e) => e.outerHTML)).replace(/src="[^"]+"/g, 'src="…"').slice(0, 600));
  const cap = fig.locator('figcaption');
  await cap.click();
  await page.waitForTimeout(400);
  await page.keyboard.type(alt);
  await page.waitForTimeout(600);
  console.log('CAPTION', i, JSON.stringify(await cap.innerText()));
}

await page.getByRole('button', { name: /^(下書き保存|一時保存)$/ }).click(); // 公開済みの記事を直すときは「一時保存」
await page.getByText('保存しました').first().waitFor({ timeout: 30000 }).catch(() => {});
await page.waitForTimeout(1500);
if (shot) await page.screenshot({ path: shot, fullPage: true });
console.log('DRAFT_URL ' + page.url());
await browser.close();
