import turtle

turtle.shape('turtle')
turtle.speed(50)
inc = 0.001
while inc < 1:
    turtle.forward(inc)
    turtle.left(2)
    inc += 0.001
    print(inc)