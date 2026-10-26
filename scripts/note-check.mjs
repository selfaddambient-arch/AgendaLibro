// 保存済みの下書きを開き直して、題名・字数・画像数を機械実測する。
//   node scripts/note-check.mjs <editor URL> <保存先.png>
import { chromium } from 'playwright';
const [url, shot] = process.argv.slice(2);
const b = await chromium.launch({ headless: false, channel: 'chrome', ignoreDefaultArgs: ['--enable-automation'], args: ['--disable-blink-features=AutomationControlled'] });
const c = await b.newContext({ storageState: 'secrets/note-state.json', locale: 'ja-JP', viewport: { width: 1280, height: 900 } });
const p = await c.newPage();
await p.goto(url);
await p.getByPlaceholder('記事タイトル').waitFor({ timeout: 60000 });
await p.waitForTimeout(5000);
console.log('title:', await p.getByPlaceholder('記事タイトル').inputValue());
console.log('chars:', (await p.locator('body').innerText()).match(/(\d[\d,]*)\s*文字/)?.[1]);
console.log('body images:', await p.locator('[contenteditable="true"] img').count(), '| all imgs:', await p.locator('img').count());
console.log('markers left:', (await p.locator('body').innerText()).includes('[[IMG'));
await p.screenshot({ path: shot });
await b.close();
