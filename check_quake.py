import requests
import os
from datetime import datetime, timedelta
import xml.etree.ElementTree as ET

WEBHOOK = os.environ.get("DISCORD_WEBHOOK")
FEED = "http://www.seis.bosai.go.jp/eq/latest_event.xml"

def get_latest_quake_time():
    r = requests.get(FEED)
    root = ET.fromstring(r.text)

    # 最新の地震の時刻
    ns = {"dc": "http://purl.org/dc/elements/1.1/"}
    time_str = root.find(".//dc:date", ns).text
    return datetime.fromisoformat(time_str.replace("Z", "+00:00"))

def main():
    latest = get_latest_quake_time()
    now = datetime.utcnow().replace(tzinfo=latest.tzinfo)

    diff = now - latest

    if diff >= timedelta(hours=24):
        msg = f"📢 24時間以上地震がありません\n最終地震: {latest}"
        requests.post(WEBHOOK, json={"content": msg})
    else:
        print("まだ24時間経っていません")

if __name__ == "__main__":
    main()
