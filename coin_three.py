import numpy as np
import matplotlib.pyplot as plt
import random

y = []
for i in range(1, 10001):
    x = []
    for j in range(1, 101):
        if random.random() >= 0.5:
            x.append(1)
        else:
            x.append(0)
    sum = 0
    each = 0
    for i in range(0, 100):
        if x[i] == 1:
            each += 1
        else:
            if each > sum:
                sum = each
                each = 0
    y.append(sum)
plt.hist(y, bins=(max(y)-min(y)+1), histtype='bar', edgecolor='r')
plt.xlabel('longest run of heads in 100 Bernoulli samples')
plt.ylabel('occurrences of different longest run of heads in 10000 samples')
plt.title('counting longest run of heads')
plt.show()