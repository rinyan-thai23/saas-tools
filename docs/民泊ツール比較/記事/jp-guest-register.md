---
title: 宿泊者名簿・パスポート確認に使える民泊管理ツールは？海外ツールの記載を公式情報で確認
slug: jp-guest-register
type: 日本対応
products: [guesty, hostaway, lodgify, ownerrez, hospitable, igms, uplisting, beds24, sirvoy]
description: 日本の宿泊者名簿・外国人宿泊者の旅券確認について公的文書の記載を紹介し、海外の民泊管理ツールの本人確認・登録機能を確認できた範囲で整理。法的判断はしません。
cards: [日本の制度-住宅宿泊事業法ほか, Guesty, Hostaway, Lodgify, OwnerRez, Hospitable, iGMS, Uplisting, Beds24, Sirvoy, PriceLabs, Hostfully-Guidebooks]
updated: 2026-11-05
pr: true
---

この記事にはアフィリエイトリンク（PR）が含まれます。

# 宿泊者名簿・パスポート確認に使える民泊管理ツールは？海外ツールの記載を公式情報で確認

> **結論**
> - 本人確認・ID収集の機能を確認できたのは Hospitable・Uplisting・Lodgify（登録フォーム）・Beds24（ChargeAutomation 連携）など一部で、ほかは機能名のみ、または記載なし。日本の宿泊者名簿の要件に合う本体機能の記載は見つからなかった（「ない」と確認したのではなく、記載が見つからなかった）。
> - 日本向けの名簿機能を確認できたのは、Beds24 の日本の販売会社（株式会社WeIns）の有料オプション「Beds24宿泊者名簿」（月額1,650円／施設）だけ。
> - **名簿や本人確認が法令上どうあるべきかの判断は、行政書士・自治体・保健所などに確認してください。** この記事は公的文書の記載の紹介までです。

## 公的文書に書かれていること（引用のみ）

| 論点 | 記載 | 出典 |
|---|---|---|
| 名簿の備置・提出 | 法第8条第1項「宿泊者名簿を備え、これに宿泊者の氏名、住所、職業その他の…事項を記載し、都道府県知事の要求があったときは、これを提出しなければならない。」 | e-Gov |
| 記載事項 | 規則第7条第3項「宿泊者の氏名、住所、職業及び宿泊日のほか、宿泊者が日本国内に住所を有しない外国人であるときは、その国籍及び旅券番号」 | e-Gov |
| 保存 | 規則第7条第1項「作成の日から三年間保存する」。第4項：電磁的記録で、必要に応じ紙面に明確に表示できるときは、記載に代えることができる | e-Gov |
| 全員分 | ポータル「宿泊者全員を記載する必要があり、代表者のみの記載は認められません。」 | 民泊制度ポータル |
| 本人確認 | ポータル「宿泊行為の開始までに、宿泊者それぞれについて本人確認を行う必要があります。」対面でない場合は「宿泊者の顔及び旅券が画像により鮮明に確認できること」など2条件 | 民泊制度ポータル |
| 外国人の旅券 | 日本国内に住所を有しない外国人宿泊者について、ポータル「旅券の呈示を求めるとともに、旅券の写しを宿泊者名簿とともに保存すること。」 | 民泊制度ポータル |
| 7日以上の宿泊 | ポータル「特に宿泊契約が７日以上の場合には、定期的な面会等により上記の確認を行う必要があります。」 | 民泊制度ポータル |

簡易宿所・特区民泊の名簿はこの記事では扱いません。


## ツール側で確認したい点

1. 宿泊者全員分（代表者だけでなく）の氏名・住所・職業などを、予約に紐づけて集められるか
2. 外国人宿泊者の国籍・旅券番号の入力欄と、旅券の画像（写し）の収集・保存ができるか
3. 3年間、必要なときに紙面に表示・出力できる形で保存できるか（CSV出力など）
4. 対面でない本人確認で、顔と旅券の画像の取得ができるか

## 各ツールの記載（2026-11-05 時点）

| 製品 | 名簿・本人確認に関する公式の記載 | 日本の名簿要件との関係 |
|---|---|---|
| Guesty | GuestVerify（ゲスト審査）、AutoComply（アドオン）という機能名のみ。内容・対応国は不明 | 未確認 |
| Hostaway | 本体の記載なし。マーケットプレイスに Chekin、Autohost、Duveなど | 未確認 |
| Lodgify | （公式サイトの公開コピーで確認。www 側との一致は未照合）「Guest Registration」：予約確定時に登録フォームを自動送信しデータを保管。「Where supported, Lodgify submits guest reporting data to the relevant authorities」。日本が対象かは不明。パスポート画像の確認機能は記載なし | 日本の対応は未確認 |
| OwnerRez | 本体機能の記載なし。連携一覧に Chekin、Authenticate、Check-in Scan ほか | 未確認 |
| Hospitable | ゲストポータルで政府発行IDの撮影・自撮り・メール電話確認（2種類）。対応国・パスポートの扱いは記載なし | 日本の名簿要件に合わせた機能の記載なし |
| iGMS | 受信箱にゲストの審査状況を表示。ダイレクト予約に Check-in form。パスポート確認の記載は見つからず | 未確認 |
| Uplisting | ゲスト本人確認（Stripe Identity）：パスポート・運転免許証・国民ID等「over 4,000 document types from 100+ countries」。従量課金は1回 £1.25（月末請求）、アドオンは月 £15〜（Manager は込み） | 本人確認とID収集。名簿の様式に合うかは未確認 |
| Beds24（WeIns） | 有料オプション「Beds24宿泊者名簿」月額1,650円／施設（税込）。ゲストがスマホ・PCから入力、Beds24と連携、CSV出力、人数分の入力完了チェック。パスポート画像は ChargeAutomation 連携の Pre-Arrival tool で収集 | 日本の販売会社の機能として確認済。記載事項が規則と一致するかは未確認 |
| Sirvoy | 記載なし。ChargeAutomation 連携（ID収集）が連携ページにある | 未確認 |
| PriceLabs／Hostfully Guidebooks | 該当なし（価格ツール、ガイドブック） | － |

## 条件別の見方

| あなたの条件 | 調べた記載から言えること |
|---|---|
| 日本語で、名簿の入力・CSV出力まで使いたい | 確認できたのは Beds24（WeIns）の有料オプション。ほかは記載が見つからなかった |
| 旅券の画像を集めたい | Uplisting（Stripe Identity）、Hospitable（政府発行IDの撮影。パスポートの扱いは記載なし）、Beds24（Pre-Arrival tool）に収集機能の記載。名簿との関係は未確認 |

## 申込前にサポートへ送る英文の例

```
Hello, I run vacation rentals in Japan. Before subscribing, could you confirm in writing:
1) Can we collect name, address, occupation, nationality and passport number for every guest (not only the booker), and store passport photos per booking?
2) Can we export or print the records for 3 years? 3) Do you have any Japan-specific guest register, or a recommended partner for it?
```

## 申し込みページ（PR）

Guesty：[Guesty](/go/guesty/)／Hostaway：[Hostaway](/go/hostaway/)／Lodgify：[Lodgify](/go/lodgify/)／OwnerRez：[OwnerRez](/go/ownerrez/)／Hospitable：[Hospitable](/go/hospitable/)／iGMS：[iGMS](/go/igms/)／Uplisting：[Uplisting](/go/uplisting/)／Beds24（海外公式。PRリンク）：[Beds24](/go/beds24/)（日本語の名簿オプションは日本の販売会社（WeIns）版の情報で、その申込は上の海外公式のリンクとは別の窓口です。申し込み画面がどちらか確認してください）

## 未確認のこと

- 各ツールの本人確認機能が、日本の宿泊者名簿・旅券確認の求めを満たすか（公式に書いている製品は見つからなかった）
- Guesty の GuestVerify／AutoComply の内容と対応国、Hospitable の対応国
- Beds24 宿泊者名簿の記載項目が規則第7条の項目と一致するか
- 宿泊者データの保管場所と個人情報の扱い（今回は調べていない）

<!-- 追加調査依頼: Beds24 宿泊者名簿（co-reception.com/new-guestregistration-news/）の入力項目（氏名・住所・職業・国籍・旅券番号・全員分）が規則第7条第3項と一致するか、旅券画像の保存ができるか -->
<!-- 追加調査依頼: Guesty の GuestVerify／AutoComply、Hospitable のゲスト確認、Uplisting の Stripe Identity について、対応国に日本発行の旅券・日本国内の住所が含まれるか、収集項目に職業・住所欄があるか（各社ヘルプ） -->
<!-- 追加調査依頼: Chekin、Autohost、Check-in Scan 等の連携サービスが日本の宿泊者名簿（国籍・旅券番号・旅券の写し）に対応しているか（各サービスの公式ページ）。Hostaway・Lodgify・OwnerRez の連携ページの記載 -->
<!-- 追加調査依頼: 宿泊者の個人情報・旅券画像の保管場所（国・期間）と、各ツールの個人情報の取扱い（プライバシーポリシー）。個人情報保護法に関する公的資料は引用のみ -->

## 出典

取得日はすべて 2026-11-05。

| 項目 | 出典URL |
|---|---|
| 日本の制度・A-15〜A-24 | https://laws.e-gov.go.jp/law/429AC0000000065 ／ https://laws.e-gov.go.jp/law/429M60000900002 ／ https://www.mlit.go.jp/kankocho/minpaku/business/host/responsibility01.html |
| 各製品・5. 日本対応「宿泊者名簿・パスポート確認」 | Guesty：https://www.guesty.com/pricing/、Hostaway：https://www.hostaway.com/marketplace/chekin/、Lodgify：https://webflow-mkt.lodgify.com/guest-registration、OwnerRez：https://www.ownerrez.com/integrations、Hospitable：https://hospitable.com/features/guest-verification、iGMS：https://help.igms.com/en/articles/9927885-how-can-igms-help-me、Uplisting：https://support.uplisting.io/en/article/guest-identification-verification-11gqur/、Beds24：https://co-reception.com/new-guestregistration-news/ ／ https://wiki.beds24.com/index.php/Pre-Arrival_tool、Sirvoy：https://sirvoy.com/integrations |
