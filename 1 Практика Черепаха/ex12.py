import turtle


def draw_arc(n):
    for i in range(90):
        turtle.right(2)
        turtle.forward(n)


turtle.left(90)
turtle.shape('turtle')
for i in range(5):
    draw_arc(1)
    draw_arc(0.2)
