import graphics as gr


def draw_sky(window, width, height):
    sky = gr.Rectangle(gr.Point(0, 0), gr.Point(width, height / 2))
    sky.setFill('blue')
    sky.draw(window)


def draw_sun(x, y, window):
    sun = gr.Circle(gr.Point(x, y), 20)
    sun.setFill('yellow')
    sun.draw(window)


def draw_clouds(x, y, r, window):
    cloud = gr.Circle(gr.Point(x - r // 2, y), r)
    cloud.setFill('white')
    cloud.draw(window)

    cloud = gr.Circle(gr.Point(x + r // 2, y), r)
    cloud.setFill('white')
    cloud.draw(window)

    cloud = gr.Circle(gr.Point(x + r, y + r // 2), r)
    cloud.setFill('white')
    cloud.draw(window)

    cloud = gr.Circle(gr.Point(x, y + r // 2), r)
    cloud.setFill('white')
    cloud.draw(window)

    cloud = gr.Circle(gr.Point(x - r, y + r // 2), r)
    cloud.setFill('white')
    cloud.draw(window)


def main():
    window = gr.GraphWin('Test', 800, 800)
    draw_sky(window, 800, 800)
    draw_sun(100, 100, window)
    draw_clouds(300, 100, 25, window)
    window.getMouse()
    window.close()


if __name__ == '__main__':
    main()
