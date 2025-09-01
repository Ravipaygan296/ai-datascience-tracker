# Use GitHub Search API (no token required but token recommended for higher rate)
import os, datetime, requests
from pathlib import Path
from datetime import timedelta

def run():
    Path("data").mkdir(exist_ok=True)
    now = datetime.datetime.utcnow()
    last_14 = (now - timedelta(days=14)).date().isoformat()

    headers = {"Accept": "application/vnd.github+json", "User-Agent":"ai-ds-tracker/1.0"}
    token = os.getenv("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"

    url = (
        "https://api.github.com/search/repositories"
        f"?q=language:Python+topic:machine-learning+created:>{last_14}"
        "&sort=stars&order=desc&per_page=10"
    )
    r = requests.get(url, timeout=25, headers=headers)
    r.raise_for_status()
    data = r.json().get("items", [])

    out = [
        "# ⭐ Trending AI GitHub Repositories (last 14 days)",
        f"_Last updated: {now.strftime('%Y-%m-%d %H:%M UTC')}_",
        "",
        "| Repo | Stars | Description |",
        "|------|-------|-------------|",
    ]
    for it in data:
        full = it["full_name"]
        stars = it["stargazers_count"]
        link = it["html_url"]
        desc = (it.get("description") or "").replace("|","-")
        out.append(f"| [{full}]({link}) | {stars} | {desc} |")

    Path("data/github_ai.md").write_text("\n".join(out), encoding="utf-8")

if __name__ == "__main__":
    run()
