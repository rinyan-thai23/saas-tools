import re,json,html,time,sys,os,urllib.request,urllib.error,math
UA="Mozilla/5.0 (compatible; personal-research-script; low-rate)"
import random
CATS=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","データ","01_カテゴリ.tsv")
OUT=sys.argv[1]; LIMIT=int(sys.argv[2]) if len(sys.argv)>2 else 10**9
DONE=OUT+".done"; LOG=OUT+".log"
def log(s):
    open(LOG,"a").write(time.strftime("%H:%M:%S ")+s+"\n")
def get(u):
    for a in range(5):
        try:
            time.sleep(random.uniform(1.5,5.0)+(random.random()<0.05)*random.uniform(10,25))
            return urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":UA}),timeout=40).read().decode("utf-8")
        except urllib.error.HTTPError as e:
            log(f"HTTP {e.code} {u}")
            if e.code in (403,): 
                if a>=2: raise SystemExit("blocked 403")
            if e.code==404: return None
            time.sleep(10*(a+1))
        except Exception as e:
            log(f"ERR {e} {u}"); time.sleep(10*(a+1))
    raise SystemExit("too many errors "+u)
def clean(s): return re.sub(r"\s+"," ",html.unescape(s)).strip()
def parse(t):
    items=[]
    for m in re.finditer(r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>',t,re.S):
        try: d=json.loads(m.group(1))
        except: continue
        if d.get("@type")=="ItemList": items=d["itemListElement"]
    rating={}
    for m in re.finditer(r'href="/software/(\d+)/[^"#]+#reviews"((?:(?!#reviews").)*?)</a>',t,re.S):
        mm=re.search(r'<span class="ms-1">\s*([\d.]+)\s*</span>.*?<span>\s*\(([\d,]+)\)',m.group(2),re.S)
        if mm: rating[m.group(1)]=(mm.group(1),mm.group(2).replace(",",""))
    rows=[]
    for it in items:
        mm=re.search(r"/software/(\d+)/",it.get("url",""))
        pid=mm.group(1) if mm else ""
        r=rating.get(pid,("",""))
        rows.append((pid,clean(it.get("name","")),it.get("url",""),r[0],r[1],clean(it.get("description",""))))
    return rows
done=set(open(DONE).read().split()) if os.path.exists(DONE) else set()
new=not os.path.exists(OUT)
f=open(OUT,"a",encoding="utf-8")
if new: f.write("カテゴリID\tカテゴリ名\t製品ID\t製品名\t製品URL\t評価\tレビュー数\t説明\n")
cats=[l.rstrip("\n").split("\t") for l in open(CATS,encoding="utf-8").read().splitlines()[1:]]
n=0
for cid,cname,slug,url in cats:
    if cid in done: continue
    if n>=LIMIT: break
    n+=1
    t=get(url)
    if t is None: log(f"cat {cid} 404"); open(DONE,"a").write(cid+"\n"); continue
    m=re.search(r"キャプテラでは、([\d,]+)の",t)
    total=int(m.group(1).replace(",","")) if m else None
    pages=math.ceil(total/25) if total else None
    p=1; cnt=0
    while True:
        if p>1:
            t=get(f"{url}?page={p}")
            if t is None: break
        rows=parse(t)
        for r in rows:
            f.write("\t".join([cid,cname]+list(r))+"\n"); cnt+=1
        f.flush()
        if len(rows)<25: break
        if pages and p>=pages: break
        p+=1
    log(f"cat {cid} {cname} total={total} got={cnt} pages={p}")
    open(DONE,"a").write(cid+"\n")
log("FINISHED" if n<LIMIT else "limit reached")
