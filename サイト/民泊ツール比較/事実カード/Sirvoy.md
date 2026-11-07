# 事実カード：Sirvoy（小規模宿泊の予約・管理システム）

- 取得日：2026-11-05（すべての行）
- 製品の種類：PMS（予約管理）＋チャネルマネージャー＋予約エンジン＋簡易ウェブサイト作成。ホテル・B&B・ホステル・グランピング・バケーションレンタル・長期賃貸向け。公式サイト：https://sirvoy.com/
- 取得方法のメモ：料金ページの金額は、ページ内のデータ（JSON）と計算スクリプトを読んで確認した。ヘルプセンター（help.sirvoy.com）は記事を直接開いた。アフィリエイト申込フォームは動的描画のため、フォーム自体は開けていない。
- 確度の凡例：確認済＝公式ページ・公式ヘルプを開いて確認／第三者のみ／未確認

## 1. 基本

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| 運営会社 | Sirvoy Limited（アイルランド共和国で登記）。所在地：1/2 Marino Mart, Fairview, Dublin, Ireland | https://sirvoy.com/terms-conditions ／ https://help.sirvoy.com/en_US/sirvoy-general/-contact-customer-support | 2026-11-05 | 確認済 |
| 対象規模 | 1室〜（料金計算機は最大1,500室）。Freeは1室のみ | https://sirvoy.com/pricing | 2026-11-05 | 確認済 |
| 利用国 | "Sirvoy is available worldwide in over 110 countries."（FAQ） | https://sirvoy.com/llms-full.txt | 2026-11-05 | 確認済（自社の記載） |

## 2. 料金

料金は「部屋数」と「プラン」で決まる。部屋数は階段式（1〜2室、3〜5室、6〜10室、11〜20室、21〜50室…）。バケーションレンタルは「1戸＝1室」として数える形（"Or apartments, campsites, etc."）。ホステルのドミトリーはベッド4つで1室。

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| プラン | Free（1室。無料のウェブサイトと予約エンジン、自動メール、予約・料金・部屋の管理）／Starter（請求書・簡易会計、自動SMS、カスタムメール／SMSテンプレート）／Pro（Starterの全機能＋チャネルマネージャー、ゲスト履歴、チームメンバー追加） | https://sirvoy.com/pricing | 2026-11-05 | 確認済 |
| 月額（月払い・EUR）Starter／Pro | 1〜2室：12／44。3〜5室：16／59。6〜10室：22／79。11〜20室：30／109。21〜50室：42／149。51〜100室：59／199 | https://sirvoy.com/pricing（ページ内の料金データ。階段の判定式は https://sirvoy.com/_astro/pricingTiers.Ca0k2uyt.js で確認） | 2026-11-05 | 確認済 |
| 月額（月払い・USD）Starter／Pro | 1〜2室：15／54。3〜5室：20／73。6〜10室：28／98。11〜20室：38／135。21〜50室：54／185 | 同上 | 2026-11-05 | 確認済 |
| 件数別の月額目安（Starter／Pro・USD・月払い） | 1室：Free $0（Starter $15／Pro $54）。3室：$20／$73。5室：$20／$73。10室：$28／$98。20室：$38／$135 | 同上 | 2026-11-05 | 確認済（上の表を件数に当てはめた） |
| 年払い | 月払い額の12/13（"1 month free"、表示は約8％引き）。画面の例：Starter 1〜2室で €12→€11、Pro €44→€41。他の階段の年払い額はこの計算式による当方の計算で、画面では確認していない | https://sirvoy.com/pricing ／ https://sirvoy.com/_astro/pricingFormat.BsJLGwxt.js | 2026-11-05 | 確認済（計算式と例）／他の年払い額は計算値 |
| 追加：複数物件 | Pro追加オプション「Multiple property connection」：もう1物件（チャネル接続あり）につき EUR 20／月（USD 23）。Booking.comまたはExpediaの複数物件を1アカウントで管理 | https://sirvoy.com/pricing ／ https://sirvoy.com/channel-manager | 2026-11-05 | 確認済 |
| 追加：SMS | 1通あたり：Starter EUR 0.10（USD 0.15）、Pro EUR 0.06（USD 0.08）。通信費＋手数料の従量課金 | https://sirvoy.com/pricing | 2026-11-05 | 確認済 |
| 追加：Google Hotel Ads | Googleの手数料に、Sirvoyの小額の手数料が上乗せ。ヘルプによれば、追加料金が発生しうるのはSMSとGoogle Hotel Adsのみ | https://help.sirvoy.com/en_US/sirvoy-general/sirvoy-pricing-and-plans | 2026-11-05 | 確認済 |
| 予約手数料（ダイレクト予約） | 0％。"With Sirvoy, there are no written contracts, no setup fees, and no commissions."（チャネル手数料は各OTA側で別途発生） | https://sirvoy.com/pricing | 2026-11-05 | 確認済 |
| 無料トライアル | 14日間、カード不要 | https://sirvoy.com/pricing | 2026-11-05 | 確認済 |
| 契約縛り | 書面の契約なし、初期費用なし。プリペイド式の残高制：月額料金は残高から月替わり（UTC 0:00）に差し引かれる。残高がマイナスになった状態が20日超でアカウントがロックされ、60日超で削除されうる。1年分以上を入金すると月額1回分のボーナスクレジット | https://sirvoy.com/terms-conditions ／ https://help.sirvoy.com/en_US/subscription/refill-and-manage-your-sirvoy-account-balance | 2026-11-05 | 確認済 |
| 解約条件 | "No action is needed if you want to cancel or close your account. You can simply stop paying for the service." 返金：初回の支払いから14日以内の解約は返金対象（EU指令・アイルランド法に基づく14日の熟慮期間）。ただし、カード登録なしの無料トライアルを使ったことがある場合の扱いは規約に条件あり（本文は途中までしか確認していない） | https://help.sirvoy.com/en_US/subscription/how-do-i-cancel-my-subscription ／ https://sirvoy.com/terms-conditions | 2026-11-05 | 確認済（解約方法）／返金の細かい条件は未確認 |
| データの扱い | 予約データはチェックアウトから少なくとも18か月保持。解約後はエクスポート機能で取得可。顧客データは解約の1年後に削除（依頼で早期削除） | https://sirvoy.com/terms-conditions | 2026-11-05 | 確認済 |
| 請求通貨 | EUR、USD、SEK、NOK、DKK、GBP、CAD、AUD、NZD の9通貨から選択。日本円（JPY）は無い | https://sirvoy.com/pricing | 2026-11-05 | 確認済 |
| 支払い手段（ゲストからの決済） | Stripe、PayPalなど。保管した番号で後から決済（Sirvoy Vault）。日本での利用可否は確認できず | https://sirvoy.com/pricing ／ https://sirvoy.com/payment-processing | 2026-11-05 | 確認済（一般）／日本での可否は未確認 |
| Sirvoy自体への支払い手段 | カード（残高チャージ）。それ以外は確認できず | https://help.sirvoy.com/en_US/subscription/refill-and-manage-your-sirvoy-account-balance | 2026-11-05 | 確認済（カード）／他は未確認 |

## 3. チャネル

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| チャネルマネージャーのプラン | Proのみ（Free・Starterは対象外。比較表で確認）。"The Channel Manager is included in Sirvoy's Pro plan with 0% added commission" | https://sirvoy.com/pricing ／ https://sirvoy.com/llms-full.txt | 2026-11-05 | 確認済 |
| Airbnb | 直接連携。「予約・空室を双方向でリアルタイム同期」と記載。公式パートナー認定かどうかの記載は確認できず | https://sirvoy.com/channel-manager/airbnb ／ https://sirvoy.com/integrations | 2026-11-05 | 確認済（連携あり）／認定の有無は未確認 |
| Booking.com | 直接連携（Pro）。Booking.comの予約は連携時に自動で取り込まれる | https://sirvoy.com/integrations ／ https://help.sirvoy.com/en_US/import-bookings/import-your-existing-bookings | 2026-11-05 | 確認済 |
| Expedia／Hotels.com | 直接連携（Pro）。連携ページの文は Expedia に "partner sites like Hotels.com and Vrbo" を含むとあるが、Vrbo は別に iCal 双方向同期として掲載されており、記載に揺れがある | https://sirvoy.com/integrations | 2026-11-05 | 確認済（Expedia・Hotels.com）／Vrboの接続方式は揺れ |
| Vrbo | iCalの双方向同期（"two-way iCal sync"）。API連携ではない（Proの "iCal import/export" で利用） | https://sirvoy.com/integrations ／ https://sirvoy.com/pricing | 2026-11-05 | 確認済 |
| Agoda | 直接連携（"Reach a global audience, especially in Asia"） | https://sirvoy.com/integrations | 2026-11-05 | 確認済 |
| 楽天トラベル／じゃらん | Sirvoyの料金・連携・チャネルマネージャー・FAQの各ページ（公式の全文テキストを含む）に、楽天・じゃらん・日本のOTAの記載なし | https://sirvoy.com/integrations ／ https://sirvoy.com/channel-manager ／ https://sirvoy.com/llms-full.txt | 2026-11-05 | 確認済（記載が無いこと） |
| その他 | Hostelworld、Google Hotel Ads、SiteMinder（"450+ additional channels" へ接続）、BookVisit。iCal連携：Wimdu、Holiday Lettings、Only-Apartments、Glamping Hubなど（一方向のものは予約がSirvoyに自動で入らない場合あり）。SiteMinder経由での楽天・じゃらんの可否は未確認 | https://sirvoy.com/integrations | 2026-11-05 | 確認済（掲載）／SiteMinder経由の日本OTAは未確認 |
| 二重予約対策 | 連携チャネル間で空室をリアルタイムに閉じる（"a room booked on one site is immediately closed everywhere else"）。iCal連携の同期間隔・遅延の記載は確認できず | https://sirvoy.com/channel-manager | 2026-11-05 | 確認済（記載）／iCalの同期間隔は未確認 |

## 4. 機能

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| 自動メッセージ | 予約・チェックイン・チェックアウト等のトリガーで自動メール（Free／Starter／Pro全て○）。カスタムのメール／SMSテンプレートはStarterとPro（Freeは×）。SMSは従量課金 | https://sirvoy.com/pricing | 2026-11-05 | 確認済 |
| カレンダー同期 | 上記「二重予約対策」。カレンダー一覧、複数室・分割予約（全プラン） | https://sirvoy.com/pricing | 2026-11-05 | 確認済 |
| 清掃タスク | "Cleaning & housekeeping scheduling"（全プラン○） | https://sirvoy.com/pricing | 2026-11-05 | 確認済 |
| スマートロック連携先 | Telkey、WeAccess、Locky、Invite（Inviteは双方向ではなく予約情報のエクスポート利用） | https://sirvoy.com/integrations | 2026-11-05 | 確認済 |
| 価格ツール連携 | 連携ページ・全文テキストに PriceLabs・Wheelhouse・Beyond などの記載なし。Sirvoy自体にレートマネージャー（手動調整・派生料金）あり。Webhook（Callback URL：StarterとFreeは×、Proは○）、Zapier／Make（一方向）あり。APIの範囲は未確認 | https://sirvoy.com/integrations ／ https://sirvoy.com/pricing | 2026-11-05 | 確認済（記載が無いこと）／APIの範囲は未確認 |
| オーナーポータル | 記載なし（オーナー向けの閲覧・精算機能は確認できず） | https://sirvoy.com/pricing | 2026-11-05 | 未確認 |
| ダイレクト予約サイト | 予約エンジン（手数料0％、全プラン）。簡易な1ページのウェブサイトビルダー、WordPressプラグイン。カスタムドメインはStarterとPro（Freeは×）。ゲストポータル（残金支払い・カード更新・キャンセル） | https://sirvoy.com/pricing ／ https://sirvoy.com/llms-full.txt | 2026-11-05 | 確認済 |
| 会計 | 請求書・領収書の発行（StarterとPro）、Peppol電子請求書（Proのみ）、Fortnox（スウェーデンの会計ソフト）連携。日本の会計ソフトとの連携は確認できず | https://sirvoy.com/pricing ／ https://sirvoy.com/integrations | 2026-11-05 | 確認済 |
| 統計・その他 | 稼働率・売上などのレポート（全プラン）、ゲスト履歴・好み・要注意ゲストの登録（Pro）、複数ユーザー（Proで最大50ログイン） | https://sirvoy.com/pricing | 2026-11-05 | 確認済 |

## 5. 日本対応

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| 管理画面・公式サイトのUI言語 | 英語、スウェーデン語、スペイン語、フィンランド語、ノルウェー語、デンマーク語、ドイツ語、フランス語、オランダ語の9言語。日本語なし。ヘルプセンターも同じ9言語 | https://sirvoy.com/pricing ／ https://help.sirvoy.com/en_US | 2026-11-05 | 確認済 |
| ゲスト向け予約エンジンの日本語 | 予約エンジンの画面は最大31言語に対応。日本語（日本語）、韓国語、中国語（簡体・繁体）が一覧にある。ゲストのブラウザ設定に合わせて切り替わる。部屋タイプと追加オプションの説明文は、言語ごとに自分で入力する必要がある | https://help.sirvoy.com/en_US/adjusting-the-booking-engine/support-up-to-31-languages-in-booking-engine | 2026-11-05 | 確認済 |
| ゲスト向けメッセージ（自動メール）の日本語 | "Send automated emails and booking confirmations in your international guests preferred language"と記載。日本語のテンプレートが標準で用意されるか、自分で作る必要があるかは確認できず | https://sirvoy.com/llms-full.txt | 2026-11-05 | 未確認 |
| サポート言語・対応時間 | 24時間365日（休日含む）。ライブチャット、電話（フリーダイヤルは米・英・豪・アイルランド・ドイツ・オーストリア・ベルギー・スペイン・デンマーク・スウェーデン・フィンランド・フランス。日本の番号の記載なし）、メール（support@sirvoy.com）。対応言語：ヘルプセンターの記事（2026-06-22更新）は English、German、Danish、Japanese、Dutch、Norwegian、Finnish、Spanish、French、Swedish。一方、公式FAQ（全文テキスト）は English、Chinese、Danish、Dutch、Finnish、French、German、Italian、Norwegian、Spanish、Swedish で、日本語が無く記載が食い違う。忙しいときは英語対応に回る旨の記載あり | https://help.sirvoy.com/en_US/sirvoy-general/-contact-customer-support ／ https://sirvoy.com/llms-full.txt | 2026-11-05 | 確認済（両方の記載）／日本語サポートの実態は未確認 |
| 通貨（JPY） | 請求通貨にJPYなし（上記）。アカウント設定（Settings > Sirvoy account > Localization）で通貨・言語・タイムゾーン・日付形式を変更できる。選べる通貨の一覧は確認できず | https://help.sirvoy.com/en_US/customize-your-account/adapting-sirvoy-to-your-local-needs-and-standards | 2026-11-05 | 確認済（設定の存在）／宿泊料金のJPY設定は未確認 |
| 請求書・インボイス | 請求書・領収書の発行機能あり（StarterとPro）。日本の適格請求書（インボイス制度）への対応は確認できず | https://sirvoy.com/pricing | 2026-11-05 | 未確認 |
| 宿泊者名簿・パスポート確認 | 記載なし。入力項目（Input Fields）の設定ページはあるが、本文は未確認。ID収集はChargeAutomation連携（一方向）が連携ページにある | https://sirvoy.com/integrations | 2026-11-05 | 未確認 |
| 住宅宿泊事業法（届出番号表示、年間180日上限など） | 関連機能の記載なし | － | 2026-11-05 | 未確認 |
| SMS | SMSはVonage経由。国によっては配信不可・送信者名が書き換わる（一覧に日本の記載なし） | https://help.sirvoy.com/en_US/message-templates-automated-messaging/sms-restrictions-by-country | 2026-11-05 | 確認済（一覧に日本が無いこと）／日本向けSMSの可否は未確認 |

## 6. アフィリエイト

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| 有無・種別 | あり。Referral Program（紹介）と Partner Program（パートナー）の2種で、同時に参加できるのは1つだけ | https://sirvoy.com/sirvoy-partnership | 2026-11-05 | 確認済 |
| 申込URL | https://sirvoy.com/sirvoy-partnership （"Become a partner"。無料、"No applications or approvals"）。登録フォームは今回の取得ではJavaScriptで描画されず、中身は未確認 | https://sirvoy.com/sirvoy-partnership | 2026-11-05 | 確認済（ページ）／フォームの項目は未確認 |
| 報酬（Referral） | 被紹介者が最初の6か月に支払った料金の50％ | https://sirvoy.com/partner-program-terms-conditions | 2026-11-05 | 確認済 |
| 報酬（Partner） | 被紹介者が解約するまでの支払いの5〜25％。アクティブな被紹介者の数で率が上がる：1〜5件目 5％、6〜15件目 10％、16〜30件目 15％、31〜50件目 20％、51件目〜 25％ | https://sirvoy.com/partner-program-terms-conditions | 2026-11-05 | 確認済 |
| 支払い条件 | 報酬が600ドル（相当額）を超えるまで払出し依頼不可。紹介した有料アカウントが2件以上、30日以上アクティブになるまで支払い保留。払出しは依頼から通常30日以内。紹介リンクの追跡は最長6か月 | https://sirvoy.com/sirvoy-partnership ／ https://sirvoy.com/partner-program-terms-conditions | 2026-11-05 | 確認済 |
| 対象外 | 特別割引・キャンペーンで登録したアカウントは対象外。自分自身のアカウントの紹介は不可 | https://sirvoy.com/partner-program-terms-conditions ／ https://sirvoy.com/sirvoy-partnership | 2026-11-05 | 確認済 |
| 契約の終了 | どちらの側も30日前の書面通知でいつでも終了可。6か月間新規の紹介が無ければSirvoyが終了手続きを始める場合がある。準拠法はアイルランド法、裁判管轄はアイルランドの裁判所 | https://sirvoy.com/partner-program-terms-conditions | 2026-11-05 | 確認済 |
| 規約上の制限（比較サイトに関わるもの） | 規約の原文（抜粋）："the Affiliate will not in a negative or detrimental way speak ill (i.e. badmouth) about or comment upon the business of Sirvoy and will not persuade, induce or attempt to induce any customers to terminate their contracts with or reduce its dealings and business with Sirvoy."（悪く言わない。顧客に解約・取引縮小を促さない）。"Sirvoy data ... will not include a (direct or indirect) link, reference, click-through or reference to the website of a Sirvoy competitor."（Sirvoyのデータを使った箇所に競合サイトへのリンクや言及を含めない）。Sirvoyのデータを競合のコンテンツと混ぜない、画面スクレイピング禁止、アフィリエイトのサイトのデザイン・ロゴをSirvoyと明確に異ならせること。"Sirvoy" を含む（または紛らわしい）ドメイン名の取得・使用禁止。ロゴ・商標は、リンクを張るために必要な範囲に限る（それ以外の販促物は事前の書面承認）。顧客と予約について連絡しない。サイトの内容を最新・正確に保ち、誤りは通知後すみやかに訂正 | https://sirvoy.com/partner-program-terms-conditions | 2026-11-05 | 確認済（規約の記載）／どの範囲が比較記事に及ぶかの解釈は未確認 |
| 参加者の想定 | 規約に "The Affiliate Program will be used by Sirvoy's own clients or for the purpose of benefiting a Sirvoy account user." とある一方、パートナー募集ページは制作会社・コンサルタント・クリエイターなども対象と説明 | https://sirvoy.com/partner-program-terms-conditions ／ https://sirvoy.com/sirvoy-partnership | 2026-11-05 | 確認済（記載の食い違い） |
| ブランド名の入札禁止（検索広告） | 検索広告での入札を禁じる文言は規約に見つからない（ドメイン名の制限のみ） | https://sirvoy.com/partner-program-terms-conditions | 2026-11-05 | 未確認（記載が無いのみ） |

## 7. 乗り換え

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| 予約データの取り込み | 内蔵のインポート機能（Settings > Sirvoy account > Bookings Import）。少数なら手入力（5件未満）、15件未満はスプレッドシート風フォーム、多数はファイルでの取り込み。必須列・日付形式の要件あり。取り込んだ予約はどのチャネルとも紐づかない（変更やキャンセルは各チャネルで要確認） | https://help.sirvoy.com/en_US/import-bookings/import-your-existing-bookings | 2026-11-05 | 確認済 |
| チャネルからの取り込み | Booking.comの予約は連携時に自動で取り込み。Airbnbの予約は、ガイドの手順またはAirbnb連携ページから取り込み | 同上 | 2026-11-05 | 確認済 |
| 他社PMSからの移行ガイド・移行代行 | 他社名を指定した移行ガイドは見つからない。セットアップガイド（新規ユーザー向け）、ライブデモ（無料の個別セットアップ支援）あり | https://help.sirvoy.com/en_US/sirvoy-general/-contact-customer-support | 2026-11-05 | 確認済（ライブデモ）／他社PMS別の移行ガイドは未確認 |
| データの持ち出し | 解約後もエクスポート機能で取得可。「Export & API」のヘルプ項目あり | https://sirvoy.com/terms-conditions | 2026-11-05 | 確認済 |

## 8. 注意すべき点（出典付き）

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| OTA連携はProのみ | Free・StarterにはOTA連携がない（iCalも比較表で×）。Proは月額がStarterの約3〜4倍（例：3〜5室で EUR 59 対 16） | https://sirvoy.com/pricing | 2026-11-05 | 確認済 |
| Freeは1室のみ | 2室以上では使えない（画面上、2室以上でFreeが選べなくなる） | https://sirvoy.com/pricing ／ https://sirvoy.com/_astro/PricingPlans.astro_astro_type_script_index_0_lang.C3esw01U.js | 2026-11-05 | 確認済 |
| プリペイド残高制 | 残高がマイナスで20日超ロック、60日超で削除の可能性。自動チャージの設定あり。SMSやGoogle広告費で残高が減る | https://sirvoy.com/terms-conditions ／ https://help.sirvoy.com/en_US/subscription/refill-and-manage-your-sirvoy-account-balance | 2026-11-05 | 確認済 |
| 日本のOTAに非対応（記載が無い） | 楽天トラベル・じゃらんの接続の記載なし。SiteMinder経由の可否は未確認 | 上記3の行 | 2026-11-05 | 確認済（記載が無いこと） |
| PriceLabsの連携一覧に無い | PriceLabsの連携先（ヘルプ記事・公式連携ページ）に Sirvoy は載っていない | https://help.pricelabs.co/portal/en/kb/articles/available-integrations | 2026-11-05 | 確認済 |
| 利用者の不満（第三者） | Capterraの要約：レポートが限られExcelダウンロードが無い、カスタム項目が持てない（2017年の古いレビュー）、チャネルと予約エンジンの連携が少しぎこちない、設定が難しいという声。評価は高く、サポートと費用対効果が好評とされる。個別レビューは開いていない | https://capterra.com/p/103570/Sirvoy-Booking-System/reviews/ | 2026-11-05 | 第三者のみ（検索結果の要約） |
| 公式サイト内の記載の食い違い | サポート言語（日本語の有無）、Vrboの接続方式（Expedia文中のVrbo対iCal）、Starterの「24/7サポート」表記（プランカードはStarterのみ記載、比較表は全プラン○）。 | https://help.sirvoy.com/en_US/sirvoy-general/-contact-customer-support ／ https://sirvoy.com/llms-full.txt ／ https://sirvoy.com/pricing | 2026-11-05 | 確認済（食い違いの存在） |

## 調べられなかったこと

- 宿泊料金の通貨としてJPYが使えるか（設定画面で選べる通貨の一覧）。日本での決済手段（Stripe／PayPalの日本対応）。
- 日本の適格請求書（インボイス制度）への対応。宿泊者名簿・パスポート確認の機能。住宅宿泊事業法に関する機能。
- 日本語サポートの実態（ヘルプには日本語あり、公式FAQには無く、食い違い）。日本語の自動メールテンプレートの有無。
- SiteMinder経由で楽天トラベル・じゃらんに接続できるか。Airbnb連携の公式パートナー認定の有無。
- iCal連携の同期遅延の実際の時間。
- API（Export & APIの範囲）、オーナーポータル機能の有無。
- 返金規約の細部（カード登録なしの無料トライアル利用者の扱い）。解約の「規約全文」。
- アフィリエイトの登録フォームの項目（動的描画のため未取得）。検索広告のブランド名入札の扱い。規約の最終更新日。
- 利用者の不満の裏取り（Capterraの個別レビュー本文は開いていない）。
- 年払い額（他の部屋数の階段）は計算値であり、画面では確認していない。
