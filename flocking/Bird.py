import math
import cmath
from graphics import *

import numpy as np


class Bird():

    height = 15
    width = 5

    def __init__(self, win, x, y, id, start, heading, speed):
        self.win = win
        self.x_limit = x
        self.y_limit = y

        self.id = id

        self.heading = heading
        self.speed = speed

        self.body = ''
        Bird.get_body(self, start)

    def get_body(self, start):
        x_c, y_c = start

        p1 = Point(x_c + Bird.width, y_c)
        p2 = Point(x_c, y_c)
        p3 = Point(x_c - Bird.width, y_c)
        p4 = Point(x_c, y_c + Bird.height)

        self.body = Polygon(Bird.rotate_points(deg=self.heading,
                                               points=[p1, p2, p3, p4]))

    def get_movement(self, flock):

        # Avoid the edge - change in heading
        s = Bird.avoid_edges(self)
        if s:
            Bird.rotate_bird(self, s)

        # Others birds - change in heading (steering)
        x0 = self.body.points[1].x
        y0 = self.body.points[1].y
        #p = Bird.apply_behaviour(self, x0, y0, flock)

        angle = float(self.heading) * 0.0174533
        return self.speed*math.sin(angle), self.speed*math.cos(angle)

    def avoid_edges(self):
        h = self.heading
        s = [0, 0, 0, 0]
        x = self.body.points[1].x
        y = self.body.points[1].y

        # Side closest to
        if y > self.y_limit - Bird.height:
            s[0] = 1
        elif y < Bird.height:
            s[2] = 1

        if x > self.x_limit - Bird.height:
            s[1] = 1
        elif x < Bird.height:
            s[3] = 1

        if s != [0, 0, 0, 0]:
            # Bottom right
            if 0 <= h < 90:
                if s[0] == 1 and s[1] == 1:
                    return 180
                if s[0] == 1:
                    return 180 - 2*h
                elif s[1] == 1:
                    return 360 - 2*h

            # Top right
            elif 90 <= h < 180:
                if s[1] == 1 and s[2] == 1:
                    return 180
                elif s[1] == 1:
                    return 360 - 2 * h
                elif s[2] == 1:
                    return 540 - 2 * h

            # Top left
            elif 180 <= h < 270:
                if s[2] == 1 and s[3] == 1:
                    return 180
                elif s[2] == 1:
                    return 540 - 2 * h
                elif s[3] == 1:
                    return 720 - 2 * h

            # Top right
            else:
                if s[3] == 1 and s[0] == 1:
                    return 180
                elif s[3] == 1:
                    return 720 - 2 * h
                elif s[0] == 1:
                    return 900 - 2 * h

    def rotate_bird(self, deg):
        """ Rotate polygon clockwise about its center. """

        # Rotate
        self.body.undraw()
        self.body.points = Bird.rotate_points(deg=deg, points=self.body.getPoints())
        self.body.draw(self.win)

        # Change heading
        self.heading = (self.heading + deg) % 360

    @staticmethod
    def rotate_points(deg, points):
        theta = float(deg) * 0.0174533
        cosang, sinang = math.cos(theta), math.sin(theta)
        cx, cy = Bird.get_centre(points)

        new_points = []
        for p in points:
            x, y = p.getX(), p.getY()
            tx, ty = x - cx, y - cy
            new_x = (tx * cosang + ty * sinang) + cx
            new_y = (-tx * sinang + ty * cosang) + cy
            new_points.append(Point(new_x, new_y))

        return new_points

    @staticmethod
    def get_centre(points):

        n = len(points)
        cx = sum(p.getX() for p in points) / n
        cy = sum(p.getY() for p in points) / n

        return cx, cy

    def apply_behaviour(self, x0, y0, flock, perception):

        for bird in flock:
            if bird.id != self.id:

                x = bird.body.points[1].x
                y = bird.body.points[1].y

                norm = (x - x0)**2 + (y - y0)**2

                if norm < (perception*Bird.height)**2:

                    # alginment
                    pass

    @staticmethod
    def average_heading(deg):
        t = 0
        for d in deg:
            d = math.radians(d)
            s2 = complex(math.sin(d), math.cos(d))
            t += s2
        b = t / len(deg)
        a = math.atan2(round(b.real, 15), round(b.imag, 15))
        return Bird.map_atan2(a)

    def align(self):
        pass

    def cohesion(self):
        pass

    def seperation(self):
        pass

    @staticmethod
    def map_atan2(rad):
        d = math.degrees(rad)
        if d < 0.0:
            return d + 360.0
        else:
            return d

    @staticmethod
    def recalculate_heading():
        pass







