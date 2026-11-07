# 使い方: python3 -I 04_PartnerStack照合.py 詳細取得フォルダ
# market.partnerstack.com のトップ1ページに埋め込まれた全プログラム一覧を取得し、
# 製品詳細.tsv の製品名と照合して「アフィリエイト」系の列を追加する（列があれば作り直す）。
import sys,os,re,json,time,unicodedata,urllib.request
D=sys.argv[1]; UA="Mozilla/5.0 (compatible; personal-research-script; low-rate)"
html=urllib.request.urlopen(urllib.request.Request("https://market.partnerstack.com/",headers={"User-Agent":UA}),timeout=60).read().decode("utf-8","ignore")
i=html.find("window.__INITIAL_STATE__ = ")+len("window.__INITIAL_STATE__ = ")
st,_=json.JSONDecoder().raw_decode(html[i:]); cs=st["company"]["companies"]
act=[c for c in cs.values() if c.get("listingType")=="active"]
clean=lambda s:re.sub(r"\s+"," ",str(s or "")).replace("\t"," ").strip()
today=time.strftime("%Y-%m-%d")
with open(os.path.join(D,"PartnerStackプログラム一覧.tsv"),"w",encoding="utf-8") as f:
    f.write("slug\tプログラム名\tサイト\t報酬の表記\t申込ページ\t取得日\n")
    for c in sorted(act,key=lambda c:c["slug"]):
        f.write("\t".join(map(clean,[c["slug"],c["name"],c.get("website"),c.get("offer"),"https://market.partnerstack.com/page/"+c["slug"],today]))+"\n")
def norm(s):
    s=unicodedata.normalize("NFKC",s).lower(); s=re.sub(r"\(.*?\)|\[.*?\]","",s)
    s=re.sub(r"\b(inc|llc|ltd|corp|co|software|by .*|the|app|hq|crm|pro)\b\.?","",s)
    return re.sub(r"[^a-z0-9ぁ-んァ-ヶ一-龥]","",s)
byn={}
for c in act: byn.setdefault(norm(c["name"]),c)
byslug={c["slug"]:c for c in act}
# 目視で確認した手動対応（製品ID: (slug, 区分)）。同社の別ブランド等は区分に書く
MANUAL={"128955":("miroaffiliate","同社"),"1024614":("mondaycom","同社（monday.com）"),
 "46497":("quickbooks","同社（QuickBooks）"),"141374":("quickbooks","同社（QuickBooks）"),"148488":("quickbooks","同社（QuickBooks）"),"189398":("quickbooks","同社（QuickBooks）"),
 "141702":("breezyhr","製品名の表記違い"),"142080":("foxit","同社（Foxit）"),"143513":("learnworlds","製品名一致"),
 "58388":("bitdefender","同社（Bitdefender）"),"124041":("capsule","製品名の表記違い"),
 "143068":("dropbox","要確認"),"187086":("payoneer557","要確認")}  # 要確認：掲載は別製品（DocSend／Workforce Management）の可能性
NEW=["アフィリエイト","アフィリ種別","申込URL","判定の根拠","確認日","アフィリ備考"]
p=os.path.join(D,"製品詳細.tsv"); L=[l.split("\t") for l in open(p,encoding="utf-8").read().split("\n") if l]
h=L[0]; 
if "アフィリエイト" in h: k=h.index("アフィリエイト"); L=[r[:k] for r in L]; h=L[0]
n_hit=0
for r in L[1:]:
    c=None; why=""
    if r[0] in MANUAL: c=byslug.get(MANUAL[r[0]][0]); why=MANUAL[r[0]][1]
    elif norm(r[1]) in byn: c=byn[norm(r[1])]; why="製品名一致"
    if c:
        n_hit+=1; val="要確認" if why=="要確認" else "あり"
        r+= [val,"PartnerStack","https://market.partnerstack.com/page/"+c["slug"],
             "PartnerStack掲載一覧と照合（%s）"%why,today,clean(c.get("offer"))+("／掲載名: "+clean(c["name"]) if why!="製品名一致" else "")]
    else: r+=["未調査","","","","",""]
L[0]=h+NEW
open(p,"w",encoding="utf-8").write("\n".join("\t".join(r) for r in L)+"\n")
print("PartnerStack掲載",len(act),"件 / 照合",n_hit,"件 / 全",len(L)-1,"件")
