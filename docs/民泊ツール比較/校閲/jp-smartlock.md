# 校閲：jp-smartlock

校閲日 2026-11-07 ／ 照合カード：Guesty, Hostaway, Lodgify, OwnerRez, Hospitable, iGMS, Uplisting, Beds24, Sirvoy, Hostfully-Guidebooks（PriceLabs は「該当なし」の記載を確認）
件数：要修正 0 ／ 注意 4 ／ 軽微 3

## 要修正

なし。

## 注意

### 1. 「どの公式一覧にも記載が見つからなかった」の範囲が、本文の確度より強い
- 記事：結論2つ目「Akerun・SESAME は、確認した10製品のどの公式一覧にも記載が見つからなかった」／description「Akerun・SESAME は確認できず」
- カード：Guesty「4. 機能」スマートロック連携＝「ブランド一覧の全文はヘルプセンター…で、今回は開けず。Akerun・SESAME が含まれるかは未確認」。Hostaway＝「サイトマップが全件かは未確認」。Guesty「調べられなかったこと」に「Locks Manager の対応ブランド全文」
- 修正案：結論でも「Guesty は全文を開けず、Hostaway はサイトマップ範囲のみ。開けた範囲では記載なし」と一言添える（本文の補足・未確認欄には既に書かれている）。

### 2. 「日本のロックを名前で挙げていたのは Beds24 の日本の販売会社だけ」
- 記事：結論1つ目
- カード：どのカードも「日本のロック」を網羅的に調べたのではなく、Akerun・SESAME の有無だけを調べている（例：Sirvoy の Telkey／WeAccess／Locky、Hostaway の KeyCafe／Operto など、各ロックの国籍の記載はカードにない）。
- 修正案：「Akerun・SESAME のほか、キーポ・KEYVOX・RemoteLOCK を挙げていたのは Beds24 の日本の販売会社だけ（ほかの製品の一覧に日本製が含まれるかは、ブランドごとの確認はしていない）」と範囲を限定する。

### 3. 条件別の選び方：Nuki／igloohome／Schlage／August を「Hostaway、Lodgify、OwnerRez、Hospitable、iGMS、Uplisting が一覧に挙げている」
- 記事：条件別の表3行目
- カード：OwnerRez「4. 機能」＝直接連携は Schlage、Igloohome、Hubitat、ほか PointCentral、Kaba、eRentalLock、RemoteLock、Brivo、Jervis、Lynx 等（Nuki・August の記載なし）。一方 Guesty は Nuki を、Beds24 海外公式は Nuki.io を挙げているが、この行には出てこない。
- 修正案：製品ごとに挙げているブランドを具体的に書く（例：OwnerRez は Schlage・igloohome）。Guesty・Beds24 海外公式も Nuki で挙がっているので入れるか、「製品ごとに違う」で済ませて製品名の列挙をやめる。

### 4. 条件別の選び方「Hospitable は一定台数まで込み」と、表の注記が食い違う
- 記事：条件別の表4行目「Hospitable は一定台数まで込み」／連携先一覧の表では「（ロックがこの数に入るかは未確認）」
- カード：Hospitable「2. 料金」追加手数料：スマートデバイス＝「Professional は1物件あたり2台、Mogul は4台まで込み。超過は1台 $5」（ロックが含まれるかの記載は拾っていない）。
- 修正案：条件別の行にも「Professional 以上。ロックが『スマートデバイス』の台数に入るかは未確認」と揃える。

## 軽微

- 記事：連携先の一覧「Beds24（日本の販売会社）」の注記「ロックによってはBeds24の月額が上がる」。カード「Beds24 4. 機能」は日本の販売会社・海外公式の連携先を1行にまとめ、この注記がどちら由来かを分けていない。記事側は「海外公式にも当たるかは未確認」と書いていて問題ないが、日本の販売会社の注記と断定している根拠はカード上は曖昧。修正案：「いずれかの一覧の注記（由来は未確認）」に弱める、またはリサーチ役に出典の切り分けを依頼。
- 記事：出典欄に Guesty ヘルプ URL（help.guesty.com … Which-brands-are-supported…）。カードでは403で開けず「第三者のみ」。修正案：出典欄に「（開けず。検索抜粋のみ）」と添える。
- 記事末尾の HTML コメント「追加調査依頼」6件が公開ファイルに残る。修正案：ビルド時に除去する、または公開前に削除。

## 指摘なし（照合して一致を確認した主張）：38件
- Beds24：キーポ（美和ロック提供）、KEYVOX、RemoteLOCK、チェックインタブレット名、海外公式の RemoteLock／Jervis／Nuki.io／Yacan／Chekin、WeIns の社名
- Guesty：LocksManager は有料アドオン・金額未確認、"40+ smart lock brands"、Nuki／RemoteLock／Tedee／Brivo、「物理キーパッド付きのみ」は第三者のみ（記事も明記）
- Hostaway："hundreds of supported devices"、ブランド列挙、サイトマップに Akerun・SESAME なし
- Lodgify：自社ロック月 $7／台、連携一覧のブランド
- OwnerRez：直接連携 Schlage／igloohome／Hubitat と月 $4／台
- Hospitable：ブランド8社、Professional 以上、2台／4台込み、超過 $5
- iGMS：ブランド、RemoteLock「Coming soon」
- Uplisting：ブランド列挙、料金ページ £10（Independent Host）とヘルプ £4/ロックの食い違い
- Sirvoy：Telkey／WeAccess／Locky／Invite（Invite は双方向でない）
- Hostfully Guidebooks：Hostfully Devices と連携、他社ロック未確認
- PriceLabs は「該当なし」
- 申込リンクは /go/ のみ。Sirvoy・Hostfully には /go/ なし。PR 表記あり。内部リンクなし（スラッグ確認対象なし）
- 法律・税務の断定なし
