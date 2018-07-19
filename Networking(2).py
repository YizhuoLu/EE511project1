import random

y = []
for i in range(1, 191):
    if random.random() < 0.05:
        y.append(1)
print(len(y))