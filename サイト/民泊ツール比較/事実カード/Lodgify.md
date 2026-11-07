# 事実カード：Lodgify

- 取得日：2026-11-05（すべての行）
- 調査の前提（重要）：
  - `www.lodgify.com`（料金・連携・規約・アフィリエイトの本体ページ）と `help.lodgify.com`（ヘルプセンター）は、curl では Cloudflare の確認画面（HTTP 403）で開けなかった。WebFetch は `www.lodgify.com` の名前解決自体ができなかった。
  - 代わりに、Lodgify 自身のサブドメイン `webflow-mkt.lodgify.com`（マーケティングサイトの同内容の公開コピー。ページ内の canonical や構造化データは `www.lodgify.com/...` を指す）と、`use.lodgify.com`（アフィリエイト規約）は開けた。下の出典URLは「実際に開いたURL」を書いた。`www` 側の同名ページと内容が同一かは未照合。
  - `www.lodgify.com/sitemap.xml` と `robots.txt` は開けた（サイトマップの言語切替に日本語がないことの確認に使用）。
  - 料金の「物件数スライダー」はJavaScriptで計算されるため、1物件の表示価格以外は取れなかった。
- 確度の凡例：`確認済`＝公式ページを開いて確認／`第三者のみ`＝公式を開けず第三者情報のみ／`未確認`

## 1. 基本

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| 運営会社（利用規約上の契約主体） | Codebay Solutions Limited（英国イングランド・ウェールズ法人、会社番号 5903966、"trading as Lodgify"）。規約の準拠法は英国法、管轄は英国裁判所 | https://webflow-mkt.lodgify.com/terms | 2026-11-05 | 確認済 |
| ソフトウェア開発の一部 | 規約に「Part of the Services shall be provided through software developed by the entity Rental Ninja S.L.」の記載（規約内の別サービス=VPSの責任先として） | https://webflow-mkt.lodgify.com/terms | 2026-11-05 | 確認済 |
| 利用規約の最終更新表示 | 「Last Updated 02/16/2026」 | https://webflow-mkt.lodgify.com/terms | 2026-11-05 | 確認済 |
| 対象規模 | 「whether you have one property or 30+」（FAQ）。Basicは1物件以下、Starterは2物件以下の制限あり（下の料金表） | https://webflow-mkt.lodgify.com/pricing | 2026-11-05 | 確認済 |
| ブランド表示の変更 | サイト上に「Lodgify has rebranded / Discover what's new」の表示あり（内容は未確認） | https://webflow-mkt.lodgify.com/pricing | 2026-11-05 | 確認済（表示の存在のみ） |

## 2. 料金

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| 課金モデル | 月額サブスク（プラン別）。「Pricing varies based on the number of properties you manage and the features included.」構造化データでは単位が「per property per month」。予約手数料なし（「Lodgify has no booking fee on any plan」） | https://webflow-mkt.lodgify.com/pricing | 2026-11-05 | 確認済 |
| プラン一覧 | Basic／Starter／Professional／Ultimate の4プラン。無料プランの記載なし（無料トライアルのみ） | https://webflow-mkt.lodgify.com/pricing | 2026-11-05 | 確認済 |
| 表示通貨 | 価格表示の切替は EUR／USD／GBP の3つのみ。JPY表示はページ上に見当たらない | https://webflow-mkt.lodgify.com/pricing | 2026-11-05 | 確認済 |
| 1物件・USDの表示価格（ページ初期表示） | Basic $14／Starter $26／Professional $47／Ultimate $68（各 /month）。画面には「Save 20%」の表示あり。ページ内の月額・年額・2年払いの切替は「Yearly -20%」「Bi-Yearly -25%」。初期表示がどの支払い周期かはページ上で明示されておらず、下の構造化データ（2年払い価格）との比率から年払いと推定（推定） | https://webflow-mkt.lodgify.com/pricing | 2026-11-05 | 確認済（数値）／周期は推定 |
| 1物件・2年払い（Bi-Yearly）の最低価格（構造化データ） | USD：Basic 13／Starter 24／Professional 44／Ultimate 64。EUR：12／21／36／53。GBP：10／19／32／49。説明文「Price shown is the starting price for 1 property, billed bi-yearly. Price scales with number of properties and varies by billing cycle, see pricing page for an exact quote.」 | https://webflow-mkt.lodgify.com/pricing （ページ内 JSON-LD） | 2026-11-05 | 確認済 |
| プランの物件数制限 | Basic：「This plan is only available for 1 property or less」／Starter：「This plan is only available for 2 properties or less」。3室以上はProfessional以上が前提（ページ記載から読み取れる範囲） | https://webflow-mkt.lodgify.com/pricing | 2026-11-05 | 確認済 |
| 物件数別の目安：1室 | 上記の1物件価格（Basic〜Ultimate） | https://webflow-mkt.lodgify.com/pricing | 2026-11-05 | 確認済 |
| 物件数別の目安：3室／5室／10室／20室 | スライダー（1〜100）の計算がJavaScriptで、静的HTMLに価格表なし。取得できなかった | https://webflow-mkt.lodgify.com/pricing | 2026-11-05 | 未確認 |
| 無料トライアル | 「Try Lodgify for free for 7 days. No credit card required.」 | https://webflow-mkt.lodgify.com/pricing | 2026-11-05 | 確認済 |
| 契約縛り | 「There's no long-term contract. You can cancel your subscription at any time. If you're on an annual plan, you'll retain access until the end of your billing period.」 | https://webflow-mkt.lodgify.com/pricing | 2026-11-05 | 確認済 |
| 契約期間・自動更新（規約） | 1か月／12か月／24か月の期間を選択、前払い。「will automatically renew ... until and unless explicitly canceled」。更新前の通知は送られない（「we will not send it a notice before the Initial Term or Subsequent Term is renewed」） | https://webflow-mkt.lodgify.com/terms （7. Fees, Payments and Refunds） | 2026-11-05 | 確認済 |
| 解約手続き（規約） | アカウント画面からの解約は契約期間終了の1日前まで、メール（問い合わせフォーム）経由は5日前まで | https://webflow-mkt.lodgify.com/terms | 2026-11-05 | 確認済 |
| 返金（規約） | 「Services canceled at the Customer's request prior to the completion of the Contract Term are not subject to a refund.」。消費者には14日間のクーリングオフ（年払い・2年払いは更新時にも適用、月払いは初回のみ）。事業者として契約する場合の扱いは規約上「Consumer」の定義に依存（定義は未確認） | https://webflow-mkt.lodgify.com/terms | 2026-11-05 | 確認済（クーリングオフの適用条件は一部未確認） |
| 決済手数料 | 「A transaction fee of 1% applies to payments your guests make online through a payment gateway such as Stripe or PayPal.」ゲートウェイ側の手数料は別。手動入金（現金・銀行振込）は手数料なし | https://webflow-mkt.lodgify.com/pricing | 2026-11-05 | 確認済 |
| ダイレクト予約手数料 | 「Lodgify does not take a cut of your bookings.」（予約手数料0%。上の1%は決済ゲートウェイ経由の支払い手数料） | https://webflow-mkt.lodgify.com/pricing | 2026-11-05 | 確認済 |
| 税・為替 | 価格は税別（「All prices are exclusive of such taxes」）。支払い額は支払い時点の為替レートの影響を受ける | https://webflow-mkt.lodgify.com/pricing | 2026-11-05 | 確認済 |
| 支払い方法（利用者→Lodgify） | Visa、Mastercard、Apple Pay、Google Pay、American Express。規約上、契約更新の支払いはクレジットカードまたはPayPal | https://webflow-mkt.lodgify.com/pricing ／ https://webflow-mkt.lodgify.com/terms | 2026-11-05 | 確認済 |
| 初期費用 | 「there's no setup fee when joining Lodgify. Free onboarding is included.」 | https://webflow-mkt.lodgify.com/pricing | 2026-11-05 | 確認済 |
| Dynamic Pricing（価格最適化）の料金 | Professional・Ultimateに追加費用なしで含まれる。Basic・Starterは3か月無料トライアルで、その後の料金はページに記載なし | https://webflow-mkt.lodgify.com/dynamic-pricing | 2026-11-05 | 確認済（トライアル後の料金は未確認） |
| Lodgify Smart Locks の料金 | 「$7 USD (£6 / €6) per connected smart lock device」月額前払い | https://webflow-mkt.lodgify.com/smart-locks | 2026-11-05 | 確認済 |
| Lodgify Payments の手数料（米国のみ） | 米国：国内 2.90% + $0.30／国際 4.40% + $0.30／外貨 1%／紛争 $15。「Currently available to U.S.-based hosts.」 | https://webflow-mkt.lodgify.com/lodgify-payments | 2026-11-05 | 確認済 |
| 料金改定の条項（規約） | 30日前の通知で料金変更可。「Fees described ... may not reflect the Fees payable by existing Customers on legacy plans.」また、地域・通貨・施策により顧客ごとに価格が異なる実験（Experiments）を行う旨の条項あり | https://webflow-mkt.lodgify.com/terms | 2026-11-05 | 確認済 |

## 3. チャネル（予約サイト連携）

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| 接続方式（公式APIか） | 「We connect via API to Airbnb, Vrbo, Booking.com and Expedia.」その他は iCal（「You can even use iCal to connect to niche or regional booking sites.」） | https://webflow-mkt.lodgify.com/vacation-rental-channel-manager | 2026-11-05 | 確認済 |
| Airbnb | API連携（Basicから） | https://webflow-mkt.lodgify.com/pricing | 2026-11-05 | 確認済 |
| Booking.com | API連携（Basicから） | https://webflow-mkt.lodgify.com/pricing | 2026-11-05 | 確認済 |
| Vrbo | API連携（Basicから） | https://webflow-mkt.lodgify.com/pricing | 2026-11-05 | 確認済 |
| Expedia | チャネルマネージャーページのFAQに「API」で接続と記載。料金ページの機能表（"API for Airbnb, Vrbo and Booking.com"）にはExpediaの記載なし。両ページで記述が異なる | https://webflow-mkt.lodgify.com/vacation-rental-channel-manager ／ https://webflow-mkt.lodgify.com/pricing | 2026-11-05 | 確認済（記述の食い違いあり） |
| Agoda | 連携一覧（Channelsカテゴリ）に掲載なし。iCal経由の可否は個別確認が必要 | https://webflow-mkt.lodgify.com/integrations | 2026-11-05 | 未確認 |
| 楽天トラベル | 連携一覧・チャネルページに記載なし | https://webflow-mkt.lodgify.com/integrations | 2026-11-05 | 未確認（公式の連携としては記載なし） |
| じゃらん | 連携一覧・チャネルページに記載なし | https://webflow-mkt.lodgify.com/integrations | 2026-11-05 | 未確認（公式の連携としては記載なし） |
| Google Vacation Rentals | Professional・Ultimateで対応（「Listing your website on Google Vacation Rentals」）。Basic・Starterは対象外 | https://webflow-mkt.lodgify.com/pricing | 2026-11-05 | 確認済 |
| その他のチャネル（連携一覧のChannels） | Glamping Hub、VRPlatform、Savvy、Lake.com、Whimstay、Houfy、iCal Sync ほか（「Directo」はChannelsとBusiness Toolsの両方に表示） | https://webflow-mkt.lodgify.com/integrations | 2026-11-05 | 確認済 |
| iCal | 全プランで対応（「Sync with other sites like Tripadvisor or Trivago via iCal.」） | https://webflow-mkt.lodgify.com/pricing | 2026-11-05 | 確認済 |

## 4. 機能

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| 自動メッセージ | 全プラン：予約確認・リマインドの自動送信。Professional以上：カスタムのメッセージ自動化とワークフロー。SMSはUltimateのみ | https://webflow-mkt.lodgify.com/pricing | 2026-11-05 | 確認済 |
| 統合受信箱・AI | 統合受信箱、クイック返信、AI文章アシスタントは全プラン | https://webflow-mkt.lodgify.com/pricing | 2026-11-05 | 確認済 |
| カレンダー同期・二重予約防止 | 「Real-time calendar sync」「Instant updates across all channels mean fewer errors, fewer cancellations and no double bookings.」（公式の主張。実際の精度は未検証） | https://webflow-mkt.lodgify.com/vacation-rental-channel-manager | 2026-11-05 | 確認済（記載の確認のみ） |
| 清掃タスク | Ultimateのみ（「Cleaning and task management」「Task management」）。Turnoの無料サブスクがUltimateに付属との記載 | https://webflow-mkt.lodgify.com/pricing | 2026-11-05 | 確認済 |
| スマートロック連携先 | 自社「Lodgify Smart Locks」（予約ごとのコード自動発行、月$7/台）。連携一覧のKeyless Access：Igloohome、Nuki、Schlage、Tedee、August、Kwikset、Yale、Wyze、Jervis Systems、Charge Automation、Homeit、Chekin、Duve、Lynx、Vikey ほか。Akerun・SESAME・日本向けロックの記載は一覧にない | https://webflow-mkt.lodgify.com/integrations ／ https://webflow-mkt.lodgify.com/smart-locks | 2026-11-05 | 確認済（日本のロックは記載なし＝動作は未確認） |
| 価格ツール連携 | PriceLabs、Beyond、Smartness、TechTape ほか（連携一覧のDynamic Pricing）。自社のDynamic Pricing（Professional以上に含む） | https://webflow-mkt.lodgify.com/integrations ／ https://webflow-mkt.lodgify.com/pricing | 2026-11-05 | 確認済 |
| オーナーポータル／オーナー向け精算 | Ultimateのみ（「Owner payments and reporting」「Owner payments, reports and statements」）。オーナーが閲覧する専用ポータルかどうかはページに記載なし | https://webflow-mkt.lodgify.com/pricing | 2026-11-05 | 確認済（ポータルの有無は未確認） |
| ダイレクト予約サイト | Starter以上：ノーコードのサイト作成、予約エンジン、予約ウィジェット（既存サイトへの埋め込み）、テンプレート、年払いは独自ドメイン無料。サイトの表示言語は「32」と表の数値に記載（言語一覧は未確認） | https://webflow-mkt.lodgify.com/pricing | 2026-11-05 | 確認済（言語の内訳は未確認） |
| 会計 | Ultimate：ゲスト向け請求書、分析、オーナー精算。会計ソフト（freee等）との連携は連携一覧に記載なし（Clearing、Beyond Booking、Key Data などはBusiness Tools） | https://webflow-mkt.lodgify.com/pricing ／ https://webflow-mkt.lodgify.com/integrations | 2026-11-05 | 確認済 |
| ホスト向けアプリ／ゲスト向けアプリ | ホスト向けアプリ：Starter以上。ゲスト向けアプリ：Ultimateのみ | https://webflow-mkt.lodgify.com/pricing | 2026-11-05 | 確認済 |
| チェックイン関連 | Ultimate：Automated check-in tools（ゲスト情報の収集）。Guest Registration（宿泊者登録）機能の説明ページあり（下の日本対応を参照） | https://webflow-mkt.lodgify.com/pricing ／ https://webflow-mkt.lodgify.com/guest-registration | 2026-11-05 | 確認済 |
| 損害保証 | Professional以上：Damage protection pre-authorisation（デポジット与信）。別途「Damage Protection by Safely」の連携あり | https://webflow-mkt.lodgify.com/pricing | 2026-11-05 | 確認済 |

## 5. 日本対応

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| 管理画面（UI）の日本語 | 公式サイトの言語切替は English／Español／Français／Português／Italiano／Deutsch／Ελληνικά の7言語で、日本語なし。サイトマップのhreflangも es, fr, pt, it, de, el, en のみ。サインアップ画面の対応言語コードも en, de, es, it, fr, pt。管理画面そのもの（app.lodgify.com）の言語一覧は未取得 | https://www.lodgify.com/sitemap.xml ／ https://webflow-mkt.lodgify.com/pricing | 2026-11-05 | 確認済（サイトとサインアップ画面）／管理画面は未確認 |
| ゲスト向けメッセージ・予約サイトの日本語 | 予約サイトの表示言語は「32」言語（Starter以上）。日本語が含まれるかは公式ページで確認できず。検索結果では、公式ブログの古い記事（日付不明）が「Japanese」を対応言語に追加したと記載、とされたが、ページ自体は開けず（403） | https://webflow-mkt.lodgify.com/pricing ／ 検索結果上の https://www.lodgify.com/blog/?p=180 | 2026-11-05 | 未確認 |
| サポート言語・対応時間 | 公式の問い合わせページ：「Our support team is available 24/7」。営業（Sales）電話は「open 24/7」（米・英・豪・伊・西・仏の番号。日本の番号なし）。一方、料金ページではプラン別：メールは全プラン、電話はProfessional以上、ライブチャットはUltimateのみ。乗り換えページは「24/7 multilingual support ... via phone, email or chat」と記載。サポート言語の一覧は公式に見当たらず（日本語対応は確認できない） | https://webflow-mkt.lodgify.com/contact ／ https://webflow-mkt.lodgify.com/pricing ／ https://webflow-mkt.lodgify.com/switching-software | 2026-11-05 | 確認済（記載の食い違いあり）／日本語サポートは未確認 |
| 通貨（JPY） | 料金表示はEUR/USD/GBPのみ。予約サイトでJPYで価格設定・決済できるかは公式ページで確認できず。ヘルプ記事「Activate Payyo」（ゲストが自国通貨で支払う機能、サポートへの依頼制）が検索結果に出たが未開封 | https://webflow-mkt.lodgify.com/pricing | 2026-11-05 | 未確認 |
| 決済手段（予約サイト） | Stripe・PayPalなどの決済ゲートウェイ（手数料1%）。Lodgify Paymentsは米国のホスト限定。日本のStripeアカウントで使えるかは未確認 | https://webflow-mkt.lodgify.com/pricing ／ https://webflow-mkt.lodgify.com/lodgify-payments | 2026-11-05 | 確認済（日本での利用可否は未確認） |
| 請求書・インボイス（適格請求書） | Ultimateに「Guest invoices」。日本のインボイス制度（登録番号の記載など）への対応は記載なし。Lodgify自身の請求書の日本向け扱いも未確認 | https://webflow-mkt.lodgify.com/pricing | 2026-11-05 | 未確認 |
| 宿泊者名簿・パスポート確認 | 「Guest Registration」：予約確定時にゲストへ登録フォームを自動送信、データ保管、「Where supported, Lodgify submits guest reporting data to the relevant authorities」。対応地域の一覧はページになく、日本が対象かは不明。パスポート画像の確認機能は記載なし。連携一覧に本人確認系（Chekin、Authenticate、Check-in Scan、Happy Guest、Truviなど）あり | https://webflow-mkt.lodgify.com/guest-registration ／ https://webflow-mkt.lodgify.com/integrations | 2026-11-05 | 確認済（日本の対応は未確認） |
| 住宅宿泊事業法に関する機能（届出番号の表示など） | 公式ページに記載なし | — | 2026-11-05 | 未確認 |
| 日本向け情報の有無 | 公式サイトに日本語ページなし（言語切替・サイトマップにjaなし）。サイトマップ内に rakuten・jalan・japan を含むURLなし | https://www.lodgify.com/sitemap.xml | 2026-11-05 | 確認済 |

## 6. アフィリエイト

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| 有無・種別 | あり。自社プログラム（運営はCodebay Solutions Limited）。追跡・ダッシュボードは LeadDyno（規約に「affiliate dashboard by LeadDyno」、申込ページのリンク先が lodgify.leaddyno.com）。PartnerStackやImpactではない | https://use.lodgify.com/lodgify-affiliate-program-terms-conditions ／ https://webflow-mkt.lodgify.com/affiliates | 2026-11-05 | 確認済 |
| 申込URL | https://www.lodgify.com/affiliates （申込ボタンのリンク先：https://lodgify.leaddyno.com/ ）。申込時に氏名・メール・PayPalメール・事業名・サイトURL/SNS・職業・宣伝方法を提出。30日以内に通知がなければ不承認扱い | https://webflow-mkt.lodgify.com/affiliates ／ 規約 §1 | 2026-11-05 | 確認済 |
| 報酬率 | Friend 20%（開始時）／Advocate 25%／Ambassador 30%。いずれも紹介先の支払いに対し、最初の支払いから最大1年（12か月）。ティア昇格の条件は規約では「過去18か月の累計売上（税抜）が3,000で25%、10,000で30%」（通貨ごと）。申込ページの表は「5 or fewer／More than 5／More than 10」（紹介数）と記載し、規約と食い違う。ページ上部に「Earn up to $2,000 per referral」の表示あり（根拠の内訳は未確認） | https://use.lodgify.com/lodgify-affiliate-program-terms-conditions （§2.2）／ https://webflow-mkt.lodgify.com/affiliates | 2026-11-05 | 確認済（ティア条件は2ページで不一致） |
| 報酬の発生条件 | 新規顧客のみ。有料契約を30日連続で維持。アップグレード・アドオン・12か月後の更新・解約や返金分は対象外。純額（税・返金控除後）に対して計算 | 規約 §2.1・§2.2 | 2026-11-05 | 確認済 |
| 支払い | PayPal。月次サイクル（紹介の翌月に確定、さらに翌月に支払い）。最低支払額なし。年間累計が1,000（通貨ごと）以上は請求書の提出が必要。支払い通貨はEUR・GBP・USD（Lodgifyが決定）。JPYでの支払いは記載なし | 規約 §2.3 ／ https://webflow-mkt.lodgify.com/affiliates | 2026-11-05 | 確認済 |
| クッキー期間 | 規約・申込ページに記載なし | — | 2026-11-05 | 未確認 |
| ブランド名の入札禁止 | あり。有料広告は可（Google/Bing/Meta/TikTok等）だが、「You may not bid on or use the keyword "Lodgify" alone」「You may not use "Lodgify" in combination with other words (e.g., "Lodgify PMS")」、スペルミス等の紛らわしい語も不可、公式提携・推奨を示唆する広告も不可 | https://use.lodgify.com/lodgify-affiliate-program-terms-conditions （§4.1） | 2026-11-05 | 確認済 |
| コンテンツ・表示の制限 | 広告関係の開示が必須（規約§8、FTCの開示ルールを引用、「clear and conspicuous」に）。商標は提供画像のみ・改変不可、「implies we endorse, sponsor or approve」「misleading or disparaging」な使い方は不可（§5）。四半期コンテンツボーナス（Friend $100／Advocate $200／Ambassador $300、承認制）の対象コンテンツは「promote Lodgify as a preferred solution」「unpublished and exclusive to Lodgify」「Lodgifyの承認を得る」「stay published for at least a year」が条件（§3.2） | 規約 §3.2・§5・§8 | 2026-11-05 | 確認済 |
| 対象外の人 | Lodgifyの既存顧客（「Lodgify customers are excluded」。代わりに顧客紹介「Refer & Earn」を利用）、役員・従業員。自分のリンクでの自己契約は不可。 | 規約 §1.1・§4.2 | 2026-11-05 | 確認済 |
| 規約の変更・一方的な取消し | 「We reserve the right to freeze, void, or reverse any or all commission at any time for any reason and without warning」。規約は随時変更可。規約ページ上の表示「Last update: October 1st, 2026」。PDF版の題名は「Affiliate Program 2.0 - T&Cs 01_02_2026」（2026年2月1日付と読める） | 規約 §2.3.4 | 2026-11-05 | 確認済 |
| 紹介先への特典（割引コード） | AdvocateとAmbassadorに割引コード（10%／15%）。Professional・Ultimateの年払い・2年払いの新規顧客のみ有効。クーポンのみ利用でリンク経由でない場合は紹介実績にならない | 規約 §3.4 | 2026-11-05 | 確認済 |
| インフルエンサー枠 | 別規約。報酬10%または15%（最大12か月）。条件は「influencer program」が優先 | 規約 §2.2.4 | 2026-11-05 | 確認済 |
| 既存顧客向けの紹介制度 | 「you'll earn 30% of their first subscription fee, and they'll get 15% off」（アカウント内の Refer & Earn） | https://webflow-mkt.lodgify.com/affiliates | 2026-11-05 | 確認済 |

## 7. 乗り換え

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| データ移行の支援 | 「Our onboarding team imports your listings, reservations and guest data from your current system.」無料の個別オンボーディング。専用ページあり | https://webflow-mkt.lodgify.com/switching-software | 2026-11-05 | 確認済 |
| オンボーディングの対象プラン | 料金ページでは Starter・Professional・Ultimate に「1:1 onboarding」。Basicは「Easy self-onboarding」で個別オンボーディングは「Not included」。乗り換えページの「Free personalized onboarding」がBasicにも適用されるかは記載が揃っていない | https://webflow-mkt.lodgify.com/pricing ／ https://webflow-mkt.lodgify.com/switching-software | 2026-11-05 | 確認済（Basicの扱いは不明） |
| 乗り換え手順 | Free demo → Onboarding → You're live → Advanced features → Always here の5段階 | https://webflow-mkt.lodgify.com/switching-software | 2026-11-05 | 確認済 |
| 他ツールからのインポート方法（具体的な形式・対応ツール） | 取り込みの具体的な方法（CSV等）、対応する元ツールの一覧は公式ページに記載なし | https://webflow-mkt.lodgify.com/switching-software | 2026-11-05 | 未確認 |
| 退会時のデータ書き出し | 確認できず | — | 2026-11-05 | 未確認 |

## 8. 注意すべき点

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| 公式の記載同士の食い違い | 同じ公式サイト内で、サポート時間（24/7とプラン別の電話・チャット）、Expedia連携の有無、アフィリエイトのティア条件（売上額か紹介数か）の記述が一致しない。実際の契約前に確認が要る | 各行の出典を参照 | 2026-11-05 | 確認済 |
| 契約更新の通知なし | 自動更新で、更新前の通知は送られない。解約は契約期間終了の1日前（アカウント画面）／5日前（メール）まで。期間途中の解約は返金なし | https://webflow-mkt.lodgify.com/terms | 2026-11-05 | 確認済 |
| 決済手数料1%は全プラン共通 | 予約手数料は0%だが、サイト経由のオンライン決済は別に1%（ゲートウェイ手数料とは別） | https://webflow-mkt.lodgify.com/pricing | 2026-11-05 | 確認済 |
| 料金はUSD/EUR/GBPで、為替の影響を受ける | 日本円での請求・円建ての価格表示は確認できず | https://webflow-mkt.lodgify.com/pricing | 2026-11-05 | 確認済 |
| 利用者の不満（第三者・検索結果の要約のみ。各ページは未開封） | チャネル同期の遅延（Vrbo・Booking.comの接続に日数がかかったとの口コミ）、サポート応答の遅れの指摘、1年目以降の値上げの指摘、動作が遅い・カレンダー操作が扱いにくいとの口コミ。個別の口コミは匿名で、典型例かは不明。評価はTrustpilot約4.8、Capterra 4.5/5（検索結果の表記） | 検索結果上の https://www.capterra.com/p/131924/Lodgify/reviews/ ／ https://au.trustpilot.com/review/lodgify.com?page=9 ／ getapp.com 各国版 | 2026-11-05 | 第三者のみ |
| 日本での利用実績 | 日本の民泊での利用事例・日本語の公式情報は見つからなかった | — | 2026-11-05 | 未確認 |

## 調べられなかったこと

- `www.lodgify.com` の本体ページ（料金・連携・アフィリエイト・規約）とヘルプセンターは403／名前解決失敗で開けず、`webflow-mkt.lodgify.com` の公開コピーで代用した。`www` 側との内容一致は未照合。
- 物件数別（3・5・10・20室）の料金。スライダー計算がJavaScriptで、静的に取得できなかった。
- 管理画面（アプリ内）の対応言語に日本語があるか。予約サイトの32言語の内訳。
- JPYでの価格設定・決済、日本のStripe／PayPalでの利用可否、Payyoの対応通貨。
- 楽天トラベル・じゃらん・Agodaとの連携（公式の連携としては記載なし。iCalでの運用可否は未検証）。
- 日本のインボイス制度（適格請求書）への対応、住宅宿泊事業法（届出番号の表示、宿泊者名簿の様式、180日カウントなど）に関する機能、Guest Registrationの対象国に日本が含まれるか、パスポート確認機能。
- Akerun・SESAMEなど日本のスマートロックとの連携（連携一覧に記載なし）。
- 日本語でのサポート可否と日本時間の対応可否。
- アフィリエイトのクッキー期間。「Earn up to $2,000 per referral」の根拠。
- 他ツールからのインポートの具体的な方法と対応ツール、退会時のデータ書き出し。
- 利用者の不満の一次情報（Trustpilot・Capterra等のページ自体は開いていない）。
