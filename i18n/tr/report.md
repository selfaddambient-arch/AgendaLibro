# トルコ語（tr）報告

（サブエージェントの返答から親の窓が作成）

## 状態
- 翻訳、レビュー反映、表紙、組版（PDF・Google Play 用 EPUB）、ストア文言まで完了。
- gate.py（I18N_LANG=tr）NG 0、epubcheck エラー0。表紙の題名・副題・著者名は Apple Vision（tr-TR）で100%一致。構造は英語版と行数まで一致（本1は1609行、本2は1133行）。
- PDF：本1が93ページ、本2が107ページ。
- Google Play は本1・本2とも新規。Kindle は非対応（kindle=false、Kindle 用 EPUB なし）。

## 題名の案（既定は1案目）
- 本1：①Yapay Zekâ Müdür Yardımcısı（副題：Sadece konuşun, yapay zekâ halleder. Beklediğinizden çok daha fazlasını.）／②Dükkânı Tek Başıma Çeviriyorum, Yanıma Yapay Zekâ Geldi／③Tek Kişilik Dükkân Sahipleri İçin Yapay Zekâ Rehberi
- 本2：①Barımıza Göre Yapıldı（副題：19 Koltuklu Bir Barın Sahibi, Rezervasyondan Araçlara Kadar Her Şeyi Yapay Zekâyla Nasıl Kurdu）／②Dükkânımız, Kendi Şartlarımızla／③Bar Sahipleri İçin Yapay Zekâyla Kendi Rezervasyon Sistemini Kurma Rehberi
- 既定を実践ガイド型に変えるかは代表の判断。

## 決めたこと
- 敬称 siz。人物は名前・役割・o（性別を示さない）。性別を示す語に直す指摘は不採用。
- 手帳の名前（辞書）：Mesai Defteri、Kârlılık Defteri、İkinci Mekân Defteri、Destek Rehberi、Işık Defteri、Sohbet Defteri。窓の案（辞書に無い3つ）：Maliyet Defteri、Müdavim Defteri、Vardiya Defteri。黒革の手帳＝Siyah Deri Defter。
- 副店長＝müdür yardımcısı、AI＝yapay zekâ、コラム＝Not Kutusu、図＝Şekil、おわりに＝Son Söz、3つの出口＝Üç Kapı。店は dükkân／mekân／bar／restoran（mağaza は使わない）。koltuk→tabure、本番環境＝canlı、コース料理＝menü。
- 数字は dot（¥8.500、$9,3、%40）。1ドル＝150円（換算日 2026-10-29）。時刻は24時間表記。書体 Baskerville。i/İ・ı/I は表紙の帯を手で大文字化（KİŞİLİK）、CSS の大文字化は不使用。

## レビュー
- agy を章ごとに実行（本1が9本、本2が11本）。全章に返事あり、Gemini API 不使用、未対応0。全件を `*/review-log.md` に記録。
- 主な直し：月末締めを「閉店」と訳していた、「昨日まで」の反転、「istemem」の意味逆転、AI にツールを「教える」側の逆転、パート従業員を「共同経営者」と訳していた、「紹介制」の読み違い。
- 不採用：辞書の名前を変える案、命令形を叙述に直す案、「19 koltuklu」を「19 kişilik」に直す案。
- 費用：翻訳は API 不使用、レビューは agy のみ。画像生成なし。

## 親への依頼・気づいた点
1. review-agy.sh の背景実行が数章ごとに途中で切れた（終了コード144）。再実行で続きから済ませた。
2. 「Kindle だけ最低価格が付く」の括弧は日本語原稿にあるのでトルコ語版にも残した。tr は Kindle 非対応なので、本文から外すかは判断。
3. 窓の案の3つ（Maliyet、Müdavim、Vardiya Defteri）を Hub の辞書に入れる場合は本文の語と合わせる。
4. Hub の BOOK_SRC_ALLOWLIST、屯の FUNNEL_SRC_ALLOWLIST に `b1-tr-gp`／`b2-tr-gp` などの追加が必要。

## Hub への引き渡し
- 印：`b1-tr-pdf／-gp`、`b2-tr-pdf／-gp`。
- `i18n/tr/`：`lang.json`、`glossary.add.yaml`、`work/style.md`、`store-copy.part.html`、`<slug>/metadata.yaml`、`<slug>/work/store.json`（一行紹介 本1:145字／本2:148字、説明文 本1:175語／本2:160語）、`<slug>/cover/cover.png`、`<slug>/build/*_tr.pdf`・`*_tr_gp.epub`、`<slug>/manuscript.md`、`<slug>/review-log.md`。
