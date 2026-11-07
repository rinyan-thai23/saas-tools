# 事実カード：Uplisting（uplisting.io）

- 取得日：2026-11-05（すべての行）
- 確度の意味：`確認済`＝公式ページ・公式ヘルプ・公式規約を開いて確認／`第三者のみ`＝公式を開けず第三者の情報だけ／`未確認`
- 価格は公式料金ページ（https://www.uplisting.io/pricing）のHTML内スクリプト（料金計算ロジック）と本文から読み取った。料金ページは画面上のスライダーで価格が変わるJavaScript描画のため、**下の「物件数別の目安」は計算ロジックから算出した値**（画面表示そのものではない）。
- 通貨は既定でGBP（英ポンド）表示。JPYは料金ページの通貨選択肢にない（後述）。

## 1. 基本

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| 運営会社 | Uplisting Limited（利用規約の記載）。準拠法はイングランド・ウェールズ法、専属管轄は英国裁判所 | https://www.uplisting.io/legal/terms-and-conditions | 2026-11-05 | 確認済 |
| 創業 | トップページに「2016 Giving hosts their life back since day one」 | https://www.uplisting.io/ | 2026-11-05 | 確認済 |
| 対象規模（公式の自己説明） | 「we are focused on urban property managers with 10 to 300+ properties」「The majority of our members have 20+ properties」。ただし20室未満の利用者も多いとも書いている | https://support.uplisting.io/en/article/is-uplisting-right-for-me-hjm9f5/ | 2026-11-05 | 確認済 |
| 料金プラン上の物件数 | Independent Host は4物件まで。他のプランは物件数の上限なし。41物件以上は「Custom pricing／Talk to sales」 | https://www.uplisting.io/pricing | 2026-11-05 | 確認済 |
| 利用者数の表記（ページ間で不一致） | 料金ページ「Trusted by 2,000+ operators」／トップページ「Trusted by 1,000+ operators」「Join 1,000+ UK operators」 | https://www.uplisting.io/pricing , https://www.uplisting.io/ | 2026-11-05 | 確認済（表記の不一致を確認） |
| 主な市場 | トップページに「Join 1,000+ UK operators」。通貨・SMS番号・コンプライアンス機能は英国向けの記述が目立つ | https://www.uplisting.io/ | 2026-11-05 | 確認済 |

## 2. 料金

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| 課金モデル | 3プラン（Independent Host／Operator／Manager）。各プランは「物件あたり単価」と「月額下限（floor）」の高い方を請求。FAQ：「Your monthly price is whichever is higher: the plan's per-property rate, or the plan's floor.」 | https://www.uplisting.io/pricing | 2026-11-05 | 確認済 |
| 従量（Pay as you go）の選択肢 | 月額£0＋予約ごとの手数料。1〜4物件は3%、5〜10物件は1.5%。10物件までの利用者のみ。「Pay nothing on months with no bookings」 | https://www.uplisting.io/pricing | 2026-11-05 | 確認済 |
| Independent Host（定額） | 1〜2物件 £40／月、3〜4物件 £72／月（4物件が上限） | https://www.uplisting.io/pricing （内部スクリプトの ih12=40, ih34=72） | 2026-11-05 | 確認済（スクリプトから算出） |
| Operator（定額） | 5物件まで £90／月（下限）。6物件以上は1物件あたり £16。年払いで10%引き | https://www.uplisting.io/pricing （op: cap5, flat90, rate16） | 2026-11-05 | 確認済（スクリプトから算出） |
| Manager（定額） | 15物件まで £208／月（下限）。16物件以上は1物件あたり £13 | https://www.uplisting.io/pricing （mg: cap15, flat208, rate13） | 2026-11-05 | 確認済（スクリプトから算出） |
| 物件数別の目安：1室 | Independent Host £40（従量なら£0＋3%）／Operator £90／Manager £208 | 同上（算出） | 2026-11-05 | 確認済（算出値） |
| 物件数別の目安：3室 | Independent Host £72（従量なら£0＋3%）／Operator £90／Manager £208 | 同上（算出） | 2026-11-05 | 確認済（算出値） |
| 物件数別の目安：5室 | Independent Host は選択不可（4物件まで）／Operator £90（従量なら£0＋1.5%）／Manager £208 | 同上（算出） | 2026-11-05 | 確認済（算出値） |
| 物件数別の目安：10室 | Operator £160（16×10。従量なら£0＋1.5%）／Manager £208 | 同上（算出） | 2026-11-05 | 確認済（算出値） |
| 物件数別の目安：20室 | Operator £320（16×20）／Manager £260（13×20）。従量は10物件までのため対象外 | 同上（算出） | 2026-11-05 | 確認済（算出値） |
| 他通貨の定額（参考） | EUR：IH 47/84、Operator 床105・19/物件、Manager 床240・15/物件。USD：IH 51/91、Operator 床114・20/物件、Manager 床264・17/物件 | https://www.uplisting.io/pricing （スクリプトの通貨表） | 2026-11-05 | 確認済（スクリプトから読取） |
| 日本円（JPY）建ての価格 | 料金ページの通貨選択は GBP／EUR／USD／AUD／NZD／CAD のみ。利用規約も請求通貨を「EUR, USD, AUD or GBP」と記載。JPYは見当たらない | https://www.uplisting.io/pricing , https://www.uplisting.io/legal/terms-and-conditions | 2026-11-05 | 確認済（記載がないことを確認） |
| 含まれる範囲（Independent Host） | 全チャネル（Airbnb／Booking.com／Vrbo）、統合受信箱と自動メッセージ、Basic直接予約サイト、SMS、AI 100アクション/月、REST APIとMCPサーバー、メール・チャットサポート（2時間応答）、無料1:1オンボーディング | https://www.uplisting.io/pricing | 2026-11-05 | 確認済 |
| 追加料金（アドオン） | スマートロック連携：Independent Hostは＋£10/月（Operator以上は込み）／Uplisting Protect（保証金）：＋£4/物件/月（Operator以上は込み）／Plus直接予約サイト：＋£30/月（Managerは込み）／オーナー管理＋オーナー明細：£40/月〜（Managerは込み）／ゲスト本人確認：£15/月〜（Managerは込み）／AI無制限：＋£49/月（Managerは込み） | https://www.uplisting.io/pricing | 2026-11-05 | 確認済 |
| アドオン別表記（ページ内で数字が異なる箇所） | 「Client Statements + Portal £8 p/l/m」「Guest Identity Verification £1.25/verification」とも記載。比較表の「From £40 p/m」「From £15 p/m」と同じページに併記されている。アドオン価格は「shown in GBP while local pricing is finalised」 | https://www.uplisting.io/pricing | 2026-11-05 | 確認済（併記を確認） |
| ゲスト本人確認の従量料金 | 1回あたり GBP £1.25／EUR €1.50／USD $1.65／CAD $2.10／AUD $2.20／NZD $2.40（再試行含む）。月末に請求 | https://support.uplisting.io/en/article/guest-identification-verification-11gqur/ | 2026-11-05 | 確認済 |
| スマートロック料金（ページ間で不一致） | 料金ページ：Independent Host に「＋£10/mo」。ヘルプ（2026-07-23更新）：「Each smart lock incurs a monthly charge of £4 per each activated lock」 | https://www.uplisting.io/pricing , https://support.uplisting.io/en/article/automate-guest-access-with-uplisting-smart-locks-16g6006/ | 2026-11-05 | 確認済（不一致を確認。どちらが現行かは未確認） |
| 無料トライアル | 14日間。「14 days free · no card · cancel anytime」 | https://www.uplisting.io/pricing | 2026-11-05 | 確認済 |
| 契約縛り（料金ページ） | 「No contract, no notice period」「Monthly plans roll month to month and you can cancel anytime. Annual billing is available on Operator and Manager only, at 10% off」 | https://www.uplisting.io/pricing | 2026-11-05 | 確認済 |
| 契約縛り（利用規約：料金ページと食い違い） | General Terms（最終編集 27-02-2024）：「continues for a minimum of 12 months」「The Subscription will auto-renew at the end of the period」。別ページ terms-and-conditions-contracted（最終編集 06-06-2024）にも同文あり。どの契約に適用されるかは未確認 | https://www.uplisting.io/legal/terms-and-conditions , https://www.uplisting.io/legal/terms-and-conditions-contracted | 2026-11-05 | 確認済（記載を確認。適用条件は未確認） |
| 解約・返金 | ヘルプ：「unless you cancel within 14 days of setting up your Subscription then no refunds for part-periods will be provided」。規約：料金は前払い・返金不可。物件数の増減は日割り（pro-rata）で請求 | https://support.uplisting.io/en/article/understanding-billing-wphphp/ , https://www.uplisting.io/legal/terms-and-conditions | 2026-11-05 | 確認済 |
| 値上げ条項 | 規約：「We reserve the right to increase the Commission and/or any fees for the Subscription Plans at least once per calendar year by 5%」。同意しない場合は通知後30日以内に解約可 | https://www.uplisting.io/legal/terms-and-conditions | 2026-11-05 | 確認済 |
| 支払い方法 | クレジットカードまたはDirect Debit（規約）。請求書はメール | https://www.uplisting.io/legal/terms-and-conditions | 2026-11-05 | 確認済 |
| ダイレクト予約の手数料 | 決済にStripeアカウントが必要。Uplisting側の予約手数料は、従量プラン（3%／1.5%）以外は料金ページに記載なし。Stripe手数料は別途（Stripe側の料金） | https://support.uplisting.io/en/article/accept-payments-via-stripe-6um8cf/ | 2026-11-05 | 確認済（Uplisting側の定額プランでの手数料は記載なし＝未確認） |
| 古い記載の残り | 乗り換えページに「We have one pricing plan」「No commission, no long-term contracts and no setup fees」と旧料金体系の文言が残る（現行は3プラン＋従量手数料プラン） | https://www.uplisting.io/switch-to-uplisting | 2026-11-05 | 確認済（不一致を確認） |

## 3. チャネル

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| Airbnb | 公式ソフトウェアパートナー。料金ページに「Airbnb Preferred+」、「Uplisting connects directly to Airbnb as an official software partner」 | https://www.uplisting.io/pricing , https://www.uplisting.io/switch-to-uplisting | 2026-11-05 | 確認済 |
| Booking.com | 「Booking.com Premier Partner」と表示。API連携 | https://www.uplisting.io/pricing | 2026-11-05 | 確認済 |
| Vrbo | 公式連携あり（ヘルプに接続手順） | https://support.uplisting.io/en/article/how-to-connect-to-vrbo-1k7b4v2/ | 2026-11-05 | 確認済 |
| Expedia | Vrboとの連携経由（「most」の国で、保証なし）またはiCal。「Uplisting syncs with Expedia via iCAL (and via the Vrbo integration, but this is not guaranteed」 | https://support.uplisting.io/en/article/expedia-1ghudfv/ | 2026-11-05 | 確認済 |
| Google Vacation Rentals | Operator以上で利用可（Independent Hostは「—」） | https://www.uplisting.io/pricing | 2026-11-05 | 確認済 |
| Agoda | 公式サイト・ヘルプの連携一覧・iCal対応サイト一覧（Expedia／Tripadvisor／Vrbo）に記載なし | https://support.uplisting.io/en/category/ical-booking-sites-6kwpid/ | 2026-11-05 | 未確認（記載なし。対応しないと断定はしない） |
| 楽天トラベル | 公式サイト・連携一覧・ヘルプ・サイトマップを調べたが記載なし | https://www.uplisting.io/integrations | 2026-11-05 | 未確認（記載なし） |
| じゃらん | 同上。記載なし | https://www.uplisting.io/integrations | 2026-11-05 | 未確認（記載なし） |
| その他の接続方式 | 汎用のiCal連携（Partner iCal）あり。「used when a direct API connection is not available」。iCalは定期同期で、APIよりリアルタイム性は劣る可能性（性能の記載は未確認）。日本のOTAをiCalで繋げる手順は公式に記載なし | https://support.uplisting.io/en/article/uplisting-partner-ical-kq812i/ | 2026-11-05 | 確認済（日本OTAとの接続可否は未確認） |

## 4. 機能

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| 自動メッセージ | テンプレート23種（予約直後・到着7日前／3日前／1日前・チェックアウト案内・お礼など）。AIメッセージ（Independent Host／Operatorは100アクション/月、Managerは無制限）、SMS | https://support.uplisting.io/en/article/message-templates-otiybs/ , https://www.uplisting.io/pricing | 2026-11-05 | 確認済 |
| メッセージの言語 | 日本語テンプレートの有無・自動翻訳の有無は、メッセージ関連ヘルプ（テンプレート／AI／SMS）に記載なし。SMS送信番号は米・英・豪・スペインの地域番号 | https://support.uplisting.io/en/article/numbers-regional-behavior-g3yrzg/ | 2026-11-05 | 未確認（日本語対応は記載なし） |
| カレンダー同期（二重予約防止） | 全チャネル統合のマルチカレンダー、iCal連携。「Calendar sync + iCal connections」 | https://www.uplisting.io/pricing | 2026-11-05 | 確認済 |
| 清掃タスク | Cleaning Scheduler（機能ページあり。ヘルプに清掃チーム向け・担当割当方法の記事あり。細部は未確認）。外部連携：Turno（旧TurnoverBnB）、Lula.Cleaning、Cleanster 等 | https://www.uplisting.io/integrations , https://support.uplisting.io/en/category/operations-y639hn/ | 2026-11-05 | 確認済 |
| スマートロック連携先 | Uplisting Smart Locks：August／Yale／Schlage／Kwikset／SmartThings／TTLock／Nuki／Igloohome／Salto。別記事でRemoteLock、連携一覧にMinut等。Akerun・SESAMEは記載なし | https://support.uplisting.io/en/article/automate-guest-access-with-uplisting-smart-locks-16g6006/ | 2026-11-05 | 確認済（日本製ロックの対応は記載なし＝未確認） |
| 価格ツール連携 | PriceLabs、Beyond、Wheelhouse（連携ページあり）、その他の価格ツールはAPI／同期（ヘルプ） | https://www.uplisting.io/integrations/pricelabs , https://support.uplisting.io/en/category/integrations-2qgn4d/ | 2026-11-05 | 確認済 |
| オーナーポータル | Client Owner Portal／オーナー明細（Managerに込み、他は有料アドオン） | https://www.uplisting.io/pricing | 2026-11-05 | 確認済 |
| ダイレクト予約サイト | Basic（全プラン）／Plus（＋£30/月、Managerは込み）。ウェブサイトビルダー。料金表では「Multi-lingual websites」は「Coming soon」、一方ヘルプには「Adding and Managing Site Languages」（Google翻訳での複数言語化）の記事があり、表記が一致しない | https://www.uplisting.io/pricing , https://support.uplisting.io/en/article/adding-and-managing-site-languages-deiamw/ | 2026-11-05 | 確認済（不一致を確認。現行の提供状況は未確認） |
| 会計 | オーナー明細・マネジメント手数料。会計ソフト連携は VRPlatform、ClearSplit、RentReel 等（連携一覧） | https://www.uplisting.io/integrations | 2026-11-05 | 確認済 |
| 保証金（デポジット） | Uplisting Protect（Airbnb／Booking.com／Vrbo／Google VR／直接予約）。Operator以上は込み | https://www.uplisting.io/pricing | 2026-11-05 | 確認済 |
| API | REST API、Webhooks、MCPサーバー、Zapier。全プランで利用可 | https://www.uplisting.io/pricing | 2026-11-05 | 確認済 |
| モバイルアプリ | iOS／Androidあり（ただし利用者レビューに機能が限定的との声あり。下記8章） | https://www.uplisting.io/switch-to-uplisting | 2026-11-05 | 確認済 |
| レポート | 稼働率ダッシュボード等は「don't have dashboards for analytics like occupancy rates, yet」（ヘルプ、2026-05-12更新）。ヘルプには別途「Reports」カテゴリあり | https://support.uplisting.io/en/article/is-uplisting-right-for-me-hjm9f5/ | 2026-11-05 | 確認済（現状の機能範囲は未確認） |

## 5. 日本対応

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| 管理画面（UI）の日本語 | 公式サイト・ヘルプ（言語は English のみ表示）に日本語UIの記載なし | https://support.uplisting.io/en/ | 2026-11-05 | 未確認（ログイン後の画面は開いていない。記載なし） |
| ゲスト向けメッセージの日本語 | 上記のとおり記載なし。直接予約サイトは多言語化機能あり（Google翻訳。要手動確認と公式が注意） | https://support.uplisting.io/en/article/adding-and-managing-site-languages-deiamw/ | 2026-11-05 | 未確認（メッセージ側は記載なし） |
| サポート言語・対応時間 | 窓口はライブチャットとメール（support@uplisting.io）。応答目安はプラン別（Independent Host 2時間／Operator 1時間／Manager 45分）。電話はManagerのみ。対応時間帯・対応言語は記載なし | https://www.uplisting.io/pricing , https://support.uplisting.io/en/article/contacting-support-bm6mt4/ | 2026-11-05 | 確認済（時間帯・言語は未確認） |
| 通貨（JPY） | 請求通貨にJPYなし（上記）。物件の売上通貨でJPYを扱えるかは記載を見つけられず | https://www.uplisting.io/legal/terms-and-conditions | 2026-11-05 | 未確認（JPYでの宿泊料設定は未確認） |
| 決済手段 | ダイレクト予約はStripe。Stripeの対応カード・通貨は未調査 | https://support.uplisting.io/en/article/accept-payments-via-stripe-6um8cf/ | 2026-11-05 | 確認済（Stripe）／日本発行カード等の可否は未確認 |
| 請求書・インボイス | Uplistingからの請求は月次メール請求書（規約）。日本のインボイス制度（適格請求書）への対応記載は見つからず | https://www.uplisting.io/legal/terms-and-conditions | 2026-11-05 | 未確認 |
| 宿泊者名簿・パスポート確認 | ゲスト本人確認（Stripe Identity）：パスポート・運転免許証・国民ID等、「over 4,000 document types from 100+ countries」。本人確認とID書類の収集であり、日本の宿泊者名簿（旅館業法・住宅宿泊事業法の記載事項）の様式を満たすかの記載はなし | https://support.uplisting.io/en/article/guest-identification-verification-11gqur/ | 2026-11-05 | 確認済（日本の名簿要件への適合は未確認） |
| 住宅宿泊事業法に関する機能（届出番号表示、年間180日カウント、定期報告） | 記載なし。Compliance Suiteは書類・許可証の保管と期限管理で、「For UK listings」の必要書類チェックリストのみ | https://www.uplisting.io/property-management-software/short-term-rental-compliance-software | 2026-11-05 | 未確認（日本向け機能の記載なし） |
| 日本の予約サイト | 楽天トラベル・じゃらん・一休等の連携記載なし（3章） | https://www.uplisting.io/integrations | 2026-11-05 | 未確認（記載なし） |
| 日本のスマートロック | Akerun／SESAME 等は記載なし。TTLockはあり | https://support.uplisting.io/en/article/automate-guest-access-with-uplisting-smart-locks-16g6006/ | 2026-11-05 | 未確認（記載なし） |

## 6. アフィリエイト

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| 有無・名称 | あり。「Refer-A-Host」（Refer-a-Host Program） | https://www.uplisting.io/refer-a-host-program | 2026-11-05 | 確認済 |
| 種別 | 自社プログラムをRewardful（getrewardful.com）で運営。申込ボタンのリンク先が uplisting.getrewardful.com | https://www.uplisting.io/refer-a-host-program （ページ内リンク） | 2026-11-05 | 確認済 |
| 申込URL | https://uplisting.getrewardful.com/signup （ページ内の「Apply Now」リンク先。直接開くとCloudflareの確認画面で403、内容は開けず） | https://www.uplisting.io/refer-a-host-program | 2026-11-05 | 確認済（リンク）／申込画面の中身は未確認 |
| 報酬 | 同一ページ内に2つの記載：「earn $300+ on each referral」「Earn $300+ commission for every host you refer」、および「For up to 12 months, you'll get paid 30% of every payment your referrals make」。両者の関係（どちらが適用されるか）は説明なし | https://www.uplisting.io/refer-a-host-program | 2026-11-05 | 確認済（記載）／適用条件は未確認 |
| 提供物 | 固有の紹介リンク、実績ダッシュボード（クリック・成約・支払い）、販促素材 | https://www.uplisting.io/refer-a-host-program | 2026-11-05 | 確認済 |
| 規約上の制限（ブランド名入札禁止、コンテンツ制限、クッキー期間、支払条件、日本居住者の参加可否など） | プログラム規約へのリンクが公式ページにない。Rewardfulの申込画面は403で開けず確認できない。一般の利用規約にも紹介制度の条項なし | https://www.uplisting.io/refer-a-host-program , https://www.uplisting.io/legal/terms-and-conditions | 2026-11-05 | 未確認 |

## 7. 乗り換え

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| 公式の乗り換え手順 | 7ステップ：14日無料トライアル→Airbnbを読み取り専用で接続（リスティング・料金・予約を取り込み、既存ソフトとは干渉しない）→機能確認→無料オンボーディング（30分）→既存の直接予約のインポート→Booking.com・Vrbo接続→既存ソフトを切断しUplistingにAirbnbのフルアクセスを付与 | https://www.uplisting.io/switch-to-uplisting | 2026-11-05 | 確認済 |
| 移行支援 | 全プランに無料の1:1オンボーディング。「We'll walk you through importing your listings, rates and calendars」 | https://www.uplisting.io/pricing | 2026-11-05 | 確認済 |
| 注意（公式の記載） | 「You can only connect one official Airbnb software partner at a time for full access」 | https://www.uplisting.io/switch-to-uplisting | 2026-11-05 | 確認済 |
| 他ツール専用の比較・移行ページ | Guesty／Lodgify／Hostaway／iGMS／Hospitable／Smoobu／Eviivo の「Alternative」ページあり。Beds24、国内ツールからの移行ガイドは見当たらない | https://www.uplisting.io/switch-to-uplisting （フッター） | 2026-11-05 | 確認済 |
| 日本のOTA予約の移行 | 記載なし | — | 2026-11-05 | 未確認 |

## 8. 注意すべき点（利用者の不満・公式内の不一致）

| 項目 | 値 | 出典URL | 取得日 | 確度 |
|---|---|---|---|---|
| 総合評価（参考） | Capterra：4.7（129件） | https://www.capterra.com/p/154137/Uplisting/reviews/ | 2026-11-05 | 第三者のみ（レビューサイトを開いて確認。個別の主張は未検証） |
| 利用者の不満：安定性・サポート | 低評価レビュー（Cons）：「The software is incredibly unstable, and the support structure is highly ineffective.」別のレビュー：「There is no phone support at all」 | https://www.capterra.com/p/154137/Uplisting/reviews/ | 2026-11-05 | 第三者のみ（個別レビューで、検証していない） |
| 利用者の不満：追加費用 | 「The extra subscriptions for things like security make it a very expensive platform」。別のレビュー：本人確認は標準機能にしてほしい、との趣旨 | https://www.capterra.com/p/154137/Uplisting/reviews/ | 2026-11-05 | 第三者のみ（同上） |
| 利用者の不満：機能不足 | 低評価レビューに「No scheduled SMS messages or dynamic tags in direct messaging」「No iCal links for multi-unit listings」等 | https://www.capterra.com/p/154137/Uplisting/reviews/ | 2026-11-05 | 第三者のみ（同上） |
| 公式自身が認める弱点 | 稼働率などの分析ダッシュボードが未提供（ヘルプ、2026-05-12更新）。モバイルアプリは限定的との利用者の声もあり（検索結果の要約のみ） | https://support.uplisting.io/en/article/is-uplisting-right-for-me-hjm9f5/ | 2026-11-05 | 確認済（公式記述）／アプリは第三者のみ |
| 契約条件の食い違い | 料金ページ「No contract」と利用規約「minimum of 12 months／auto-renew」が併存（2章） | https://www.uplisting.io/pricing , https://www.uplisting.io/legal/terms-and-conditions | 2026-11-05 | 確認済 |
| 料金体系の変更が最近 | 料金ページのスクリプト内コメントに「price book, plan version 5」。通貨ごとの価格を修正した旨のコメントあり。価格が頻繁に変わる可能性 | https://www.uplisting.io/pricing | 2026-11-05 | 確認済（コメントの存在）／変更頻度は未確認 |

## 調べられなかったこと（未確認の一覧）

1. 管理画面（ログイン後）の言語設定。日本語UIの有無（公式サイト・ヘルプに記載なし。アカウントは作っていない）
2. ゲスト向け自動メッセージの日本語対応（テンプレートは英語。翻訳機能の記載なし）
3. サポートの対応時間帯と対応言語（応答目安のみ記載。日本語対応は記載なし）
4. 楽天トラベル・じゃらん・Agodaへの対応（公式に記載なし。非対応と断定はできない）
5. JPYでの宿泊料設定・精算、日本発行カードの決済可否、Stripe側の条件
6. 日本のインボイス制度（適格請求書）への対応
7. 住宅宿泊事業法関連（届出番号表示、180日カウント、定期報告）の機能
8. Akerun・SESAMEなど日本製スマートロックとの連携
9. アフィリエイトの規約全文（ブランド名入札禁止・コンテンツ制限・クッキー期間・支払条件）。Rewardfulの申込画面がCloudflareで403のため開けなかった。公式ページ内の報酬記載も2種類あり（$300+ と 30%×12か月）、関係は不明
10. 利用規約「最低12か月」と料金ページ「契約なし」のどちらが現行の実態か（問い合わせないと確定できない）
11. スマートロック料金（£10/月か £4/ロックか）の現行値
12. Plusプランの多言語サイト機能が現在提供されているか（料金表は「Coming soon」）
13. ダイレクト予約でのUplisting側の手数料（従量プラン以外）
14. Trustpilot等、Capterra以外の評価（今回は開いていない）
