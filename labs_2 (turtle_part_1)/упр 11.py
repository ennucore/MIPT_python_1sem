import turtle

turtle.shape('turtle')

def okr(r):
    for i in range(0, 360, 1):
        turtle.forward(r)
        turtle.left(1)
    for i in range(0, 360, 1):
         turtle.forward(r)
         turtle.right(1)
turtle.left(90)
turtle.speed(1000)
n=int(input())
r=1
for i in range(0,n):
    okr(r)
    r+=1
