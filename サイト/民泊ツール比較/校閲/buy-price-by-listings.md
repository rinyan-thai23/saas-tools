# 校閲：buy-price-by-listings

校閲日 2026-11-07 ／ 照合カード：Guesty, Hostaway, Lodgify, OwnerRez, Hospitable, iGMS, Uplisting, Beds24, Sirvoy, PriceLabs, Hostfully-Guidebooks（項目「2. 料金」）
再計算した合計値：OwnerRez 3/10/20室、Hospitable 3〜20室、iGMS 3〜20室（PRO・PRO+・年払い）、Uplisting 5〜20室、Beds24 海外公式 1〜20室、PriceLabs 3〜20室、Guesty Lite 3室。すべて一致（換算なし、通貨はカードのまま）。
件数：要修正 1 ／ 注意 4 ／ 軽微 3

## 要修正

### 1. 「円建ては Beds24 の日本の販売会社だけ」は、他社の円建て可否が「未確認」なのを「ない」と書いている
- 記事：結論3つ目「通貨は製品ごとに違い、円建ては Beds24 の日本の販売会社だけ」／条件別の表3行目「ツール利用料を円で払いたい｜Beds24 の日本の販売会社のみ円建て」
- カード：円建てなしを確認できているのは Uplisting（通貨にJPYなし、確認済）、Sirvoy（9通貨にJPYなし）、Beds24 海外公式（JPYは含まれない）、Lodgify（表示は EUR／USD／GBP のみ）。一方、Guesty「請求通貨」＝円が選べるかは未確認、Hostaway＝JPY請求の可否は未確認、iGMS＝未確認（円請求の可否）、Hospitable＝「JPY の記載は見つからず」、PriceLabs＝未確認（JPY請求）、Hostfully＝JPY請求の記載は見つからない（Japan は請求先国の選択肢にあり）。
- 修正案：「円建てと確認できたのは Beds24 の日本の販売会社だけ。Guesty・Hostaway・iGMS・Hospitable・PriceLabs・Hostfully は円建ての記載が見つからなかった（できないと確認したわけではない）」。条件別の行も同様に。

## 注意

### 1. 表の見出し「月額・月払い」と、表内の数字の支払い周期が揃っていない
- 記事：「料金早見表（月額・月払い…）」。Guesty Lite 行に Annual $20〜／Pay as you grow、Lodgify 行は初期表示の価格
- カード：Lodgify「1物件・USDの表示価格」＝「初期表示がどの支払い周期かは明示されておらず、…年払いと推定（推定）」。Guesty Lite の Annual は年払いプランの単価。
- 修正案：Lodgify 行に「年払いの可能性が高い（推定）」と明記し、Guesty の Annual は「年払い」と表示して見出しの「月払い」と区別する。

### 2. PriceLabs の合計値は「段階の読み方が解釈」であることが書かれていない
- 記事：PriceLabs 行（計）$28.97 など／表の読み方「日本は『Rest of the world』に当たると読んだが…」
- カード：PriceLabs「件数別の月額目安」＝確度「計算値（公式の計算機は実行していない。段階の読み方は文言からの解釈）」。
- 修正案：読み方の注に「各件数帯の単価を順に積み上げる解釈。公式の計算機は未実行」を追記。

### 3. 条件別「公式の料金だけで総額を見積もりたい｜…は表で出せる」は「総額」と言い切れない
- 記事：条件別の表1行目
- カード：OwnerRez＝表は基本料金のみで、Property Management・Hosted Sites・SMS・Rezzy AI・ロック連携等は別料金（OwnerRez 2. 料金「機能の追加課金」）。Beds24 海外公式＝各室が別の部屋タイプ・2チャネルの前提の算出値。Hospitable＝全物件が稼働の場合。
- 修正案：「基本料金の目安が出せる（機能の追加課金・前提は表の注を参照）」に変える。

### 4. Guesty Lite の「Limited time offer」表示が落ちている
- 記事：Guesty Lite 行（$9／$20／$29）
- カード：Guesty「課金モデル（Lite）」＝「"Limited time offer" の表示あり」。
- 修正案：表の読み方に「Lite の価格ページに期間限定の表示あり。現行の通常価格は未確認」を足す。

## 軽微

- 記事：「Lodgify、Hospitable、iGMS は税別と記載」。カードでは PriceLabs（単価表「税別」）も税別。他製品の税の扱い（Guesty・Uplisting・Beds24・Sirvoy）は未記載。修正案：PriceLabs を追加し、残りは「税の扱いは未確認」と書く。
- 記事：条件別の表4行目「予約手数料のかからないものを選びたい」。カードでは Sirvoy も「予約手数料 0％」（確認済）だが挙がっていない。修正案：Sirvoy を追記（網羅でないなら「例」と書く）。
- 記事末尾の HTML コメント「追加調査依頼」6件が公開ファイルに残る。修正案：ビルド時に除去。

## 指摘なし（照合して一致を確認した主張）：約62件
- Guesty：Lite 3種の単価、Pro 4〜199室は見積り・価格非公開、第三者の推定は載せない方針
- Hostaway：公式価格非公開・フォーム見積り
- Lodgify：Basic $14／Starter $26／Pro $47／Ultimate $68、Basic 1物件まで・Starter 2物件まで、3室以降は未確認
- OwnerRez：$40／$70／$88／$127／$196（再計算一致）
- Hospitable：Essentials $0／Host $29／Pro $59／Mogul $99、3〜20室の Pro・Mogul 合計（再計算一致）、Host は最大2物件、稼働物件のみ課金、料金ページ描画なし、Contact sales の第三者記録
- iGMS：PRO・PRO+ 全合計（再計算一致）、年払い PRO $38／$150／約$227、FLEX 1泊$1最低$20、無料プラン予約5件まで
- Uplisting：£40／£72／£90／£160／£260、従量プラン3%／1.5%
- Beds24：海外公式 €16.60／€24.00／€31.40／€49.90／€86.90（式 12.90＋2.60×室＋0.55×リンクで再計算一致）、日本の販売会社 ¥4,580／¥17,280／¥24,210（参考価格・3室5室は未確認）
- Sirvoy：Starter／Pro の全帯、Free 1室
- PriceLabs：$9.99／$28.97／$47.95／$92.90／$177.80（再計算一致）
- Hostfully Guidebooks：1冊まで無料、単価 $12／$10／$9／$7／$6、合計方式は未確認
- 結論1・2、条件別2行目・4行目の OwnerRez／Beds24／Lodgify 予約手数料なし・Lodgify の決済ゲートウェイ1%・Guesty Lite 予約の1%
- 申込リンクは /go/ のみ。Sirvoy・Hostfully に /go/ なし。PR 表記あり。内部リンクなし。法律・税務の断定なし。為替換算なし
