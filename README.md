# AgentLayer Refactored

FastAPI 기반의 구조화된 AgentLayer 백엔드

## 주요 기능

- LangGraph 기반 흐름 실행 (`flow.py`)
- 헌법 규칙 검사 (`rule_checker.py`)
- 로그 저장 (`logger.py`)
- CLI 실행기
- FastAPI API
- 마켓플레이스 & DAO API

## 실행 방법

```bash
uvicorn agentlayer.api:app --reload
