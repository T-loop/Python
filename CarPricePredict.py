import torch
import torch.nn as nn

torch.manual_seed(42)
num_samples = 1000

baujahr = torch.randint(1995, 2024, (num_samples, 1)).float()
kilometer = torch.randint(0, 300_000, (num_samples, 1)).float()
ps = torch.randint(60, 400, (num_samples, 1)).float()
verbrauch = torch.rand(num_samples, 1) * 8 + 4
tueren = torch.randint(2, 6, (num_samples, 1)).float()

X = torch.cat([baujahr, kilometer, ps, verbrauch, tueren], dim=1)

price = (
    (baujahr - 1995) * 800
    - kilometer * 0.03
    + ps * 120
    - verbrauch * 500
    + tueren * 1000
    + 10_000
)

price += torch.randn(num_samples, 1) * 2000
y = price

X_mean = X.mean(dim=0)
X_std = X.std(dim=0)
X = (X - X_mean) / X_std

class CarPriceNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(5, 32)
        self.fc2 = nn.Linear(32, 16)
        self.fc3 = nn.Linear(16, 1)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.relu(self.fc2(x))
        x = self.fc3(x)
        return x

model = CarPriceNet()

loss_fn = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

epochs = 500
for epoch in range(epochs):
    optimizer.zero_grad()
    predictions = model(X)
    loss = loss_fn(predictions, y)
    loss.backward()
    optimizer.step()
    if epoch % 50 == 0:
        print(f"Epoch {epoch:03d} | RMSE: {loss.sqrt().item():.2f} €")

test_car = torch.tensor([[2018., 60000., 150., 6.5, 4.]])
test_car = (test_car - X_mean) / X_std
predicted_price = model(test_car)

print(int(predicted_price.item()))
