from random import randint
import turtle

number_of_turtles = 40
steps_of_time_number = 500

turtle.shape('turtle')
turtle.penup()
turtle.goto(-300, -300)
turtle.pendown()
turtle.goto(-300, 300)
turtle.goto(300, 300)
turtle.goto(300, -300)
turtle.goto(-300, -300)

pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.goto(randint(-300, 300), randint(-300, 300))
    unit.shapesize(0.5, 0.5)
    unit.vx = randint(-5, 5)
    unit.vy = randint(-5, 5)

for i in range(steps_of_time_number):
    for unit in pool:
        x = unit.xcor() + unit.vx
        y = unit.ycor() + unit.vy
        unit.goto(x, y)
        if (unit.xcor() <= -250) or (unit.xcor() >= 250):
            unit.vx = -unit.vx
        if (unit.ycor() <= -250) or (unit.ycor() >= 250):
            unit.vy = -unit.vy
