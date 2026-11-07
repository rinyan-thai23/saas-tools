# 商品ページ用の下調べ。口コミTSV(05_口コミ)を集計し、公式サイトの指定ページ本文を保存して先頭を表示する。
# 使い方: python3 -I 取得スクリプト/09_商品調査.py <口コミTSV> <公式URL1> [公式URL2 ...]
import sys, re, csv, html, time, urllib.request
from collections import Counter
tsv, urls = sys.argv[1], sys.argv[2:]
r = list(csv.DictReader(open(tsv, encoding="utf-8"), delimiter="\t")); n = len(r)
print(f"## 口コミ {n}件")
T = {'サポート':'support|customer service','オンボーディング':'onboarding','連携・同期':'integrat|sync|channel|calendar','自動化':'automat','価格':'pric|cost|expens|fee|bill|charge','使いやすさ':'easy|intuitive|user.friendly','学習':'learning curve|complex|overwhelm|steep','UI':'interface|clunky|\\bui\\b|dated','レポート・会計':'report|account|owner statement|invoice','メッセージ':'messag|inbox|template','不具合':'bug|glitch|crash|slow|error'}
for k, v in T.items():
    a = sum(1 for x in r if re.search(v, x['良い点'], re.I)); b = sum(1 for x in r if re.search(v, x['改善点'], re.I))
    print(f"{k}: 良い{a}({a*100//n}%) 改善{b}({b*100//n}%)")
j = ' '.join(x['投稿者'] for x in r)
print("規模:", Counter(re.findall(r'(\d+～\d+人規模|\d+人以上規模|自営業)', j)).most_common(6))
print("使用期間:", Counter(re.findall(r'使用期間： (\S+(?: \S+)?)', j)).most_common(6))
c = Counter(x['評価'] for x in r); low = c['1.0'] + c['2.0']
print("評価:", dict(c), f"低評価{low}件({low*100//n}%)")
print("## 低評価(1-2点)")
for x in r:
    if x['評価'] in ('1.0', '2.0'): print(x['日付'], x['評価'], x['タイトル'], '|', x['改善点'][:230].replace('\n', ' '))
print("\n## 公式サイト")
for u in urls:
    try:
        t = urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), timeout=40).read().decode("utf-8", "ignore")
    except Exception as e:
        print(u, "ERR", e); continue
    t = re.sub(r'<script.*?</script>|<style.*?</style>|<svg.*?</svg>', '', t, flags=re.S)
    x = html.unescape(re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', t)))
    print(f"\n### {u} ({len(x)}字)\n{x[:1800]}"); time.sleep(2)
