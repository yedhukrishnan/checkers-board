import ast
import time

from checkers_board import CheckersBoard
from movement import Movement
from printer import print_board

# file_name = 'games/black_winning_games'
# winner = file_name.split('/')[-1].split('_')[0]

piece = {' ': 0, 'b': 1, 'B': 2, 'w': 3, 'W': 4}


def games_list(file_name):
    data = open(file_name, 'r').read()
    return ast.literal_eval(data)

def reduce_board(board_state):
    new_board_state = []
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 1:
                new_board_state.append(board_state[i][j])

    return new_board_state

def generate_data(game, winner):
    board = CheckersBoard()
    movement = Movement()
    board.set_pieces_on_board_for_a_new_game()
    game_states = ''

    for move in game[:-1]:
        board = movement.make_move(board, move)
        board_state = board.get_wooden_board()
        reduced_board_state = reduce_board(board_state)
        reduced_board_state = [piece[item] for item in reduced_board_state]
        game_states += ''.join(str(x) for x in reduced_board_state) + '\n'

    timestamp = str(int(time.time() * 1000000))
    file = open('games/' + winner + '/' + winner + timestamp, 'w+')
    file.write(game_states)
    file.close()


games = games_list('games/black_winning_games')
for game in games:
    generate_data(game, 'black')

games = games_list('games/white_winning_games')
for game in games:
    generate_data(game, 'white')
