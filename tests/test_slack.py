import requests
import datetime

# 1. Slack Webhook URL (Slack에서 생성한 URL로 대체하세요)
WEBHOOK_URL = ''

# 2. 클라우드 비용 예시 데이터
cloud_cost_data = {
    "AWS": 125.67,
    "GCP": 89.50,
    "Azure": 45.20,
}
total_cost = sum(cloud_cost_data.values())
today = datetime.datetime.now().strftime("%Y-%m-%d")

# 3. Block Kit 메시지 구성
blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": f"☁️ {today} 클라우드 비용 리포트",
        }
    },
    {"type": "divider"},
]

# 클라우드별 비용 추가
for provider, cost in cloud_cost_data.items():
    blocks.append({
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": f"*{provider}*: ${cost:.2f}"
        }
    })

# 총 비용 표시
blocks.append({"type": "divider"})
blocks.append({
    "type": "section",
    "text": {
        "type": "mrkdwn",
        "text": f"*총 비용*: `${total_cost:.2f}`"
    }
})

# 4. Slack으로 전송
payload = {
    "blocks": blocks
}

response = requests.post(WEBHOOK_URL, json=payload)

if response.status_code == 200:
    print("✅ 메시지 전송 성공!")
else:
    print(f"❌ 메시지 전송 실패: {response.text}")
