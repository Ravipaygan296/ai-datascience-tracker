# Lightweight TF demo; gracefully skips if TF not installed
from pathlib import Path
import datetime

def run():
    Path("data").mkdir(exist_ok=True)
    now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    try:
        import tensorflow as tf
        import numpy as np
        X = np.random.rand(200, 1).astype("float32")
        y = 3.0 * X + 2.0 + 0.05 * np.random.randn(200, 1)
        model = tf.keras.Sequential([tf.keras.layers.Dense(1)])
        model.compile(optimizer="adam", loss="mse")
        model.fit(X, y, epochs=3, verbose=0)
        w = model.get_weights()
        msg = f"TensorFlow demo trained (Linear Regression) — weights shapes: {[x.shape for x in w]}"
    except Exception as e:
        msg = f"TensorFlow demo skipped: {type(e).__name__} - {e}"

    content = [
        "# 🧪 TensorFlow Demo",
        f"_Last updated: {now}_",
        "",
        f"- {msg}",
    ]
    Path("data/models.md").write_text("\n".join(content), encoding="utf-8")

if __name__ == "__main__":
    run()
