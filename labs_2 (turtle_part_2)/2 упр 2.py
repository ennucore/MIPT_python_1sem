zero = [0, 0, 0, 60, 30, 60, 30, 0, 0, 0]
one = [0, 30, 30, 60, 30, 0]
two = [0, 60, 30, 60, 30, 30, 0, 0, 30, 0]
three = [0, 60, 30, 60, 0, 30, 30, 30, 0, 0]
four = [0, 60, 0, 30, 30, 30, 30, 60, 30, 0]
five = [30, 60, 0, 60, 0, 30, 30, 30, 0, 0, 0, 0]
six = [30, 60, 0, 30, 0, 0, 30, 0, 30, 30, 0, 30]
seven = [0, 60, 30, 60, 0, 30, 0, 0]
eught = [0, 0, 0, 60, 30, 60, 30, 0, 0, 0, 0, 30, 30, 30]
nine = [30, 30, 0, 30, 0, 60, 30, 60, 30, 30, 0, 0]

d = 0
x = []
number = [zero, one, two, three, four, five, six, seven, eught, nine]

import turtle
turtle.shape('turtle')

print('введите индекс')
s = str(input())
for i in s:
    i = int(i)
    x = x + [i]

for i in x:
    n = number[i]
    for j in range(0, len(n), 2):
        n[j] += d
    turtle.penup()
    turtle.goto(n[0], n[1])
    turtle.pendown()
    for j in range(2, len(n), 2):
        turtle.goto(n[j], n[j + 1])
    for j in range(0, len(n), 2):
        n[j] = n[j] - d
    d += 40
