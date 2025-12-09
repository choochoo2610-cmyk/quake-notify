import requests
import os

WEBHOOK = os.environ.get("DISCORD_WEBHOOK")

def main():
    res = requests.post(WEBHOOK, json={"content": "✅ テスト通知: Discord Webhook OK"})
    print("status:", res.status_code)

if __name__ == "__main__":
    main()
