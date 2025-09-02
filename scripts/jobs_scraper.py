import requests
from bs4 import BeautifulSoup
import re
import json
from datetime import datetime

OUTPUT_FILE = "data/jobs.json"
BASE_URL = "https://example.com/jobs"  # replace with your source

def scrape_jobs():
    jobs = []
    print("[INFO] Starting job scrape...")

    try:
        response = requests.get(BASE_URL, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"[ERROR] Failed to fetch jobs: {e}")
        return jobs

    soup = BeautifulSoup(response.text, "html.parser")

    for link in soup.find_all("a", href=True):
        href = link["href"]

        # ✅ FIXED: regex properly placed
        if href and re.search(r"/job/\d+", href):  
            title = link.get_text(strip=True)
            jobs.append({
                "title": title,
                "url": href,
                "scraped_at": datetime.utcnow().isoformat()
            })

    print(f"[INFO] Scraped {len(jobs)} jobs.")
    return jobs


def save_jobs(jobs):
    try:
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            json.dump(jobs, f, indent=2)
        print(f"[INFO] Saved {len(jobs)} jobs to {OUTPUT_FILE}")
    except Exception as e:
        print(f"[ERROR] Failed to save jobs: {e}")


def run():
    jobs = scrape_jobs()
    if jobs:
        save_jobs(jobs)


if __name__ == "__main__":
    run()

