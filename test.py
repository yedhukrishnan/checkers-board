# # TEMP file: for testing ONLY
#
# from checkers_board import *
# from printer import *
# from assets import *
# from helpers import *
# from movement import *
# from move_list import *
# from itertools import cycle
#
# # Print empty wooden board
# b = CheckersBoard(piece)
# # print_board(b.wooden_board)
#
# # Set and print initial board
# # b.set_pieces_on_board_for_a_new_game(initial_white_positions, initial_black_positions)
# b.set_piece([6, 1], 'b')
# b.set_piece([4, 1], 'w')
# # print_board(b.wooden_board)
#
# # Check if the board returns the correct piece
# # print b.get_piece([7, 0])
#
# m = Movement(b, piece)
#
# #  position parser shouldn't be a part of movement class. Movement class should deal with rows and columns only
# init_pos = position_parser('c3')
# fin_pos = position_parser('b4')
#
# # print_board(b.wooden_board)
#
# ml = MoveListGenerator(b, piece)
#
# def get_moves(piece_set):
#     move_list = []
#     for i in range(8):
#         for j in range(8):
#             if b.get_piece([i, j]) in piece_set:
#                 move_list.append(ml.get_capturing_move_list(readable_position([i, j])))
#                 move_list.append(ml.get_move_list(readable_position([i, j])))
#
#     move_list = [item for sublist in move_list for item in sublist]
#     capturing_move_list = [move for move in move_list if 'x' in move]
#     if capturing_move_list == []:
#         return move_list
#     return capturing_move_list
#
#
# player = cycle([piece_set_two, piece_set_one])
#
# while True:
#     current_piece = next(player)
#     print_board(b.wooden_board)
#     moves = get_moves(current_piece)
#     for (i, move) in enumerate(moves):
#         print i, move
#     selected_move = input('Select a move: ')
#     m.make_move(moves[selected_move])
#

from game import Game

game = Game()
game.start()