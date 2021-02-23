import graphics as gr


def draw_sky(window, width, height):
    sky = gr.Rectangle(gr.Point(0, 0), gr.Point(width, height / 2))
    sky.setFill('blue')
    sky.draw(window)


def draw_sun(x, y, window):
    sun = gr.Circle(gr.Point(x, y), 50)
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


def draw_house(x, y, window):
    def draw_roof(x, y, window):
        roof = gr.Polygon(gr.Point(x, y), gr.Point(x, y), gr.Point(x + 250, y), gr.Point(x + 125, y - 125))
        roof.setFill('brown')
        roof.setWidth(3)
        roof.draw(window)

    def draw_facade(x, y, window):
        facade = gr.Rectangle(gr.Point(x, y), gr.Point(x + 250, y + 250))
        facade.setFill('grey')
        facade.setWidth(3)
        facade.draw(window)

    def draw_casement(x, y, window):
        casement = gr.Rectangle(gr.Point(x + 80, y + 80), gr.Point(x + 170, y + 170))
        casement.setFill('yellow')
        casement.setWidth(3)
        casement.draw(window)
        casement = gr.Line(gr.Point(x + 125, y + 80), gr.Point(x + 125, y + 170))
        casement.setWidth(3)
        casement.draw(window)
        casement = gr.Line(gr.Point(x + 80, y + 125), gr.Point(x + 170, y + 125))
        casement.setWidth(3)
        casement.draw(window)

    draw_roof(x, y, window)
    draw_facade(x, y, window)
    draw_casement(x, y, window)


def draw_earth(window, width, height):
    earth = gr.Rectangle(gr.Point(0, height / 2), gr.Point(width, height))
    earth.setFill('silver')
    earth.draw(window)


def main():
    window = gr.GraphWin('Test', 800, 800)
    draw_sky(window, 800, 800)
    draw_earth(window, 800, 800)
    draw_sun(600, 100, window)
    draw_clouds(200, 100, 25, window)
    draw_tree(650, 500, window)
    draw_house(150, 300, window)
    window.getMouse()
    window.close()


if __name__ == '__main__':
    main()
