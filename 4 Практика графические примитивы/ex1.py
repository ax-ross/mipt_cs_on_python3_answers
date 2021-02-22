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


def draw_tree(x, y, window):
    def draw_crown(x, y, window):
        crown = gr.Polygon(gr.Point(x + 80, y), gr.Point(x + 80, y), gr.Point(x - 80, y), gr.Point(x, y - 80))
        crown.setFill('green')
        crown.setWidth(3)
        crown.draw(window)

    stem = gr.Rectangle(gr.Point(x - 5, y), gr.Point(x + 5, y + 80))
    stem.setFill('brown')
    stem.setWidth(3)
    stem.draw(window)

    draw_crown(x, y, window)
    draw_crown(x, y - 55, window)
    draw_crown(x, y - 110, window)


def main():
    window = gr.GraphWin('Test', 800, 800)
    draw_sky(window, 800, 800)
    draw_sun(100, 100, window)
    draw_clouds(300, 100, 25, window)
    draw_tree(500, 430, window)
    window.getMouse()
    window.close()


if __name__ == '__main__':
    main()
