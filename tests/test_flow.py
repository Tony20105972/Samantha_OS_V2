# tests/test_flow.py

from agentlayer.flow import run_flow

def test_flow():
    input_data = {"input": "hello"}
    result = run_flow(input_data)
    assert "step3" in result
