import random
import json
from datetime import datetime, timedelta
import os

OUTPUT_PATH = "output/deployment_logs.json"

DAYS = 30
AVG_DEPLOYMENTS_PER_DAY = 5
FAILURE_RATE = 0.15
AVG_RECOVERY_TIME_MIN = 30
STD_RECOVERY_TIME_MIN = 15

deployments = []

start_date = datetime.now() - timedelta(days=DAYS)

for day in range(DAYS):
    day_start = start_date + timedelta(days=day)
    num_deploys = max(1, int(random.gauss(AVG_DEPLOYMENTS_PER_DAY, 2)))

    for d in range(num_deploys):
        commit_time = day_start + timedelta(hours=random.uniform(0, 20))
        deploy_time = commit_time + timedelta(minutes=random.uniform(20, 300))
        is_failure = random.random() < FAILURE_RATE

        recovery_time = None
        if is_failure:
            mins = max(5, int(random.gauss(AVG_RECOVERY_TIME_MIN, STD_RECOVERY_TIME_MIN)))
            recovery_time = deploy_time + timedelta(minutes=mins)

        deployments.append({
            "commit_time": commit_time.isoformat(),
            "deploy_time": deploy_time.isoformat(),
            "failed": is_failure,
            "recovery_time": recovery_time.isoformat() if recovery_time else None
        })

os.makedirs("output", exist_ok=True)

with open(OUTPUT_PATH, "w") as f:
    json.dump(deployments, f, indent=4)

print(f"[log_generator] Generated logs → {OUTPUT_PATH}")
