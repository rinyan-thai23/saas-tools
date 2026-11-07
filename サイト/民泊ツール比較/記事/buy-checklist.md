---
title: 民泊ツールの申込前チェックリスト：問い合わせ文例つき
slug: buy-checklist
type: 買う直前
products: [guesty, hostaway, lodgify, ownerrez, hospitable, igms, uplisting, beds24, sirvoy]
description: 民泊の管理ツール（PMS・チャネルマネージャー）を申し込む直前に確認する項目を、営業形態・予約サイト・料金・契約・サポート・円と請求書・法令対応の順にまとめた。ベンダーへの問い合わせ文例つき。
cards: [Guesty, Hostaway, Lodgify, OwnerRez, Hospitable, iGMS, Uplisting, Beds24, Sirvoy, 日本のOTA連携-楽天トラベルじゃらん等, 日本の制度-住宅宿泊事業法ほか]
updated: 2026-11-05
pr: true
---

# 民泊ツールの申込前チェックリスト（問い合わせ文例つき）

この記事にはアフィリエイトリンク（PR）が含まれます。内容は公式ページ等の記載（取得日 2026-11-05）に基づき、リンクの有無では変えていません。Sirvoy には申込リンクを付けていません。

> **結論**
> - 順番は、営業形態と予約サイトの条件 → 料金 → トライアル → 契約 → サポート → 円と請求書 → 法令対応です。予約サイト側の条件（営業形態で載せられるか）は、ツールを替えても変わりません。
> - 公式で見つからなかった項目は、「できない」ではなく「聞く」項目です。下の文例を使えます。
> - 届出番号の表示・年180日の管理・定期報告を、ツール本体の機能として公式に確認できた製品はありません。ツール内でやるのか、別の方法でやるのかを自分で決めておきます。

## 1. 先に決める：営業形態と予約サイト

予約サイトが公式に書いている条件です（法律の判断ではありません）。

| 予約サイト | 公式に書かれている条件 |
|---|---|
| 楽天トラベル | 旅館業法の許可を得た施設が対象。「民泊新法（住宅宿泊事業法）の施設様はご参画いただけません」 |
| じゃらんnet | 旅館業法の宿泊営業許可の施設が対象。住宅宿泊事業法の民泊・特区民泊は「ご参画いただけません」 |
| Airbnb | 日本の民泊新法の物件は、ソフト連携で作成したリスティングを受け付けない。例外は日本のAPIパートナー。届出番号は自分でログインして追加する必要がある |

- [ ] 自分の営業形態（届出／許可／特区民泊の認定）で、使いたい予約サイトに載せられるか確認した
- [ ] Airbnb に、既存の掲載をツールにつなげてよいかを確認した（扱いは未確認）。楽天トラベルに民泊を出せるのは Rakuten Oyado だけ、と同社ページにある

楽天トラベル・じゃらんは、民泊新法・特区民泊の施設を対象外と各社が明記しています。旅館業法の許可施設を各ツールにつなげられるかは、各ツールで未確認です。

→ [楽天トラベル・じゃらん連携](/articles/jp-ota-rakuten-jalan/)

## 2. 申込前のチェックリスト

- [ ] **料金**：月額・初期費用・アドオンの内訳を書面で受け取った（Guesty Pro、Hostaway は価格非公開）→ [物件数別の料金](/articles/buy-price-by-listings/)
- [ ] **トライアル**：期間・カード要否・終了後の自動課金を確認した（Hostaway と Guesty Pro は記載を確認できず）→ [無料トライアル比較](/articles/buy-free-trial/)
- [ ] **契約**：最低期間、自動更新、通知期限、中途解約の費用、値上げ時の解約条件を確認した → [契約・解約](/articles/buy-contract-cancel/)
- [ ] **サポート**：日本語と日本時間の窓口があるか書面で確認した（日本語と明記があったのは Beds24 の日本の販売会社のみ。Sirvoy は記載が食い違う）→ [サポート時間](/articles/buy-support-hours-jst/)
- [ ] **ダイレクト予約**：ツール側の手数料率、決済会社の手数料、日本での決済と円の可否を確認した → [ダイレクト予約の手数料](/articles/buy-direct-booking-fees/)
- [ ] **円と請求書**：ツール自身の請求が円か（Guesty は原則USD、Uplisting・Sirvoy・Beds24 公式の請求通貨に JPY なし）、インボイス対応を確認した → [円とインボイス](/articles/jp-yen-invoice/)
- [ ] **管理画面**：海外公式の管理画面は日本語なしが多い前提で、英語で運用できるか試した（Beds24 の日本の販売会社は日本語版あり）
- [ ] **移行**：既存予約の取り込み方法と、切り替え時の停止を聞いた

## 3. 法令対応：ツールでやるか、別の方法か

観光庁・e-Gov の記載です。各製品の公式ページに、年180日・届出番号・定期報告・日本の名簿要件に合う本体機能の記載は見つかりませんでした（ない、と確認したわけではありません）。ID・パスポートを集める機能を持つ製品はありますが（例：Hospitable、Uplisting）、日本の名簿の記載事項に合うかは未確認です。例外は Beds24 の日本の販売会社版で、宿泊者名簿の有料オプション（月¥1,650／施設）と、定期報告のデータを作る無料の外部シート（システム本体の機能ではない）があります。

- [ ] **年180日**：日数は届出住宅ごとに算定（民泊制度ポータルの記載）。上限は法第2条第3項、数え方は規則第3条。カウントの方法を決めた
- [ ] **宿泊者名簿**：日本国内に住所を有しない外国人宿泊者は国籍・旅券番号を記載（規則第7条）。旅券の写しの保存は民泊制度ポータルの記載。名簿は3年間保存。ツール内か外部かを決めた
- [ ] **定期報告**：2か月ごと（偶数月の15日まで、規則第12条）。日数・宿泊者数・国籍別の内訳。作成方法を決めた
- [ ] **届出番号**：予約サイトへの表示を確認した（Airbnb は自分で追加）

→ [住宅宿泊事業法](/articles/jp-minpaku-law/) ／ [宿泊者名簿](/articles/jp-guest-register/)

## 4. 製品ごとに、特に聞くこと

| 製品 | 特に聞くこと |
|---|---|
| Guesty | Lite（1〜3室）と Pro（4室以上）の契約期間・解約金の違い。規約は13か月＋自動更新で、契約書の記載が優先 |
| Hostaway | 価格・契約期間・解約金・トライアル（公式で確認できず） |
| Lodgify | 自動更新前に通知が来ない点と、解約の締め日（画面なら期間終了の1日前、メールなら5日前） |
| Hospitable | 年払いは30日を過ぎると返金なし。Essentials は人間のチャット・メールなし（AI とコミュニティのみ） |
| iGMS | トライアル終了までにプランを選ぶ必要あり。10物件以上は年間契約 |
| Uplisting | 料金ページ（契約なし）と規約（最低12か月）の食い違い |
| Beds24 | 海外公式（€、14日、月末解約）と日本の販売会社 WeIns / Co-Reception（¥、1か月無料、毎月20日締め。日本の販売会社版の情報）のどちらで契約するか |

## 5. 問い合わせ文例

### 英語のベンダー向け（営業・サポート共通）

```
Subject: Questions before signing up (property in Japan, [N] units)

Hello, I operate [N] units in Japan ([registered under the Japanese Minpaku law / licensed under the Hotel Business Act]). Before I sign up, could you confirm the following in writing?
1. Total monthly price, setup/onboarding fee, and any add-ons for [N] units.
2. Minimum term, auto-renewal, notice period, and early termination fee.
3. Is a free trial available for my plan? Is a credit card required?
4. Can I be billed in JPY? If not, which currency?
5. Support: Japanese language? Hours in JST? Phone/chat/email?
6. Can I connect Airbnb listings registered under the Japanese Minpaku law (existing listings)? Rakuten Travel / Jalan?
7. Fees for direct bookings (platform fee and payment processor) and whether Stripe works for a business in Japan.
```

### 日本の販売会社向け（Beds24 の日本の販売会社、日本語）

「[N]室・[営業形態]で利用予定です。月額の総額（国内OTA連携の費用を含む）、契約の主体、受付時間、解約の締め日を教えてください。」

[Guesty](/go/guesty/)（PR）／ [Hostaway](/go/hostaway/)（PR）／ [Lodgify](/go/lodgify/)（PR）／ [OwnerRez](/go/ownerrez/)（PR）／ [Hospitable](/go/hospitable/)（PR）／ [iGMS](/go/igms/)（PR）／ [Uplisting](/go/uplisting/)（PR）／ [Beds24（海外公式。PRリンク）](/go/beds24/)

Beds24 のリンクは海外公式（beds24.com）側の紹介リンクです。日本の販売会社版（日本語UI・円建て・宿泊者名簿オプションなど）の申込は、海外公式のリンクとは別です。

## 未確認のこと

- Hostaway、Guesty Pro の価格・契約・トライアル。円請求の可否
- Airbnb の民泊新法の既存掲載と、各社のソフト連携の関係。例外の日本のAPIパートナー名
- 各製品の年180日・届出番号・定期報告・名簿の機能、インボイス対応（公式で見つからなかった項目。ないと確認したわけではない）
- Lodgify は公式の公開コピー（webflow-mkt.lodgify.com）で確認していて、本体サイトとの一致は未照合

この記事は法的な助言ではありません。制度の判断は観光庁・自治体などの一次資料で確認してください。

## 出典

取得日はすべて 2026-11-05。

- 楽天トラベル：https://travel.rakuten.co.jp/info/hotel_msg.html ／ Rakuten Oyado：https://vacation-stay.com/host.html ／ じゃらんnet：https://www.jalan.net/jalan/doc/howto/10sankaku.html ／ Airbnb：https://www.airbnb.com/help/article/2351 ／ https://www.airbnb.com/help/article/2177
- 法令：https://laws.e-gov.go.jp/law/429AC0000000065 ／ https://laws.e-gov.go.jp/law/429M60000900002 ／ https://www.mlit.go.jp/kankocho/minpaku/overview/minpaku/law1.html ／ https://www.mlit.go.jp/kankocho/minpaku/business/host/responsibility01.html
- 各製品の料金・規約・サポート：https://www.guesty.com/terms-of-service/ ／ https://www.hostaway.com/terms/ ／ https://webflow-mkt.lodgify.com/terms ／ https://www.ownerrez.com/pricing ／ https://help.hospitable.com/en/articles/4596748-how-does-our-pricing-work ／ https://www.igms.com/pricing/ ／ https://www.uplisting.io/legal/terms-and-conditions ／ https://beds24.com/en/company/eula-november ／ https://co-reception.com/pricing/ ／ https://sirvoy.com/pricing

<!-- 追加調査依頼: 各製品の円（JPY）請求の可否（Guesty、Hostaway、Hospitable、iGMS、OwnerRez、Lodgify） -->
<!-- 追加調査依頼: 各製品の年180日管理、届出番号の表示、定期報告、宿泊者名簿・旅券確認の機能の有無 -->
<!-- 追加調査依頼: 各製品の適格請求書（インボイス）発行への対応 -->
<!-- 追加調査依頼: Airbnb の日本のAPIパートナー名と、既存の民泊新法掲載をソフト連携につなげる場合の扱い -->
<!-- 追加調査依頼: 英語の問い合わせ文例に対する各社の実際の回答（サポート言語・日本時間）で、記事の未確認項目を更新 -->
