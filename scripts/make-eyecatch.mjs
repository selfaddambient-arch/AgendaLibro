// note の見出し画像（1280×670）を作る。
import { chromium } from 'playwright';
import { pathToFileURL } from 'node:url';
const page = '/Users/keikawaguchi/AntiGravity/AgendaLibro/books/uchi-no-mise/eyecatch.html';
const out = 'books/uchi-no-mise/note/';
const items = {
  'eyecatch-a.png': ['うちの店は、|うちの仕様で', '19席のバー店主が、AIで予約システムから道具まで自分で作った記録'],
  'eyecatch-ch1.png': ['第1章|AIから予約される店', '『うちの店は、うちの仕様で』'],
  'eyecatch-ch2.png': ['第2章|予約システムの裏側', '『うちの店は、うちの仕様で』技術編'],
  'eyecatch-ch3.png': ['第3章|自分の店の道具を、|他の店に配る', '『うちの店は、うちの仕様で』'],
  'eyecatch-ch4.png': ['第4章|一人で製品を作り続ける仕組み', '『うちの店は、うちの仕様で』技術編'],
  'eyecatch-ch5.png': ['第5章|小さな店の、これから', '『うちの店は、うちの仕様で』'],
  'eyecatch-ep.png': ['おわりに', '『うちの店は、うちの仕様で』'],
  'eyecatch-b.png': ['2冊目を、1日で書いて、|無料で配るまで', '『うちの店は、うちの仕様で』出版の経緯'],
};
const b = await chromium.launch();
const p = await b.newPage({ viewport: { width: 1280, height: 670 } });
for (const [f, [t, s]] of Object.entries(items)) {
  await p.goto(pathToFileURL(page).href + '?t=' + encodeURIComponent(t) + '&s=' + encodeURIComponent(s));
  await p.screenshot({ path: out + f });
}
await b.close();
