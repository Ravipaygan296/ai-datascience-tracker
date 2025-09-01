# scripts/ml_demo.py
import torch
import tensorflow as tf

print("✅ PyTorch version:", torch.__version__)
print("✅ TensorFlow version:", tf.__version__)

# Simple tensor test
x = torch.rand(3, 3)
print("Random Torch Tensor:\n", x)

# Simple TF test
hello = tf.constant("Hello from TensorFlow")
print(hello.numpy().decode())
