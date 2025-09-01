# Fast, real ML run (Scikit-learn) to prove ML skills on every run
import datetime
from pathlib import Path
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def run():
    Path("data").mkdir(exist_ok=True)
    X, y = load_iris(return_X_y=True)
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, random_state=42)
    clf = LogisticRegression(max_iter=500).fit(Xtr, ytr)
    acc = accuracy_score(yte, clf.predict(Xte))
    now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    lines = [
        "# 📈 ML Metrics (Scikit-learn)",
        f"_Last updated: {now}_",
        "",
        f"- Logistic Regression on Iris: **{acc:.3f}** accuracy",
    ]
    Path("data/metrics.md").write_text("\n".join(lines), encoding="utf-8")

if __name__ == "__main__":
    run()
