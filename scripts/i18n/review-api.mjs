// レビューの予備経路：agy の枠が尽きたとき、Gemini API（secrets/.env の GEMINI_API_KEY）で同じレビューを行う。
//   I18N_LANG=ms node scripts/i18n/review-api.mjs [slug]
// agy 版（review-agy.sh）と同じ頼み方・同じ置き場（<名前>.gemini.md）。費用は 1言語あたり 数十円の見込み。
import { readFileSync, writeFileSync, readdirSync, existsSync, statSync } from 'node:fs';
const LG = process.env.I18N_LANG || 'en';
const MODEL = process.env.GEMINI_MODEL || 'gemini-3.8-flash';
const key = readFileSync('secrets/.env', 'utf8').match(/GEMINI_API_KEY=(.*)/)[1].trim().replace(/^["']|["']$/g, '');
const NAME = JSON.parse(readFileSync(`i18n/${LG}/lang.json`, 'utf8')).name;
const PRE = `You are a careful bilingual reviewer (Japanese and ${NAME}). The text below is one part of a Japanese nonfiction book (a solo bar owner using AI) and its ${NAME} translation, made by AI. Review the translation. Reply in Japanese, as a numbered list only. Each item: the type (① 意味の取り違え ② 不自然な表現 ③ その言語の読者に伝わらない箇所), the exact quoted passage of the translation, the problem in one line, and a suggested fix in ${NAME}. Also report any heading/number mismatch, changed fact or number, lost sentence, or leftover Japanese. Do not rewrite the whole text. If there is nothing to report in a category, say so briefly.`;
const slugs = process.argv[2] ? [process.argv[2]] : ['hitori-de-mise', 'uchi-no-mise'];
let tin = 0, tout = 0;
for (const slug of slugs) {
  const dir = `i18n/${LG}/${slug}/review`;
  for (const f of readdirSync(dir).filter((n) => /^\d.*\.md$/.test(n) && !/\.(gemini|chatgpt)\.md$/.test(n)).sort()) {
    const out = `${dir}/${f.replace(/\.md$/, '.gemini.md')}`;
    if (existsSync(out) && statSync(out).size > 0) { console.log('skip', out); continue; }
    const body = { contents: [{ parts: [{ text: PRE + '\n\n' + readFileSync(`${dir}/${f}`, 'utf8') }] }], generationConfig: { temperature: 0.2 } };
    const r = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/${MODEL}:generateContent`, { method: 'POST', headers: { 'content-type': 'application/json', 'x-goog-api-key': key }, body: JSON.stringify(body) });
    const d = await r.json();
    const text = d.candidates?.[0]?.content?.parts?.map((p) => p.text || '').join('');
    if (!text) { console.log('NG', r.status, JSON.stringify(d).slice(0, 200).replace(key, '***')); process.exit(3); }
    writeFileSync(out, text);
    tin += d.usageMetadata?.promptTokenCount || 0; tout += d.usageMetadata?.candidatesTokenCount || 0;
    console.log('ok', out, text.length);
  }
}
console.log('ALLDONE', { tin, tout });
