// 組版：表紙 → EPUB → PDF（A5）。
//   node scripts/build.mjs
import { chromium } from 'playwright';
import { execFileSync } from 'node:child_process';
import { pathToFileURL } from 'node:url';
import { resolve } from 'node:path';
import { writeFileSync, existsSync, readFileSync } from 'node:fs';

// 本の切り替え：環境変数 BOOK（既定は 2冊目 uchi-no-mise）。設定は books/<略名>/book.json
const slug = process.env.BOOK || 'uchi-no-mise';
const book = resolve(`books/${slug}`);
const cfg = existsSync(`${book}/book.json`) ? JSON.parse(readFileSync(`${book}/book.json`, 'utf8')) : {};
const name = cfg.name || 'bontaraku-02_uchi-no-mise';
const tmp = `${book}/build/.tmp`;
execFileSync('mkdir', ['-p', tmp]);
const run = (cmd, args, opts = {}) => execFileSync(cmd, args, { stdio: 'inherit', cwd: book, ...opts });

execFileSync('node', ['scripts/make-qr.mjs'], { stdio: 'inherit', env: { ...process.env, BOOK: slug } });
const browser = await chromium.launch();

// 表紙：book.json の cover が html なら cover.html を 1600×2560 で撮る（仮表紙）。無ければ画像（Gemini生成）を長辺2560pxへ拡大（KDPの下限）
if (cfg.cover?.type === 'image') {
  // 加工済みの 1600×2560 の画像（scripts/make-cover.py で作る）をそのまま使う
  execFileSync('sips', ['-s', 'format', 'png', `${book}/${cfg.cover.file}`, '--out', `${book}/build/cover.png`], { stdio: 'ignore' });
  execFileSync('cp', [`${book}/${cfg.cover.file}`, `${tmp}/cover.jpg`]);
} else if (cfg.cover?.type === 'html') {
  const cp = await browser.newPage({ viewport: { width: 1600, height: 2560 } });
  await cp.goto(pathToFileURL(`${book}/${cfg.cover.file}`).href);
  await cp.screenshot({ path: `${book}/build/cover.png` });
  execFileSync('sips', ['-s', 'format', 'jpeg', `${book}/build/cover.png`, '--out', `${tmp}/cover.jpg`], { stdio: 'ignore' });
} else {
  const coverSrc = `${book}/images/Gemini_Generated_Image_tbl9pjtbl9pjtbl9.jpeg`;
  execFileSync('sips', ['-z', '2560', '1718', '-s', 'format', 'png', coverSrc, '--out', `${book}/build/cover.png`], { stdio: 'ignore' });
  execFileSync('sips', ['-z', '2560', '1718', '-s', 'format', 'jpeg', coverSrc, '--out', `${tmp}/cover.jpg`], { stdio: 'ignore' });
}

// EPUB3
run('python3', ['../../scripts/preprocess.py', 'epub', `${tmp}/epub.md`], { env: { ...process.env, BOOK: slug } });
run('pandoc', [
  `${tmp}/epub.md`, '-f', 'markdown+east_asian_line_breaks', '-t', 'epub3',
  '--metadata-file=metadata.yaml', '--shift-heading-level-by=-1', '--split-level=1',
  '--toc', '--toc-depth=2', '--epub-cover-image=build/cover.png', '--css=epub.css',
  '--resource-path=.', '-o', `build/${name}.epub`,
]);

// PDF（A5・QR入り）：表紙は余白なしの1ページを別に作り、本文の前に連結する
run('python3', ['../../scripts/preprocess.py', 'pdf', `${book}/build/.tmp/pdf.md`], { env: { ...process.env, BOOK: slug } });
run('pandoc', [
  `${book}/build/.tmp/pdf.md`, '-f', 'markdown+east_asian_line_breaks', '-t', 'html5', '--standalone',
  '--metadata-file=metadata.yaml', '--shift-heading-level-by=-1', '--toc', '--toc-depth=2',
  '--css=pdf.css', '--resource-path=.', '--embed-resources', '-o', `${book}/build/.tmp/pdf.html`,
]);
const pp = await browser.newPage();
await pp.goto(pathToFileURL(`${book}/build/.tmp/pdf.html`).href);
await pp.pdf({
  path: `${tmp}/body.pdf`, format: 'A5', printBackground: true, displayHeaderFooter: true,
  headerTemplate: '<span></span>',
  footerTemplate: '<div style="font-size:8px;width:100%;text-align:center"><span class="pageNumber"></span></div>',
  margin: { top: '16mm', bottom: '16mm', left: '14mm', right: '14mm' },
});
writeFileSync(`${tmp}/cover.html`, `<style>@page{size:148mm 210mm;margin:0}html,body{margin:0}img{display:block;width:148mm;height:210mm}</style><img src="cover.jpg">`);
const cv = await browser.newPage();
await cv.goto(pathToFileURL(`${tmp}/cover.html`).href);
await cv.pdf({ path: `${tmp}/cover.pdf`, width: '148mm', height: '210mm', printBackground: true, margin: { top: 0, bottom: 0, left: 0, right: 0 } });
await browser.close();
execFileSync('pdfunite', [`${tmp}/cover.pdf`, `${tmp}/body.pdf`, `${book}/build/${name}_A5.pdf`]);

