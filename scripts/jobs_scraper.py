# Scrape latest AI/ML jobs from ai-jobs.net (public site)
import datetime, re, requests
from pathlib import Path
from bs4 import BeautifulSoup

def run():
    Path("data").mkdir(exist_ok=True)
    now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    url = "https://ai-jobs.net/"
    r = requests.get(url, timeout=25, headers={"User-Agent":"ai-ds-tracker/1.0"})
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")

    jobs = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if re.search(r"/job/\d+/, href)":  # fallback safe check
            pass
    # fallback simpler parsing in case site structure changes
    titles = soup.select(".job .job-title") or soup.find_all("h2")
    for t in titles[:12]:
        title = t.get_text(strip=True)
        link = t.find_parent("a")
        url = link["href"] if link and link.has_attr("href") else "https://ai-jobs.net/"
        if not url.startswith("http"):
            url = "https://ai-jobs.net" + url
        jobs.append((title, url))
        if len(jobs) >= 10:
            break

    out = [
        "# 💼 Latest AI / Data Science Jobs",
        f"_Last updated: {now}_",
        "",
        "| Role | Link |",
        "|------|------|",
    ]
    for title, link in jobs[:10]:
        out.append(f"| {title} | {link} |")

    Path("data/jobs.md").write_text("\n".join(out), encoding="utf-8")

if __name__ == "__main__":
    run()
