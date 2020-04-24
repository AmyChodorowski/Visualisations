from flocking.Flock import *
from random import *

def set_screen(x, y):

    win = GraphWin('Simple flying', x, y)
    return win


def main():
    x = 800
    y = 800
    N = 50
    speed = 5
    perception = 10
    alignment = True
    cohesion = True
    separation = False

    win = set_screen(x, y)

    flock = Flock(win, x, y, N=N, speed=(speed-speed/10, speed+speed/10), perception=perception)

    while True:

        try:
            for bird in flock.flock:
                bird.body.move(*bird.get_movement(flock.flock, flock.perception, flock.perception_2,
                                                  alignment=alignment, cohesion=cohesion, separation=separation))
                #time.sleep(0.0001)


        except GraphicsError:
            break

    win.close()


main()
