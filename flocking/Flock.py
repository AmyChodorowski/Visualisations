from flocking.Bird import *
from random import *


class Flock():

    def __init__(self, win, x, y, N, speed, perception):
        self.win = win
        self.x_limit = x
        self.y_limit = y

        self.s = speed
        self.perception = perception  # Distance in hieghts

        self.flock = []
        Flock.create_flock(self, N)

    def create_flock(self, N):
        deg = (0, 360)
        height = Bird.height
        x = self.x_limit
        y = self.y_limit
        w = self.win

        for i in range(N):
            c = (randint(0+height, x-height), randint(0+height, y-height))
            h = randint(*deg)
            s = uniform(*self.s)
            b = Bird(w, x, y, i, c, h, s)
            b.body.draw(w)
            self.flock.append(b)

    def order_flock(self, N):
        pass

