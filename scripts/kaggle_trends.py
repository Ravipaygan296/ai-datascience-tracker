# Try Kaggle API if credentials exist; else scrape public Kaggle Datasets page
import os, datetime, subprocess, shlex, re, requests
from pathlib import Path
from bs4 import BeautifulSoup

def _via_kaggle_cli():
    try:
        if not (os.getenv("KAGGLE_USERNAME") and os.getenv("KAGGLE_KEY")):
            return None
        cmd = "kaggle datasets list --sort-by hotness -p 10"
        out = subprocess.check_output(shlex.split(cmd), timeout=40).decode("utf-8", "ignore")
        lines = [l.strip() for l in out.splitlines() if "/" in l and not l.startswith("ref")]
        items = []
        for l in lines[:10]:
            ds = l.split()[0]
            items.append((ds, f"https://www.kaggle.com/datasets/{ds}"))
        return items or None
    except Exception:
        return None

def _via_scrape():
    url = "https://www.kaggle.com/datasets?sort=hotness"
    r = requests.get(url, timeout=25, headers={"User-Agent":"ai-ds-tracker/1.0"})
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")
    items = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if re.match(r"^/datasets/[^/]+/[^/]+$", href):
            name = href.strip("/").split("/", 2)[-1]
            items.append((name, "https://www.kaggle.com" + href))
    seen, uniq = set(), []
    for name, link in items:
        if link not in seen:
            uniq.append((name, link))
            seen.add(link)
        if len(uniq) >= 10:
            break
    return uniq

def run():
    Path("data").mkdir(exist_ok=True)
    now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    items = _via_kaggle_cli() or _via_scrape()

    out = [
        "# 🏆 Trending Kaggle Datasets",
        f"_Last updated: {now}_",
        "",
        "| Dataset | Link |",
        "|---------|------|",
    ]
    for name, link in items:
        out.append(f"| {name} | {link} |")
    Path("data/kaggle.md").write_text("\n".join(out), encoding="utf-8")

if __name__ == "__main__":
    run()
