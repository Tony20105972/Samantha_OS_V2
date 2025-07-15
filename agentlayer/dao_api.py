# agentlayer/dao_api.py

from fastapi import APIRouter

router = APIRouter()

dao_proposals = []

@router.get("/dao/proposals")
def list_proposals():
    return dao_proposals

@router.post("/dao/proposals")
def create_proposal(proposal: dict):
    dao_proposals.append(proposal)
    return {"status": "proposal added"}
