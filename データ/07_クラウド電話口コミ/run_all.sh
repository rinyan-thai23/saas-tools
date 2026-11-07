#!/bin/bash
cd "$(dirname "$0")"
while IFS='|' read -r pid name url; do
  python3 -I ../../取得スクリプト/08_口コミ関連順100件.py "$pid" "$name" "$url" . 100 > "log_${name}_rel.txt" 2>&1
  python3 -I ../../取得スクリプト/08_口コミ関連順100件.py "$pid" "$name" "$url" . 100 most_recent > "log_${name}_rec.txt" 2>&1
  echo "$name done" >> progress.txt
done < targets.txt
echo ALL > fin_all
