import requests
import os
from datetime import datetime, timedelta
import xml.etree.ElementTree as ET

WEBHOOK = os.environ.get("DISCORD_WEBHOOK")
FEED = "https://www.data.jma.go.jp/developer/xml/feed/eqvol.xml"

def get_latest_quake_time():
    r = requests.get(FEED)
    root = ET.fromstring(r.text)
    time_str = root.find(".//updated").text
    return datetime.fromisoformat(time_str.replace("Z", "+00:00"))

def main():
    latest = get_latest_quake_time()
    now = datetime.utcnow().replace(tzinfo=latest.tzinfo)
    diff = now - latest

    if diff >= timedelta(hours=12):
        msg = f"📢 12時間以上地震がありません\n最終更新: {latest}"
        requests.post(WEBHOOK, json={"content": msg})
    else:
        print("まだ12時間経っていません")

if __name__ == "__main__":
    main()
