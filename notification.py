
import os
import requests

def send_slack_message(message: str):
    webhook_url = os.getenv("SLACK_WEBHOOK_URL")
    if webhook_url:
        payload = {"text": message}
        try:
            requests.post(webhook_url, json=payload)
        except Exception as e:
            print(f"Slack 전송 실패: {e}")

def send_webhook_message(payload: dict):
    webhook_url = os.getenv("CUSTOM_WEBHOOK_URL")
    if webhook_url:
        try:
            requests.post(webhook_url, json=payload)
        except Exception as e:
            print(f"Webhook 전송 실패: {e}")
