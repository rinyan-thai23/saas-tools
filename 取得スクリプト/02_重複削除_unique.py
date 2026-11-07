# 使い方: python3 -I 02_重複削除_unique.py 入力.tsv 出力.tsv
# 製品IDで重複を削除し、レビュー数の多い順に並べる。掲載カテゴリは「;」でまとめる。
import sys,collections
src,out=sys.argv[1],sys.argv[2]
L=[l for l in open(src,encoding="utf-8").read().split("\n") if l][1:]
g=collections.OrderedDict()
conf=0
for l in L:
    cid,cname,pid,name,url,rt,rv,desc=l.split("\t")
    if pid not in g:
        g[pid]=dict(name=name,url=url,rt=rt,rv=rv,desc=desc,cats=[])
    else:
        d=g[pid]
        if (d["rt"],d["rv"])!=(rt,rv): conf+=1
        if not d["rt"] and rt: d["rt"],d["rv"]=rt,rv
        if len(desc)>len(d["desc"]): d["desc"]=desc
    g[pid]["cats"].append((cid,cname))
rows=sorted(g.items(),key=lambda kv:-int(kv[1]["rv"] or 0))
with open(out,"w",encoding="utf-8") as f:
    f.write("製品ID\t製品名\tレビュー数\t評価\t製品URL\t掲載カテゴリ数\tカテゴリID\tカテゴリ名\t説明\n")
    for pid,d in rows:
        f.write("\t".join([pid,d["name"],d["rv"],d["rt"],d["url"],str(len(d["cats"])),
            ";".join(c[0] for c in d["cats"]),";".join(c[1] for c in d["cats"]),d["desc"]])+"\n")
print(len(rows),"unique; rating/review conflicts:",conf)
