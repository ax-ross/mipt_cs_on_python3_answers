import turtle


def draw_circle(n):
    for i in range(180):
        turtle.left(2)
        turtle.forward(n)


turtle.shape('turtle')

for i in range(3):
    draw_circle(1)
    turtle.left(180)
    draw_circle(1)
    turtle.left(60)
