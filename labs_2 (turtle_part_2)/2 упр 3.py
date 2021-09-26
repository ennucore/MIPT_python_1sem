inp = open('num (для упр 3).txt')

chisla = []
for line in inp:
    st = line
    st = st.rstrip()
    chisla = chisla + [list(map(int, st.split(", ")))]
print(chisla)
    
import turtle
turtle.shape('turtle')

numbers = []
print('введите индекс')
s = str(input())
for i in s:
    i = int(i)
    numbers = numbers + [i]

d = 0
for i in numbers:
    n = chisla[i]
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
