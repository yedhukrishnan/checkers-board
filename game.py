from checkers_board import CheckersBoard
from move_list import MoveListGenerator
from movement import Movement
from helpers import *
from assets import *
from itertools import cycle
from printer import *
import random


class Game():
    def __init__(self):
        self.board = CheckersBoard(piece)
        self.board.set_pieces_on_board_for_a_new_game()
        self.movement = Movement(self.board, piece)
        self.move_list_generator = MoveListGenerator(self.board, piece)
        self.players = cycle([piece_set_two, piece_set_one])

    def start(self):
        return self.begin_game_loop()

    def start_random(self):
        return self.begin_game_loop(True)

    def begin_game_loop(self, is_random = False):
        game_moves = []
        while True:
            current_piece_set = next(self.players)
            print_board(self.board.wooden_board)
            moves = self.move_list_generator.get_moves_for_current_player(current_piece_set)
            if moves:
                selected_move = self.select_move(moves, is_random)
                self.movement.make_move(moves[selected_move])
                game_moves.append(moves[selected_move])
            else:
                winner = next(self.players)
                print winner[0] + " wins"
                break
        return game_moves

    def select_move(self, moves, is_random):
        if is_random:
            choice = random.choice(range(len(moves)))
        else:
            self.print_available_moves(moves)
            choice = input('Select a move: ')
        return choice

    def print_available_moves(moves):
        for (index, move) in enumerate(moves):
            print index, move

