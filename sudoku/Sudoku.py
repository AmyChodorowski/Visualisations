import numpy as np
import time as t

from IPython.display import clear_output


class Sudoku:

    def __init__(self):
        self.grid = [[0]*9 for i in range(9)]
        self.grid = np.array(self.grid)
        self.status = 'Initialised'

    def print_grid(self):
        print(self.grid)

    def print_grid_pretty(self):
        sep = '-------------------------'
        line = '| {0} {1} {2} | {3} {4} {5} | {6} {7} {8} |'

        graph = ''
        for ii in range(3):
            graph += '\n' + sep
            for jj in range(3):
                row_i = ii*3 + jj
                row = self.grid[row_i]
                graph += '\n' + line.format(*row)
        graph += '\n' + sep
        graph += '\n'

        clear_output(wait=True)
        print(graph)
        t.sleep(2)

    @staticmethod
    def print_ready():
        print('Ready', end=" ")
        for i in range(5):
            print('.', end=" ")
            t.sleep(1)
        print(".")

    def initialise_game_1(self):
        row_1 = [5, 3, 0, 0, 7] + [0] * 4
        row_2 = [6, 0, 0, 1, 9, 5] + [0] * 3
        row_3 = [0, 9, 8] + [0] * 4 + [6, 0]
        row_4 = [8] + [0] * 3 + [6] + [0] * 3 + [3]
        row_5 = [4] + [0] * 2 + [8, 0, 3] + [0] * 2 + [1]
        row_6 = [7] + [0] * 3 + [2] + [0] * 3 + [6]
        row_7 = [0, 6] + [0] * 4 + [2, 8, 0]
        row_8 = [0] * 3 + [4, 1, 9, 0, 0, 5]
        row_9 = [0] * 4 + [8, 0, 0, 7, 9]
        self.grid = np.array([row_1, row_2, row_3,
                              row_4, row_5, row_6,
                              row_7, row_8, row_9])
        self.status = 'Ready'

    def possible(self, y, x, n):
        # Row
        if n in self.grid[y, :]:
            # print("{} in row".format(n))
            return False

        # Columns
        elif n in self.grid[:, x]:
            # print("{} in column".format(n))
            return False

        # Box
        else:
            y0 = (y//3) * 3
            x0 = (x//3) * 3
            for i in range(3):
                for j in range(3):
                    if self.grid[y0+i, x0+j] == n:
                        # print("{} in box".format(n))
                        return False
        return True

    def solve(self):
        for y in range(9):
            for x in range(9):
                if self.grid[y, x] == 0:
                    for n in range(1, 10):
                        if self.possible(y, x, n):
                            self.grid[y, x] = n
                            self.solve()
                            self.grid[y, x] = 0
                    return

        self.print_grid_pretty()
        input("Done! Anymore solutions?")

    def solve_with_print(self):
        for y in range(9):
            for x in range(9):
                if self.grid[y, x] == 0:
                    for n in range(1, 10):
                        if self.possible(y, x, n):
                            # Fill in
                            self.grid[y, x] = n
                            self.print_grid_pretty()

                            # Start again
                            self.solve_with_print()

                            # Back track
                            self.grid[y, x] = 0
                            self.print_grid_pretty()
                    return

        self.print_grid_pretty()
        input("Done! Anymore solutions?")
