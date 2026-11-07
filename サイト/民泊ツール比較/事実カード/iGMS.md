# 事実カード：iGMS（igms.com）

- 取得日：すべて 2026-11-05
- 書式：`_スキーマ.md` に従う。確度は 確認済／第三者のみ／未確認
- 取得方法の注記：
  - 料金は公式 pricing ページ（表と、ページが読み込む公開API https://www.igms.com/api/public-endpoints/prices のJSON）で確認した。値は一致。
  - 料金表の見出しは「price per property per month in USD for 1 to 20 properties」。表の数字は「物件数N件のときの1物件あたり月額」。合計はこれに物件数を掛けた私の計算値（公式の合計ではない）。
  - 紹介プログラムの報酬表は画像だったため、画像を開いて読んだ。
  - iGMS のヘルプ記事の一部は日付が古い（2025年1月付など）。現行ページと食い違う点は併記した。

## 1. 基本

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| 運営会社 | AirGMS Technologies Inc.（2015年創業、自己資本経営「bootstrapped」）。住所表記：1107 1st Ave #702, Seattle, WA 98101-2944, United States | https://www.igms.com/pricing/ | 2026-11-05 | 確認済 |
| 利用規約の準拠法 | カナダ・ブリティッシュコロンビア州の法律（規約の「Governing Law」） | https://igms.com/terms/ | 2026-11-05 | 確認済 |
| 対象規模 | トップページ：「Built for independent hosts — Managing 2-8 properties」。物件管理会社向けページもあり。料金表は1〜20物件、20+物件は担当者付き | https://igms.com/ ／ https://www.igms.com/pricing/ | 2026-11-05 | 確認済 |
| パートナー認定（公式の自称） | 「Airbnb Preferred Partner, a Booking.com Advanced Partner, a Vrbo Connected Partner and an official Google Vacation Rentals partner」 | https://www.igms.com/pricing/ | 2026-11-05 | 確認済 |
| 評判の規模 | 「Rated by 3,000+ hosts」（無料プランページ）。Capterra 4.6（307件、2026-10-19更新） | https://igms.com/go/free-plan/ ／ https://www.capterra.com/p/157033/iGMS/reviews/ | 2026-11-05 | 確認済 |
| プラン名 | FLEX／PRO／PRO+。無料プランは「pilot」。旧 HOST・LITE プランは新規受付終了（規約に記載） | https://www.igms.com/pricing/ ／ https://igms.com/terms/ | 2026-11-05 | 確認済 |

## 2. 料金

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| 課金モデル | PRO／PRO+：1物件あたり月額（物件数が増えるほど単価が下がる）。FLEX：予約された泊数あたり $1、最低 $20／物件／月、予約手数料 0%。請求は「1物件目の後は、その月に1件以上確定予約のあった物件のみ」。最低料金は1物件分 | https://www.igms.com/pricing/ | 2026-11-05 | 確認済 |
| active property の定義 | 請求周期中に1回以上予約が入った1つの貸出物件。複数サイトの掲載はチャネルマネージャーでグルーピングしないと別物件として課金される。キャンセル予約は課金対象外。部屋単位で別貸しすると別物件 | https://www.igms.com/pricing/ | 2026-11-05 | 確認済 |
| 請求書の時期 | 毎月初に前月の active 物件数分を請求（後払い）。月内のどの時期に連携・解除しても、その月に予約があれば active 扱い | https://www.igms.com/pricing/ | 2026-11-05 | 確認済 |
| PRO 1物件あたり月額・月払い（USD） | 1室 $48.00／3室 $23.33／5室 $19.80／10室 $17.40／20室 $14.20 | https://www.igms.com/pricing/ ／ https://www.igms.com/api/public-endpoints/prices | 2026-11-05 | 確認済 |
| PRO 1物件あたり月額・年払い（USD） | 1室 $38.00／3室 $20.67／5室 $17.40／10室 $15.00／20室 $11.35 | 同上 | 2026-11-05 | 確認済 |
| PRO+ 1物件あたり月額・月払い（USD） | 1室 $69.00／3室 $31.33／5室 $30.80／10室 $25.20／20室 $19.25 | 同上 | 2026-11-05 | 確認済 |
| PRO+ 1物件あたり月額・年払い（USD） | 1室 $56.00／3室 $27.67／5室 $27.00／10室 $20.10／20室 $16.00 | 同上 | 2026-11-05 | 確認済 |
| 目安：月額合計・PRO 月払い（計算値） | 1室 $48／3室 約$70／5室 約$99／10室 約$174／20室 約$284 | 上記単価×物件数 | 2026-11-05 | 確認済（計算値） |
| 目安：月額合計・PRO 年払い（計算値） | 1室 $38／3室 約$62／5室 約$87／10室 $150／20室 約$227 | 同上 | 2026-11-05 | 確認済（計算値） |
| 目安：月額合計・PRO+ 月払い（計算値） | 1室 $69／3室 約$94／5室 約$154／10室 約$252／20室 約$385 | 同上 | 2026-11-05 | 確認済（計算値） |
| 目安：月額合計・PRO+ 年払い（計算値） | 1室 $56／3室 約$83／5室 $135／10室 約$201／20室 $320 | 同上 | 2026-11-05 | 確認済（計算値） |
| FLEX の目安（計算値） | 月の予約泊数 20泊以下は物件あたり $20、22泊なら $22（公式の例）。1物件あたり $1×泊数、最低 $20 | https://www.igms.com/pricing/ | 2026-11-05 | 確認済 |
| 無料プラン（Free、pilot） | 月額 $0。予約5件・ゲストメッセージ10件まで。Airbnb／Vrbo／Booking.com の統合カレンダー・受信箱、自動メッセージ、アプリ、清掃員・共同ホスト招待。Stripe 経由のダイレクト決済にのみ 4%（Stripe の手数料は別）。上限に達すると同期・送信を止める場合あり。ライブチャット・電話・オンボーディング・優先対応は有料のみ（無料プラン規約）。「The Free Plan is offered as a pilot ... and it may change as we learn.」 | https://igms.com/go/free-plan/ ／ https://www.igms.com/go/free-plan-terms/ | 2026-11-05 | 確認済 |
| 無料トライアル | 14日、クレジットカード不要（公式ページ記載）。トライアル終了までにプラン未選択だとアカウントはブロックされる（ヘルプ記事） | https://www.igms.com/pricing/ ／ https://help.igms.com/en/articles/9927745-how-to-choose-your-igms-subscription-plan | 2026-11-05 | 確認済 |
| 契約縛り（月払い） | 解約手数料なし。解約後に最終請求書（規約：「no credits or refunds for partial months」） | https://help.igms.com/en/articles/9927743-how-do-i-cancel-my-igms-subscription ／ https://igms.com/terms/ | 2026-11-05 | 確認済 |
| 契約縛り（年払い・10物件未満） | 一括前払い。「The full annual fee is non-refundable, regardless of whether the service is fully used.」途中解約でも未使用分の返金なし | https://igms.com/terms/ | 2026-11-05 | 確認済 |
| 契約縛り（年払い・10物件以上） | 月ごと請求＋署名する年間契約。契約期間前に解約すると月払い料金に切り替わり、差額（使用済み月分）を請求される | https://www.igms.com/pricing/ ／ https://igms.com/terms/ | 2026-11-05 | 確認済 |
| 解約の方法・所要日数 | ヘルプ記事のリンクから申請。営業日48時間以内に処理しメールで連絡。アカウント削除でテンプレ・メモ・清掃指示も消える。プロモコード／特別料金は新規アカウントでは引き継がれない | https://help.igms.com/en/articles/9927743-how-do-i-cancel-my-igms-subscription | 2026-11-05 | 確認済 |
| 料金の変更 | 「iGMS will provide notice ... at least 30 days before the change is to take effect」（規約）。「All fees are non-refundable and exclusive of applicable taxes.」 | https://igms.com/terms/ | 2026-11-05 | 確認済 |
| 追加手数料 | 「There are NO hidden fees at all, and we don't charge an obligatory setup fee」。ダイレクト決済は Stripe 利用（Stripe 手数料別）。無料プランの 4% は上記。PRO／PRO+ でのダイレクト予約の iGMS 側手数料率は pricing ページに明記なし（FLEX は「0% booking fee」） | https://www.igms.com/pricing/ | 2026-11-05 | 確認済（記載内容）／未確認（PRO・PRO+ のダイレクト手数料率） |
| 提携先の追加料金 | 「Partners may charge additional subscription fees」 | https://www.igms.com/pricing/ | 2026-11-05 | 確認済 |
| 税 | 「exclusive of applicable taxes」（規約） | https://igms.com/terms/ | 2026-11-05 | 確認済 |
| 決済手段 | 主要クレジットカード。処理は Stripe | https://www.igms.com/pricing/ | 2026-11-05 | 確認済 |
| 請求通貨 | 料金表は USD のみ表示。他通貨での請求の記載は見つからず | https://www.igms.com/pricing/ | 2026-11-05 | 未確認（円請求の可否） |

## 3. チャネル

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| API接続のチャネル | 「Airbnb, Vrbo and Booking.com by direct API; Expedia, Tripadvisor and other calendars by iCal」 | https://www.igms.com/features/channel-manager/ | 2026-11-05 | 確認済 |
| iCal接続のチャネル | Expedia、Tripadvisor、その他のカレンダー。iCal は1時間ごとに更新、物件へのグルーピング不可。iCal のカレンダーでも予約は統合カレンダーに表示され、清掃タスクは自動作成される（公式の説明）。「iCal 接続だとレポート機能が使えない」という記載は検索要約でのみ見え、原文は未確認 | https://www.igms.com/features/channel-manager/ ／ https://help.igms.com/en/articles/9927919-how-does-the-channel-manager-work | 2026-11-05 | 確認済（更新頻度・グルーピング）／未確認（レポート） |
| Agoda | 公式の対応チャネル一覧に Agoda の記載なし | https://igms.com/integrations | 2026-11-05 | 確認済（記載なし） |
| Google Vacation Rentals | 公式パートナー（掲載機能あり）。詳細な提供プランは未確認 | https://www.igms.com/pricing/ | 2026-11-05 | 確認済 |
| 楽天トラベル | 公式ページに記載なし。iCal で取り込めるかは未確認 | https://igms.com/integrations | 2026-11-05 | 未確認 |
| じゃらん | 同上。記載なし | https://igms.com/integrations | 2026-11-05 | 未確認 |
| 重複予約防止 | API接続のチャネルは「A booking on Booking.com blocks the same dates on Airbnb and Vrbo straight away」。API接続と iCal を併用すると二重ブロックになるため、直接接続したら iCal を外す | https://www.igms.com/features/channel-manager/ ／ https://help.igms.com/en/articles/9927919-how-does-the-channel-manager-work | 2026-11-05 | 確認済 |
| Airbnb の注意（利用者の口コミ） | 手動ブロック日が API 接続後に Airbnb カレンダーから消えた、という Capterra 口コミあり（2026-07-06） | https://www.capterra.com/p/157033/iGMS/reviews/ | 2026-11-05 | 確認済（口コミの記載。真偽は未検証） |

## 4. 機能

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| プラン別の差（公式の要約） | FLEX：基本（チャネル管理、自動化、ダイレクト予約、ヘルプ）。PRO：FLEXに加え AI返信、予約できるウェブサイト、ブランド管理、オーナーポータル、20物件以上は専任CSM。PRO+：PROに加え 自動翻訳、キャッシュフローレポート、収益管理、Dynamic Pricing（US・CA・AU・MX・UK・ES で利用可）、サポート追跡ツール、AIエージェント、AI物件ナレッジ、オーナー明細、物件経費。AIアップセルは「SOON」 | https://www.igms.com/pricing/ | 2026-11-05 | 確認済 |
| 自動メッセージ | テンプレ、カスタムトリガー、レビュー自動化、AI返信。無料プランでも自動メッセージは利用可 | https://www.igms.com/pricing/ ／ https://igms.com/go/free-plan/ | 2026-11-05 | 確認済 |
| 清掃・タスク | 清掃タスクの自動作成・割り当て、チェックリスト、SMS通知、チーム管理。Turno、Operto Teams、Cleanster 連携 | https://www.igms.com/pricing/ ／ https://igms.com/integrations | 2026-11-05 | 確認済 |
| スマートロック連携先 | 価格ページ：August、Yale、Schlage、Igloohome、Nuki、Google Nest、Keycafe、RemoteLock ほか。連携ページ：Jervis、RemoteLock（RemoteLock は「Coming soon」表示あり）。日本のロック（Akerun・SESAME）は記載なし | https://www.igms.com/pricing/ ／ https://igms.com/integrations | 2026-11-05 | 確認済（記載内容）／未確認（日本のロック） |
| 価格ツール連携 | PriceLabs、Wheelhouse、Beyond、DPGO（公式の連携ページ）。内蔵 Dynamic Pricing は PRO+（上記の国のみ） | https://igms.com/integrations ／ https://www.igms.com/pricing/ | 2026-11-05 | 確認済 |
| オーナーポータル | PRO 以上（明細は PRO+） | https://www.igms.com/pricing/ | 2026-11-05 | 確認済 |
| ダイレクト予約サイト | PRO 以上（Bookable Website、独自ドメイン、ブランド管理、複数物件検索）。決済は Stripe | https://www.igms.com/pricing/ ／ https://www.igms.com/direct-booking-payment-processing-for-hosts/ | 2026-11-05 | 確認済 |
| 会計・レポート | キャッシュフローレポート、月次収益レポート、オーナー明細、物件経費（PRO+）。会計ソフト（QuickBooks 等）との連携は確認できず | https://www.igms.com/pricing/ | 2026-11-05 | 確認済（記載内容）／未確認（会計ソフト連携） |
| ゲスト審査・保険 | Safely、Superhog、Minut、InsuraGuest 等と連携（連携ページ） | https://igms.com/integrations | 2026-11-05 | 確認済 |
| モバイルアプリ | iOS／Android あり。無料プランから利用可 | https://igms.com/go/free-plan/ | 2026-11-05 | 確認済 |

## 5. 日本対応

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| 管理画面のUI言語 | 英語とスペイン語。「The app is available in English and Spanish.」日本語なし | https://www.igms.com/pricing/ | 2026-11-05 | 確認済 |
| ゲスト向けメッセージの言語 | 「iGMS supports 109 languages」。ゲストの最初のメッセージから言語を自動検出し、テンプレを自動送信。判別できない場合は英語。日本語が含まれるかの言語一覧は未確認（別ページに「120+ languages」の記載もあり、数字が不統一） | https://help.igms.com/en/articles/9927780-how-do-i-create-message-templates-in-different-languages（2025-01-17付） | 2026-11-05 | 確認済（109言語の記載）／日本語の可否は未確認 |
| 受信箱の自動翻訳 | PRO+ の機能として表示（「Auto-translation for messages」）。同ヘルプ記事は、自動化メッセージのみシステム翻訳、通常メッセージはブラウザ拡張の利用を案内しており、記事の日付が古い（2025年）ため現行仕様は未確認 | https://www.igms.com/pricing/ ／ 上記ヘルプ記事 | 2026-11-05 | 確認済（記載内容）／現行仕様は未確認 |
| サポート言語 | 価格ページ：「Multilingual Support (ENG, ESP)」＝英語・スペイン語。日本語サポートの記載なし | https://www.igms.com/pricing/ | 2026-11-05 | 確認済（ENG・ESP）／日本語は記載なし |
| サポート窓口・時間 | メール（対応は「Response within 48 hours」の表記）、ライブチャット、1対1オンボーディング（有料プラン）、20物件以上は専任CSM、電話は要請ベース。無料トライアル中は平日24時間チャット（ヘルプ記事）。別記事には「Monday-Friday 24h, Saturday-Sunday 5:00am-5:00pm (EST)」の記載ありとの検索要約（未開封） | https://www.igms.com/pricing/ ／ https://help.igms.com/en/articles/9927885-how-can-igms-help-me | 2026-11-05 | 確認済（トライアル中の平日24時間）／第三者のみ（週末の時間） |
| 通貨（JPY） | 物件ごとに料金通貨を設定できる設定画面の記載あり（検索要約）。円が使える一覧は見つからず。Stripe の対応国・通貨も未確認 | https://help.igms.com/en/articles/10628302-how-to-configure-availability-and-pricing-settings-in-igms（検索要約） | 2026-11-05 | 第三者のみ（要再確認）／JPYは未確認 |
| 決済手段（サブスク） | 主要クレジットカード（Stripe）。PayPal 等は記載なし | https://www.igms.com/pricing/ | 2026-11-05 | 確認済 |
| 請求書・インボイス（日本のインボイス制度） | 予約に対する請求書管理機能（ゲスト向け）はあるが、iGMS自身が発行する請求書の様式・日本の適格請求書（T番号）対応の記載は見つからず | https://help.igms.com/en/articles/9927753-invoice-management-via-igms-feature-overview（検索要約） | 2026-11-05 | 未確認 |
| 宿泊者名簿・パスポート確認 | 受信箱の「smart Inbox badges」でゲストの審査状況を表示（Safely 等と連携）。パスポート確認・日本の宿泊者名簿に合わせた機能の記載は見つからず。ダイレクト予約に「Check-in form」あり | https://help.igms.com/en/articles/9927885-how-can-igms-help-me ／ https://www.igms.com/pricing/ | 2026-11-05 | 未確認（日本の名簿要件） |
| 住宅宿泊事業法に関する機能 | 届出番号の表示・管理に関する記載は見つからず | https://www.igms.com/pricing/ | 2026-11-05 | 未確認 |
| 日本国内の予約サイト（楽天・じゃらん等） | 公式一覧に記載なし | https://igms.com/integrations | 2026-11-05 | 未確認 |

## 6. アフィリエイト

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| 有無 | あり。自社の紹介プログラム（Referral Program）。フッターに「Affiliate / Referral Program」 | https://try.igms.com/referral-program | 2026-11-05 | 確認済 |
| 種別・基盤 | 自社運営。公式の別ページ（Community Extras）に「transparent tracking via the LeadDyno platform」と記載（LeadDyno は外部のアフィリエイト追跡ツール）。PartnerStack／Impact 等ではない | https://try.igms.com/igms-community-extras | 2026-11-05 | 確認済 |
| 申込URL | 「GET STARTED」「JOIN NOW」ボタンは HubSpot フォーム https://share.hsforms.com/1cZwY0EaVT-CmvJdPT18ttQ20prz へリンク（取得時はフォーム枠のみ表示） | https://try.igms.com/referral-program | 2026-11-05 | 確認済（リンク先）／フォーム項目は未確認 |
| 報酬（現行ページ） | 「Earn up to $550 for each paid client who integrates their vacation rental listings with iGMS.」内訳：有料顧客1件あたり $50（10物件未満）。10物件以上を連携した有料顧客には追加 $500（合計 $550）。画像の表記：「$50 for each paid client to iGMS」「Extra $500 for paid customer with 10 or more active properties linked」 | https://try.igms.com/referral-program（報酬表は画像 /_cdn/8c147ced8ebc223d.png） | 2026-11-05 | 確認済 |
| 報酬の食い違い | 別の公式ページ（Community Extras）は「earn up to $250 for each new iGMS user」と記載。現行の紹介ページ（最大 $550）とは数字が違う。古い記載の可能性（日付不明） | https://try.igms.com/igms-community-extras | 2026-11-05 | 確認済（食い違いの事実）／どちらが有効かは未確認 |
| 報酬が発生するタイミング | 「as soon as your referral pays for their first full month」（紹介先が最初の1か月分を満額支払った時）。「after the free trial」に10物件以上連携で $550 | https://try.igms.com/referral-program | 2026-11-05 | 確認済 |
| 支払い方法 | PayPal（「use the same email address as your PayPal account」）。月次支払い（「Earn monthly payouts」）。最低支払額の記載なし | https://try.igms.com/referral-program | 2026-11-05 | 確認済 |
| 紹介された側の特典 | $30 のボーナス（ページ記載） | https://try.igms.com/referral-program | 2026-11-05 | 確認済 |
| 規約上の制限（ブランド名入札禁止、コンテンツ制限、クッキー期間など） | 紹介ページに規約・利用条件へのリンクや条項の記載は見つからなかった。プロモ素材は提供される（「ready-to-use marketing materials」）。「Exclusive affiliate-only opportunities」の記載あり | https://try.igms.com/referral-program | 2026-11-05 | 未確認（規約ページは見つからず。申込後に提示される可能性） |
| 日本居住者の参加可否・円払い | 記載なし（PayPal 払い） | https://try.igms.com/referral-program | 2026-11-05 | 未確認 |

## 7. 乗り換え

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| 他PMSからの自動データ移行 | 公式の自動移行機能の記載は見つからず。ブログ「Escaping PMS Lock-in During Property Management Software Migration」は一般的な移行チェックリスト（CSV／API、段階移行など）で、iGMS固有の取り込み機能ではない | https://www.igms.com/property-management-software-migration/ | 2026-11-05 | 確認済（自動移行の記載なし） |
| オンボーディング支援 | 10物件以上は無料のセットアップセッション（価格ページFAQ）。1対1ガイド付きオンボーディングは有料プランの特典（無料プランでは対象外） | https://www.igms.com/pricing/ ／ https://igms.com/go/free-plan/ | 2026-11-05 | 確認済 |
| 過去の移行支援プログラム | 2020年の告知に「Easy Onboarding and Data Migration Service」（他ソフトからの移行で5物件以上は無償、1時間のセットアップ、データ移行、メッセージテンプレの移行、チャネルの結合）。日付が古く現行の条件は未確認 | https://www.igms.com/igms-support-program-for-hosts/ | 2026-11-05 | 確認済（2020年の記載）／現行条件は未確認 |
| Vrbo の切替 | Vrbo サポートに依頼してアカウントをiGMSへ移す（Advertiser ID が必要）という説明（検索要約。Vrbo の記事を引用） | https://help.igms.com/en/articles/9927957-how-to-connect-a-vrbo-account-to-igms-via-api | 2026-11-05 | 第三者のみ（検索要約） |
| 他ツールからの乗り換えガイド | 公式の「Switch to iGMS」リンクは登録ページ（https://www.igms.com/app/register.html）。専用の移行ガイドページは見つからず（/switch-to-igms/ は404）。比較ページ（iGMS vs Hospitable など）はある | https://www.igms.com/pricing/ | 2026-11-05 | 確認済（専用ガイドは見つからず） |
| 試用 | 14日トライアル、カード不要。無料プランも別にある | https://www.igms.com/pricing/ | 2026-11-05 | 確認済 |

## 8. 注意すべき点（出典付き）

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| 年払いは返金不可 | 規約：年額前払いは未使用分の返金なし。10物件以上の年間契約は、途中解約で月払い料金との差額請求 | https://igms.com/terms/ | 2026-11-05 | 確認済 |
| 管理画面が英語・スペイン語のみ | 第5節 | https://www.igms.com/pricing/ | 2026-11-05 | 確認済 |
| ヘルプ記事と現行プランの不一致 | 解約・プラン選択のヘルプ記事（2025年1月付）は旧プラン（Host、4プラン）を前提にしている | https://help.igms.com/en/articles/9927745-how-to-choose-your-igms-subscription-plan | 2026-11-05 | 確認済 |
| 解約できないという口コミ | Capterra 2025-02-27：「Cannot cancel, after repeated attempts. No way to cancel on the site.」（口コミの記載。真偽は未検証。公式ヘルプはリンクからの申請と営業日48時間以内の処理を案内） | https://www.capterra.com/p/157033/iGMS/reviews/ | 2026-11-05 | 確認済（口コミの記載） |
| API接続後に手動ブロックが消えたという口コミ | Capterra 2026-07-06（1.0評価）：Airbnb の手動ブロック日がAPI接続後に消えたが、オンボーディングで説明がなかった | 同上 | 2026-11-05 | 確認済（口コミの記載） |
| サポートの評価が割れる | Capterra には「support is second to none」等の好意的な口コミと、サポート不満の口コミが混在。ヘルプ記事の記載では iGMS 側が「24時間平日チャット」で対応と返答（検索要約） | 同上 | 2026-11-05 | 確認済（Capterraの口コミ内容）／第三者のみ（iGMS返答の要約） |
| 無料プランの限界 | 予約5件・メッセージ10件まで。サービスレベル・稼働率・応答時間の保証なし | https://www.igms.com/go/free-plan-terms/ | 2026-11-05 | 確認済 |
| Dynamic Pricing の対象国 | 米・加・豪・メキシコ・英・スペインのみ（日本は対象外の表示） | https://www.igms.com/pricing/ | 2026-11-05 | 確認済 |
| Expedia・Tripadvisor は iCal のみ | 1時間更新で、物件へのグルーピング不可 | https://www.igms.com/features/channel-manager/ | 2026-11-05 | 確認済 |
| 評価の概況 | Capterra 4.6（307件）。G2 4.6（43件）、Trustpilot はアクセス不可（403） | https://www.capterra.com/p/157033/iGMS/reviews/ | 2026-11-05 | 確認済（Capterra）／第三者のみ（G2は検索要約） |

## 調べられなかったこと

- 楽天トラベル・じゃらん等の国内予約サイトとの連携（公式一覧に記載なし。iCal 取り込みの可否は未検証）
- Akerun・SESAME 等の日本製スマートロック対応（公式一覧になし）
- 日本語UI・日本語サポート（UIは英語・スペイン語のみ。サポートも ENG／ESP と記載）。ゲスト向け109言語に日本語が含まれるかの一覧は未取得
- JPY での請求（サブスク）、Stripe 経由の円決済の対応可否
- 日本の適格請求書（T番号）、宿泊者名簿・パスポート確認、住宅宿泊事業法の届出番号に関する機能
- 紹介プログラムの規約（ブランド名入札禁止、コンテンツ制限、クッキー期間、支払い条件の詳細、日本居住者の可否）。HubSpot の申込フォームは項目を取得できなかった。紹介ページ内の報酬額（最大 $550）と Community Extras の記載（最大 $250）の食い違いの理由も未確認
- PRO／PRO+ のダイレクト予約における iGMS 側の手数料率
- 受信箱の自動翻訳の現行仕様（記事が古い）、サポート週末時間の原文確認
- 会計ソフト（QuickBooks 等）との連携
- Capterra 以外の口コミ原文（G2・Trustpilot は取得不可）、Reddit 等のコミュニティ評判
- 移行支援（5物件以上の無償移行）の現行条件
