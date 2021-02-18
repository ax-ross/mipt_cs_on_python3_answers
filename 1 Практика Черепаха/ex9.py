import turtle
import math


def draw_polygon(n, a):
    for i in range(n):
        turtle.forward(a)
        turtle.left(360 / n)


turtle.shape('turtle')
R = 15
for n in range(3, 13):
    turtle.left(180 - (180 - (360 / n)) / 2)
    a = R * 2 * math.sin(math.pi / n)
    draw_polygon(n, a)
    turtle.right(180 - (180 - (360 / n)) / 2)
    turtle.penup()
    turtle.forward(15)
    turtle.pendown()
    R += 15
