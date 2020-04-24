import unittest

from flocking.Bird import Bird


class TestBird(unittest.TestCase):

    def test_average_heading_all_opposites(self):
        all_opposite = [0, 90, 180, 270]
        sets = [[x+0 for x in all_opposite],
                [x+45 for x in all_opposite], #45
                [x+36 for x in all_opposite],  # 36
                [(x+200) % 360 for x in all_opposite],
                [x+360 for x in all_opposite]]

        for angles in sets:
            print('The mean angle of', angles, 'is:', round(Bird.average_heading(angles), 12), 'degrees')
            print()

    def test_average_heading_test_close_groups(self):
        sets = [[350, 10],
                [10, 20, 30],
                [89, 90, 91]]

        for angles in sets:
            print('The mean angle of', angles, 'is:', round(Bird.average_heading(angles), 12), 'degrees')
            print()

    def test_average_heading_test_close_groups_and_anomaly(self):
        close_group = [1, 2, 3, 3, 2, 1]
        sets = [close_group,
                close_group + [90],
                close_group + [180],
                close_group + [182],
                close_group + [184],
                close_group + [200],
                close_group + [250],
                close_group+[270]]
        for angles in sets:
            print('The mean angle of', angles, 'is:', round(Bird.average_heading(angles), 12), 'degrees')
            print()

    def test_average_heading_test_different_permutations(self):
        sets = [
                [0, 90, 180, 270],
                [90, 0, 180, 270],
                [90, 180, 0, 270],
                [90, 180, 270, 0]]

        for angles in sets:
            print('The mean angle of', angles, 'is:', round(Bird.average_heading(angles), 12), 'degrees')
            print()

    def test_average_heading_test_different_permutations_2(self):
        sets = [[10, 20, 30],
                [10, 30, 20],
                [20, 10, 30],
                [20, 30, 10],
                [30, 10, 20],
                [30, 10, 20]]

        for angles in sets:
            print('The mean angle of', angles, 'is:', round(Bird.average_heading(angles), 12), 'degrees')
            print()



    def test_rotating(self):
        pass
