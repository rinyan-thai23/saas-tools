# 校閲レポート：switch-airbnb-only-to-channel-manager

- 校閲日：2026-11-07 ／ 照合カード：Guesty、Hostaway、Lodgify、OwnerRez、Hospitable、iGMS、Uplisting、Beds24、日本のOTA連携、日本の制度
- 件数：要修正 0 ／ 注意 2 ／ 軽微 4
- 全般：PR表記あり。/go/ は hospitable・igms・guesty・ownerrez・beds24・hostaway・uplisting（Sirvoy・Hostfully への /go/ なし、それ以外の広告リンクなし）。内部リンク `/articles/switch-checklist-double-booking/` は存在。結論（民泊新法リスティングの扱いは未確認、届出番号は自分で登録、3室の月額）と本文に食い違いなし。法的断定なし（「法的な助言ではありません」の注記あり）。

## 指摘

### 注意

1. **見出しが引用より強い（Hospitable のカードと衝突）**
   - 記事（切り替えの流れ3）：「**Airbnb につなぐツールは1つ。** Uplisting の公式ページに『フルアクセスで接続できる Airbnb の公式ソフトは同時に1つ』とあります。」
   - カード：Uplisting の原文は「one official Airbnb software partner at a time for full access」。Hospitable「試用しながら準備」＝Airbnb・Vrbo は制限付き接続で旧PMSと併用可（価格・空室管理は Hospitable を主接続にする必要）。同じ記事の手順1でも Uplisting は読み取り専用接続から始める。
   - 修正案：見出しを「フルアクセスで接続できるツールは1つ」に直し、Hospitable の「制限付き接続で併用可」を一言添える。

2. **/go/beds24/ と「日本の販売会社（株式会社WeIns）経由」の不一致の可能性**
   - 記事（条件別）：「公式で確認できたのは、[Beds24](/go/beds24/) の日本の販売会社（株式会社WeIns）経由のみ」
   - カード：Beds24 の紹介制度は海外公式の referrercode 方式。日本の販売会社の紹介制度は未確認。
   - 修正案：遷移先が WeIns でないなら、リンクは「Beds24（海外公式）」とし、日本の販売会社の説明はリンクなしで書く。

### 軽微

3. 3室の表「Guesty Lite ｜ $27＋予約の1%」→ カード：Lite 料金ページに「Limited time offer」の表示あり。修正案：備考に「期間限定表示あり」。
4. 3室の表「iGMS ｜ Free は $0」→ カード：無料プランは「pilot」で「it may change」。修正案：備考に「試験提供」（switch-spreadsheet-to-pms には記載あり）。
5. 申込前チェック「請求通貨が円か…（円の請求を確認できた製品は少ない）」→ カード：円建て請求を確認できたのは Beds24 の日本の販売会社のみ。修正案：「確認できたのは Beds24 の日本の販売会社のみ」。
6. 申込前チェック「日本語の管理画面が無い前提（Beds24 の日本の販売会社を除く）」→ カード：Hostaway・Lodgify・Uplisting の管理画面の日本語は「記載なし／未確認」で、無いと確認したわけではない。修正案：「日本語の管理画面は確認できていない前提」。

## 指摘なし（照合して一致を確認した主張）

約40件。主なもの：Airbnb ヘルプ 2351（ソフト連携リスティング不可・日本のAPIパートナー例外）、2177（届出番号は自分でログイン登録、旅館業法・特区は代替入力可）、Preferred+ の掲載製品と iGMS の等級不明、楽天・じゃらんの参画不可と Rakuten Oyado、3室の月額（Guesty Lite $27＋1%、Hospitable $0／$74、iGMS 約$70、Uplisting £72／従量 £0＋3%（10物件まで）、OwnerRez $70・最低$40、Beds24 公式 €24.00・日本の販売会社は1室の例 ¥4,580〜で3室の例なし）、各トライアル日数とカード不要、Hospitable の過去予約5,000件・結合、OwnerRez の掲載情報1回インポート、iGMS の手動ブロック口コミ（2026-07・真偽未検証の注記）、Uplisting の「No contract」と規約「最低12か月」の併記、Hostaway・Guesty Pro は見積り、Lodgify 3室は未確認。
