import turtle

turtle.shape('turtle')

z=10
for i in range (0, 10):
    turtle.forward(z)
    turtle.left(90)
    turtle.forward(z)
    turtle.left(90)
    turtle.forward(z)
    turtle.left(90)
    turtle.forward(z)
    turtle.penup()
    turtle.forward(5)
    turtle.right(90)
    turtle.forward(5)
    turtle.right(180)
    turtle.pendown()
    z+=10
