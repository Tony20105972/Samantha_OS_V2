# agentlayer/rule_checker.py

import json
import os

CONSTITUTION_PATH = os.path.join(os.path.dirname(__file__), "constitution.json")

def check_rules(result: dict) -> list:
    with open(CONSTITUTION_PATH, "r") as f:
        rules = json.load(f)

    violations = []
    for rule in rules.get("rules", []):
        if not eval(rule["condition"], {}, result):
            violations.append({
                "rule": rule["name"],
                "description": rule["description"]
            })
    return violations
