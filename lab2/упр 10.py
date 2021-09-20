import turtle

turtle.shape('turtle')

def okr(r):
    for i in range(0, 360, 1):
        turtle.forward(r)
        turtle.left(1)

n=int(input())
r=2
for i in range(0,n):
    okr(2)
    turtle.right(360/n)
