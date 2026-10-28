// note の記事を公開する（代表承認 2026-10-28）。公開画面でハッシュタグとマガジンを設定して「投稿する」。
//   BOOK=hitori-de-mise node scripts/note-publish.mjs <slug> [--dry]
// --dry：公開画面でタグ・マガジンの設定まで行い、「投稿する」は押さない。
import { chromium } from 'playwright';
import { readFileSync } from 'node:fs';

const SLUG = process.env.BOOK || 'uchi-no-mise';
const slug = process.argv[2];
const dry = process.argv.includes('--dry');
const update = process.argv.includes('--update'); // 公開済みの記事を更新する（「更新する」を押す）
const key = JSON.parse(readFileSync(`books/${SLUG}/note/drafts.json`, 'utf8'))[slug];
const MAGAZINE = SLUG === 'hitori-de-mise' ? '一人で店を回す、その横にAIが来た。' : 'うちの店は、うちの仕様で';
const TAGS = ['飲食店経営', '個人店', '生成AI', 'AI活用', 'バイブコーディング', 'ClaudeCode', 'Gemini', 'MCP', 'DX', '東中野', '屯', '本多楽', 'Agendaシリーズ', '無料公開'];

const browser = await chromium.launch({ headless: false, channel: 'chrome', ignoreDefaultArgs: ['--enable-automation'], args: ['--disable-blink-features=AutomationControlled'] });
const ctx = await browser.newContext({ storageState: 'secrets/note-state.json', locale: 'ja-JP', viewport: { width: 1280, height: 1000 } });
const p = await ctx.newPage();
await p.goto(`https://editor.note.com/notes/${key}/publish/`);
await p.getByText('ハッシュタグ').first().waitFor({ timeout: 60000 });
await p.waitForTimeout(3000);

// ハッシュタグ（すでに付いているものは足さない）
const inp = p.getByPlaceholder('ハッシュタグを追加する');
// 選択済みのタグか（選択済みは「×」の絵を持つボタン。候補のタグは子の無いボタン）
const chip = (t) => p.evaluate((tt) => [...document.querySelectorAll('button')].some((e) => e.textContent.trim() === '#' + tt && e.children.length > 0), t);
for (const t of TAGS) {
  if (await chip(t)) continue;
  for (let k = 0; k < 4; k++) {  // タグの確定を待ち、入らなければやり直す
    await inp.fill('#' + t);
    await inp.press('Enter');
    await p.waitForTimeout(700);
    if (await chip(t)) break;
  }
}
let tagCount = 0;
for (const t of TAGS) if (await chip(t)) tagCount++;

// マガジン：名前の行にある「追加」を押す（「追加済」ならそのまま）
const btns = p.getByRole('button', { name: /^追加(済)?$/ });
let btn = null;
for (let i = 0; i < (await btns.count()); i++) {
  const t = await btns.nth(i).evaluate((e) => { let n = e; for (let k = 0; k < 4 && n.parentElement; k++) { n = n.parentElement; if (n.innerText.length > 12 && n.innerText.length < 90) return n.innerText.replace(/\s+/g, ' '); } return ''; });
  if (t.startsWith(MAGAZINE)) { btn = btns.nth(i); break; }
}
if (!btn) { console.log('MAGAZINE_ROW_NOT_FOUND'); await browser.close(); process.exit(3); }
const label = (await btn.textContent()).trim();
if (label === '追加') { await btn.click(); await p.waitForTimeout(800); }
const magLabel = (await btn.textContent()).trim();

// 記事タイプは無料（既定）
const free = await p.getByRole('radio', { name: '無料' }).isChecked().catch(() => true);
console.log(JSON.stringify({ slug, key, tags: tagCount, magazine: magLabel, free }));
if (dry) { await p.screenshot({ path: `/private/tmp/claude-502/-Users-keikawaguchi-AntiGravity-AgendaLibro/441d50a6-9423-46bd-b06c-f8a7a50a3bef/scratchpad/_dry-${slug}.png`, fullPage: true }); await browser.close(); process.exit(0); }

if (tagCount < TAGS.length || magLabel !== '追加済' || !free) { console.log('SETTINGS_NG'); await browser.close(); process.exit(2); }
await p.getByRole('button', { name: update ? '更新する' : '投稿する' }).click();
await p.waitForTimeout(8000);
console.log('AFTER_URL', p.url());
await browser.close();
