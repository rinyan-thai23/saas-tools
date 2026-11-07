# 事実カード：日本のOTA連携（楽天トラベル・じゃらん等）

- 取得日はすべて 2026-11-05。引用は原文のまま短く。**評価・おすすめは書かない。**
- 確度の使い方：`確認済`＝その行の出典ページを開いて、その記載を確認した（ベンダー自社ページの自己申告も「そのベンダーが書いている」事実として確認済）。`第三者のみ`＝公式を開けず、第三者の記載のみ。`未確認`＝確かめられていない。
- 「公式ページに記載なし」は「接続できない」という意味ではない。**記載を見つけられなかっただけ**で、接続可否は「未確認」とした。
- 用語：「OTA」＝予約サイト。「SC」＝サイトコントローラー（チャネルマネージャー）。「PMS」＝宿泊管理システム。

---

## 1. 国内OTAの側：外部ツールが接続する「公式の仕組み」

### 1-1. 楽天トラベル（運営：楽天グループ）

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| 1-1-01 掲載できる施設（楽天トラベル公式・新規参画ページ） | 「「旅館業法」に基づき『旅館業営業許可証』取得の施設様がご参画いただけます。※ただし、ラブホテル、民泊新法（住宅宿泊事業法）の施設様はご参画いただけません。」 | https://travel.rakuten.co.jp/info/hotel_msg.html | 2026-11-05 | 確認済 |
| 1-1-02 民泊新法・特区民泊の案内先（同ページ） | 「住宅宿泊事業法、特区民泊の施設様は同じ楽天グループ運営サイトの『Rakuten Oyado』でご登録を行っております。」 | https://travel.rakuten.co.jp/info/hotel_msg.html | 2026-11-05 | 確認済 |
| 1-1-03 新規参画の流れ（同ページ） | お申込フォーム → 「弊社での審査を経てシステム登録」 → 「貴施設管理画面でプラン作成、在庫、料金登録で掲載販売開始」 | https://travel.rakuten.co.jp/info/hotel_msg.html | 2026-11-05 | 確認済 |
| 1-1-04 外部システム連携の公式サービス名「R-Connect」 | 楽天トラベル公式（楽天トラベルEXPO2014のページ）：「R-Connect　ホテルシステム販売連携サービス　ホテルシステム＆楽天トラベルのシステム連携により、予約データの自動取込、在庫連動が可能に！」（2014年のページ。現行の仕様・申込条件は未確認） | https://travel.rakuten.co.jp/expo/2014/program_tokyo/festa/index.html | 2026-11-05 | 確認済（古いページ） |
| 1-1-05 R-Connect の申請手順 | 第三者（楽天トラベルの店舗運営支援会社）：「手間いらずと連携する前に楽天トラベル管理画面上でR-Connectの申請を行う必要がございます。」「楽天トラベルでは楽天側にR-Connect申請が必須になりますが、じゃらんでは特にじゃらん側で設定、申請するものはありません。」 | https://fivestar-corporation.co.jp/archives/23056 | 2026-11-05 | 第三者のみ |
| 1-1-06 楽天トラベルの公式な「連携ベンダー認定一覧」 | 公式ページでは見つからなかった（検索のみ。楽天トラベルの施設向け管理画面のヘルプはログインが必要とみられ、開けていない） | - | 2026-11-05 | 未確認 |
| 1-1-07 楽天グループのSC | 「ねっぱん！サイトコントローラー＋＋」の運営は「楽天トラベルサービス株式会社」（ねっぱん！公式サイトのフッター表記） | https://www.neppan.com/ | 2026-11-05 | 確認済 |
| 1-1-08 Rakuten Oyado（旧 Vacation STAY）経由で楽天トラベルに出す方法 | Rakuten Oyado（楽天ステイ運営）の施設向けページ：「Rakuten Oyadoに施設を登録、掲載するだけで楽天トラベルにも施設を掲載することができます。」「※楽天トラベルへの施設・在庫の配信は「インスタントブッキング（即時予約確定）」対応施設のみとなります。」「楽天トラベルに民泊施設（住宅宿泊事業法/特区民泊）を配信できるのはRakuten Oyadoだけです。」 | https://vacation-stay.com/host.html | 2026-11-05 | 確認済 |
| 1-1-09 Rakuten Oyado の販売手数料 | 「販売手数料は一律３%」「どの提携サイト（自動掲載先）で販売されても一律３％」（手数料の一部を宿泊者負担にする仕組みとの記載あり） | https://vacation-stay.com/host.html | 2026-11-05 | 確認済 |
| 1-1-10 Rakuten Oyado と併用できる既存SC | 同ページFAQ：「ねっぱん、AirHost、Beds24、suitebookをご利用の場合は連携/連動サイトとしてRakuten Oyadoを追加することでそのままご利用いただけます。」「※ PMSで在庫・料金等の管理をする場合にも、事前にRakuten Oyadoでの施設登録が必要です。」 | https://vacation-stay.com/host.html | 2026-11-05 | 確認済 |
| 1-1-11 名称変更 | 楽天ステイ：「本日より「Vacation STAY」の名称を「Rakuten Oyado」に改称しました」（2024年12月3日付のプレスリリース） | https://corp.stay.rakuten.co.jp/press/20241203_01/ | 2026-11-05 | 確認済 |
| 1-1-12 Rakuten Oyado の個別連携ページ（TEMAIRAZU・TL-リンカーン・ねっぱん・Beds24・AirHost・suitebook） | 検索結果の要約に vacation-stay.jp 配下の個別ページが出たが、ページ本体は 502 エラーで開けなかった（要点は 1-1-10 で公式ページから確認済み） | https://vacation-stay.jp/contents/host/how-to-use-services/ | 2026-11-05 | 未確認 |

### 1-2. じゃらんnet（運営：リクルート）

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| 1-2-01 掲載できる施設（じゃらんnet公式・参画のご案内） | 「「旅館業法」に基づき「宿泊営業許可」を得た施設様がご参画いただけます。」「※また、住宅宿泊事業法に基づく「民泊」、および、国家戦略特区法に基づく「特区民泊」もご参画いただけません。」FAQ「民泊は掲載することができますか？」→「住宅宿泊事業法（民泊新法）や国家戦略特区（特区民泊）に基づく施設様はご掲載いただくことができません。」（ページの更新日は記載なし） | https://www.jalan.net/jalan/doc/howto/10sankaku.html | 2026-11-05 | 確認済 |
| 1-2-02 ご参画の条件（同ページ） | 「ご参画・ご掲載は無料です。送客実績に対してシステム利用料・ポイント付与料等をご負担いただきます。」必要環境に「じゃらんnetからの通知を受け取れる電話とFAXがあること」 | https://www.jalan.net/jalan/doc/howto/10sankaku.html | 2026-11-05 | 確認済 |
| 1-2-03 じゃらんnetの公式な「サイトコントローラー連携の認定ベンダー一覧」 | 公式ページでは見つからなかった | - | 2026-11-05 | 未確認 |
| 1-2-04 リクルート公式の提携ベンダー一覧（価格設定ツール「レベニューアシスタント」用。OTAへの在庫・料金の接続用ではない） | 2021年3月29日時点。提携サイトコントローラーベンダー：株式会社クリップス／株式会社シーナッツ／手間いらず株式会社。提携PMSベンダー：株式会社ウェルコム、株式会社鹿児島システムサービス、キヤノンITソリューションズ株式会社、株式会社クリップサイト、株式会社クリップス、株式会社シダン、信南交通株式会社、新日本コンピュータサービス株式会社、総合システムサービス株式会社、株式会社タップ、ダイナテック株式会社、株式会社電算インフォメーション、デンセイシリウス株式会社、電通工業株式会社、株式会社NASII、株式会社ナバック、株式会社日本メイサー、株式会社ビジコン・ジャパン、株式会社ビジネスブレーン、株式会社富士通九州システムズ、有限会社マックス、株式会社ユーコム。「連携可能なベンダーは今後も増加予定となっております。」 | https://www.recruit.co.jp/newsroom/recruit-lifestyle/uploads/2021/03/RecruitLifestyle_jalan_20210329.pdf | 2026-11-05 | 確認済（5年以上前の資料） |
| 1-2-05 レベニューアシスタントの現行ページ | 「PMSやサイトコントローラー、じゃらんと連携してデータを収集します。」（提携ベンダー名の記載は現行ページに無し） | https://www.ra.jalan.net/ | 2026-11-05 | 確認済 |
| 1-2-06 SC側から見たじゃらん連携 | 手間いらず・ねっぱん！の公式ページが、連携先として「株式会社リクルート」を掲載（2-1・2-2 を参照） | https://www.temairazu.com/partner | 2026-11-05 | 確認済 |

### 1-3. 一休.com（運営：一休）

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| 1-3-01 新規掲載の窓口（一休公式FAQ） | 「一休.comへの新規掲載をご希望の宿泊施設様におかれましては、以下ページをご一読の上、専用フォームからご依頼いただきますようお願いいたします。」（フォーム先の本文は開けていない） | https://faq.ikyu.com/app/answers/detail/a_id/812 | 2026-11-05 | 確認済 |
| 1-3-02 一休.comの公式な外部ツール連携の案内 | 公式ページでは見つからなかった（www.ikyu.com の参画案内ページは 403 で開けず） | - | 2026-11-05 | 未確認 |
| 1-3-03 SC側から見た一休連携 | 手間いらず・ねっぱん！の公式ページが、連携先として「株式会社一休」を掲載 | https://www.neppan.com/collaboration/ | 2026-11-05 | 確認済 |

### 1-4. Booking.com（日本向け）

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| 1-4-01 外部ツール接続の公式入口（Booking.com Connectivity Portal） | 「Connect your channel manager PMS web portal application to Booking.com」「List properties, sync rates and availability, and more.」API：Rates & Availability API／Content & Images API／Promotions API | https://connect.booking.com/ | 2026-11-05 | 確認済 |
| 1-4-02 新規の接続事業者の受付状況（同ページ） | 「we are pausing integrations with new connectivity providers until further notice.」（既存の Connectivity Partner は「You need a portal account.」） | https://connect.booking.com/ | 2026-11-05 | 確認済 |
| 1-4-03 住宅宿泊仲介業者としての登録 | 観光庁の登録簿（令和8年6月22日現在）に「Booking.com B.V.」（ブッキングドットコム、登録番号 観光庁長官（02）第S0044号、登録年月日 令和5年8月27日） | https://www.mlit.go.jp/kankocho/minpaku/business/mediation/content/001964516.pdf | 2026-11-05 | 確認済 |
| 1-4-04 日本の民泊（届出番号）に関する Booking.com 側の規則 | 公式ヘルプでは見つからなかった | - | 2026-11-05 | 未確認 |

### 1-5. Airbnb

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| 1-5-01 外部ソフトの公式パートナー表示（Airbnb Preferred Partners ページ） | 「These are our top performing partners. They provide the requisite functionality and software connections that meet or exceed all our technical and performance benchmarks.」掲載（Preferred+ と表示）：Airhost, Beds24, Channex, Guesty, Hospitable, Host Platform, Hostaway, Hostfully, Kross Booking, Lodgify, OwnerRez, Rentals United, stays.net, Tokeet, Uplisting, Hostify, Octorate, TRACK, SuperHote ほか。iGMS と NextPax は同ページに載るが、取得したテキストでは等級の表示が見えなかった。Sirvoy は同ページで見つからず | https://www.airbnb.com/software-partners/preferred-partners | 2026-11-05 | 確認済 |
| 1-5-02 日本の住宅宿泊事業（民泊新法）のリスティングをソフト連携で作る件 | Airbnb ヘルプ：「In Japan, we don't accept listings created through software connections for places to stay (minpaku) used for Housing Accommodation Business under the Japanese Housing Accommodation Business Act (Act No.65 of 2017). The only exception to the policy is for Japanese API partners who have entered into the license agreement with regard to Airbnb brand and intellectual properties within Japan」 | https://www.airbnb.com/help/article/2351 | 2026-11-05 | 確認済 |
| 1-5-03 上記の例外にあたる「日本のAPIパートナー」の名前 | 公式ページでは見つからなかった | - | 2026-11-05 | 未確認 |
| 1-5-04 届出番号の登録（Airbnb ヘルプ） | 「You must complete the notification of the private lodging business with the respective local government, then must add your notification number to your listing page.」「You need to directly log in to your account and complete the adding process, even if you usually use management tools, etc. provided/operated by a third party.」旅館業法の許可・特区法の認定がある場合は「you can enter those details instead of adding your notification number.」 | https://www.airbnb.com/help/article/2177 | 2026-11-05 | 確認済 |
| 1-5-05 住宅宿泊仲介業者としての登録 | 観光庁の登録簿に「Airbnb Global Services Limited」（登録番号 観光庁長官（02）第S0001号、登録年月日 令和5年5月24日） | https://www.mlit.go.jp/kankocho/minpaku/business/mediation/content/001964516.pdf | 2026-11-05 | 確認済 |

### 1-6. 参考：観光庁の仲介業者の登録簿に載っている主なOTA（令和8年6月22日現在、登録数66）

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| 1-6-01 住宅宿泊仲介業者の登録簿（抜粋） | Airbnb Global Services Limited（S0001）／Booking.com B.V.（S0044）／EXPEDIA,INC.（S0106、令和4年10月13日登録）／AGODA TRAVEL SERVICES PTE. LTD.（S0118）／HomeAway.com, Inc.（令和8年1月21日登録）／上海携程商務有限公司（Ctrip）／携程旅行網（香港）有限公司（Trip）ほか | https://www.mlit.go.jp/kankocho/minpaku/business/mediation/content/001964516.pdf | 2026-11-05 | 確認済 |
| 1-6-02 同登録簿に載っていないもの | 登録簿の本文に「楽天」「リクルート」「一休」の文字は無し（第12条により、仲介の委託先は「住宅宿泊仲介業者又は旅行業者」であり、旅行業者は別リスト） | 同上 | 2026-11-05 | 確認済 |
| 1-6-03 民泊を取り扱う旅行業者のリスト（令和7年3月末時点、報告のあった旅行業者のみ） | 10社：（一社）田辺市熊野ツーリズムビューロー／（一社）みなかみ町体験旅行／楽天ステイ（株）／（株）ジャルパック／（株）SOZONEXT／株式会社日本コスパ／日中交流ビジネス合同会社／NPO遠野山・里・暮らしネットワーク／（株）天満屋トラベル／（株）雨風太陽。※「本リストに名前のない旅行業者においても、民泊物件を取り扱うことは可能です。」 | https://www.mlit.go.jp/kankocho/minpaku/business/mediation/list.html | 2026-11-05 | 確認済 |

---

## 2. 国内の予約サイトに接続できる「ツール側の公式ページ」（国内SC・PMS）

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| 2-1 手間いらず（TEMAIRAZU）：パートナー一覧 | 公式の「パートナー一覧」の「国内宿泊予約サイト」に「楽天グループ株式会社」「株式会社リクルート」「株式会社JTB」「株式会社ベストリザーブ」「株式会社一休」ほかを掲載（楽天グループは「国内宿泊予約サイト」と「国内ブッキングエンジン」の両方に掲載。リクルートも同様）。「海外宿泊予約サイト」に Agoda／Booking.com B.V.／Expedia,Inc.／Airbnb, Inc. ほか。「国内ホテルシステム（PMS）」に株式会社エアホスト、RoomBoss Co.,Ltd. ほか。「海外ホテルシステム（PMS）」は Oracle OPERA Cloud／Shiji／Infor／MEWS／RMS Australia ほか（本カードの9つの海外PMSは載っていない） | https://www.temairazu.com/partner | 2026-11-05 | 確認済 |
| 2-2 ねっぱん！サイトコントローラー＋＋：連携サイト一覧 | 「国内サイト」に「楽天グループ株式会社様」「株式会社リクルート様」「株式会社JTB様」「株式会社一休様」「楽天ステイ株式会社様」ほか。「海外サイト」に Agoda／Expedia／Booking.com B.V.／Airbnb,Inc. ほか。連携PMS一覧に「合同会社エアホスト様」 | https://www.neppan.com/collaboration/ | 2026-11-05 | 確認済 |
| 2-3 AirHost：楽天トラベル連携の仕様（AirHost公式ヘルプ） | 「Starting June 30, 2025, the login method for the Rakuten Travel management screen will change…unified with "Rakuten for Business (hereinafter referred to as "RFB")."」チャネル追加には「RFB Username」「RFB Password」「Facility ID」を入力。「Rakuten Travel does not support setting a separate cleaning fee.」「Currently, AirHost supports rate and inventory synchronization only with the old Rakuten Travel management page.」「For package reservations, Rakuten Travel does not allow direct communication.」 | https://support.airhost.co/en/articles/8659935-channel-creating-and-synchronizing-rakuten-travel-channel | 2026-11-05 | 確認済 |
| 2-4 AirHost：じゃらん連携 | AirHost公式サイト：「API連携により、客室在庫・料金・空室状況がAirHostからじゃらんnetにリアルタイムで自動的に同期され」「じゃらんnetサイトからのゲストメッセージもエアホストで受信して返信することもできます。」／AirHost公式ヘルプにじゃらん用のチャネル作成・同期仕様ページあり | https://airhost.jp/integration/jalan-net | 2026-11-05 | 確認済 |
| 2-5 AirHost のAirbnb上の表示 | Airbnb Preferred Partners ページに「Airhost, Preferred+」（1-5-01） | https://www.airbnb.com/software-partners/preferred-partners | 2026-11-05 | 確認済 |
| 2-6 手間いらず公式サイトのお知らせ欄 | 手間いらず公式サイトのパートナー一覧ページ上部に「当社システムへの不正アクセスに関する経過および対応について（第二報）」の見出しが表示されている。リンク先の本文は開けておらず、内容・日付は未確認 | https://www.temairazu.com/partner | 2026-11-05 | 確認済（見出しの存在のみ） |

---

## 3. 海外PMS 9社：楽天トラベル・じゃらんへの接続（国内OTAの認定ベンダー一覧と、各社の連携一覧ページで確認）

- 国内OTA側（楽天トラベル・じゃらん・一休）の公式な認定ベンダー一覧は、見つからなかった（1-1-06、1-2-03、1-3-02）。そのため、確認できたのは「各社が自社ページに書いていること」と、「国内SC・OTA（Rakuten Oyado）の公式ページに載っている社名」だけ。

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| 3-01 Guesty：楽天トラベル／じゃらん | 公式のチャネルマネージャーのページに、Airbnb／Booking.com／Vrbo／Expedia／Agoda／Google の記載はあるが、楽天トラベル・じゃらんの記載は見つけられなかった。接続可否は不明 | https://www.guesty.com/features/channel-manager/ | 2026-11-05 | 未確認 |
| 3-02 Hostaway：楽天トラベル／じゃらん | 公式のチャネルマネージャーのページに、Airbnb／Booking.com／Expedia／Vrbo の記載はあるが、楽天トラベル・じゃらんの記載は見つけられなかった。接続可否は不明 | https://www.hostaway.com/features/channel-manager/ | 2026-11-05 | 未確認 |
| 3-03 Lodgify：楽天トラベル／じゃらん | 公式の channel-manager ページと integrations ページは、この環境からは 403 エラーで開けなかった（検索の要約では「Lodgify connects via API to Airbnb, Vrbo and Booking.com」とあるが、本文は開けていない）。楽天トラベル・じゃらんの記載は確認できず、接続可否は不明 | https://www.lodgify.com/channel-manager/ | 2026-11-05 | 未確認 |
| 3-04 OwnerRez：楽天トラベル／じゃらん | 公式の channel management ページと API channel integration の説明ページに、楽天トラベル・じゃらんの記載は見つけられなかった（Airbnb／Booking.com／Vrbo／Expedia の記載あり）。接続可否は不明 | https://www.ownerrez.com/channel-management | 2026-11-05 | 未確認 |
| 3-05 Hospitable：楽天トラベル／じゃらん | 公式の integrations ページに、楽天トラベル・じゃらんの記載は見つけられなかった。接続可否は不明 | https://hospitable.com/integrations | 2026-11-05 | 未確認 |
| 3-06 iGMS：楽天トラベル／じゃらん | 公式の channel manager ページに、楽天トラベル・じゃらんの記載は見つけられなかった（Airbnb／Booking.com／Vrbo／Expedia／Tripadvisor の記載あり）。接続可否は不明 | https://www.igms.com/channel-manager/ | 2026-11-05 | 未確認 |
| 3-07 Uplisting：楽天トラベル／じゃらん | 公式の integrations ページと channel-manager ページに、楽天トラベル・じゃらんの記載は見つけられなかった。接続可否は不明 | https://www.uplisting.io/integrations | 2026-11-05 | 未確認 |
| 3-08 Beds24：楽天トラベル | Beds24 公式Wiki：「The connection between Beds24 and Rakuten Tavel is made via Vacation STAY.」「Vacation STAY and Rakuten Travel are connected via an API integration.」「The property creation on Rakuten Travel is semi-automated, so it might take up to a few weeks for the property to show up on Rakuten travel.」できること：「Beds24 can export Inventory／export Price／import Bookings／import Cancellations」。制限：Extra Person・Minimum Stay・Maximum Stay の料金／ルールは送れない。「Vacation STAY does not support modification.」 | https://wiki.beds24.com/index.php/Rakuten | 2026-11-05 | 確認済 |
| 3-09 Beds24：楽天トラベル（楽天側の記載） | 楽天LIFULL STAY（当時）のプレスリリース（2019-05-31）：「Vacation STAY」と「Beds24」のシステム連携開始。「Vacation STAY」ならびに同サイトと連携している「楽天トラベル」をはじめとする宿泊予約サイトへ「将来的に物件を掲載できる」。Rakuten Oyado の現行ページにも Beds24 の記載あり（1-1-10） | https://corp.stay.rakuten.co.jp/press/20190531_01/ | 2026-11-05 | 確認済 |
| 3-10 Beds24：じゃらん | Beds24 の日本の販売サイト（株式会社WeIns）の「Beds24対応OTA」に「楽天バケーションステイ（Vacation STAY）」「楽天トラベル」「じゃらん」「一休.com」「Yahoo!トラベル」「STAYJAPAN」を掲載。同サイトの料金例に「Airbnb、Booking.com、Expedia、じゃらん、楽天トラベル」。**Beds24 公式Wiki（英語）のチャネル一覧には Jalan が見当たらなかった** | https://co-reception.com/beds24%e5%af%be%e5%bf%9cota/ | 2026-11-05 | 確認済（販売会社サイトの記載。Beds24本社Wikiでは確認できず） |
| 3-11 Beds24：じゃらんの制限（販売会社のnote・2021年） | 「Beds24は、じゃらんと在庫の連携が可能です。ただし、料金はじゃらん管理画面で設定する必要があります。」「Beds24とじゃらんの同期は在庫のみ。」「じゃらんでアカウントを開設できるのは旅館業の宿のみ。」「現状、上記民泊の受け入れ予定はなし（じゃらん営業担当者談）。※2020年9月25日時点の情報です。」（古い情報。現行の連携範囲は未確認） | https://note.com/beds24japan/n/n7114273b8a5c | 2026-11-05 | 第三者のみ（販売会社の2021年記事） |
| 3-12 Sirvoy：楽天トラベル／じゃらん | 公式の booking channel partners ページに、Booking.com／Expedia／Hotels.com／Agoda／Hostelworld／Airbnb／Vrbo の記載と、「SiteMinder　A third-party tool that connects you to many other booking sites through a single platform.」の記載があるが、楽天トラベル・じゃらんの記載は見つけられなかった。接続可否は不明 | https://help.sirvoy.com/setting-up-new-channels/all-of-sirvoy%E2%80%99s-booking-channel-partners | 2026-11-05 | 未確認 |
| 3-13 9社のうち、国内SC・Rakuten Oyado の公式ページに社名が載っている会社 | Rakuten Oyado の「そのまま使える」リストに載るのは「ねっぱん、AirHost、Beds24、suitebook」（1-1-10）。手間いらず／ねっぱん！の連携PMS欄に、9社の名前は載っていない（2-1、2-2） | https://vacation-stay.com/host.html | 2026-11-05 | 確認済 |
| 3-14 参考（9社以外）：Zeevou／Rentals United の楽天トラベル連携 | Zeevou：「Rakuten Travel」のチャネルページあり（iCal同期による接続の説明と報じられている。ページ本文は詳しく読んでいない）。Rentals United：Vacation Stay の連携の説明ページがある（開けず）。比較対象外のため要点のみ | https://zeevou.com/channels/rakuten-travel/ | 2026-11-05 | 第三者のみ |

---

## 4. 国内の民泊向け管理ツール（比較の参考。名前と公式URLのみ）

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| 4-01 ねっぱん！サイトコントローラー＋＋（楽天トラベルサービス株式会社） | 名前・公式URL | https://www.neppan.com/ | 2026-11-05 | 確認済 |
| 4-02 手間いらず／TEMAIRAZU（手間いらず株式会社） | 名前・公式URL | https://www.temairazu.com/ | 2026-11-05 | 確認済 |
| 4-03 TL-リンカーン（株式会社シーナッツ） | 名前・公式URL（TL-リンカーンのログイン画面は https://www.tl-lincoln.net/ ） | https://www.seanuts.co.jp/ | 2026-11-05 | 確認済 |
| 4-04 AirHost（エアホスト） | 名前・公式URL。AirHost の英語ヘルプのドメインは support.airhost.co（運営表記 Airhost Pte Ltd） | https://airhost.jp/ | 2026-11-05 | 確認済 |
| 4-05 suitebook（株式会社SQUEEZE） | 名前・公式URL。suitebook.io にアクセスすると squeeze-inc.co.jp/services/ に転送される。現行の提供状況は未確認 | https://squeeze-inc.co.jp/ | 2026-11-05 | 確認済（転送先のみ） |
| 4-06 RoomBoss | 名前・公式URL（手間いらずのパートナー一覧「国内ホテルシステム（PMS）」にも社名あり） | https://www.roomboss.com/ | 2026-11-05 | 確認済 |
| 4-07 Beds24（日本の販売サイト：株式会社WeIns） | 名前・公式URL（日本の販売サイト）。Beds24 本体は https://beds24.com/ | https://co-reception.com/ | 2026-11-05 | 確認済 |

---

## 調べられなかったこと

1. **楽天トラベル・じゃらんnet・一休.com の「公式な認定ベンダー一覧」**：どれも公式ページでは見つけられなかった（施設向けの管理画面・ヘルプはログインが必要とみられる）。楽天トラベルの R-Connect の現行仕様・申込条件・手数料も未確認（2014年の公式ページと第三者の記事のみ）。
2. **じゃらんの現行の接続方法**：リクルート公式の接続仕様書は見つからなかった。AirHost と販売会社（Beds24の日本の販売サイト）のページは「在庫（と料金）の連携」を書いているが、じゃらん公式側での確認は取れていない。
3. **海外PMS 9社が楽天トラベル・じゃらんに接続できるか**：Beds24（楽天トラベル＝Vacation STAY／Rakuten Oyado 経由で公式Wikiに記載。じゃらん＝販売会社サイトに記載、本社Wikiには無し）以外の8社（Guesty、Hostaway、Lodgify、OwnerRez、Hospitable、iGMS、Uplisting、Sirvoy）は、公式ページに記載が見つからないため「未確認」。「接続できない」と確認したわけではない。Lodgify は公式ヘルプが開けなかった。
4. **Rakuten Oyado の個別連携ページ**（vacation-stay.jp）は 502 エラーで開けず、検索結果の要約のみ。
5. **Booking.com の日本の民泊に関する規則**（届出番号の必須化など）、**Airbnb の「日本のAPIパートナー」の名前**。
6. **一休.com の掲載条件・審査・ツール連携**（公式の参画ページは 403 で開けず、専用フォームの先も未確認）。
7. **Expedia／Vrbo／Agoda／Trip.com** の日本向けの接続の仕組み（本カードでは登録簿への掲載のみ確認）。
8. **各ツールの料金・機能・評価**（本カードの対象外）。国内ツール（4章）は名前と公式URLのみで、機能は調べていない。
9. 手間いらず公式サイトの「不正アクセス」お知らせ（2-6）の本文・日付。
10. 国内の民泊向け管理ツールの網羅性：4章は今回確認できたものだけで、網羅ではない。
