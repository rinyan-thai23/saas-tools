# 使い方: python3 -I 06_自社サイト確認.py 詳細取得フォルダ [件数上限]
# 日本語対応で「未調査」の製品について、(1) Bing の最上位結果から公式ドメインを推定し、
# (2) トップページのリンクと /affiliate など定番パスを確認して、アフィリエイトの有無と種別を判定する。
# 見つかったものは アフィリ調査結果.tsv に追記。見つからなかったものは 自社確認済_なし.txt に製品IDを残す（次の段階の検索用）。
# robots.txt で禁止されているパスは取得しない。
import sys,os,re,time,random,html,base64,unicodedata,urllib.request,urllib.error,urllib.parse,urllib.robotparser
D=sys.argv[1]; LIM=int(sys.argv[2]) if len(sys.argv)>2 else 10**9
UA="Mozilla/5.0 (compatible; personal-research-script; low-rate)"
R=os.path.join(D,"アフィリ調査結果.tsv"); NO=os.path.join(D,"自社確認済_なし.txt"); DOM=os.path.join(D,"アフィリ_公式ドメイン.tsv"); LOG=os.path.join(D,"自社サイト確認.log")
log=lambda s:open(LOG,"a").write(time.strftime("%H:%M:%S ")+s+"\n")
NET={"partnerstack.com":"PartnerStack","firstpromoter.com":"FirstPromoter","rewardful.com":"Rewardful","tapfiliate.com":"Tapfiliate","refersion.com":"Refersion",
 "impact.com":"Impact","impactradius.com":"Impact","sjv.io":"Impact","awin.com":"Awin","awin1.com":"Awin","shareasale.com":"ShareASale","cj.com":"CJ Affiliate",
 "partnerize.com":"Partnerize","goaffpro.com":"GoAffPro","leaddyno.com":"LeadDyno","growsurf.com":"GrowSurf","linksynergy.com":"Rakuten","rakutenadvertising.com":"Rakuten",
 "tolt.io":"Tolt","getrewardful.com":"Rewardful","postaffiliatepro.com":"Post Affiliate Pro","affiliatly.com":"Affiliatly","referralcandy.com":"ReferralCandy",
 "referralhero.com":"ReferralHero","promotekit.com":"PromoteKit","affonso.io":"Affonso","dub.co":"Dub","lemonsqueezy.com":"Lemon Squeezy"}
SKIP=("wikipedia.org","linkedin.com","youtube.com","capterra.","g2.com","facebook.com","twitter.com","x.com","reddit.com","play.google.com","apps.apple.com","crunchbase.com","trustpilot.com",
 "softwareadvice.com","getapp.com","gartner.com","instagram.com","pinterest.com","medium.com","quora.com","microsoft.com/en-us/microsoft-365","bing.com","amazon.com","github.com","producthunt.com")
def norm(s): return re.sub(r"[^a-z0-9]","",unicodedata.normalize("NFKC",s).lower())
def host_of(u): return urllib.parse.urlparse(u).netloc.lower().removeprefix("www.")
def is_net(h):
    for d,l in NET.items():
        if h==d or h.endswith("."+d): return l
def fetch(u,maxb=1500000):
    time.sleep(random.uniform(0.3,0.8))
    try:
        r=urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":UA,"Accept-Language":"en-US,en;q=0.9"}),timeout=15)
        ct=r.headers.get("Content-Type","")
        if "html" not in ct and "text" not in ct: return r.geturl(),""
        return r.geturl(),r.read(maxb).decode("utf-8","ignore")
    except Exception as e: return None,""
_rp={}
def allowed(u):
    h=urllib.parse.urlparse(u).netloc
    if h not in _rp:
        rp=urllib.robotparser.RobotFileParser()
        try:
            time.sleep(random.uniform(0.2,0.5)); t=urllib.request.urlopen(urllib.request.Request("https://%s/robots.txt"%h,headers={"User-Agent":UA}),timeout=10).read().decode("utf-8","ignore")
            rp.parse(t.splitlines())
        except Exception: rp.parse([])
        _rp[h]=rp
    return _rp[h].can_fetch("*",u)
def reg(h):
    p=h.split(".")
    if len(p)>=3 and ".".join(p[-2:]) in("co.uk","com.au","co.jp","com.br","co.nz","co.in","com.sg","co.za"): return ".".join(p[-3:])
    return ".".join(p[-2:])
def bing_domain(name,_retry=0):
    q=urllib.parse.quote_plus(name+" official site")
    time.sleep(random.uniform(6,12))
    try: t=urllib.request.urlopen(urllib.request.Request("https://www.bing.com/search?q=%s&setlang=en&cc=US&mkt=en-US"%q,headers={"User-Agent":UA,"Accept-Language":"en-US,en;q=0.9"}),timeout=40).read().decode("utf-8","ignore")
    except urllib.error.HTTPError as e:
        if e.code in(403,429): raise SystemExit("bing blocked %s"%e.code)
        return None
    except Exception: return None
    if "b_algo" not in t and ("captcha" in t.lower() or "unusual traffic" in t.lower()):
        log("bing captcha: 10分待って再試行"); time.sleep(600)
        if _retry<3: return bing_domain(name,_retry+1)
        raise SystemExit("bing captcha")
    n=norm(name); first=norm(re.split(r"[\s\-–:/]+",name.strip())[0])
    for x in re.findall(r'<li class="b_algo"[^>]*>(.*?)</li>',t,re.S):
        m=re.search(r'<h2[^>]*><a[^>]*href="([^"]+)"',x,re.S)
        if not m: continue
        u=html.unescape(m.group(1)); q2=urllib.parse.parse_qs(urllib.parse.urlparse(u).query).get("u",[""])[0]
        if q2.startswith("a1"):
            try: b=q2[2:]; u=base64.urlsafe_b64decode(b+"="*(-len(b)%4)).decode()
            except Exception: pass
        h=host_of(u.strip('"'))
        if not h or any(h==s.rstrip(".") or h.endswith("."+s.rstrip(".")) or (s.endswith(".") and h.split(".")[0]==s.rstrip(".")) or (s.endswith(".") and s.rstrip(".") in h.split(".")) for s in SKIP): continue
        lab=norm(h.split(".")[-2] if h.count(".")>=1 else h)
        if lab and (lab==n or lab==first or (len(lab)>=4 and lab in n) or (len(n)>=4 and n in lab and len(lab)-len(n)<=4)):
            return "https://"+reg(h)
        return None   # 最上位の非除外結果が製品名と合わなければ不明とする
    return None
KW=re.compile(r"affiliate|referral|refer-a|refer-friend|/refer|ambassador|partner",re.I)
def evaluate(url,body):
    low=body.lower(); path=urllib.parse.urlparse(url).path.lower()
    nets=set(l for d,l in NET.items() if re.search(r"[\"'/.]"+re.escape(d)+r"[\"'/?]",low))
    aff=len(re.findall(r"affiliate",low)); ref=len(re.findall(r"referral|refer a friend|refer friends",low)); com=("commission" in low) or ("earn" in low and "%" in low)
    if ("affiliate" in path or aff>=3) and (com or "affiliate" in path): return "あり",nets
    if ("referral" in path or "refer" in path or ref>=3) and com: return "要確認",nets
    return None,nets
def check_site(base):
    home_url,home=fetch(base+"/")
    if not home_url: return None
    hb=home_url.rstrip("/"); cands=[]
    for m in re.finditer(r'<a[^>]+href="([^"#]+)"[^>]*>(.*?)</a>',home,re.S|re.I):
        href=urllib.parse.urljoin(home_url,html.unescape(m.group(1))); txt=re.sub(r"<[^>]+>","",m.group(2)).lower()
        if re.search(r"affiliate|referral|ambassador",href+" "+txt,re.I): cands.append((0,href))
        elif re.search(r"\bpartners?\b|partner program",href+" "+txt,re.I): cands.append((1,href))
    seen=[]; out=[]
    for _,h in sorted(cands,key=lambda x:x[0]):
        if h not in seen and h.startswith("http"): seen.append(h)
    for g in ("/affiliate","/affiliates","/affiliate-program","/partners/affiliate"):
        u=urllib.parse.urljoin(home_url,g)
        if u not in seen: seen.append(u)
    best=None; tried=0
    for u in seen:
        if tried>=5: break
        lab=is_net(host_of(u))
        if lab and re.search(r"affiliate|referral|partner",u,re.I): return ("あり",lab+"（第三者）",u,"公式サイトの affiliate リンク先が第三者ネットワーク")
        if not allowed(u): continue
        tried+=1; fu,body=fetch(u)
        if not fu or not body: continue
        v,nets=evaluate(fu,body)
        if v:
            kind=(("／".join(sorted(nets))+"（第三者）") if nets else "自社")
            cand=(v,kind,fu,"公式サイトの affiliate／referral ページ（自動判定）")
            if v=="あり": return cand
            best=best or cand
    return best
done=set(); 
for p in (R,NO):
    if os.path.exists(p): done|={l.split("\t")[0] for l in open(p,encoding="utf-8").read().split("\n")[1:] if l and p==R}|({l.strip() for l in open(p,encoding="utf-8")} if p==NO else set())
L=[l.split("\t") for l in open(os.path.join(D,"製品詳細.tsv"),encoding="utf-8").read().split("\n") if l]; k=L[0].index("アフィリエイト")
T=[r for r in L[1:] if r[6]=="あり" and r[k]=="未調査" and r[0] not in done]
if not os.path.exists(DOM): open(DOM,"w",encoding="utf-8").write("製品ID\t製品名\t公式ドメイン（推定）\n")
today=time.strftime("%Y-%m-%d"); n=0
for r in T:
    if n>=LIM: break
    n+=1
    base=bing_domain(r[1]); open(DOM,"a",encoding="utf-8").write("\t".join([r[0],r[1],base or ""])+"\n")
    res=check_site(base) if base else None
    if res: open(R,"a",encoding="utf-8").write("\t".join([r[0],r[1],res[0],res[1],res[2],res[3],today,"ドメイン:"+base])+"\n"); log("%s %s %s %s %s"%(r[0],r[1],res[0],res[1],res[2]))
    else: open(NO,"a",encoding="utf-8").write(r[0]+"\n"); log("%s %s 未検出 domain=%s"%(r[0],r[1],base))
log("FINISHED" if n<LIM else "limit")
