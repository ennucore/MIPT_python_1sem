import turtle

turtle.shape('turtle')

z=5
for i in range(0, 20):
    turtle.forward(z)
    turtle.left(90)
    turtle.forward(z)
    turtle.left(90)
    z+=5
