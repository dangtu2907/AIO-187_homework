import torch
import torch.nn as nn


class SoftmaxStable(nn.Module):
    def __init__(self):
        super(SoftmaxStable, self).__init__()

    def forward(self, x):
        c = torch.max(x)
        x_exp = torch.exp(x - c)
        total = x_exp.sum(0, keepdim=True)
        return x_exp / total


data = torch.Tensor([1, 2, 3])
stable_softmax = SoftmaxStable()
output = stable_softmax.forward(data)
print(output)
