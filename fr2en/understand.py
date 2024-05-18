import torch
from torch import nn
import torch.nn.functional as F

class LinearRegressionModel(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(LinearRegressionModel, self).__init__()
        self.linear = nn.Linear(input_dim, output_dim)  

    def forward(self, x):
        out = self.linear(x)
        return out
    
# 모델 생성
model = LinearRegressionModel(3, 3)

# 임의의 입력 데이터 생성
torch.manual_seed(0)
train_data = torch.randn(1, 3)
test_data = torch.randn(1, 3)

# 모델 테스트
output_data = model(train_data)
cost = F.mse_loss(output_data, test_data)
print(cost)

print(output_data)
