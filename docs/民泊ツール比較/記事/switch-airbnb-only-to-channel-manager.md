---
title: Airbnb だけの運用からチャネルマネージャーへ｜先に確認する日本の条件と切り替えの流れ
slug: switch-airbnb-only-to-channel-manager
type: 乗り換え
products: [hospitable, igms, uplisting, ownerrez, guesty, hostaway, lodgify, beds24]
description: Airbnb のみで運用している3〜15室の民泊が、チャネルマネージャーを入れる前に確認すること。日本の民泊新法のリスティングの扱い、3室の月額の目安、切り替えの流れを公式情報で整理。
cards: [Guesty, Hostaway, Lodgify, OwnerRez, Hospitable, iGMS, Uplisting, Beds24, 日本のOTA連携-楽天トラベルじゃらん等, 日本の制度-住宅宿泊事業法ほか]
updated: 2026-11-05
pr: true
---

この記事にはアフィリエイトリンク（PR）が含まれます。内容は公式ページ等の記載（取得日 2026-11-05）に基づき、リンクの有無では変えていません。

# Airbnb だけの運用からチャネルマネージャーへ

> **結論**
> - 住宅宿泊事業法（民泊新法）の物件は、先に Airbnb への確認が要ります。Airbnb のヘルプには、日本の民泊新法の宿泊施設は「ソフト連携で作成されたリスティング」を受け付けない、例外はライセンス契約を結んだ日本のAPIパートナー、とあります。既存のリスティングをツールにつなげる場合の扱いは、確認できていません（未確認）。
> - 届出番号は、ツールを使っていても自分で Airbnb にログインして登録する、と Airbnb のヘルプにあります。ツールを入れても、この作業は無くなりません。
> - 3室の月額は、公式の表で比べられるものだけ下の表に並べました。Hostaway と Guesty Pro は見積り制、Lodgify の3室は未確認です。

## 先に知っておくこと

- Airbnb の公式パートナー一覧（Preferred Partners）には、Guesty、Hospitable、Hostaway、Lodgify、OwnerRez、Uplisting、Beds24 が「Preferred+」として載っています。iGMS も同じページに載っていますが、取得したテキストでは等級が見えませんでした。
- 営業形態が旅館業法の許可や特区民泊の認定の場合は、届出番号の代わりにその情報を Airbnb に入力できる、とヘルプにあります。上の「ソフト連携」の記載が、この営業形態に同じように当たるかは確認できていません（未確認）。
- 楽天トラベル・じゃらんnet の公式の参画案内は、どちらも民泊新法の施設を対象外としています。民泊新法・特区民泊の案内先は、楽天グループの Rakuten Oyado です。両社とも民泊新法・特区民泊は対象外と明記していますが、旅館業法の許可施設に各ツールが接続できるかは未確認です。Airbnb 以外にも出す場合は、この点が先に来ます。

## 3室の月額の目安

金額は各社の表示通貨のままです。「計算値」は公式の単価からの掛け算・足し算で、公式がその合計を載せているわけではありません。税・追加機能・決済手数料は含みません。

| 製品 | 3室の月額 | 備考 |
|---|---|---|
| Guesty Lite | $27＋予約の1%（Pay as you grow、計算値） | 1〜3室向け。接続先は Airbnb・Booking.com・Vrbo。14日無料、カード不要。料金ページに期間限定の表示あり |
| Hospitable | Essentials $0／Professional $74（計算値） | Essentials は機能制限があり、サポートは AI とコミュニティのみ。14日無料、カード不要 |
| iGMS | Free は $0／PRO 月払い 約$70（計算値） | Free は試験提供（変更の可能性あり）で、予約5件・メッセージ10件まで。FLEX は1泊 $1（1物件あたり最低 $20） |
| Uplisting | Independent Host £72／従量は £0＋予約の3% | 従量は10物件まで。14日無料、カード不要 |
| OwnerRez | $70（計算値） | 最低月$40、契約縛りなし、返金なし |
| Beds24 | 公式 €24.00（3部屋タイプ・2チャネル、計算値） | 日本の販売会社は円建て（1室の例で ¥4,580〜。3室の例は載っていない） |

## 切り替えの流れ（公式資料にある範囲）

1. **まず無料の試用で試す。** 上の製品の多くは14日間の試用があります。Uplisting の公式手順は、最初に Airbnb を読み取り専用で接続し、リスティング・料金・予約を取り込む形です（既存のソフトとは干渉しない、と記載）。
2. **取り込める範囲を見る。** Hospitable は、リスティングを作り直さず既存のものに接続し、Airbnb の過去予約を最大5,000件取り込みます。OwnerRez は Airbnb の掲載情報（写真・説明・設備）を1回限りで取り込めます。
3. **フルアクセスで接続できるツールは1つ。** Uplisting の公式ページに「フルアクセスで接続できる Airbnb の公式ソフトは同時に1つ」とあります。一方、Hospitable は試用中、Airbnb・Vrbo を制限付きの接続にして旧ツールと併用できると案内しています（価格・空室管理は Hospitable を主接続にする必要があります）。
4. **手動で入れていたブロック日を控えておく。** iGMS では、API 接続後に Airbnb の手動ブロック日が消えたという Capterra の口コミ（2026-07）があります（口コミの記載で、真偽は未検証）。
5. **Airbnb 以外をつなぐ。** Hospitable は各チャネルの掲載を物件に「結合」して同期します。iGMS と OwnerRez は、API で直接つないだチャネルの iCal を外すよう案内しています。詳しくは [ダブルブッキング防止チェックリスト](/articles/switch-checklist-double-booking/) を参照してください。

## 条件別の選び方

| 条件 | 公式情報から言えること |
|---|---|
| まず費用を抑えて試したい | [Hospitable](/go/hospitable/) の Essentials（$0）、[iGMS](/go/igms/) の Free は、どちらも制限つき。上限を超える運用になるかを先に見る |
| 1〜3室で Airbnb・Booking.com・Vrbo だけ | [Guesty](/go/guesty/) Lite は料金が公開。4室以上は Pro（見積り）に移る |
| 契約縛りなしで月額を読みたい | [OwnerRez](/go/ownerrez/)（月$40〜、返金なし）。Uplisting は料金ページと規約の記載が食い違う（下記） |
| 日本語の画面・円建て請求が必要 | 公式で確認できたのは、Beds24 の日本の販売会社版（株式会社WeIns / Co-Reception。リンクなし）のみ。その申込は [Beds24（海外公式。PRリンク）](/go/beds24/)とは別 |
| 見積りで相談したい | [Hostaway](/go/hostaway/)（料金ページは入力フォームのみ）、Guesty Pro |

Uplisting は、料金ページに「No contract」、利用規約（最終編集 2024-02-27）に「最低12か月・自動更新」とあり、どちらが現行かは未確認です。[Uplisting を見る（PR）](/go/uplisting/)

## 申し込む前に確認すること

- [ ] 自分の営業形態（届出／許可／特区民泊）で、既存の Airbnb リスティングをツールにつなげてよいかを、Airbnb とツール会社に書面で確認した
- [ ] 届出番号を自分で Airbnb に登録済みで、ツール側で上書きされないか確認した
- [ ] 日本語の管理画面は確認できていない前提（Beds24 の日本の販売会社版を除く。Guesty は公式のサポート言語一覧に日本語なし）で、試用中に英語の画面で運用できるか試した
- [ ] 請求通貨が円か、為替手数料がかかるかを確認した（円の請求を確認できたのは Beds24 の日本の販売会社版のみ）
- [ ] 試用の前に、手動ブロック日と未来の予約の一覧を控えた

## 未確認のこと

- 民泊新法の既存リスティングをツールに接続できるか、例外となる日本のAPIパートナーの名前
- Hostaway・Guesty Pro の公式の料金、Lodgify の3室の料金
- 円（JPY）での請求の可否（Beds24 の日本の販売会社以外）
- Airbnb で設定済みの自動メッセージが、各ツールに引き継げるか

この記事は法的な助言ではありません。制度の判断は観光庁・自治体などの一次資料で確認してください。

## 出典

取得日はすべて 2026-11-05。

- **日本のOTA連携**：1-1-01・1-1-02 https://travel.rakuten.co.jp/info/hotel_msg.html ／ 1-2-01 https://www.jalan.net/jalan/doc/howto/10sankaku.html ／ 1-5-01 https://www.airbnb.com/software-partners/preferred-partners ／ 1-5-02 https://www.airbnb.com/help/article/2351 ／ 1-5-04 https://www.airbnb.com/help/article/2177
- **Guesty**：§2 料金 https://www.guesty.com/packages/guesty-lite/ ／ **Hospitable**：§2・§7 https://help.hospitable.com/en/articles/4596748-how-does-our-pricing-work ／ https://hospitable.com/switch-to-hospitable
- **iGMS**：§2・§3・§8 https://www.igms.com/pricing/ ／ https://www.capterra.com/p/157033/iGMS/reviews/ ／ **Uplisting**：§2・§7 https://www.uplisting.io/pricing ／ https://www.uplisting.io/switch-to-uplisting ／ https://www.uplisting.io/legal/terms-and-conditions
- **OwnerRez**：§2・§7 https://www.ownerrez.com/support/articles/costs-and-fees ／ https://www.ownerrez.com/support/articles/listing-content-importing-from-airbnb ／ **Beds24**：§2 https://beds24.com/en/pricing/pricing ／ https://co-reception.com/
- **Hostaway**：§2 https://www.hostaway.com/pricing/ ／ **Lodgify**：§2 https://webflow-mkt.lodgify.com/pricing

<!-- 追加調査依頼: Airbnb の日本の民泊新法の既存リスティングをツールにつなげられるか（Airbnb のヘルプ 2351 の適用範囲）と、例外となる日本のAPIパートナー名 -->
<!-- 追加調査依頼: 旅館業法の許可・特区民泊の施設に、Airbnb の「ソフト連携で作成されたリスティング」の制限が当たるか -->
<!-- 追加調査依頼: Hostaway・Guesty Pro の公式の料金（3室・5室・10室）、Lodgify の3室の料金 -->
<!-- 追加調査依頼: Airbnb 上で設定済みの自動メッセージ・予約ルールが各ツールに引き継げるか（各社のヘルプ） -->
<!-- 追加調査依頼: Uplisting の「No contract」と規約「最低12か月」のどちらが現行か -->
<!-- 追加調査依頼: /go/beds24/ の遷移先が海外公式（beds24.com の紹介リンク）で確定か。日本の販売会社（WeIns）に紹介制度があるか -->
