# 📊 Automated DORA Metrics Analytics System

![GitHub Actions](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-003B57?style=for-the-badge&logo=python&logoColor=white)
![Automation-Daily](https://img.shields.io/badge/Automation-Daily%20Updates-brightgreen?style=for-the-badge)
![Repo Size](https://img.shields.io/github/repo-size/Lyynn777/dora-metrics-automation?style=for-the-badge)
![Last Commit](https://img.shields.io/github/last-commit/Lyynn777/dora-metrics-automation?style=for-the-badge)
 
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

