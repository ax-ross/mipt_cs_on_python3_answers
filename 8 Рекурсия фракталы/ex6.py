import turtle


def draw_curve_levy(n, l):
    if n == 0:
        turtle.forward(l)
    else:
        turtle.left(45)
        draw_curve_levy(n - 1, l / 2)
        turtle.right(90)
        draw_curve_levy(n - 1, l / 2)
        turtle.left(45)


turtle.speed('fastest')
draw_curve_levy(7, 2000)
