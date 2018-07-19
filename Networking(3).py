import numpy as np
import matplotlib.pyplot as plt
import random

y = []
for i in range(1, 10001):
    x = []
    for j in range(1, 191):
        if random.random()<0.05:
            x.append(1)
    y.append(len(x))
plt.hist(y, bins=(max(y)-min(y)+1), histtype='bar', edgecolor='r')
plt.title('distribution of the random number of edges')
plt.xlabel('number of successfully connected edges')
plt.ylabel('occurrences of different edge numbers in 10000 samples')
plt.show()