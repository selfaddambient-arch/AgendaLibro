// note ログイン用ブラウザ。代表が見える画面でログインし、目印ファイルを置くと
// ログイン状態（storageState）だけを secrets/note-state.json に保存して終わる。
// パスワードは扱わない。
//   node scripts/note-login.mjs          （ブラウザを開いて待つ）
//   touch secrets/.login-done            （ログイン後に窓が置く）
import { chromium } from 'playwright';
import { existsSync, mkdirSync, rmSync } from 'node:fs';

const SENTINEL = 'secrets/.login-done';
const STATE = 'secrets/note-state.json';

mkdirSync('secrets', { recursive: true });
rmSync(SENTINEL, { force: true });

const browser = await chromium.launch({ headless: false });
const context = await browser.newContext({ locale: 'ja-JP', viewport: { width: 1280, height: 900 } });
const page = await context.newPage();
await page.goto('https://note.com/login');
console.log('note ログイン待ち。ログイン後、' + SENTINEL + ' を置くと保存します。');

while (!existsSync(SENTINEL)) await new Promise((r) => setTimeout(r, 2000));

await context.storageState({ path: STATE });
rmSync(SENTINEL, { force: true });
await browser.close();
console.log('保存しました：' + STATE);
