# 製品詳細ページ（1ページ目のみ）を取得し、概要・言語・国内製品・代替製品・レビュー5件を抽出する。
# 使い方: python3 -I 03_詳細取得.py 入力ユニーク一覧.tsv 出力フォルダ [最小レビュー数=100] [件数上限]
# 途中で止まっても出力フォルダの .done から再開できる。403が出たら止まる。
import re,sys,os,time,random,html,urllib.request,urllib.error
UA="Mozilla/5.0 (compatible; personal-research-script; low-rate)"
DMIN,DMAX=8.0,22.0
def clean(s): return re.sub(r"\s+"," ",html.unescape(s)).strip()
def text(s):
    s=re.sub(r"<script.*?</script>|<style.*?</style>|<svg.*?</svg>","",s,flags=re.S)
    return clean(re.sub(r"<[^>]+>"," ",s))
def parse(t,pid,name):
    x=text(t); r={}
    r["国内製品"]="あり" if "国内製品" in x else "なし"
    note=""
    langs=[]
    m=re.search(r'id="offcanvas-[^"]*Label"[^>]*>\s*言語\s*</h5>.*?<ul[^>]*>(.*?)</ul>',t,re.S)
    if m: langs=[clean(re.sub(r"<[^>]+>","",l)) for l in re.findall(r"<li[^>]*>(.*?)</li>",m.group(1),re.S)]
    else:
        m=re.search(r'<h4[^>]*>\s*言語.*?</h4>\s*<p[^>]*>(.*?)</p>',t,re.S)
        if m: langs=[l.strip() for l in re.split(r"[,、]",re.sub(r"<[^>]+>","",clean(m.group(1)))) if l.strip()]
        else: note+="言語欄なし;"
    r["言語"]=";".join(langs); r["日本語対応"]="あり" if "日本語" in langs else ("なし" if langs else "不明")
    m=re.search(r'id="productOverview"[^>]*>(.*?)(?:readmore-lines__link|</section>)',t,re.S)
    ov=text(m.group(1)) if m else ""
    if not ov:
        m=re.search(r"の概要：(.{0,1500})",x); ov=m.group(1) if m else ""; note+="概要は代替抽出;" if ov else "概要なし;"
    r["概要"]=ov[:1500]
    a=t.find('id="alternatives"'); b=t.find('id="reviews"')
    alts=[]
    if a>=0 and b>a:
        sec=t[a:b]
        for m in re.finditer(r'<img alt="([^"]+)" class="img-fluid position-absolute',sec):
            n=clean(m.group(1))
            if n and n not in alts: alts.append(n)
        ids=[]; [ids.append(i) for i in re.findall(r'href="/software/(\d+)/',sec) if i not in ids and i!=pid]
        r["代替製品ID"]=";".join(ids)
    else: r["代替製品ID"]=""; note+="代替欄なし;"
    r["代替製品"]=";".join(alts)
    k=t.find("この製品の関連カテゴリー"); cats=[]
    if k>=0:
        for m in re.finditer(r'<a[^>]*href="/directory/(\d+)/[^"]+"[^>]*>(.*?)</a>',t[k:k+6000],re.S):
            n=text(m.group(2))
            if n and n not in cats: cats.append(n)
    r["関連カテゴリ"]=";".join(cats)
    # reviews
    revs=[]
    if b>=0:
        rx=text(t[b:])
        first=rx.find("投稿経路")
        anc=rx.rfind("並び順： 関連性 新着順",0,first if first>=0 else len(rx))
        body=rx[anc+len("並び順： 関連性 新着順"):] if anc>=0 else rx
        parts=[]
        for n,seg in enumerate(body.split("投稿経路")[:-1]):
            parts.append(seg if n==0 else seg.rsplit("日本語に翻訳する",1)[-1])
        for p in parts:
            dm=re.search(r"(\d{4}年\d{1,2}月\d{1,2}日)",p)
            tm=re.search(r'"(.{2,200})"\s*(?=\d{4}年)',p) or re.search(r'“([^”]{2,200})”',p)
            head=p[:dm.start()].strip() if dm else p[:200]
            rt=re.search(r"\d{4}年\d{1,2}月\d{1,2}日\s*([\d.]+)",p)
            pros=re.search(r"良いポイント:\s*(.*?)(?:改善してほしい点:|$)",p); cons=re.search(r"改善してほしい点:\s*(.*)$",p)
            revs.append(dict(タイトル=tm.group(1) if tm else "",日付=dm.group(1) if dm else "",評価=rt.group(1) if rt else "",
                投稿者=head[:200],良い点=(pros.group(1).strip() if pros else p[-600:])[:1500],改善点=(cons.group(1).strip() if cons else "")[:1500]))
    r["レビュー"]=revs[:5]; r["備考"]=note
    return r
def get(u):
    for a in range(4):
        try:
            time.sleep(random.uniform(DMIN,DMAX)+(random.random()<0.05)*random.uniform(20,60))
            return urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":UA}),timeout=40).read().decode("utf-8")
        except urllib.error.HTTPError as e:
            log(f"HTTP {e.code} {u}")
            if e.code==403: raise SystemExit("blocked 403")
            if e.code==404: return None
            time.sleep(30*(a+1))
        except Exception as e:
            log(f"ERR {e} {u}"); time.sleep(30*(a+1))
    raise SystemExit("too many errors "+u)
def log(s): open(os.path.join(OUT,"取得.log"),"a").write(time.strftime("%H:%M:%S ")+s+"\n")
if __name__=="__main__":
    src,OUT=sys.argv[1],sys.argv[2]; dmin=int(sys.argv[3]) if len(sys.argv)>3 else 100; lim=int(sys.argv[4]) if len(sys.argv)>4 else 10**9
    os.makedirs(OUT,exist_ok=True); D=os.path.join(OUT,".done")
    done=set(open(D).read().split()) if os.path.exists(D) else set()
    P=os.path.join(OUT,"製品詳細.tsv"); R=os.path.join(OUT,"レビュー1ページ目.tsv")
    fp=open(P,"a",encoding="utf-8"); fr=open(R,"a",encoding="utf-8")
    if os.path.getsize(P)==0: fp.write("製品ID\t製品名\t製品URL\tレビュー数\t評価\t国内製品\t日本語対応\t言語\t概要\t関連カテゴリ\t代替製品\t代替製品ID\t取得レビュー数\t備考\n")
    if os.path.getsize(R)==0: fr.write("製品ID\t製品名\t順番\tタイトル\t日付\t評価\t投稿者\t良い点\t改善点\n")
    rows=[l.split("\t") for l in open(src,encoding="utf-8").read().split("\n")[1:] if l]
    rows=[r for r in rows if r[2] and int(r[2])>=dmin]; n=0
    for r in rows:
        pid,name,rv,rt,url=r[0],r[1],r[2],r[3],r[4]
        if pid in done: continue
        if n>=lim: break
        n+=1; t=get(url)
        if t is None: log(f"404 {pid} {name}"); open(D,"a").write(pid+"\n"); continue
        d=parse(t,pid,name)
        f=lambda s:s.replace("\t"," ").replace("\n"," ")
        fp.write("\t".join(map(f,[pid,name,url,rv,rt,d["国内製品"],d["日本語対応"],d["言語"],d["概要"],d["関連カテゴリ"],d["代替製品"],d["代替製品ID"],str(len(d["レビュー"])),d["備考"]]))+"\n"); fp.flush()
        for i,v in enumerate(d["レビュー"],1):
            fr.write("\t".join(map(f,[pid,name,str(i),v["タイトル"],v["日付"],v["評価"],v["投稿者"],v["良い点"],v["改善点"]]))+"\n")
        fr.flush(); open(D,"a").write(pid+"\n"); log(f"ok {pid} {name} 日本語={d['日本語対応']} 国内={d['国内製品']} rev={len(d['レビュー'])} {d['備考']}")
    log("FINISHED" if n<lim else "limit")
