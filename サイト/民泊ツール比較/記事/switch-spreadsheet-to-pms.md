---
title: 表計算（スプレッドシート）管理から民泊管理ツールへ｜3〜15室の料金の切り替わり点と注意点
slug: switch-spreadsheet-to-pms
type: 乗り換え
products: [beds24, ownerrez, hospitable, igms, uplisting, guesty, hostaway, lodgify, sirvoy]
description: 表計算での民泊管理から管理ツールへ。1〜20室の月額の目安、料金体系が切り替わる室数、予約データの取り込み方を整理。
cards: [Beds24, OwnerRez, Hospitable, iGMS, Uplisting, Guesty, Hostaway, Lodgify, Sirvoy, 日本のOTA連携-楽天トラベルじゃらん等, 日本の制度-住宅宿泊事業法ほか]
updated: 2026-11-05
pr: true
---

この記事にはアフィリエイトリンク（PR）が含まれます。

# 表計算（スプレッドシート）管理から民泊管理ツールへ｜何物件から検討するか

> **結論**
> - 「何物件から元が取れるか」は、時間の節約や売上の増加を示す根拠が確認できた資料にないため、この記事では答えを出しません。費用の側（月額の目安と、料金体系が切り替わる室数）だけを並べます。
> - 3〜5室のあたりで料金の仕組みが変わる製品が多いです（Guesty Lite は3室まで、Hospitable の Host プランは2室まで、Uplisting の Independent Host は4室まで、Lodgify の Basic は1室・Starter は2室まで）。
> - 楽天トラベル・じゃらんも同じ画面で管理したい人は、公式ページで確認できたのは Beds24 の日本の販売会社版（WeIns / Co-Reception）だけです。申込は海外公式（PRリンク）とは別です。ほかの製品は公式ページに記載が見つからず「未確認」です。

## 先に知っておくこと（日本で使うときの前提）

表計算で管理している人が、ツールに移したくなる作業の候補と、公式ページでわかっていることを分けます。

**1. 日本の制度の作業（公式資料の引用の範囲。法的な判断はしません）**

| 作業 | 制度側の事実（観光庁・e-Gov の引用） | ツール側 |
|---|---|---|
| 年間の宿泊日数の管理（住宅宿泊事業＝民泊新法の場合） | 年180日の上限。数え方は毎年4月1日正午から翌年4月1日正午まで、正午から翌日の正午までを1日とする。届出住宅ごとに算定する（法第2条第3項、規則第3条、民泊制度ポータル） | 9製品とも、180日の自動カウント機能の記載は公式ページで見つからなかった（未確認）。Beds24 の日本の販売会社が「count-180days-automatically」という解説記事を出しているが、本文は開いていない |
| 定期報告（住宅宿泊事業＝民泊新法の場合） | 2・4・6・8・10・12月の15日までに、直前2か月分の宿泊日数・宿泊者数・延べ宿泊者数・国籍別の内訳（規則第12条） | Beds24 の日本の販売会社が、定期報告のデータを自動生成する無料の外部シートを配布している（システム本体の機能ではない）。ほかは記載が見つからなかった（未確認） |
| 宿泊者名簿 | 全員分を記載。作成の日から3年間保存。電磁的記録でもよい（規則第7条、ポータル） | Beds24 の日本の販売会社に有料オプションの名簿機能（月1,650円/施設）あり。ほかの製品が日本の名簿の様式に合うかは未確認 |

なお、旅館業法には営業日数の上限を定める条文が見当たらず（B-05）、特区民泊も要件に上限の記載がありません（C-05）。同じ180日の上限が旅館業・特区民泊にも当てはまる、とは読めませんでした（制度の判断はしません）。

**2. 国内の予約サイトを使っている・使いたい場合**

- 楽天トラベルの公式ページには、民泊新法（住宅宿泊事業法）の施設は参画できないという趣旨の記載があり、民泊新法・特区民泊の施設の案内先は楽天グループの「Rakuten Oyado」とされています。
- じゃらんnet の公式ページにも、民泊新法・特区民泊に基づく施設は掲載できないという趣旨の記載があります。
- 両社とも民泊新法・特区民泊は対象外と明記していますが、旅館業法の許可施設に各ツールが接続できるかは、どのツールも未確認です。
- つまり、物件がどの制度（届出・許可）に基づくかで、国内予約サイトにつなぐ方法が変わります。

**3. 通貨と言語**

- 9製品のうち、日本語の管理画面が確認できるのは、Beds24 の日本の販売会社版（株式会社WeIns）だけです。日本語サポートも同じですが、Sirvoy はヘルプ記事に日本語が含まれ、公式FAQには日本語がなく食い違っています（実態は未確認）。Guesty の公式サポート言語一覧には日本語がありません。ほかの製品の管理画面に日本語は見つかりませんでした。
- 請求通貨は、公式の記載で円（JPY）が確認できた製品はありません（Beds24 は日本の販売会社が円建てで請求）。

## 比較表1：月額料金の目安（物件数別）

- 金額は各社の表示通貨のままです。円への換算はしていません。
- 「計算値」は、公式の料金表や計算式から当サイトが掛け算・足し算した値で、公式がその合計を載せているわけではありません。
- 全室が稼働している前提です。税・追加機能・決済手数料は含みません。

| 製品（通貨・プラン） | 1室 | 3室 | 5室 | 10室 | 20室 | 確度 |
|---|---|---|---|---|---|---|
| Beds24 公式（EUR、2チャネル接続、各室が別の部屋タイプの場合） | €16.60 | €24.00 | €31.40 | €49.90 | €86.90 | 計算値（公式の計算機スクリプトの定数から算出）。同じ型の部屋が複数なら、部屋タイプ数が減って安くなりうる |
| OwnerRez（USD） | $40 | $70 | $88 | $127 | $196 | 公式の料金表。5室の$88は公式ページの表示、ほかは計算値。最低料金は月$40 |
| Hospitable Professional（USD、月払い） | $59 | $74 | $104 | $179 | $329 | 計算値 |
| Hospitable Mogul（USD、月払い） | $99 | $99 | $159 | $309 | $609 | 計算値。20室を超えると別扱い（Enterprise） |
| iGMS PRO（USD、月払い） | $48 | 約$70 | 約$99 | 約$174 | 約$284 | 計算値（公式の1物件あたり単価×物件数） |
| iGMS PRO（USD、年払い） | $38 | 約$62 | 約$87 | $150 | 約$227 | 計算値 |
| Uplisting（GBP） | £40（Independent Host） | £72（Independent Host） | £90（Operator） | £160（Operator） | £320（Operator）／£260（Manager） | 計算値（公式料金ページの計算ロジックから算出） |
| Guesty Lite（USD） | $9＋予約の1%（Pay as you grow） | $27＋予約の1%（計算値） | Lite は3室まで | Lite は3室まで | Lite は3室まで | Lite の単価は確認済み。Pro（4室以上）の価格は非公開（見積り） |
| Hostaway | 公式は非公開（見積り） | 同左 | 同左 | 同左 | 同左 | 第三者の推定はあるが、数字がサイトごとに大きく異なり、公式の裏付けもない |
| Lodgify（USD、1物件） | Basic $14／Starter $26／Professional $47／Ultimate $68 | 未確認 | 未確認 | 未確認 | 未確認 | 1物件の表示価格のみ。支払周期は推定。3室以上はスライダー計算で取得できなかった。公式サイトの確認は公開コピー由来で、本体（www）との一致は未照合 |
| Sirvoy（USD、月払い） | Free $0／Starter $15／Pro $54 | $20／$73 | $20／$73 | $28／$98 | $38／$135 | 公式の料金データを室数に当てはめたもの。チャネルマネージャーは Pro のみ |

補足:

- Beds24 の日本の販売会社（WeIns）は円建ての参考価格を載せています。「一棟貸切・部屋タイプ1・Airbnb／Booking.com／Expedia」で月4,580円、「部屋タイプ3・10室・5つの予約サイト（じゃらん・楽天トラベル含む）」で月17,280円、「部屋タイプ5・20室・同5サイト」で月24,210円です。公式は「プランではなく参考価格」としており、3例が税込かは明記がなく、3室・5室の価格は未確認です。国内予約サイト（じゃらん・楽天トラベル・Yahoo!トラベル）の接続には、部屋タイプあたり月1,200円（税込）と初期費用3,000円（税込）の料金表記もあります（3つ目の予約サイトは初期費用のみ）。ただし、これが上の3例の金額に含まれるのか別なのかは未確認です。
- Hostaway の第三者の推定は、1〜4室で月$125〜$175、5〜9室で月$175〜$250といった例がありますが、公式の裏付けはなく、1室あたり$25〜$50という別の報告もあります。参考にとどめてください。
- Hospitable は、機能で絞ると料金が変わります。スマートロック連携は Professional 以上、オーナーポータルは Mogul のみです。

## 比較表2：料金体系が切り替わる室数

| 製品 | 切り替わり |
|---|---|
| Guesty | Lite は1〜3室、Pro は4〜199室（Pro は見積り） |
| Hospitable | Host は最大2物件。3室以上は Professional か Mogul |
| Lodgify | Basic は1物件以下、Starter は2物件以下。3室以上は Professional 以上が前提（ページの記載から読み取れる範囲） |
| Uplisting | Independent Host は4物件まで。5物件以上は Operator（5物件までは月£90が下限）。従量プラン（月£0＋予約ごとの手数料）は10物件まで |
| Sirvoy | Free は1室のみ。チャネルマネージャーは Pro のみ（Starter 以下には予約サイト連携がない） |
| iGMS | 単価が物件数に応じて下がる方式。1物件目の後は、その月に予約のあった物件だけが課金対象 |
| OwnerRez | 1物件目$40、2〜3物件目各$15、4物件目$10、5〜9物件目各$8、10〜19物件目各$7、20〜49物件目各$6 |
| Beds24 | 基本料＋部屋数＋「部屋タイプ数×チャネル数」で計算（式は公式の計算機スクリプトから読み取り） |

## 何物件から検討する価値があるか：言えること／言えないこと

- **言えること**：上の2つの表のとおり、費用は製品ごとに仕組みが違い、3〜5室のあたりで切り替わるものが複数あります。
- **言えないこと**：どの物件数から元が取れるか。確認できた資料に、時間の節約量や売上の増加を示す根拠がないためです。
- 表計算を続ける費用（手作業の時間など）は、この記事では扱いません。ご自身の運営で、二重予約や返信の遅れが実際に何件起きているかを数えたうえで、上の月額と見比べる使い方を想定しています。

## 予約データの取り込み：表計算から移すとき

表計算の予約データをツールに入れる方法として、公式ページに書かれているものです。

| 製品 | 公式に書かれている取り込み | 書かれていない点 |
|---|---|---|
| Sirvoy | 内蔵の予約インポート。5件未満は手入力、15件未満はスプレッドシート風フォーム、多数はファイル取り込み。必須列・日付形式の要件あり | 取り込んだ予約はどのチャネルとも紐づかない（変更・キャンセルは各チャネルで確認が必要）。列名の詳細は未確認 |
| OwnerRez | Excel テンプレートで予約・請求・入金・返金を一括取り込み（Tools > Import/Export）。Airbnb の掲載情報は1回限りのインポート | データ移行の代行は記載なし。無料の1時間「Jumpstart」通話はある |
| Hospitable | リスティングは作り直さず既存の掲載に接続。ダイレクト・手動の予約は自動で移らず、少数なら手入力、大量なら CSV をサポートが取り込む | CSV の形式は未確認 |
| Beds24 | 既存の掲載を取り込む機能（公式）。日本の販売会社の楽天トラベル連動の手順では、既存の予約は自動で取り込まれず手入力が必要 | 表計算ファイルの取り込み形式は未確認 |
| Lodgify | 「オンボーディングチームが、現在のシステムからリスティング・予約・ゲストデータを取り込む」と記載（料金ページでは Starter 以上の1:1オンボーディング。乗り換えページの無料オンボーディングが Basic にも及ぶかは記載が揃わず不明） | 具体的な形式・対応元は公式ページに記載なし（未確認） |
| Guesty | 大量データ向けに「templates and bulk tools」を提供と記載。Pro は専任担当者が設定・データ移行を行う | 形式・手順は未確認 |
| Uplisting | Airbnb を読み取り専用で接続してリスティング・料金・予約を取り込み、既存の直接予約のインポートも手順に含まれる。全プランに無料の1:1オンボーディング | 直接予約の取り込み方法の詳細は未確認 |
| iGMS | 他ツールからの自動データ移行機能は記載が見つからなかった | 10物件以上は無料のセットアップセッションあり |
| Hostaway | 公式ブログに「24/7 customer support and live onboarding」の記載 | インポート方法は未確認（ヘルプセンターを開けていない） |

利用者が自分で表計算ファイルを取り込む手順が公式に書かれているのは、Sirvoy と OwnerRez だけでした（どちらも列の詳細は確認していません）。Hospitable は大量の場合に CSV をサポートが取り込むと書かれていますが、形式は未確認です。

## 予約サイトの範囲（Airbnb 以外）

| 製品 | 公式APIで接続 | 国内予約サイト（楽天トラベル・じゃらん） |
|---|---|---|
| Guesty | Airbnb・Booking.com・Vrbo・Expedia（Lite は Airbnb・Booking.com・Vrbo の3つ） | 公式のチャネル一覧の表示分に記載なし（未確認） |
| Hostaway | Airbnb・Booking.com・Vrbo・Expedia | 公式の一覧に記載なし（未確認） |
| Lodgify | Airbnb・Vrbo・Booking.com（Expedia はページにより記述が食い違う）。ほかは iCal | 連携一覧に記載なし（未確認） |
| OwnerRez | Airbnb・Booking.com・Vrbo・Google Vacation Rentals | 記載なし（未確認） |
| Hospitable | Airbnb・Vrbo・Booking.com・Agoda（Expedia は iCal のみ） | 記載なし（未確認） |
| iGMS | Airbnb・Vrbo・Booking.com（Expedia・Tripadvisor は iCal） | 記載なし（未確認） |
| Uplisting | Airbnb・Booking.com・Vrbo（Expedia は Vrbo 経由か iCal） | 記載なし（未確認） |
| Beds24 | Airbnb・Booking.com・Vrbo・Expedia・Agoda（XML/API） | 楽天トラベルは公式Wikiに記載あり（Vacation STAY＝Rakuten Oyado 経由）。日本の販売会社は別手順（R-Connect 申請など）を記載しており、現行方式は未確認。じゃらんは日本の販売会社が提供（公式の英語チャネル一覧・Wikiには記載なし） |
| Sirvoy（公式サイトで確認） | Airbnb・Booking.com・Expedia・Agoda（Pro）。Vrbo は iCal | 公式ページに記載なし |

「記載なし」は「接続できない」という意味ではありません。記載を見つけられなかっただけです。

## 条件別の選び方

| あなたの条件 | 見る順番 |
|---|---|
| 楽天トラベル・じゃらんも一緒に管理したい／日本語の画面とサポートが必要 | 公式で確認できたのは Beds24 の日本の販売会社版（WeIns / Co-Reception。リンクなし）。申込は [Beds24（海外公式。PRリンク）](/go/beds24/)とは別です。じゃらんは民泊新法の施設は掲載対象外とされています。お知らせ一覧に連動エラーの投稿が複数ある（件名のみ確認）こと、解約の締切（毎月20日までにメール）などの契約条件も、必ず確認してください |
| Airbnb・Booking.com・Vrbo が中心。英語の画面で運用できる。費用を物件数に応じて増やしたい | [OwnerRez](/go/ownerrez/)（月$40から、契約縛りなし、返金なし）、[Hospitable](/go/hospitable/)（月払いは縛りなし。物件が増えると追加課金）、[iGMS](/go/igms/)（単価が物件数で下がる）の順に、自分の室数の行を比べる。Sirvoy（Pro：5室 $73、10室 $98。Vrbo は iCal、JPY なし）も比較表1にある |
| 都市部で10室以上を持つ予定 | [Uplisting](/go/uplisting/) は公式が「10〜300+物件の都市型管理者」向けと説明している。ただし規約は「最低12か月・自動更新」、料金ページは「契約なし」と食い違うので、申込前に確認 |
| 料金が見積り制でもよい。担当者との相談で決めたい | [Guesty](/go/guesty/)（Pro は4室以上で見積り）、[Hostaway](/go/hostaway/)（料金ページは入力フォームのみ） |
| 自社の予約サイトも作りたい | 予約サイト機能は多くの製品にあります（OwnerRez・Hospitable・iGMS・Beds24・Sirvoy・Guesty・Uplisting・Hostaway。プラン条件あり。例：Hospitable は Professional 以上、iGMS は PRO 以上）。比較表1の価格で選びます。[Lodgify](/go/lodgify/) はサイト作成が中心（Starter 以上。ただし3室以上の価格は未確認、請求は EUR/USD/GBP） |
| 1室だけ。まず無料で試したい | Sirvoy の Free（1室のみ。予約サイト連携は Pro のみ）、Hospitable の Essentials（$0。人のサポートなし。価格ツールとの外部連携は有料プランが必要で、予約サイトの接続は全プラン共通）、iGMS の無料プラン（予約5件・メッセージ10件まで、試験提供）。いずれも制限が大きいので、条件を読んでから |

## 申し込む前に確認すること

- [ ] 自分の物件が、どの制度（住宅宿泊事業の届出、旅館業の許可、特区民泊）に基づくか。国内予約サイトにつなぐ方法が変わる
- [ ] 年180日の管理と2か月ごとの定期報告を、今は表計算でやっているか。やっているなら、移したあとの方法を決める（ツール側の対応はほぼ未確認）
- [ ] 宿泊者名簿（全員分・3年保存）と旅券の写しの保存場所を、移したあとも決められるか
- [ ] 請求通貨と支払い方法：円で請求されるか（Beds24 の日本の販売会社以外は、円の記載が見つからなかった）。支払いはカードのみの製品が多い（OwnerRez・Beds24 の日本の販売会社など）
- [ ] 無料トライアルの日数と、カード登録の要否：Beds24 公式14日（本番前に入金・本人確認が必要）／日本の販売会社1か月無料、OwnerRez 14日、Hospitable 14日（カード不要）、iGMS 14日（カード不要）、Uplisting 14日（カード不要）、Guesty Lite 14日（カード不要）、Lodgify 7日（カード不要）、Sirvoy 14日（カード不要）。Hostaway は無料トライアルが公式で確認できず（デモ申込はある）
- [ ] 解約条件：Guesty は規約上13か月の初期期間＋自動更新（契約書の記載が優先）、Lodgify は規約上、更新前の通知なしで自動更新（料金ページには「no long-term contract, cancel any time」ともあり、両方の記載がある）、iGMS の年払い（10物件未満）は返金なし、Beds24 の日本の販売会社は最低1か月・日割りなし・再登録に5万円
- [ ] 価格の通知ルール：値上げの通知期間（Hostaway 14日前、Lodgify 30日前、iGMS 30日前、Beds24 公式6週間前、Uplisting は規約に「年1回以上、5%」の値上げ条項）
- [ ] 表計算の予約データの列と日付形式を、取り込み方法（上の表）に合わせて整える。必要な列は製品ごとに異なる
- [ ] 乗り換え後の最初の1か月は、表計算の控えを残しておく（旧データとの突き合わせ用）

## 未確認のこと

- 管理ツールを導入して時間や二重予約がどう変わるか（効果）。確認できた資料に根拠がありません
- 180日の自動カウント・届出番号の表示・定期報告の機能（9製品とも公式ページで記載が見つからなかった。Beds24 の日本の販売会社の外部シートを除く）
- Lodgify の3・5・10・20室の料金、Hostaway の公式料金、Guesty Pro の公式料金
- 円（JPY）での請求の可否（Guesty・Hostaway・Hospitable・iGMS・OwnerRez・Lodgify・Uplisting）
- 楽天トラベル・じゃらんへの接続（Beds24 以外の8製品）
- 表計算ファイルから取り込む形式（Guesty・Hostaway・Lodgify・Hospitable〔サポートが CSV を取り込むが形式は未確認〕・iGMS・Uplisting）
- 日本のインボイス制度（適格請求書）への対応

## 出典

取得日はすべて 2026-11-05。

- **Beds24**：§2 料金（2-1 公式、2-2 日本の販売会社）https://beds24.com/en/pricing/pricing ／ https://co-reception.com/ ／ https://co-reception.com/pricing/ ／ https://co-reception.com/jalan-rakuten-ikyu/ ／ https://co-reception.com/beds24利用規約/。§5 日本対応（名簿・定期報告シート）https://co-reception.com/new-guestregistration-news/ ／ https://co-reception.com/民泊新法の定期報告を自動化：データ自動生成シ/ 。§7 乗り換え https://beds24.com/en/channel-manager/channel-manager
- **OwnerRez**：§2 料金、§7 乗り換え（インポート方法）https://www.ownerrez.com/support/articles/costs-and-fees ／ https://www.ownerrez.com/pricing ／ https://www.ownerrez.com/support/articles/importing-outside-bookings ／ https://www.ownerrez.com/support/articles/jumpstart
- **Hospitable**：§2 料金、§7 乗り換え https://help.hospitable.com/en/articles/4596748-how-does-our-pricing-work ／ https://hospitable.com/switch-to-hospitable ／ https://help.hospitable.com/en/articles/16309227-switching-to-hospitable-from-another-pms
- **iGMS**：§2 料金、§7 乗り換え https://www.igms.com/pricing/ ／ https://igms.com/terms/ ／ https://igms.com/go/free-plan/
- **Uplisting**：§2 料金、§7 乗り換え https://www.uplisting.io/pricing ／ https://www.uplisting.io/switch-to-uplisting ／ https://www.uplisting.io/legal/terms-and-conditions ／ https://support.uplisting.io/en/article/is-uplisting-right-for-me-hjm9f5/
- **Guesty**：§2 料金、§7 乗り換え https://www.guesty.com/pricing/ ／ https://www.guesty.com/packages/guesty-lite/ ／ https://www.guesty.com/terms-of-service/ ／ https://www.guesty.com/onboarding/
- **Hostaway**：§2 料金、§7 乗り換え https://www.hostaway.com/pricing/ ／ https://www.hostaway.com/terms/ ／ https://www.hostaway.com/blog/switching-pms-platforms/ ／ https://www.roommaster.com/blog/hostaway-pricing（第三者の推定）
- **Lodgify**：§2 料金、§7 乗り換え https://webflow-mkt.lodgify.com/pricing ／ https://webflow-mkt.lodgify.com/switching-software ／ https://webflow-mkt.lodgify.com/terms（`www.lodgify.com` は開けず、同内容の公開コピーを開いた）
- **Sirvoy**：料金、乗り換え https://sirvoy.com/pricing ／ https://help.sirvoy.com/en_US/import-bookings/import-your-existing-bookings
- **日本のOTA連携**：1-1-01・1-1-02（楽天トラベル）https://travel.rakuten.co.jp/info/hotel_msg.html ／ 1-2-01（じゃらんnet）https://www.jalan.net/jalan/doc/howto/10sankaku.html ／ 3章 海外PMS 9社
- **日本の制度**：A-07〜A-09（年180日）、A-16・A-17・A-19・A-20（宿泊者名簿）、A-26（定期報告）https://laws.e-gov.go.jp/law/429AC0000000065 ／ https://laws.e-gov.go.jp/law/429M60000900002 ／ https://www.mlit.go.jp/kankocho/minpaku/overview/minpaku/law1.html ／ https://www.mlit.go.jp/kankocho/minpaku/business/host/responsibility01.html

<!-- 追加調査依頼:
1. Lodgify の3・5・10・20室の公式料金（スライダー計算。Professional 以上の単価と、価格表示の支払周期）
2. Hostaway の公式料金（1・3・5・10・20室）と、1室向けプランの有無
3. Guesty Pro の公式料金（4室以上）とオンボーディング費用の公式額
4. 9製品の「年180日のカウント」「届出番号の表示」「定期報告用データの出力」機能の有無（ヘルプセンター・ログイン後の画面を含む）
5. 表計算（CSV/Excel）からの予約取り込み形式（必須列・日付形式）：Guesty、Hostaway、Lodgify、Hospitable、iGMS、Uplisting
6. 円（JPY）での請求の可否：Guesty、Hostaway、Hospitable、iGMS、OwnerRez、Lodgify
7. Beds24 の日本の販売会社の3室・5室の円建て料金（計算機の式）と、3例の税込・税別、国内予約サイト接続料（月1,200円・初期3,000円）が3例に含まれるか
8. /go/beds24/ の遷移先が海外公式（beds24.com の紹介リンク）で確定か。日本の販売会社（WeIns）に紹介制度があるか。Beds24 の楽天トラベル接続の現行方式
9. Sirvoy の日本語サポートの実態（ヘルプ記事と公式FAQの食い違い）
-->
