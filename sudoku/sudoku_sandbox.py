# https://www.youtube.com/watch?v=G_UYXzGuqvM


from sudoku.Sudoku import Sudoku

s = Sudoku()
s.initialise_game_1()
s.print_grid_pretty()

print('Ready')
print('')

s.solve()
