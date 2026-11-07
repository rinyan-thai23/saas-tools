#!/usr/bin/env python3
"""記事/*.md を静的HTMLにする。使い方: python3 ビルド/build.py [--publish]
- 既定は noindex（公開前）。--publish では運営者情報の未記入・仮リンクをエラーにする。
- /go/<slug>/ は ビルド/go-links.tsv の遷移先へ飛ばす。アフィリURLが決まったらこのTSVだけ書き換える。
"""
import csv, html, re, shutil, sys
from pathlib import Path
import markdown

ROOT = Path(__file__).resolve().parent.parent
SRC, OUT = ROOT / "記事", ROOT.parent / "minpaku"  # GitHub Pages(docs)で /minpaku/ として公開
BASE = next((a.split("=", 1)[1].rstrip("/") for a in sys.argv if a.startswith("--base=")), "/saas-tools/minpaku")  # 独自ドメインなら --base=''  
PUBLISH = "--publish" in sys.argv
errors, warnings = [], []

def parse(path):
    t = path.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n(.*)", t, re.S)
    fm = {}
    for line in m.group(1).splitlines():
        k, _, v = line.partition(":")
        fm[k.strip()] = v.strip()
    body = re.sub(r"<!--.*?-->", "", m.group(2), flags=re.S)
    body = re.sub(r"(^> (?!- |\d+\. )[^\n]*\n)(> (?:- |\d+\. ))", r"\1>\n\2", body, flags=re.M)  # 引用内リストの前に空行
    body = re.sub(r"(^(?!- |\d+\. |\s)[^\n>|#][^\n]*\n)(- )", r"\1\n\2", body, flags=re.M)  # 段落直後のリスト
    return fm, body.strip() + "\n"

go = {}
with open(ROOT / "ビルド" / "go-links.tsv", encoding="utf-8") as f:
    for r in csv.DictReader(f, delimiter="\t"):
        go[r["slug"]] = r

pages = {}
for p in sorted(SRC.glob("*.md")):
    fm, body = parse(p)
    pages[fm.get("slug", p.stem)] = (fm, body)

def url_for(slug, fm):
    if slug == "index": return "/"
    return f"/{slug}/" if fm.get("type") == "固定" else f"/articles/{slug}/"

valid = {url_for(s, fm) for s, (fm, _) in pages.items()} | {f"/go/{s}/" for s in go}

CSS = """:root{--bg:#fff;--fg:#1b1f23;--mut:#5b6670;--line:#d8dee4;--acc:#0b5cad;--soft:#f5f7fa}
@media(prefers-color-scheme:dark){:root{--bg:#14181c;--fg:#e6e9ec;--mut:#9aa5af;--line:#2d353d;--acc:#6db3f2;--soft:#1c2228}}
*{box-sizing:border-box}body{overflow-wrap:anywhere;margin:0;background:var(--bg);color:var(--fg);font:16px/1.85 -apple-system,"Hiragino Sans","Noto Sans JP",sans-serif}
header,main,footer{max-width:820px;margin:0 auto;padding:0 16px}header{padding-top:14px;padding-bottom:10px;border-bottom:1px solid var(--line)}
header a{color:var(--fg);text-decoration:none;font-weight:700}nav a{margin-right:14px;font-weight:400;font-size:14px;color:var(--mut)}
h1{font-size:1.6rem;line-height:1.4;margin:1.4em 0 .6em}h2{font-size:1.25rem;margin:2em 0 .6em;padding-bottom:.3em;border-bottom:1px solid var(--line)}h3{font-size:1.05rem;margin:1.5em 0 .4em}
a{color:var(--acc)}blockquote{margin:1em 0;padding:.6em 1em;background:var(--soft);border-left:4px solid var(--acc)}blockquote p{margin:.4em 0}
.tw{overflow-x:auto;margin:1em 0}table{border-collapse:collapse;font-size:14px;line-height:1.6;min-width:100%}th,td{border:1px solid var(--line);padding:6px 9px;vertical-align:top;text-align:left}th{background:var(--soft);white-space:nowrap}
code{background:var(--soft);padding:1px 4px;border-radius:3px;font-size:.9em}footer{padding-top:20px;padding-bottom:40px;color:var(--mut);font-size:13px;border-top:1px solid var(--line);margin-top:3em}
ul,ol{padding-left:1.4em}li{margin:.2em 0}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin:1em 0}
.card{display:block;padding:14px 16px;border:1px solid var(--line);border-radius:10px;background:var(--soft);text-decoration:none;color:var(--fg);line-height:1.5}
details.src{margin:2em 0;padding:10px 14px;border:1px solid var(--line);border-radius:8px;background:var(--soft)}details.src summary{cursor:pointer;font-weight:700}details.src h2{display:none}details.src li{font-size:14px}
.card b{display:block;margin-bottom:4px}.card span{font-size:13px;color:var(--mut)}.card:hover{border-color:var(--acc)}"""

def render(slug, fm, body):
    html_body = markdown.markdown(body, extensions=["tables", "sane_lists"])
    html_body = html_body.replace("<table>", '<div class="tw"><table>').replace("</table>", "</table></div>")
    def fix(m):
        href = m.group(1)
        if href.startswith("/go/"):
            return f'<a href="{href}" rel="sponsored nofollow noopener" target="_blank"'
        if href.startswith("http"):
            return f'<a href="{href}" rel="nofollow noopener" target="_blank"'
        return m.group(0)
    html_body = re.sub(r'<a href="([^"]+)"', fix, html_body)
    # 出典・情報源は折りたたむ（本文を読みやすくする）
    m = re.search(r"<h2>(出典|情報源と取得日)</h2>", html_body)
    if m:
        html_body = (html_body[:m.start()] + f'<details class="src"><summary>根拠を見る（{m.group(1)}）</summary>' + html_body[m.start():] + "</details>")
    html_body = html_body.replace('href="/', f'href="{BASE}/')
    robots = "" if PUBLISH else '<meta name="robots" content="noindex,nofollow">'
    title = html.escape(fm.get("title", slug))
    desc = html.escape(fm.get("description", ""))
    return f"""<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}">{robots}<style>{CSS}</style></head><body>
<header><a href="{BASE}/">民泊ツール比較</a><nav><a href="{BASE}/compare-table/">総合比較表</a><a href="{BASE}/disclosure/">広告表示と運営方針</a><a href="{BASE}/changelog/">更新履歴</a></nav></header>
<main>{html_body}</main>
<footer>最終確認日 {html.escape(fm.get("updated",""))} ／ 料金・仕様は変わるため、申込前に公式ページで再確認してください。<br><a href="{BASE}/disclosure/">広告表示と運営方針</a></footer></body></html>"""

if OUT.exists(): shutil.rmtree(OUT)
for slug, (fm, body) in pages.items():
    u = url_for(slug, fm)
    # --- チェック ---
    for href in re.findall(r"\]\((/[^)\s]*)\)", body):
        h = href.split("#")[0]
        if h not in valid: errors.append(f"{slug}: リンク切れ {href}")
        if re.match(r"/go/(sirvoy|hostfully)", h): errors.append(f"{slug}: Sirvoy/Hostfullyへの/go/ {h}")
    if re.search(r"/go/", body) and "PR" not in body[:700] and "広告" not in body[:700]:
        errors.append(f"{slug}: /go/ リンクがあるのに冒頭にPR表記がない")
    for w in ["追加調査依頼", "TODO", "事実カード"]:
        if w in body: errors.append(f"{slug}: 公開本文に『{w}』が残っている")
    if "未設定" in body or "未記入" in body: (errors if PUBLISH else warnings).append(f"{slug}: 『未設定/未記入』のプレースホルダーが残っている")
    d = OUT / u.strip("/") if u != "/" else OUT
    d.mkdir(parents=True, exist_ok=True)
    (d / "index.html").write_text(render(slug, fm, body), encoding="utf-8")

for s, r in go.items():
    d = OUT / "go" / s; d.mkdir(parents=True, exist_ok=True)
    dest = html.escape(r["遷移先URL"])
    (d / "index.html").write_text(f'<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="robots" content="noindex,nofollow"><meta http-equiv="refresh" content="0;url={dest}"><title>移動中</title></head><body><p><a href="{dest}" rel="sponsored nofollow">公式サイトへ移動します</a></p></body></html>', encoding="utf-8")
    if PUBLISH and "仮" in r["状態"]: warnings.append(f"/go/{s}/: 遷移先は仮（アフィリURL未設定）")
(OUT / "robots.txt").write_text("User-agent: *\n" + ("Disallow: /go/\n" if PUBLISH else "Disallow: /\n"), encoding="utf-8")

print(f"ページ {len(pages)} 本 + /go/ {len(go)} 本 → {OUT}")
for w in warnings: print("警告:", w)
for e in errors: print("エラー:", e)
sys.exit(1 if errors else 0)
