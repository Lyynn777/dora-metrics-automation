import json
import numpy as np
from datetime import datetime
import os

INPUT_PATH = "output/deployment_logs.json"
OUTPUT_PATH = "output/metrics.json"

with open(INPUT_PATH, "r") as f:
    logs = json.load(f)

for entry in logs:
    entry["commit_time"] = datetime.fromisoformat(entry["commit_time"])
    entry["deploy_time"] = datetime.fromisoformat(entry["deploy_time"])
    entry["recovery_time"] = datetime.fromisoformat(entry["recovery_time"]) if entry["recovery_time"] else None

lead_times = [(e["deploy_time"] - e["commit_time"]).total_seconds() / 3600 for e in logs]

failures = sum(1 for e in logs if e["failed"])
failure_rate = failures / len(logs)

recovery_times = [
    (e["recovery_time"] - e["deploy_time"]).total_seconds() / 3600
    for e in logs if e["failed"] and e["recovery_time"]
]

metrics = {
    "deployment_frequency_per_day": round(len(logs) / 30, 2),
    "average_lead_time_hours": round(float(np.mean(lead_times)), 2),
    "change_failure_rate_percent": round(failure_rate * 100, 2),
    "mttr_hours": round(float(np.mean(recovery_times)), 2)
}

with open(OUTPUT_PATH, "w") as f:
    json.dump(metrics, f, indent=4)

print(f"[metrics_calculator] Saved metrics → {OUTPUT_PATH}")
