class CheckersBoard:

    wooden_board = []

    def __init__(self, board = None):
        self.wooden_board = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
        self.piece = {
            'black': 'b',
            'white': 'w',
            'black_king': 'B',
            'white_king': 'W',
            'empty': ' '
        }
        self.promoted_piece = {
                'b': 'B',
                'B': 'B',
                'w': 'W',
                'W': 'W'
            }

        if board:
            self.wooden_board = board

        # initial_white_positions = [ 'a1', 'c1', 'e1', 'g1', 'b2', 'd2',
        #                             'f2', 'h2', 'a3', 'c3', 'e3', 'g3' ]
        self.initial_white_positions = [[7, 0], [7, 2], [7, 4], [7, 6], [6, 1],
                                        [6, 3], [6, 5], [6, 7], [5, 0], [5, 2],
                                        [5, 4], [5, 6]]

        # initial_black_positions = [ 'b6', 'd6', 'f6', 'h6', 'a7', 'c7',
        #                             'e7', 'g7', 'b8', 'd8', 'f8', 'h8' ]
        self.initial_black_positions = [[2, 1], [2, 3], [2, 5], [2, 7], [1, 0],
                                        [1, 2], [1, 4], [1, 6], [0, 1], [0, 3],
                                        [0, 5], [0, 7]]

    def set_pieces_on_board_for_a_new_game(self):
        self.set_pieces_on_board(self.initial_white_positions, self.piece['white'])
        self.set_pieces_on_board(self.initial_black_positions, self.piece['black'])

    def set_pieces_on_board(self, positions, piece):
        for position in positions:
            self.set_piece(position, piece)

    def set_piece(self, position, piece):
        [row, column] = position
        self.wooden_board[row][column] = piece

    def get_piece(self, position):
        [row, column] = position
        return self.wooden_board[row][column]

    def get_wooden_board(self):
        return self.wooden_board
        # return 0 <= value <= 8

    def promote(self, position):
        (row, column) = position
        piece = self.wooden_board[row][column]
        self.wooden_board[row][column] = self.promoted_piece[piece]
