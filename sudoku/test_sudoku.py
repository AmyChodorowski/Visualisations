import unittest

from sudoku.Sudoku import Sudoku


class TestSudoku(unittest.TestCase):

    def test_initialise_game_1(self):
        s = Sudoku()
        s.initialise_game_1()

        self.assertEqual(s.grid[2, 0], 0)
        self.assertEqual(s.grid[0, 2], 0)
        self.assertEqual(s.grid[0, 3], 0)

    def test_possible(self):
        s = Sudoku()
        s.initialise_game_1()

        self.assertFalse(s.possible(4, 4, 1))
        self.assertFalse(s.possible(4, 4, 2))
        self.assertFalse(s.possible(4, 4, 3))
        self.assertFalse(s.possible(4, 4, 4))
        self.assertTrue(s.possible(4, 4, 5))
        self.assertFalse(s.possible(4, 4, 6))
        self.assertFalse(s.possible(4, 4, 7))
        self.assertFalse(s.possible(4, 4, 8))
        self.assertFalse(s.possible(4, 4, 9))

        # Check box 1a
        self.assertFalse(s.possible(2, 0, 3))
        self.assertFalse(s.possible(0, 2, 3))

        # Check box 2c
        self.assertFalse(s.possible(8, 6, 5))

        # Bug 1
        self.assertFalse(s.possible(0, 3, 1))

    def test_find_unsolved(self):
        s = Sudoku()

        self.assertEqual(len(s.unsolved), (9 * 9))

        s.initialise_game_1()
        s.find_unsolved()

        self.assertEqual(len(s.unsolved), (9 * 9) - 30)

        self.assertListEqual(s.unsolved[0], [0, 2])
        self.assertListEqual(s.unsolved[9], [1, 7])
        self.assertListEqual(s.unsolved[50], [8, 6])

    def test_possible_values(self):
        s = Sudoku()
        s.initialise_game_1()

        self.assertListEqual(s.possible_values(3, 3), [5, 7, 9])
        self.assertListEqual(s.possible_values(4, 4), [5])
        self.assertListEqual(s.possible_values(7, 1), [2, 7, 8])

    def test_check_unsolved_solutions(self):
        s = Sudoku()
        s.initialise_game_1()
        s.find_unsolved()

        us_b1 = s.unsolved
        s.check_unsolved_solutions()
        us_a1 = s.unsolved

        # 1) Grid [4, 4] is 5
        # 2) Grid [5, 3] is 9
        # 3) Grid [6, 4] is 3
        # 4) Grid [6, 5] is 7
        # 5) Grid [6, 8] is 4
        # 6) Grid [7, 7] is 3

        self.assertEqual(len(us_b1), 51)
        self.assertEqual(len(us_a1), 51 - 6)

        us_b2 = s.unsolved
        s.check_unsolved_solutions()
        us_a2 = s.unsolved

        # 1) Grid [2, 4] is 4
        # 2) Grid [2, 5] is 2
        # 3) Grid [2, 8] is 7
        # 4) Grid [3, 3] is 7
        # 5) Grid [4, 1] is 2
        # 6) Grid [4, 7] is 9
        # 7) Grid [6, 3] is 5
        # 8) Grid [7, 0] is 2
        # 9) Grid [7, 2] is 7
        # 10) Grid [7, 6] is 6
        # 11) Grid [8, 5] is 6
        # 12) Grid [8, 6] is 1

        self.assertEqual(len(us_b2), 51 - 6)
        self.assertEqual(len(us_a2), 51 - 6 - 12)
        pass



