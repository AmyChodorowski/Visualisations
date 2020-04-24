from flocking.Flock import *


def set_screen(x, y):

    win = GraphWin('Simple flying', x, y)
    return win


def main():
    x = 500
    y = 500

    win = set_screen(x, y)


    flock = Flock(win, x, y, N=10, speed=(2/20, 5/20), perception=5)

    while True:

        try:
            for index, bird in enumerate(flock.flock):
                bird.body.move(*bird.get_movement(flock.flock))

        except GraphicsError:
            break

    win.close()


main()
