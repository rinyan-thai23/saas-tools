# 事実カード：OwnerRez

- 取得日：2026-11-05（すべての行）
- 調査の前提：
  - 公式サイト `www.ownerrez.com` の料金ページ・サポート記事（Costs & Fees、Affiliate Program、チャネル・文化設定など）・連携一覧・利用規約はcurlで開けた（HTTP 200）。ただし料金ページの物件数スライダーはJavaScriptで、初期表示は5物件（$88）だけ。物件数別の表は「Costs & Fees」記事の静的な表から取った。
  - 「物件数別の目安」のうち5室・10室・20室などの合計額は、公式の料金表から私が計算した値（計算と明記）。公式ページに合計額として書かれているのは5室の$88のみ。
  - アフィリエイトの正式な規約（Affiliate Program Terms & Conditions）は、アプリ内のログイン後の画面で表示される。ログインできないため本文は開けていない。公式サポート記事の要約までを確認。
- 確度の凡例：`確認済`＝公式ページを開いて確認／`第三者のみ`＝公式を開けず第三者情報のみ／`未確認`

## 1. 基本

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| 運営会社 | OwnerRez, Inc.（米国。フッターの電話番号は(206)市外局番。利用規約の準拠法はワイオミング州法）。規約は英語版が優先 | https://www.ownerrez.com/support/articles/privacy-security-terms-of-service | 2026-11-05 | 確認済 |
| 対象規模 | 「Available to both small homeowners and large PMs alike」。1物件から数百物件までの料金表（200+まで） | https://www.ownerrez.com/vacation-rental-channel-manager ／ https://www.ownerrez.com/support/articles/costs-and-fees | 2026-11-05 | 確認済 |
| 製品の位置づけ | PMS＋チャネルマネージャー（「channel management, CRM, PM, accounting, messaging and websites」）。自社は会計ソフトではないと明記（「OwnerRez is not an accounting product」） | https://www.ownerrez.com/pricing ／ https://www.ownerrez.com/integrations | 2026-11-05 | 確認済 |

## 2. 料金

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| 課金モデル | 物件数に応じた月額。物件が多いほど1物件あたりの単価が下がる。予約数は無制限、予約手数料・セットアップ費用・契約縛りなし（「Unlimited bookings • No setup fees, booking fees, or contracts • 14-day free trial」）。課金・料金表示はUSD（$） | https://www.ownerrez.com/pricing | 2026-11-05 | 確認済 |
| 最低料金 | 月$40（「The minimum fee is $40.00, even if all of your properties are disabled.」） | https://www.ownerrez.com/support/articles/costs-and-fees | 2026-11-05 | 確認済 |
| 料金表（基本料金） | 1物件目 $40（合計）／2〜3物件目 各$15／4物件目 $10／5〜9物件目 各$8／10〜19物件目 各$7／20〜49物件目 各$6／50〜99物件目 各$4／100〜199物件目 各$3／200物件目以降 各$2 | https://www.ownerrez.com/support/articles/costs-and-fees | 2026-11-05 | 確認済 |
| 物件数別の目安：1室 | $40/月（基本料金のみ） | 同上 | 2026-11-05 | 確認済 |
| 物件数別の目安：3室 | $70/月（計算：40＋15×2）。公式ページに合計額の記載はなし | 同上（表から計算） | 2026-11-05 | 確認済（表）／合計は計算 |
| 物件数別の目安：5室 | $88/月。料金ページの初期表示「For 5 properties: $88/month」と、表からの計算（40＋15×2＋10＋8）が一致 | https://www.ownerrez.com/pricing ／ costs-and-fees | 2026-11-05 | 確認済 |
| 物件数別の目安：10室 | $127/月（計算：40＋15×2＋10＋8×5＋7）。公式ページに合計額の記載はなし | costs-and-fees（表から計算） | 2026-11-05 | 確認済（表）／合計は計算 |
| 物件数別の目安：20室 | $196/月（計算：10室までの合計127＋10〜19物件目の9室分7×9=63→19室で190＋20室目6）。公式ページに合計額の記載はなし | costs-and-fees（表から計算） | 2026-11-05 | 確認済（表）／合計は計算 |
| 基本料金に含まれるもの | 「Everything but the Premium Features is included」。チャネル管理（Airbnb・Vrbo・Booking.com・Google Vacation Rentals等）、チームのログイン無制限とオーナー／清掃スタッフ用ポータル、電子署名、トリガー、自動返信など | https://www.ownerrez.com/pricing | 2026-11-05 | 確認済 |
| プレミアム機能（物件数に応じた別料金） | Property Management（1物件目$10／2物件目$5／3〜9物件目各$3／10〜19各$2／20〜199各$1）、QuickBooks連携（1物件目$10／2物件目$5／3〜199各$1）、Hosted Sites（1物件目$15／2物件目$5／3〜9各$3／10〜19各$2／20〜199各$1）、WordPress Plugin＋Integrated Sites（QuickBooksと同じ表）、SMS（番号1つ$15/月、送信500セグメントまで込み、以降1.5¢）、Rezzy AI（1物件$9/月）。電子署名とチャネル管理は無料 | https://www.ownerrez.com/support/articles/costs-and-fees | 2026-11-05 | 確認済 |
| ドアロック直接連携の別料金 | Schlage／Igloohome／Hubitat：1台あたり月$4 | 同上 | 2026-11-05 | 確認済 |
| 損害保護（RentalGuardian経由） | 補償額別の月額（例：$500で$13、$1,500で$27、$3,000で$45、$5,000で$69 ほか）。トライアル中も有料。アカウント内の全物件・全予約を対象にする必要があり、選択的な適用は不可 | 同上 | 2026-11-05 | 確認済 |
| 無料トライアル | 14日間（「during which all activity is free」。プレミアム機能も期間中は無料、継続して有効なら終了後に請求）。損害保護のみトライアル中も有料 | https://www.ownerrez.com/pricing ／ costs-and-fees | 2026-11-05 | 確認済 |
| 契約縛り | なし（「Is there a contract or minimum term required? Of course not!」「We don't impose contracts or early termination fees」） | https://www.ownerrez.com/pricing ／ https://www.ownerrez.com/support/articles/closing-your-account | 2026-11-05 | 確認済 |
| 解約条件 | いつでもアカウントを閉鎖可能。請求サイクル終了まで利用可。未使用期間の返金なし（「OwnerRez does not issue refunds for any unused time」「As a subscription service, OwnerRez does not offer refunds.」）。閉鎖時に決済・チャネル連携・サイト・オーナーポータル等が停止し、SMS番号は解放され復元不可。データは保持され、多くの場合アカウントの再開は可能（手作業が必要） | https://www.ownerrez.com/support/articles/closing-your-account ／ https://www.ownerrez.com/support/articles/refund-policy | 2026-11-05 | 確認済 |
| 追加手数料（ダイレクト予約手数料など） | 「No commissions, no guest fees, or per-booking fees.」決済手数料はStripe等の決済事業者側に別途発生 | https://www.ownerrez.com/pricing | 2026-11-05 | 確認済 |
| 支払い方法（利用者→OwnerRez） | クレジットカード必須（Visa・Mastercard・Discover・American Express）。小切手その他は不可、ACHは「plan to add」 | https://www.ownerrez.com/pricing | 2026-11-05 | 確認済 |
| 税 | 米国の一部の州の利用者にだけ売上税を請求。米国外の請求先は対象外 | https://www.ownerrez.com/support/articles/costs-and-fees | 2026-11-05 | 確認済 |

## 3. チャネル（予約サイト連携）

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| 接続方式 | 「Direct API integrations with leading channels like Vrbo, Airbnb, Booking.com, and Google Vacation Rentals.」第三者のチャネルマネージャーを介さない直接連携。iCalはAPI連携の代替ではなく、API連携がない場合に限る（「iCal calendar syncs are not a supported alternative for OwnerRez channel integrations, and they must never run alongside a channel connection for the same channel」） | https://www.ownerrez.com/pricing ／ https://www.ownerrez.com/support/articles/channel-management-calendar-import-export | 2026-11-05 | 確認済 |
| Airbnb | API連携（連携一覧に記載） | https://www.ownerrez.com/integrations | 2026-11-05 | 確認済 |
| Booking.com | API連携。法人識別子（LEID）の設定が必要と記載 | https://www.ownerrez.com/integrations ／ https://www.ownerrez.com/support/articles/channel-management-api-integrations-booking-com-setup-connecting | 2026-11-05 | 確認済 |
| Vrbo | API連携。公式サイトに「OwnerRez is part of a select group of channel partners awarded “elite” status by the channels」との自己申告あり | https://www.ownerrez.com/integrations ／ https://www.ownerrez.com/vacation-rental-channel-manager | 2026-11-05 | 確認済 |
| Expedia | 連携一覧のチャネルに独立した記載なし（Vrbo連携の「Auto-populated Expedia URLs」の記事はあるがExpedia本体への連携ではない） | https://www.ownerrez.com/integrations | 2026-11-05 | 未確認（記載なし） |
| Agoda | 連携一覧に記載なし | https://www.ownerrez.com/integrations | 2026-11-05 | 未確認（記載なし） |
| 楽天トラベル | 連携一覧・サイト全体のサイトマップに記載なし | https://www.ownerrez.com/integrations ／ https://www.ownerrez.com/sitemap.xml | 2026-11-05 | 未確認（記載なし） |
| じゃらん | 連携一覧・サイトマップに記載なし | 同上 | 2026-11-05 | 未確認（記載なし） |
| その他のチャネル（連携一覧のChannel Integrations） | Google Vacation Rentals、Hopper（Capital One含む）、HomeToGo、Houfy、Savvy、Florida Rentals、Find Rentals、GuestsMiles、GetawayGogo、GoLightly、ECBYO、Rentalz、Whimstay、Glamping Hub、Lake.com、Homes & Villas by Marriott Bonvoy、Tripskip ほか多数（米国中心） | https://www.ownerrez.com/integrations | 2026-11-05 | 確認済 |
| iCal | 全チャネルでiCalの取り込み／書き出しが可能（「Almost all vacation rental channels ... support iCal」）。ただしAPI連携のあるチャネルとは併用不可。全物件×全チャネルで取り込みと書き出しを両方設定する運用 | https://www.ownerrez.com/support/articles/channel-management-calendar-import-export | 2026-11-05 | 確認済 |
| Channel Bridge | OwnerRez独自のブラウザ拡張。API連携で取れない情報を取得する補助ツール | https://www.ownerrez.com/vacation-rental-channel-manager | 2026-11-05 | 確認済 |

## 4. 機能

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| 自動メッセージ | トリガー・自動返信が基本料金に含まれる（「even things like triggers, digital signatures, auto-responders」）。SMSは有料の別機能。Rezzy AIは有料（1物件$9/月）で、ゲスト対応のAI返信とタスク作成を行うとの説明 | https://www.ownerrez.com/pricing ／ costs-and-fees | 2026-11-05 | 確認済 |
| カレンダー同期（二重予約防止） | チャネルマネージャーが可用性・料金・コンテンツを各チャネルへ同期（「Instead of updating each one manually ... you can make changes in OwnerRez」）。二重予約防止の精度の検証はなし | https://www.ownerrez.com/support/articles/channel-management-overview | 2026-11-05 | 確認済（記載の確認のみ） |
| 清掃タスク | 清掃スタッフ用のポータルが基本料金に含まれる（「portal site for owners and cleaners」）。Rezzy AIがタスクを自動作成する説明あり。連携先：Turno、Breezeway、Operto Teams、ResortCleaning、TIDY ほか12件ほど。社内の清掃タスク機能の詳細は未確認 | https://www.ownerrez.com/pricing ／ https://www.ownerrez.com/integrations | 2026-11-05 | 確認済（社内タスク機能の詳細は未確認） |
| スマートロック連携先 | 直接連携：Schlage、Igloohome、Hubitat（各$4/台/月）。そのほか連携一覧：PointCentral、Kaba、eRentalLock、RemoteLock、Brivo、Jervis Systems、Lynx、i-Checkin、CodeBox、GuestsKey。Akerun・SESAMEなど日本のロックの記載なし | https://www.ownerrez.com/integrations ／ costs-and-fees | 2026-11-05 | 確認済（日本のロックは記載なし＝未確認） |
| 価格ツール連携 | PriceLabs、Beyond Pricing、DPGO、RankBreeze、RateGenie、Rented、Wheelhouse、RevMax | https://www.ownerrez.com/integrations | 2026-11-05 | 確認済 |
| オーナーポータル | 基本料金に含まれる（「portal site for owners and cleaners」）。オーナー精算・手数料計算はプレミアム機能のProperty Management | https://www.ownerrez.com/pricing | 2026-11-05 | 確認済 |
| ダイレクト予約サイト | Hosted Sites（プレミアム、独自ドメイン可）、WordPress Plugin＋Integrated Sites（プレミアム）、予約ウィジェット（基本料金内）。Stripe・PayPalなど多数の決済事業者に対応 | https://www.ownerrez.com/pricing ／ https://www.ownerrez.com/integrations | 2026-11-05 | 確認済 |
| 会計 | QuickBooks Online連携（プレミアム）。連携一覧のAccounting：Accountable、Clearing、VRPlatform、Owner Center、TopKey、Avalara、PX Accounting。freee・マネーフォワード等は記載なし | https://www.ownerrez.com/integrations ／ costs-and-fees | 2026-11-05 | 確認済 |
| 外部AI連携 | Claude／ChatGPT（MCP）の機能ページあり（内容は未確認） | https://www.ownerrez.com/pricing（メニュー表示） | 2026-11-05 | 確認済（表示の存在のみ） |

## 5. 日本対応

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| UIの日本語 | 公式サポート記事によれば、アカウントの表示言語（Culture）は「English only to eleven languages, including Spanish, French, Dutch, German, Portuguese, Italian, Greek, Danish, Finnish, Swedish, or English」。日本語は挙がっていない | https://www.ownerrez.com/support/articles/guests-multi-language-guest-forms | 2026-11-05 | 確認済（記事に日本語の記載なし） |
| ゲスト向けメッセージ・フォームの日本語 | ゲストフォーム（レビュー、旅行保険、公開予約リンク、Googleのグローバルランディングページ）は、ゲストの希望言語に自動翻訳される（Airbnb／Booking.com／Marriott Bonvoy／Vrboが希望言語を共有した場合）。対応言語の一覧に日本語があるかは記事から不明。それ以外のメッセージは、言語タグ＋翻訳済みの文面をトリガーで送る運用（手作業）。 | https://www.ownerrez.com/support/articles/guests-multi-language-guest-forms ／ https://www.ownerrez.com/support/articles/language-tags | 2026-11-05 | 確認済（日本語の可否は未確認） |
| サポート言語と対応時間 | サポートはメール（help@ownerrez.com）、問い合わせフォーム、アプリ内チケットの3経路。「We may not respond immediately」と記載。対応時間・対応言語は公式に記載なし。フッターに電話番号(206) 651-4090あり（サポート記事の3経路には電話は含まれない）。英語以外のサポート可否は未確認 | https://www.ownerrez.com/support/articles/my-account-ask-for-help | 2026-11-05 | 確認済（時間・言語は未確認） |
| 通貨（JPY） | 公式の説明：1物件に設定できる通貨は1つで、決済事業者も同じ通貨である必要がある。通貨換算はしない（フォーラムでOwnerRez社員が回答、2023年）。ゲスト向けの通貨はGuest Cultureで設定。Stripeの対応通貨は「Stripe supports these currencies」とStripeの一覧へのリンクのみで、JPYの明記はなし。OwnerRezでJPY運用が可能かは公式に確認できず | https://www.ownerrez.com/forums/general-help/booking-page-show-prices-in-other-currency ／ https://www.ownerrez.com/support/articles/guest-culture ／ https://www.ownerrez.com/support/articles/payment-processing-gateways-stripe | 2026-11-05 | 未確認 |
| 決済手段 | Stripe、PayPal、Worldline、Authorize.net、PowerTranz、Ascent、Lynnbrook、VRP/Yapstone、Clearview ほか。Stripeの事業所・銀行所在地の要件は「following locations」へのリンクのみ（日本を含むかはこの記事内で未確認）。日本のコンビニ決済などの記載なし | https://www.ownerrez.com/integrations ／ https://www.ownerrez.com/support/articles/payment-processing-gateways-stripe | 2026-11-05 | 確認済（日本での利用可否は未確認） |
| 請求書・インボイス | 日本のインボイス制度（適格請求書）への対応の記載なし。OwnerRez自身の請求は米ドル・カード払い | https://www.ownerrez.com/pricing | 2026-11-05 | 未確認 |
| 宿泊者名簿・パスポート確認 | 本体機能としての記載は確認できず。連携一覧のGuest Communicationに Chekin、Authenticate、Check-in Scan、Happy Guest ほか。日本の宿泊者名簿の様式への対応は記載なし | https://www.ownerrez.com/integrations | 2026-11-05 | 未確認 |
| 住宅宿泊事業法に関する機能（届出番号表示など） | 公式ページに記載なし | — | 2026-11-05 | 未確認 |
| 日本向け情報の有無 | サイトマップ（約7,900URL）とサポート記事に「japan／JPY／rakuten／jalan」を含むページを確認できず（フォーラム投稿・ブログ全体は本文を未検索） | https://www.ownerrez.com/sitemap.xml | 2026-11-05 | 確認済（URLの範囲のみ） |

## 6. アフィリエイト

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| 有無・種別 | あり。自社プログラム（OwnerRez内の機能）。PartnerStackやImpact等の外部ネットワークの記載なし | https://www.ownerrez.com/support/articles/affiliate-program | 2026-11-05 | 確認済 |
| 申込方法 | OwnerRezのアカウントが必要。アプリ右上のプロフィールメニュー→Affiliate Programで規約に同意して登録（アカウントがなければ先にサインアップ）。公開の申込URLはなし。 | 同上 | 2026-11-05 | 確認済 |
| 報酬 | 紹介先が毎月支払う利用料金の割合：1年目30%／2年目20%／3〜5年目10%／5年経過後0%。アドオンや特別料金は対象外（「Special fees for add-ons or other services are not eligible」）。基本料金（月額利用料）が対象 | 同上 | 2026-11-05 | 確認済 |
| 支払い | PayPalで月1回まで、残高が$100以上で支払い。税務書類が必要（米国は署名済みW-9、米国と法的関係がない人は「その旨の声明＋国の身分証のコピー」）。米国居住者には1099 | 同上 | 2026-11-05 | 確認済 |
| 主な条件 | 自分のアカウントが有効で良好な状態であること。紹介先は新規のみ。OwnerRezの商標・著作権を守ること、「You may not represent yourself as an official representative of OwnerRez or use misleading advertising to redirect referrals」。従業員・広告パートナー・別契約で報酬を受ける人は不可 | 同上 | 2026-11-05 | 確認済 |
| ブランド名の入札禁止・コンテンツ制限 | 上記の「公式代表を名乗らない」「誤解を招く広告をしない」以外の具体的な制限（検索広告のブランドキーワード入札など）は、サポート記事に記載なし。正式な規約本文（アプリ内）は未取得 | 同上 | 2026-11-05 | 未確認 |
| クッキー期間 | 記載なし。紹介コード（Affiliate Code）またはリンクで追跡 | 同上 | 2026-11-05 | 未確認 |
| 報酬が通貨・国で変わるか／日本からの参加可否 | 米国外の人向けの税務書類の扱いは記載あり（上記）。日本在住者の参加可否・日本の源泉の扱いは未確認 | 同上 | 2026-11-05 | 未確認 |

## 7. 乗り換え

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| データ移行の支援 | 14日トライアルに無料の1時間「Jumpstart」通話が付く（セットアップ手順の説明・質問対応）。他社からのデータ移行を代行するとの記載はなし。セルフオンボーディング用のチェックリストと動画、週次のライブデモあり | https://www.ownerrez.com/onboarding ／ https://www.ownerrez.com/support/articles/jumpstart | 2026-11-05 | 確認済 |
| 追加の支援 | 有料の外部パートナー「Certified Advisors」を紹介（設定代行など。料金は未確認） | https://www.ownerrez.com/support/articles/jumpstart ／ https://www.ownerrez.com/certified-advisors | 2026-11-05 | 確認済（料金は未確認） |
| インポート方法 | ①Excelテンプレートでの一括取り込み（Import Bookings／Charges／Payments／Refunds、Tools > Import/Export）。②Airbnb・Vrbo等の予約はChannel Bridge、iCal、チャネル連携で取り込み。③Airbnbの掲載情報（写真・説明・設備）の1回限りのインポート | https://www.ownerrez.com/support/articles/importing-outside-bookings ／ https://www.ownerrez.com/support/articles/listing-content-importing-from-airbnb | 2026-11-05 | 確認済 |
| 他ツールからの移行ガイド | 特定製品（Lodgify等）専用の移行ガイドは確認できず。Streamline／LiveRez／LMPM／VRM利用者向けの乗り換え訴求ページあり（「Seamless Onboarding」）。比較ページに「OwnerRez vs Lodgify」あり（本文未取得） | https://www.ownerrez.com/streamline-alternative-forced-migration ／ https://www.ownerrez.com/ownerrez-vs-competitors | 2026-11-05 | 確認済（Lodgify専用ガイドは未確認） |

## 8. 注意すべき点

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| 日本向けの機能が見当たらない | UI・ゲスト向け言語の一覧に日本語がなく、楽天トラベル・じゃらん・Agoda・Expediaの連携記載もない。チャネルは北米・欧州向けが中心 | https://www.ownerrez.com/support/articles/guests-multi-language-guest-forms ／ https://www.ownerrez.com/integrations | 2026-11-05 | 確認済（記載がないという事実） |
| 機能の学習コスト | 公式サイトに載る利用者レビューのタイトルに「Great Software, Steep Learning Curve」（"There is definitely an initial learning curve with how deep the settings go"という別の投稿もある）。第三者レビューの要約でも同様の指摘 | https://www.ownerrez.com/vacation-rental-channel-manager | 2026-11-05 | 確認済（公式サイト上のレビュー） |
| サポートの応答 | 第三者レビューに、メールの返信が遅い・24時間対応ではないとの指摘が少数あり。公式はサポート記事で「We may not respond immediately」と記載。多数のレビューは高評価 | https://www.ownerrez.com/support/articles/my-account-ask-for-help ／ 検索結果上の https://www.capterra.com/p/100831/OwnerRez/reviews/?page=2 | 2026-11-05 | 第三者のみ（Capterra等は未開封） |
| 返金なし・カード必須 | 返金なし（未使用期間も）。支払いはクレジットカードのみ | https://www.ownerrez.com/support/articles/refund-policy ／ https://www.ownerrez.com/pricing | 2026-11-05 | 確認済 |
| 損害保護は全物件に適用が必須 | 有効にするとアカウント内の全物件・全予約が対象で、案件ごとの除外は不可。トライアル中も課金 | https://www.ownerrez.com/support/articles/costs-and-fees | 2026-11-05 | 確認済 |
| 通貨の制約 | 1物件につき通貨は1つ。OwnerRezは通貨換算を行わない（社員の回答、2023年） | https://www.ownerrez.com/forums/general-help/booking-page-show-prices-in-other-currency | 2026-11-05 | 確認済（古い投稿） |
| iCalとAPI連携の併用不可 | 同じチャネルでAPI連携とiCalを併用してはならない。国内サイト（iCalのみの運用になる場合）は、全物件×全サイトで取り込みと書き出しの設定が必要で、物件が多いと手間が増える | https://www.ownerrez.com/support/articles/channel-management-calendar-import-export | 2026-11-05 | 確認済 |
| 機能の追加課金 | 基本料金のほか、Hosted Sites・Property Management・SMS・Rezzy AI・QuickBooks・ロック連携などが別料金。必要な機能を足すと上記の目安額より高くなる | https://www.ownerrez.com/support/articles/costs-and-fees | 2026-11-05 | 確認済 |

## 調べられなかったこと

- アフィリエイトの正式な規約本文（アプリ内のログイン後のみ）。ブランド名の入札禁止・コンテンツ制限・クッキー期間は未確認。日本在住者の参加可否・税務の扱いも未確認。
- 日本語のUI・サポート・ゲスト向け言語（ゲストフォームの対応言語の完全な一覧）。サポートの対応時間と対応言語。
- JPYでの価格設定・決済（OwnerRezでの運用可否）、日本でのStripe・PayPalの利用可否の実測。
- 楽天トラベル・じゃらん・Agoda・Expediaとの連携（公式の連携としては記載なし。iCalでの運用可否は未検証）。
- 日本のインボイス制度、宿泊者名簿・パスポート確認、住宅宿泊事業法（届出番号、宿泊日数の上限管理など）に関する機能。
- Akerun・SESAMEなど日本のスマートロックとの連携（記載なし）。
- 清掃タスク機能（社内側）の詳細、Claude／ChatGPT（MCP）連携の内容、Certified Advisorsの料金、「OwnerRez vs Lodgify」比較ページの本文。
- 利用者の不満の一次情報（Capterra・GetApp・Software Advice等のページ自体は開いていない。公式サイト上のレビューのみ確認）。
- 他社（Lodgifyなど）からのデータ移行の代行の有無（記載なし）。
