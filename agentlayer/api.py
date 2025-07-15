# agentlayer/api.py

from fastapi import FastAPI
from agentlayer.flow import run_flow
from agentlayer.rule_checker import check_rules

app = FastAPI()

@app.get("/")
def root():
    return {"message": "AgentLayer API is running."}

@app.post("/run")
def run_agent():
    result = run_flow()
    violations = check_rules(result)
    return {"result": result, "violations": violations}
