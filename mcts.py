from checkers_board import CheckersBoard
from move_list import MoveListGenerator
from movement import Movement
from assets import *

piece_set = {
    'w': [piece['white'], piece['white_king']],
    'b': [piece['black'], piece['black_king']]
}

class Node():
    def __init__(self, board, turn, move_list,  parent = None):
        self.board = board
        self.visits = 0
        self.reward = 0.0
        self.turn = turn
        self.parent = parent
        self.children = []
        self.move_list = move_list

    def add_child(self, board):
        child_node = Node(self, board, self)
        self.children.append(child_node)

    def update(self, reward):
        self.reward += reward
        self.visits += 1

    def next_turn(self):
        if self.turn == 'b':
            return 'w'
        return 'b'

class Tree():
    def __init__(self, root):
        self.node = root

class State():
    def __init__(self, board, turn):
        self.board = board
        self.turn = turn
        self.visits = 0
        self.reward = 0.0

    def get_all_possible_states(self):
        # return list of all states from current state
        return

    def random_play(self):
        return




board = CheckersBoard(piece)
board.set_pieces_on_board_for_a_new_game(initial_white_positions, initial_black_positions)
movement = Movement(board, piece)
move_list_generator = MoveListGenerator(board, piece)

node = Node(board.wooden_board, 'b', move_list_generator.get_moves_for_player())