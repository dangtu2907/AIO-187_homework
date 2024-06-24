import math

class Softmax:
    def __init__(self, values):
        self.values = values
    
    def __call__(self):
        exp_values = [math.exp(value) for value in self.values]
        total = sum(exp_values)
        softmax_values = [exp_value / total for exp_value in exp_values]
        rounded_values = [round(value, 4) for value in softmax_values]
        return rounded_values

values = [int(x) for x in input().split()]
softmax = Softmax(values)
output = softmax()
print(output)
