// note のプロフィール（自己紹介）を直す（代表承認 2026-10-28）。
//   node scripts/note-profile.mjs
// 「1人で店を回す、その横にAIが来た。」→「一人で店を回す、その横にAIが来た。」、末尾に本の一覧の行。ほかは変えない。
import { chromium } from 'playwright';
// 140文字に収めるため、代表の指示（2026-10-28）で「飲食店向けAIセミナーなどを開催」と bit.ly の行を外し、短い行にした
const LINE = '本：https://bontallc.com/books?via=note';
const b = await chromium.launch({ headless: false, channel: 'chrome', ignoreDefaultArgs: ['--enable-automation'], args: ['--disable-blink-features=AutomationControlled'] });
const ctx = await b.newContext({ storageState: 'secrets/note-state.json', locale: 'ja-JP', viewport: { width: 1280, height: 1000 } });
const p = await ctx.newPage();
await p.goto('https://note.com/settings/profile');
const ta = p.locator('textarea[name="editBiography"]');
await ta.waitFor({ timeout: 60000 });
await p.waitForTimeout(2000);
const before = await ta.inputValue();
console.log('BEFORE\n' + before);
let next = before.replace(/^飲食店向けAIセミナーなどを開催\n/m, '').replace(/\nhttp:\/\/bit\.ly\/\S+\s*$/, '').replace('1人で店を回す、その横にAIが来た。', '一人で店を回す、その横にAIが来た。');
// 自己紹介は140文字まで。入らないときは足さない
if (!next.includes(LINE) && (next.replace(/\s+$/, '') + '\n' + LINE).length <= 140) next = next.replace(/\s+$/, '') + '\n' + LINE;
await ta.click();
await p.keyboard.press('Meta+A');
await p.keyboard.insertText(next);
await p.waitForTimeout(800);
await p.locator('button:not([disabled])', { hasText: /^保存$/ }).last().click();
await p.waitForTimeout(5000);
await p.goto('https://note.com/settings/profile');
await p.locator('textarea[name="editBiography"]').waitFor({ timeout: 60000 });
await p.waitForTimeout(2000);
const after = await p.locator('textarea[name="editBiography"]').inputValue();
console.log('AFTER\n' + after);
console.log(JSON.stringify({ 旧題名: (after.match(/1人で店を回す/g) || []).length, 新題名: after.includes('一人で店を回す、その横にAIが来た。'), 行: after.includes(LINE) }));
await b.close();
