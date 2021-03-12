import turtle


def curve_minkowski(n, l):
    if n == 0:
        turtle.forward(l)
    else:
        curve_minkowski(n - 1, l / 4)
        turtle.left(90)
        curve_minkowski(n - 1, l / 4)
        turtle.right(90)
        curve_minkowski(n - 1, l / 4)
        turtle.right(90)
        curve_minkowski(n - 1, l / 4)
        curve_minkowski(n - 1, l / 4)
        turtle.left(90)
        curve_minkowski(n - 1, l / 4)
        turtle.left(90)
        curve_minkowski(n - 1, l / 4)
        turtle.right(90)
        curve_minkowski(n - 1, l / 4)


curve_minkowski(2, 400)
