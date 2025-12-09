import requests
import os
from datetime import datetime, timedelta

WEBHOOK = os.environ.get("DISCORD_WEBHOOK")

# 防災科研の最新地震JSON
URL = "https://www.jquake.net/json/quake.json"

def get_latest_quake_time():
    r = requests.get(URL)
    data = r.json()

    # 最新の地震の時刻を取得
    latest = data[0]["time"]
    # 例: "2025/12/09 01:23:00"
    dt = datetime.strptime(latest, "%Y/%m/%d %H:%M:%S")
    return dt

def main():
    latest = get_latest_quake_time()
    now = datetime.utcnow() + timedelta(hours=9)  # JSTに変換
    diff = now - latest

    if diff >= timedelta(hours=12):
        msg = f"📢 12時間以上地震がありません\n最終地震時刻: {latest}"
        r = requests.post(WEBHOOK, json={"content": msg})
        print("status:", r.status_code)
    else:
        print("まだ12時間経っていません")

if __name__ == "__main__":
    main()
