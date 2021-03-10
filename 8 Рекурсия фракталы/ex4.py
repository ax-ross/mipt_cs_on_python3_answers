import turtle


def draw_koch_snowflake(n, l):
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

    for i in range(3):
        draw_koch_curve(n, l)
        turtle.right(120)


turtle.speed('fastest')
draw_koch_snowflake(5, 150)

