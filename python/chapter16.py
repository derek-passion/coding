from matplotlib.pyplot import hist, show
import random
def roll():
    return random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
b = []
for e in range(10000):
    t = roll() - 3
    a[t] = a[t] + 1
for e in range(3, 19):
    for g in range(a[e-3]):
        b.append(e)
print(a)
hist(b)
show()