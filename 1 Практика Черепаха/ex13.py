import turtle


def draw_circle(n):
    for i in range(180):
        turtle.left(2)
        turtle.forward(n)


def draw_arc(n):
    for i in range(90):
        turtle.right(2)
        turtle.forward(n)


turtle.shape('turtle')

turtle.fillcolor('yellow')
turtle.begin_fill()
draw_circle(3)
turtle.end_fill()

turtle.left(90)
turtle.penup()
turtle.goto(40, 120)
turtle.pendown()

turtle.fillcolor('blue')
turtle.begin_fill()
draw_circle(0.3)
turtle.end_fill()

turtle.penup()
turtle.goto(-30, 120)
turtle.pendown()

turtle.begin_fill()
draw_circle(0.3)
turtle.end_fill()

turtle.penup()
turtle.goto(0, 100)
turtle.pendown()
turtle.width(10)
turtle.goto(0, 60)

turtle.penup()
turtle.goto(35, 50)
turtle.pendown()
turtle.left(180)

turtle.color('red')
draw_arc(1.2)
