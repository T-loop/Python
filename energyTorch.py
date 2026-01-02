import torch
import torch.nn as nn
import torch.optim as optim

torch.manual_seed(42)

N = 1000

temperature = torch.rand(N, 1) * 35
area = torch.rand(N, 1) * 200
people = torch.randint(1, 6, (N, 1)).float()
hour = torch.rand(N, 1) * 24
insulation = torch.rand(N, 1)

X = torch.cat([temperature, area, people, hour, insulation], dim=1)

y = (
    0.3 * area
    + 5 * people
    - 2 * insulation * area
    + 10 * torch.sin(hour / 24 * 3.14)
    + 0.5 * temperature**2
)

class EnergyNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(5, 64)
        self.fc2 = nn.Linear(64, 64)
        self.fc3 = nn.Linear(64, 32)
        self.fc4 = nn.Linear(32, 1)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.relu(self.fc2(x))
        x = self.relu(self.fc3(x))
        x = self.fc4(x)
        return x

model = EnergyNet()

loss_fn = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

epochs = 2000

for epoch in range(epochs):
    pred = model(X)
    loss = loss_fn(pred, y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    if epoch % 200 == 0:
        print(f"Epoch {epoch:4d} | Loss: {loss.item():.2f}")

torch.save(model.state_dict(), "energy_model.pth")
print("\n Modell gespeichert: energy_model.pth")
