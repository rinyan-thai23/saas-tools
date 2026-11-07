# 校閲：jp-cleaning

校閲日 2026-11-07 ／ 照合カード：Guesty, Hostaway, Lodgify, OwnerRez, Hospitable, iGMS, Uplisting, Beds24, Sirvoy（PriceLabs・Hostfully-Guidebooks は「該当なし」を確認）
件数：要修正 0 ／ 注意 2 ／ 軽微 3

## 要修正

なし。

## 注意

### 1. 「日本語の窓口で清掃管理の仕組みを案内していたのは、Beds24 の日本の販売会社だけ」
- 記事：結論3つ目／条件別の表4行目「Beds24 の日本の販売会社の解説とCRS案内が確認できたのみ。ほかは日本語の案内を確認できていない」
- カード：Beds24「4. 機能」清掃タスク＝日本の販売会社が解説記事と CRS を案内、は確認済み。しかし他製品のカードには、清掃に関する日本語の案内の有無を調べた記載がない（Guesty・iGMS・Sirvoy などは Capterra 上で日本語対応表示あり、とは README にあるのみ）。
- 修正案：「だけ」を「カードに記載があったのは Beds24 の日本の販売会社だけ（他社の日本語の清掃関連資料の有無は調べていない）」にする。

### 2. iGMS：「解約するとテンプレート・メモ・清掃指示が消える」
- 記事：補足の1つ目
- カード：iGMS「2. 料金」解約の方法・所要日数＝「アカウント削除でテンプレ・メモ・清掃指示も消える」（解約ヘルプ記事）。「解約」と「アカウント削除」は同じか、カードでは区別されていない。
- 修正案：「解約手続き（アカウント削除）で消える」とカードの語に合わせる。

## 軽微

- 記事：比較表 Hospitable 行「外部の清掃サービスとの連携」列に「清掃員への支払いは手数料あり（Essentials 2.5%…）」。カード（Hospitable 2. 料金・追加手数料）の事実は正しいが、外部サービス連携ではなく Hospitable 内の支払い機能の手数料。修正案：「使えるプラン」列か別の注記に移す。
- 記事：Beds24 行「サブアカウントは月額 ¥830」。カード（Beds24 2-2）は「すべて税込表記」。また料金ページでは「3名以上は作業用アカウント月額830円」と別の呼称もある。修正案：「¥830（税込表記）」と書く。
- 記事末尾の HTML コメント「追加調査依頼」5件が公開ファイルに残る。修正案：ビルド時に除去。

## 指摘なし（照合して一致を確認した主張）：34件
- Guesty：自動タスク作成、写真・メモ、権限を絞った表示
- Hostaway：予約に基づく自動タスク、予約変更でタスクも変わる
- Lodgify：Ultimate のみ、Turno 無料サブスク付属
- OwnerRez：清掃スタッフ用ポータルは基本料金内、Rezzy AI 月 $9 でタスク自動作成、連携先（Turno／Breezeway／Operto Teams／ResortCleaning／TIDY ほか12件ほど）、社内タスク詳細は未確認
- Hospitable：Tasks Manager／Tasks App／Cleaner Marketplace／清掃員支払い、全プラン、手数料 2.5%／1.5%・上限 US$5
- iGMS：タスク自動作成・割り当て・チェックリスト・SMS、iCal でも自動作成、無料プランに清掃員招待、Turno／Operto Teams／Cleanster
- Uplisting：Cleaning Scheduler、Turno／Lula.Cleaning／Cleanster
- Beds24：Housekeeping、CRS、サブアカウントで権限付き共有、¥830（販売会社のオプション一覧）
- Sirvoy：Cleaning & housekeeping scheduling、全プラン
- 結論：9製品すべてに記載あり、Lodgify は Ultimate のみ、Hospitable・Sirvoy は全プラン
- PriceLabs・Hostfully は対象外（カードの「該当なし」と一致）
- 申込リンクは /go/ のみ。Sirvoy に /go/ なし。PR 表記あり。内部リンクなし。法律・税務の断定なし
