// シリーズ記事の指定デザインの節に、実際に飾った写真を1枚と、写真の記事へのリンク1行を足して一時保存する（公開は note-publish.mjs --update）。
//   node scripts/note-series-photo.mjs <editor.note.com/notes/…/edit/> <説明文の書き出し> <写真ファイル> <キャプション> <写真の記事URL> [--save]
// 挿入位置：その節の説明文の段落の直前（見本の図と説明文のあいだ）。写真→リンクの1行の順に並ぶ。
// ※リンクの行の後ろで Enter を押すと note がリンクカードに変えてしまうので、段落の「先頭」で Enter を押して空の段落をつくる。
import { chromium } from 'playwright';
import { readFileSync } from 'node:fs';
import { basename } from 'node:path';
const [editUrl, lead, photo, caption, articleUrl] = process.argv.slice(2);
const save = process.argv.includes('--save');
const browser = await chromium.launch({ headless: false, channel: 'chrome', ignoreDefaultArgs: ['--enable-automation'], args: ['--disable-blink-features=AutomationControlled'] });
const ctx = await browser.newContext({ storageState: 'secrets/note-state.json', locale: 'ja-JP', viewport: { width: 1280, height: 900 } });
const page = await ctx.newPage();
await page.goto(editUrl);
await page.getByPlaceholder('記事タイトル').waitFor({ timeout: 60000 });
await page.waitForTimeout(4000);
const body = page.locator('[contenteditable="true"]').first();
const dump = () => body.evaluate((el) => { const a = [...el.children]; const i = a.findIndex((x) => x.tagName === 'H2' && x.innerText.startsWith('Josefin')); const j = a.findIndex((x, k) => k > i && x.tagName === 'H2'); return a.slice(i, j).map((x) => x.tagName + ':' + (x.tagName === 'FIGURE' ? (x.querySelector('figcaption')?.innerText || '') : x.innerText).slice(0, 26).split('\n').join('/') + (x.querySelector('a') ? '[a]' : '')).join(' | '); });
const caretBeforeText = async () => {
  await body.evaluate((el, ld) => { const p = [...el.querySelectorAll(':scope > p')].find((x) => x.innerText.startsWith(ld)); const w = document.createTreeWalker(p, NodeFilter.SHOW_TEXT); const n = w.nextNode(); const r = document.createRange(); r.setStart(n, 0); r.collapse(true); const s = getSelection(); s.removeAllRanges(); s.addRange(r); }, lead);
  await page.keyboard.press('Enter');
  await page.keyboard.press('ArrowUp');
  await page.waitForTimeout(500);
};
// 1) 説明文の段落を、先頭にリンクの1行を足した形で置き換える（段落ごと貼り替える方式。段落の途中への貼り付けは、前後の段落と混ざる）
const para = body.locator('p', { hasText: lead }).first();
const inner = await para.evaluate((q) => q.innerHTML.replace(/ (name|id|target|rel|class)="[^"]*"/g, ''));
await para.click({ clickCount: 3 });
await page.waitForTimeout(500);
const link = `<p>実際に飾った写真は、こちらの記事で見られます：<a href="${articleUrl}">${articleUrl}</a><br>${inner}</p>`;
await body.evaluate((el, h) => {
  const dt = new DataTransfer();
  dt.setData('text/html', h);
  dt.setData('text/plain', h.replace(/<[^>]+>/g, ''));
  el.dispatchEvent(new ClipboardEvent('paste', { clipboardData: dt, bubbles: true, cancelable: true }));
}, link);
await page.waitForTimeout(1000);
console.log('LINK', await dump());
// 2) 写真：その段落の先頭で Enter → 上の空の段落に目印を打ち、目印を消して画像を貼る
await body.evaluate((el) => { const p = [...el.querySelectorAll(':scope > p')].find((x) => x.innerText.startsWith('実際に飾った写真は')); const w = document.createTreeWalker(p, NodeFilter.SHOW_TEXT); const n = w.nextNode(); const r = document.createRange(); r.setStart(n, 0); r.collapse(true); const s = getSelection(); s.removeAllRanges(); s.addRange(r); });
await page.keyboard.press('Enter');
await page.keyboard.press('Enter');
await page.keyboard.press('ArrowUp');
await page.keyboard.type('[[PHOTO]]');
await page.waitForTimeout(500);
console.log('TYPED', await dump());
await page.getByText('[[PHOTO]]', { exact: true }).click({ clickCount: 3 });
await page.keyboard.press('Backspace');
await page.waitForTimeout(600);
console.log('CLEARED', await dump());
const before = await body.locator('img').count();
const b64 = readFileSync(photo).toString('base64');
await body.evaluate((el, [name, d]) => {
  const bin = Uint8Array.from(atob(d), (c) => c.charCodeAt(0));
  const dt = new DataTransfer();
  dt.items.add(new File([bin], name, { type: 'image/jpeg' }));
  el.dispatchEvent(new ClipboardEvent('paste', { clipboardData: dt, bubbles: true, cancelable: true }));
}, [basename(photo), b64]);
await page.waitForFunction((n) => document.querySelectorAll('[contenteditable="true"] img').length > n, before, { timeout: 60000 });
await page.waitForTimeout(3000);
const cap = body.locator('figure.figcaption-placeholder figcaption').last();
await cap.click();
await page.keyboard.type(caption);
await page.waitForTimeout(500);
console.log('FINAL', await dump());
if (save) {
  await page.getByRole('button', { name: '一時保存' }).click();
  await page.getByText('保存しました').first().waitFor({ timeout: 30000 }).catch(() => {});
  await page.waitForTimeout(1500);
}
await browser.close();
