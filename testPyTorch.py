# data
import torch
import torchvision
from torchvision import transforms, datasets


'''train = datasets.MNIST("", train=True, download=True,
                        transform = transforms.Compose([transforms.ToTensor()]))

test = datasets.MNIST("", train=False, download=True,
                        transform = transforms.Compose([transforms.ToTensor()]))


trainset = torch.utils.data.DataLoader(train, batch_size=10, shuffle = True)
testset = torch.utils.data.DataLoader(test, batch_size=10, shuffle=True)
'''


#
import torch.nn as nn
import torch.nn.functional as F

# CLIMATE: temperature, precipitation, wind speed, uv radiation, humidity, air quality
# population 1, population density 10, temperature 10, average income (cumulative with deciles) 10, age cumulative by deciles 10,
# rainfall 10, humidity level 1, wind speed/h 1, GDP
inSize = 58

class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(inSize, 16)
        self.fc2 = nn.Linear(16, 16)
        self.fc3 = nn.Linear(16, 10)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)


        return F.log_softmax(x, dim=1)


        #return x

net = Net()
X = torch.rand(1,58)
output = net(X)

print (output)
