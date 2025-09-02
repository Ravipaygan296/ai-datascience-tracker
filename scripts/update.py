# update.py
# Runs everything; safe & idempotent with structured logging

import os, sys, traceback
from pathlib import Path
from datetime import datetime

# Ensure scripts dir is importable
THIS_DIR = Path(__file__).parent.resolve()
if str(THIS_DIR) not in sys.path:
    sys.path.insert(0, str(THIS_DIR))

from fetch_papers import run as run_papers
from kaggle_trends import run as run_kaggle
from github_trends import run as run_gh
from jobs_scraper import run as run_jobs
from sklearn_demo import run as run_sklearn
from tensorflow_demo import run as run_tf
from pytorch_demo import run as run_torch

TASKS = {
    "fetch_papers": run_papers,
    "kaggle_trends": run_kaggle,
    "github_trends": run_gh,
    "jobs_scraper": run_jobs,
    "sklearn_demo": run_sklearn,
    "tensorflow_demo": run_tf,
    "pytorch_demo": run_torch,
}

def main():
    Path("data").mkdir(exist_ok=True)

    print(f"\n=== Update run started: {datetime.utcnow().isoformat()} UTC ===\n")

    for name, func in TASKS.items():
        print(f"▶ Running {name} ...")
        try:
            func()
            print(f"✔ {name} completed.\n")
        except Exception as e:
            print(f"✘ {name} failed: {e}")
            traceback.print_exc()
            print()

    print(f"=== Update run finished: {datetime.utcnow().isoformat()} UTC ===\n")

if __name__ == "__main__":
    main()

