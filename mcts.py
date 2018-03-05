from checkers_board import CheckersBoard
from move_list import MoveListGenerator
from movement import Movement
from assets import *
import random
from printer import *
import copy

IN_PROGRESS = 'progress'

piece_set = {
    'w': [piece['white'], piece['white_king']],
    'b': [piece['black'], piece['black_king']]
}

class Node():
    def __init__(self, parent = None):
        # self.board = board
        # self.turn = turn
        # self.move_list = move_list
        self.visits = 0
        self.reward = 0.0
        self.parent = parent
        self.children = []
        self.state = State()

    def set_state(self, board, turn):
        self.state.initialize(board, turn)

    def add_child(self, board):
        child_node = Node(self, board, self)
        self.children.append(child_node)

    def get_random_child(self):
        pass

    def get_child_with_maximum_score(self):
        scores = [child.state.reward for child in self.children]
        return children.index(max(scores))

class Tree():
    def __init__(self, root):
        self.node = root


class State():
    def __init__(self):
        # self.board = board
        # self.turn = turn
        self.visits = 0
        self.reward = 0.0
        self.movement = Movement()

    def initialize(self, board, turn):
        self.board = board
        self.turn = turn

    def get_all_possible_states(self):
        move_list_generator = MoveListGenerator()
        return move_list_generator.get_moves_for_player(self.board, piece_set[self.turn])

    def game_over(self):
        # Game is over if the player has no available moves
        return not self.get_all_possible_states()

    def random_play(self):
        available_moves = self.get_all_possible_states()
        choice = random.choice(range(len(available_moves)))
        self.board = self.movement.make_move(available_moves[choice])
        self.turn = self.next_turn()

    def next_turn(self):
        if self.turn == 'b':
            return 'w'
        return 'b'

    def get_status(self):
        if not self.get_all_possible_states():
            return self.next_turn()
        else:
            return IN_PROGRESS

    def update(self, reward):
        self.reward += reward
        self.visits += 1


def find_best_node_with_uct(node):
    print len(node.children)
    rewards = [child.state.reward for child in node.children]
    print rewards
    index = rewards.index(max(rewards))
    return node.children[index]

def select_promising_node(root_node):
    node = root_node
    while len(node.children) != 0:
        node = find_best_node_with_uct(node)
    return node

def expand_node(parent_node):
    available_next_states = parent_node.state.get_all_possible_states()
    for state in available_next_states:
        new_node = Node(parent_node)
        new_node.state.initialize(state, parent_node.state.next_turn())
        parent_node.children.append(new_node)


def simulate_random_playout(node_to_explore):
    # TODO: Status part has to be moved out for a generic MCTS algorithm
    # Now it is tied to Checkers
    opponent = 'b'

    temp_node = copy.deepcopy(node_to_explore)
    temp_state = temp_node.state

    status = temp_state.get_status()
    if status == opponent:
        temp_node.parent.state.reward = 0
        return status

    while status == IN_PROGRESS:
        # temp_state.toggle_turn()
        temp_state.random_play()
        status = temp_state.get_status()

    return status


def back_propagate(node_to_explore, result):
    WIN_SCORE = 1
    temp_node = node_to_explore.deepcopy()
    while temp_node:
        if temp_node.state.turn == result:
            temp_node.state.update(WIN_SCORE)
        temp_node = temp_node.parents


def find_next_move(board, turn):
    board = CheckersBoard(board)

    root_node = Node()
    root_node.set_state(board.wooden_board, turn)
    tree = Tree(root_node)

    # Tree search loop. Fixed for now
    for i in range(100):
        promising_node = select_promising_node(root_node)
        if not promising_node.state.game_over():
            expand_node(promising_node)

        node_to_explore = copy.deepcopy(promising_node)
        # node_to_explore = promising_node

        if promising_node.children > 0:
            node_to_explore = promising_node.get_random_child()

        result = simulate_random_playout(node_to_explore)
        back_propagate(node_to_explore, result)

    winner_node = root_node.get_child_with_maximum_score()
    tree.set_root(winner_node)

    return winner_node.state.board





board = CheckersBoard()
board.set_pieces_on_board_for_a_new_game()
movement = Movement()
move_list_generator = MoveListGenerator()

available_moves = move_list_generator.get_moves_for_player(board.wooden_board, piece_set['b'])
choice = random.choice(range(len(available_moves)))
print_board(board.wooden_board)
print available_moves
print choice
board = movement.make_move(board, available_moves[choice])

print_board(board.wooden_board)

find_next_move(board.wooden_board, 'w')
