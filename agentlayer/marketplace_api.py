# agentlayer/marketplace_api.py

from fastapi import APIRouter

router = APIRouter()

marketplace = []

@router.get("/marketplace")
def get_all_agents():
    return marketplace

@router.post("/marketplace")
def add_agent(agent: dict):
    marketplace.append(agent)
    return {"status": "agent added"}
