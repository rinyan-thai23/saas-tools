---
title: iGMS から Hospitable へ乗り換える前に｜自動移行がない部分と、解約で消えるもの
slug: switch-igms-to-hospitable
type: 乗り換え
products: [igms, hospitable]
description: iGMS を使っている3〜15室の民泊が Hospitable へ移るときの確認事項。iGMS の解約と消えるデータ、Hospitable の移行ガイドで自動移行されないもの、月額の目安を公式情報で整理。
cards: [iGMS, Hospitable, 日本のOTA連携-楽天トラベルじゃらん等]
updated: 2026-11-05
pr: true
---

この記事にはアフィリエイトリンク（PR）が含まれます。内容は公式ページ等の記載（取得日 2026-11-05）に基づき、リンクの有無では変えていません。

# iGMS から Hospitable へ乗り換える前に

> **結論**
> - Hospitable には、他のPMSからデータを自動で移す仕組みがありません（公式ヘルプ）。リスティングは作り直さず既存のものに接続でき、Airbnb は過去予約を最大5,000件取り込みますが、自動メッセージは作り直しで、ダイレクト予約・手動予約は自動では移りません。
> - iGMS はアカウントを削除すると、メッセージのテンプレート・メモ・清掃の指示も消えます。解約の前に控えるのが先です。
> - 日本語は、どちらも管理画面にありません（iGMS は英語・スペイン語、Hospitable は英語のみ）。楽天トラベル・じゃらんは、どちらも公式ページに記載が見つかりませんでした。

## iGMS の解約で確認すること

| プラン | 公式の記載（iGMS 規約・ヘルプ） |
|---|---|
| 月払い | 解約手数料なし。最終請求書が出る。部分月のクレジット・返金はなし |
| 年払い・10物件未満 | 一括前払い。全額が返金不可で、途中解約でも未使用分の返金なし |
| 年払い・10物件以上 | 月ごと請求＋署名する年間契約。期間前に解約すると月払い料金に切り替わり、差額（使用済み月分）を請求される |
| 解約の手続き | ヘルプのリンクから申請。営業日48時間以内に処理し、メールで連絡 |
| データ | アカウントを削除すると、テンプレート・メモ・清掃指示も消える。プロモコード・特別料金は新規アカウントに引き継がれない |
| 請求の考え方 | 毎月初に前月の active 物件（その月に予約があった物件）分を後払いで請求 |

Capterra には、2025-02に「何度試してもサイトで解約できなかった」との口コミがあります（口コミの記載で、真偽は未検証。公式ヘルプは営業日48時間以内の処理を案内）。

## Hospitable の移行ガイドで分かること

| 項目 | 公式の記載 |
|---|---|
| 自動移行 | なし。他のPMSとは連携しておらず、API でデータを移す方法はない |
| リスティング | 再作成不要。既存のものに接続する |
| 予約 | Airbnb は過去予約を最大5,000件取り込む。Booking.com は過去予約を API で送らない。Vrbo は切替後に移る（一部の過去の金額情報は別途取り込みが必要） |
| ダイレクト・手動予約 | 自動では移らない。少数なら手入力、大量なら CSV を Support が取り込む |
| 自動メッセージ | 自動では移らない。作り直しが必要 |
| 切替の手順 | Vrbo：公式の Software Switch で直接引き継ぎ。Airbnb：旧PMSを切断してから接続。Booking.com：接続変更中の掲載の一時停止を推奨（最大10分程度） |
| 併用 | Airbnb・Vrbo は制限付き接続で旧PMSと併用可。価格・空室の管理は Hospitable を主接続にする必要がある |
| 試用・支援 | 14日間の試用で設定を先に進められる。トライアル中に無料のオリエンテーション通話。有料の "Rapid Rollout"（1対1、通常3回・合計3〜5時間）は任意で、金額は未確認 |

二重予約の防止は、各チャネルの掲載を物件に「結合（Merge）」して同期します。公式ヘルプは「これは同期と二重予約防止に欠かせない手順」としています。Vrbo は、接続が切れた状態でゲストが予約すると、Hospitable がすぐに予約を作れず、二重予約になりうる、とも書かれています。

## 月額の目安（USD、月払い。iGMS は年払いも併記、計算値）

「計算値」は公式の単価からの掛け算・足し算です。全室が稼働している前提で、税・追加機能・決済手数料は含みません。

| 室数 | iGMS PRO（月払い／年払い） | Hospitable Professional | Hospitable Mogul |
|---|---|---|---|
| 3室 | 約$70／約$62 | $74 | $99 |
| 5室 | 約$99／約$87 | $104 | $159 |
| 10室 | 約$174／$150 | $179 | $309 |

- iGMS は、その月に予約があった物件のみ課金（1物件目は常に課金）。Hospitable は、基本料金は物件が停止中でも課金され、追加物件の料金は期間中にチェックインがあった物件（または Dynamic Pricing を有効にした物件）が対象です。
- iGMS には、1泊$1・最低$20／物件の FLEX と、月$0の Free（予約5件・メッセージ10件まで）があります。Hospitable には、月$0の Essentials（機能制限、サポートは AI とコミュニティのみ）があります。試用は、iGMS が14日間（カード不要）、Hospitable が14日間です。
- Hospitable は年払いで12%引き。ただし12か月の約束で、トライアル開始から30日を過ぎると返金なしです。月払いは契約なしで、当月末に終わります。
- iGMS の PRO+ と Hospitable Mogul の機能の範囲は同じではありません（比較は [iGMS と Hospitable の比較](/articles/vs-igms-hospitable/)）。

## チャネルの差

- **Airbnb・Vrbo・Booking.com：** どちらも API で接続します。
- **Agoda：** Hospitable は API で接続（全プラン共通）。iGMS は公式の対応チャネル一覧に Agoda の記載がありません。
- **Expedia：** どちらも iCal の扱いです（iGMS は1時間ごとに更新、物件へのグルーピング不可。Hospitable は20分ごとに確認、一方向）。
- **楽天トラベル・じゃらん：** どちらの公式ページにも記載が見つからず、iCal で取り込めるかも未確認です。

## 条件別の判断

| 条件 | 見るところ |
|---|---|
| Agoda も使っている | Hospitable は公式に接続あり。iGMS の一覧には記載なし。[Hospitable を見る（PR）](/go/hospitable/) |
| ダイレクト予約・自動メッセージを多く作り込んでいる | Hospitable は自動で移らないため、作り直す件数を数えてから決める |
| iGMS の年払い契約の途中 | 返金なし（10物件以上は月払い料金との差額請求）。更新日に合わせる。[iGMS を見る（PR）](/go/igms/) |
| 日本語のゲスト向けメッセージが必要 | Hospitable の定型メッセージは英・西・仏・独。日本語の追加要望は、2026-06の投稿が取得時点で「New」のまま。iGMS は「109言語」とあるが日本語が含まれるかは未確認 |

## 乗り換え前に確認すること

- [ ] iGMS のメッセージテンプレート・メモ・清掃の指示を、解約前に別の場所へ控えた
- [ ] iGMS の契約（月払い／年払い、10物件以上の年間契約か）と更新日を確認した
- [ ] Airbnb の手動ブロック日を控えた（iGMS では API 接続後に消えたという口コミがあります）
- [ ] ダイレクト予約・手動予約の一覧を作り、件数が多い場合は Hospitable の Support に CSV の取り込みを依頼する準備をした
- [ ] 各チャネルの掲載を Hospitable で「結合」した（[チェックリスト](/articles/switch-checklist-double-booking/)）
- [ ] 請求通貨（円の記載は公式で見つからなかった）と、英語の画面での運用を試用中に試した

## 未確認のこと

- 両社の円（JPY）請求の可否、日本語サポートの可否、Hospitable の人間サポートの対応時間
- iGMS からのデータの書き出し方法（今回は調べていない）
- Hospitable の Rapid Rollout の金額
- Hospitable の料金ページの現行表示（ヘルプ記事の金額で代替）

この記事は法的な助言ではありません。契約の判断は、規約と各社への確認を優先してください。

## 出典

取得日はすべて 2026-11-05。

- **iGMS**：§2 料金（契約縛り、解約の方法）https://igms.com/terms/ ／ https://help.igms.com/en/articles/9927743-how-do-i-cancel-my-igms-subscription ／ https://www.igms.com/pricing/ ／ §3 チャネル https://www.igms.com/features/channel-manager/ ／ §8 注意 https://www.capterra.com/p/157033/iGMS/reviews/
- **Hospitable**：§2 料金、§3 チャネル、§7 乗り換え https://help.hospitable.com/en/articles/4596748-how-does-our-pricing-work ／ https://hospitable.com/switch-to-hospitable ／ https://help.hospitable.com/en/articles/16309227-switching-to-hospitable-from-another-pms ／ https://help.hospitable.com/en/articles/14189123-understanding-how-reservations-sync-across-channels ／ §5 日本対応 https://feedback.hospitable.com/p/add-japanese-as-a-language-option-in-pre-defined-guest
- **日本のOTA連携**：3-05、3-06 https://hospitable.com/integrations ／ https://www.igms.com/channel-manager/

<!-- 追加調査依頼: iGMS から他ツールへ移るときのデータの書き出し（予約・ゲスト・テンプレート）の方法 -->
<!-- 追加調査依頼: Hospitable の Rapid Rollout の金額と、Support による CSV 取り込みの形式・費用 -->
<!-- 追加調査依頼: 両社の円（JPY）請求の可否、日本語サポートの可否、Hospitable の人間サポートの対応時間 -->
<!-- 追加調査依頼: iGMS の「109 languages」に日本語が含まれるか、Hospitable の定型メッセージの日本語対応の現状 -->
<!-- 追加調査依頼: 両社の楽天トラベル（Rakuten Oyado 経由を含む）・じゃらんへの iCal 接続の可否 -->
