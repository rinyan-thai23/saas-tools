---
title: 【民泊】スマートロック連携｜海外の管理ツールで、Akerun・SESAME など日本のロックはつながる？
slug: jp-smartlock
type: 日本対応
products: [guesty, hostaway, lodgify, hospitable, ownerrez, igms, uplisting, beds24, sirvoy, hostfully-guidebooks]
description: 民泊のスマートロックと管理ツールの連携を、10製品で比較。Nuki・igloohome・TTLock など海外製はつながるが、Akerun・SESAME など日本製は公式の一覧になし。日本の販売会社経由の Beds24 の例と、確認する質問を整理します。
cards: [Guesty, Hostaway, Lodgify, Hospitable, OwnerRez, iGMS, Uplisting, Beds24, Sirvoy, Hostfully-Guidebooks]
updated: 2026-11-07
pr: true
---

# 【民泊】スマートロック連携｜海外の管理ツールで、Akerun・SESAME など日本のロックはつながる？

この記事にはアフィリエイトリンク（PR）が含まれます。紹介報酬の有無で、内容や順番は変えていません。

## 先に結論：海外ツールの連携先に、Akerun・SESAME などの日本製は載っていない

> - **今回調べた海外ツールの公式の連携一覧に、Akerun・SESAME は、どれも載っていません。** 「つながらない」と確認したわけではなく、**記載が見つからなかった**ということです。
> - **連携が載っているのは、Nuki、igloohome、TTLock、August、Yale、Schlage など海外製**。ツールによって、対応するロックが違います。
> - **日本の販売会社経由の Beds24 は、キーポ（美和ロック）、KEYVOX、RemoteLOCK との連携を案内**しています。KEYVOX は SESAME 連携にも対応する、という解説記事もあります。
> - **管理ツールを入れても、どのロックとも自動でつながるわけではありません。** ツールとロックが API で直接つながるかを確認する必要があります（解説記事の指摘）。
> - **連携の目的は、予約の期間に合わせて暗証番号を発行し、終了後に失効させること。** ツール側の連携が無くても、ロック側のアプリで手動で発行する方法は残ります。

## スマートロック連携の比較（公式の記載）

| ツール | 連携するロック | 追加費用 | Akerun・SESAME |
|---|---|---|---|
| [Hostaway](/articles/hostaway/) | Nuki、igloohome、TTLock、Salto、August、Yale ほか多数 | 記載なし | 公式の一覧になし |
| [Hospitable](/articles/hospitable/) | August、igloohome、Jervis、Nuki、Schlage、SmartThings、TTLock、Yale（Professional 以上） | プランに含まれる | 公式の一覧になし |
| [Uplisting](/articles/uplisting/) | August、Yale、Schlage、Kwikset、SmartThings、TTLock、Nuki、igloohome、Salto。RemoteLock なども | Independent Host は月£10（Operator 以上は込み）。ヘルプでは「1台£4」の記載もあり、食い違い | 記載なし |
| [Lodgify](/articles/lodgify/) | 自社の Smart Locks のほか、igloohome、Nuki、Schlage、Tedee、August、Kwikset、Yale ほか | 自社の Smart Locks は月$7/台 | 一覧になし |
| [OwnerRez](/articles/ownerrez/) | 直接連携：Schlage、igloohome、Hubitat。ほか PointCentral、Kaba、RemoteLock、Brivo など | 直接連携は月$4/台 | 一覧になし |
| [iGMS](/articles/igms/) | August、Yale、Schlage、igloohome、Nuki、Google Nest、Keycafe、RemoteLock ほか | 記載なし | 記載なし |
| [Guesty](/articles/guesty/) | LocksManager（有料アドオン）。「40以上のブランド」と公式が主張 | 有料アドオン（金額は未確認） | 未確認 |
| [Beds24](/articles/beds24/) | 海外公式：RemoteLock、Jervis、Nuki、Yacan など。**日本の販売会社：キーポ（美和ロック）、KEYVOX、RemoteLOCK** | ロックによって月額が上がる | 海外公式・日本の販売会社とも一覧になし。KEYVOX 経由の可能性は、解説記事の記述 |
| [Sirvoy](/articles/sirvoy/) | Telkey、WeAccess、Locky、Invite（Invite は予約情報のエクスポート） | 記載なし | 記載なし |
| [Hostfully Guidebooks](/articles/hostfully-guidebooks/) | 同社のスマートロック等（Hostfully Devices）。予約ごとの暗証番号をガイドブックに自動表示 | － | 記載なし |

## 日本で選ぶときの考え方

### 1. 日本製のロックを使う（Akerun、SESAME など）
- 海外ツールの公式の一覧には、載っていません。**直接つなぐのではなく、間に入るサービスを使う**方法があります。
- 解説記事によると、**KEYVOX は OTA・PMS 連携があり、SESAME 連携にも対応**します。SESAME は、既存のロックをつなぐと合鍵と履歴をクラウドで管理できる（SESAME Biz）、Akerun は法人・ホテル向けの管理型で、入退室ログや複数拠点の管理に対応する、とされています。
- ただし、**Akerun・SESAME が、民泊の管理ツールと API でつながるかは、公式の情報で確認できていません。**

### 2. 海外製のロックを使う（Nuki、igloohome、TTLock など）
- 海外ツールの連携は、こちらが中心です。igloohome や TTLock は、複数のツールが対応しています。
- **日本で購入・利用できるか、日本の住宅事情（ドアの形、電波の規制）に合うか**は、メーカーに確認してください（今回は調べていません）。

### 3. 日本の販売会社経由の Beds24
- キーポ、KEYVOX、RemoteLOCK との連携が、日本の販売会社の案内にあります。チェックイン用のタブレット（maneKEY、KEYVOX、民泊IN など）との連携も案内されています。
- 詳しくは [Beds24 の評判・口コミ](/articles/beds24/) へ。

## 暗証番号の運用のポイント

1. **予約の期間に合わせて**、暗証番号を発行し、チェックアウト後に失効させる。
2. 予約が**変更・キャンセル**されたとき、番号が更新されるか（同期の速さ）。
3. **停電・電池切れ・通信障害**のときの代替（物理キー、キーボックス）。
4. ゲストへの**案内**を、日本語（や、ゲストの言語）で送れるか。
5. **本人確認**との組み合わせ：無人のチェックインでも、宿泊の開始までに、宿泊者それぞれの本人確認が必要です（[宿泊者名簿・本人確認](/articles/jp-guest-register/)）。
6. **清掃スタッフ**用の番号を別に発行できるか。

## 日本で使うときの注意

- **民泊新法の人は先に確認**：Airbnb のヘルプには、日本の民泊新法の宿について「ソフト連携で作った掲載は受け付けない」とあります。例外は、Airbnb と契約した日本のAPIパートナーです。ロックの連携の前に、予約サイトの接続を確認してください。
- **日本語**：ツールの管理画面は、Beds24 の日本の販売会社以外は、日本語の記載がありません。
- 年180日の管理、届出番号などの機能は、各ツールの公式ページに記載が見つかりませんでした。

## 申し込む前に聞く質問

1. 使いたいロック（機種名）が、連携の一覧にあるか。なければ、API で個別に対応できるか。
2. 連携の**追加費用**（1台あたり、月額）。
3. 予約の変更・キャンセルで、暗証番号が自動で更新されるか。
4. 停電・通信障害のときの対応。
5. 日本語のゲストに、暗証番号の案内をどう送るか。

より細かい項目は [申込前チェックリスト](/articles/buy-checklist/) にあります。

[Beds24 海外公式を見る（PR）](/go/beds24/)

## よくある質問

### Akerun や SESAME は、海外の管理ツールとつながりますか？
今回調べたツールの公式の連携一覧には、載っていません。KEYVOX が SESAME 連携に対応する、という解説記事の記述がありますが、民泊の管理ツールと直接つながるかは、確認できていません。

### 日本で使えるスマートロックと連携できるのは？
Beds24 の日本の販売会社が、キーポ（美和ロック）、KEYVOX、RemoteLOCK との連携を案内しています。そのほかの海外ツールは、Nuki、igloohome、TTLock など海外製の連携が中心です。

### スマートロックの連携は、無料ですか？
ツールによります。Hospitable は Professional 以上のプランに含まれ、Uplisting は Operator 以上に込み、OwnerRez の直接連携は月$4/台、Lodgify の自社ロックは月$7/台です。

### ツールがロックに対応していなくても、運用できますか？
ロック側のアプリで、暗証番号を手動で発行する方法があります。ただし、予約のたびに手作業になります。

## 関連記事

- 日本対応：[宿泊者名簿・本人確認](/articles/jp-guest-register/)、[清掃管理](/articles/jp-cleaning/)、[日本語UI・日本語サポート](/articles/jp-japanese-ui-support/)
- 選び方：[申込前チェックリスト](/articles/buy-checklist/)

情報は、各ツールの公式サイトとヘルプ、日本の販売会社の案内、検索で見つかった解説記事を読んで日本語にまとめたものです。確認日 2026-11-07。対応するロックは変わるため、申込前に公式で再確認してください。
