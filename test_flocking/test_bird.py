import unittest
import itertools
import random

from flocking.Bird import Bird


class TestBird(unittest.TestCase):

    # Average heading
    def test_average_heading_all_opposites(self):
        all_opposite = [0, 90, 180, 270]

        self.assertEqual(Bird.average_heading([x+0 for x in all_opposite]), 180)
        self.assertEqual(Bird.average_heading([x+45 for x in all_opposite]), 180)
        self.assertEqual(Bird.average_heading([x+36 for x in all_opposite]), 180)
        self.assertEqual(Bird.average_heading([(x+200) % 360 for x in all_opposite]), 0)

    def test_average_heading_test_close_groups(self):
        self.assertEqual(Bird.average_heading([350, 10]), 0)
        self.assertEqual(Bird.average_heading([10, 20, 30]), 20)
        self.assertEqual(Bird.average_heading([89, 90, 91]), 90)

    def test_average_heading_test_close_groups_and_anomaly(self):
        close_group = [1, 2, 3, 3, 2, 1]

        self.assertEqual(Bird.average_heading(close_group), 2)
        self.assertTrue(Bird.average_heading(close_group + [90]) > 2)
        self.assertTrue(Bird.average_heading(close_group + [180]) > 2)
        self.assertEqual(Bird.average_heading(close_group + [182]), 2)
        self.assertTrue(Bird.average_heading(close_group + [184]) < 2)

        self.assertTrue(Bird.average_heading(close_group + [200]) > 358)
        self.assertTrue(Bird.average_heading(close_group + [200]) < 360)

    def test_average_heading_test_different_permutations(self):
        self.assertEqual(Bird.average_heading([0, 90, 180, 270]), 180)
        self.assertEqual(Bird.average_heading([90, 0, 180, 270]), 180)
        self.assertEqual(Bird.average_heading([90, 180, 0, 270]), 180)
        self.assertEqual(Bird.average_heading([90, 180, 270, 0]), 0)

    def test_average_heading_test_different_permutations_2(self):
        sets = itertools.permutations([10, 20, 30])
        for s in sets:
            self.assertEqual(Bird.average_heading(list(s)), 20)

    # Rotating
    def test_rotating_accuracy(self):
        s_0 = (5, 1)
        h = 4
        rotate = [90, 10, 40, 20, 323, 25, 23]

        b = Bird(start=s_0, heading=h, speed=None, win=None, x=None, y=None, id=None)
        p = b.body.points
        print("Initial heading: %f, %f " % (h, Bird.calculate_heading(base=[p[1].x, p[1].y],
                                                                      tip=[p[3].x, p[3].y])))

        for _ in range(10000):
            r = random.randint(0, 306)
            p = Bird.rotate_points(r, p)
            h += r
            h = h % 360

            print("Rotate: %d, Heading: %f, %f" % (r, h, Bird.calculate_heading(base=[p[1].x, p[1].y],
                                                                                tip=[p[3].x, p[3].y])))
