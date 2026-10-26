// 組版：cover.png → EPUB → PDF（A5）。
//   node scripts/build.mjs
import { chromium } from 'playwright';
import { execFileSync } from 'node:child_process';
import { pathToFileURL } from 'node:url';
import { resolve } from 'node:path';

const book = resolve('books/uchi-no-mise');
const name = 'bontaraku-02_uchi-no-mise';
const tmp = `${book}/build/.tmp`;
execFileSync('mkdir', ['-p', tmp]);
const run = (cmd, args, opts = {}) => execFileSync(cmd, args, { stdio: 'inherit', cwd: book, ...opts });

execFileSync('node', ['scripts/make-qr.mjs'], { stdio: 'inherit' });
const browser = await chromium.launch();

// 仮表紙 1600×2560
const cp = await browser.newPage({ viewport: { width: 1600, height: 2560 } });
await cp.goto(pathToFileURL(`${book}/cover.html`).href);
await cp.screenshot({ path: `${book}/build/cover.png` });

// EPUB3
run('python3', ['../../scripts/preprocess.py', 'epub', `${tmp}/epub.md`]);
run('pandoc', [
  `${tmp}/epub.md`, '-f', 'markdown+east_asian_line_breaks', '-t', 'epub3',
  '--metadata-file=metadata.yaml', '--shift-heading-level-by=-1', '--split-level=1',
  '--toc', '--toc-depth=2', '--epub-cover-image=build/cover.png', '--css=epub.css',
  '--resource-path=.', '-o', `build/${name}.epub`,
]);

// PDF（A5・QR入り）
run('python3', ['../../scripts/preprocess.py', 'pdf', `${book}/build/.tmp/pdf.md`]);
run('pandoc', [
  `${book}/build/.tmp/pdf.md`, '-f', 'markdown+east_asian_line_breaks', '-t', 'html5', '--standalone',
  '--metadata-file=metadata.yaml', '--shift-heading-level-by=-1', '--toc', '--toc-depth=2',
  '--css=pdf.css', '--resource-path=.', '--embed-resources', '-o', `${book}/build/.tmp/pdf.html`,
]);
const pp = await browser.newPage();
await pp.goto(pathToFileURL(`${book}/build/.tmp/pdf.html`).href);
await pp.pdf({
  path: `${book}/build/${name}_A5.pdf`, format: 'A5', printBackground: true, displayHeaderFooter: true,
  headerTemplate: '<span></span>',
  footerTemplate: '<div style="font-size:8px;width:100%;text-align:center"><span class="pageNumber"></span></div>',
  margin: { top: '16mm', bottom: '16mm', left: '14mm', right: '14mm' },
});
await browser.close();
