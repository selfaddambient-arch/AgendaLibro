// 屯の予約MCP記事（articles/2026-11-mcp-muse）の見出し画像を Nano Banana 系で作る（1回限り）。
//   node scripts/gen-mcp-header.mjs [--suffix _r2]
// 画風・手本の付け方は scripts/gen-headers.mjs と同じ。鍵は secrets/.env の GEMINI_API_KEY（値は出さない）。
import { readFileSync, writeFileSync, readdirSync, appendFileSync } from 'node:fs';
import { execFileSync } from 'node:child_process';

const MODEL = 'gemini-nano-banana-2.1';
const key = readFileSync('secrets/.env', 'utf8').match(/GEMINI_API_KEY=(.*)/)[1].trim().replace(/^["']|["']$/g, '');
const argv = process.argv.slice(2);
const suffix = argv.includes('--suffix') ? argv[argv.indexOf('--suffix') + 1] : '';
const OUTDIR = 'articles/2026-11-mcp-muse/note-header';
const PALETTE = '色彩は、手本のベージュ基調から変えて、夜のバーの紺（ネイビー）と琥珀（アンバー）を基調にする。壁・空・背景の広い面は深い紺、灯り・木の家具・グラスは琥珀色にし、茶色やオレンジが画面の大半を占めないようにする。';

const STYLE = `輪郭線・縁取り・線画を一切使わない。形は色の面だけ。手本の線の描き方は写さない。

最優先の指示（必ず守る）：
- 輪郭線・縁取り・線画を使わない。形は色の面の切り替えだけで表す。
- 添付した手本の画像は、人物の姿（髪・服の色・体つき）を写すためだけに使う。線の描き方は写さない。
- 画像の中に文字・数字・記号・看板の文字を入れない（メニュー表や画面も、文字のない色の帯で表す）。

フラットデザインの挿絵を描いてください。手本と同じ人物（灰青の髪・緑の上着・からし色のズボン・白い靴）で、人物は30代後半の印象にしてください。回路模様のあしらいは、線ではなく、小さな色の点や面で表す。
- グラデーションは使わない。ベタ塗りの色の面だけで描く。
- ${PALETTE}
- アングルやポーズは自由。手や顔を崩さない。横長16:9。
場面：`;
const SCENE = '夜のバーのカウンター席。手本の人物がスツールに座り、片手に持ったスマートフォンに話しかけている。スマートフォンの画面から、文字のない丸い吹き出しの形をした琥珀色の面がいくつか浮かび、点々と連なって、カウンターの奥にともる琥珀色の灯りへつながっている（AIが店に問い合わせて予約を取りにいく様子）。スマートフォンの画面は、文字のない色の帯と色の四角だけで表す。人物は1人だけ。キャラクターやマスコット、ロボットは描かない。看板・壁・棚は無地の色の面にし、文字や模様は描かない。瓶・ボトル・棚の上の小物は描かない。';

const refs = readdirSync('books/_style/flat-character').filter((f) => /\.(png|jpg)$/.test(f)).sort().map((f) => ({
  inline_data: { mime_type: f.endsWith('png') ? 'image/png' : 'image/jpeg', data: readFileSync('books/_style/flat-character/' + f).toString('base64') },
}));
const body = { contents: [{ parts: [{ text: STYLE + SCENE }, ...refs] }], generationConfig: { responseModalities: ['IMAGE'], imageConfig: { aspectRatio: '16:9' } } };
const r = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/${MODEL}:generateContent`, {
  method: 'POST', headers: { 'content-type': 'application/json', 'x-goog-api-key': key }, body: JSON.stringify(body),
});
const d = await r.json();
const part = d.candidates?.[0]?.content?.parts?.find((p) => p.inlineData || p.inline_data);
const u = d.usageMetadata;
appendFileSync(`${OUTDIR}/usage.log`, `${new Date().toISOString()} mcp${suffix} http=${r.status} ok=${!!part} in=${u?.promptTokenCount} out=${u?.candidatesTokenCount}\n`);
if (!part) { console.log('FAILED', r.status, JSON.stringify(d).slice(0, 300).split(key).join('***')); process.exit(1); }
const f16 = `${OUTDIR}/16x9/mcp${suffix}.png`;
writeFileSync(f16, Buffer.from((part.inlineData || part.inline_data).data, 'base64'));
const fn = `${OUTDIR}/note/mcp${suffix}.png`;
execFileSync('sips', ['--resampleWidth', '1280', f16, '--out', fn], { stdio: 'ignore' });
execFileSync('sips', ['-c', '670', '1280', fn], { stdio: 'ignore' });
console.log('ok', f16, fn);
