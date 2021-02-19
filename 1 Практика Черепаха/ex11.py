import turtle


def draw_circle(n):
    for i in range(180):
        turtle.left(2)
        turtle.forward(n)


turtle.shape('turtle')
turtle.left(90)
n = 1
for i in range(10):
    draw_circle(n)
    turtle.left(180)
    draw_circle(n)
    n += 0.2
