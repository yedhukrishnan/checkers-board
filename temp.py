from checkers_board import *
from printer import *
from assets import *
from helpers import *

#pi = { 'black': 'b', 'white': 'w' }
b = CheckersBoard(piece)
#p = Printer(b)
print_board(b.wooden_board)

# initial_white_row_and_columns = 

b.set_pieces_on_board_for_a_new_game(initial_white_positions, initial_black_positions)
print_board(b.wooden_board)

print b.get_piece([7, 0])

# Yet to decide where to place this method
