# 事実カード：Hospitable（hospitable.com）

- 取得日：すべて 2026-11-05
- 書式：`_スキーマ.md` に従う。確度は 確認済／第三者のみ／未確認
- 取得方法の注記：
  - hospitable.com/pricing は Framer 製で、プラン月額が JavaScript 描画のため静的HTMLでは「--」表示。価格は公式ヘルプ記事（help.hospitable.com）の表で確認した。
  - ヘルプ記事の価格は USD。円建て請求の記載は見つからなかった（後述）。
  - 金額の「合計」列は、公式の「基本料金＋追加物件単価」から私が計算した値（計算値）。公式がその合計を載せているわけではない。

## 1. 基本

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| 運営会社 | Hospitable R&D BV（オランダ法の有限会社、会社番号 867550636）。サイト運営者表記も同じ。「Hospitable is not affiliated with Airbnb, Inc.」 | https://hospitable.com/legal/subscription-agreement | 2026-11-05 | 確認済 |
| 利用規約の準拠法 | エストニア法、紛争はタリン（Tallinn）の裁判所 | https://hospitable.com/legal/subscription-agreement | 2026-11-05 | 確認済 |
| 対象規模（公式の区分） | 「Hosts 1—10 properties」「Co-hosts and Property Managers 11—20 properties」「Enterprise 21+ properties」 | https://hospitable.com/pricing | 2026-11-05 | 確認済 |
| 利用者数（公式の自称） | 「Trusted by 26,000+ hosts」（affiliates・switch ページ）。ページごとに数字が違う（integrations ページは 18,000 subscribers、旧検索結果は 23,000+）ため時期差あり | https://hospitable.com/affiliates ／ https://hospitable.com/integrations | 2026-11-05 | 確認済 |
| 認証 | 「SOC 2 Type II certification」 | https://hospitable.com/pricing | 2026-11-05 | 確認済 |
| プラン名 | Essentials／Host／Professional／Mogul（旧 Legacy は 2024-05-01 より前の契約者のみ） | https://help.hospitable.com/en/articles/4596748-how-does-our-pricing-work | 2026-11-05 | 確認済 |

## 2. 料金

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| 課金モデル | 基本料金（プラン固定）＋「active property」への追加料金。active property = 請求期間中に1回以上チェックインがあった物件、または Dynamic Pricing を有効にした物件 | https://help.hospitable.com/en/articles/4596748-how-does-our-pricing-work | 2026-11-05 | 確認済 |
| Essentials | 基本料金 $0、物件数無制限、追加物件料金なし。ただし機能制限あり（下記）。サポートは AI（Smarty）とコミュニティのみ | 同上 ／ https://help.hospitable.com/en/articles/4605159-how-to-contact-hospitable-support | 2026-11-05 | 確認済 |
| Host | 基本 $29／月、含まれる物件 1、追加物件 $10／件。最大物件数 2 | 同上 | 2026-11-05 | 確認済 |
| Professional | 基本 $59／月、含まれる物件 2、追加物件 $15／件。物件数無制限 | 同上 | 2026-11-05 | 確認済 |
| Mogul | 基本 $99／月、含まれる物件 3、追加物件 $30／件。物件数無制限 | 同上 | 2026-11-05 | 確認済 |
| 目安：1室（月払い、USD、計算値） | Essentials $0／Host $29／Professional $59／Mogul $99 | 上記から計算 | 2026-11-05 | 確認済（計算値） |
| 目安：3室（月払い、USD、計算値） | Essentials $0／Host は上限2のため不可／Professional $59+15=$74／Mogul $99 | 上記から計算 | 2026-11-05 | 確認済（計算値） |
| 目安：5室（月払い、USD、計算値） | Professional $59+15×3=$104／Mogul $99+30×2=$159 | 上記から計算 | 2026-11-05 | 確認済（計算値） |
| 目安：10室（月払い、USD、計算値） | Professional $59+15×8=$179／Mogul $99+30×7=$309 | 上記から計算 | 2026-11-05 | 確認済（計算値） |
| 目安：20室（月払い、USD、計算値） | Professional $59+15×18=$329／Mogul $99+30×17=$609（21室以上は pricing ページに「Managing 20+ properties? Get a personalized walkthrough」、Enterprise 扱い） | 上記から計算 ／ https://hospitable.com/pricing | 2026-11-05 | 確認済（計算値） |
| 計算の前提 | 全物件が active の場合。チェックインのない月は追加物件料金の対象外（active でない）。基本料金は物件が停止・ミュート中でも契約中は請求される。公式例：「Professional で4物件 → $59 + $15×2 = $89」 | https://help.hospitable.com/en/articles/4596748-how-does-our-pricing-work | 2026-11-05 | 確認済 |
| 年払い | 年額前払いで 12% 割引（Host／Professional／Mogul）。事前に購入した物件数を超えると超過分は月額レートで課金。使わなかった分は次回更新などに充当されるクレジットで、現金返金なし | 同上 | 2026-11-05 | 確認済 |
| 無料トライアル | 「Try all features for free for 14 days」「No credit card required」 | https://hospitable.com/pricing | 2026-11-05 | 確認済 |
| 契約縛り（月払い） | 「No Contract or Commitments」。月払いはいつでも解約でき、当月末で終了 | https://help.hospitable.com/en/articles/4596748-how-does-our-pricing-work | 2026-11-05 | 確認済 |
| 契約縛り（年払い） | 12か月の約束。トライアル開始から30日以内は全額返金で解約可。30日経過後は更新期間の終わりに解約が有効になり返金なし | 同上 | 2026-11-05 | 確認済 |
| 解約の方法 | Settings → Plans & billing から。ダウングレードは即時ではなく請求周期末に反映される場合あり（Essentials へは期末）。Host へのダウングレードは稼働物件が2以下であること | 同上 | 2026-11-05 | 確認済 |
| 利用規約上の返金 | 「No refunds or credits for Subscription Charges ... will be provided to You if You elect to terminate your subscription ... prior to the end of Your then effective Subscription Term.」 | https://hospitable.com/legal/subscription-agreement | 2026-11-05 | 確認済 |
| Dynamic Pricing の料金 | Host／Professional／Mogul は込み。ただし期間中チェックインのない物件で DP を有効化していた場合は $10 の追加。Essentials は「最初の3予約または30日の無料」、その後 $15／物件／月 | https://help.hospitable.com/en/articles/4596748-how-does-our-pricing-work | 2026-11-05 | 確認済 |
| ダイレクト予約の手数料 | Professional／Mogul のみ。Basic 1%、Premium 4% + 3% 決済手数料（予約ごと）。Host・Essentials は不可 | 同上 | 2026-11-05 | 確認済 |
| 追加手数料：アップセル | Essentials 10%、Host／Professional／Mogul 7%（processing fee） | https://hospitable.com/pricing | 2026-11-05 | 確認済 |
| 追加手数料：セキュリティデポジット | 「Security Deposits 2% processing fee」。対応通貨は USD・GBP・AUD のみ（ヘルプ記事の記載。検索結果で確認、記事本文は未開封） | https://hospitable.com/pricing | 2026-11-05 | 確認済（2%）／第三者のみ（通貨：検索要約のみ） |
| 追加手数料：Vrbo の MoR | 「Hospitable MoR on Vrbo」3.9% 決済手数料（豪州 2.7%）＋Vrbo手数料。「Stripe MoR on Vrbo」1% サービス料＋Vrbo の 5% pay-per-booking＋Stripe手数料 | https://hospitable.com/pricing | 2026-11-05 | 確認済 |
| 追加手数料：ゲスト審査 | ID確認 $2／件（初回無料）、Full verification $5／件（検索要約。pricing ページには「Full Verification / ID Check」とあるが金額は描画されず） | https://hospitable.com/features/guest-verification | 2026-11-05 | 第三者のみ（要再確認） |
| 追加手数料：スマートデバイス | Professional は1物件あたり2台、Mogul は4台まで込み。超過は1台 $5 | https://help.hospitable.com/en/articles/4596748-how-does-our-pricing-work | 2026-11-05 | 確認済 |
| 追加手数料：清掃チームへの支払い | Essentials 2.5%（1回あたり上限 US$5）、有料プラン 1.5%（上限 US$5） | https://hospitable.com/pricing | 2026-11-05 | 確認済 |
| 料金ページの表示状況 | 公式 pricing ページはプラン月額を JS で描画（静的HTMLでは「--」）。Host プランに「Maximum Properties 2」の記載あり。第三者 PricingSaaS は「2026年7月に比較表の月額が Contact sales に置き換わった」と記録（未検証） | https://hospitable.com/pricing ／ https://pricingsaas.com/companies/hospitable | 2026-11-05 | 確認済（JS描画の事実）／第三者のみ（Contact sales の件） |
| 税 | 「Prices exclude — where applicable」（税抜表示の注記） | https://hospitable.com/pricing | 2026-11-05 | 確認済 |

## 3. チャネル

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| 対応チャネル（公式表示） | 「Booking channels supported: Airbnb, Vrbo, Booking.com, Agoda」（全プラン共通） | https://hospitable.com/pricing | 2026-11-05 | 確認済 |
| 接続方式 | Airbnb・Agoda・Booking.com・Vrbo は「direct, two-way connections」（API接続）。ほかは iCal 取り込み（一方向、20分ごとに確認） | https://help.hospitable.com/en/articles/14189123-understanding-how-reservations-sync-across-channels ／ https://help.hospitable.com/en/articles/16309227-switching-to-hospitable-from-another-pms | 2026-11-05 | 確認済 |
| 公式パートナー認定 | Airbnb「Preferred+ Partner」のバッジを掲載。Booking.com Connectivity Partner と説明するブログあり。Vrbo は「Vrbo Partner Connection (Official Integration)」 | https://hospitable.com/airbnb-partnerships ／ https://hospitable.com/booking-com-connectivity-partners ／ https://help.hospitable.com/en/articles/16309227-switching-to-hospitable-from-another-pms | 2026-11-05 | 確認済 |
| Expedia | 専用接続なし。「iCal-only channels (Tripadvisor, Expedia, Hipcamp, Hopper, Houfy, Plum Guide, Holidu, ...)」に分類。Vrbo 経由の Expedia 配信は Vrbo 側の設定に依存 | https://help.hospitable.com/en/articles/16309227-switching-to-hospitable-from-another-pms | 2026-11-05 | 確認済 |
| Google Vacation Rentals | Professional 以上で掲載機能あり | https://hospitable.com/pricing | 2026-11-05 | 確認済 |
| 楽天トラベル | 公式ページ・ヘルプに記載なし。専用接続は確認できない。iCal 取り込みの対象にはなり得るが、楽天側が iCal を出力するかは未確認 | https://help.hospitable.com/en/articles/16309227-switching-to-hospitable-from-another-pms | 2026-11-05 | 未確認 |
| じゃらん | 同上。記載なし | 同上 | 2026-11-05 | 未確認 |
| iCal の制約 | 一方向（取り込みのみ）、即時ではない。Booking.com 接続時は iCal 取り込みを外す必要あり。Airbnb は PMS 利用時に iCal 取り込み不可 | https://help.hospitable.com/en/articles/10373495-connecting-channels-with-ical-imports ほか（検索要約） | 2026-11-05 | 第三者のみ（検索要約。記事本文は未開封） |
| 重複予約防止 | 各チャネルの掲載を物件に「Merge（結合）」して同期する。ヘルプに「Merge your listings ... This is a crucial step in syncing listing calendars and preventing double bookings!」 | https://help.hospitable.com/en/articles/16309227-switching-to-hospitable-from-another-pms | 2026-11-05 | 確認済 |
| 接続が切れた場合 | 「For VRBO channels, if the channel is disconnected when a guest books, Hospitable cannot create the reservation immediately, leading to potential double bookings.」 | https://help.hospitable.com/en/articles/14189123-understanding-how-reservations-sync-across-channels | 2026-11-05 | 確認済 |

## 4. 機能

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| 統合受信箱／カレンダー | 全プランで Unified Inbox と Calendar | https://hospitable.com/pricing | 2026-11-05 | 確認済 |
| 自動メッセージ | Essentials は「Scheduled Guest Messages: Limited」。Host 以上は「Automated guest messaging」。Q&A自動返信・AI下書きは Essentials では「10 per week」まで。Mogul は「Fully automated guest messaging with Inbox AI」 | https://hospitable.com/pricing | 2026-11-05 | 確認済 |
| 清掃・タスク | 全プランに Tasks Manager／Tasks App、Cleaner Marketplace、清掃員への支払い機能 | https://hospitable.com/pricing | 2026-11-05 | 確認済 |
| スマートロック連携先（公式パートナー一覧） | August、Igloohome、Jervis、Nuki、Schlage、SmartThings、TT Locks（TTLock）、Yale。Professional 以上で利用可 | https://hospitable.com/integrations/smart-locks-integration-partners ／ https://help.hospitable.com/en/articles/4596748-how-does-our-pricing-work | 2026-11-05 | 確認済 |
| 日本のスマートロック（Akerun、SESAME） | 公式の一覧に載っていない。個別対応の有無は確認できていない | 同上 | 2026-11-05 | 未確認 |
| 価格ツール連携 | 自前の Dynamic Pricing（Host 以上は込み）。外部は PriceLabs、Beyond Pricing に接続可（移行ガイドの記載）。Essentials でも外部連携は有料プランが必要と明記 | https://help.hospitable.com/en/articles/16309227-switching-to-hospitable-from-another-pms ／ https://help.hospitable.com/en/articles/4596748-how-does-our-pricing-work | 2026-11-05 | 確認済 |
| オーナーポータル | Mogul のみ（Owner Portals、Owner Statements & Invoices） | https://hospitable.com/pricing ／ https://help.hospitable.com/en/articles/4596748-how-does-our-pricing-work | 2026-11-05 | 確認済 |
| ダイレクト予約サイト | Professional 以上（Direct Booking Website、チャージバック／損害補償付き）。ダイレクト予約手数料は第2節 | https://hospitable.com/pricing | 2026-11-05 | 確認済 |
| 会計 | Mogul：Accounting built in or via QuickBooks。「Trust Accounting: Currently in pilot」 | https://hospitable.com/pricing | 2026-11-05 | 確認済 |
| その他 | Guest Portal、Rental Agreements、レビュー管理、Google Vacation Rentals、AI Copilot、API／MCP、App Marketplace | https://hospitable.com/pricing | 2026-11-05 | 確認済 |
| 稼働の注意（モバイル） | プラン変更はモバイルアプリからはできない（Web または携帯ブラウザ） | https://help.hospitable.com/en/articles/4596748-how-does-our-pricing-work | 2026-11-05 | 確認済 |

## 5. 日本対応

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| 管理画面のUI言語 | 英語のみ。「How can I change the user interface language on Hospitable? At this time, Hospitable is only available in English.」ブラウザ翻訳拡張の利用を案内 | https://help.hospitable.com/en/articles/8060844-faqs-troubleshooting-account-settings | 2026-11-05 | 確認済 |
| ゲスト向け定型メッセージの言語 | 事前定義メッセージの言語は英語・スペイン語・フランス語・ドイツ語。日本語の追加要望が公式フィードバックにあり（2026-06-08 投稿、取得時のステータス「New」、票1）。回避策は受信箱で手書き | https://feedback.hospitable.com/p/add-japanese-as-a-language-option-in-pre-defined-guest | 2026-11-05 | 確認済（要望ページ）。日本語が実装済みかは未確認 |
| 多言語機能（公式の説明） | ゲストの言語を「listing view or first message」から自動検出。テンプレに該当言語がなければフォールバック言語、なければ送信しない。受信箱の自動翻訳、AI返信も多言語 | https://hospitable.com/features/multilingual-support | 2026-11-05 | 確認済 |
| 対応言語数（ダイレクト予約サイト） | 「Hospitable currently supports: English (default), Spanish, French, German」（2026-08-20 記事） | https://help.hospitable.com/en/articles/14804543-managing-languages-on-your-site | 2026-11-05 | 確認済 |
| サポート言語 | 英語（ヘルプセンターは英語・ポルトガル語(BR)・スペイン語）。日本語サポートの記載は見つからず | https://help.hospitable.com/en/articles/4605159-how-to-contact-hospitable-support | 2026-11-05 | 未確認（日本語は記載なし） |
| サポート窓口と対応時間 | Host／Professional／Mogul：メール・ライブチャット・コミュニティ。Essentials：AIボット Smarty とコミュニティのみ（人間のチャット・メールなし）。人間の対応時間・タイムゾーンは記載なし | https://help.hospitable.com/en/articles/4605159-how-to-contact-hospitable-support | 2026-11-05 | 確認済（窓口）／未確認（対応時間） |
| 請求通貨 | 契約者の請求住所で決まり、後から自分では変更不可（サポートに依頼）。公式の記載で出てくる通貨は USD、EUR、GBP、AUD、CAD、THB（例）。**JPY の記載は見つからず** | https://help.hospitable.com/en/articles/8060843-subscription-faqs-troubleshooting ／ 検索要約 | 2026-11-05 | 確認済（変更不可の記載）／未確認（JPY請求の可否） |
| 物件・ダイレクト予約の通貨 | 物件の通貨はリード掲載から設定。Airbnb と Vrbo Partner の通貨は一致が必要で、Agoda と Booking.com は例外。例として「Booking.com (JPY)」の結合が成功する図あり（JPY の物件を扱える示唆） | https://help.hospitable.com/en/articles/12806877-property-currencies-in-hospitable-how-they-work-how-they-re-set-and-how-they-affect-your-channel-calendars | 2026-11-05 | 確認済 |
| 決済手段（サブスク） | Visa・MasterCard（全通貨）、AMEX（SGD・GBP除く）、Discover（EUR・USD）、PayPal。ACH／SEPA の口座引落は不可。請求書払いは企業顧客のみ個別対応 | https://help.hospitable.com/en/articles/4533299-accepted-payment-methods | 2026-11-05 | 確認済 |
| 請求書・インボイス（日本のインボイス制度） | 月次のサブスク請求書メールあり、Plans & billing → Invoices でダウンロード可、VAT番号欄あり（EU向け）。**日本の適格請求書発行事業者登録番号（T番号）や消費税の表示は見つからず** | https://help.hospitable.com/en/articles/4602476-change-your-billing-address-tax-id-vat-or-company-name（検索要約） | 2026-11-05 | 第三者のみ（検索要約）／日本のインボイス対応は未確認 |
| 宿泊者名簿・パスポート確認 | ゲスト確認機能：ゲストポータルで政府発行IDの撮影・自撮り・メール電話確認。ID確認と Full verification の2種。対応国・パスポートの扱いは記載なし。日本の宿泊者名簿（旅館業法・民泊法の名簿要件）に合わせた機能の記載なし | https://hospitable.com/features/guest-verification | 2026-11-05 | 確認済（機能の存在）／未確認（日本の名簿要件） |
| 住宅宿泊事業法に関する機能 | 日本の届出番号の専用欄は確認できず。物件の Details → Licences（または Licensing）にライセンス・登録番号を入力し Vrbo／Booking.com に連携する機能あり（日本固有ではない） | 検索要約（help.hospitable.com の複数記事）／ https://hospitable.com/short-term-rental-license | 2026-11-05 | 第三者のみ（検索要約）／日本向けは未確認 |
| 日本国内の予約サイト（楽天・じゃらん等） | 公式一覧に記載なし（第3節） | https://hospitable.com/integrations | 2026-11-05 | 未確認 |

## 6. アフィリエイト

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| 有無 | あり。自社運営（affiliates.hospitable.com）。PartnerStack／Impact 等の外部ネットワークの記載なし | https://help.hospitable.com/en/articles/16821478-hospitable-affiliate-program | 2026-11-05 | 確認済 |
| 申込URL | https://affiliates.hospitable.com（承認待ちなし、「immediate access to your affiliate dashboard」）。ただし規約では「Hospitable may accept or reject any Affiliate at its sole discretion」 | https://hospitable.com/affiliates ／ https://affiliates.hospitable.com/terms | 2026-11-05 | 確認済 |
| 報酬 | 紹介1件につき固定 $200（定率・段階なし、上限なし）。紹介された側は最初の3か月の請求が 25% 割引 | https://hospitable.com/affiliates ／ https://help.hospitable.com/en/articles/16821478-hospitable-affiliate-program | 2026-11-05 | 確認済 |
| 報酬の発生条件 | 紹介リンクで登録し、予約チャネルの掲載を1件以上接続した時点（無料プランも対象）。物件管理会社経由の場合は物件が稼働し初回支払いを受けた時。1人につき1回。最終判断は Hospitable | https://help.hospitable.com/en/articles/16821478-hospitable-affiliate-program | 2026-11-05 | 確認済 |
| 支払い | 月次。Hospitable が請求書を自動作成し、請求日から Net-30 で支払い。最低支払額なし | 同上 | 2026-11-05 | 確認済 |
| 対象者 | 「established online presence」（ブログ、YouTube、ニュースレター、SNS、コミュニティ）を持つ人。知人を1人ずつ紹介する用途なら「Refer a Host」（既存顧客向け、$100 の請求クレジット、紹介される側 $30 クレジット）を使う | 同上 | 2026-11-05 | 確認済 |
| 規約上の制限（規約本文、JSバンドルから抽出） | 禁止：Hospitable のサービス・料金・機能の誤表示、無断の主張・保証、スパム・無許可の勧誘、公式代表者を装うこと、自己紹介・架空アカウント。開示義務あり（法令上必要な場合は提携関係を明示）。ロゴ等は限定・非独占・取消可能のライセンス、改変不可。個人データの扱いに制限。賠償（indemnify）条項あり | https://affiliates.hospitable.com/terms（SPAのため本文は https://affiliates.hospitable.com/assets/Terms-Fdqi3mI8.js から取得） | 2026-11-05 | 確認済 |
| ブランド名入札（ブランドキーワードの有償検索広告）禁止 | 規約本文に該当する文言は見つからなかった（「brand」「bidding」「trademark」の用途制限は上記のロゴ利用のみ） | 同上 | 2026-11-05 | 確認済（記載なし。明文の禁止は確認できず） |
| クッキー有効期間 | 記載なし。「Hospitable isn't responsible for missed tracking caused by ... browser or cookie restrictions」とのみ。ダッシュボードが「sole source of truth」 | 同上 ／ ヘルプ記事 | 2026-11-05 | 未確認 |
| コンテンツの制限 | 規約は上記の禁止事項のみ。比較記事の内容に関する個別の制限は記載なし | 同上 | 2026-11-05 | 確認済（記載なし） |
| 解除・変更 | 「at any time, with or without cause」で終了可。規約はいつでも変更可。違反でない終了なら終了前の有効な紹介分は支払い | 同上 | 2026-11-05 | 確認済 |
| 日本居住者の参加可否・円払い・源泉税 | 記載なし | 同上 | 2026-11-05 | 未確認 |

## 7. 乗り換え

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| 他PMSからの自動データ移行 | なし。「Hospitable does not have a connection or integration with any other PMS, meaning there is no way of transferring your data from a different PMS ... via API connection.」 | https://help.hospitable.com/en/articles/16309227-switching-to-hospitable-from-another-pms | 2026-11-05 | 確認済 |
| 移行ガイド | あり（公式ページと、Airbnb・Booking.com・Agoda・Vrbo ごとの接続ガイド） | https://hospitable.com/switch-to-hospitable ／ 上記ヘルプ記事 | 2026-11-05 | 確認済 |
| 予約・リスティング | リスティングは再作成不要（既存のものに接続）。Airbnb は過去予約を最大5,000件取り込み。Booking.com は過去予約を API で送らない。Vrbo は切替後に移る（一部の過去の金額情報は別途取り込みが必要） | https://hospitable.com/switch-to-hospitable | 2026-11-05 | 確認済 |
| ダイレクト／手動予約 | 自動では移らない。少数なら手入力、大量なら CSV を Support が取り込み | 同上 ／ 上記ヘルプ記事 | 2026-11-05 | 確認済 |
| 自動メッセージ | 自動では移らない。作り直しが必要 | 同上 | 2026-11-05 | 確認済 |
| 切替時のダウンタイム | Vrbo：公式の Software Switch で直接引き継ぎ。Airbnb：旧PMSを切断してから接続。Booking.com：接続変更中に掲載を一時停止することを推奨（最大10分程度）。Hostaway→Airbnb の切断解放は24〜48時間かかることがある | 上記ヘルプ記事 | 2026-11-05 | 確認済 |
| 試用しながら準備 | 14日トライアルで設定を先に進められる。Airbnb・Vrbo は制限付き接続で旧PMSと併用可（価格・空室管理は Hospitable を主接続にする必要あり） | https://hospitable.com/switch-to-hospitable | 2026-11-05 | 確認済 |
| オンボーディング | 無料のオリエンテーション通話（トライアル中）。有料の「Rapid Rollout」（1対1、通常3回・合計3〜5時間）は任意 | https://help.hospitable.com/en/articles/4596748-how-does-our-pricing-work | 2026-11-05 | 確認済 |

## 8. 注意すべき点（出典付き）

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| 管理画面が英語のみ | 上記第5節 | https://help.hospitable.com/en/articles/8060844-faqs-troubleshooting-account-settings | 2026-11-05 | 確認済 |
| 日本語の定型メッセージ未対応（少なくとも2026-06時点） | 日本語要望は「New」のまま（票1） | https://feedback.hospitable.com/p/add-japanese-as-a-language-option-in-pre-defined-guest | 2026-11-05 | 確認済 |
| 料金が物件数で増える | 公式の例で、Professional の4物件は $89。Mogul の追加物件は1件 $30 | https://help.hospitable.com/en/articles/4596748-how-does-our-pricing-work | 2026-11-05 | 確認済 |
| Essentials でのサポート | 人間のチャット・メールなし（AI のみ） | https://help.hospitable.com/en/articles/4605159-how-to-contact-hospitable-support | 2026-11-05 | 確認済 |
| 年払いは30日後返金不可 | 上記第2節 | https://help.hospitable.com/en/articles/4596748-how-does-our-pricing-work | 2026-11-05 | 確認済 |
| 旧レートの喪失（利用者の不満） | Capterra 2026-01-07 の1.0評価：「A same-day payment problem caused by a card change ... resulted in permanent loss of a legacy rate with no discretion or escalation offered.」 | https://www.capterra.com/p/189280/smartbnb/reviews/ | 2026-11-05 | 確認済（口コミの記載。事実の真偽は未検証） |
| 一人物件では高い（口コミ） | 「The price is also a bit high since I only have one property.」 | https://www.capterra.com/p/189280/smartbnb/reviews/ | 2026-11-05 | 確認済（口コミの記載） |
| 評価の概況 | Capterra 4.7（145件）。G2 は 4.9／239件、Software Advice 4.7（検索要約） | https://www.capterra.com/p/189280/smartbnb/reviews/ ／ https://www.g2.com/products/hospitable-com | 2026-11-05 | 確認済（Capterra）／第三者のみ（G2） |
| 通知・アプリの不満（G2の記載） | 通知機能が弱い、アプリが時々ログアウトされる（検索要約） | https://www.g2.com/products/hospitable-com | 2026-11-05 | 第三者のみ |
| 国内予約サイトの導線がない | 楽天・じゃらんの専用接続なし。iCal での取り込みが可能かは未確認 | https://help.hospitable.com/en/articles/16309227-switching-to-hospitable-from-another-pms | 2026-11-05 | 未確認 |

## 調べられなかったこと

- 楽天トラベル・じゃらん・その他国内予約サイトとの連携（公式一覧に記載なし。iCal 出力の有無も未確認）
- Akerun・SESAME 等の日本製スマートロックの対応（公式パートナー一覧に載っていないこと以上は不明）
- 日本語でのサポート可否、人間サポートの対応時間・タイムゾーン
- JPY での請求（サブスク）可否。公式の請求通貨リストの全文は取得できていない
- 日本の適格請求書（T番号・消費税）への対応
- 日本の宿泊者名簿（旅館業法／住宅宿泊事業法）の要件に合わせた機能、日本の届出番号の専用表示
- ゲスト確認（ID確認）の対応国・パスポート対応
- アフィリエイトのクッキー有効期間、ブランド名入札の明文規定（規約本文に見当たらず）、日本居住者への報酬支払い条件
- pricing ページの現在の月額の「画面上の」表示（JS描画のため静的取得不可。ヘルプ記事の金額で代替）。第三者が報告した「2026年7月の Contact sales 表示」は未検証
- ゲスト審査料金（$2／$5）、セキュリティデポジットの対応通貨の原文確認（検索要約のみ）
- iCal 取り込み仕様の個別記事、G2 の口コミ原文（G2・Trustpilot は取得不可／403）
- Reddit 等のコミュニティでの評判
