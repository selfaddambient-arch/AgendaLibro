// PDF 用の QR を3つ作る。リンクは原稿の「3つの出口」と同じ文字列。
import QRCode from 'qrcode';
const out = 'books/uchi-no-mise/images/_qr/';
const links = {
  'qr-tamuro.png': 'https://tamuroreservation.vercel.app/?src=book',
  'qr-agenda.png': 'https://bontallc.com/agenda?via=book',
  'qr-note.png': 'https://note.com/bontallc',
};
for (const [f, url] of Object.entries(links)) await QRCode.toFile(out + f, url, { width: 400, margin: 2 });
