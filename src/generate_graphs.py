import json
import matplotlib.pyplot as plt
from datetime import datetime
from collections import defaultdict

LOG_PATH = "output/deployment_logs.json"

with open(LOG_PATH, "r") as f:
    logs = json.load(f)

for e in logs:
    e["deploy_time"] = datetime.fromisoformat(e["deploy_time"])
    e["commit_time"] = datetime.fromisoformat(e["commit_time"])
    e["recovery_time"] = datetime.fromisoformat(e["recovery_time"]) if e["recovery_time"] else None


# 1. Deployment frequency per day
deployments_per_day = defaultdict(int)
for e in logs:
    deployments_per_day[e["deploy_time"].date()] += 1

days = list(deployments_per_day.keys())
counts = list(deployments_per_day.values())

plt.figure(figsize=(10,5))
plt.plot(days, counts, marker='o')
plt.title("Deployment Frequency per Day")
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.savefig("output/df_trend.png")
plt.close()

# 2. Lead Time histogram
lead_times = [(e["deploy_time"] - e["commit_time"]).total_seconds()/3600 for e in logs]

plt.figure(figsize=(8,5))
plt.hist(lead_times, bins=20)
plt.title("Lead Time Distribution (hours)")
plt.grid()
plt.savefig("output/lead_time_hist.png")
plt.close()

# 3. Change Failure Rate Pie
failures = sum(1 for e in logs if e["failed"])

plt.figure(figsize=(6,6))
plt.pie([len(logs)-failures, failures], labels=["Success","Failure"], autopct="%1.1f%%")
plt.title("Change Failure Rate")
plt.savefig("output/cfr_pie.png")
plt.close()

# 4. MTTR histogram
recovery_times = [
    (e["recovery_time"] - e["deploy_time"]).total_seconds()/3600
    for e in logs if e["failed"] and e["recovery_time"]
]

plt.figure(figsize=(8,5))
plt.hist(recovery_times, bins=15)
plt.title("MTTR Distribution (hours)")
plt.grid()
plt.savefig("output/mttr_hist.png")
plt.close()

print("[generate_graphs] Saved graphs to output/")
