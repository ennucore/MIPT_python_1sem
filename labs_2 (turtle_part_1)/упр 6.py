import turtle

n=int(input())
for i in range(0, n):
    turtle.shape('turtle')
    turtle.forward(50)
    turtle.stamp()
    turtle.left(180)
    turtle.forward(50)
    turtle.left(180)
    turtle.left(360//n)
