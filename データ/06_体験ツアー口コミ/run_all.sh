#!/bin/bash
cd "$(dirname "$0")"
while IFS='|' read -r pid name url; do
  python3 -I ../../取得スクリプト/08_口コミ関連順100件.py "$pid" "$name" "$url" . 100 > "log_${name}_rel.txt" 2>&1
  python3 -I ../../取得スクリプト/08_口コミ関連順100件.py "$pid" "$name" "$url" . 100 most_recent > "log_${name}_rec.txt" 2>&1
  echo "$name done" >> progress.txt
done <<'L'
132175|Xola|https://www.capterra.jp/software/132175/xola-booking-and-marketing-system
178518|Bokun|https://www.capterra.jp/software/178518/bokun
99249|Checkfront|https://www.capterra.jp/software/99249/checkfront
122690|Rezdy|https://www.capterra.jp/software/122690/rezdy
126665|TrekkSoft|https://www.capterra.jp/software/126665/tour-activity-booking-system
117299|Bookeo|https://www.capterra.jp/software/117299/bookeo
148394|Regiondo|https://www.capterra.jp/software/148394/regiondo-pro
74193|Zaui|https://www.capterra.jp/software/74193/zaui-software
L
echo ALL > fin_all
