# tests/test_rules.py

from agentlayer.rule_checker import check_rules

def test_rules_pass():
    result = {"step3": "final result"}
    violations = check_rules(result)
    assert len(violations) == 0
