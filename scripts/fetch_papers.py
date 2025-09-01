# Fetch latest AI/ML papers from arXiv (real API)
import datetime, urllib.parse, requests
import xml.etree.ElementTree as ET
from pathlib import Path

ARXIV_SEARCH = "cat:cs.AI OR cat:cs.LG"
MAX_RESULTS = 10

def _parse_atom(xml_text):
    ns = {"a": "http://www.w3.org/2005/Atom"}
    root = ET.fromstring(xml_text)
    entries = []
    for e in root.findall("a:entry", ns):
        title = (e.findtext("a:title", default="", namespaces=ns) or "").strip().replace("\n"," ")
        link = ""
        for ln in e.findall("a:link", ns):
            if ln.get("type") == "text/html":
                link = ln.get("href")
        updated = (e.findtext("a:updated", default="", namespaces=ns) or "")[:10]
        entries.append((updated, title, link))
    return entries

def run():
    Path("data").mkdir(exist_ok=True)
    now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    q = urllib.parse.quote(ARXIV_SEARCH)
    url = (
        f"https://export.arxiv.org/api/query?"
        f"search_query={q}&sortBy=submittedDate&sortOrder=descending&max_results={MAX_RESULTS}"
    )
    r = requests.get(url, timeout=25, headers={"User-Agent":"ai-ds-tracker/1.0"})
    r.raise_for_status()
    rows = _parse_atom(r.text)

    out = [
        "# 📑 Latest AI/ML Papers",
        f"_Last updated: {now}_",
        "",
        "| Date | Title | Link |",
        "|------|-------|------|",
    ]
    for d, title, link in rows:
        out.append(f"| {d} | {title} | {link} |")
    Path("data/papers.md").write_text("\n".join(out), encoding="utf-8")

if __name__ == "__main__":
    run()
