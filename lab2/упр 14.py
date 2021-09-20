import turtle

turtle.shape('turtle')

print('введите нечетное n для количества лучиков звезды')
n=int(input())
turtle.left(270 - 90 / n)

for i in range(0,n):
    turtle.forward(100)
    turtle.left(180 - 180 / n)
