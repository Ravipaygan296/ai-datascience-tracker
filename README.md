# 🤖 AI & Data Science Tracker (Auto-updating)

This repository is a **ready-to-run template** that auto-fetches AI/DS data (arXiv papers, Kaggle trends, GitHub AI repos, jobs, Hugging Face models) and runs lightweight ML demos (Scikit-Learn).  
It is designed to be **safe, reliable, and contribution-friendly**: the GitHub Action will update the `.md` files automatically so your GitHub contribution graph shows regular activity.

> ⚠️ Heavy frameworks (TensorFlow / PyTorch) are included as optional demos and will be run in a **separate weekly workflow** to avoid frequent heavy installs.

## What is included
- `data/` — auto-generated markdown files (papers, kaggle, github_ai, jobs, models, metrics)
- `scripts/` — Python scripts that fetch/produce the content
- `.github/workflows/update.yml` — lightweight workflow (every 3 hours) that updates the repo
- `.github/workflows/weekly-ml.yml` — optional heavier workflow (weekly) that installs TF / Torch and runs demos
- `requirements.txt` — minimal dependencies for the lightweight workflow

## Quick start (create repository on GitHub)
1. Create a new GitHub repository (example: `ai-datascience-tracker`).
2. Upload this project root (you can upload the zip from this page).
3. In the repo settings → Actions, enable workflows.
4. (Optional) Add GitHub secrets:
   - `KAGGLE_USERNAME` and `KAGGLE_KEY` if you want the Kaggle CLI path to work.
   - `GITHUB_TOKEN` is optional — a token is automatically provided to Actions; using it allows higher API rate limits if you set `GITHUB_TOKEN` as a secret.
5. The workflow `.github/workflows/update.yml` will run (every 3 hours) and refresh files in `/data/`.

## Files worth reading
- `scripts/update.py` — master script that runs every sub-script
- `scripts/fetch_papers.py` — real arXiv API fetch (safe)
- `scripts/github_trends.py` — uses GitHub search API (token optional)
- `scripts/kaggle_trends.py` — uses Kaggle CLI if configured, else scrapes public Kaggle page
- `scripts/sklearn_demo.py` — quick Scikit-Learn run (fast) to demonstrate ML skills
- `scripts/tensorflow_demo.py` & `scripts/pytorch_demo.py` — optional demos (skip if frameworks not installed)

## Notes & tips
- The lightweight workflow installs only the small dependencies (`requests`, `beautifulsoup4`, `lxml`, `scikit-learn`, `pandas`). It is fast and reliable.
- If you want to run TensorFlow/PyTorch regularly in Actions, use the `weekly-ml.yml` workflow (it runs once per week to avoid long installs and timeouts).
- Keep `data/` tracked (we commit the generated `.md` files so your GitHub contributions show).
- Customize the scripts to add more sources or format output for your profile.

If you'd like, I can:
- Create the GitHub repo for you (I cannot perform that action without your auth), or
- Add a short demo `profile-bio.md` and `portfolio.md` that reference these generated files.

Enjoy — unzip and push to GitHub, then watch your contributions grow!