import random

from spirograph.Spiro import *
from graphics import *


def set_screen(win, X, Y, main_r):

    # Points = [x,y]
    main_center = (X / 2, Y / 2)
    main_top = (X / 2, 0)
    main_bottom = (X / 2, Y)
    main_left = (0, Y / 2)
    main__right = (X, Y / 2)

    # Main points
    pt_center = Point(*main_center)
    pt_top = Point(*main_top)
    pt_bottom = Point(*main_bottom)
    pt_left = Point(*main_left)
    pt_right = Point(*main__right)

    # Main circle
    cir = Circle(pt_center, main_r)
    cir.draw(win)
    x_axis = Line(pt_top, pt_bottom)
    y_axis = Line(pt_left, pt_right)
    x_axis.draw(win)
    y_axis.draw(win)

    # K
    Text(Point(X+20, 50), 'K:').draw(win)
    entry_k = Entry(Point(X+80, 50), 10)
    entry_k.setText(float(90/main_r))
    entry_k.draw(win)

    # L
    Text(Point(X+20, 100), 'L:').draw(win)
    entry_l = Entry(Point(X+80, 100), 10)
    entry_l.setText(0.9)
    entry_l.draw(win)

    return entry_k, entry_l


def remove_spiro(win):
    for item in win.items[7:]:
        item.undraw()
    win.update()


def main():
    Y = 500.0
    X = 500.0
    main_r = 200
    main_center = (X / 2, Y / 2)

    win = GraphWin('Spirograph', X+200, Y)

    entry_k, entry_l = set_screen(win, X, Y, main_r)
    spiro = Spiro(main_center, main_r)

    while True:

        try:

            # Calculate k and l
            k = (random.randint(-50, 10)/60) + 1
            l = (random.randint(-50, 10)/60) + 1

            # Set k
            spiro.set_k(k)
            entry_k.setText(k)

            # Set l
            spiro.set_l(k)
            entry_l.setText(l)

            # Draw spirograph
            spiro.draw(win)

            # Remove flocking
            remove_spiro(win)

        except GraphicsError:
            break

    win.close()

main()
