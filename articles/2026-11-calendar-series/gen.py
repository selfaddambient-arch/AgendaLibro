# 6本の記事原稿（NN/article.md）を designs.py から生成する。
import os, sys, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from designs import D
HUB = os.path.expanduser('~/AntiGravity/AgendaHub/public/cal/images')
BASE = os.path.dirname(os.path.abspath(__file__))
CAL = 'https://bontallc.com/cal'
FIRST_TITLE = '2027年は、壁に一枚。貼っても、額に入れても飾れるA1・A2・A3サイズの年間カレンダーを作りました'
FIRST_URL = 'https://note.com/bontallc/n/ncb3b34c01984'
THEMES = [
 (1, '和の文字', '5', ['18_zen_old_mincho_sumi','19_zen_kaku_blue','25_klee_hand','30_kaisei_kanji','33_rounded_pastel'],
  '注文ページの絞り込みにある「和の文字」の回です。漢数字や漢字の曜日、和風月名など、日本語の文字を生かした5種を紹介します。'),
 (2, '数字が主役', '4', ['03_plex_mono_grid','12_source_code_grey','24_anton_numerals','29_plex_linear'],
  '注文ページの絞り込みにある「数字が主役」の回です。等幅書体や大きな数字など、数字の見せ方に特徴のある4種を紹介します。最後の1種は横向きに飾るデザインです。'),
 (3, '暗い地と深い色', '4', ['14_bodoni_noir','34_gloock_bordeaux','17_big_shoulders_forest','35_dmserif_mediterranean'],
  '注文ページの絞り込みにある「暗い地」の回です。地の暗い3種に、深い色合いの1種を加えた4種を紹介します。'),
 (4, '色が楽しい', '5', ['16_space_grotesk_orange','23_outfit_tiles','27_rubik_riso','28_lexend_seasons','32_jost_bauhaus'],
  '注文ページの絞り込みにある「色が楽しい」の回です。色の使い方に特徴のある5種を紹介します。'),
 (5, '白・生成りのセリフ体', '5', ['02_fraunces_cream','11_source_serif_paper','15_cormorant_ivory','22_garamond_margin','26_playfair_months'],
  '注文ページの絞り込みにある「白・生成りでシンプル」から、セリフ体の5種を紹介する回です。'),
 (6, '白・生成りのサンセリフと横長', '4', ['10_source_sans_white','13_josefin_cream','31_sora_dots','21_manrope_landscape'],
  '注文ページの絞り込みにある「白・生成りでシンプル」から、サンセリフ体と横向きの4種を紹介する回です。最後の1種は横向きに飾るデザインです。'),
]
def title(n):
    t = THEMES[n-1]
    return f'壁に飾る2027年カレンダー｜{t[1]}の{t[2]}種' if n in (1,2,3,5,6) else f'壁に飾る2027年カレンダー｜{t[1]}{t[2]}種'
def url(code, n): return f'{CAL}?design={code}&utm_source=note&utm_campaign=cal-series-{n}'
def cal_url(n): return f'{CAL}?utm_source=note&utm_campaign=cal-series-{n}'
def link(u): return f'[{u}]({u})'
for n, theme, k, ids, lead in THEMES:
    d = os.path.join(BASE, f'{n:02d}'); os.makedirs(os.path.join(d, 'images'), exist_ok=True)
    o = [f'# {title(n)}', '',
         f'壁に飾る2027年カレンダーの紹介シリーズです。全6回のうち、この回は第{n}回「{theme}」です。',
         lead,
         '全30種のうち、はじめの3種（Swiss Grotesk・Shippori Washi・Night Lime）は最初の記事で紹介しています。', '']
    for i in ids:
        x = D[i]; shutil.copyfile(f'{HUB}/{i}.jpg', os.path.join(d, 'images', f'{i}.jpg'))
        o += [f'## {x["name"]}' + ('（横向きに飾る）' if x['land'] else ''), '',
              f'![{x["name"]} の見本](images/{i}.jpg)', '', x['text'],
              f'このデザインを選んだ状態で開く：{link(url(x["code"], n))}', '']
    o += ['## 選べること', '',
          'サイズはA1（594×841mm）・A2（420×594mm）・A3（297×420mm）から選べます。',
          'ポスター単体と額装セットがあり、額装セットの額はブラック・ホワイト・シルバーから選べます。',
          '月曜始まり・日曜始まりも選べます。',
          '名前やメッセージを入れるカスタマイズ（額装）もできます。',
          '価格（すべて送料込み・税込）は、ポスター単体がA1 4,400円／A2 2,980円／A3 2,200円、額装セットがA1 9,900円／A2 6,600円／A3 4,980円、カスタマイズ（額装）がA1 15,500円／A2 12,200円／A3 10,580円です。',
          '住所やデザインの好みがわからない相手には、「受け取りリンク」で贈れます。サイズと、額装セットかポスター単体かを選んで購入すると、受け取り用のリンクがメールで届きます。それをLINEやメールで相手に送ると、相手がデザインと額の色、お届け先を選びます。相手の画面に金額は表示されません。', '',
          '## 部屋に置いて見る', '',
          'スマホで注文ページ（bontallc.com/cal）を開き、デザイン・サイズ・種類を選んで「部屋に置いて見る（スマホのカメラが開きます）」を押すと、カメラで自分の部屋の壁に実物大で置いた様子を確かめられます。',
          '壁から1〜2m離れて、カメラを壁に向けます',
          'スマホをゆっくり左右に動かすと、額が壁に貼り付きます',
          '置いた後は指で動かさず、スマホを動かして眺めてください。置き直したいときは、いったん閉じてもう一度開きます', '',
          '## 年内にお届けしたい方へ', '',
          '年内にお届けしたい場合は、お早めにご注文ください。ご注文から約7〜10日で発送します。', '',
          '## 注文ページへ', '',
          'この回のデザインも、ほかのデザインも、注文ページで選べます。',
          link(cal_url(n)), '',
          '## シリーズの他の回', '']
    others = [FIRST_TITLE] + [title(m) for m in range(1, 7) if m != n]
    o += ['\n'.join(others), '']
    open(os.path.join(d, 'article.md'), 'w', encoding='utf8').write('\n'.join(o))
print('ok')
