# agentlayer/logger.py

import json
import os

LOG_FILE = os.path.join(os.path.dirname(__file__), "log.json")

def log_execution(data: dict):
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(data) + "\n")
