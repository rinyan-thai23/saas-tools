# 1製品の口コミ(良い点/改善点)を、関連性順で上位N件取る。Capterra日本の製品ページ ?page=N を使う(1ページ5件)。
# 注意: robots.txt に反する取得(利用者が自己責任で実施を指示)。間隔は長めに空ける。403が出たら止まる。
# 使い方: python3 -I 取得スクリプト/08_口コミ関連順100件.py 製品ID 製品名 製品URL 出力フォルダ [件数=100] [並び順: 空=関連順 / most_recent=新着順]
import sys, os, time, random, importlib.util
here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("detail", os.path.join(here, "03_詳細取得.py"))
d = importlib.util.module_from_spec(spec); spec.loader.exec_module(d)
d.OUT = sys.argv[4]; d.DMIN, d.DMAX = 3.0, 6.0   # 03 の get() が使う間隔
pid, name, url, out = sys.argv[1:5]; want = int(sys.argv[5]) if len(sys.argv) > 5 else 100
sort = sys.argv[6] if len(sys.argv) > 6 else ""
q = lambda page: [f"page={page}"] * (page > 1) + ([f"sort={sort}"] if sort else [])
os.makedirs(out, exist_ok=True)
rows, seen = [], set()
for page in range(1, (want + 4) // 5 + 1):
    qs = "&".join(q(page)); t = d.get(url + ("?" + qs if qs else ""))
    if t is None: print("404", page); break
    revs = d.parse(t, pid, name)["レビュー"]
    new = [r for r in revs if (r["タイトル"], r["日付"], r["投稿者"]) not in seen]
    print(f"page {page}: {len(revs)}件 (新規{len(new)})", flush=True)
    if not new: break
    for r in new: seen.add((r["タイトル"], r["日付"], r["投稿者"])); rows.append(r)
    if len(rows) >= want: break
rows = rows[:want]
f = lambda s: str(s).replace("\t", " ").replace("\n", " ")
path = os.path.join(out, f"{pid}_{name}{"_" + sort if sort else ""}.tsv")
with open(path, "w", encoding="utf-8") as fo:
    fo.write("製品ID\t製品名\t関連順\tタイトル\t日付\t評価\t投稿者\t良い点\t改善点\n")
    for i, r in enumerate(rows, 1):
        fo.write("\t".join(map(f, [pid, name, i, r["タイトル"], r["日付"], r["評価"], r["投稿者"], r["良い点"], r["改善点"]])) + "\n")
print(f"{len(rows)}件 → {path}")
