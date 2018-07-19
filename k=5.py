import numpy as np
import matplotlib.pyplot as plt
import random

y = []
for i in range(1, 301):
    x = []
    for j in range(1, 6):
        if random.random() >= 0.5:
            x.append(1)
    y.append(len(x))
plt.hist(y, bins=(max(y)-min(y)+1), histtype = 'bar', edgecolor='r')
plt.title('Counting Successes when k = 5')
plt.xlabel('number of successes in 5 samples')
plt.ylabel('occurrences of different number of successes in 300 samples')
plt.show()