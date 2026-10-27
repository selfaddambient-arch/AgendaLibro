// note に下書きを作る。題名・本文を入れて「下書き保存」まで。公開ボタンは押さない。
//   node scripts/note-draft.mjs <記事.md> [--url <editor.note.com/notes/…/edit/>] [--image <画像>] [--shot <保存先.png>]
// 記事.md：1行目「# 題名」、以降は空行区切りのブロック。「## 」は見出し、「1. 」は番号リスト。
// ログイン状態は secrets/note-state.json（scripts/note-login.mjs で作る）。
import { chromium } from 'playwright';
import { readFileSync } from 'node:fs';
import { basename, resolve, dirname } from 'node:path';

const argv = process.argv.slice(2);
const opt = (k) => (argv.includes(k) ? argv[argv.indexOf(k) + 1] : undefined);
const file = argv[0];
const editUrl = opt('--url') ?? 'https://editor.note.com/new';
const image = opt('--image');
const shot = opt('--shot');
const titleOnly = argv.includes('--title-only'); // 記事 ID を得るため、題名だけで保存する

const blocks = readFileSync(file, 'utf8').trim().split(/\n{2,}/);
const title = blocks.shift().replace(/^# /, '');

const browser = await chromium.launch({
  headless: false,
  channel: 'chrome',
  ignoreDefaultArgs: ['--enable-automation'],
  args: ['--disable-blink-features=AutomationControlled'],
});
const context = await browser.newContext({
  storageState: 'secrets/note-state.json',
  locale: 'ja-JP',
  viewport: { width: 1280, height: 900 },
});
const page = await context.newPage();
await page.goto(editUrl);
const titleBox = page.getByPlaceholder('記事タイトル');
await titleBox.waitFor({ timeout: 60000 });

// 見出し画像：画像ボタン →「画像をアップロード」→ 切り抜き画面で「保存」
// 既に見出し画像がある下書きでは入れ直さない（本文の外にある img の数で判定）
const hasEyecatch = (await page.locator('img').count()) - (await page.locator('[contenteditable="true"] img').count()) > 0;
if (image && !hasEyecatch) {
  await page.mouse.click(509, 121);
  const [chooser] = await Promise.all([
    page.waitForEvent('filechooser'),
    page.getByText('画像をアップロード').click(),
  ]);
  await chooser.setFiles(image);
  await page.getByRole('button', { name: '保存', exact: true }).click();
  await page.waitForTimeout(4000);
}

await titleBox.fill(title);
if (titleOnly) {
  await page.getByRole('button', { name: '下書き保存' }).click();
  await page.getByText('保存しました').first().waitFor({ timeout: 30000 }).catch(() => {});
  await page.waitForTimeout(1500);
  console.log('DRAFT_URL ' + page.url());
  await browser.close();
  process.exit(0);
}
// 本文欄はタイトル欄の直下の contenteditable
const body = page.locator('[contenteditable="true"]').first();
await body.click();

// 本文は HTML にして貼り付ける（キー入力だと見出し・リストの自動変換が不安定）
const esc = (t) => t.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
// 本文中の [表示](URL) だけリンクにする
const inline = (t) => esc(t).replace(/\[([^\]]+)\]\((https?:[^)\s]+)\)/g, '<a href="$2">$1</a>');
const toHtml = (block) => {
  const im = block.match(/^!\[(.*)\]\((.+)\)$/);
  if (im) return `<p>[[IMG:${im[2]}]]</p>`;
  if (block.startsWith('### ')) return `<h3>${inline(block.slice(4))}</h3>`;
  if (block.startsWith('## ')) return `<h2>${inline(block.slice(3))}</h2>`;
  const lines = block.split('\n');
  if (lines.every((l) => /^\d+\. /.test(l))) {
    return '<ol>' + lines.map((l) => `<li><p>${inline(l.replace(/^\d+\. /, ''))}</p></li>`).join('') + '</ol>';
  }
  if (lines.every((l) => /^- /.test(l))) {
    return '<ul>' + lines.map((l) => `<li><p>${inline(l.slice(2))}</p></li>`).join('') + '</ul>';
  }
  if (lines.every((l) => /^> ?/.test(l))) {
    return `<blockquote><p>${inline(lines.map((l) => l.replace(/^> ?/, '')).join('\n')).split('\n').join('<br>')}</p></blockquote>`;
  }
  if (lines.every((l) => /^\|/.test(l))) {
    // note のエディタは表に対応しない（セルが1行に潰れる）ので「見出し：値」の箇条書きにする
    const rows = lines.filter((l) => !/^\|\s*-/.test(l)).map((l) => l.replace(/^\||\|$/g, '').split('|').map((c) => c.trim()));
    const [head, ...data] = rows;
    return '<ul>' + data.map((r) => `<li><p>${inline(head[0])}：${inline(r[0])}　${r.slice(1).map((c, i) => `${inline(head[i + 1])}：${inline(c)}`).join('／')}</p></li>`).join('') + '</ul>';
  }
  return `<p>${inline(block).split('\n').join('<br>')}</p>`;
};
const html = blocks.map(toHtml).join('');
await page.keyboard.press('Meta+A'); // 既存の本文があれば置き換える
await body.evaluate((el, h) => {
  const dt = new DataTransfer();
  dt.setData('text/html', h);
  dt.setData('text/plain', el.innerText);
  el.dispatchEvent(new ClipboardEvent('paste', { clipboardData: dt, bubbles: true, cancelable: true }));
}, html);
await page.waitForTimeout(1500);

// 本文中の画像：目印の段落を選んで消し、画像ファイルを貼り付ける（note が自動でアップロードする）
for (const m of html.matchAll(/\[\[IMG:(.+?)\]\]/g)) {
  const path = resolve(dirname(file), m[1]);
  const b64 = readFileSync(path).toString('base64');
  const before = await page.locator('[contenteditable="true"] img').count();
  await page.getByText(m[0], { exact: true }).click({ clickCount: 3 });
  await page.keyboard.press('Backspace');
  await body.evaluate((el, [name, data]) => {
    const bin = Uint8Array.from(atob(data), (c) => c.charCodeAt(0));
    const dt = new DataTransfer();
    dt.items.add(new File([bin], name, { type: 'image/png' }));
    el.dispatchEvent(new ClipboardEvent('paste', { clipboardData: dt, bubbles: true, cancelable: true }));
  }, [basename(path), b64]);
  await page.waitForFunction((n) => document.querySelectorAll('[contenteditable="true"] img').length > n, before, { timeout: 60000 });
  await page.waitForTimeout(2500);
}

await page.getByRole('button', { name: '下書き保存' }).click();
await page.getByText('保存しました').first().waitFor({ timeout: 30000 }).catch(() => {});
await page.waitForTimeout(1500);
if (shot) await page.screenshot({ path: shot });
console.log('DRAFT_URL ' + page.url());
console.log('CHARS ' + (await page.locator('body').innerText()).match(/(\d[\d,]*)\s*文字/)?.[1]);
await browser.close();
