// カレンダー紹介シリーズの記事に、他の回へのリンクとマガジンへのリンクを入れて一時保存する（公開は note-publish.mjs --update）。
//   node scripts/note-series-links.mjs <editor.note.com/notes/…/edit/> <設定.json> <series|first>
// 設定.json: { "links": [{"title","url"}…], "magazine": {"title","url"}, "firstTitle": "…" }
//   series: 「シリーズの他の回」の段落（題名の並び）をリンク付きに置き換え、末尾にマガジンの1行を足す
//   magonly: マガジンの1行だけを末尾に足す（写真の記事など、他の回リンクを持たない記事用）
//   first : 末尾に見出し「続きのシリーズ」と6本へのリンクを足し、その後にマガジンの1行を足す
import { chromium } from 'playwright';
import { readFileSync } from 'node:fs';
const [editUrl, cfgPath, mode] = process.argv.slice(2);
const cfg = JSON.parse(readFileSync(cfgPath, 'utf8'));
const esc = (t) => t.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const a = (l) => `<a href="${esc(l.url)}">${esc(l.title)}</a>`;
const magHtml = `<p>マガジン「${esc(cfg.magazine.title)}」にまとめています：<a href="${esc(cfg.magazine.url)}">${esc(cfg.magazine.url)}</a></p>`;
const browser = await chromium.launch({ headless: false, channel: 'chrome', ignoreDefaultArgs: ['--enable-automation'], args: ['--disable-blink-features=AutomationControlled'] });
const ctx = await browser.newContext({ storageState: 'secrets/note-state.json', locale: 'ja-JP', viewport: { width: 1280, height: 900 } });
const page = await ctx.newPage();
await page.goto(editUrl);
await page.getByPlaceholder('記事タイトル').waitFor({ timeout: 60000 });
await page.waitForTimeout(4000);
const body = page.locator('[contenteditable="true"]').first();
const paste = (html) => body.evaluate((el, h) => {
  const dt = new DataTransfer();
  dt.setData('text/html', h);
  dt.setData('text/plain', h.replace(/<[^>]+>/g, ''));
  el.dispatchEvent(new ClipboardEvent('paste', { clipboardData: dt, bubbles: true, cancelable: true }));
}, html);
const tail = () => body.evaluate((el) => [...el.children].slice(-4).map((c) => c.tagName + ':' + c.innerText.replace(/\n/g, '⏎').slice(-160) + ' [a=' + c.querySelectorAll('a').length + ']'));
const caretToEnd = () => body.evaluate((el) => { const last = el.lastElementChild; const r = document.createRange(); r.selectNodeContents(last); r.collapse(false); const s = getSelection(); s.removeAllRanges(); s.addRange(r); });
if (mode === 'magonly') {
  // マガジンの1行だけ足す（下のブロック）
} else if (mode === 'series') {
  const p = body.locator('p', { hasText: cfg.firstTitle }).last();
  await p.click({ clickCount: 3 });
  await page.waitForTimeout(500);
  await paste('<p>' + cfg.links.map(a).join('<br>') + '</p>');
  await page.waitForTimeout(1200);
} else {
  await body.locator(':scope > *').last().click();
  await caretToEnd();
  await page.keyboard.press('Enter');
  await page.keyboard.press('Enter');
  await page.keyboard.type('## ');
  await page.keyboard.type('続きのシリーズ（壁に飾る2027年カレンダー）');
  await page.keyboard.press('Enter');
  await paste('<p>' + cfg.links.map(a).join('<br>') + '</p>');
  await page.waitForTimeout(1200);
}
// マガジンの1行（なければ足す）
if (!(await body.evaluate((el, u) => el.innerHTML.includes(u), cfg.magazine.url))) {
  await caretToEnd();
  await page.keyboard.press('Enter');
  await page.waitForTimeout(400);
  await paste(magHtml);
  await page.waitForTimeout(1200);
}
console.log('TAIL', JSON.stringify(await tail(), null, 1));
await page.getByRole('button', { name: '一時保存' }).click();
await page.getByText('保存しました').first().waitFor({ timeout: 30000 }).catch(() => {});
await page.waitForTimeout(1500);
await browser.close();
