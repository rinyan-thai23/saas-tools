import re,sys,html
src,out=sys.argv[1],sys.argv[2]
t=open(src,encoding='utf-8').read()
rows={}
for m in re.finditer(r'<a[^>]*href="(/directory/(\d+)/([^"/]+)/software)"[^>]*>(.*?)</a>',t,re.S):
    path,cid,slug,name=m.groups()
    name=html.unescape(re.sub(r'<[^>]+>','',name)).strip()
    name=re.sub(r'\s+',' ',name)
    rows[cid]=(cid,name,slug,"https://www.capterra.jp"+path)
rs=sorted(rows.values(),key=lambda r:int(r[0]))
with open(out,'w',encoding='utf-8') as f:
    f.write("カテゴリID\tカテゴリ名\tスラッグ\tURL\n")
    for r in rs: f.write("\t".join(r)+"\n")
print(len(rs), sum(1 for r in rs if not r[1]))
