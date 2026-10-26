# 挿絵 index（REGIA-20261026-01・全4窓分）

| ファイル名 | 内容 | 挿入先の節 | 撮影URL | 備考 |
|---|---|---|---|---|
| fig1-2_plan-tabs.png | 予約フォームのメニュー選択。4つのタブが全部見える | 第1章 | https://tamuroreservation.vercel.app/ （本番・閲覧のみ） | 時間を1つ選んだ状態（タブはその後に出る）。入力・送信なし |
| fig1-3a_calendar-today.png | カレンダーで「本日」が黒枠で強調された状態（凡例にも「本日」） | 第1章 | https://tamuroreservation.vercel.app/ （本番・閲覧のみ） | 撮影日の10/26（月）が本日。貸切・臨時休業の表示は実際の店のカレンダー |
| fig1-3b_confirm-today.png | 確認画面。日時が「本日」バッジ付きで大きく出た状態 | 第1章 | https://tamuro-reservation-dev.vercel.app/confirm （dev） | 「次へ」まで進めて、送信はしていない。実データの書き込みなし |
| fig1-4_talk.png | /talk で最初の選択肢を1回押した直後（人数の質問が出た） | 第1章 | https://tamuro-reservation-dev.vercel.app/talk （dev） | **「ひとりで今夜」という選択肢はこの製品に無い**。撮影時刻（深夜1時）の最初の4択は「味付け／いつから／名前の由来／予約したいです」で、その「予約したいです」を押した。本番では会話の撮影をしない決まりなので dev |
| fig1-5_confirm-mail.png | 予約確定メール（合成データ） | 第1章 | （HTMLを lib/mail.ts の sendReservationEmail から生成して描画） | 送信なし。「本日の話題」にあたる欄は **「当日のトークテーマ」**（Q.…／A: …／B: …）。氏名「山田 太郎」・example.com |
| fig1-6_weekly-report.png | 週次レポートメールの上部（合成データ） | 第1章 | （lib/weekly-report-synthetic.ts の合成データで生成して描画） | 上から約1240pxまで。週は2031-03-10〜16の合成。実送信なし |
| fig1-7_group-discount.png | 6名を選んだときの料金欄（複数割8%・−¥2,928・¥33,672） | 第1章 | https://tamuroreservation.vercel.app/ （本番・閲覧のみ） | スタンダードプラン×6。送信なし |
| fig1-7b_compare.png | 1名・4名・6名の料金欄を横に並べた比較 | 第1章 | 上と同じ（3回の料金欄を合成して並置） | 1名¥5,900／4名¥22,692（複数割7%）／6名¥33,672（複数割8%） |
| fig1-8_welcome-plans.png | 「おかえり＆はじめまして」プランが選べる画面 | 第1章 | https://tamuroreservation.vercel.app/ （本番・閲覧のみ） | メニューのA満喫コースの先頭 |
| fig1-9_stamp-card.png | マイページの来店回数（通算3回・次の特典まであと2回） | 第1章 | https://tamuro-reservation-dev.vercel.app/mypage （dev） | **「スタンプカード」は無い**ため、来店回数カードで代用。合成会員（山田 太郎）をdevに作り、撮影後に削除済み |
| fig1-10_unanswered.png | 管理画面「答えられなかった質問」（未確認5件） | 第1章 | http://localhost:3100/admin/questions （ローカルのエミュレータ） | 合成の質問5件。撮影後に全件削除。上のナビ帯は切り落とし |
| fig2-1_mcp.svg | 構成図：お客さんのAI → 屯のMCPサーバー → 屯の予約システム、下段に「条件入りの予約ページURL」が左へ戻る矢印、「確定はお客さんが押す」の注記 | 第2章（図2-1） | —（描画） | xmllint 通過。白地・墨の線 |
| fig2-1_mcp.png | 同上の PNG（2000×880） | 第2章（図2-1） | —（描画） | SVG を倍率2で描画 |
| fig2-2_test-result.png | AI試験の結果（合格率と原因別）を等幅フォントで描画 | 第2章 | （HTML描画） | **本文の値（1,775件・28.5％）ではなく、実ログ**（docs/talk-eval/判定_2026-10-04.md：36本中9本合格＝25.0％、原因R1〜R5）。本文の値の内訳が手元に無いため。差し替えが要るなら数値を指示してほしい |
| fig2-3_rules-before-after.png | 公開読み取りだった頃のルールと修正後（左右） | 第2章 | （HTML描画） | 実コミット 8e26a7e の前後から、reservations の部分だけ（各10行以内）。鍵・識別子なし |
| fig2-4_requirements.png | T-AI-MURO 要件定義書 第3版の目次 | 第2章 | （HTML描画） | docs/Tamuro_chat_window_requirements_v3.md の見出し12個だけ。本文なし |
| fig3-1a_luce-open.png | 予約ページ上部の灯り手帳の埋め込み（営業中） | 第3章 | https://tamuroreservation.vercel.app/ （本番・閲覧のみ） | 撮影時は閉店中だったため、**状態の応答だけをブラウザ内で営業中に差し替え**（本番のLuceには何も送っていない） |
| fig3-1b_luce-extended.png | 同・延長営業中（朱色の「+30分」） | 第3章 | 同上 | 指示は staging の Luce で延長を押す方法だったが、Luce の staging が手元に無いため、同じ差し替えで再現。文言は Luce の ja 辞書とdisplay生成の規則どおり |
| fig3-2_agenda-lp.png | 玄関 /agenda の冒頭（上端から4:3＝2560×1920。ヘッダーと最初の製品の項。全体の画像は _orig/agenda-lp_full.png） | 第3章（図3-2） | https://bontallc.com/agenda | 本番。ふだんの表示（?via=book なし） |
| fig3-3a_timbro.png | 打刻手帳の詳細ページのファーストビュー（390×844） | 第3章（図3-3a） | https://bontallc.com/agenda/timbro | 紹介写真の店名は自社の店（屯）、スタッフは架空（AgendaTimbro の撮影用固定データ） |
| fig3-3b_oro.png | 採算手帳の詳細ページのファーストビュー（390×844） | 第3章（図3-3b） | https://bontallc.com/agenda/oro | 本番 |
| fig3-3c_bis.png | 2軒目手帳の詳細ページのファーストビュー（390×844） | 第3章（図3-3c） | https://bontallc.com/agenda/bis | 本番 |
| fig3-4_timbro-kiosk.png | 打刻画面（店舗端末）。合成スタッフ「佐藤 花子」「山田 太郎」「鈴木 一郎」が未出勤で並ぶ | 3-4 | staging `/agendatimbro/`（テスト用ログインの persona の店舗に端末を登録して表示）| 1024×768・倍率2。名簿は実 API の応答から persona 自身の行（「TEST 」で始まる合成名2件）だけを撮影時に外した。この幅ではカードが細く、名前が1字ずつ縦に折り返す（製品側の既存の見え方・コードは変えていない）。店名は persona の合成名「TEST timbro-owner / timbro」 |
| fig3-5_qa-languages.png | 相談手帳で言語切替メニューを開き、20言語が並んだ状態 | 第3章（図3-5） | https://bontallc.com/agendaqa | 幅1280。メニューの高さが画面の高さの約6割で頭打ちのため、20言語が一度に入る 1280×1520 で開き、上から980pxを切り出した（390×844 では17言語まで） |
| fig3-6a_luce-admin.png | 管理画面。看板が OPEN（点灯中・閉店予定 18:00）で、延長ボタン「閉店予定を 18:30 まで延ばす（＋30分）」が見える | 3-6 | staging `/agendaluce/admin?storeId=<合成店舗>` | 看板のカードと延長ボタンが1枚に入るよう縦 929px（CSS）で切り出し |
| fig3-6b_luce-admin-extended.png | 延長を1回押した直後。閉店予定 18:30・お客さまの画面に朱色の「＋30分」・「延長しました。お客さまの画面にも出ています。」 | 3-6 | 同上 | 縦 1013px（CSS）で切り出し |
| fig3-6c_luce-public.png | 同じ店の公開ページ。「延長営業中 ＋30分」「18:30 まで延長」 | 3-6 | staging `/agendaluce/s/<合成スラッグ>?lang=ja` | 撮影後に延長を取り消し、管理画面「点灯中」・公開ページ「営業中」・＋30分の札0件に戻ったことを確認 |
| fig4-1_series.svg | 構成図：上 AgendaHub（玄関）、中に7つの手帳、下 AgendaID。手帳はすべて ID へ線 | 第4章（図4-1） | —（描画） | xmllint 通過。識別色は手帳の上辺の面のみ。原価手帳（Ricetta）は色の正本に未登録のため無彩の面 |
| fig4-1_series.png | 同上の PNG（2080×1000） | 第4章（図4-1） | —（描画） | SVG を倍率2で描画 |
| fig4-2_bootstrap-steps.png | 新しい手帳を立ち上げる工程（工程／実行者の2列・15行） | 第4章（図4-2） | —（描画） | 正本 product-bootstrap SKILL.md §4-17（工程1〜24）を15行に要約。パス名・鍵名は載せていない |
| fig4-3_identity-colors.png | 識別色の一覧（製品名／呼び名／色見本・13製品） | 第4章（図4-3） | —（描画） | 正本 design/agenda-tokens.json（0.7.0）の全13製品。準備中の製品も含む。Ricetta は正本に色が無いため載せていない |
| fig4-4_series-nav.png | 管理画面のナビ（モバイル）。上の帯（製品名・言語・相談手帳・Agendaシリーズを見る）と、設定シート（スタッフ・店舗・プラン・打刻の画面へ・相談手帳）を開いた状態 | 4-4 | staging `/agendatimbro/admin/staff`（テスト用ログイン timbro-owner）| 390×844・倍率2。モバイルでは縦のサイドバーは上の帯＋下タブ＋設定シートに分かれる。全項目が1画面に入る形として設定シートを開いて撮った（下タブの勤怠表・勤務データはシートの下に隠れる）。メールは合成アドレス |
| fig5-1_summary.png | 全体図：お客さんのAI →（MCPという窓）→ 屯 →（道具になって渡る）→ 他の店。屯の下に「店の個性に向き合う」 | 第5章 5-5（図5-1） | —（描画。fig5-1_summary.svg から） | 原稿の語句のみ。代表指示（2026-10-26）で追加 |
