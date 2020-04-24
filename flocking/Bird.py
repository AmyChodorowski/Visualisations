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

    def get_movement(self, flock, perception, perception_2, alignment=False, cohesion=False, separation=False):

        # Avoid the edge - change in heading
        if Bird.close_to_edge(self, perception/10):
            rotate = Bird.avoid_edges(self)
            if rotate:
                Bird.rotate_bird(self, rotate)

        # Others birds - change in heading (steering)
        else:
            if alignment or cohesion or separation:
                x0 = self.body.points[1].x
                y0 = self.body.points[1].y
                steering = Bird.apply_behaviour(self, x0, y0, flock, perception_2,
                                                alignment, cohesion, separation)

                if steering:
                    rotate = 0.1*(steering - self.heading)
                    Bird.rotate_bird(self, rotate)

        angle = float(self.heading) * 0.0174533
        return self.speed*math.sin(angle), self.speed*math.cos(angle)

    def close_to_edge(self, perception):

        x = self.body.points[1].x
        y = self.body.points[1].y

        # Side closest to
        if y > self.y_limit - perception:
            return True
        elif y < perception:
            return True

        if x > self.x_limit - perception:
            return True
        elif x < perception:
            return True

        return False

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
    def calculate_heading(base, tip):

        # get x,y
        x = tip[0] - base[0]
        y = tip[1] - base[1]

        # get deg
        rad = math.atan2(x, y)
        deg = Bird.map_atan2(rad)

        return deg

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

    def apply_behaviour(self, x0, y0, flock, perception_2, alignment, cohesion, separation):
        affected = False
        align_headings = []
        cohesion_x = []
        cohesion_y = []
        seperation_x = []
        seperation_y = []

        for bird in flock:
            if bird.id != self.id:

                x = bird.body.points[1].x
                y = bird.body.points[1].y
                h = bird.heading

                norm = (x - x0)**2 + (y - y0)**2
                if norm < perception_2:
                    affected = True
                    align_headings.append(h)
                    cohesion_x.append(x)
                    cohesion_y.append(y)
                    seperation_x.append(x/norm)
                    seperation_y.append(y/norm)

        # Cohesion
        if affected:
            steering_headings = []

            if alignment:
                steering_headings.append(Bird.average_heading(align_headings))

            if cohesion:
                cohesion_headings = [sum(cohesion_x)/len(cohesion_x), sum(cohesion_y)/len(cohesion_y)]
                steering_headings.append(Bird.calculate_heading([x0, y0], cohesion_headings))

            if separation:
                separation_headings = [sum(seperation_x) / len(seperation_x), sum(seperation_y) / len(seperation_y)]
                steering_headings.append(Bird.calculate_heading([x0, y0], separation_headings))

            if len(steering_headings) == 0 :
                return steering_headings[0]
            else:
                return Bird.average_heading(steering_headings)

        else:
            return False

    @staticmethod
    def average_heading(deg):
        if len(deg) > 0:
            t = 0
            for d in deg:
                d = math.radians(d)
                t += complex(math.sin(d), math.cos(d))
            a = math.atan2(round(t.real, 15), round(t.imag, 15))
            return round(Bird.map_atan2(a), 12)
        else:
            return None

    @staticmethod
    def map_atan2(rad):
        d = math.degrees(rad)
        if d < 0.0:
            return d + 360.0
        else:
            return abs(d)









