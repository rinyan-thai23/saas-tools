---
title: ダイレクト予約の手数料と自社予約サイト：民泊ツール9製品の比較
slug: buy-direct-booking-fees
type: 買う直前
products: [guesty, hostaway, lodgify, ownerrez, hospitable, igms, uplisting, beds24, sirvoy]
description: 自社の予約サイトで受ける予約（ダイレクト予約）にかかる手数料、サイト機能、決済手段、日本語・円の扱いを、公式の記載で比較。申込前に確認する項目つき。
cards: [Guesty, Hostaway, Lodgify, OwnerRez, Hospitable, iGMS, Uplisting, Beds24, Sirvoy]
updated: 2026-11-05
pr: true
---

# ダイレクト予約の手数料・自社予約サイト機能の比較

この記事にはアフィリエイトリンク（PR）が含まれます。内容は公式ページ等の記載（取得日 2026-11-05）に基づき、リンクの有無では変えていません。Sirvoy には申込リンクを付けていません。PriceLabs と Hostfully Guidebooks は予約を扱わないため対象外です。

> **結論**
> - 「手数料0%」の意味は製品で違います。ツール側の予約手数料が0%でも、決済会社（Stripe 等）の手数料は別にかかります。
> - ツール側に率が書かれていたのは、Hospitable、Hostaway（上位サイトのみ）、Guesty Lite の従量プラン（1%）、Lodgify（決済ゲートウェイ経由の支払いに1%）、iGMS の無料プラン（4%）、Uplisting の従量プラン（3%／1.5%）です。
> - 日本での決済可否と、予約サイトの日本語・円表示は、ほとんどの製品で公式に確認できませんでした。日本語が公式に確認できたのは Sirvoy の予約エンジンと、Beds24 のゲスト言語（予約ページ・メールの言語コードに ja）です。

## 比較表：ツール側の手数料

率は公式の記載のとおりです。【確認済】は公式ページを開いて確認。決済会社の手数料は含みません。Lodgify は公式サイトの本体を開けず、公式の公開コピー（webflow-mkt.lodgify.com）で確認しています。本体サイトとの一致は照合していません。

| 製品 | ダイレクト予約にかかるツール側の費用 |
|---|---|
| Guesty | 公式：予約エンジンに "percentage-based fees" はなし。ただし Lite の Pay as you grow は予約ごとに1%【確認済】。第三者は Pro で2〜3.5%と報告（公式と食い違い、未検証） |
| Hostaway | Booking Website は契約に含む。上位の Booking Website Pro は月$49＋対象予約の0.5%。【確認済】。これとは別の記載として「ゲストに1.8%を上乗せ（米国のみ）」もあるが、どの商品にかかるかは公式の文面から不明 |
| Lodgify | 予約手数料0%。決済ゲートウェイ（Stripe・PayPal 等）経由の支払いに別途1%。手動入金（現金・銀行振込）は手数料なし【確認済】 |
| OwnerRez | "No commissions, no guest fees, or per-booking fees"【確認済】。サイトは別料金のプレミアム機能（下記） |
| Hospitable | Professional・Mogul のみ。Basic 1%、Premium 4%＋決済手数料3%（予約ごと）。Host・Essentials は不可【確認済】。アップセルは7〜10%、デポジットは2%の処理手数料 |
| iGMS | PRO・PRO+ の iGMS 側の手数料率は価格ページに明記なし【未確認】。FLEX は "0% booking fee"。無料プラン（pilot）は Stripe 経由の決済に4% |
| Uplisting | 定額プランのツール側手数料は記載なし【未確認】。従量プランは予約ごとに3%（1〜4物件）／1.5%（5〜10物件）。決済は Stripe |
| Beds24（海外公式の情報。日本の販売会社の案内は別記） | 予約手数料なし（"Beds24 never charges commissions on bookings"）【確認済】。日本の販売会社版の案内では「Stripe決済ごとに3.6%」（Stripe が利用者から徴収） |
| Sirvoy | 予約エンジンの手数料0%（全プラン）【確認済】 |

月100万円のダイレクト売上なら、率だけの計算で 0.5%＝5,000円、1%＝1万円、4%＝4万円です。決済会社の手数料は別です。

## 比較表：予約サイトの機能と決済

| 製品 | 予約サイト | 決済・通貨 |
|---|---|---|
| Guesty | 全プランに予約エンジン。30言語。日本語が含まれるかは公式で未確認（ヘルプ抜粋に日本語の記載、第三者のみ） | GuestyPay は米国・カナダ・EU/UK のみ。外部決済は Stripe（Lite）、Stripe・Merchant Warrior・Hyp（Pro）。日本での Stripe 利用は未確認 |
| Hostaway | Booking Website（テンプレート、コード不要）。言語は English・Spanish・French・Italian（記事により Portuguese）で日本語なし【言語は第三者のみ】 | Payment Processing。マーケットプレイスに Stripe、Braintree 等。日本での利用可否は未確認 |
| Lodgify | Starter 以上。ノーコード、ウィジェット、年払いは独自ドメイン無料。表示言語は「32」（日本語の有無は未確認） | Stripe・PayPal。Lodgify Payments は米国のみ。価格表示は EUR/USD/GBP、JPY は未確認 |
| OwnerRez | Hosted Sites（独自ドメイン可）と WordPress Plugin＋Integrated Sites はプレミアム（Hosted Sites は1物件目$15、2物件目$5、3〜9物件目各$3。5室で$29【計算値】）。予約ウィジェットは基本料金内 | Stripe、PayPal 等。1物件に設定できる通貨は1つで、決済事業者も同じ通貨が必要。Stripe の日本の対応は未確認 |
| Hospitable | Professional 以上で Direct Booking Website。チャージバック／損害補償付き | 手数料は上の表。ダイレクト予約の決済の日本対応は未確認 |
| iGMS | PRO 以上。Bookable Website、独自ドメイン、ブランド管理、複数物件検索 | Stripe。円の設定は第三者のみ・未確認 |
| Uplisting | Basic（全プラン）／Plus（月£30、Manager は込み）。多言語は料金表で "Coming soon"、ヘルプにはGoogle翻訳の記事があり不一致 | Stripe アカウントが必要。日本発行カード等の可否は未確認。JPY は未確認 |
| Beds24（海外公式） | 予約エンジン、ウィジェット、WordPress プラグインが月額に含まれる。独自サブドメインは月€19。「デザインが簡素」という声（第三者のみ）。ゲスト言語コードに ja あり | Stripe、PayPal 等。宿泊料の通貨に JPY が含まれる記載は公式Wiki（Airbnb 連携の通貨設定）の抜粋にあるが、日本の Stripe で円決済が使える旨の公式記載は見つかっていない |
| Sirvoy | 1ページの簡易ビルダー、WordPress プラグイン。予約エンジンは日本語を含む31言語。独自ドメインは Starter・Pro | Stripe、PayPal 等。日本での利用可否は未確認 |

## 条件別の選び方

- **ツール側の予約手数料を避けたい人**：Lodgify、OwnerRez、Beds24、Sirvoy は「0%」「手数料なし」と公式に書かれています（Lodgify は決済経由に1%が別）。
- **日本語の予約画面が要る人**：確認できたのは Sirvoy と Beds24 です（Sirvoy は部屋の説明文を言語ごとに自分で入力）。Hostaway は日本語なしとされています（第三者のみ）。Guesty は第三者の抜粋にあり、公式では未確認。
- **円で決済したい人**：日本のStripeでの円決済が使えると公式に確認できた製品はありません。Beds24 は宿泊料の通貨に JPY が含まれる記載が公式Wikiにありますが、日本の Stripe での円決済が使える旨の記載ではありません。申込前に確認が必要です。

[Guesty](/go/guesty/)（PR）／ [Hostaway](/go/hostaway/)（PR）／ [Lodgify](/go/lodgify/)（PR）／ [OwnerRez](/go/ownerrez/)（PR）／ [Hospitable](/go/hospitable/)（PR）／ [iGMS](/go/igms/)（PR）／ [Uplisting](/go/uplisting/)（PR）／ [Beds24（海外公式。PRリンク）](/go/beds24/)

Beds24 のリンクは海外公式（beds24.com）側の紹介リンクです。表にある「3.6%」などの日本の販売会社（WeIns / Co-Reception）の案内は日本の販売会社版の情報で、その申込は海外公式のリンクとは別です。

## 申し込む前に確認すること

- [ ] ツール側の手数料率（Hostaway の Pro、Hospitable のプラン、iGMS・Uplisting の定額プラン）を書面で確認した
- [ ] 決済会社（Stripe 等）の手数料を、自分の決済額で計算した
- [ ] その決済会社を日本の事業者として使えるか、円で受け取れるかを確認した
- [ ] 予約サイトに日本語の画面と円の価格表示があるか、実画面で確認した
- [ ] 届出番号などの表示欄を、自社の予約サイトに置けるかを確認した

## 未確認のこと

- 日本のStripeアカウントでの利用可否（Guesty、Hostaway、Lodgify、OwnerRez、Hospitable、iGMS、Uplisting、Beds24、Sirvoy）、円での価格設定
- Guesty・Lodgify・Uplisting の予約サイトの日本語の有無
- Beds24 の日本発行カードでの Stripe 利用可否

この記事は法的な助言ではありません。

## 出典

取得日はすべて 2026-11-05。表記は「製品名：URL」。

- Guesty：https://www.guesty.com/pricing/ ／ https://www.guesty.com/features/guesty-websites/ ／ https://www.guesty.com/features/guestypay/
- Hostaway：https://www.hostaway.com/features/direct-booking/ ／ https://www.hostaway.com/features/operations/
- Lodgify（公式の公開コピーを開いた。本体サイトとの一致は未照合）：https://webflow-mkt.lodgify.com/pricing ／ https://webflow-mkt.lodgify.com/lodgify-payments
- OwnerRez：https://www.ownerrez.com/pricing ／ https://www.ownerrez.com/support/articles/costs-and-fees ／ https://www.ownerrez.com/forums/general-help/booking-page-show-prices-in-other-currency
- Hospitable：https://help.hospitable.com/en/articles/4596748-how-does-our-pricing-work ／ https://hospitable.com/pricing
- iGMS：https://www.igms.com/pricing/ ／ https://igms.com/go/free-plan/ ／ https://www.igms.com/direct-booking-payment-processing-for-hosts/
- Uplisting：https://www.uplisting.io/pricing ／ https://support.uplisting.io/en/article/accept-payments-via-stripe-6um8cf/ ／ https://support.uplisting.io/en/article/adding-and-managing-site-languages-deiamw/
- Beds24：https://beds24.com/en/pricing/pricing ／ https://co-reception.com/pricing/ ／ https://wiki.beds24.com/index.php/Setting/properties.airbnbxmlcurrency
- Sirvoy：https://sirvoy.com/pricing ／ https://help.sirvoy.com/en_US/adjusting-the-booking-engine/support-up-to-31-languages-in-booking-engine

<!-- 追加調査依頼: 日本の事業者・日本のStripeアカウントで、各製品のダイレクト予約の決済（円）が使えるか -->
<!-- 追加調査依頼: iGMS PRO・PRO+、Uplisting 定額プランでのダイレクト予約の手数料率（営業へ問い合わせ） -->
<!-- 追加調査依頼: Guesty・Lodgify の予約サイトの対応言語に日本語が含まれるか（公式ヘルプ） -->
<!-- 追加調査依頼: 各製品の予約サイトに、住宅宿泊事業法の届出番号などの法定表示欄を置けるか -->
<!-- 追加調査依頼: Hospitable ダイレクト予約の決済手数料の表記（Basic 1%／Premium 4%＋3%）の正確な意味 -->
