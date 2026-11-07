# 校閲レポート：alt-ownerrez

- 校閲日：2026-11-07 ／ 照合カード：OwnerRez、Hospitable、iGMS、Beds24、Lodgify、Hostaway、日本のOTA連携、日本の制度
- 件数：要修正 0 ／ 注意 6 ／ 軽微 3
- 全般：PR表記あり。/go/ は beds24・lodgify・hostaway・hospitable・igms のみ（Sirvoy・Hostfully への /go/ なし、それ以外の広告リンクなし）。内部リンク `/articles/jp-yen-invoice/` は存在。

## 指摘

### 注意

1. **「ない」と書いているが、カードは「記載なし」**
   - 記事（結論1）：「日本語UI・日本向けの記載・サポートの対応時間がない」
   - カード OwnerRez：サポート「対応時間・対応言語は公式に記載なし」（確認済・時間は未確認）。UI は言語一覧に日本語が挙がっていない。
   - 修正案：「日本語UIが一覧にない／日本向けの記載・サポートの対応時間の記載が見つからなかった」。

2. **料金の優劣の結論が、無料プラン・年払いを含めると崩れる**
   - 記事（結論3）：「料金は、表の範囲で OwnerRez が Hospitable・iGMS より低い（アドオン別）」
   - カード：Hospitable Essentials は基本 $0・物件数無制限（機能制限あり）、iGMS PRO 年払いは5室 約$87（OwnerRez $88 より低い）、iGMS FLEX／無料プランあり。表は Professional／Mogul と PRO 月払いだけ。
   - 修正案：「月払いの有料プランの比較（Hospitable Essentials $0・iGMS 無料／FLEX・年払いは除く）」と範囲を明記する。

3. **Lodgify の Expedia の食い違いを落としている**
   - 記事（条件別）：「Lodgify は FAQ で API と記載」
   - カード Lodgify：Expedia は「チャネルマネージャーページの FAQ は API、料金ページの機能表に Expedia の記載なし。両ページで記述が異なる」（確認済・記述の食い違いあり）。
   - 修正案：「Lodgify は FAQ では API、料金ページの機能表には Expedia の記載がなく食い違い」と書く。

4. **Hospitable の日本語メッセージを「未対応のまま」と断定**
   - 記事（要点）：「日本語の追加要望は未対応のまま」
   - カード Hospitable：要望は「2026-06-08 投稿、取得時のステータス『New』、票1」。「日本語が実装済みかは未確認」。
   - 修正案：「日本語の追加要望のステータスは『New』（2026-11-05 取得時）」。

5. **宿泊者名簿の一文が候補のカードと合わない**
   - 記事：「各候補の本体機能は、Beds24 日本側の有料オプション以外は記載が見つからなかった」
   - カード：Beds24 は Pre-Arrival tool（パスポート収集）・公式の宿泊者登録フォームあり、Hospitable はゲスト確認（ID撮影）、Lodgify は Guest Registration、Hostaway はマーケットプレイスに Chekin 等（いずれも日本の名簿要件との適合は未確認）。
   - 修正案：「日本の名簿要件に合う本体機能の記載は…見つからなかった（ID収集の機能は複数あるが適合は未確認）」。

6. **Beds24 の楽天の接続方式・/go/beds24/ の遷移先**
   - 記事（比較表）：「楽天は Rakuten Oyado 経由、じゃらんは日本の販売会社が提供」／結論の「[Beds24](/go/beds24/)（日本の販売会社経由）」
   - カード：楽天は公式Wiki（Vacation STAY＝Rakuten Oyado 経由）と日本の販売会社（R-Connect＋Rakuten for Business）で記述が併存し「現行は未確認」。紹介制度は海外公式の referrercode 方式で、日本の販売会社の紹介制度は未確認。
   - 修正案：楽天の方式を「公式Wikiでは〜、現行は未確認」と併記。リンクが海外公式に飛ぶ可能性があるなら、文言を「Beds24（海外公式）」にし、日本の販売会社の説明は別扱いにする。

### 軽微

7. 結論2は「Lodgify・Hostaway」を立ち上げ支援の候補とするが、条件別の表では「Hospitable／Lodgify／Hostaway」。Hospitable の無料オリエンテーション通話（カード確認済）を結論にも入れるか、表に合わせる。
8. 条件別「Hostaway も API」→ カードでは API 接続は「比較ページ（自社の主張）」。チャネル一覧には Expedia が載るのは確認済。修正案：「自社の説明では API」。
9. 「ドアロック連携（1台月$4）」→ カードでは直接連携の Schlage・Igloohome・Hubitat のみが1台あたり月$4。修正案：「Schlage／Igloohome／Hubitat の直接連携は1台月$4」。

## 指摘なし（照合して一致を確認した主張）

約40件。主なもの：OwnerRez 5室 $88・10室 $127・20室 $196、1物件目 $40、契約なし・返金なし・カードのみ、11言語に日本語なし、通貨は1物件1つ（2023年の社員回答）、Jumpstart 通話、学習コスト（公式サイト上のレビュー題）、閉鎖時の挙動、iCal 併用不可。Hospitable／iGMS／Beds24／Uplisting 相当の料金・契約・Capterra 数値（Lodgify 1,312／4.5、Hostaway 1,623／4.8 を含む）、Beds24 の計算式と条件、Lodgify の1%・自動更新・EUR/USD/GBP、Hostaway の「24/7の電話」の自社主張・導入費 $500 の自社主張、楽天／じゃらん・Airbnb ヘルプ・旅券の記述。
