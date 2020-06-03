# https://www.youtube.com/watch?v=G_UYXzGuqvM

from sudoku.Sudoku import Sudoku

s = Sudoku()
s.initialise_game_1()
s.print_ready()
s.print_grid_pretty()
s.solve_simple_constraint()
s.print_grid_pretty()

