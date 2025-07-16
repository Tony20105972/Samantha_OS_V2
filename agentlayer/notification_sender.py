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
            print("Slack delivery failed:", e)

def send_to_webhook(payload: dict):
    webhook_url = os.getenv("CUSTOM_WEBHOOK_URL")
    if webhook_url:
        try:
            requests.post(webhook_url, json=payload)
        except Exception as e:
            print("Webhook delivery failed:", e)

def save_output_html(result: dict, violations: list):
    timestamp = datetime.utcnow().isoformat()
    html_content = f"""
    <html>
    <head>
        <title>AgentLayer Execution Report</title>
        <style>
            body {{
                font-family: 'Segoe UI', sans-serif;
                padding: 2em;
                background: #f9f9f9;
            }}
            h1 {{ color: #2c3e50; }}
            .section {{
                background: #ffffff;
                padding: 1.5em;
                border-radius: 10px;
                margin-bottom: 1.5em;
                box-shadow: 0 2px 6px rgba(0,0,0,0.1);
            }}
            pre {{
                background: #f4f4f4;
                padding: 1em;
                border-radius: 6px;
                overflow-x: auto;
            }}
        </style>
    </head>
    <body>
        <h1>🚀 Agent Execution Report</h1>
        <div class="section">
            <strong>🕒 Timestamp:</strong> {timestamp}
        </div>
        <div class="section">
            <h2>✅ Execution Result</h2>
            <pre>{result}</pre>
        </div>
        <div class="section">
            <h2>⚠️ Violations Detected</h2>
            <pre>{violations if violations else 'None – all rules passed! 🎉'}</pre>
        </div>
    </body>
    </html>
    """

    output_dir = os.getenv("OUTPUT_DIR", "output")
    os.makedirs(output_dir, exist_ok=True)

    with open(os.path.join(output_dir, "output.html"), "w", encoding="utf-8") as f:
        f.write(html_content)
