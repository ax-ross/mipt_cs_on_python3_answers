import turtle


def draw_star(n):
    for i in range(n):
        turtle.forward(150)
        turtle.left(180 - 180 / n)
        # turtle.forward(50)


turtle.left(180)
draw_star(5)
turtle.penup()
turtle.goto(200, 0)
turtle.pendown()
draw_star(11)
