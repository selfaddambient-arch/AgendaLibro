// プレスリリース送付先リストの機械ゲート（読み取りのみ。送信・入力はしない）。
//   node scripts/press-gate.mjs
// 1. 全行に根拠のページURLがある  2. 送付先がメールの行は、根拠ページにそのアドレスが実在する
//    （本文に表示＝innerText。「mailtoリンク」と記した行だけ、リンク先 href にあること）
// 3. 20件以上30件以下  4. 根拠ページに「プレスリリース／情報提供／取材／リリース」のいずれかの語がある（受付先の確認）
import { chromium } from 'playwright';
import { readFileSync } from 'node:fs';

function parseCsv(t) {
  const rows = []; let row = [], cur = '', q = false;
  for (let i = 0; i < t.length; i++) {
    const c = t[i];
    if (q) { if (c === '"' && t[i + 1] === '"') { cur += '"'; i++; } else if (c === '"') q = false; else cur += c; }
    else if (c === '"') q = true;
    else if (c === ',') { row.push(cur); cur = ''; }
    else if (c === '\n') { row.push(cur); rows.push(row); row = []; cur = ''; }
    else if (c !== '\r') cur += c;
  }
  if (cur || row.length) { row.push(cur); rows.push(row); }
  return rows;
}
const [head, ...data] = parseCsv(readFileSync('books/uchi-no-mise/press/targets.csv', 'utf8'));
const col = Object.fromEntries(head.map((h, i) => [h, i]));
const browser = await chromium.launch();
const ctx = await browser.newContext({ locale: 'ja-JP', userAgent: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/130.0 Safari/537.36' });
const cache = new Map();
async function load(u) {
  if (cache.has(u)) return cache.get(u);
  const p = await ctx.newPage();
  let out = { ok: false, text: '', mailto: [] };
  try {
    const r = await p.goto(u, { waitUntil: 'load', timeout: 45000 });
    await p.waitForTimeout(1500);
    out = { ok: r.status() < 400, status: r.status(), text: (await p.locator('body').innerText()).replace(/\s+/g, ' '), mailto: await p.$$eval('a[href^="mailto:"]', (as) => as.map((a) => a.getAttribute('href').replace('mailto:', '').split('?')[0])) };
  } catch (e) { out.err = e.message.slice(0, 60); }
  await p.close(); cache.set(u, out); return out;
}
let fail = 0; const byMethod = {}; const bad = [];
for (const r of data.filter((r) => r.length > 1)) {
  const [name, , method, dest, evidence, , , where] = [r[col['媒体名']], 0, r[col['送付方法']], r[col['送付先']], r[col['根拠のページURL']], 0, 0, r[col['アドレスの確認箇所']]];
  byMethod[method] = (byMethod[method] || 0) + 1;
  if (!/^https?:\/\//.test(evidence)) { bad.push(`${name}: 根拠URLなし`); fail++; continue; }
  const pg = await load(evidence);
  if (!pg.ok) { bad.push(`${name}: 根拠ページを開けない ${pg.status ?? pg.err}`); fail++; continue; }
  if (!/プレスリリース|情報提供|取材|リリース/.test(pg.text)) { bad.push(`${name}: 根拠ページに受付の語がない`); fail++; }
  if (method === 'メール') {
    const inText = pg.text.includes(dest);
    const inMailto = pg.mailto.includes(dest);
    if (where === '本文' && !inText) { bad.push(`${name}: ${dest} が本文にない`); fail++; }
    if (where === 'mailtoリンク' && !inMailto) { bad.push(`${name}: ${dest} がmailtoリンクにない`); fail++; }
  }
}
await browser.close();
const n = data.filter((r) => r.length > 1).length;
console.log(`行数 ${n}（20〜30）/ 送付方法別 ${JSON.stringify(byMethod)}`);
bad.forEach((b) => console.log('  NG:', b));
const ok = fail === 0 && n >= 20 && n <= 30;
console.log(ok ? 'GATE PASS' : 'GATE FAIL');
process.exit(ok ? 0 : 1);
