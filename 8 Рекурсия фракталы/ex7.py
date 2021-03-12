import turtle


def draw_dragon_curve(n, l, flag=True):
    if n == 0:
        turtle.forward(l)
    else:
        turtle.right(45)
        draw_dragon_curve(n - 1, l / 2 ** 0.5, flag=True)
        if flag:
            turtle.left(90)
        else:
            turtle.right(90)
        draw_dragon_curve(n - 1, l / 2 ** 0.5, flag=False)
        turtle.left(45)


turtle.speed(0)
draw_dragon_curve(9, 250)
