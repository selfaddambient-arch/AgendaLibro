// note 下書き7本の機械ゲート。
//   node scripts/note-gate.mjs
// 1. 7本の本文が原稿（「はじめに」以降）と一致：原稿の各行（図の印はキャプション、表はセル、見出し・リスト記号は除く）が
//    7本の本文のどこかにあること。【図・強調記号・【 】（末尾の【ストアURL】仮行を除く）が残っていないこと
// 2. 各記事の「全7回の◯回目」と、末尾の案内リンクがすべて ?src=note / ?via=note 付きであること
// 3. 公開状態の記事が 0 本（公開側の一覧とキーの突き合わせ。未ログインで開けないこと）
import { chromium } from 'playwright';
import { readFileSync } from 'node:fs';
import { execFileSync } from 'node:child_process';

const book = 'books/uchi-no-mise';
const drafts = JSON.parse(readFileSync(`${book}/note/drafts.json`, 'utf8'));
const slugs = ['intro', 'ch1', 'ch2', 'ch3', 'ch4', 'ch5', 'ep'];
const norm = (t) => t.replace(/[\s　]+/g, '');

// ---- 原稿から期待する行を作る
const ms = readFileSync(`${book}/bontaraku-02_uchi-no-mise_manuscript.md`, 'utf8').split('\n');
const start = ms.findIndex((l) => l.startsWith('## はじめに'));
// 図のキャプションの上書き（scripts/preprocess.py の CAPTION_OVERRIDE）
const caps = JSON.parse(execFileSync('python3', ['-c', "import importlib.util,json;s=importlib.util.spec_from_file_location('p','scripts/preprocess.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m);print(json.dumps(m.CAPTION_OVERRIDE,ensure_ascii=False))"], { encoding: 'utf8' }));
const expected = [];
for (const raw of ms.slice(start)) {
  let l = raw.trim();
  if (!l) continue;
  const m = l.match(/^【図(\d+-\d+[a-z]?)】(.*)$/);
  if (m) { expected.push(`図${m[1]}${caps[m[1]] ?? m[2]}`); continue; }
  if (/^\|\s*-/.test(l)) continue;
  if (l.startsWith('|')) { l.replace(/^\||\|$/g, '').split('|').map((c) => c.trim()).filter(Boolean).forEach((c) => expected.push(c)); continue; }
  l = l.replace(/^#+\s*/, '').replace(/^(\d+\.|-)\s+/, '').replace(/^>\s?/, '').replace(/\[([^\]]+)\]\(([^)]+)\)/g, '$1').replace(/\\_/g, '_');
  expected.push(l.replace('この本は無料で配っています。', 'この本は、PDFとnoteとGoogle Playで無料で読めます（Kindleだけは、ストアの決まりで最低価格を付けています）。')); // note だけの書き換え（2026-10-27 代表指示）
}

const browser = await chromium.launch({ headless: false, channel: 'chrome', ignoreDefaultArgs: ['--enable-automation'], args: ['--disable-blink-features=AutomationControlled'] });
const ctx = await browser.newContext({ storageState: 'secrets/note-state.json', locale: 'ja-JP', viewport: { width: 1280, height: 900 } });
const page = await ctx.newPage();
let all = '';
const report = [];
let fail = 0;
for (const [i, slug] of slugs.entries()) {
  await page.goto(`https://editor.note.com/notes/${drafts[slug]}/edit/`);
  await page.getByPlaceholder('記事タイトル').waitFor({ timeout: 60000 });
  await page.waitForTimeout(5000);
  const body = page.locator('[contenteditable="true"]').first();
  const text = await body.innerText();
  all += text + '\n';
  const links = await body.evaluate((el) => [...el.querySelectorAll('a')].map((a) => a.href));
  const footIdx = text.indexOf('この本の、ほかの読み方');
  const foot = footIdx >= 0 ? text.slice(footIdx) : '';
  const tail = links.slice(-2);
  const okTail = tail.length === 2 && tail[0] === 'https://tamuroreservation.vercel.app/?src=note' && tail[1] === 'https://bontallc.com/agenda?via=note';
  const okNo = text.includes(`全7回の${i + 1}回目`);
  const stray = (text.match(/【図|\*\*|【/g) || []).length - (foot.match(/【ストアURL】/g) || []).length;
  report.push({ slug, key: drafts[slug], chars: text.length, 全7回: okNo, 案内リンク: okTail, 残り記号: stray, 画像: await body.locator('img').count() });
  if (!okNo || !okTail || stray !== 0) fail++;
}
const A = norm(all);
const missing = expected.filter((e) => !A.includes(norm(e)));
console.log(JSON.stringify(report, null, 1));
console.log(`原稿の行 ${expected.length} / 本文に見つからない ${missing.length}`);
missing.slice(0, 15).forEach((m) => console.log('  欠け:', m.slice(0, 60)));

// ---- 公開状態 0 本
const pub = await ctx.request.get('https://note.com/api/v2/creators/bontallc/contents?kind=note&page=1&per_page=50');
const keys = Object.values(drafts).concat('n580b9262d396');
const pubText = await pub.text();
const published = keys.filter((k) => pubText.includes(k));
const anon = await browser.newContext();
const anonStatus = [];
for (const k of keys) anonStatus.push((await anon.request.get(`https://note.com/bontallc/n/${k}`)).status());
console.log('公開一覧 HTTP', pub.status(), '/ 一覧にある下書きキー', published.length, '/ 未ログインでの記事URL', anonStatus.join(','));
await browser.close();
const ok = fail === 0 && missing.length === 0 && published.length === 0 && anonStatus.every((s) => s === 404);
console.log(ok ? 'GATE PASS' : 'GATE FAIL');
process.exit(ok ? 0 : 1);
