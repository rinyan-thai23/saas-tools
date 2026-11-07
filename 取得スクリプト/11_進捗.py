# 旧記事の作り直し進捗。作り直し済み = type が商品以外で、updated が 2026-11-07 以降かつタイトルに『民泊』あり
import re, glob, os, time
d = "docs/民泊ツール比較/記事"; done, todo = [], []
for f in sorted(glob.glob(d + "/*.md")):
    s = open(f, encoding="utf-8").read(); slug = os.path.basename(f)[:-3]
    if re.search(r"^type: 商品", s, re.M): continue
    ok = "民泊" in re.search(r"title: (.*)", s).group(1) and re.search(r"updated: (2026-11-(0[7-9]|[123]\d)|2026-12|2027)", s)
    (done if ok else todo).append((slug, os.path.getmtime(f)))
print(f"作り直し済み {len(done)} / 全{len(done)+len(todo)}  残り {len(todo)}")
if done: print("最新:", max(done, key=lambda x: x[1])[0], time.strftime("%H:%M", time.gmtime(max(x[1] for x in done))), "UTC")
print("残り:", " ".join(s for s, _ in todo))
