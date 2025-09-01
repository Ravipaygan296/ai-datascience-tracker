# Runs everything; safe & idempotent
import os, sys
from pathlib import Path

# Ensure scripts dir is importable
THIS_DIR = Path(__file__).parent.resolve()
if str(THIS_DIR) not in sys.path:
    sys.path.insert(0, str(THIS_DIR))

from fetch_papers import run as run_papers
from kaggle_trends import run as run_kaggle
from github_trends import run as run_gh
from jobs_scraper import run as run_jobs
from hf_models import run as run_hf
from sklearn_demo import run as run_sklearn
from tensorflow_demo import run as run_tf
from pytorch_demo import run as run_torch

def main():
    Path("data").mkdir(exist_ok=True)
    try:
        run_papers()
    except Exception as e:
        print("fetch_papers error:", e)
    try:
        run_kaggle()
    except Exception as e:
        print("kaggle_trends error:", e)
    try:
        run_gh()
    except Exception as e:
        print("github_trends error:", e)
    try:
        run_jobs()
    except Exception as e:
        print("jobs_scraper error:", e)
    try:
        run_hf()
    except Exception as e:
        print("hf_models error:", e)
    try:
        run_sklearn()
    except Exception as e:
        print("sklearn_demo error:", e)
    # Optional heavy demos — they gracefully skip if library missing
    try:
        run_tf()
    except Exception as e:
        print("tensorflow_demo error:", e)
    try:
        run_torch()
    except Exception as e:
        print("pytorch_demo error:", e)

if __name__ == "__main__":
    main()
