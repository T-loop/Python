import torch
import torch.nn as nn

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
model.load_state_dict(torch.load("energy_model.pth"))
model.eval()

def predict_energy(temp, area, people, hour, insulation):
    x = torch.tensor([[temp, area, people, hour, insulation]])
    with torch.no_grad():
        prediction = model(x)
    return prediction.item()

result = predict_energy(
    temp=15,
    area=120,
    people=3,
    hour=18,
    insulation=0.7
)

print(" Vorhergesagter Energieverbrauch:", round(result, 2), "kWh")
