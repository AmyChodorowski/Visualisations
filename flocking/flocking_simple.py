from flocking.Flock import *
from random import *

def set_screen(x, y):

    win = GraphWin('Simple flying', x, y)
    return win


def main():
    x = 600
    y = 400
    N = 50
    speed = 3
    perception = 10
    vision = 70
    alignment = True
    cohesion = True
    separation = True

    win = set_screen(x, y)

    flock = Flock(win, x, y, N=N, speed=(speed-speed/10, speed+speed/10), perception=perception, vision=vision)

    while True:

        try:
            for bird in flock.flock:
                bird.body.move(*bird.get_movement(flock.flock, flock.perception, flock.perception_2, vision,
                                                  alignment=alignment, cohesion=cohesion, separation=separation))
                #print(bird.heading)
            #print("--")


        except GraphicsError:
            break

    win.close()


main()
