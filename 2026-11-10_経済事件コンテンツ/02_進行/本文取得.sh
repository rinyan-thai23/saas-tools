#!/bin/bash
# Wikipedia の本文(原文)を、API で取得して標準出力に出す。要約ではなく、そのままの本文。
# 使い方: ./本文取得.sh ja "ステルスマーケティング" > /tmp/out.txt
#         ./本文取得.sh en "Dark pattern"
# 失敗(混雑)したら、数秒おいて最大6回、再試行する。リダイレクトは自動でたどる。
lang="$1"; title="$2"
for i in 1 2 3 4 5 6; do
  curl -s -m 60 -G "https://${lang}.wikipedia.org/w/api.php" \
    --data-urlencode action=query --data-urlencode prop=extracts \
    --data-urlencode explaintext=1 --data-urlencode redirects=1 \
    --data-urlencode "titles=${title}" --data-urlencode format=json -o /tmp/_wp.json
  python3 -I - <<'P' && exit 0
import json,sys
try:
    d=json.load(open('/tmp/_wp.json'))['query']['pages']
    for k,v in d.items():
        if 'missing' in v: sys.exit(2)
        sys.stdout.write(v.get('extract',''))
except Exception:
    sys.exit(1)
P
  sleep 6
done
echo "取得失敗: ${lang} ${title}" >&2; exit 1
