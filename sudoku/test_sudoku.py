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
