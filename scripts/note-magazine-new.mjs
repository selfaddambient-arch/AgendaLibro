// note のマガジンを作る（無料）。--create を付けたときだけ「作成」を押す。
//   node scripts/note-magazine-new.mjs <タイトル> <説明文> <画像> [--create] [--private]
import { chromium } from 'playwright';
const [TITLE, DESC, IMG] = process.argv.slice(2);
const create = process.argv.includes('--create');
const priv = process.argv.includes('--private');
const b = await chromium.launch({ headless: false, channel: 'chrome', ignoreDefaultArgs: ['--enable-automation'], args: ['--disable-blink-features=AutomationControlled'] });
const c = await b.newContext({ storageState: 'secrets/note-state.json', locale: 'ja-JP', viewport: { width: 1280, height: 1000 } });
const p = await c.newPage();
await p.goto('https://note.com/magazines/new');
await p.locator('input#name').waitFor({ timeout: 60000 });
await p.waitForTimeout(1500);
await p.mouse.click(582, 370);
const [chooser] = await Promise.all([p.waitForEvent('filechooser', { timeout: 15000 }), p.getByText('画像をアップロード').click()]);
await chooser.setFiles(IMG);
await p.waitForTimeout(3500);
const use = p.getByRole('button', { name: 'この画像を使う' });
if (await use.count()) { await use.click(); await p.waitForTimeout(3000); }
const save = p.getByRole('button', { name: '保存', exact: true });
if (await save.count()) { await save.click(); await p.waitForTimeout(3000); }
await p.locator('input#name').fill(TITLE);
await p.locator('textarea').first().fill(DESC);
// 公開設定：既定の状態を画面で確かめる（スイッチが無い画面では、公開／非公開の選択肢を文字で探す）
const vis = await p.evaluate(() => [...document.querySelectorAll('input[type=radio],input[type=checkbox],[role=radio],[role=switch]')].map((e) => ({ t: e.type || e.getAttribute('role'), n: e.name || e.id, c: e.checked ?? e.getAttribute('aria-checked'), l: (e.closest('label')?.innerText || e.parentElement?.innerText || '').replace(/\s+/g, ' ').slice(0, 40) })));
console.log('VIS', JSON.stringify(vis));
await p.screenshot({ path: 'docs/evidence/note-magazine-new.png', fullPage: true });
if (create) {
  await p.getByRole('button', { name: '作成' }).click();
  await p.waitForTimeout(5000);
  console.log('AFTER_URL', p.url());
}
await b.close();
