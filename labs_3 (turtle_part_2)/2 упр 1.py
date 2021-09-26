import turtle
from random import *

turtle.shape('turtle')

for i in range(0, 100):
    turtle.forward(randint(1, 100))
    turtle.left(randint(1, 360))
