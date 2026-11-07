# 事実カード：Beds24（beds24.com）

- 取得日：2026-11-05（すべての行）
- 確度の意味：`確認済`＝公式ページ・公式Wiki・公式規約（または、日本の販売会社の公式サイト）を開いて確認／`第三者のみ`＝公式を開けず第三者の情報だけ／`未確認`
- **重要な前提：Beds24には「海外の公式（Beds24 GmbH、ユーロ建て、英独のみ）」と「日本の販売会社 株式会社WeIns（co-reception.com、円建て、日本語）」の2つの入口がある。** 料金・規約・サポート・トライアル期間が別々。この2つを分けて書く。公式WikiはWeInsを日本のサービスパートナーとして掲載している（出典：下記）。
- 公式料金ページは計算機がJavaScript描画のため、**計算式は同ページが読み込む計算機スクリプトから読み取った**。

## 1. 基本

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| 運営会社（海外） | Beds24 GmbH（ベルリン、Invalidenstraße 65）。CEO: Mario Bellinzona。Amtsgericht Berlin Charlottenburg HRB 284224 B。料金ページのフッターは「© Visit Group 2026」 | https://beds24.com/en/company/impressum | 2026-11-05 | 確認済 |
| 親会社との関係 | 公式Wikiの更新情報（2025-09-02）：「Beds24 has joined forces with Visit Group」（北欧のホスピタリティ向け技術プラットフォーム） | https://wiki.beds24.com/index.php/New_Features_and_Updates | 2026-11-05 | 確認済 |
| 日本の販売会社 | 株式会社WeIns（ウィンズ、福岡市中央区大名）、サイト名「Beds24の販売サイト」(co-reception.com)。設立2014年11月、代表取締役 長坂創太 | https://co-reception.com/company/ | 2026-11-05 | 確認済 |
| 公式WikiでのWeInsの位置づけ | 「Co-Reception provides solution and consulting for Property Management in Japan. Services provided includes Beds24 in Japanese language…」（Partner／Area: Japan／Price: Upon Request）。ページ最終編集 2022-02-14 | https://wiki.beds24.com/index.php/Co-Reception | 2026-11-05 | 確認済 |
| 対象規模 | 公式は「hotel, B&B, inn, guest house, holiday home or vacation rental, cottage, hostel, campground, agency or hotel group」と幅広い。1室から利用可（計算式の最小は1室）。物件数の上限は料金ページに記載なし | https://beds24.com/en/pricing/pricing | 2026-11-05 | 確認済 |
| 利用国・規模の自己申告 | 公式：「over 150 countries」（ページにより「over 120 countries」の表記も）。日本の販売会社：「全世界で70,000施設突破」「簡易宿所・民泊向けサイトコントローラー市場シェアNo.1（2025年度:63.1%）」と出典「ミックITリポート2025年5月号」を表示 | https://beds24.com/en/pricing/pricing , https://beds24.com/reseller.html?lang=en , https://co-reception.com/ | 2026-11-05 | 確認済（表記）／シェアの一次資料は未確認 |

## 2. 料金

### 2-1 公式（Beds24 GmbH、ユーロ建て）

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| 課金モデル | 前払い（プリペイド）の従量制。「Pay as you go: no contract, no minimum term, no set-up fees」「Beds24 never charges commissions on bookings」。月額＝基本料＋部屋数＋チャネル連携数 | https://beds24.com/en/pricing/pricing | 2026-11-05 | 確認済 |
| 最低料金 | 「from €15.50/month」 | https://beds24.com/en/pricing/pricing | 2026-11-05 | 確認済 |
| 計算式 | 基本料 €12.90＋1室あたり €2.60＋「部屋タイプ数×チャネル数」あたり €0.55（計算機スクリプトの定数 BASE_PRICE=12.90、PRICE_PER_ROOM=2.60、PRICE_PER_CHANNEL_LINK=0.55）。ページ本文：「Each link costs €0.55 per month」「One link is a connection of one category or room type … to one channel」 | https://beds24.com/en/pricing/pricing （計算機 https://beds24.citybreakweb.com/themes/custom/citybreakweb/cb_beds24/js/pricing-calculator.js） | 2026-11-05 | 確認済（スクリプトから算出） |
| 物件数別の目安：1室 | 1部屋タイプ・2チャネル（例：Airbnb＋Booking.com）で €16.60／月。チャネルなしなら €15.50 | 同上（算出） | 2026-11-05 | 確認済（算出値。前提：各室が別の部屋タイプ） |
| 物件数別の目安：3室 | 3部屋タイプ・2チャネルで €24.00／月（チャネルなし €20.70、3チャネル €25.65） | 同上（算出） | 2026-11-05 | 確認済（算出値。同上） |
| 物件数別の目安：5室 | 5部屋タイプ・2チャネルで €31.40／月（チャネルなし €25.90、3チャネル €34.15） | 同上（算出） | 2026-11-05 | 確認済（算出値。同上） |
| 物件数別の目安：10室 | 10部屋タイプ・2チャネルで €49.90／月（チャネルなし €38.90、3チャネル €55.40） | 同上（算出） | 2026-11-05 | 確認済（算出値。同上） |
| 物件数別の目安：20室 | 20部屋タイプ・2チャネルで €86.90／月（チャネルなし €64.90、3チャネル €97.90） | 同上（算出） | 2026-11-05 | 確認済（算出値。同上） |
| 目安の前提 | 同じ型の部屋を複数持つ場合は「部屋タイプ数」を減らせる（同タイプ複数室は1リンクで数える）ため、実際はこの目安より安くなり得る。ポートフォリオが混在する場合は公式が「contact us for a quote」と案内 | https://beds24.com/en/pricing/pricing | 2026-11-05 | 確認済 |
| オプション | SMS通知 €0.10/通、追加ユーザーログイン €2.00/月、専用サブドメイン（Private label）€19.00/月、個別オンボーディング・オンライン研修 €79.00〜 | https://beds24.com/en/pricing/pricing | 2026-11-05 | 確認済 |
| 無料トライアル | 公式ページ：「FREE trial, without obligation … No credit card required to start」。規約：登録後14日間は無料（全機能）。ただし本番運用（予約受付・チャネル接続）の前に初回入金・アカウント情報・本人確認が必要（「Before you take live bookings or connect channels, we ask for a payment, your account details and a quick identity verification」） | https://beds24.com/en/pricing/pricing , https://beds24.com/en/company/eula-november | 2026-11-05 | 確認済 |
| 契約縛り・解約 | 規約：有料開始後は無期限契約、どちらからも「one month's notice to the end of a month」で解約可。残高は解約時に返金（未払分を差し引き）。料金ページ：「no contract, no minimum term」 | https://beds24.com/en/company/eula-november | 2026-11-05 | 確認済 |
| 料金改定 | 規約：「Beds24 may change the rates … giving six weeks' notice to the end of a month」。顧客は4週間以内に異議可（異議時は従前料金で継続） | https://beds24.com/en/company/eula-november | 2026-11-05 | 確認済 |
| 規約の適用時期 | 英語版規約の冒頭：新規登録は2026-10-12以降、既存顧客は2026-11-04から新規約。英語は参考訳で、拘束力があるのはドイツ語版。準拠法はドイツ法、管轄はベルリン | https://beds24.com/en/company/eula-november | 2026-11-05 | 確認済 |
| 支払い通貨・手段 | 料金表示はユーロ。支払いは USD／AUD／CAD／EUR／GBP／NZD のいずれか。**JPYは含まれない**。€50未満の入金は小額手数料あり。EU圏外の顧客は付加価値税なし（EU内でVAT番号なしの顧客とドイツ顧客は課税） | https://beds24.com/en/pricing/pricing | 2026-11-05 | 確認済 |
| 追加手数料（ダイレクト予約など） | 予約手数料なし（公式：「No. Beds24 never charges commissions on bookings」）。ただしOTA側の手数料、決済代行（Stripe等）の手数料は別。取引課金の機能（SMS、決済サービス等）は都度課金（規約） | https://beds24.com/en/pricing/pricing , https://beds24.com/en/company/eula-november | 2026-11-05 | 確認済 |

### 2-2 日本の販売会社（WeIns / co-reception.com、円建て）

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| 料金の目安（自社掲載の例） | 一棟貸切／ヴィラ（部屋タイプ1・室数1・Airbnb／Booking.com／Expedia）¥4,580／月。グランピング・旅館（タイプ3・10室・Airbnb／Booking.com／Expedia／じゃらん／楽天トラベル）¥17,280／月。小規模ホテル（タイプ5・20室・同5OTA）¥24,210／月。「以下の金額はプランではなく、参考価格」。税込表記かどうかは3例では明記なし（別ページは「税込4,580円/1棟から」） | https://co-reception.com/ | 2026-11-05 | 確認済 |
| 特別料金と基本仕様 | 「1棟・2部屋タイプ・2室・3OTAまでは、特別料金の4,580円」。算出された料金は予約エンジン・PMS込み。予約ごとの手数料なし。Airbnbアカウント1つにつきBeds24アカウント1つ必要。1アカウントで2名まで同時ログイン可、3名以上は作業用アカウント月額830円。支払いはクレジットカードのみ（銀行振込不可）。前月20日締め・前月末請求 | https://co-reception.com/pricing/ | 2026-11-05 | 確認済 |
| 1室・3室・5室・10室・20室の価格 | 計算機は同ページにあるがWordPressプラグインで動的描画。式は読み取れず。上の3例（1室／10室／20室）のみ確認 | https://co-reception.com/pricing/ | 2026-11-05 | 未確認（3室・5室は例なし） |
| 国内OTA連携の追加料金 | じゃらん・楽天トラベル・Yahoo!トラベル（一休.com）：月額 ¥1,200（税込）／部屋タイプ、初期費用 ¥3,000（税込）／部屋タイプ。3OTA目は初期費用のみで月額追加なし | https://co-reception.com/jalan-rakuten-ikyu/ | 2026-11-05 | 確認済 |
| 有料オプション | 宿泊者名簿 ¥1,650/月/施設、ヒントプラン（AI価格提案）¥600/月/部屋タイプ（3か月無料）、ホテルモード ¥16,200/月〜（14室以上推奨）、サブアカウント ¥830/月、フィッシングバスター ¥110/月/部屋、LINE通知 ¥11/通、SMS通知 ¥33/通（すべて税込表記） | https://co-reception.com/オプション一覧/ （URLは「オプション一覧」を日本語表記） | 2026-11-05 | 確認済 |
| 月額内（追加料金なし）の機能 | 予約エンジン、自動メッセージ（メール）、自動集金、レポート、Google民泊連携、チェックインシステム連携、スマホアプリ等 | 同上 | 2026-11-05 | 確認済 |
| 決済手数料 | Stripe決済ごとに3.6%（Stripeが利用者から徴収） | https://co-reception.com/pricing/ | 2026-11-05 | 確認済 |
| 無料トライアル | 1か月無料（初期費用無料）。※公式（Beds24 GmbH）は14日間で、日本の販売会社経由は期間が異なる | https://co-reception.com/ | 2026-11-05 | 確認済 |
| 契約縛り（日本の販売会社） | 「日本語版Beds24とBeds24コネクターのアカウントは発行後、最低1ヶ月契約となります。日割り計算は有りません」。トライアル後、カード登録で次月から自動引落。解約は毎月20日までにメールで連絡（電話不可）。20日を過ぎると翌月分が決済される。施行日 2020/3/25 | https://co-reception.com/beds24利用規約/ , https://co-reception.com/解約方法のご案内/ | 2026-11-05 | 確認済 |
| 再登録費用 | サポート窓口のフォームに「ご解約される施設を再度登録する際は5万円の費用発生」 | https://co-reception.com/support-ticket/ | 2026-11-05 | 確認済 |

## 3. チャネル

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| Airbnb | 公式マーケットプレイスで「Preferred Partner」、双方向XML連携 | https://beds24.com/en/marketplace , https://beds24.com/en/channel-manager/channel-manager | 2026-11-05 | 確認済 |
| Booking.com | 「Preferred Partner」、双方向XML | 同上 | 2026-11-05 | 確認済 |
| Vrbo | 「Preferred Partner」。Abritel／Fewo-Direkt／Stayz（XML＆iCal）も一覧にあり | 同上 | 2026-11-05 | 確認済 |
| Expedia | 「Preferred Partner」。Hotels.com、Orbitz、Wotif 等も一覧にあり | 同上 | 2026-11-05 | 確認済 |
| Agoda | 連携あり（「synchronized reservations, availability, and rates」。Agoda Homesも一覧にあり）。Preferred Partnerの表示なし | https://beds24.com/en/marketplace | 2026-11-05 | 確認済 |
| 楽天トラベル（公式Wikiの記述） | 「Rakuten Travel and Rakuten Oyado」のページあり。接続は**Vacation STAY経由**（「The connection between Beds24 and Rakuten Travel is made via Vacation STAY」）。在庫・料金を送信、予約・キャンセルを取り込み。Extra Person料金・最低泊数・最大泊数は送信不可。既存予約は自動取り込みされない。公式ページ最終編集 2024-12-03 | https://wiki.beds24.com/index.php/Rakuten | 2026-11-05 | 確認済 |
| 楽天トラベル（日本の販売会社の記述） | 「楽天トラベル × Beds24 在庫と価格を連動」（2021-02-05付）。R-Connectの申請とRakuten for Businessでの弊社アカウント作成が必要。同期間隔は約50秒。2023-08-17以降、楽天トラベルの新規参画申込が再開。**公式Wiki（Vacation STAY経由）と日本側の手順の関係は記述がそろっておらず、どちらが現行かは未確認** | https://co-reception.com/rakuten-travel-beds24/ | 2026-11-05 | 確認済（記載）／現行の接続方式は未確認 |
| じゃらん | 公式（英語）のチャネル一覧・Wikiに「Jalan」の記載なし（Wiki検索で該当なし）。日本の販売会社が「Beds24とじゃらんの連動」を提供（同期間隔 約50秒、月額 ¥1,200/部屋タイプ、初期費用 ¥3,000/部屋タイプ）。**掲載条件：旅館業許可が必須。特区民泊・住宅宿泊事業法（民泊新法）の施設は掲載対象外**（「じゃらん社の方針…（2020年9月確認）」） | https://co-reception.com/jalan-rakuten-ikyu/ , https://co-reception.com/ | 2026-11-05 | 確認済（日本の販売会社の記載）／公式Beds24の記載なし／条件の最新性は未確認 |
| Yahoo!トラベル（一休.com）・楽天バケーションステイ（Vacation STAY）・STAYJAPAN・AsiaYo ほか | 日本の販売会社の対応OTA一覧に記載。るるぶ・Relux 等の国内OTAは「Beds24コネクター」（日本製サイトコントローラー「ねっぱん！」経由の間接連動）が必要で、費用は「Beds24ご利用料金＋ねっぱんご利用料金」 | https://co-reception.com/beds24対応ota/ , https://co-reception.com/beds24-connector/ | 2026-11-05 | 確認済 |
| 接続方式まとめ | Airbnb／Booking.com／Expedia／Vrbo／Agoda：公式のXML／API連携。楽天：Vacation STAY経由（公式Wiki）。Vrbo・Airbnb：iCalでも可。iCal取り込みは3カレンダーまで（公式一覧「iCal import (3 calendar)」）。メタ検索：Google Hotel Ads、Google for Vacation Rentals、Trivago、TripAdvisor | https://beds24.com/en/channel-manager/channel-manager | 2026-11-05 | 確認済 |

## 4. 機能

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| 自動メッセージ | 公式：「Automatically send customised personal emails to guests. Automate email triggers.」統合受信箱（Airbnb・Booking.comのメッセージとテンプレート）あり。日本の販売会社：メール自動送信（内容・タイミングを自由に設定）、SMS・LINE通知は有料 | https://beds24.com/en/features/features , https://beds24.com/en/features/unified-inbox , https://co-reception.com/オプション一覧/ | 2026-11-05 | 確認済 |
| カレンダー同期（二重予約防止） | 「Pooled inventory」で全チャネルの在庫を共有。予約が入ると全チャネルへ即時に在庫を更新 | https://beds24.com/en/channel-manager/channel-manager | 2026-11-05 | 確認済 |
| 清掃タスク | 「Housekeeping: Manage cleaning and housekeeping.」。日本の販売会社は清掃レポート・清掃管理方法の解説記事と、清掃管理システム「CRS」（Beds24連携）を案内。サブアカウントで清掃会社に権限付き共有が可能 | https://beds24.com/en/features/features , https://co-reception.com/オプション一覧/ , https://wiki.beds24.com/index.php/Co-Reception | 2026-11-05 | 確認済 |
| スマートロック連携先 | 公式マーケットプレイス／Wiki：RemoteLock、Jervis、Nuki.io、Yacan、Chekin 等。日本の販売会社：キーポ（美和ロック提供）、KEYVOX、RemoteLOCK。チェックインタブレット：maneKEY、KEYVOX、民泊IN、Beds24宿泊者名簿、AdvaNceD IoT、HOTEL SMART、KEY STATION、SmartInn。Akerun・SESAME はどちらの一覧にも記載なし。ロックによってはBeds24の月額が上がる | https://beds24.com/en/marketplace , https://co-reception.com/interfacing-with-other-systems/ | 2026-11-05 | 確認済（Akerun・SESAMEの対応は未確認） |
| 価格ツール連携 | 公式マーケットプレイス：PriceLabs、Beyond、Smartpricing、RoomPriceGenie、Pricepoint、DIAMO。日本の販売会社：自社のAI価格提案「ヒントプラン」「ホテルモード」 | https://beds24.com/en/marketplace , https://co-reception.com/オプション一覧/ | 2026-11-05 | 確認済 |
| オーナーポータル | 公式Wiki：オーナー用の権限ロールでサブアカウントを設定し、閲覧範囲を制限可（Questions and Answersの「Owner Portal」節。Wiki検索の抜粋で確認し、ページ全体は開いていない）。追加ログイン €2.00/月（公式料金ページ「Additional users with access control and owner management」） | https://wiki.beds24.com/index.php/Questions_and_Answers , https://beds24.com/en/pricing/pricing | 2026-11-05 | 確認済 |
| ダイレクト予約サイト | 予約エンジン／ウィジェット／WordPressプラグイン。月額に含まれる（予約手数料なし）。決済はStripe等。Private label（独自サブドメイン）€19.00/月。利用者レビューには「無料だがデザインが簡素」との声あり（8章） | https://beds24.com/en/features/features , https://beds24.com/en/pricing/pricing | 2026-11-05 | 確認済 |
| 会計 | 請求書の自動作成（Invoices）、レポートCSV出力。会計連携：QuickBooks、Xero、BedPlus（公式マーケットプレイス） | https://beds24.com/en/features/features , https://beds24.com/en/marketplace | 2026-11-05 | 確認済 |
| 事前チェックイン | ChargeAutomation連携の「Pre-Arrival tool」でID／パスポート、カード、連絡先、自撮りを収集（無料のオンラインプレチェックイン。Beds24側は通常のチャネルマネージャー料金） | https://wiki.beds24.com/index.php/Pre-Arrival_tool | 2026-11-05 | 確認済 |
| モバイルアプリ | iOS／Androidあり。日本の販売会社の説明では料金設定など詳細な設定はアプリからはできない（空室・メッセージの確認が中心）、ログイン人数の制限なし | https://beds24.com/ （App Store・Google Playへのリンク）, https://co-reception.com/オプション一覧/ | 2026-11-05 | 確認済 |

## 5. 日本対応

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| UIの日本語 | 公式Wiki（2020-11-17編集）：管理画面は英語・ドイツ語が基本。「The Japanese version is only available via our partner Co-Reception who also provide Japanese language support.」日本の販売会社は日本語版Beds24を提供 | https://wiki.beds24.com/index.php/Setting/ownerslang , https://co-reception.com/ | 2026-11-05 | 確認済 |
| 公式サイトの言語 | beds24.com の言語切替は English／Deutsch のみ | https://beds24.com/en/pricing/pricing | 2026-11-05 | 確認済 |
| ゲスト向け予約ページ・メールの言語 | 「Let your guests book in their own language. Over 20 languages are already supported.」ゲスト言語コード一覧に ja（Japanese）あり。この言語コードはゲストへのメール送信言語の判定にも使われる | https://beds24.com/en/features/features , https://wiki.beds24.com/index.php/Setting/bookingslang | 2026-11-05 | 確認済 |
| サポート言語・対応時間（公式） | 窓口はチケット（メール）とフォーラム。「Beds24 is designed as a self-service-system.」公式Wiki：「customer support is only available in English or German」。対応時間帯は記載なし | https://beds24.com/en/using-beds24/support , https://wiki.beds24.com/index.php/Setting/ownerslang | 2026-11-05 | 確認済（時間帯は未確認） |
| サポート言語・対応時間（日本の販売会社） | 日本語。「お電話で、基本操作の説明を行います。※設定のご依頼や、問題解決はメールサポートにて対応。」解約は電話不可でメールのみ。受付時間帯は記載を見つけられず | https://co-reception.com/ , https://co-reception.com/解約方法のご案内/ | 2026-11-05 | 確認済（時間帯は未確認） |
| 通貨（JPY） | 宿泊料のJPY：公式WikiのAirbnb連携の通貨設定ページ（Wiki検索の抜粋で確認）の対応通貨リストにJPYが含まれる。一方、公式のBeds24利用料の支払通貨にJPYはない。日本の販売会社は円建て請求（カード払い） | https://wiki.beds24.com/index.php/Setting/properties.airbnbxmlcurrency , https://beds24.com/en/pricing/pricing , https://co-reception.com/pricing/ | 2026-11-05 | 確認済 |
| 決済手段 | Stripe（日本の販売会社の案内では「Stripe決済ごとに3.6%」）、PayPal、Global Payments 等（公式マーケットプレイス）。Booking.comの全予約を事前決済にする自動集金機能（日本の販売会社が説明） | https://beds24.com/en/marketplace , https://co-reception.com/pricing/ , https://co-reception.com/ | 2026-11-05 | 確認済 |
| 請求書・インボイス（宿泊客向け） | 日本の販売会社のブログ（2023-04-12）：適用税率・税率ごとの消費税額・事業者登録番号を記載した領収書をBeds24で自動作成する設定方法を解説。公式の機能一覧に請求書テンプレートあり | https://co-reception.com/invoice-system/ , https://beds24.com/en/features/features | 2026-11-05 | 確認済（ブログ記事。現行の画面での再現は未確認） |
| 請求書・インボイス（Beds24利用料の請求書） | 日本の事業者向けにBeds24（またはWeIns）が適格請求書を発行するかの記載は見つからず | — | 2026-11-05 | 未確認 |
| 宿泊者名簿・パスポート確認 | 日本の販売会社の有料オプション「Beds24宿泊者名簿」¥1,650/月/施設。ゲストがスマホ・PCから入力し、Beds24と連携、CSV出力、人数分の入力完了チェック。旧版（¥1,200/月）は予約へ反映されない。パスポート画像の収集はChargeAutomation連携のPre-Arrival tool（上記）。公式の機能一覧にも宿泊者登録フォームの自動作成あり | https://co-reception.com/new-guestregistration-news/ , https://co-reception.com/オプション一覧/ , https://beds24.com/en/features/features | 2026-11-05 | 確認済 |
| 住宅宿泊事業法に関する機能 | 日本の販売会社が「民泊新法の定期報告データを自動生成するシート」を無料配布（2023-08-16。2か月に1回の報告作業が約1/100に短縮と記載）。**システム本体の機能ではなく外部シート（note記事）**。届出番号の表示、年間180日の自動カウントについては、「count-180days-automatically」という解説記事のURLはあるが内容は開いていない。申込フォームに「物件許可種別：旅館業／民泊新法／特区民泊」の項目あり | https://co-reception.com/民泊新法の定期報告を自動化：データ自動生成シ/ , https://co-reception.com/beds24-application-form/ | 2026-11-05 | 確認済（配布シート）／本体機能は未確認 |
| 日本の予約サイト | 楽天トラベル・じゃらん・Yahoo!トラベル（一休.com）に対応（3章）。じゃらんは民泊新法・特区民泊は掲載対象外 | https://co-reception.com/jalan-rakuten-ikyu/ | 2026-11-05 | 確認済 |
| 日本のスマートロック | キーポ（美和ロック）、KEYVOX、RemoteLOCK（4章）。Akerun・SESAMEは記載なし | https://co-reception.com/interfacing-with-other-systems/ | 2026-11-05 | 確認済（Akerun・SESAMEは未確認） |

## 6. アフィリエイト

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| 有無・名称 | 公式Wikiに「Beds24 Referral Programme」（紹介制度）あり。また2025-09-16の更新情報で「Beds24 Affiliate Program」と紹介 | https://wiki.beds24.com/index.php/Refer_a_Friend , https://wiki.beds24.com/index.php/New_Features_and_Updates | 2026-11-05 | 確認済 |
| 種別 | 自社運営（外部のアフィリエイト網は使っていない。アカウント設定の「association code」と紹介リンクで追跡） | https://wiki.beds24.com/index.php/Refer_a_Friend | 2026-11-05 | 確認済 |
| 申込URL／方法 | 管理画面（SETTINGS > ACCOUNT）で「association code」を取得。リンク形式：`https://beds24.com/join.html?referrercode=XXX`（XXXをコードに置換）。専用の申込ページはない | https://wiki.beds24.com/index.php/Refer_a_Friend | 2026-11-05 | 確認済 |
| 報酬 | 「We will credit you 10% of all net payments (excluding taxes and fees) from each new customer who signed up with your referrer code to your Beds24 account.」＝紹介された新規顧客の純支払額の10%を、**自分のBeds24アカウントにクレジット**（現金ではなくアカウント残高）。期間の上限は記載なし | https://wiki.beds24.com/index.php/Refer_a_Friend | 2026-11-05 | 確認済（期間・現金化の可否は未確認） |
| 規約上の制限 | 唯一の記載：「We reserve the right to terminate the programme if the programme is misused or unfairly used.」ブランド名入札禁止、コンテンツ制限、クッキー期間などは記載なし。Wikiページ最終編集 2025-04-19 | https://wiki.beds24.com/index.php/Refer_a_Friend | 2026-11-05 | 確認済（記載が少ない＝他の制限は未確認） |
| その他の提携制度 | 「Partner and reseller program」：ホワイトラベル（自社ブランド）でBeds24を販売するリセラー、APIベースのホワイトラベルのチャネルマネージャー、統合パートナー（Marketplace）。条件は個別問い合わせ | https://beds24.com/reseller.html?lang=en | 2026-11-05 | 確認済 |
| 日本の販売会社の紹介制度 | 公式サイトで紹介報酬の制度は見つからず（OTA向けアフィリエイト等のURLはあるが内容は開いていない） | https://co-reception.com/ | 2026-11-05 | 未確認 |

## 7. 乗り換え

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| 物件の取り込み | 公式：「Listing import: If you have existing listings you can import them into Beds24 so you can get instantly started.」「Quick setup via property import」 | https://beds24.com/en/channel-manager/channel-manager , https://beds24.com/en/pricing/pricing | 2026-11-05 | 確認済 |
| 移行支援（公式） | 個別オンボーディング・オンライン研修 €79.00〜（有料）。公式の他ツールからの移行ガイド（手順書）は、今回は見つからず。規約には「Switching providers and data portability」（Beds24から他社へ移る際のデータ提供） | https://beds24.com/en/pricing/pricing , https://beds24.com/en/company/eula-november | 2026-11-05 | 確認済（他社からの移行ガイドは未確認） |
| 日本の販売会社の移行支援 | 申込フォームに「既に利用中のサイトコントローラーのシステム名」（ねっぱん／手間いらず／その他）の欄あり。国内OTA連動は、他社サイトコントローラーと連動中の場合は事前に解除が必要で、解除後はオーバーブック防止のためOTA側で売り止めする手順。新規OTA連動の所要は4営業日（サポート窓口フォームの記載）。既存予約は自動取り込みされないため手入力が必要（楽天トラベルの手順） | https://co-reception.com/beds24-application-form/ , https://co-reception.com/jalan-rakuten-ikyu/ , https://co-reception.com/support-ticket/ | 2026-11-05 | 確認済 |
| ねっぱん！との併用 | 「Beds24とねっぱん！を連動」するコネクター（月額はBeds24＋ねっぱんの合計）。Beds24とねっぱん連動の準備・手順・注意点の記事あり | https://co-reception.com/beds24-connector/ | 2026-11-05 | 確認済 |

## 8. 注意すべき点（利用者の不満・公式内の注意）

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| 総合評価（参考） | Capterra：4.7（117件）。最終更新 2026-09-29 | https://www.capterra.com/p/123511/Beds24-com/reviews/ | 2026-11-05 | 第三者のみ（レビューサイトを開いて確認。個別の主張は未検証） |
| 利用者の不満：UI・学習コスト | Capterraの低評価（Cons）：「The user interface could be more modern and intuitive. Some settings and configuration options are difficult to find, and the learning curve can be steep」。別のレビュー：「This is a DIY solution, which means that you have to do a lot of reading」 | https://www.capterra.com/p/123511/Beds24-com/reviews/ | 2026-11-05 | 第三者のみ |
| 利用者の不満：国内OTA接続 | Capterraの日本語レビュー：「国内OTAとの接続はサポートへの依頼が必要で手間に感じました」。ITreview（2025-08-23、1件のみ）：「UIが致命的に悪い」「サポートがメールのみ」「不具合、バグが多い印象です（特にサイトコントローラ周りでは…取り込みエラーが起きます）」。一方「とにかく安いこと」「日本語サポートが受けられるようになりました」とも書かれている | https://www.capterra.com/p/123511/Beds24-com/reviews/ , https://www.itreview.jp/products/beds24/reviews/219517 | 2026-11-05 | 第三者のみ（個別レビュー） |
| 利用者の不満：サポート | Capterraの低評価：「support was only available by email, and their support team was based in Germany, working only during their business hours」（海外公式サポートの話。日本語サポートは別窓口） | https://www.capterra.com/p/123511/Beds24-com/reviews/ | 2026-11-05 | 第三者のみ |
| 利用者の不満：予約エンジンの見た目 | Capterraの日本語レビューに「予約エンジンのデザイン性」「月額費用に含まれている予約サイトが少し安っぽいデザイン」との趣旨 | https://www.capterra.com/p/123511/Beds24-com/reviews/ | 2026-11-05 | 第三者のみ |
| 連携障害のお知らせが頻繁 | 日本の販売会社のお知らせ一覧に、楽天トラベル・Airbnb・じゃらんコネクターの「連動エラー」「サーバーエラー」「復旧のお知らせ」の投稿が多数（件名のみ確認。件数・期間の集計はしていない） | https://co-reception.com/wp-sitemap.xml （サイトマップ上のページ名のみ確認。記事本文は開いていない） | 2026-11-05 | 確認済（ページ名のみ） |
| 日本の販売会社の契約条件 | 最低1か月・日割りなし、解約は毎月20日締め・メールのみ、再登録に5万円、支払いはカードのみ（2章） | https://co-reception.com/beds24利用規約/ , https://co-reception.com/support-ticket/ | 2026-11-05 | 確認済 |
| じゃらん掲載の対象外 | 民泊新法・特区民泊の施設はじゃらんに掲載できない（3章） | https://co-reception.com/jalan-rakuten-ikyu/ | 2026-11-05 | 確認済（日本の販売会社の記載。2020年9月確認とある） |
| 規約が直近に改定 | 英語規約：新規約は新規登録に2026-10-12以降、既存顧客に2026-11-04から適用（旧規約は2018-05-20付のUser agreement） | https://beds24.com/en/company/eula-november | 2026-11-05 | 確認済 |
| 契約主体の混同 | 公式料金（€、14日トライアル、月単位で解約）と日本の販売会社の条件（¥、1か月トライアル、20日締め）は別。どちらで契約するかで条件が変わる。日本の販売会社経由の契約主体や、公式との料金差の理由は記載なし | https://beds24.com/en/pricing/pricing , https://co-reception.com/pricing/ | 2026-11-05 | 確認済（差異）／契約主体の詳細は未確認 |
| Trustpilot（日本語ページ）の評価 | 検索結果の要約には「5段階中2.8」とあったが、ページはアクセス拒否（403）で開けず | https://jp.trustpilot.com/review/beds24.com | 2026-11-05 | 未確認 |

## 調べられなかったこと（未確認の一覧）

1. 日本の販売会社の料金計算式（計算機は動的描画）。3室・5室の円建て料金。3例が税込かどうか
2. 日本語サポートの受付時間帯・電話番号・対応曜日（サイトに記載を見つけられず）
3. 楽天トラベル連携の現行方式（公式Wiki＝Vacation STAY経由／日本の販売会社＝R-Connect＋Rakuten for Business の2系統の記述が併存。最終更新は公式が2024-12、日本側が2021年の記事）
4. じゃらん連携の公式Beds24側の記載（英語のチャネル一覧とWikiに記載なし。日本の販売会社の提供サービスとして確認）。じゃらん掲載条件の最新状況
5. 住宅宿泊事業法対応：届出番号の表示、年間180日の自動カウントの本体機能の有無（「定期報告シート」は外部配布で確認）
6. Beds24利用料に対する適格請求書（インボイス）の発行有無
7. Akerun・SESAMEとの連携（どの一覧にも記載なし）
8. 他社ツール（Uplisting等）からの移行ガイド・データ移行ツールの有無
9. アフィリエイト（Referral）の有効期間、現金化の可否、日本居住者の参加可否、クッキー期間、ブランド名入札禁止の有無（Wikiに記載なし）
10. 日本の販売会社独自の紹介制度の有無
11. 日本の販売会社と公式Beds24の間の契約関係・料金差の理由
12. Trustpilotの評価の中身、Capterra以外の評価の網羅
13. 計算機スクリプトの定数が実際の請求と一致するか（アカウントを作成して請求を確認していない）
14. 「count-180days-automatically」「Booking.com事前決済」等、日本の販売会社の個別ブログ記事の中身（URLの存在のみ確認）
