# 事実カード：PriceLabs（価格最適化）

- 取得日：2026-11-05（すべての行）
- 製品の種類：ダイナミックプライシング（価格最適化）ツール。PMS・チャネルマネージャーではない（PMS／Airbnb等に料金と最低宿泊数を送る）。
- 取得方法のメモ：料金ページ（pricelabs.co/plans/）はJavaScript描画だが、HTML内に埋め込まれた公式データを読んだ。ヘルプセンター（help.pricelabs.co）は、同サイトが画面表示に使う公開API経由で記事本文を読んだ（記事の中身は画面と同じ）。WebFetchでは pricelabs.co が名前解決できず、curlで取得した。
- 確度の凡例：確認済＝公式ページ・公式ヘルプを開いて確認／第三者のみ／未確認

## 1. 基本

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| 運営会社 | PriceLabs Revenue Inc.（デラウェア州法人）。利用規約の準拠法はイリノイ州法、紛争は仲裁 | https://pricelabs.co/tandc/ | 2026-11-05 | 確認済 |
| 対象規模 | 「ホスト、物件管理者、ホテル向け」。件数の下限・上限なし（"There is no limit to the number of unique properties you connect to PriceLabs."） | https://hello.pricelabs.co/ja/ ／ https://help.pricelabs.co/portal/en/kb/articles/billing | 2026-11-05 | 確認済 |
| 自社掲載の実績 | 「70万件以上 日次価格設定物件数」「150カ国以上」（自社の数字。第三者検証なし） | https://hello.pricelabs.co/ja/ | 2026-11-05 | 確認済（自社の主張として） |

## 2. 料金

料金は「同期するリスティング数」と「リスティングの所在地」で決まる。日本は、公式が挙げた高単価地域（米・英・加・欧州・豪・NZ・イスラエル）にもブラジルにも入らないため、公式の文言どおりなら「Rest of the world」に当たる。ただし日本が明示的に載っているページは見つからなかった。

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| 課金モデル | リスティング1件ごとの月額（段階制）。同期（Sync Prices）したリスティングが課金対象。"Charges are based on the number of unique properties PriceLabs updates, regardless of days synced." 日割りなし | https://help.pricelabs.co/portal/en/kb/articles/billing | 2026-11-05 | 確認済 |
| 単価（米・英・加・欧州・豪・NZ・イスラエル） | 1件目 USD 19.99／2〜5件目 各 14.99／6〜15件目 各 12.99／16〜25件目 各 8.99／26〜50件目 各 6.99／51〜100件目 各 5.99／101〜250件目 各 5.49／251件目〜 各 5.00（税別） | https://help.pricelabs.co/portal/en/kb/articles/how-much-does-pricelabs-costs | 2026-11-05 | 確認済 |
| 単価（Rest of the world） | 1件目 USD 9.99／2〜5件目 各 9.49／6〜15件目 各 8.99／16〜25件目 各 7.99／26〜50件目 各 6.99／51〜100件目 各 5.99／101〜250件目 各 5.49／251件目〜 各 5.00（税別） | https://help.pricelabs.co/portal/en/kb/articles/how-much-does-pricelabs-costs ／ https://pricelabs.co/plans/ | 2026-11-05 | 確認済 |
| 単価（ブラジル） | 1件目 BRL 47.5 から（段階制） | 同上 | 2026-11-05 | 確認済 |
| 件数別の月額目安（Rest of the world・USD・税別） | 1件 9.99／3件 28.97／5件 47.95／10件 92.90／20件 177.80。上の単価表を「各件数帯の単価を、その帯に入る件から順に積み上げる」と読んだ当方の計算値 | 計算の根拠は上の行 | 2026-11-05 | 計算値（公式の計算機は実行していない。段階の読み方は文言からの解釈） |
| 件数別の月額目安（高単価地域・USD・税別） | 1件 19.99／3件 49.97／5件 79.95／10件 144.90／20件 254.80。同じ計算方法 | 同上 | 2026-11-05 | 計算値（同上） |
| 公式の計算機 | "Use our Pricing Calculator to get an exact quote" と案内あり。計算機のURLは取得できず、実行していない | https://help.pricelabs.co/portal/en/kb/articles/how-much-does-pricelabs-costs | 2026-11-05 | 未確認 |
| 最低料金 | 月額の最低料金（ミニマムチャージ）の別規定は、読んだ範囲では見当たらない（最小は1件分の単価） | https://help.pricelabs.co/portal/en/kb/articles/billing | 2026-11-05 | 未確認 |
| 無料トライアル | 30日間、全機能、カード不要。"You get a 30-day free trial when you add your listings for the first time." 請求周期は無料期間の終了後から始まる | https://pricelabs.co/plans/ ／ https://help.pricelabs.co/portal/en/kb/articles/billing | 2026-11-05 | 確認済 |
| 契約縛り | 月単位（"Billing is month-to-month, and you can cancel anytime."）。利用規約は月単位で自動更新 | https://help.pricelabs.co/portal/en/kb/articles/billing ／ https://pricelabs.co/tandc/ | 2026-11-05 | 確認済 |
| 売上連動プラン | 連携先の総売上の1%。切り替えには1年間の約束が必要で、その間は定額プランに戻せない（解約・一時停止は可能）。請求はUSD。切り替えはサポートへメール | https://help.pricelabs.co/portal/en/kb/articles/billing ／ https://pricelabs.co/plans/ | 2026-11-05 | 確認済 |
| 解約・停止の条件 | リスティングの同期（Sync Prices）をオフにすると、次の請求周期から課金されない。後払い（最終請求は周期の終わり）。解約後もPriceLabsが最後に送った料金・最低宿泊数はPMS／チャネル側に残り、以後は上書きされない。アカウント削除はメール依頼（未払いがないこと） | https://help.pricelabs.co/portal/en/kb/articles/pausing-your-subscription | 2026-11-05 | 確認済 |
| 追加：同期回数 | 自動同期は1日1回が標準に含まれる。追加の自動同期は 1リスティング・1回あたり USD 1。手動同期は無料・無制限 | https://pricelabs.co/plans/ ／ https://help.pricelabs.co/portal/en/kb/articles/billing | 2026-11-05 | 確認済 |
| 追加：同じ物件を複数チャネルで使う場合 | 同一物件を紐づけ（マッピング）すれば、追加チャネルごとに月 USD 1／件。紐づけないと二重課金になりうる | https://help.pricelabs.co/portal/en/kb/articles/billing | 2026-11-05 | 確認済 |
| 追加：複数ユニット（マルチユニット） | 追加ユニットごとに月 USD 5 | https://help.pricelabs.co/portal/en/kb/articles/billing | 2026-11-05 | 確認済 |
| 別商品 | Market Dashboards：新規アカウントは無料1枠、以後 USD 9.99／ダッシュボード／月から（件数で増える）。Revenue Estimator Pro：登録時に無料2回分。Portfolio Analytics：「Dynamic Pricing契約に含まれる」記載あり。Listing Optimizer の価格は読めなかった | https://pricelabs.co/plans/ | 2026-11-05 | 確認済（Listing Optimizerの価格のみ未確認） |
| バンドル（Performance／Expansion） | 割引バンドルがある。価格は計算機でのみ表示とされ、未取得 | https://help.pricelabs.co/portal/en/kb/articles/billing | 2026-11-05 | 未確認（価格） |
| 料金改定 | 手数料体系の変更は30日前に通知。異議がある場合の唯一の救済は解約 | https://pricelabs.co/tandc/ | 2026-11-05 | 確認済 |
| 支払い手段 | 主要なクレジットカード／デビットカード。EUなどデビットにCVVがない地域ではクレジットカードのみ | https://pricelabs.co/plans/ ／ https://help.pricelabs.co/portal/en/kb/articles/billing | 2026-11-05 | 確認済 |
| 請求通貨 | 料金表はUSD（ブラジルはBRL）。売上連動プランはUSD請求。日本円（JPY）請求の記載は見つからない | https://help.pricelabs.co/portal/en/kb/articles/billing | 2026-11-05 | 未確認（JPY請求） |
| 税 | 請求先住所と現地税制に応じて税が加算される場合あり | https://help.pricelabs.co/portal/en/kb/articles/billing | 2026-11-05 | 確認済 |
| ダイレクト予約手数料 | 該当なし（予約を扱う製品ではない）。広告に「手数料なし」の記載あり："flat monthly pricing with no commission or long-term contract"（定額プランについて） | https://pricelabs.co/plans/ | 2026-11-05 | 確認済 |

## 3. チャネル・連携先（価格の送り先）

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| Airbnb | 公式連携（記事名に "official Airbnb integration"）。料金・最低宿泊・チェックイン／アウト制限を最大540日先まで送れる。条件：PMSを使っている場合はPMSと連携すること（"integrate PriceLabs with your PMS, not directly with Airbnb"）、AirbnbのSmart Pricingはオフ、リスティングが公開中・予約可能であること | https://help.pricelabs.co/portal/en/kb/articles/how-to-integrate-pricelabs-with-airbnb-official-airbnb-integration | 2026-11-05 | 確認済 |
| Booking.com | 直接連携。料金・最低宿泊・チェックイン／アウト制限を送れる。標準の価格窓は1年（サポートに頼むと720日） | https://help.pricelabs.co/portal/en/kb/articles/how-to-integrate-pricelabs-with-booking | 2026-11-05 | 確認済 |
| Vrbo | 直接連携（Chromeの拡張機能でインポート）。最大365日先 | https://help.pricelabs.co/portal/en/kb/articles/vrbo | 2026-11-05 | 確認済 |
| Houfy | 直接連携の一覧に記載 | https://help.pricelabs.co/portal/en/kb/articles/available-integrations | 2026-11-05 | 確認済 |
| Expedia／Agoda | 直接連携の一覧に載っていない。PMS／チャネルマネージャー経由になる（"Data will flow from PriceLabs → PMS → Airbnb/VRBO/other channels."） | https://help.pricelabs.co/portal/en/kb/articles/available-integrations | 2026-11-05 | 確認済（一覧に無いこと）／経由先ごとの可否は未確認 |
| 楽天トラベル／じゃらん | 連携一覧（OTA・PMS・チャネルマネージャー合計約190件）に名前なし。サイトコントローラー経由の可否は未確認 | https://help.pricelabs.co/portal/en/kb/articles/available-integrations ／ https://pricelabs.co/integrations/ | 2026-11-05 | 確認済（一覧に無いこと）／経由の可否は未確認 |
| PMS連携（一部。一覧は約190件で、公式は "160+" "150+" と表記） | Beds24、Cloudbeds、Channex、Guesty、Hospitable、Hostaway、Hostex、Hostfully、iGMS、Lodgify、OwnerRez、Rentals United、Smoobu、Uplisting など | https://help.pricelabs.co/portal/en/kb/articles/available-integrations | 2026-11-05 | 確認済 |
| Hostfully との連携 | あり。料金・最低宿泊・チェックイン／アウト制限を最大720日先まで送れる。注意：PriceLabsを有効にした物件は、Hostfully側から日別料金を変更・送信できなくなる | https://help.pricelabs.co/portal/en/kb/articles/hostfully | 2026-11-05 | 確認済 |
| Sirvoy との連携 | 連携一覧（ヘルプ記事・公式連携ページの両方）に Sirvoy の名前なし | https://help.pricelabs.co/portal/en/kb/articles/available-integrations ／ https://pricelabs.co/integrations/ | 2026-11-05 | 確認済（一覧に無いこと） |
| 一覧に無いPMS | support@pricelabs.co に連絡するよう案内。PMS側がPriceLabsのAPIを使う形の連携先も別枠で多数 | https://help.pricelabs.co/portal/en/kb/articles/available-integrations | 2026-11-05 | 確認済 |

## 4. 機能（該当するものだけ）

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| 価格最適化 | 市場データと自分の実績から、日々の料金と最低宿泊日数を自動更新。カスタマイズ設定30以上。ハイパーローカルプラス（HLP）アルゴリズム。最終価格はユーザーが管理（"constitutes recommendations only"） | https://pricelabs.co/plans/ ／ https://hello.pricelabs.co/ja/ ／ https://pricelabs.co/tandc/ | 2026-11-05 | 確認済 |
| 付随ツール | Portfolio Analytics、Market Dashboards、Revenue Estimator Pro、Listing Optimizer（Airbnb向け）、AI Insights、API、AIツール向けMCPコネクタ | https://pricelabs.co/plans/ ／ https://help.pricelabs.co/portal/en/kb/articles/pricelabs-mcp-ai-connector | 2026-11-05 | 確認済（存在のみ） |
| ユーザー数 | "Unlimited multi-user access" | https://pricelabs.co/plans/ | 2026-11-05 | 確認済 |
| 自動メッセージ／清掃タスク／スマートロック／オーナーポータル／ダイレクト予約サイト／会計 | 該当なし（価格ツールのため）。オーナー向けレポート機能（Owner Analytics Dashboard）はベータの記載あり（10件超のユーザー向け） | https://help.pricelabs.co/portal/en/kb/articles/understanding-owner-analytics-dashboard | 2026-11-05 | 確認済（ベータの存在のみ） |

## 5. 日本対応

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| 公式サイトの日本語 | あり（トップ、料金、ダイナミックプライシング等の日本語ページ） | https://hello.pricelabs.co/ja/ ／ https://hello.pricelabs.co/ja/plans/ | 2026-11-05 | 確認済 |
| ヘルプセンターの日本語 | あり（日本語に翻訳された記事が存在。例：請求、通貨変更、カスタマイズ一覧）。どこまで翻訳済みかは未集計 | https://help.pricelabs.co/portal/ja/kb/articles/how-to-choose-currency | 2026-11-05 | 確認済（一部）／網羅率は未確認 |
| アプリ画面（管理画面）の日本語 | 確認できず（ログインしていない） | － | 2026-11-05 | 未確認 |
| サポート言語・対応時間 | メール（support@pricelabs.co）。日本語サポートの有無・営業時間は確認できず。毎日のトレーニングセッションは英語・スペイン語・フランス語・ポルトガル語で開催（日本語は無し） | https://help.pricelabs.co/portal/ja/kb/articles/pricelabs%E3%82%92%E5%8A%B9%E6%9E%9C%E7%9A%84%E3%81%AB%E6%B4%BB%E7%94%A8%E3%81%99%E3%82%8B%E3%81%9F%E3%82%81%E3%81%AE%E4%BD%BF%E3%81%84%E6%96%B9%E3%83%88%E3%83%AC%E3%83%BC%E3%83%8B%E3%83%B3%E3%82%B0%E3%82%BB%E3%83%83%E3%82%B7%E3%83%A7%E3%83%B3 | 2026-11-05 | 確認済（トレーニング言語）／日本語サポートは未確認 |
| 日本の物件・市場データ | 日本は提供国に含まれる（"We already serve clients in 99 countries ... including regions like Russia, South Africa, Japan"）。条件："provided there's some competition in your area that we can track"。日本での価格精度は確認できず | https://help.pricelabs.co/portal/en/kb/articles/does-pricelabs-cover-my-area | 2026-11-05 | 確認済（提供国）／精度は未確認 |
| 通貨（JPY） | 通貨はPriceLabs側で持たず、PMS／チャネル／OTAから取り込む（"PriceLabs does not store the currency of a listing."）。JPYを明示した対応表は見つからず | https://help.pricelabs.co/portal/en/kb/articles/how-to-change-the-currency-of-a-listing | 2026-11-05 | 確認済（仕組み）／JPYでの動作は未確認 |
| 請求書・インボイス | 請求書はPDF／CSVで取得でき、会社名・住所・税IDを請求書に載せる設定あり。日本の適格請求書（インボイス制度）への対応は確認できず | https://help.pricelabs.co/portal/en/kb/articles/updating-billing-information ／ https://help.pricelabs.co/portal/en/kb/articles/billing | 2026-11-05 | 確認済（PDF／CSV）／インボイス制度は未確認 |
| 住宅宿泊事業法（届出番号、年間180日上限など） | 関連機能は見つからない | － | 2026-11-05 | 未確認 |
| 宿泊者名簿・パスポート確認 | 該当なし（価格ツール） | － | 2026-11-05 | 未確認 |

## 6. アフィリエイト

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| 有無・種別 | あり。(a) Ambassadors Program（アフィリエイト型。PriceLabs利用者でなくても可）、(b) 利用者向け紹介プログラム（Referral） | https://hello.pricelabs.co/ambassadors/ ／ https://hello.pricelabs.co/referral/ | 2026-11-05 | 確認済 |
| 申込URL | Googleフォーム（審査あり）：https://docs.google.com/forms/d/e/1FAIpQLScyeC7WWmLj6J8jAEERyJ5zP7YShhO-JA9RvypwYpdI5PpdZw/viewform 。事前に無料のPriceLabsアカウント作成が必要。問い合わせ：ambassadors@pricelabs.co | https://hello.pricelabs.co/ambassadors/ | 2026-11-05 | 確認済（フォームの中身は未確認） |
| 報酬（Ambassadors） | 紹介した顧客の最初の12回のDynamic Pricing請求書の10％。支払いはPriceLabsクレジット。PriceLabs利用者は超過分が50ドル超なら四半期末にPayPal／銀行へ現金化を依頼可。非利用者は四半期ごとにPayPal／銀行へ（現金化） | https://hello.pricelabs.co/ambassadors/ | 2026-11-05 | 確認済 |
| 報酬（利用者向けReferral） | 紹介者・被紹介者の双方にPriceLabsクレジット USD 10（被紹介者が最初の有料請求を払ったとき） | https://hello.pricelabs.co/referral/ | 2026-11-05 | 確認済 |
| 被紹介者の特典 | 30日間の無料トライアル、Market Dashboard 1枠、Revenue Estimator 2回分、USD 10クレジット（リスティング接続後） | https://hello.pricelabs.co/ambassadors/ | 2026-11-05 | 確認済 |
| 対象・条件 | 新規アカウントのみ（既存アカウントは対象外）。Dynamic Pricingの購入のみが対象。被紹介者が登録フォームの「Referral Code」欄にコードを入れる必要あり。無料トライアルがあるため、クレジット反映は最大2か月かかることがある。承認後の紹介から10％が適用 | https://hello.pricelabs.co/ambassadors/ | 2026-11-05 | 確認済 |
| 規約上の制限（ブランド名の入札禁止、コンテンツ制限など） | 専用の規約ページ・規約文書は見つからなかった。ブランド名入札やコンテンツ制限の記載は、開いた範囲（アンバサダーページ、リファラルページ、利用規約）には無い。承認後にメールで詳細が送られると案内されており、その内容は未取得 | https://hello.pricelabs.co/ambassadors/ ／ https://pricelabs.co/tandc/ | 2026-11-05 | 未確認 |

## 7. 乗り換え

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| 取り込み方法 | アカウント作成後、Airbnb／Booking.com／Vrbo、またはPMS（連携一覧）からリスティングをインポート。公開中で予約可能な状態であること。"Add/Reconnect Listings" で再接続 | https://help.pricelabs.co/portal/en/kb/articles/getting-started ／ https://help.pricelabs.co/portal/en/kb/articles/how-to-integrate-pricelabs-with-airbnb-official-airbnb-integration | 2026-11-05 | 確認済 |
| 他社の価格ツールからの移行ガイド・データ移行支援 | 探していない／見つかっていない | － | 2026-11-05 | 未確認 |
| 他社の価格ツールとの併用 | Airbnb側のSmart Pricingはオフにする必要あり。AirbnbのPricing Tipsで設定した価格は同期で上書きされる | https://help.pricelabs.co/portal/en/kb/articles/how-to-integrate-pricelabs-with-airbnb-official-airbnb-integration | 2026-11-05 | 確認済 |
| PriceLabsをやめるとき | 最後に送った料金・最低宿泊はPMS／チャネル側に残る（上の「解約・停止の条件」参照） | https://help.pricelabs.co/portal/en/kb/articles/pausing-your-subscription | 2026-11-05 | 確認済 |

## 8. 注意すべき点（出典付き）

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| PMSを使う場合は、Airbnbに直接つながない | PMS／チャネルマネージャーを使っているなら、PriceLabsはPMSと連携する（Airbnb・Booking.com・Vrbo共通の案内）。VrboがすでにPMSとつながっている場合は、PMSをPriceLabsにつなぐよう案内 | https://help.pricelabs.co/portal/en/kb/articles/how-to-integrate-pricelabs-with-airbnb-official-airbnb-integration ／ https://help.pricelabs.co/portal/en/kb/articles/vrbo | 2026-11-05 | 確認済 |
| 価格を送れる先の期間 | Airbnb 540日、Vrbo 365日、Booking.com 標準1年（依頼で720日）。Hostfully 720日 | 各連携記事（上記） | 2026-11-05 | 確認済 |
| 売上連動プランの縛り | 1年間は定額プランに戻れない | https://help.pricelabs.co/portal/en/kb/articles/billing | 2026-11-05 | 確認済 |
| 同じ物件の二重課金 | PMSとAirbnb等の両方からインポートした同一物件は、紐づけないと別々に課金される | https://help.pricelabs.co/portal/en/kb/articles/billing | 2026-11-05 | 確認済 |
| 利用者の不満（返金・サポート・同期） | Trustpilotに、解約後に請求されたが返金されなかった、同期に30分かかった、マークアップが反映されないという投稿があるとの要約。BiggerPocketsに「Airbnb接続が足りず再同期できない」との投稿。いずれも個別の投稿で、件数・時期・真偽は未確認。ページ自体は開いていない | https://ca.trustpilot.com/review/pricelabs.co ／ https://www.biggerpockets.com/forums/530/topics/1049086-pricelabs-connection-problems | 2026-11-05 | 第三者のみ（検索結果の要約のみ） |
| 評価の高い側の声 | Capterra等でサポートを称賛する投稿が多いとの要約（個別の確認はしていない） | https://capterra.com/p/158348/PriceLabs/reviews/ | 2026-11-05 | 第三者のみ |
| 同期の制限 | 物件数が多いと予約サイト側のレート制限で同期が失敗することがある、と公式ヘルプが説明 | https://help.pricelabs.co/portal/en/kb/articles/pricelabs-airbnb-integration | 2026-11-05 | 未確認（検索結果の要約のみ。公式記事の本文は開いていない） |

## 調べられなかったこと

- 公式の料金計算機の結果（件数別の正確な月額）。上の件数別目安は、単価表からの当方の計算値。
- Performance／Expansion バンドルの価格。Listing Optimizer の価格。
- 日本円（JPY）での請求の可否、日本の適格請求書（インボイス制度）への対応。
- 管理画面（アプリ）の日本語対応。日本語でのサポート可否と対応時間。
- 日本の市場データの精度・カバー範囲（提供国に入っていることまでは確認）。
- 楽天トラベル・じゃらん・Agodaへの価格反映（サイトコントローラー経由の可否）。
- 住宅宿泊事業法（年間180日上限など）に関連する機能の有無。
- Ambassadors Program の規約全文（ブランド名入札、コンテンツ制限）。承認後にメールで届く詳細は未取得。
- 他社の価格ツールからの移行ガイドの有無（調べていない）。
- 利用者の不満の裏取り（Trustpilot・BiggerPocketsのページ本体を開いていない）。
- ログインが必要な範囲（アプリ内の設定画面、請求画面）はすべて未確認。
