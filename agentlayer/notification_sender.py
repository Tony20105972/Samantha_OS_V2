# agentlayer/notification_sender.py

import os
import requests
from datetime import datetime

def send_to_slack(message: str):
    slack_url = os.getenv("SLACK_WEBHOOK_URL")
    if slack_url:
        try:
            requests.post(slack_url, json={"text": message})
        except Exception as e:
            print("Slack 전송 실패:", e)

def send_to_webhook(payload: dict):
    webhook_url = os.getenv("CUSTOM_WEBHOOK_URL")
    if webhook_url:
        try:
            requests.post(webhook_url, json=payload)
        except Exception as e:
            print("Webhook 전송 실패:", e)

def save_output_html(result: dict, violations: list):
    timestamp = datetime.utcnow().isoformat()
    html_content = f"""
    <html>
    <head><title>AgentLayer 실행 결과</title></head>
    <body>
        <h1>🎯 Agent 실행 리포트</h1>
        <p><b>🕒 실행 시각:</b> {timestamp}</p>
        <h2>✅ 실행 결과</h2>
        <pre>{result}</pre>
        <h2>⚠️ 위반 항목</h2>
        <pre>{violations if violations else '없음 🙌'}</pre>
    </body>
    </html>
    """

    output_dir = os.getenv("OUTPUT_DIR", "output")
    os.makedirs(output_dir, exist_ok=True)

    with open(os.path.join(output_dir, "output.html"), "w", encoding="utf-8") as f:
        f.write(html_content)
