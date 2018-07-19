import matplotlib.pyplot as plt
import random

y = []
for i in range(1, 101):
    b = random.random()
    if b >= 0.5:
        y.append(1)
    else:
        y.append(0)
plt.hist(y, bins=(max(y)-min(y)+1), histtype = 'bar', edgecolor='r')
plt.xlabel('heads and tails')
plt.ylabel('number of heads and tails')
plt.title('100 Bernoulli trials')
plt.show()