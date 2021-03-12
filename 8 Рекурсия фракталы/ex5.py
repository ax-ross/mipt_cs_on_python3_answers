import turtle


def draw_curve_minkowski(n, l):
    if n == 0:
        turtle.forward(l)
    else:
        draw_curve_minkowski(n - 1, l / 4)
        turtle.left(90)
        draw_curve_minkowski(n - 1, l / 4)
        turtle.right(90)
        draw_curve_minkowski(n - 1, l / 4)
        turtle.right(90)
        draw_curve_minkowski(n - 1, l / 4)
        draw_curve_minkowski(n - 1, l / 4)
        turtle.left(90)
        draw_curve_minkowski(n - 1, l / 4)
        turtle.left(90)
        draw_curve_minkowski(n - 1, l / 4)
        turtle.right(90)
        draw_curve_minkowski(n - 1, l / 4)


draw_curve_minkowski(2, 400)
