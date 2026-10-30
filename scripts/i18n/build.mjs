// 多言語版の組版：PDF（A5・QR入り）と EPUB（Kindle 用・Google Play 用。中身は同じで、リンクの印だけ kindle／gp）。
//   I18N_LANG=en node scripts/i18n/build.mjs [slug…]      → i18n/<言語>/<slug>/build/
// 表紙は i18n/<言語>/<slug>/cover/cover.png（scripts/i18n/cover.mjs で作る）。奥付は i18n/<言語>/lang.json。
import { chromium } from 'playwright';
import { execFileSync } from 'node:child_process';
import { pathToFileURL } from 'node:url';
import { resolve } from 'node:path';
import { readFileSync, writeFileSync, mkdirSync, copyFileSync, existsSync } from 'node:fs';
import QRCode from 'qrcode';

const LG = process.env.I18N_LANG || 'en';
const NAME = { 'hitori-de-mise': 'bontaraku-01_hitori-de-mise', 'uchi-no-mise': 'bontaraku-02_uchi-no-mise' };
const lang = JSON.parse(readFileSync(`i18n/${LG}/lang.json`, 'utf8'));
const slugs = process.argv.slice(2).length ? process.argv.slice(2) : Object.keys(NAME);
const yml = (s) => Object.fromEntries(readFileSync(`i18n/${LG}/${s}/metadata.yaml`, 'utf8').split('\n').filter((l) => l.includes(':')).map((l) => [l.split(':')[0], l.slice(l.indexOf(':') + 1).trim().replace(/^"|"$/g, '')]));
const run = (cmd, args, opts = {}) => execFileSync(cmd, args, { stdio: 'inherit', ...opts });

const browser = await chromium.launch();
for (const slug of slugs) {
  const d = resolve(`i18n/${LG}/${slug}`), tmp = `${d}/build/.tmp`, out = `${d}/build`;
  mkdirSync(`${tmp}/_qr`, { recursive: true });
  const meta = yml(slug);
  const cover = `${d}/cover/cover.png`;
  if (!existsSync(cover)) throw new Error('表紙がありません: ' + cover);
  copyFileSync(cover, `${tmp}/cover.png`);
  // pandoc に渡す書誌
  writeFileSync(`${tmp}/meta.yaml`, ['title: ' + JSON.stringify(meta.title), 'subtitle: ' + JSON.stringify(meta.subtitle), 'author: ' + JSON.stringify(meta.author),
    'publisher: ' + JSON.stringify(meta.publisher), 'lang: ' + lang.bcp47, 'toc-title: ' + JSON.stringify(lang.toc_title), ...(lang.dir === 'rtl' ? ['dir: rtl'] : [])].join('\n') + '\n');
  writeFileSync(`${tmp}/pdf.css`, readFileSync('i18n/_common/pdf.css', 'utf8') + `\nbody { font-family: ${lang.font}; }\n`);
  writeFileSync(`${tmp}/epub.css`, readFileSync('i18n/_common/epub.css', 'utf8'));
  const resource = `--resource-path=${resolve('books', slug)}:${tmp}`;
  const prep = (fmt) => run('python3', ['scripts/i18n/prep.py', slug, fmt, `${tmp}/${fmt}.md`], { env: { ...process.env, I18N_LANG: LG } });

  // PDF（A5）
  prep('pdf');
  const exits = JSON.parse(readFileSync(`${tmp}/pdf.exits.json`, 'utf8'));
  for (const [f, url] of Object.entries(exits)) await QRCode.toFile(`${tmp}/_qr/${f}`, url, { width: 400, margin: 2 });
  run('pandoc', [`${tmp}/pdf.md`, '-f', 'markdown', '-t', 'html5', '--standalone', `--metadata-file=${tmp}/meta.yaml`, '--shift-heading-level-by=-1',
    '--toc', '--toc-depth=2', `--css=${tmp}/pdf.css`, resource, '--embed-resources', '-o', `${tmp}/pdf.html`]);
  const pp = await browser.newPage();
  await pp.goto(pathToFileURL(`${tmp}/pdf.html`).href);
  await pp.pdf({ path: `${tmp}/body.pdf`, format: 'A5', printBackground: true, displayHeaderFooter: true, headerTemplate: '<span></span>',
    footerTemplate: '<div style="font-size:8px;width:100%;text-align:center"><span class="pageNumber"></span></div>',
    margin: { top: '16mm', bottom: '16mm', left: '14mm', right: '14mm' } });
  await pp.close();
  execFileSync('sips', ['-s', 'format', 'jpeg', cover, '--out', `${tmp}/cover.jpg`], { stdio: 'ignore' });
  writeFileSync(`${tmp}/cover.html`, `<style>@page{size:148mm 210mm;margin:0}html,body{margin:0}img{display:block;width:148mm;height:210mm}</style><img src="cover.jpg">`);
  const cv = await browser.newPage();
  await cv.goto(pathToFileURL(`${tmp}/cover.html`).href);
  await cv.pdf({ path: `${tmp}/cover.pdf`, width: '148mm', height: '210mm', printBackground: true, margin: { top: 0, bottom: 0, left: 0, right: 0 } });
  await cv.close();
  run('pdfunite', [`${tmp}/cover.pdf`, `${tmp}/body.pdf`, `${out}/${NAME[slug]}_${LG}.pdf`]);

  // EPUB（Kindle 用・Google Play 用）
  for (const fmt of (lang.kindle === false ? ['gp'] : ['kindle', 'gp'])) {
    prep(fmt);
    run('pandoc', [`${tmp}/${fmt}.md`, '-f', 'markdown', '-t', 'epub3', `--metadata-file=${tmp}/meta.yaml`, '--shift-heading-level-by=-1', '--split-level=1',
      '--toc', '--toc-depth=2', `--epub-cover-image=${tmp}/cover.png`, `--css=${tmp}/epub.css`, resource, '-o', `${out}/${NAME[slug]}_${LG}_${fmt}.epub`]);
  }
  console.log('組版済み', LG, slug);
}
await browser.close();
