import graphics as gr

SIZE_X = 800
SIZE_Y = 800

window = gr.GraphWin("Model", SIZE_X, SIZE_Y)

coords = gr.Point(400, 700)
velocity = gr.Point(2, 0)
acceleration = gr.Point(0, 0)

ball = gr.Circle(coords, 10)
ball.setFill('red')
ball.draw(window)

sun = gr.Circle(gr.Point(400, 400), 50)
sun.setFill('yellow')
sun.draw(window)


def add(point_1, point_2):
    new_point = gr.Point(point_1.x + point_2.x, point_1.y + point_2.y)
    return new_point


def sub(point_1, point_2):
    new_point = gr.Point(point_1.x - point_2.x, point_1.y - point_2.y)
    return new_point


def check_coords(coords, velocity):
    if coords.x < 0 or coords.x > SIZE_X:
        velocity.x = -velocity.x

    if coords.y < 0 or coords.y > SIZE_Y:
        velocity.y = -velocity.y


def update_velocity(velocity, acceleration):
    return add(velocity, acceleration)


def update_acceleration(ball_coords, center_coords):
    diff = sub(ball_coords, center_coords)
    distance_2 = (diff.x ** 2 + diff.y ** 2) ** (3 / 2)

    G = 2000

    return gr.Point(-diff.x * G / distance_2, -diff.y * G / distance_2)


while True:
    acceleration = update_acceleration(ball.getCenter(), gr.Point(400, 400))
    velocity = update_velocity(velocity, acceleration)
    check_coords(ball.getCenter(), velocity)
    ball.move(velocity.x, velocity.y)
    gr.time.sleep(0.02)
