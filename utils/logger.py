import json
from datetime import datetime
import os

LOG_FILE = "logs.json"

def log_message(message, result):
    log_entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "message": message,
        "risk_level": result["risk_level"],
        "final_score": result["final_score"],
        "fraud_type": result["fraud_type"]
    }

    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)
    else:
        logs = []

    logs.append(log_entry)

    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=4)