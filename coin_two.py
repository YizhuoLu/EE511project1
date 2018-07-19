import numpy as np
import matplotlib.pyplot as plt
import random


y = []
for j in range(1, 101):
    x = []
    for i in range(1, 8):
        b = random.random()
        if b >= 0.5:
            x.append(1)
    y.append(len(x))
plt.hist(y, bins=(max(y)-min(y)+1), histtype='bar', edgecolor='r')
plt.xlabel('number of successes in 7 fair Bernoulli trials')
plt.ylabel('number of different numbers of successes in 100 samples')
plt.title('successes-counting')
plt.show()