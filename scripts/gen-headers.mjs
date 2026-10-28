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

// 本の切り替え：環境変数 BOOK（既定は 2冊目 uchi-no-mise）。画像は books/<略名>/note-headers/ に保存する
const SLUG = process.env.BOOK || 'uchi-no-mise';
const OUTDIR = `books/${SLUG}/note-headers`;
const PALETTES = {
  'uchi-no-mise': '色彩は、手本のベージュ基調から変えて、夜のバーの紺（ネイビー）と琥珀（アンバー）を基調にする。壁・空・背景の広い面は深い紺、灯り・木の家具・グラスは琥珀色にし、茶色やオレンジが画面の大半を占めないようにする。',
  'hitori-de-mise': '色彩は、手本に近い、昼の店の明るい生成り（クリーム）・深い緑・からし色を基調にする。壁・背景の広い面は生成り、家具や小物は緑とからし色にし、紺や黒を画面の大半に使わない。昼の自然光の雰囲気にする。',
};
const PALETTE = PALETTES[SLUG];

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

const BOOK_ITEMS = {
  'uchi-no-mise': {
  intro: '東中野の小さなバーのカウンター。19席ほどの小さな店で、カウンターの中に人物が立ち、客席のスツールは空いている。小さな灯りがいくつか下がっている。',
  ch1: 'スマートフォンに話しかける客と、それを受け止める店。左に、スマホに話しかけている客（手本の人物とは別の服装でよい）、右に、カウンターの中の店主。二人の間を、小さな光の点の列が結んでいる。吹き出しは、色の丸だけで表す。壁の黒板や額縁は無地にする。',
  ch2: '机に向かい、プログラムを点検する人物。画面は、文字のない色の帯と色の四角だけで表す。夜の静かな部屋。',
  ch3: '色違いの手帳が並ぶ棚と人物。棚に、色の違う手帳が7冊ほど並び、人物が一冊を手に取って見ている。手帳の背は無地の色の面にし、文字や模様は描かない。棚や壁の飾りも無地にする。',
  ch4: '複数の画面が並ぶ机に向かう人物。大きな机に、画面が4枚ほど並び、人物は背中側から少し見える。画面の中身は抽象的な図形だけ。',
  ch5: '夜の店の灯りと、開いた本。窓の外に夜の街、店の暖かい灯り、手前に開かれた本。人物は小さく遠くに立つ。',
  ep: '灯りのついた店の入口。夜、木の扉と暖かい灯りがこぼれる小さな店の前に、人物が立ち、扉を開けようとしている。看板・扉・窓は無地の色の面にし、木目や模様や文字は描かない。',
  magazine: 'カウンター・手帳・本を一枚にまとめた絵。バーのカウンターの上に、数冊の手帳と、開いた一冊の本、グラスが置かれ、背景に夜の店の灯り。人物は後ろの方に小さく立つ。手帳の表紙は無地にし、本のページは無地の淡い色の面だけにして、文字や点の模様は描かない。壁の黒板や看板も無地にする。',
},
  'hitori-de-mise': {
    intro: '東中野の地下にある小さな店の昼。ハンバーグカレー店のカウンターの中に人物が立ち、客席は空いている。窓のない地下の店に暖かい灯り。',
    ch1: 'AIエージェントという新しい従業員。厨房で人物が仕込みをし、その横に、小さなロボット型のAIアシスタントが並んで手伝っている。吹き出しの中は、色の丸だけにし、記号や数字や文字に見える形は描かない。',
    ch2: '長い文章を打ったスマホから、図解スライドが生まれる場面。人物がスマホを持ち、横に、色の丸や四角の面だけでできた簡単な図解の紙が浮かぶ（文字・矢印・線は入れない）。',
    ch3: 'クリエイティブと集客の自動化。テーブルに、色とりどりのイラストの紙、バナー、丸いロゴのマークが並び、人物が一枚を手に取って眺めている。紙には文字を入れず、絵柄だけにする。',
    ch4: 'ワインリストをスマホで撮るだけ。人物がテーブルのワインボトルのラベルをスマホで撮影している。横に、できあがった一覧の紙（文字は入れず、文字のない色の帯だけで表す）。',
    ch5: '経営分析と利益改善。カウンターに電卓、棒グラフと円グラフの描かれた紙、料理の絵だけを描いた丸いコースターのようなカードが並び、人物が見比べている（メニュー表や、文字の書かれた紙は描かない）。グラフは色の面の棒と円だけにし、文字や数字は入れない。紙・電卓・カードの縁や細かな模様は描かず、細い濃い線を使わない。壁のポスターや回路のチップにも、AIなどの文字は書かない。',
    ch6: '自分の店専用のシステム開発。夜のカウンター席でノートパソコンに向かう人物。画面は、文字のない色の帯と色の四角だけで表す、横に小さなスマホアプリの画面。',
    ep: '未来のレシピ。昼の窓辺で、人物が開いたレシピノートと本を手に、微笑んでいる。ノートに文字は入れず、絵柄だけにする。',
    magazine: 'ハンバーグカレーの店のカウンター・手帳・本・スマホをまとめた一枚の絵。カウンターの上に、カレーの皿、手帳、開いた本、スマホが置かれ、後ろに小さく人物が立つ。手帳や本は無地の色の面だけにして、文字・模様・細い濃い線を描かない。カウンターの木目も描かない。',
  },
};
const ITEMS = BOOK_ITEMS[SLUG];

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
  appendFileSync(`${OUTDIR}/usage.log`, `${new Date().toISOString()} ${slug}${suffix} http=${r.status} ok=${!!part} in=${u?.promptTokenCount} out=${u?.candidatesTokenCount}\n`);
  if (!part) { console.log(slug, 'FAILED', r.status, JSON.stringify(d).slice(0, 300).replace(key, '***')); continue; }
  const b64 = (part.inlineData || part.inline_data).data;
  const f16 = `${OUTDIR}/16x9/${slug}${suffix}.png`;
  writeFileSync(f16, Buffer.from(b64, 'base64'));
  const fn = `${OUTDIR}/note/${slug}${suffix}.png`;
  // 横を 1280 に合わせて縮め、中央を高さ 670 で切り出す
  execFileSync('sips', ['--resampleWidth', '1280', f16, '--out', fn], { stdio: 'ignore' });
  execFileSync('sips', ['-c', '670', '1280', fn], { stdio: 'ignore' });
  console.log(slug, 'ok', f16);
}
