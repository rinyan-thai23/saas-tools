# 記事1本の自動チェック。使い方: python3 -I 取得スクリプト/10_記事チェック.py 記事のmdパス
# 1) タイトルにジャンル名(民泊)  2) 内部リンクが実在  3) 禁句  4) 本文の金額($/€/£/¥)が商品ページ(type: 商品)のどれかに載っているか
import sys, re, glob, os
p = sys.argv[1]; d = os.path.dirname(os.path.abspath(p))
t = open(p, encoding="utf-8").read(); out = []
m = re.match(r"---\n(.*?)\n---\n(.*)", t, re.S); fm, body = m.group(1), m.group(2)
title = re.search(r"title: (.*)", fm).group(1)
if "民泊" not in title: out.append(f"タイトルに『民泊』なし: {title}")
slugs = {os.path.basename(f)[:-3] for f in glob.glob(d + "/*.md")}
for h in re.findall(r"\]\(/articles/([^/)]+)/\)", body):
    if h not in slugs: out.append(f"リンク先なし: /articles/{h}/")
for w in ["事実カード", "追加調査依頼", "TODO", "確認できました。", "という意味です"]:
    if w in body: out.append(f"禁句: {w}")
prod = ""
for f in glob.glob(d + "/*.md"):
    s = open(f, encoding="utf-8").read()
    if re.search(r"^type: 商品", s, re.M): prod += s
nums = set(re.findall(r"[\$€£¥][\d,]+(?:\.\d+)?", body))
miss = sorted(n for n in nums if n not in prod and n.replace(",", "") not in prod.replace(",", ""))
if miss: out.append("商品ページに無い金額(計算値なら本文に『計算』と書く): " + " ".join(miss))
print("OK" if not out else "\n".join(out))
