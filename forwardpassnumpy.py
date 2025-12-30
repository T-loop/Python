import numpy as np

class SimpleNN:
    def __init__(self):
        # random init
        self.W1 = np.random.randn(3, 2)
        self.b1 = np.random.randn(3)
        self.W2 = np.random.randn(1, 3)
        self.b2 = np.random.randn(1)

    def relu(self, x):
        return np.maximum(0, x)

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def forward(self, x):
        z1 = self.W1 @ x + self.b1
        h = self.relu(z1)
        z2 = self.W2 @ h + self.b2
        y = self.sigmoid(z2)
        return y

# Nutz
nn = SimpleNN()
x = np.array([1.0, 2.0])
output = nn.forward(x)
print("Output:", output)
