# https://www.youtube.com/watch?v=G_UYXzGuqvM

from sudoku.Sudoku import Sudoku

s = Sudoku()
s.initialise_game_2()
s.print_grid_pretty()
s.solve_count()
print('There are {n} soultions'.format(n=s.solutions))

