// 公開した note 記事を、未ログインで開いて表示を確かめる。
//   BOOK=hitori-de-mise node scripts/note-verify-public.mjs [slug ...]
import { chromium } from 'playwright';
import { readFileSync } from 'node:fs';
const mdFile = (slug) => `books/${process.env.BOOK || 'uchi-no-mise'}/note/${slug === 'intro' && (process.env.BOOK || 'uchi-no-mise') === 'uchi-no-mise' ? 'a-hajimeni' : slug}.md`;
const SLUG = process.env.BOOK || 'uchi-no-mise';
const drafts = JSON.parse(readFileSync(`books/${SLUG}/note/drafts.json`, 'utf8'));
const slugs = process.argv.slice(2).length ? process.argv.slice(2) : Object.keys(drafts);
const total = Object.keys(drafts).length;
const WANT = ['飲食店経営', '個人店', '生成AI', 'AI活用', 'バイブコーディング', 'ClaudeCode', 'Gemini', 'MCP', 'DX', '東中野', '屯', '本多楽', 'Agendaシリーズ', '無料公開'];
const b = await chromium.launch();
const ctx = await b.newContext({ locale: 'ja-JP', viewport: { width: 1280, height: 900 } });
let bad = 0;
for (const s of slugs) {
  const p = await ctx.newPage();
  const r = await p.goto(`https://note.com/bontallc/n/${drafts[s]}`, { waitUntil: 'load', timeout: 60000 });
  await p.waitForTimeout(2500);
  const artEl = p.locator('.note-common-styles__textnote-body').first();
  const body = ((await artEl.count()) ? await artEl.innerText() : await p.locator('body').innerText()).replace(/\s+/g, '');
  const tags = [...new Set(await p.$$eval('a[href*="/hashtag/"]', (as) => as.map((a) => a.textContent.trim().replace(/^#/, ''))))];
  const missing = WANT.filter((t) => !tags.some((x) => x.toLowerCase() === t.toLowerCase()));
  const imgs = await artEl.locator('img').count();
  const wantImgs = (readFileSync(mdFile(s), 'utf8').match(/^!\[/gm) || []).length;
  const info = {
    slug: s, status: r.status(), title: (await p.title()).slice(0, 50),
    全N回: body.includes('全' + total + '回の'), ストアURL仮行: (body.match(/【ストアURL】/g) || []).length, 旧題名: (body.match(/1人で店を回す/g) || []).length, 括弧: (body.match(/[【】]/g) || []).length,
    kindle: SLUG === 'hitori-de-mise' ? (await p.locator('a[href*="B0GFY4WW4Y"]').count()) > 0 : null, tags: tags.length, 足りないタグ: missing, imgs, 本文の画像: wantImgs,
  };
  console.log(JSON.stringify(info));
  if (info.status !== 200 || info.ストアURL仮行 || info.旧題名 || info.括弧 || info.足りないタグ.length || info.imgs < info.本文の画像) bad++;
  await p.close();
}
await b.close();
process.exit(bad ? 1 : 0);
