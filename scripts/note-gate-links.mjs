// 導線の仕上げの機械ゲート（未ログインで確認）。
//   node scripts/note-gate-links.mjs
// 15本：冒頭の PDF リンク／末尾の PDF リンク（302）／bontallc.com のリンクが ?via=note 系／【 】0／公開（200）
// 案内記事・経緯の記事：公開（200）。マガジン2つ：公開・説明文の末尾。プロフィール：旧題名0。
import { chromium } from 'playwright';
import { readFileSync, writeFileSync } from 'node:fs';
const PDF = { 'hitori-de-mise': 'https://bontallc.com/books/hitori-de-mise/pdf?via=note', 'uchi-no-mise': 'https://bontallc.com/books/uchi-no-mise/pdf?via=note' };
const S = '/private/tmp/claude-502/-Users-keikawaguchi-AntiGravity-AgendaLibro/441d50a6-9423-46bd-b06c-f8a7a50a3bef/scratchpad/';
const b = await chromium.launch();
const ctx = await b.newContext({ locale: 'ja-JP', viewport: { width: 1280, height: 900 } });
let bad = 0;
const row = (o) => { console.log(JSON.stringify(o)); if (Object.values(o).some((v) => v === false)) bad++; };
for (const slug of ['hitori-de-mise', 'uchi-no-mise']) {
  const drafts = JSON.parse(readFileSync(`books/${slug}/note/drafts.json`, 'utf8'));
  for (const [s, key] of Object.entries(drafts)) {
    const p = await ctx.newPage();
    const r = await p.goto(`https://note.com/bontallc/n/${key}`, { waitUntil: 'load', timeout: 60000 });
    await p.waitForTimeout(2500);
    const el = p.locator('.note-common-styles__textnote-body').first();
    const text = await el.innerText();
    const links = await el.evaluate((e) => [...e.querySelectorAll('a')].map((a) => a.href));
    const first = text.split('\n').find((l) => l.trim());
    const bont = links.filter((h) => h.includes('bontallc.com'));
    const pdfN = links.filter((h) => h === PDF[slug]).length;
    const cards = await el.evaluate((e, u) => [...e.querySelectorAll('figure')].some((f) => (f.getAttribute('data-src') || '') === u), `https://bontallc.com/books/${slug}?via=note`);
    row({ slug, s, 公開200: r.status() === 200, 冒頭がPDF案内: first.startsWith('この本は PDF・Google Play でも無料で読めます'), PDFリンク2か所以上: pdfN >= 2, カード: cards, via付き: bont.every((h) => /via=note1?$/.test(h) || /via=note1?&/.test(h)), 括弧0: !/[【】]/.test(text), 旧題名0: !text.includes('1人で店を回す') });
    await p.close();
  }
  const rr = await ctx.request.get(PDF[slug], { maxRedirects: 0 });
  row({ slug, PDF302: rr.status() === 302, to: (rr.headers()['location'] || '').slice(0, 50) });
}
for (const [name, key] of [['案内記事', 'ne8a093f1a536'], ['出版の経緯', 'n580b9262d396']]) {
  const p = await ctx.newPage();
  const r = await p.goto(`https://note.com/bontallc/n/${key}`, { waitUntil: 'load', timeout: 60000 });
  await p.waitForTimeout(2500);
  const text = await p.locator('.note-common-styles__textnote-body').first().innerText();
  const tags = new Set(await p.$$eval('a[href*="/hashtag/"]', (as) => as.map((a) => a.textContent.trim())));
  row({ name, 公開200: r.status() === 200, タグ: tags.size, 括弧0: !/[【】]/.test(text), 本の一覧リンク: (await p.locator('a[href*="bontallc.com/books?via=note"], figure[data-src*="bontallc.com/books?via=note"]').count()) > 0 });
  await p.close();
}
for (const [slug, url] of Object.entries({ 'hitori-de-mise': 'https://note.com/bontallc/m/m653458c91a21', 'uchi-no-mise': 'https://note.com/bontallc/m/m1576d0e10b0e' })) {
  const p = await ctx.newPage();
  const r = await p.goto(url, { waitUntil: 'load' });
  await p.waitForTimeout(2500);
  const og = await p.locator('meta[property="og:description"]').getAttribute('content').catch(() => '');
  const t = (await p.locator('body').innerText()) + (og || '');
  row({ マガジン: slug, 公開200: r.status() === 200, 説明文: t.includes('PDF版（無料・再配布自由）・Google Play版（無料）・Kindle版（99円）はこちら') });
  await p.close();
}
{
  const p = await ctx.newPage();
  await p.goto('https://note.com/bontallc', { waitUntil: 'load' });
  await p.waitForTimeout(4000);
  const t = await p.locator('body').innerText();
  row({ プロフィール旧題名0: !t.includes('1人で店を回す'), プロフィール新題名: t.includes('一人で店を回す、その横にAIが来た。') });
  await p.screenshot({ path: S + 'creator.png' });
  await p.close();
}
await b.close();
console.log(bad ? `NG ${bad}` : 'ALL OK');
process.exit(bad ? 1 : 0);
