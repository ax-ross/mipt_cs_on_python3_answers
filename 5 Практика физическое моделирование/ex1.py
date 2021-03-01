import graphics as gr

SIZE_X = 400
SIZE_Y = 400

window = gr.GraphWin("Model", SIZE_X, SIZE_Y)

coords = gr.Point(200, 200)
velocity = gr.Point(1, -2)
acceleration = gr.Point(0, 0.1)
ball = gr.Circle(coords, 10)
ball.setFill('red')
ball.draw(window)


def add(point_1, point_2):
    new_point = gr.Point(point_1.x + point_2.x, point_1.y + point_2.y)
    return new_point


def sub(point_1, point_2):
    new_point = gr.Point(point_1.x - point_2.x, point_1.y - point_2.y)
    return new_point


def clear_window():
    rectangle = gr.Rectangle(gr.Point(0, 0), gr.Point(SIZE_X, SIZE_Y))
    rectangle.setFill('green')
    rectangle.draw(window)


def check_coords(coords, velocity):
    if coords.x < 0 or coords.x > SIZE_X:
        velocity.x = -velocity.x

    if coords.y < 0 or coords.y > SIZE_Y:
        velocity.y = -velocity.y


def update_velocity(velocity, acceleration):
    return add(velocity, acceleration)


def update_acceleration(ball_coords, center_cords):
    diff = sub(ball_coords, center_cords)
    distance_2 = (diff.x ** 2 + diff.y ** 2) ** (3 / 2)
    G = 2000
    return gr.Point(-diff.x * G / distance_2, -diff.y * G / distance_2)


while True:
    acceleration = update_acceleration(coords, gr.Point(400, 400))
    velocity = update_velocity(velocity, acceleration)
    check_coords(coords, velocity)
    ball.move(velocity.x, velocity.y)
    gr.time.sleep(0.02)
