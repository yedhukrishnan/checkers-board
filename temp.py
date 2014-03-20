# TEMP file: for testing ONLY

from checkers_board import *
from printer import *
from assets import *
from helpers import *
from movement import *
from move_list import *

# Print empty wooden board
b = CheckersBoard(piece)
print_board(b.wooden_board)

# Set and print initial board
b.set_pieces_on_board_for_a_new_game(initial_white_positions, initial_black_positions)
print_board(b.wooden_board)

# Check if the board returns the correct piece
print b.get_piece([7, 0])

m = Movement(b, piece)

#  position parser shouldn't be a part of movement class. Movement class should deal with rows and columns only
init_pos = position_parser('c3')
fin_pos = position_parser('b4')

# Make and check a simple move
# m.make_simple_move(init_pos, fin_pos)
# print_board(b.wooden_board)


# Make and check a capturing nove
# b.set_piece([4, 5], 'b')
# print_board(b.wooden_board)
# m.make_capture_move([5, 4], [3, 6])

print_board(b.wooden_board)


#readable_position([0,0])
#readable_position([7,7])
#readable_position([0,7])
#readable_position([7,0])

ml = MoveList(b, piece)

#print ml.get_move_list('c3')
#print ml.get_move_list('h6')

#b.set_piece([5,2], piece['empty'])
#b.set_piece([5,4], piece['empty'])
#b.set_piece([4,3], piece['black_king'])

#print ['d4-c3', 'd4-e3', 'd4-c5', 'd4-e5']
#print ml.get_move_list('d4')

b.set_piece(position_parser('d4'), piece['black'])
b.set_piece(position_parser('a7'), piece['empty'])
print_board(b.wooden_board)
print ml.get_capturing_move_list('e3')
