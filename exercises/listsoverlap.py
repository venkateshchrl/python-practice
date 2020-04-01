import random
a = random.sample(range(1, 30), 10)
b = random.sample(range(1, 20), 11)
print(a)
print(b)
output = []
for i in a:
    if i in b and i not in output:
        output.append(i)
print(output)