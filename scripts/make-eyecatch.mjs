// note の見出し画像（1280×670）を作る。
import { chromium } from 'playwright';
import { pathToFileURL } from 'node:url';
const page = '/Users/keikawaguchi/AntiGravity/AgendaLibro/books/uchi-no-mise/eyecatch.html';
const out = 'books/uchi-no-mise/note/';
const items = {
  'eyecatch-a.png': ['うちの店は、|うちの仕様で', '19席のバー店主が、AIで予約システムから道具まで自分で作った記録'],
  'eyecatch-b.png': ['2冊目を、1日で書いて、|無料で配るまで', '『うちの店は、うちの仕様で』出版の経緯'],
};
const b = await chromium.launch();
const p = await b.newPage({ viewport: { width: 1280, height: 670 } });
for (const [f, [t, s]] of Object.entries(items)) {
  await p.goto(pathToFileURL(page).href + '?t=' + encodeURIComponent(t) + '&s=' + encodeURIComponent(s));
  await p.screenshot({ path: out + f });
}
await b.close();
