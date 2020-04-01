import random
a = random.sample(range(1, 30), 10)
b = random.sample(range(1, 20), 11)
print(a)
print(b)
print(list({i for i in a if i in b}))