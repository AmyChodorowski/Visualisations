from graphics import *
import math

class Spiro():

    def __init__(self, centre, r):
        self.centre = centre
        self.r = r
        self.k = 0.4
        self.l = 0.4

    def set_k(self, k):
        self.k = float(k)

    def get_k(self):
        return self.k

    def set_l(self, l):
        self.l = float(l)

    def get_l(self):
        return self.l

    def get_point(self, deg):
        angle = float(deg) * 0.0174533
        x_c, y_c = self.centre

        k_1 = 1 - self.k
        k_2 = (1 - self.k) / self.k

        x = x_c + self.r * (k_1 * math.cos(angle) + self.l * self.k * math.cos(k_2 * angle))
        y = y_c + self.r * (k_1 * math.sin(angle) - self.l * self.k * math.sin(k_2 * angle))

        return (x, y)

    def draw(self, win):

        if self.k != 1:
            turns = Spiro.calculate_turns(self.k, self.r)
            angle_max = 360 * turns
            resoultion = int(turns * 1000)
            # print(turns, resoultion)

            if resoultion < 20000:
                if turns > 5:
                    for i in range(0, resoultion):
                        angle = angle_max * (i / resoultion)
                        position_n = Spiro.get_point(self, angle)
                        p = Point(*position_n)
                        p.draw(win)
                else:
                    delay = 0.0001 / 2 * turns

                    for i in range(0, resoultion):
                        angle = angle_max * (i / resoultion)
                        position_n = Spiro.get_point(self, angle)
                        p = Point(*position_n)
                        time.sleep(delay)
                        p.draw(win)

    @staticmethod
    def calculate_turns(k, R):
        r = k * R
        turns = r / Spiro.float_gcd(R, r)
        return turns

    @staticmethod
    def float_gcd(a, b, rtol=1e-05, atol=1e-08):
        t = min(abs(a), abs(b))
        while abs(b) > rtol * t + atol:
            a, b = b, a % b
        return a