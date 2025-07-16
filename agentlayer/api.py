from fastapi import FastAPI
from agentlayer.flow import run_flow
from agentlayer.rule_checker import check_rules
from agentlayer.notification_sender import send_to_slack, send_to_webhook  # ✅ 추가

app = FastAPI()

@app.get("/")
def root():
    return {"message": "AgentLayer API is running."}

@app.post("/run")
def run_agent():
    result = run_flow()
    violations = check_rules(result)

    # ✅ Slack/Webhook 전송
    message = f"🚀 Agent 실행 완료\nResult: {result}\nViolations: {violations}"
    send_to_slack(message)
    send_to_webhook({
        "status": "executed",
        "result": result,
        "violations": violations
    })

    return {"result": result, "violations": violations}
