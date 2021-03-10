import turtle


def draw_koch_curve(n, l):
    if n == 1:
        turtle.forward(l / 3)

    else:
        draw_koch_curve(n - 1, l / 3)
        turtle.left(60)
        draw_koch_curve(n - 1, l / 3)
        turtle.right(120)
        draw_koch_curve(n - 1, l / 3)
        turtle.left(60)
        draw_koch_curve(n - 1, l / 3)


turtle.speed('fastest')
draw_koch_curve(2, 150)
