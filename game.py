from checkers_board import CheckersBoard
from move_list import MoveListGenerator
from movement import Movement
from helpers import *
from assets import *
from itertools import cycle
from printer import *


class Game():
    def __init__(self):
        self.board = CheckersBoard(piece)
        # self.board.set_pieces_on_board_for_a_new_game(initial_white_positions, initial_black_positions)
        self.custom_position()
        self.movement = Movement(self.board, piece)
        self.move_list_generator = MoveListGenerator(self.board, piece)
        self.players = cycle([piece_set_two, piece_set_one])

    def start(self):
        while True:
            current_piece_set = next(self.players)
            print_board(self.board.wooden_board)
            moves = self.get_moves_for_current_player(current_piece_set)
            for (index, move) in enumerate(moves):
                print index, move
            selected_move = input('Select a move: ')
            self.movement.make_move(moves[selected_move])

    def get_moves_for_current_player(self, piece_set):
        move_list = []
        for i in range(8):
            for j in range(8):
                if self.board.get_piece([i, j]) in piece_set:
                    move_list.append(self.move_list_generator.get_capturing_move_list(readable_position([i, j])))
                    move_list.append(self.move_list_generator.get_move_list(readable_position([i, j])))

        move_list = [item for sublist in move_list for item in sublist]
        capturing_move_list = [move for move in move_list if 'x' in move]
        if not capturing_move_list:
            return move_list
        return capturing_move_list

    # def custom_position(self):
    #     self.board.set_piece([4, 5], 'b')
    #     self.board.set_piece([6, 7], 'b')
    #     self.board.set_piece([3, 4], 'W')
    #     self.board.set_piece([2, 3], 'b')

