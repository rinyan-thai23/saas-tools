---
title: 管理ツールを乗り換えるときのダブルブッキング防止チェックリスト
slug: switch-checklist-double-booking
type: 乗り換え
products: [guesty, hostaway, lodgify, ownerrez, hospitable, igms, uplisting, beds24, sirvoy]
description: 民泊の管理ツールを乗り換える3〜15室の運営者向け。API と iCal の違い、各社の公式ヘルプにある切り替え時の注意を根拠に、二重予約を防ぐ確認項目を前・中・後に分けて整理。
cards: [Guesty, Hostaway, Lodgify, OwnerRez, Hospitable, iGMS, Uplisting, Beds24, Sirvoy, 日本のOTA連携-楽天トラベルじゃらん等]
updated: 2026-11-05
pr: true
---

この記事にはアフィリエイトリンク（PR）が含まれます。内容は公式ページ等の記載（取得日 2026-11-05）に基づき、リンクの有無では変えていません。

# 管理ツールを乗り換えるときのダブルブッキング防止チェックリスト

> **結論**
> - 各社のヘルプには、API と iCal の併用の禁止（OwnerRez・iGMS）、接続が切れている間の二重予約の可能性（Hospitable の Vrbo）、Airbnb のフルアクセスは1社のみ（Uplisting）といった注意があります。乗り換え中に二重予約が実際に起きる頻度を示すデータは、今回は見つけられませんでした。
> - 切り替えの手順はツールごとに違います。Hospitable の移行ガイドは、Airbnb は旧ツールを切ってから接続、Booking.com は一時停止を推奨、Vrbo は公式の引き継ぎです。Uplisting は、Airbnb を読み取り専用で先に接続し、最後に既存のソフトを切断します。必ず乗り換え先の公式手順に従ってください。
> - 国内の予約サイトは、手順を今回確認できたのは Beds24 の日本の販売会社だけです。ほかは、売り止めを含めて個別確認が必要です。

## 同期の方式で分かること

| 方式 | 公式ヘルプの記載 |
|---|---|
| API（双方向） | iGMS：Booking.com の予約が Airbnb・Vrbo の同じ日付をすぐにブロックする。Guesty：1件の予約が全チャネルの日付を同時にブロックする |
| iCal | Hospitable：一方向（取り込みのみ）で、20分ごとに確認する。iGMS：1時間ごとに更新、物件へのグルーピング不可。Sirvoy：一方向のものは予約が自動で入らない場合がある（間隔の記載は確認できず） |
| 併用 | OwnerRez：同じチャネルで API 連携と iCal を併用してはならない。iGMS：併用すると二重ブロックになるため、直接接続したら iCal を外す。Hospitable：Booking.com 接続時は iCal 取り込みを外す（検索要約、第三者のみ） |
| 接続が切れた場合 | Hospitable：Vrbo は、接続が切れた状態でゲストが予約すると予約をすぐ作れず、二重予約になりうる |
| 公式の主張 | Lodgify の「二重予約なし」は公式の主張で、実際の精度は未検証。利用者の声には、Vrbo・Booking.com の接続に日数がかかった、との投稿がある（第三者のみ） |

## 乗り換え前

- [ ] **未来の予約をすべて一覧にした。** 全チャネル・ダイレクト予約・手入力の予約を含める。
  - 根拠：Guesty は、将来の予約を含む既存データを事前に新PMSへ移す進め方を公式FAQで案内。Hospitable は、ダイレクト・手動予約は自動では移らない（少数なら手入力、大量なら CSV を Support が取り込む）。
- [ ] **手動で入れたブロック日を控えた。** 根拠：iGMS で、API 接続後に Airbnb の手動ブロック日が消えた、という口コミ（2026-07、真偽は未検証）。
- [ ] **接続の一覧を作った。** どのチャネルが API で、どれが iCal か（物件×チャネル）。
- [ ] **国内予約サイトの手順を確認した。** Beds24 の日本の販売会社は、他社サイトコントローラーと連動中の場合は事前に解除が必要で、解除後は OTA 側で売り止めする、と案内。新規のOTA連動は4営業日。楽天トラベルの手順では、既存予約は自動で取り込まれず手入力。
- [ ] **切り替えの日程を、更新日・締切から逆算した。** 例：Lodgify の解約はアカウント画面から終了の1日前まで。Guesty は更新拒否が終了の30日前までの書面。
- [ ] **乗り換え先の公式の移行手順を読んだ。** Hospitable は移行ガイドで、Airbnb・Booking.com・Vrbo・Agoda ごとの接続手順を載せている。Uplisting は7ステップを公開。
- [ ] **試用で先に設定した。** Hospitable は14日間の試用中に設定を進められる。Uplisting は最初に Airbnb を読み取り専用で接続でき、既存のソフトとは干渉しない、と記載。

## 切り替え中

- [ ] **Airbnb のフルアクセスの接続は1社だけにした。** Uplisting の公式ページ：フルアクセスで接続できる Airbnb の公式ソフトは同時に1つ。
- [ ] **（Hospitable の移行ガイドの場合）Airbnb は旧ツールを切ってから新ツールをつないだ。** 根拠：Hospitable の移行ガイド。Uplisting の公式手順は順序が逆で、Airbnb を読み取り専用で先に接続し、最後に既存のソフトを切断してフルアクセスを付ける。Hostaway から Airbnb の切断解放に24〜48時間かかることがある、とも記載。この時間は他の組み合わせでも同じかは未確認。
- [ ] **Booking.com は接続変更中、掲載を一時停止した。** Hospitable は最大10分程度の停止を推奨。Guesty は、ほとんどのチャネルで約30分のダウンタイムがあると公式FAQに記載。
- [ ] **Vrbo は公式の引き継ぎ手順を使った。** Hospitable：公式の Software Switch で直接引き継ぐ。
- [ ] **新旧の併用は、主接続を決めた。** Hospitable：Airbnb・Vrbo は制限付き接続で旧PMSと併用できるが、価格・空室の管理は Hospitable を主接続にする必要がある。
- [ ] **各チャネルの掲載を物件に結合した。** Hospitable のヘルプ：これは同期と二重予約防止に欠かせない手順。
- [ ] **iCal を外した。** API でつないだチャネルは、iCal 取り込みを外す（iGMS・OwnerRez）。
- [ ] **Sirvoy など取り込み予約を使う場合は、取り込んだ予約がどのチャネルとも紐づかないことを理解し、変更・キャンセルの扱いを各チャネルで確認した。** （Sirvoy 公式ヘルプ：取り込んだ予約はどのチャネルとも紐づかない）

## 切り替え後

- [ ] 全チャネルで、控えた未来の予約とブロック日が一致するか確認した。
- [ ] 各チャネルのカレンダーに、同じ日の予約が重ならないか確認した。
- [ ] 価格の同期を確認した。Hostaway では、価格の同期漏れで設定より約$400安く予約が入った、との利用者の報告がある（第三者のみ、検索抜粋）。
- [ ] 接続が切れていないか確認した。Hospitable のヘルプでは、Vrbo は切断中に予約を作れない場合がある。
- [ ] 旧ツールを解約する前に、旧ツールの請求・停止手順を確認した。Guesty は、全リスティングの停止手順が終わるまで契約が続く、と規約にある。
- [ ] 旧ツールのデータ（テンプレート・メモ）を消す前に控えた。iGMS はアカウント削除で消える。

## 日本の予約サイトと、届出番号の注意

- 楽天トラベルとじゃらんnet は、公式の参画案内で住宅宿泊事業法（民泊新法）の施設を対象外としています。民泊新法の物件の楽天トラベルへの経路は Rakuten Oyado で、ツールで管理する場合も先に Rakuten Oyado への施設登録が必要です。
- Airbnb のヘルプでは、届出番号はツールを使っていても自分でログインして追加する必要があります。ツールを切り替えたときにこの登録が残るかは、今回は確認できていません。切り替え後に Airbnb の画面で届出番号の表示を確認してください。
- Airbnb のヘルプには、日本の民泊新法の施設について「ソフト連携で作成されたリスティング」を受け付けない、例外はライセンス契約を結んだ日本のAPIパートナー、とあります。例外の会社名は確認できていません。既存のリスティングをつなぎ直す場合の扱いは未確認です。
- 楽天トラベル・じゃらんは、民泊新法・特区民泊を対象外と明記しています。旅館業法の許可施設について海外ツールから接続できるかは、ツールごとに未確認です（手順を確認できたのは Beds24 の日本の販売会社のみ）。

## 公式の移行手順と、申し込みページ（PR）

公式の移行手順（広告ではないリンク）：[Hospitable の移行ガイド](https://help.hospitable.com/en/articles/16309227-switching-to-hospitable-from-another-pms)／[Uplisting の7ステップ](https://www.uplisting.io/switch-to-uplisting)／[Guesty の移行FAQ](https://www.guesty.com/switch-to-pms/)。Sirvoy は公式ヘルプ（[既存予約の取り込み](https://help.sirvoy.com/en_US/import-bookings/import-your-existing-bookings)）を参照してください。

申し込みページ（いずれも広告リンク）：[Hospitable（PR）](/go/hospitable/)／[Uplisting（PR）](/go/uplisting/)／[Guesty（PR）](/go/guesty/)／[OwnerRez（PR）](/go/ownerrez/)／[iGMS（PR）](/go/igms/)／[Hostaway（PR）](/go/hostaway/)／[Lodgify（PR）](/go/lodgify/)／[Beds24（海外公式。PRリンク）](/go/beds24/)。Beds24 の日本の販売会社（WeIns／Co-Reception）は別窓口で、リンクは付けていません。表計算管理からの移行は [別の記事](/articles/switch-spreadsheet-to-pms/) にまとめています。

## 未確認のこと

- 乗り換え中の二重予約の実際の頻度、チャネルごとの切り替え所要時間（Hostaway・Lodgify・OwnerRez・Beds24・Sirvoy の切り替え手順）
- 楽天トラベル・じゃらんの在庫を、海外ツールに切り替えるときの手順
- iCal の更新間隔（Guesty・Hostaway・Lodgify・Uplisting・Sirvoy）

この記事は法的な助言ではありません。手順は、各社の公式ヘルプを優先してください。

## 出典

取得日はすべて 2026-11-05。

- **Hospitable**：§3 チャネル、§7 乗り換え https://help.hospitable.com/en/articles/16309227-switching-to-hospitable-from-another-pms ／ https://help.hospitable.com/en/articles/14189123-understanding-how-reservations-sync-across-channels ／ https://hospitable.com/switch-to-hospitable
- **iGMS**：§3 チャネル、§8 注意 https://www.igms.com/features/channel-manager/ ／ https://help.igms.com/en/articles/9927919-how-does-the-channel-manager-work ／ https://www.capterra.com/p/157033/iGMS/reviews/
- **Guesty**：§4、§7 https://www.guesty.com/pricing/ ／ https://www.guesty.com/switch-to-pms/ ／ https://www.guesty.com/terms-of-service/
- **OwnerRez**：§3 https://www.ownerrez.com/support/articles/channel-management-calendar-import-export ／ **Uplisting**：§7 https://www.uplisting.io/switch-to-uplisting
- **Lodgify**：§2、§4、§8 https://webflow-mkt.lodgify.com/vacation-rental-channel-manager ／ https://webflow-mkt.lodgify.com/terms ／ **Hostaway**：§8 https://www.capterra.com/p/152433/Hostaway/reviews/?page=8
- **Sirvoy**：§3、§7 https://sirvoy.com/channel-manager ／ https://help.sirvoy.com/en_US/import-bookings/import-your-existing-bookings
- **Beds24**：§7 https://co-reception.com/jalan-rakuten-ikyu/ ／ https://co-reception.com/support-ticket/ ／ https://co-reception.com/beds24-application-form/
- **日本のOTA連携**：1-1-01、1-1-10 https://travel.rakuten.co.jp/info/hotel_msg.html ／ https://vacation-stay.com/host.html ／ 1-2-01 https://www.jalan.net/jalan/doc/howto/10sankaku.html ／ 1-5-02 https://www.airbnb.com/help/article/2351 ／ 1-5-04 https://www.airbnb.com/help/article/2177

<!-- 追加調査依頼: Hostaway・Lodgify・OwnerRez・Beds24（海外公式）・Sirvoy の「他ツールからの切り替え」時の Airbnb／Booking.com／Vrbo の接続手順と、売り止めの要否 -->
<!-- 追加調査依頼: Guesty・Hostaway・Lodgify・Uplisting・Sirvoy の iCal の更新間隔 -->
<!-- 追加調査依頼: Hostaway から Airbnb の接続を切ったあとの解放に24〜48時間かかる、という記載が他の組み合わせにも当たるか -->
<!-- 追加調査依頼: 楽天トラベル・じゃらんの在庫を国内ツールから海外ツールに切り替える際の売り止め・解除の手順（各社の公式手順） -->
