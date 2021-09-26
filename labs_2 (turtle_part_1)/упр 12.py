import turtle

turtle.shape('turtle')

def dug(r):
    for i in range(0, 180, 1):
        turtle.forward(r)
        turtle.right(1)
    for i in range(0, 180):
        turtle. forward(r/10)
        turtle.right(1)

n=int(input())
r=2
turtle.left(90)
for i in range(0,n):
    dug(r)

