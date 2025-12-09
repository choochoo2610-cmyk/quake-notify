import requests
import os
from datetime import datetime, timedelta

WEBHOOK = os.environ.get("DISCORD_WEBHOOK")
URL = "https://prod-kyoshin-eeapi.nict.go.jp/latest.json"

def get_latest_quake_time():
    r = requests.get(URL)
    data = r.json()
    latest = data["updated_at"]  # 例: "2025-12-09T01:23:45+09:00"
    return datetime.fromisoformat(latest)

def main():
    latest = get_latest_quake_time()
    now = datetime.now(latest.tzinfo)
    diff = now - latest

    if diff >= timedelta(hours=12):
        msg = f"📢 12時間地震がありません\n最終観測: {latest}"
        requests.post(WEBHOOK, json={"content": msg})
    else:
        print("まだ12時間経っていません")

if __name__ == "__main__":
    main()
