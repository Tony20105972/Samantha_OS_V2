from fastapi import FastAPI
from agentlayer.flow import run_flow
from agentlayer.rule_checker import check_rules
from agentlayer.notification_sender import send_to_slack, send_to_webhook, save_output_html

app = FastAPI()

@app.get("/")
def root():
    return {"message": "AgentLayer API is running."}

@app.post("/run")
def run_agent():
    result = run_flow()
    violations = check_rules(result)

    # 💬 English Slack message with styling
    message = (
        ":robot_face: *Agent Execution Summary*\n\n"
        f"*Result:* ```{result}```\n"
        f"*Violations:* {'❌ ' + str(violations) if violations else '✅ None – all rules passed!'}"
    )

    send_to_slack(message)
    send_to_webhook({
        "status": "executed",
        "result": result,
        "violations": violations,
    })

    save_output_html(result, violations)

    return {"result": result, "violations": violations}
