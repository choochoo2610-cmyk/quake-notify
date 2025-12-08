import requests
from datetime import datetime, timezone, timedelta
import os

WEBHOOK = os.environ.get("DISCORD_WEBHOOK")
JMA_URL = "https://www.jma.go.jp/bosai/quake/data/list.json"

def send(msg):
    requests.post(WEBHOOK, json={"content": msg})

def main():
    data = requests.get(JMA_URL).json()
    latest = datetime.min.replace(tzinfo=timezone.utc)

    for q in data:
        if "time" in q:
            t = datetime.fromisoformat(q["time"])
            if t.tzinfo is None:
                t = t.replace(tzinfo=timezone.utc)
            if t > latest:
                latest = t

    now = datetime.now(timezone.utc)

    if now - latest >= timedelta(hours=24):
        send(f"✅ 24時間以上 地震なし\n最終時刻: {latest}")
