import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def relu(x):
    return max(0, x)

# Input
x = [1.0, 2.0]

# Hidden Layer (2 Neuronen)
W1 = [
    [0.5, -1.0],
    [1.0, 0.5]
]
b1 = [0.0, 0.5]

# Output Layer
W2 = [1.0, -0.5]
b2 = 0.1

# ---- Hidden Layer
h = []
for i in range(2):
    z = W1[i][0]*x[0] + W1[i][1]*x[1] + b1[i]
    h.append(relu(z))

# ---- Output Layer --
z_out = W2[0]*h[0] + W2[1]*h[1] + b2
y = sigmoid(z_out)

print("Output:", y)
