// note のマガジンを作る（無料・非公開）。--create を付けたときだけ「作成」を押す。
//   node scripts/note-magazine.mjs [--create]
import { chromium } from 'playwright';
const create = process.argv.includes('--create');
const S = '/private/tmp/claude-502/-Users-keikawaguchi-AntiGravity-AgendaLibro/441d50a6-9423-46bd-b06c-f8a7a50a3bef/scratchpad/';
const SLUG = process.env.BOOK || 'uchi-no-mise';
const CFGS = {
  'uchi-no-mise': ['うちの店は、うちの仕様で', '19席のバー店主が、AIで予約システムから道具まで自分で作った記録。全7回。', 'books/uchi-no-mise/note-headers/note/magazine.png'],
  'hitori-de-mise': ['1人で店を回す、その横にAIが来た', '話すと、やってくれる。想像以上に。全8回。', 'books/hitori-de-mise/note-headers/note/magazine.png'],
};
const [TITLE, DESC, IMG] = CFGS[SLUG];
const b = await chromium.launch({ headless: false, channel: 'chrome', ignoreDefaultArgs: ['--enable-automation'], args: ['--disable-blink-features=AutomationControlled'] });
const c = await b.newContext({ storageState: 'secrets/note-state.json', locale: 'ja-JP', viewport: { width: 1280, height: 1000 } });
const p = await c.newPage();
await p.goto('https://note.com/magazines/new');
await p.locator('input#name').waitFor({ timeout: 60000 });
// マガジン画像
await p.waitForTimeout(1500);
await p.mouse.click(582, 370);
const [chooser] = await Promise.all([p.waitForEvent('filechooser', { timeout: 15000 }), p.getByText('画像をアップロード').click()]);
await chooser.setFiles(IMG);
await p.waitForTimeout(2000);
const use = p.getByRole('button', { name: 'この画像を使う' });
if (await use.count()) { await use.click(); await p.waitForTimeout(3000); }
const save = p.getByRole('button', { name: '保存', exact: true });
if (await save.count()) { await save.click(); await p.waitForTimeout(3000); }
await p.locator('input#name').fill(TITLE);
await p.locator('textarea').first().fill(DESC);
// 公開設定を「非公開」にする（公開は代表が行う）
const sw = p.getByRole('switch');
if (await sw.count() && (await sw.first().getAttribute('aria-checked')) === 'true') await sw.first().click();
else await p.getByText('公開', { exact: true }).last().click();
await p.waitForTimeout(800);
await p.screenshot({ path: S + 'mg5.png', fullPage: true });
console.log('switch state:', await sw.count() ? await sw.first().getAttribute('aria-checked') : 'no-switch');
if (create) {
  await p.getByRole('button', { name: '作成' }).click();
  await p.waitForTimeout(5000);
  console.log('AFTER_URL', p.url());
  await p.screenshot({ path: S + 'mg6.png' });
}
await b.close();
