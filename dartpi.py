import turtle
import math
import random

fred = turtle.Turtle()

wn = turtle.Screen()
wn.setworldcoordinates(-1,-1,1,1)
wn.tracer(100)

fred.up()

numdarts = 25000
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
    fred.goto(x, y)
    distance = fred.distance(0, 0)
    if distance > 1:
        fred.dot(5, "red")
        numred += 1
    else:
        fred.dot(5, "blue")
        numblue += 1

print("Pi estimate:")
print((numblue / numdarts) * 4)

wn.exitonclick()
