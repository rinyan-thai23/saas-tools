# 使い方: python3 -I 05_アフィリ結果反映.py 詳細取得フォルダ
# 詳細取得/アフィリ調査結果.tsv（Web検索で調べた結果）を 製品詳細.tsv のアフィリ列に反映する。
import sys,os
D=sys.argv[1]; R=os.path.join(D,"アフィリ調査結果.tsv"); P=os.path.join(D,"製品詳細.tsv")
res={}
if os.path.exists(R):
    for l in open(R,encoding="utf-8").read().split("\n")[1:]:
        if l: x=l.split("\t"); res[x[0]]=x
L=[l.split("\t") for l in open(P,encoding="utf-8").read().split("\n") if l]
k=L[0].index("アフィリエイト"); n=0
for r in L[1:]:
    if r[0] in res and r[k]=="未調査":
        x=res[r[0]]; r[k:k+6]=[x[2],x[3],x[4],x[5],x[6],x[7]]; n+=1
open(P,"w",encoding="utf-8").write("\n".join("\t".join(r) for r in L)+"\n"); print("反映",n,"件 / 結果ファイル",len(res),"件")
