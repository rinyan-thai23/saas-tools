# 使い方: python3 -I 07_自社サイト再確認.py 詳細取得フォルダ [件数上限]
# 06 で「未検出」だった製品を、(1) 公式ドメインが不明なら製品名から推測して確認し、(2) 追加のパス（/partners など）と sitemap.xml を調べて再確認する。
# 見つかったものは アフィリ調査結果.tsv に追記。見つからなかったものは 自社再確認_なし.txt に製品IDを残す（検索ツールで調べる対象）。
import sys,os,re,time,random,html,urllib.parse
src=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"06_自社サイト確認.py"),encoding="utf-8").read().split("done=set();")[0]
exec(src)
NO2=os.path.join(D,"自社再確認_なし.txt"); LOG2=os.path.join(D,"自社サイト再確認.log")
log2=lambda s:open(LOG2,"a").write(time.strftime("%H:%M:%S ")+s+"\n")
def guess_domain(name):
    n=norm(name); w=norm(re.split(r"[\s\-–:/(]+",name.strip())[0])
    base=[]
    for x in (n,w):
        if x and len(x)>=3 and x not in base: base.append(x)
    cands=[]
    for x in base:
        for d in (x+".com",x+".io",x+".co",x+".net",x+".app","get"+x+".com","use"+x+".com","try"+x+".com",x+"hq.com",x+".ai"): cands.append(d)
    for d in cands[:14]:
        u,t=fetch("https://"+d+"/")
        if not t: continue
        m=re.search(r"<title[^>]*>(.*?)</title>",t,re.S|re.I); title=norm(m.group(1)) if m else ""
        og=re.search(r'property="og:site_name"\s+content="([^"]+)"',t,re.I); og=norm(og.group(1)) if og else ""
        if (w and (w in title or w in og)) and len(t)>3000 and "domainforsale" not in norm(t[:3000]) and "thisdomain" not in norm(t[:3000]):
            return "https://"+host_of(u).split(":")[0]
    return None
EXTRA=("/affiliate-program","/affiliates-program","/partner-program","/partners","/partner","/referral","/referral-program","/refer","/become-an-affiliate","/company/affiliates","/en/affiliates","/en/affiliate")
def check_more(base):
    seen=[]; best=None
    su,sm=fetch(base+"/sitemap.xml")
    if sm:
        for m in re.finditer(r"<loc>([^<]+)</loc>",sm):
            u=html.unescape(m.group(1)).strip()
            if re.search(r"affiliate|referral|partner-program|become-a-partner",u,re.I) and u not in seen: seen.append(u)
    for g in EXTRA:
        u=base+g
        if u not in seen: seen.append(u)
    tried=0
    for u in seen:
        if tried>=8: break
        lab=is_net(host_of(u))
        if lab: return ("あり",lab+"（第三者）",u,"sitemap に第三者ネットワークのURL")
        if not allowed(u): continue
        tried+=1; fu,body=fetch(u)
        if not fu or not body: continue
        v,nets=evaluate(fu,body)
        if v:
            kind=(("／".join(sorted(nets))+"（第三者）") if nets else "自社")
            cand=(v,kind,fu,"公式サイトの追加パス／sitemap で検出（自動判定）")
            if v=="あり": return cand
            best=best or cand
    return best
R=os.path.join(D,"アフィリ調査結果.tsv"); NO=os.path.join(D,"自社確認済_なし.txt")
res_ids={l.split("\t")[0] for l in open(R,encoding="utf-8").read().split("\n")[1:] if l}
done2=set(l.strip() for l in open(NO2,encoding="utf-8")) if os.path.exists(NO2) else set()
doms={l.split("\t")[0]:l.split("\t")[2] for l in open(DOM,encoding="utf-8").read().split("\n")[1:] if l and len(l.split("\t"))>2}
names={l.split("\t")[0]:l.split("\t")[1] for l in open(os.path.join(D,"製品詳細.tsv"),encoding="utf-8").read().split("\n") if l}
T=[i for i in (l.strip() for l in open(NO,encoding="utf-8")) if i and i not in res_ids and i not in done2]
SH=os.environ.get("SHARD","0/1").split("/"); T=[t for k,t in enumerate(T) if k%int(SH[1])==int(SH[0])]
today=time.strftime("%Y-%m-%d"); n=0
for i in T:
    if n>=LIM: break
    n+=1; nm=names[i]; base=doms.get(i) or ""; how="既知"
    if not base: base=guess_domain(nm) or ""; how="推測"
    res=None
    if base:
        try: res=check_site(base) or check_more(base)
        except Exception as e: log2("ERR %s %s"%(nm,e))
    if res:
        open(R,"a",encoding="utf-8").write("\t".join([i,nm,res[0],res[1],res[2],res[3],today,"再確認 ドメイン:"+base+"（"+how+"）"])+"\n"); log2("%s %s %s %s %s"%(i,nm,res[0],res[1],res[2]))
    else:
        open(NO2,"a",encoding="utf-8").write(i+"\n"); log2("%s %s 未検出 domain=%s(%s)"%(i,nm,base or None,how))
log2(("FINISHED" if n<LIM else "limit")+" shard="+os.environ.get("SHARD","0/1"))
