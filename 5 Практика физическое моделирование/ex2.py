import graphics as gr

SIZE_X = 800
SIZE_Y = 800

window = gr.GraphWin("Model", SIZE_X, SIZE_Y)

coords = gr.Point(400, 400)
velocity = gr.Point(6, 0)
acceleration = gr.Point(-0.1, 0)

ball = gr.Circle(coords, 10)
ball.setFill('red')
ball.draw(window)


def add(point_1, point_2):
    new_point = gr.Point(point_1.x + point_2.x, point_1.y + point_2.y)
    return new_point



def update_velocity(velocity, acceleration):
    return add(velocity, acceleration)


dy = -0.5
while True:
    velocity = update_velocity(velocity, acceleration)
    ball.move(velocity.x, dy)
    gr.time.sleep(0.04)
    if velocity.x < -6 or velocity.x > 6:
        acceleration.x = -acceleration.x
    if velocity.x < 0 and acceleration.x < 0:
        dy = 0.5
    elif velocity.x < 0 and acceleration.x > 0:
        dy = -0.5
    elif velocity.x > 0 and acceleration.x > 0:
        dy = 0.5
    else:
        dy = -0.5
