# Warriors in battlefield: our pieces
# Thinking of a better implementation

piece = {
    'black': 'b',
    'white': 'w',
    'black_king': 'B',
    'white_king': 'W',
    'empty': ' '
    }

# Initial positions list for black and white pieces.
# The commented lists shows human readable positions. But as a computer, I uses, rows and columns

# initial_white_positions = ['a1', 'c1', 'e1', 'g1', 'b2', 'd2', 'f2', 'h2', 'a3', 'c3', 'e3', 'g3']
initial_white_positions = [[7, 0], [7, 2], [7, 4], [7, 6], [6, 1], [6, 3], [6, 5], [6, 7], [5, 0], [5, 2], [5, 4], [5, 6]]

# initial_black_positions = ['b6', 'd6', 'f6', 'h6', 'a7', 'c7', 'e7', 'g7', 'b8', 'd8', 'f8', 'h8']
initial_black_positions = [[2, 1], [2, 3], [2, 5], [2, 7], [1, 0], [1, 2], [1, 4], [1, 6], [0, 1], [0, 3], [0, 5], [0, 7]]

# Offset position to add for pieces [especially to get neighbour cells]
move_offset = { piece['black']: [1], piece['white']: [-1], piece['black_king']: [1, -1], piece['white_king']: [-1, 1] }


piece_set_one = [piece['white'], piece['white_king']]
piece_set_two = [piece['black'], piece['black_king']]
