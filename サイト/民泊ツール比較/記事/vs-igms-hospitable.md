---
title: iGMS と Hospitable を比較：料金・チャネル・日本での使い勝手
slug: vs-igms-hospitable
type: 比較
products: [igms, hospitable]
description: iGMS と Hospitable を物件数別の月額（計算値）、チャネル、日本語・円・国内予約サイトの対応で比較。未確認の点も分けて書く。
cards: [iGMS, Hospitable, 日本のOTA連携-楽天トラベルじゃらん等, 日本の制度-住宅宿泊事業法ほか]
updated: 2026-11-05
pr: true
---

**この記事にはアフィリエイトリンク（PR）が含まれます。** リンク経由で申し込むと、運営者に報酬が入ることがあります。

# iGMS と Hospitable を比較：3〜15室の民泊運営者が申込前に見ること

> **結論**
> Agoda をつなぎたい人は Hospitable（Agoda が公式表示にある）。1〜2 室を月払いで小さく始めたい人は、Hospitable（Essentials $0／Host $29）か iGMS の Free プラン（予約5件・メッセージ10件までの pilot）が選択肢で、1室の有料プランは iGMS PRO $48 が Hospitable Professional $59 より低い。3〜10 室で月払い、プランの機能が足りる人は iGMS PRO の合計（計算値）がやや低く、20 室では差が開く。
> どちらも管理画面は英語（iGMS は英語とスペイン語）。楽天トラベル・じゃらんは、民泊新法・特区民泊が各社の対象外と明記されており、旅館業法の許可施設への接続可否は両ツールとも未確認。円での請求、日本の宿泊者名簿に合う機能も、公式ページで確認できなかった。
> 申し込む前に、無料の枠か 14 日トライアルで「画面の英語」と「請求の通貨」を自分の目で確かめる。

読み方：印のない行は、公式ページ・公式ヘルプ・公式規約を開いて確認した内容です。「計算値」は公式の単価からこのサイトで計算した値、「第三者のみ」は公式を開けず第三者の情報だけの内容、「記載が見つからなかった」は「できない」という意味ではありません。金額は USD で、円には換算していません。データの取得日は 2026-11-05 です。

## 先に知っておくこと（日本で使うときの前提）

- **営業形態で、使える国内予約サイトが変わります。** 楽天トラベルの新規参画ページは、旅館業許可の施設を対象とし、民泊新法（住宅宿泊事業法）の施設は「ご参画いただけません」と書いています。民泊新法・特区民泊は楽天グループの別サイト「Rakuten Oyado」で登録する案内です。じゃらんnet も、旅館業法の許可施設が対象で、民泊新法・特区民泊は掲載できないと公式ページに書いています（ページの更新日は記載なし）。
- **Airbnb の公式ヘルプ**は、日本の民泊新法の物件について「ソフトウェア連携で作られたリスティングは受け付けない」（例外は、Airbnb とライセンス契約を結んだ日本の API パートナー）と書いています。届出番号は、管理ツールを使っていても Airbnb にログインして自分で入力する、とも書かれています。この記述と、各ツールへの「既存リスティングの接続」を組み合わせた運用が通るかどうかは、公式ページで確認できず**未確認**です。
- **楽天トラベル・じゃらんの「公式の認定ベンダー一覧」は見つかりませんでした。** iGMS も Hospitable も、自社の公式一覧に楽天トラベル・じゃらんの記載が見つかりませんでした。また、Rakuten Oyado の公式ページが「そのまま使える」と挙げる既存ツールは、ねっぱん、AirHost、Beds24、suitebook で、iGMS と Hospitable は載っていません。ただし「載っていない」ことは「つながらない」ことの確認ではありません。
- **法令の引用（判断はしません）。** 住宅宿泊事業法は、住宅宿泊事業の定義として、省令で算定した宿泊日数が一年間で「百八十日を超えないもの」としています。宿泊者名簿の記載事項は施行規則で「氏名、住所、職業及び宿泊日」に加え、日本国内に住所がない外国人は「国籍及び旅券番号」とされています。定期報告は「二月、四月、六月、八月、十月及び十二月」の15日までです。これらをツールで扱えるかは、下の表のとおり、どちらも公式に確認できていません。
- **Capterra の言語欄では、日本語対応ありとされるのは Guesty・iGMS・Sirvoy・Hostfully のみ**（README の記載）。ただし iGMS 公式の価格ページは、管理画面を「英語とスペイン語」と書いています。どの機能が日本語対応なのかは、わかっていません。

## 比較表

### 料金（月払い・USD）

| 項目 | iGMS | Hospitable |
|---|---|---|
| 課金モデル | PRO／PRO+：1物件あたりの月額（物件が増えるほど単価が下がる）。FLEX：予約された泊数あたり $1（最低 $20／物件／月）、予約手数料 0% | プラン固定の基本料金＋追加の「active property」ごとの単価 |
| 「物件」の数え方 | 請求周期中に1回以上予約が入った物件（キャンセル予約は対象外）。1物件目の後は、その月に確定予約のあった物件だけ課金。複数サイトの掲載をチャネルマネージャーでまとめないと別物件として課金。部屋単位で別貸しすると別物件。請求は毎月初に前月分（後払い） | 請求期間中に1回以上チェックインがあった物件、または Dynamic Pricing を有効にした物件。基本料金は、物件を停止・ミュートしていても契約中は請求される |
| 無料プラン | あり（Free、「pilot」と公式が表現）。予約5件・ゲストメッセージ10件まで。ライブチャット・電話・オンボーディングは有料のみ。公式は「it may change」と記載 | Essentials：基本料金 $0、物件数無制限、機能制限あり。サポートは AI とコミュニティのみ |
| 無料トライアル | 14日、カード不要。期限までにプランを選ばないとアカウントはブロックされる（ヘルプ記事） | 14日、カード不要 |

**物件数別の月額合計（計算値）**
前提：全物件がその月に「物件」として数えられる場合。公式が載せているのは単価で、合計はこのサイトの計算です。

| 物件数 | iGMS PRO（月払い） | iGMS PRO（年払い、月額換算） | iGMS PRO+（月払い） | Hospitable Professional | Hospitable Mogul |
|---|---|---|---|---|---|
| 1室 | $48 | $38 | $69 | $59（Host $29、Essentials $0） | $99 |
| 3室 | 約$70 | 約$62 | 約$94 | $74 | $99 |
| 5室 | 約$99 | 約$87 | 約$154 | $104 | $159 |
| 10室 | 約$174 | $150 | 約$252 | $179 | $309 |
| 20室 | 約$284 | 約$227 | 約$385 | $329 | $609 |

- Hospitable の計算式：Professional は基本 $59（2物件込み）＋追加 $15／物件、Mogul は基本 $99（3物件込み）＋追加 $30／物件。Host は基本 $29＋追加 $10 で、物件は最大2。Hospitable の年払いは 12% 割引（金額は計算していません）。20室は、Hospitable の料金ページが「Managing 20+ properties? Get a personalized walkthrough」と案内する規模です。
- **プランの中身は同じではありません。** iGMS は PRO でオーナーポータルと予約できるウェブサイト、PRO+ で収益レポート・オーナー明細など。Hospitable は Professional でダイレクト予約サイト・Google Vacation Rentals・スマートロック連携、Mogul でオーナーポータルです。合計の近さだけで「同等」とは言えません。
- 公式の料金ページは、Hospitable がプラン月額を JavaScript で描画する作りで、この調査では**ヘルプ記事の表**で金額を確認しました。第三者の PricingSaaS は「2026年7月に比較表の月額が Contact sales に置き換わった」と記録していますが、**未検証**です。

**契約・手数料**

| 項目 | iGMS | Hospitable |
|---|---|---|
| 月払いの契約縛り | なし。解約手数料なし。解約後に最終請求書、日割りの返金なし（規約） | 「No Contract or Commitments」。当月末で終了 |
| 年払い | 一括前払い（10物件未満）。「The full annual fee is non-refundable」。10物件以上は、署名する年間契約で、途中解約すると月払い料金との差額を請求 | 12か月の約束。トライアル開始から30日以内は全額返金で解約可、以後は返金なし |
| ダイレクト予約の手数料 | FLEX は 0%。無料プランの Stripe 決済は 4%（Stripe 手数料は別）。**PRO／PRO+ の iGMS 側の手数料率は、料金ページに記載が見つからなかった** | Professional／Mogul のみ。Basic 1%、Premium 4%＋決済手数料 3%（予約ごと）。Host・Essentials は不可 |
| そのほかの手数料 | 「NO hidden fees」「obligatory setup fee なし」と公式は記載。提携先（連携サービス）が別途料金を取る場合あり。税別 | アップセル 7%（Essentials 10%）、セキュリティデポジット 2%、清掃チームへの支払い 1.5%（1回あたり上限 US$5）、スマートデバイスは込みの台数を超えると 1台 $5、Vrbo の決済代行（MoR）3.9%＋Vrbo 手数料。ゲスト審査（ID確認 $2／件、Full verification $5／件）は第三者のみ。税別 |
| 料金変更 | 30日前までに通知（規約） | 記載が見つからなかった |

### チャネル（予約サイト連携）

| 項目 | iGMS | Hospitable |
|---|---|---|
| Airbnb／Booking.com／Vrbo | API 接続（直接）。公式の自称：Airbnb Preferred Partner、Booking.com Advanced Partner、Vrbo Connected Partner | Airbnb・Booking.com・Vrbo は直接の双方向接続。Airbnb「Preferred+」のバッジを掲載。Vrbo は公式の Software Switch に対応 |
| Agoda | 公式の対応チャネル一覧に記載なし | Agoda も直接の双方向接続（全プラン共通の公式表示） |
| Expedia | iCal（1時間ごとの更新、物件へのグルーピング不可） | 専用接続なし。iCal 取り込み（一方向、20分ごとに確認）に分類。Vrbo 経由の配信は Vrbo 側の設定に依存 |
| Google Vacation Rentals | 公式パートナーの掲載機能あり（提供プランの詳細は未確認） | Professional 以上 |
| 楽天トラベル・じゃらん | 公式ページに記載が見つからなかった。**接続の可否は未確認** | 同左。iCal で取り込めるかも、楽天側が iCal を出すかも**未確認** |
| 二重予約の防止 | API 接続のチャネル間で即時にブロック。API と iCal を併用すると二重ブロックになるため、直接接続したら iCal を外す | 各チャネルの掲載を物件に「Merge（結合）」して同期する。Vrbo は、接続が切れている間に予約が入ると Hospitable が予約を作れず、二重予約の可能性があると公式ヘルプが書いている |

### 機能

| 項目 | iGMS | Hospitable |
|---|---|---|
| 自動メッセージ | テンプレート、カスタムトリガー、レビュー自動化、AI返信。無料プランでも自動メッセージは使える | Essentials は定型の予約メッセージが限定的。Host 以上で自動メッセージ。AI の下書き・自動返信は Essentials で週10件まで。Mogul は Inbox AI による全自動 |
| 清掃・タスク | 清掃タスクの自動作成・割り当て、チェックリスト、SMS 通知。Turno、Operto Teams、Cleanster と連携 | 全プランに Tasks Manager と Tasks App、清掃員の探索（Cleaner Marketplace）、清掃員への支払い機能 |
| スマートロック | August、Yale、Schlage、Igloohome、Nuki、Google Nest、Keycafe、RemoteLock ほか（RemoteLock は連携ページで「Coming soon」の表示あり）。Akerun・SESAME は記載なし | August、Igloohome、Jervis、Nuki、Schlage、SmartThings、TTLock、Yale。Professional 以上。Akerun・SESAME は記載なし（個別対応の有無は未確認） |
| 価格ツール | PriceLabs、Wheelhouse、Beyond、DPGO と連携。内蔵の Dynamic Pricing は PRO+ だが、**対象は米・加・豪・メキシコ・英・スペインのみで日本は対象外**の表示 | 内蔵の Dynamic Pricing は Host 以上に込み（日本の物件で使えるかは記載が見つからなかった）。外部は PriceLabs、Beyond Pricing |
| オーナーポータル | PRO 以上（オーナー明細は PRO+） | Mogul のみ |
| ダイレクト予約サイト | PRO 以上（独自ドメイン、複数物件検索、決済は Stripe） | Professional 以上。チャージバック・損害補償付き |
| 会計 | キャッシュフローレポート、オーナー明細、物件経費（PRO+）。QuickBooks 等の連携は確認できず | Mogul：会計機能内蔵、または QuickBooks 連携。Trust Accounting は「pilot」 |
| アプリ | iOS／Android アプリ。無料プランから利用可 | プラン変更はモバイルアプリからはできない（Web か携帯ブラウザ） |

### 日本対応

| 項目 | iGMS | Hospitable |
|---|---|---|
| 管理画面の言語 | 英語とスペイン語。日本語なし | 英語のみ（「At this time, Hospitable is only available in English.」） |
| ゲスト向け自動メッセージの言語 | 「109 languages」で、ゲストの最初のメッセージから言語を自動検出して送信。判別できなければ英語。**109言語に日本語が含まれるかは未確認**（別ページに「120+ languages」の記載があり、数字が一致しない。ヘルプ記事は2025-01-17付） | 定型メッセージは英語・スペイン語・フランス語・ドイツ語。日本語追加の要望が公式フィードバックにある（2026-06-08投稿、取得時のステータスは「New」、票1）。回避策は受信箱での手書き。**日本語が実装済みかは未確認** |
| 受信箱の翻訳 | PRO+ の機能として表示。ヘルプ記事（2025年）と説明が違い、**現行の仕様は未確認** | 受信箱の自動翻訳と AI 返信が多言語、と公式の機能ページが説明 |
| サポートの言語 | 英語・スペイン語。日本語の記載なし | 英語（ヘルプセンターは英語・ポルトガル語・スペイン語）。日本語サポートの記載が見つからなかった |
| サポートの窓口と時間 | メール（"Response within 48 hours"）、ライブチャット、有料プランは1対1オンボーディング。トライアル中は平日24時間チャット（ヘルプ記事）。週末の時間は第三者のみ（未開封） | Host 以上：メール・ライブチャット・コミュニティ。Essentials：AI ボット「Smarty」とコミュニティのみ。**人間の対応時間・タイムゾーンの記載が見つからなかった** |
| 請求通貨（円） | 料金表は USD のみ。円請求の記載が見つからなかった | 請求通貨は契約者の請求住所で決まり、自分では変更できない（サポートに依頼）。公式の記載に出る通貨は USD・EUR・GBP・AUD・CAD・THB（例）で、**JPY の記載は見つからなかった** |
| 物件の通貨（宿泊料） | 物件ごとに通貨を設定する画面の記載（検索要約のみ＝第三者のみ）。円が使える一覧は見つからなかった | 物件の通貨はリード掲載から設定。「Booking.com (JPY)」を結合する例の図があり、JPY の物件を扱える示唆はある（断定はできません） |
| ツール利用料の支払い | クレジットカード（Stripe 処理） | Visa・Mastercard（全通貨）、AMEX（SGD・GBP を除く）、Discover（EUR・USD）、PayPal。口座引落は不可 |
| 請求書・適格請求書（T番号） | 記載が見つからなかった（**未確認**） | 月次の請求書をダウンロード可、EU 向けの VAT 番号欄あり。日本の登録番号や消費税の表示は見つからなかった（**未確認**。検索要約のため第三者のみ） |
| 宿泊者名簿・パスポート | 受信箱のゲスト審査バッジ（Safely 等と連携）。パスポート確認・日本の名簿様式に合わせた機能の記載は見つからなかった | ゲストポータルで政府発行ID・自撮りを確認する機能あり。対応国、パスポートの扱い、日本の名簿要件に合わせた機能の記載はなし |
| 届出番号 | 記載が見つからなかった | 物件の Licences 欄にライセンス・登録番号を入れて Vrbo／Booking.com へ連携する機能。日本固有ではない（検索要約のため第三者のみ。日本向けは未確認） |

### 乗り換え

| 項目 | iGMS | Hospitable |
|---|---|---|
| 他ツールからの自動データ移行 | 公式の自動移行機能の記載は見つからなかった | なし（「there is no way of transferring your data from a different PMS」） |
| 移行ガイド | 専用の移行ガイドは見つからなかった（/switch-to-igms/ は404）。比較ページ（vs Hospitable など）はある | 公式の移行ページと、Airbnb・Booking.com・Agoda・Vrbo ごとの接続ガイドがある |
| 予約・メッセージの引き継ぎ | 記載なし | リスティングは再作成不要。Airbnb は過去予約を最大5,000件取り込み。Booking.com は過去予約を送らない。ダイレクト／手動の予約と自動メッセージは自動では移らない |
| 切り替え中の注意 | Vrbo は Vrbo サポートに依頼してアカウントを移す説明（検索要約＝第三者のみ） | Airbnb・Vrbo は制限付き接続で旧ツールと併用できる（価格・空室管理は Hospitable を主にする）。Hostaway→Airbnb の切断が反映されるまで24〜48時間かかることがある |
| オンボーディング | 10物件以上は無料のセットアップセッション。1対1のオンボーディングは有料プランの特典 | トライアル中は無料の説明通話。有料の「Rapid Rollout」（通常3回・合計3〜5時間）は任意 |

### 利用者の声（海外レビュー）

海外レビュー（Capterra、2026-11-03時点）：iGMS 307件／4.6、Hospitable 145件／4.7。これは英語圏のレビューで、日本の運営者の実感ではありません。個別の口コミの真偽は検証していません。

| | iGMS | Hospitable |
|---|---|---|
| 不満として挙がっていた点（Capterra の個別口コミ） | 「解約できない」（2025-02-27）。Airbnb の手動ブロック日が API 接続後に消えた（2026-07-06、評価1.0）。サポートの評価は好意的な口コミと不満が混在 | カード変更が原因の支払いトラブルで旧レートを失った（2026-01-07、評価1.0）。1物件だけだと料金が高め。G2 では通知機能が弱い、アプリが時々ログアウトされる（検索要約のため第三者のみ） |
| 公式ヘルプの確認 | 公式ヘルプは解約を、リンクからの申請で営業日48時間以内に処理と案内している（口コミの真偽は未検証） | — |

## 条件別の選び方

| あなたの条件 | 先に試す方 | 根拠 |
|---|---|---|
| Agoda も同じツールでつなぎたい | Hospitable | Hospitable は Agoda を直接接続として公式表示。iGMS は公式の対応チャネル一覧に Agoda の記載なし |
| 1〜2室で、固定費を抑えて始めたい | Hospitable（Essentials か Host）／iGMS の Free プラン | Hospitable は $0／$29。iGMS の Free は予約5件・メッセージ10件までの「pilot」で、変更の可能性を公式が明記 |
| 3〜10室で月払い、PRO か Professional の機能で足りる | iGMS PRO | 計算値で 3室 約$70 対 $74、10室 約$174 対 $179。差は小さいので、次の行の条件とあわせて判断 |
| 20室前後で月払い | iGMS | 計算値で 約$284（PRO）対 $329（Professional）。ただし Hospitable は 20+ で個別案内の規模 |
| 予約のない月が多い物件がある | iGMS は予約のあった物件、Hospitable はチェックインのあった物件または Dynamic Pricing を有効にした物件に課金（基本料金・最低料金は別にかかる。Hospitable の基本料金は停止・ミュート中も請求）。iGMS の FLEX（$1／泊、最低 $20／物件）も選択肢 | 月ごとの稼働に波がある場合は、各社の数え方で自分の物件数を試算する |
| オーナー向けの精算・ポータルが必要 | iGMS PRO／PRO+、または Hospitable Mogul | iGMS はポータルが PRO、明細が PRO+。Hospitable は Mogul のみ。20室では Mogul の計算値が大きくなる |
| ゲストへ日本語で自動メッセージを送りたい | どちらも決め手なし | iGMS は109言語に日本語があるか未確認。Hospitable の定型メッセージは4言語で、日本語の要望は2026-06時点で「New」。トライアルで日本語の文面が自動送信できるか確かめる |
| 日本のスマートロック（Akerun・SESAME） | どちらも決め手なし | どちらの公式一覧にも記載なし |
| 契約の縛りを避けたい | 月払いの Hospitable／iGMS | 年払いはどちらも返金に制約（iGMS は10物件未満の年払いは返金なし、10物件以上は月払い料金との差額を請求。Hospitable は30日以内のみ全額返金） |

### 公式サイトで試す（PR）

- iGMS：[iGMS を見る（PR）](/go/igms/)
- Hospitable：[Hospitable を見る（PR）](/go/hospitable/)

## 申し込む前に確認すること

- [ ] 物件の営業形態（民泊新法・簡易宿所・特区民泊）と、載せたい国内予約サイトの掲載条件が合うか。楽天トラベル・じゃらんは、公式ページで掲載条件が上のとおり書かれている
- [ ] 英語の管理画面（Hospitable）／英語・スペイン語の管理画面（iGMS）で、日々の操作ができるか。トライアルで実際に触る
- [ ] 日本語のゲスト向けメッセージが自動で送れるか（iGMS は日本語の可否、Hospitable は日本語テンプレートの有無）
- [ ] 請求画面で通貨（円か外貨か）とカード会社の外貨手数料を確認する。両社とも円請求の記載は見つからなかった
- [ ] 「物件」の数え方に自分の運用を当てはめる（iGMS：部屋単位で別貸し・グルーピング漏れ、Hospitable：Dynamic Pricing を入れただけの物件）
- [ ] 年払いにする前に、返金条件を読む（iGMS：10物件未満は返金なし、10物件以上は月払い料金との差額を請求。Hospitable：30日以内のみ全額返金）
- [ ] ダイレクト予約を使う場合の手数料率。iGMS の PRO／PRO+ は記載が見つからなかったので、申込前に問い合わせる
- [ ] 旧ツールからの切り替えは、予約・自動メッセージが自動では移らない（Hospitable）ことを前提に、手入力する範囲を洗い出す
- [ ] 旧ツールを切ってから Airbnb の連携が空くまで、時間がかかる場合がある（Hospitable の移行ガイドの例：24〜48時間）。繁忙日を避けて切り替える
- [ ] 届出番号は Airbnb にログインして自分で入力する（Airbnb ヘルプの記載）。住宅宿泊事業の名簿・定期報告をどう運用するかは、ツールとは別に準備する

## 未確認のこと

- 楽天トラベル・じゃらんとの接続（両社とも公式に記載が見つからず、iCal での取り込みの可否も未検証）
- 日本のスマートロック（Akerun・SESAME）への対応
- 円での請求（両社）、Stripe 経由の円決済の可否（iGMS）
- iGMS のゲスト向け 109 言語に日本語が含まれるか、受信箱の自動翻訳の現行仕様
- Hospitable の定型メッセージに日本語が追加済みか（2026-06時点の要望は「New」）
- 日本の適格請求書（T番号）への対応（両社）、日本の宿泊者名簿の要件に合わせた機能（両社）、届出番号の専用欄（両社）
- iGMS PRO／PRO+ のダイレクト予約の手数料率
- 日本語サポートの有無、Hospitable の人間サポートの対応時間
- Hospitable の Dynamic Pricing が日本の物件で使えるか
- 2026年7月に Hospitable の料金ページが Contact sales に変わったという第三者の記録
- iGMS の移行支援（5物件以上の無償移行）の現行条件
- 口コミ（Capterra 以外の G2・Trustpilot は原文を取得できていません）

## 出典

取得日はすべて 2026-11-05。

**iGMS**
- https://www.igms.com/pricing/ ／ https://www.igms.com/api/public-endpoints/prices — 1. 基本、2. 料金（課金モデル、PRO／PRO+ の単価、FLEX、active property の定義、請求の時期、追加手数料）、4. 機能、5. 日本対応（UI言語、サポート言語）、8. 注意（Dynamic Pricing の対象国）
- https://igms.com/go/free-plan/ ／ https://www.igms.com/go/free-plan-terms/ — 2. 料金（無料プラン）
- https://igms.com/terms/ — 2. 料金（年払い・契約縛り・料金変更・税）
- https://help.igms.com/en/articles/9927743-how-do-i-cancel-my-igms-subscription ／ https://help.igms.com/en/articles/9927745-how-to-choose-your-igms-subscription-plan — 2. 料金（解約、トライアル）、8. 注意
- https://www.igms.com/features/channel-manager/ ／ https://help.igms.com/en/articles/9927919-how-does-the-channel-manager-work — 3. チャネル（接続方式、iCal、二重予約防止）
- https://igms.com/integrations — 3. チャネル（Agoda・楽天・じゃらんの記載なし）、4. 機能（清掃、ロック、価格ツール）、5. 日本対応
- https://help.igms.com/en/articles/9927780-how-do-i-create-message-templates-in-different-languages ／ https://help.igms.com/en/articles/9927885-how-can-igms-help-me — 5. 日本対応（ゲスト言語、サポート窓口・時間）
- https://www.igms.com/property-management-software-migration/ ／ https://www.igms.com/igms-support-program-for-hosts/ — 7. 乗り換え
- https://www.capterra.com/p/157033/iGMS/reviews/ — 8. 注意（口コミ）

**Hospitable**
- https://help.hospitable.com/en/articles/4596748-how-does-our-pricing-work — 2. 料金（課金モデル、各プラン、計算の前提、年払い、解約、手数料）、4. 機能
- https://hospitable.com/pricing — 1. 基本、2. 料金（トライアル、各種手数料）、3. チャネル、4. 機能
- https://hospitable.com/legal/subscription-agreement — 2. 料金（規約上の返金）
- https://help.hospitable.com/en/articles/14189123-understanding-how-reservations-sync-across-channels ／ https://help.hospitable.com/en/articles/16309227-switching-to-hospitable-from-another-pms — 3. チャネル、7. 乗り換え
- https://hospitable.com/integrations/smart-locks-integration-partners — 4. 機能（ロック）
- https://help.hospitable.com/en/articles/8060844-faqs-troubleshooting-account-settings ／ https://feedback.hospitable.com/p/add-japanese-as-a-language-option-in-pre-defined-guest ／ https://hospitable.com/features/multilingual-support — 5. 日本対応（UI言語、ゲスト言語）
- https://help.hospitable.com/en/articles/4605159-how-to-contact-hospitable-support ／ https://help.hospitable.com/en/articles/8060843-subscription-faqs-troubleshooting ／ https://help.hospitable.com/en/articles/12806877-property-currencies-in-hospitable-how-they-work-how-they-re-set-and-how-they-affect-your-channel-calendars ／ https://help.hospitable.com/en/articles/4533299-accepted-payment-methods — 5. 日本対応（サポート、通貨、決済手段）
- https://hospitable.com/features/guest-verification ／ https://hospitable.com/short-term-rental-license — 5. 日本対応（ゲスト確認、届出番号）
- https://hospitable.com/switch-to-hospitable — 7. 乗り換え
- https://www.capterra.com/p/189280/smartbnb/reviews/ ／ https://www.g2.com/products/hospitable-com ／ https://pricingsaas.com/companies/hospitable — 8. 注意

**日本の予約サイトと制度**
- カード「日本のOTA連携-楽天トラベルじゃらん等」：1-1-01（楽天トラベルの掲載対象）、1-1-02、1-1-08・1-1-10（Rakuten Oyado）、1-2-01（じゃらんの掲載対象）、1-5-02・1-5-04（Airbnb のヘルプ）、3-05（Hospitable）、3-06（iGMS）、3-13。URL：https://travel.rakuten.co.jp/info/hotel_msg.html ／ https://www.jalan.net/jalan/doc/howto/10sankaku.html ／ https://vacation-stay.com/host.html ／ https://www.airbnb.com/help/article/2351 ／ https://www.airbnb.com/help/article/2177
- カード「日本の制度-住宅宿泊事業法ほか」：A-07（年間180日）、A-17（名簿の記載事項）、A-26（定期報告）。URL：https://laws.e-gov.go.jp/law/429AC0000000065 ／ https://laws.e-gov.go.jp/law/429M60000900002
- README（設計図）：Capterra の評価・口コミ数と、言語欄で日本語対応とされる製品

<!-- 追加調査依頼:
1. iGMS PRO／PRO+ のダイレクト予約における iGMS 側の手数料率（料金ページに記載なし。申込フォームか営業に確認）
2. iGMS の「109 languages」に日本語が含まれるか（言語一覧）。受信箱の自動翻訳の現行仕様（ヘルプが2025年付で古い）
3. Hospitable の定型メッセージに日本語が追加されたか（feedback の「New」から更新されていないか）。管理画面・ゲスト向け日本語対応の現状
4. 両社の円（JPY）請求の可否。iGMS の物件通貨に JPY があるか、Stripe 経由で円決済ができるか。Hospitable の請求通貨一覧の全文
5. 両社の日本の適格請求書（T番号・消費税）への対応、日本の宿泊者名簿（国籍・旅券番号の記載事項）に合う機能、届出番号の表示欄の有無
6. 両社が楽天トラベル（Rakuten Oyado 経由を含む）・じゃらんに iCal などで接続できるか。楽天・じゃらん側が iCal を出力・取り込みするか
7. Airbnb の日本の民泊新法物件で、「ソフト連携で作られたリスティング不可」の規定下に、既存リスティングを PMS に接続する運用が可能か（Airbnb の日本のAPIパートナー名も含む）
8. Hospitable の Dynamic Pricing（内蔵）が日本の物件で使えるか。iGMS の日本向け価格提案は PRO+ の対象国外で確定しているか
9. Hospitable の人間サポートの対応時間とタイムゾーン、日本語サポートの有無。iGMS の週末サポート時間の原文
10. Hospitable の料金ページの現行表示（2026年7月に Contact sales へ置換されたという第三者記録の真偽）
11. iGMS の移行支援（他ソフトから5物件以上の無償移行）の現行条件
12. Capterra の言語欄で iGMS が日本語対応とされる根拠（どの機能が日本語に対応か）
-->
