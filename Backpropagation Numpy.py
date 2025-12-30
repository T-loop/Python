import numpy as np


# Aktivierung Funktionn
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def sigmoid_derivative(z):
    s = sigmoid(z)
    return s * (1 - s)


X = np.array([[1.0],
              [0.0]])  # 2 Input-Neuronen
y = np.array([[1.0]])  # Zielwert


# Input -> Hidden1
W1 = np.array([[0.1, 0.2],
               [0.3, 0.4]])
b1 = np.array([[0.1],
               [0.1]])

# Hidden1 -> Hidden2
W2 = np.array([[0.5, 0.6],
               [0.7, 0.8]])
b2 = np.array([[0.1],
               [0.1]])

# Hidden2 -> Output
W3 = np.array([[0.9, 1.0]])
b3 = np.array([[0.2]])


eta = 0.1      # Lernrate
epochs = 100   # Anzahl Epochen


for epoch in range(epochs):
    # Forward Pass
    z1 = W1 @ X + b1
    a1 = sigmoid(z1)

    z2 = W2 @ a1 + b2
    a2 = sigmoid(z2)

    z3 = W3 @ a2 + b3
    a3 = sigmoid(z3)


    loss = 0.5 * np.sum((a3 - y)**2)

    # Backpropagation
    delta3 = (a3 - y) * sigmoid_derivative(z3)
    delta2 = (W3.T @ delta3) * sigmoid_derivative(z2)
    delta1 = (W2.T @ delta2) * sigmoid_derivative(z1)

    #  Gradienten
    dW3 = delta3 @ a2.T
    db3 = delta3

    dW2 = delta2 @ a1.T
    db2 = delta2

    dW1 = delta1 @ X.T
    db1 = delta1

    #  Gewichte aktualisieren
    W3 -= eta * dW3
    b3 -= eta * db3

    W2 -= eta * dW2
    b2 -= eta * db2

    W1 -= eta * dW1
    b1 -= eta * db1

#ok
    if (epoch+1) % 10 == 0:
        print(f"Epoche {epoch+1}, Loss: {loss:.4f}, Output: {a3.ravel()[0]:.4f}")

print("\nTrainiertes Output-Neuron:", a3.ravel()[0])
