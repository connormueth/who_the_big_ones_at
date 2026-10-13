import random

numdarts = 100
numred = 0
numblue = 0
for i in range(numdarts):
    randx = random.random()
    randy = random.random()
    flip1 = random.randint(1, 2)
    flip2 = random.randint(1, 2)
    if flip1 == 1:
        x = randx * -1
    else: x = randx
    if flip2 == 1:
        y = randy * -1
    else: y = randy
    if x**2 + y**2 <= 1:
        numblue += 1
    else:
        numred += 1

print(numblue)
print(numred)

print("Pi estimate:")
print((numblue / numdarts) * 4)
