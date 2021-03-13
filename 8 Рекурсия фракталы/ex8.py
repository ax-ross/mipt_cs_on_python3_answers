import turtle


def draw_cantor_set(n, l, x=0, y=0):
    if n == 0:
        turtle.forward(l)
    else:
        draw_cantor_set(n - 1, l, x=x, y=y)
        turtle.penup()
        turtle.goto(x, y - 10)
        turtle.pendown()
        draw_cantor_set(n - 1, l / 3, x=x, y=y - 10)
        turtle.penup()
        turtle.goto(x + 2 * l / 3, y - 10)
        turtle.pendown()
        draw_cantor_set(n - 1, l / 3, x=x + 2 * l / 3, y=y - 10)


turtle.speed('fastest')
draw_cantor_set(5, 300)