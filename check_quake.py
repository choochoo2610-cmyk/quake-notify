import requests
import os

WEBHOOK = os.environ.get("DISCORD_WEBHOOK")

def main():
    # 外部サイトにアクセスできるかテスト
    r = requests.get("https://example.com")
    print("GET example.com:", r.status_code)

    # Discordにテスト送信
    if WEBHOOK:
        res = requests.post(WEBHOOK, json={"content": "✅ テスト2: 通信OK"})
        print("Webhook status:", res.status_code)

if __name__ == "__main__":
    main()
