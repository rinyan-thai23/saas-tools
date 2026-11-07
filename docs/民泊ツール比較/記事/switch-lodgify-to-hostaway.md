---
title: Lodgify から Hostaway へ乗り換える前に｜解約の締切と、ダイレクト予約サイトの扱い
slug: switch-lodgify-to-hostaway
type: 乗り換え
products: [lodgify, hostaway]
description: Lodgify を使っている3〜15室の民泊が Hostaway へ移るときの確認事項。Lodgify の自動更新と解約の締切、予約サイトと決済の差、Hostaway の移行支援の記載範囲を公式情報で整理。
cards: [Lodgify, Hostaway, 日本のOTA連携-楽天トラベルじゃらん等]
updated: 2026-11-05
pr: true
---

この記事にはアフィリエイトリンク（PR）が含まれます。内容は公式ページ等の記載（取得日 2026-11-05）に基づき、リンクの有無では変えていません。

# Lodgify から Hostaway へ乗り換える前に

> **結論**
> - Lodgify は自動更新で、更新前の通知は送られない、と規約にあります。アカウント画面からの解約は契約期間の終了の1日前まで、メール経由は5日前までです。規約上、期間の途中で解約しても返金はありません（消費者向けの14日間クーリングオフの扱いは本文参照）。乗り換えの日程は、この締切から逆算するのが安全です。
> - Lodgify で自社の予約サイトを作っている人は、Hostaway 側で予約サイト（Booking Website）を用意する必要があります。Lodgify のサイトから Hostaway への移行方法は、今回は調べていません（未調査）。
> - Hostaway の移行支援は、公式ブログに「24/7 のサポートとライブのオンボーディング」とあるだけで、手順・費用は未確認です。

## Lodgify を終わらせる条件

| 項目 | 公式の記載（Lodgify 料金ページ・規約） |
|---|---|
| 契約縛り | 料金ページ：長期契約はなく、いつでも解約できる。年払いは請求期間の終了まで使える |
| 更新 | 規約：1か月／12か月／24か月から選ぶ前払い。解約しない限り自動更新。更新前の通知は送られない |
| 解約の締切 | アカウント画面からは契約期間終了の1日前まで、メール（問い合わせフォーム）経由は5日前まで |
| 返金 | 契約期間の途中で解約しても返金なし。消費者には14日間のクーリングオフ（年払い・2年払いは更新時にも適用、月払いは初回のみ。事業者としての契約への当たり方は規約上の定義に依存し、未確認） |
| 料金改定 | 30日前の通知で変更可。旧プランの契約者は、現行の表示価格と違う場合がある |
| データの書き出し | 退会時に書き出せるかは確認できず |

注：Lodgify の本体サイトとヘルプセンターは、この調査では403で開けませんでした。規約と料金は、同内容の公開コピー（webflow-mkt.lodgify.com）で確認しており、本体側との一致は未照合です。

## Hostaway 側で確認できたこと

- **料金：** 公式は非公開（物件数を答えるフォーム→見積り）。導入費用は Hostaway の比較ページに "$500"（自社の主張）。
- **契約：** 規約は期間を「個別契約による」としています。値上げは14日前までに通知され、同意しない場合は発効の5日前までの通知で解約できます。
- **移行支援：** 手順・期間・費用の具体は、開いた公式ページに記載なし。移行ガイドの記事は、一般的な説明と自社の実績データが中心です。
- **取り込み方法：** CSV などの仕様は未確認です（ヘルプセンターは403）。

## 機能の差（公式の記載の範囲）

| 項目 | Lodgify | Hostaway |
|---|---|---|
| Airbnb・Booking.com・Vrbo | API連携（Basic から） | 対応 |
| Expedia | チャネルマネージャーのページにAPIとあるが、料金ページの機能表には記載なし（食い違い） | 対応 |
| その他の予約サイト | iCal連携（全プラン） | iCal連携の項目あり |
| ダイレクト予約サイト | Starter 以上。決済ゲートウェイ経由のオンライン決済に1%の手数料（予約手数料は0%） | Booking Website は契約に含む。上位の Pro は月$49＋対象予約の0.5% |
| 予約サイトの言語 | 「32」言語（内訳は未確認） | English、Spanish、French、Italian（第三者の抜粋。日本語なし） |
| 清掃タスク | Ultimate のみ | 予約に連動して自動作成 |
| オーナー向け | Ultimate のみ（精算・報告） | オーナーポータルあり |
| スマートロック | 自社 Smart Locks（月$7/台）と連携先 | Nuki、igloohome、TTLock など多数 |
| 請求通貨 | EUR・USD・GBP の表示。JPY は未確認 | 記載なし。JPY は未確認 |

- **楽天トラベル・じゃらん：** どちらも公式ページに記載が見つかりませんでした（「接続できない」と確認したわけではありません）。
- **Agoda：** Hostaway は公式のチャネル一覧になく、接続は断定できません（未確認）。Lodgify も連携一覧に掲載がなく、iCal 経由で使えるかは Lodgify に個別に確認が必要です。
- **日本語：** どちらも日本語の公式サイトはありません。Lodgify の管理画面の言語は未確認、Hostaway は日本語対応の記述が確認できていません。
- **ゲスト登録（宿泊者名簿）：** Lodgify の Guest Registration は対応地域の一覧がなく、日本が対象かは不明です。

## 利用者の声（第三者のみ）

Capterra（海外レビュー、2026-11-03時点）は Lodgify が 1,312件／4.5、Hostaway が 1,623件／4.8 です。Lodgify には、チャネル同期の遅延、サポート応答の遅れ、1年目以降の値上げの指摘があります（検索抜粋で、各ページは未開封）。Hostaway には、値上げが頻繁との投稿があります。英語圏の声で、日本の運営者の実感ではありません。

## 条件別の判断

| 条件 | 見るところ |
|---|---|
| Lodgify の更新日が近い | 解約の締切（アカウント画面なら終了の1日前）。更新後の解約は原則返金なし（規約。消費者向けクーリングオフの当たり方は未確認） |
| 自社の予約サイトを使っている | Hostaway 側の予約サイト（Booking Website）の用意、ドメイン、既存のダイレクト予約の扱いを見積り時に確認。[Hostaway の見積り（PR）](/go/hostaway/) |
| 清掃管理・オーナー精算を使っている | Lodgify では Ultimate が前提。Hostaway で同等の範囲か確認 |
| 今の運用を続けるか迷っている | [Lodgify の料金と試用（PR）](/go/lodgify/)（7日間無料、カード不要）で、プラン別の差を先に見る |

## 乗り換え前に確認すること

- [ ] Lodgify の契約期間・更新日・解約の締切を確認した
- [ ] Lodgify から、未来の予約・ゲスト情報・メッセージテンプレートを控えた
- [ ] Hostaway の見積りで、月額・初期費用・契約期間・解約金・値上げ条件を書面で受け取った
- [ ] 既存のダイレクト予約（デポジットを含む）を、新しい予約サイトにどう引き継ぐか確認した
- [ ] 独自ドメインと決済アカウント（Stripe など）の付け替えを確認した
- [ ] 切り替え中のダブルブッキング対策を決めた（[チェックリスト](/articles/switch-checklist-double-booking/)）
- [ ] 請求通貨が円か、為替手数料がかかるかを確認した

## 未確認のこと

- Hostaway の移行の手順・期間・費用、インポートの形式
- Lodgify のサイトから Hostaway への予約サイト・ドメインの移行方法（今回は調べていない）
- Lodgify の退会時のデータ書き出し、Lodgify の3・5・10・20室の公式料金（スライダー計算で取得できず）
- Hostaway の公式の料金、無料トライアル、標準の契約期間
- 両社の円（JPY）請求の可否、日本語サポートの可否

この記事は法的な助言ではありません。契約の判断は、契約書と各社への確認を優先してください。

## 出典

取得日はすべて 2026-11-05。

- **Lodgify**：§2 料金（契約縛り、契約期間・自動更新、解約手続き、返金）https://webflow-mkt.lodgify.com/pricing ／ https://webflow-mkt.lodgify.com/terms ／ §3 チャネル、§4 機能 https://webflow-mkt.lodgify.com/vacation-rental-channel-manager ／ https://webflow-mkt.lodgify.com/integrations ／ §5 日本対応 https://webflow-mkt.lodgify.com/guest-registration ／ §7 乗り換え https://webflow-mkt.lodgify.com/switching-software ／ §8 注意（第三者）https://www.capterra.com/p/131924/Lodgify/reviews/
- **Hostaway**：§2 料金 https://www.hostaway.com/terms/ ／ https://www.hostaway.com/features/direct-booking/ ／ §3・§4 https://www.hostaway.com/vacation-rental-channel-manager/ ／ https://www.hostaway.com/features/smart-locks/ ／ §7 乗り換え https://www.hostaway.com/blog/switching-pms-platforms/
- **日本のOTA連携**：3-02、3-03 https://www.hostaway.com/features/channel-manager/ ／ https://www.lodgify.com/channel-manager/
- **その他**：README（Capterra の評価・口コミ数、2026-11-03時点）

<!-- 追加調査依頼: Hostaway の他社PMSからの移行の手順・期間・費用、インポート形式（ヘルプセンターは403で未取得） -->
<!-- 追加調査依頼: Lodgify の退会時のデータ書き出し（予約・ゲスト・メッセージ）の可否と方法 -->
<!-- 追加調査依頼: Lodgify の3・5・10・20室の公式料金、予約サイトの32言語に日本語が含まれるか -->
<!-- 追加調査依頼: Hostaway の Booking Website への既存ダイレクト予約・独自ドメインの引き継ぎ方法 -->
<!-- 追加調査依頼: 両社の円（JPY）請求の可否と、日本語サポート・管理画面の日本語の現状 -->
