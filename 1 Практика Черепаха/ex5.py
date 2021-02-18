import turtle

turtle.shape('turtle')

for i in range(10, 110, 10):
    turtle.forward(i)
    turtle.left(90)
    turtle.forward(i)
    turtle.left(90)
    turtle.forward(i)
    turtle.left(90)
    turtle.forward(i)
    turtle.right(45)
    turtle.penup()
    turtle.forward(7)
    turtle.pendown()
    turtle.left(135)