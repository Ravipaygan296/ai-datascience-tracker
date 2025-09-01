# Lightweight PyTorch demo; gracefully skips if torch not installed
from pathlib import Path
import datetime

def run():
    Path("data").mkdir(exist_ok=True)
    now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    try:
        import torch, torch.nn as nn, torch.optim as optim
        X = torch.randn(200, 1)
        y = 4 * X + 1 + 0.1 * torch.randn(200, 1)
        model = nn.Linear(1, 1)
        opt = optim.SGD(model.parameters(), lr=0.1)
        loss_fn = nn.MSELoss()
        for _ in range(50):
            opt.zero_grad()
            loss = loss_fn(model(X), y)
            loss.backward()
            opt.step()
        params = [p.detach().numpy().tolist() for p in model.parameters()]
        msg = f"PyTorch demo trained (Linear Regression) — params lengths: {[len(p) for p in params]}"
    except Exception as e:
        msg = f"PyTorch demo skipped: {type(e).__name__} - {e}"

    p = Path("data/models.md")
    existing = p.read_text(encoding="utf-8") if p.exists() else ""
    out = existing.rstrip() + f"\n\n## PyTorch Demo ({now})\n- {msg}\n"
    p.write_text(out, encoding="utf-8")

if __name__ == "__main__":
    run()
