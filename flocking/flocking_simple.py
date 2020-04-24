from flocking.Flock import *


def set_screen(x, y):

    win = GraphWin('Simple flying', x, y)
    return win


def main():
    x = 800
    y = 800
    speed = 3
    perception = 5
    align = True
    cohesion = False
    separation = False

    win = set_screen(x, y)

    flock = Flock(win, x, y, N=50, speed=(speed-speed/10, speed+speed/10), perception=perception)

    while True:

        try:
            for bird in flock.flock:
                bird.body.move(*bird.get_movement(flock.flock, flock.perception, flock.perception_2,
                                                  align=align, cohesion=cohesion, separation=separation))
                # time.sleep(0.0001)


        except GraphicsError:
            break

    win.close()


main()
