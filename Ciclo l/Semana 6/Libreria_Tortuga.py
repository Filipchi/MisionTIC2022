import os
os.system("cls")

import turtle
from turtle import *

# color("red", "yellow")
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill
# os.system("pause")
# done

"""
turtle.forward(100) # Avanza
turtle.left(90)     # Angulo
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
os.system("pause")
done
"""
# Aplicando ciclo for

# for x in range(4):
#     turtle.forward(100)
#     turtle.left(90)
# turtle.done() # sustituye system pause
"""
grados = 0
turtle.speed(60)
turtle.color("cyan")
turtle.shape("turtle")
for x in range(1, 40):
    for x in range(4):
        turtle.forward(150)
        turtle.left(90)
    turtle.left(grados + 10)
turtle.done()
"""

colores = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
t = turtle
t.bgcolor('black')
t.shape("turtle")
t.speed(40000)

for x in range(360):
    t.pencolor(colores[x % 6])
    t.width(x/100+1)
    t.forward(x)
    t.left(59)
t.exitonclick()
