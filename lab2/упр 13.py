import turtle

turtle.shape('turtle')

turtle.speed(10000)
turtle.color("black", "yellow")
turtle.begin_fill()
for i in range(0, 360, 1):
    turtle.forward(2)
    turtle.left(1)
turtle.end_fill()

turtle.penup()
turtle.goto(50, 150)
turtle.pendown()
turtle.color("black", "blue")
turtle.begin_fill()
for i in range(0, 72, 1):
    turtle.forward(1)
    turtle.left(5)
turtle.end_fill()

turtle.penup()
turtle.goto(-50, 150)
turtle.pendown()
turtle.begin_fill()
for i in range(0, 72, 1):
    turtle.forward(1)
    turtle.left(5)
turtle.end_fill()

turtle.penup()
turtle.goto(-55, 120)
turtle.pendown()
turtle.right(90)
turtle.width(5)
turtle.color("red")
for i in range(0, 180, 1):
    turtle.forward(1)
    turtle.left(1)

turtle.penup()
turtle.goto(0, 150)
turtle.pendown()
turtle.left(180)
turtle.color("black")
turtle.forward(30)
