// PDF 用の QR を3つ作る。リンクは原稿の「3つの出口」と同じ文字列。本は環境変数 BOOK（既定 uchi-no-mise）。
import QRCode from 'qrcode';
import { existsSync, readFileSync, mkdirSync } from 'node:fs';
const slug = process.env.BOOK || 'uchi-no-mise';
const cfgPath = `books/${slug}/book.json`;
const cfg = existsSync(cfgPath) ? JSON.parse(readFileSync(cfgPath, 'utf8')) : {};
const out = `books/${slug}/images/_qr/`;
mkdirSync(out, { recursive: true });
const links = cfg.qr_urls || {
  'qr-tamuro.png': 'https://tamuroreservation.vercel.app/?src=book',
  'qr-agenda.png': 'https://bontallc.com/agenda?via=book',
  'qr-note.png': 'https://note.com/bontallc',
};
for (const [f, url] of Object.entries(links)) await QRCode.toFile(out + f, url, { width: 400, margin: 2 });
