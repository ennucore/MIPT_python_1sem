import turtle
import math

turtle.shape('turtle')

print('введите икс-овую составляющую скорости')
V0x = int(input())
print('введиет игрек-овую составляющую скорости')
V0y = int(input())
print('введите ускорение свободного падения')
g = float(input())
print('введите отношение коэффициента сопротивления к массе')
ga = float(input())
dt = 0.05
x = 0
y = 0
i=1
j=1
turtle.goto(x, y)
Vx=V0x
Vy=V0y

while 2==2:
    x = (V0x/ga)*(1 - math.exp(-ga*dt*i))
    Vx = V0x*math.exp(-ga*dt*i)
    y = ((V0y + g/ga)/ga) * (1 - math.exp(-ga*dt*j)) - (g*dt*j)/ga
    Vy = (V0y + g/ga)*math.exp(-ga*dt*j) - g/ga 
    if y <= 0:
        V0y =  -Vy
        j = 0
    turtle.goto(x,y)
    i += 1
    j += 1
