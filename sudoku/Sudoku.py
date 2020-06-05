import numpy as np
import time as t

from IPython.display import clear_output


class Sudoku:

    def __init__(self):
        self.grid = [[0]*9 for i in range(9)]
        self.grid = np.array(self.grid)
        self.status = 'Initialised'
        self.unsolved = []
        self.find_unsolved()
        self.solutions = 0

    def print_grid(self):
        print(self.grid)

    def print_grid_pretty(self, sleeping=0.1):
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
        t.sleep(sleeping)

    @staticmethod
    def print_ready():
        print('Ready', end=" ")
        for i in range(5):
            print('.', end=" ")
            t.sleep(1)
        print(".")

    def initialise_game_1(self):
        """
        Easy
        """
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

    def initialise_game_2(self):
        """
        Hard
        """
        row_1 = [5] + [0] * 8
        row_2 = [0] * 5 + [9] + [0] * 3
        row_3 = [0] * 6 + [7, 8, 5]
        row_4 = [0, 0, 7, 0, 4, 8, 0, 5, 0]
        row_5 = [0, 0, 1, 3] + [0] * 5
        row_6 = [0, 0, 6, 0, 7] + [0] * 4
        row_7 = [8, 6] + [0] * 4 + [9, 0 ,3]
        row_8 = [7] + [0] * 4 + [5, 0, 6, 2]
        row_9 = [0] * 2 + [3, 7] + [0] * 5
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
        """
        Recursive method solve
        :return:
        """
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
                            self.print_grid_pretty(sleeping=0.01)

                            # Start again
                            self.solve_with_print()

                            # Back track
                            self.grid[y, x] = 0
                            self.print_grid_pretty(sleeping=0.01)
                    return

        self.print_grid_pretty()
        input("Done! Anymore solutions?")

    def solve_count(self):
        for y in range(9):
            for x in range(9):
                if self.grid[y, x] == 0:
                    for n in range(1, 10):
                        if self.possible(y, x, n):
                            # Fill in
                            self.grid[y, x] = n

                            # Start again
                            self.solve_count()

                            # Back track
                            self.grid[y, x] = 0
                    return

        self.find_unsolved()
        if len(self.unsolved) == 0:
            print('Found a good solution')
            self.solution += 1
        else:
            print('Found a false solution')

    def find_unsolved(self):
        """
        Get a list of index for unsolved spots
        :return: list()
        """
        self.unsolved = []
        for y in range(9):
            for x in range(9):
                if self.grid[y, x] == 0:
                    self.unsolved.append([y, x])

    def solve_simple_constraint(self):
        self.find_unsolved()
        unsolved_before = len(self.unsolved)
        unsolved_after = None

        while len(self.unsolved) > 0 and unsolved_before != unsolved_after:
            unsolved_before = len(self.unsolved)
            self.check_unsolved_solutions()
            unsolved_after = len(self.unsolved)

    def solve_simple_constraint_with_print(self):
        self.find_unsolved()
        unsolved_before = len(self.unsolved)
        unsolved_after = None

        while len(self.unsolved) > 0 and unsolved_before != unsolved_after:
            unsolved_before = len(self.unsolved)
            self.check_unsolved_solutions()
            unsolved_after = len(self.unsolved)

            self.print_grid_pretty(sleeping=1)

    def possible_values(self, y, x):
        """
        Returns a list of possible values for grid [y,x]
        :return: list()
        """
        possible_values = []
        for n in range(1, 10):
            if self.possible(y, x, n):
                possible_values.append(n)

        if possible_values:
            return possible_values
        else:
            raise ValueError("Grid [{y}, {x}] has no possible solutions".format(y=y, x=x))

    def check_unsolved_solutions(self):
        """
        Going through the unsolved solutions and checking
        """
        remove_index = []

        for index, coor in enumerate(self.unsolved):
            values = self.possible_values(*coor)

            # Solution found
            if len(values) == 1:
                print("Grid [{y}, {x}] is {v}".format(y=coor[0], x=coor[1], v=values[0]))
                self.grid[coor[0], coor[1]] = values[0]  # Update grid
                remove_index.append(index)  # Remove from unsolved

        self.unsolved = [i for j, i in enumerate(self.unsolved) if j not in remove_index]
