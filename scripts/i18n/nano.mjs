// Nano Banana（Gemini の画像生成）の呼び出し。鍵は secrets/.env の GEMINI_API_KEY（値は出さない）。
//   node scripts/i18n/nano.mjs cover <slug> [suffix]     → i18n/en/<slug>/cover/art<suffix>.png（文字なしの絵）
//   node scripts/i18n/nano.mjs trial <slug> <入力画像> <出力.png> "<指示>"   → 画面写真の日本語を英語に描き換える試し
// 使った量は i18n/en/nano-usage.log に1行ずつ残す（費用の上限：画像全体で300円）。
import { readFileSync, writeFileSync, appendFileSync } from 'node:fs';
const MODEL = 'gemini-nano-banana-2.1';
const key = readFileSync('secrets/.env', 'utf8').match(/GEMINI_API_KEY=(.*)/)[1].trim().replace(/^["']|["']$/g, '');
const [mode, slug, a3, a4, a5] = process.argv.slice(2);
const mime = (f) => (f.endsWith('png') ? 'image/png' : 'image/jpeg');
const b64 = (f) => readFileSync(f).toString('base64');

async function call(parts, aspect) {
  const body = { contents: [{ parts }], generationConfig: { responseModalities: ['IMAGE'], ...(aspect ? { imageConfig: { aspectRatio: aspect } } : {}) } };
  const r = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/${MODEL}:generateContent`, {
    method: 'POST', headers: { 'content-type': 'application/json', 'x-goog-api-key': key }, body: JSON.stringify(body) });
  const d = await r.json();
  const part = d.candidates?.[0]?.content?.parts?.find((p) => p.inlineData || p.inline_data);
  const u = d.usageMetadata;
  appendFileSync('i18n/en/nano-usage.log', `${new Date().toISOString()} ${mode} ${slug} http=${r.status} ok=${!!part} in=${u?.promptTokenCount} out=${u?.candidatesTokenCount}\n`);
  if (!part) { console.log('FAILED', r.status, JSON.stringify(d).slice(0, 400).replace(key, '***')); process.exit(1); }
  return Buffer.from((part.inlineData || part.inline_data).data, 'base64');
}

if (mode === 'cover') {
  const ref = slug === 'hitori-de-mise' ? 'books/hitori-de-mise/cover/cover.jpg' : 'books/uchi-no-mise/build/cover.png';
  const suffix = a3 || '';
  const prompt = `添付の本の表紙イラストと同じ絵柄（フラットなベクター調）・同じ構図・同じ色調・同じ時間帯の雰囲気で、文字を一切含まない版を描いてください。
やること：
- 題名・副題・著者名・下部の帯の文字・ロゴ・星のマークを、すべて取り除く。取り除いた所は、壁・天井・照明などの絵で自然に埋める。
- 画面の上の約3分の1は、後から英語の題名を重ねるため、静かで模様の少ない壁面と、吊り下げ照明だけにする。
- 画像の中に、文字・数字・記号・看板やメニューの文字を入れない。新聞やパソコン画面など文字が入りそうな物は、文字のない灰色や色の帯で表す。
- 縦長の本の表紙の構図（縦横比 2:3）にする。`;
  const img = await call([{ text: prompt }, { inline_data: { mime_type: mime(ref), data: b64(ref) } }], '2:3');
  writeFileSync(`i18n/en/${slug}/cover/art${suffix}.png`, img);
  console.log('ok', `i18n/en/${slug}/cover/art${suffix}.png`, img.length);
} else if (mode === 'trial') {
  const [inp, out, instr] = [a3, a4, a5];
  const img = await call([{ text: instr }, { inline_data: { mime_type: mime(inp), data: b64(inp) } }]);
  writeFileSync(out, img);
  console.log('ok', out, img.length);
}
