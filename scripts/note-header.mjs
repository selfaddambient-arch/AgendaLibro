// 下書きの見出し画像を差し替えて下書き保存（公開はしない）。
//   node scripts/note-header.mjs <slug|magazine> <画像> [--shot <保存先.png>]
// slug は books/uchi-no-mise/note/drafts.json の鍵名（intro・ch1…・ep・keii）。magazine はマガジンの画像を差し替える。
import { chromium } from 'playwright';
import { readFileSync } from 'node:fs';

const [slug, image] = process.argv.slice(2);
const shot = process.argv.includes('--shot') ? process.argv[process.argv.indexOf('--shot') + 1] : null;
const drafts = JSON.parse(readFileSync('books/uchi-no-mise/note/drafts.json', 'utf8'));
const MAGAZINE = 'https://note.com/bontallc/m/m1576d0e10b0e';
const browser = await chromium.launch({ headless: false, channel: 'chrome', ignoreDefaultArgs: ['--enable-automation'], args: ['--disable-blink-features=AutomationControlled'] });
const ctx = await browser.newContext({ storageState: 'secrets/note-state.json', locale: 'ja-JP', viewport: { width: 1280, height: 900 } });
const page = await ctx.newPage();

if (slug === 'magazine') {
  await page.goto(MAGAZINE + '/edit');
  await page.waitForTimeout(5000);
  await page.mouse.click(1001, 287); // 画像の「×」
  await page.waitForTimeout(2000);
  const [chooser] = await Promise.all([page.waitForEvent('filechooser', { timeout: 15000 }), page.getByRole('button', { name: 'ファイルを選択' }).click()]);
  await chooser.setFiles(image);
  await page.waitForTimeout(3500);
  const crop = page.getByRole('button', { name: 'この画像を使う' });
  if (await crop.count()) { await crop.click(); await page.waitForTimeout(3000); }
  if (shot) await page.screenshot({ path: shot.replace('.png', '-before.png'), fullPage: true });
  const save = page.getByText('更新', { exact: true }).last();
  await save.click();
  await page.waitForTimeout(12000);
  await page.goto(MAGAZINE + '/edit');
  await page.waitForTimeout(5000);
  console.log('magazine image after reload:', await page.evaluate(() => [...document.images].filter((x) => x.naturalWidth > 300).length));
  if (shot) await page.screenshot({ path: shot, fullPage: true });
  console.log('MAGAZINE updated:', page.url());
  await browser.close();
  process.exit(0);
}

await page.goto(`https://editor.note.com/notes/${drafts[slug]}/edit/`);
await page.getByPlaceholder('記事タイトル').waitFor({ timeout: 60000 });
await page.waitForTimeout(4000);
const outside = async () => (await page.locator('img').count()) - (await page.locator('[contenteditable="true"] img').count());
if ((await outside()) > 0) {
  await page.mouse.click(899, 133); // 見出し画像の「×」
  await page.waitForTimeout(2500);
  console.log('after remove, header imgs:', await outside());
}
await page.mouse.click(331, 121);
const [chooser] = await Promise.all([page.waitForEvent('filechooser', { timeout: 15000 }), page.getByText('画像をアップロード').click()]);
await chooser.setFiles(image);
await page.getByRole('button', { name: '保存', exact: true }).click();
await page.waitForTimeout(4000);
await page.getByRole('button', { name: '下書き保存' }).click();
await page.getByText('保存しました').first().waitFor({ timeout: 30000 }).catch(() => {});
await page.waitForTimeout(1500);
if (shot) await page.screenshot({ path: shot });
console.log('header imgs now:', await outside());
await browser.close();
