---
title: Lodgify の代替ツール｜自動更新・決済手数料・日本語情報なしから選ぶ5候補
slug: alt-lodgify
type: 代替
products: [lodgify, ownerrez, hospitable, igms, beds24, sirvoy]
description: Lodgifyの自動更新・決済手数料1%・日本語情報なしが合わない人へ。5候補を条件別に整理（2026-11-05時点の公式情報）
cards: [Lodgify, OwnerRez, Hospitable, iGMS, Beds24, Sirvoy, 日本のOTA連携-楽天トラベルじゃらん等, 日本の制度-住宅宿泊事業法ほか]
updated: 2026-11-05
pr: true
---

この記事にはアフィリエイトリンク（PR）が含まれます。

# Lodgify の代替ツール：契約・ダイレクト予約・日本対応で選ぶ5候補

> **結論**
> - Lodgify の合わない点が「更新前の通知がない自動更新」「サイト経由の決済に別途1%」なら、月払い・月単位で、予約手数料のない [OwnerRez](/go/ownerrez/)・[Beds24（海外公式。PRリンク）](/go/beds24/)・Sirvoy が比較の出発点（OwnerRez・Sirvoy は契約なし、Beds24 は月単位で解約通知あり）。
> - 予約サイトの日本語表示なら、予約エンジンが日本語を含む最大31言語に対応する Sirvoy（管理画面は日本語ではない）。
> - 管理画面の日本語・円請求・楽天／じゃらんを公式で確認できたのは Beds24 の日本の販売会社版（WeIns / Co-Reception）だけ。この版の申込は、上の海外公式のリンクとは別。Lodgify はこれらの記載が見つからなかった。

## 先に知っておくこと

- 楽天トラベルの新規参画ページ（公式）は民泊新法の施設は参画不可とし、同グループの「Rakuten Oyado」を案内。じゃらんnet の参画案内（公式）も民泊新法・特区民泊は不可。両社とも民泊新法・特区民泊は対象外と明記しているが、旅館業法の許可施設への接続可否は各ツールで未確認。制度の判断はこの記事ではしない。
- Airbnb の公式ヘルプは、日本の住宅宿泊事業ではソフト連携で作ったリスティングを受け付けないとし（例外の「日本のAPIパートナー」の名前は見つからなかった）、届出番号は Airbnb に直接ログインして入れる案内。既存の掲載を接続する場合の扱いは未確認。

## Lodgify が合わなくなりやすい点

Lodgify の本体サイトとヘルプは開けず、同内容とみられる公開コピー（webflow-mkt.lodgify.com）で確認した。本体（www）側との一致は未照合。

| 項目 | 内容 | 確度 |
|---|---|---|
| 自動更新 | 1・12・24か月から選び前払い。更新前の通知は送られない。解約はアカウント画面から期間終了の1日前、メールは5日前まで。期間途中の解約は返金なし（規約）。一方、料金ページには「no long-term contract, cancel any time」とあり、両方の記載がある | 確認済 |
| 決済手数料 | 予約手数料は0%だが、Stripe・PayPal 等の決済ゲートウェイ経由の支払いに別途1%（全プラン。ゲートウェイ側の手数料は別） | 確認済 |
| プランの壁 | Basic は1物件以下、Starter は2物件以下。3室以上は Professional 以上が前提と読める。清掃タスク・オーナー精算は Ultimate のみ、Google Vacation Rentals は Professional 以上 | 確認済 |
| 料金 | 1物件の表示価格は Basic $14／Starter $26／Professional $47／Ultimate $68（周期は年払いと推定）。3室以上はスライダー（JavaScript）で取得できなかった | 確認済（1物件）／未確認（3室以上） |
| 通貨・表記ゆれ | 料金の表示通貨は EUR・USD・GBP のみ（JPY は確認できず）。サポート時間と Expedia の接続は、公式内で記述が食い違う | 確認済 |
| 利用者の声 | 同期の遅れ、サポートの遅さ、1年目以降の値上げ、動作が重いとの個別の口コミ | 第三者のみ |
| 日本対応 | 公式サイトは7言語で日本語なし。管理画面の言語、予約サイト32言語の内訳、楽天／じゃらん、住宅宿泊事業法の機能は記載が見つからなかった | 確認済（サイト）／他は未確認 |

## 条件別の選び方

| あなたの不満・条件 | まず見る候補 | 理由 |
|---|---|---|
| ダイレクト予約の手数料を抑えたい | OwnerRez／Beds24／Sirvoy | OwnerRez は予約手数料なし、Beds24 も予約手数料なし、Sirvoy の予約エンジンは手数料0%（チャネル＝OTA側の手数料は別） |
| 自動更新が不安 | Hospitable・iGMS（月払い）／OwnerRez／Sirvoy／Beds24 | 月払いは契約なし。Sirvoy は書面の契約がなく、残高式で支払いを止めれば終了。Beds24 は月単位で、解約は通知が必要（海外公式は月末まで1か月前通知） |
| 予約サイトを日本語表示に | Sirvoy | 予約エンジンの画面が日本語を含む最大31言語に対応。ただし部屋の説明文は言語ごとに自分で入力 |
| 管理画面も日本語・円・国内サイト | Beds24 の日本の販売会社版（WeIns / Co-Reception。リンクなし） | 日本語UI・円建て。楽天・じゃらん等は有料の追加。この版の申込は海外公式のリンクとは別 |

## 候補の比較表

月額は月払いの目安。「計算値」は公式の単価表から当方で計算。通貨は各社の表示のまま。

| 項目 | OwnerRez | Hospitable | Beds24 | Sirvoy（Pro） | iGMS |
|---|---|---|---|---|---|
| 5室 | $88（公式表示） | Professional $104／Mogul $159（計算値） | €31.40（計算値*） | $73（公式表） | PRO 約$99（計算値） |
| 10室 | $127（計算値） | $179／$309（計算値） | €49.90（計算値*） | $98 | PRO 約$174（計算値） |
| ダイレクト予約サイト | Hosted Sites は別料金 | Professional 以上。手数料1%または4%＋3% | 月額に含む | 全プランで予約エンジン | PRO 以上 |
| 管理画面の日本語 | 一覧に日本語なし | なし | あり（日本の販売会社版） | なし（9言語） | なし（英・西） |
| 楽天／じゃらん | 記載が見つからなかった | 同左 | 日本の販売会社版が提供。楽天は公式Wikiでは Rakuten Oyado 経由、販売会社は別手順の記載で現行方式は未確認。じゃらんは販売会社が提供 | 記載なし | 記載が見つからなかった |
| 海外レビュー（Capterra、2026-11-03時点） | 271件／4.9 | 145件／4.7 | 117件／4.7 | 未取得 | 307件／4.6 |

\* 公式の計算式（基本€12.90＋1室€2.60＋部屋タイプ数×チャネル数×€0.55）。各室が別の部屋タイプで2チャネルの場合。請求との一致は未確認。Lodgify の海外レビューは 1,312件／4.5。Capterra は英語圏のレビューで、日本の運営者の実感ではない。

## 候補ごとの要点

- **OwnerRez**：1物件目 $40、5〜9物件目は各$8。契約なし・返金なし・カードのみ。Expedia は連携一覧に独立した記載が見つからなかった。公式サイト上のレビューに「Steep Learning Curve」の題がある。
- **Beds24**：海外公式（ユーロ建て、英独のみ、月末まで1か月前通知。PRリンクはこちら）と日本の販売会社版（円建て、日本語、最低1か月・解約は毎月20日までにメール、再登録5万円）で条件が別。日本語UI・円建て・名簿オプションは販売会社版の情報で、申込は海外公式のリンクとは別。Capterra に UI の分かりにくさの指摘。
- **Sirvoy**：チャネルマネージャーは Pro のみ。Airbnb・Booking.com・Expedia・Agoda は直接連携、Vrbo は iCal。請求通貨に JPY なし。サポートは24時間365日だが、日本語対応はヘルプ記事と公式FAQで記載が食い違う。オーナーポータルの記載は見つからなかった。
- **Hospitable**：月払いは契約なし。管理画面は英語のみ。
- **iGMS**：月払いは解約手数料なし、年払い（10物件未満）は返金不可。サポートは英語・スペイン語。

## 申し込む前に確認すること

- [ ] Lodgify の契約期間の終了日と、解約の受付期限（アカウント画面なら終了の1日前まで）。更新前の通知がないので、日付を自分で管理する
- [ ] 移行：Lodgify 側の退会時データ書き出しは公式で確認できていない。Hospitable は他PMSからの自動移行がなく、自動メッセージは作り直し
- [ ] JPY 払いと適格請求書：OwnerRez・Hospitable・iGMS・Sirvoy は記載が見つからなかった（[円請求・インボイスの整理](/articles/jp-yen-invoice/)）
- [ ] 宿泊者名簿は全員分、外国人は旅券番号と旅券の写しの保存（観光庁）。日本の名簿の記載事項に合う本体機能の記載は、Beds24 日本側の有料オプション以外は見つからなかった（ID・パスポート収集の機能は Beds24・Hospitable などにあり、Lodgify にも Guest Registration があるが、日本の名簿要件との適合や対象国は未確認）
- [ ] 無料トライアル中に実際の掲載を接続し、二重予約にならないかを確認する

## 未確認のこと

- Lodgify の管理画面の対応言語、3室以上の料金、JPY の価格設定・決済、Guest Registration の対象国。
- 楽天トラベル・じゃらんへの配信可否（記載が見つからなかっただけで、できないと確認したわけではない）、Akerun・SESAME との連携。価格は取得日時点。

## 出典

取得日 2026-11-05。

- Lodgify（公開コピー）：https://webflow-mkt.lodgify.com/pricing ／ https://webflow-mkt.lodgify.com/terms ／ https://webflow-mkt.lodgify.com/switching-software
- https://www.ownerrez.com/support/articles/costs-and-fees ／ https://help.hospitable.com/en/articles/4596748-how-does-our-pricing-work ／ https://www.igms.com/pricing/
- Beds24：https://beds24.com/en/pricing/pricing ／ https://co-reception.com/pricing/ ／ Sirvoy：https://sirvoy.com/pricing ／ https://help.sirvoy.com/en_US/adjusting-the-booking-engine/support-up-to-31-languages-in-booking-engine
- https://travel.rakuten.co.jp/info/hotel_msg.html ／ https://www.jalan.net/jalan/doc/howto/10sankaku.html ／ https://www.airbnb.com/help/article/2351 ／ https://www.mlit.go.jp/kankocho/minpaku/business/host/responsibility01.html

<!-- 追加調査依頼:
1. Lodgify 本体（www.lodgify.com）とヘルプセンターの料金・規約・連携ページが公開コピーと一致するか。3・5・10・20室の月額（スライダーの計算結果）。
2. Lodgify の管理画面（app.lodgify.com）の対応言語に日本語があるか。予約サイトの32言語に日本語が含まれるか。
3. Lodgify の JPY 価格設定・決済（Payyo 含む）、日本の Stripe・PayPal での利用可否、適格請求書の扱い。
4. Lodgify からのデータ書き出し、他ツールからのインポート方法と対応ツール、Guest Registration の対象国に日本が含まれるか。
5. OwnerRez・Hospitable・iGMS・Sirvoy が iCal・SiteMinder 経由等で楽天トラベル／じゃらんに配信できるかの公式な記載。
6. Sirvoy の日本語サポート（ヘルプ記事と公式FAQで食い違い）、自動メールの日本語テンプレートの有無、JPY での宿泊料設定。
7. /go/beds24/ の遷移先が海外公式（beds24.com の紹介リンク）で確定か。日本の販売会社（WeIns）に紹介制度があるか。
8. Beds24 の楽天トラベル接続の現行方式（公式Wiki=Rakuten Oyado 経由／販売会社=R-Connect 申請）。
-->
