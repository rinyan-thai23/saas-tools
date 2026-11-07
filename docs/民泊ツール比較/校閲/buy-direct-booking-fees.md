# 校閲レポート：buy-direct-booking-fees

- 照合先：事実カード 9製品（Guesty、Hostaway、Lodgify、OwnerRez、Hospitable、iGMS、Uplisting、Beds24、Sirvoy）
- 件数：要修正 0 ／ 注意 2 ／ 軽微 3
- 照合して一致を確認した主張：約70（手数料表9行、機能・決済表9行、計算値2点、結論3点、条件別3点、未確認の一覧）

## 指摘

### 1. 注意：結論2の列挙に Lodgify の「決済経由1%」が入っていない
- 記事（結論2）：「ツール側に率が書かれていたのは、Hospitable、Hostaway（上位サイトのみ）、Guesty Lite の従量プラン（1%）、iGMS の無料プラン（4%）、Uplisting の従量プラン（3%／1.5%）です。」
- 記事（結論1）：「ツール側の予約手数料が0%でも、決済会社（Stripe 等）の手数料は別にかかります。」
- カード：Lodgify「決済手数料」「A transaction fee of 1% applies to payments your guests make online through a payment gateway such as Stripe or PayPal.」ゲートウェイ側の手数料は別。「8. 注意」「決済手数料1%は全プラン共通…（ゲートウェイ手数料とは別）」。つまり Lodgify の1%はツール側の費用。
- 問題：結論だけ読むと Lodgify は「ツール側の率なし」に見える。表と「条件別」には1%が書かれているので、結論だけの欠落。
- 修正案：結論2に「Lodgify（決済ゲートウェイ経由の支払いに1%）」を加える。

### 2. 注意：Lodgify の【確認済】は公式本体ではなく公開コピーで確認したもの
- 記事：Lodgify 行（予約手数料0%・決済経由1%・Starter 以上・32言語・EUR/USD/GBP）の【確認済】、出典欄の webflow-mkt.lodgify.com。冒頭「【確認済】は公式ページを開いて確認」。
- カード：Lodgify 調査の前提：www.lodgify.com は 403 で開けず、webflow-mkt.lodgify.com の公開コピーで代用。「www 側の同名ページと内容が同一かは未照合」。
- 修正案：Lodgify 行か出典欄に「公式の公開コピーで確認。本体サイトとの一致は未照合」と注記する。

### 3. 軽微：「円で決済したい人」の言い回しが Beds24 の表の記載と並べて読むと紛らわしい
- 記事：「日本のStripeでの円決済が使えると公式に確認できた製品はありません。」
- 記事（表）：Beds24「宿泊料の JPY は、公式Wiki（Airbnb 連携の通貨設定）の抜粋に含まれる」。
- カード：Beds24「通貨（JPY）」Wiki の対応通貨リストに JPY（検索抜粋で確認）。日本の販売会社の案内では「Stripe決済ごとに3.6%」。日本のStripeでの円決済が使えるかを明記した記載ではない。
- 評価：事実としては矛盾しないが、「JPY が通貨設定にある」ことと「日本の Stripe で円決済できる」ことが別だと分かるようにしたい。
- 修正案：「宿泊料の通貨に JPY が含まれる記載は Beds24 の Wiki にあるが、日本の Stripe での円決済が使える旨の公式記載はなし」。

### 4. 軽微：「未確認のこと」に Hospitable・iGMS の決済の日本対応が入っていない
- 記事：「日本のStripeアカウントでの利用可否（Guesty、Hostaway、Lodgify、OwnerRez、Uplisting、Sirvoy）、円での価格設定」
- カード：Hospitable「ダイレクト予約の決済の日本対応は未確認」（記事の表にも同じ記載あり）。iGMS「Stripe の対応国・通貨も未確認」「円の設定は第三者のみ」。
- 修正案：未確認の一覧に Hospitable、iGMS、（Beds24 の日本発行カード・Stripe 利用可否も確認していなければ）を加える。

### 5. 軽微：Hostaway の「ゲストに1.8%上乗せ」が Pro の説明の一部に読める
- 記事：「上位の Booking Website Pro は月$49＋対象予約の0.5%。ゲストに1.8%を上乗せ（米国のみ）【確認済】」
- カード：Hostaway「ダイレクト予約手数料」Pro の文言と、"Hostaway also marks up and charges a 1.8% fee directly to guests (US only)." は別の文として並ぶ。どの商品の費用かは明記されていない。
- 修正案：「（別の記載として）ゲストに1.8%を上乗せ（米国のみ）。どの商品にかかるかは公式の文面からは不明」。

## 確認した範囲の補足（指摘なし）
- 計算値：「月100万円なら 0.5%＝5,000円、1%＝1万円、4%＝4万円」は正しい。OwnerRez Hosted Sites「5室で$29」（15＋5＋3×3）も正しい（カードの料金表と一致）。
- 内部リンク：/go/ は Guesty、Hostaway、Lodgify、OwnerRez、Hospitable、iGMS、Uplisting、Beds24 のみ。Sirvoy への /go/ なし。PriceLabs・Hostfully は対象外と明記。
- PR 表記：冒頭あり、各リンクに（PR）あり。
- 日本語の確認範囲：Sirvoy（31言語・日本語あり）と Beds24（言語コード ja）はカードと一致。Guesty は「第三者のみ」と明記、Hostaway は「日本語なし（第三者のみ）」と確度どおり。
- 法的な断定なし。届出番号の表示欄は「確認する」項目としてのみ登場。
