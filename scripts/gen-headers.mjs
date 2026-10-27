// note の見出し画像を Gemini の画像生成（Nano Banana 系）で作る。
//   node scripts/gen-headers.mjs [--only slug,slug] [--suffix _r2]
// 手本は books/_style/flat-character/ の画像を毎回付ける。16:9 を note-headers/16x9/、中央 1280×670 を note-headers/note/ に保存。
// 鍵は secrets/.env の GEMINI_API_KEY（値は出力しない）。
import { readFileSync, writeFileSync, readdirSync, appendFileSync } from 'node:fs';
import { execFileSync } from 'node:child_process';

const MODEL = 'gemini-nano-banana-2.1';
const key = readFileSync('secrets/.env', 'utf8').match(/GEMINI_API_KEY=(.*)/)[1].trim().replace(/^["']|["']$/g, '');
const argv = process.argv.slice(2);
const only = argv.includes('--only') ? argv[argv.indexOf('--only') + 1].split(',') : null;
const suffix = argv.includes('--suffix') ? argv[argv.indexOf('--suffix') + 1] : '';

const STYLE = `フラットデザインの挿絵を描いてください。添付した手本画像と同じ画風・同じ人物（灰青の髪・緑の上着・からし色のズボン・白い靴、回路模様のあしらい）で、人物は30代後半の印象にしてください。
- グラデーションは使わない。ベタ塗りの面と細い線で描く。
- 画像の中に文字・数字・ロゴ・看板の文字を一切入れない（文字に見える模様も入れない）。
- 色彩は、手本のベージュ基調から変えて、夜のバーの紺（ネイビー）と琥珀（アンバー）を基調にする。壁・空・背景の広い面は深い紺、灯り・木の家具・グラスは琥珀色にし、茶色やオレンジが画面の大半を占めないようにする。
- アングルやポーズは自由。手や顔を崩さない。横長16:9。
場面：`;

const ITEMS = {
  intro: '東中野の小さなバーのカウンター。19席ほどの小さな店で、カウンターの中に人物が立ち、客席のスツールは空いている。小さな灯りがいくつか下がっている。',
  ch1: 'スマートフォンに話しかける客と、それを受け止める店。左に、スマホに話しかけている客（手本の人物とは別の服装でよい）、右に、カウンターの中の店主。二人の間を、細い回路の線が結んでいる。吹き出しは記号だけで文字は入れない。',
  ch2: '机に向かい、プログラムを点検する人物。画面には、丸や四角の図形とチェックの印だけを描く（行や文字に見える横線の並びは描かない）。夜の静かな部屋。',
  ch3: '色違いの手帳が並ぶ棚と人物。棚に、色の違う手帳が7冊ほど並び、人物が一冊を手に取って見ている。手帳の背に文字は入れない。',
  ch4: '複数の画面が並ぶ机に向かう人物。大きな机に、画面が4枚ほど並び、人物は背中側から少し見える。画面の中身は抽象的な図形だけ。',
  ch5: '夜の店の灯りと、開いた本。窓の外に夜の街、店の暖かい灯り、手前に開かれた本。人物は小さく遠くに立つ。',
  ep: '灯りのついた店の入口。夜、木の扉と暖かい灯りがこぼれる小さな店の前に、人物が立ち、扉を開けようとしている。看板に文字は入れない。',
  magazine: 'カウンター・手帳・本を一枚にまとめた絵。バーのカウンターの上に、数冊の手帳と、開いた一冊の本、グラスが置かれ、背景に夜の店の灯り。人物は後ろの方に小さく立つ。手帳の表紙は無地にし、本のページは図形の絵だけにして文字に見える線は描かない。',
};

const refs = readdirSync('books/_style/flat-character').filter((f) => /\.(png|jpg)$/.test(f)).sort().map((f) => ({
  inline_data: { mime_type: f.endsWith('png') ? 'image/png' : 'image/jpeg', data: readFileSync('books/_style/flat-character/' + f).toString('base64') },
}));

for (const [slug, scene] of Object.entries(ITEMS)) {
  if (only && !only.includes(slug)) continue;
  const body = { contents: [{ parts: [{ text: STYLE + scene }, ...refs] }], generationConfig: { responseModalities: ['IMAGE'], imageConfig: { aspectRatio: '16:9' } } };
  const r = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/${MODEL}:generateContent`, {
    method: 'POST', headers: { 'content-type': 'application/json', 'x-goog-api-key': key }, body: JSON.stringify(body),
  });
  const d = await r.json();
  const part = d.candidates?.[0]?.content?.parts?.find((p) => p.inlineData || p.inline_data);
  const u = d.usageMetadata;
  appendFileSync('books/uchi-no-mise/note-headers/usage.log', `${new Date().toISOString()} ${slug}${suffix} http=${r.status} ok=${!!part} in=${u?.promptTokenCount} out=${u?.candidatesTokenCount}\n`);
  if (!part) { console.log(slug, 'FAILED', r.status, JSON.stringify(d).slice(0, 300).replace(key, '***')); continue; }
  const b64 = (part.inlineData || part.inline_data).data;
  const f16 = `books/uchi-no-mise/note-headers/16x9/${slug}${suffix}.png`;
  writeFileSync(f16, Buffer.from(b64, 'base64'));
  const fn = `books/uchi-no-mise/note-headers/note/${slug}${suffix}.png`;
  // 横を 1280 に合わせて縮め、中央を高さ 670 で切り出す
  execFileSync('sips', ['--resampleWidth', '1280', f16, '--out', fn], { stdio: 'ignore' });
  execFileSync('sips', ['-c', '670', '1280', fn], { stdio: 'ignore' });
  console.log(slug, 'ok', f16);
}
