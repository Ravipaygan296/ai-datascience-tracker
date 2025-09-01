# Hugging Face models (official public API)
import datetime, requests
from pathlib import Path

def run():
    Path("data").mkdir(exist_ok=True)
    now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    url = "https://huggingface.co/api/models?sort=likes&limit=10"
    r = requests.get(url, timeout=25, headers={"User-Agent":"ai-ds-tracker/1.0"})
    r.raise_for_status()
    models = r.json()

    out = [
        "# 🧠 Popular Hugging Face Models",
        f"_Last updated: {now}_",
        "",
        "| Model | Likes |",",
        "|-------|-------|",
    ]
    for m in models:
        mid = m.get("modelId", "")
        likes = m.get("likes", 0)
        out.append(f"| {mid} | {likes} |")

    Path("data/models.md").write_text("\n".join(out), encoding="utf-8")

if __name__ == "__main__":
    run()
