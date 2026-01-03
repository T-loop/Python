import torch
import torch.nn as nn
import torch.optim as optim

torch.manual_seed(0)

N = 500

study_hours = torch.rand(N, 1) * 10
attendance = torch.rand(N, 1) * 100
tests = torch.randint(1, 6, (N, 1)).float()

X = torch.cat([study_hours, attendance, tests], dim=1)

y = (
    (study_hours > 4) &
    (attendance > 60) &
    (tests >= 3)
).float()

class PassNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(3, 16)
        self.fc2 = nn.Linear(16, 16)
        self.fc3 = nn.Linear(16, 1)
        self.relu = nn.ReLU()
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.relu(self.fc2(x))
        x = self.sigmoid(self.fc3(x))
        return x

model = PassNet()

loss_fn = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

epochs = 1000

for epoch in range(epochs):
    y_pred = model(X)
    loss = loss_fn(y_pred, y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if epoch % 100 == 0:
        acc = ((y_pred > 0.5) == y).float().mean()
        print(f"Epoch {epoch:4d} | Loss: {loss.item():.4f} | Acc: {acc:.2f}")

with torch.no_grad():
    sample = torch.tensor([[1.0, 10.0, 1.0]])
    prob = model(sample)
    prediction = (prob > 0.5).int()

print(prob.item())
print("Bestanden" if prediction.item() == 1 else "Nicht bestanden")
