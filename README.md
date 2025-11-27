# 📊 Automated DORA Metrics Analytics System  
_A fully automated DevOps analytics pipeline powered by GitHub Actions_

This project automatically generates deployment logs, calculates the four DORA metrics, and produces visual analytics dashboards. All metrics are refreshed daily using GitHub Actions.

---

## Features

- ✔ Realistic deployment log simulation (30 days)
- ✔ Automated calculation of:
  - Deployment Frequency
  - Lead Time for Changes
  - Change Failure Rate
  - Mean Time to Recovery (MTTR)
- ✔ Graphs generated automatically:
  - Deployment trend
  - Lead time histogram
  - CFR pie chart
  - MTTR histogram
- ✔ Daily updates through GitHub Actions
- ✔ Outputs stored in `/output` folder

---

## What Are DORA Metrics?

DORA (DevOps Research & Assessment) metrics measure the performance of software delivery teams:

| Metric | Meaning |
|--------|---------|
| Deployment Frequency | How often code is deployed |
| Lead Time for Changes | Time from commit → deploy |
| Change Failure Rate | Percentage of failed deployments |
| MTTR | Time to recover from failure |

---


## 🛠 How It Works

1. GitHub Actions triggers daily.
2. It generates fresh deployment logs.
3. Calculates the DORA metrics.
4. Builds graphs.
5. Automatically commits updated results.


---
