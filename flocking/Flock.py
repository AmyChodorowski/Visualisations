from flocking.Bird import *
from random import *


class Flock():

    def __init__(self, win, x, y, N, speed, perception, vision, alignment=False, cohesion=False, separation=False):
        self.win = win
        self.x_limit = x
        self.y_limit = y

        self.s = speed
        self.vision = vision
        self.perception = perception * Bird.height
        self.perception_2 = (perception * Bird.height)**2

        self.flock = []
        Flock.create_flock(self, N)

        self.alignment = alignment
        self.cohesion = cohesion
        self.separation = separation

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

