class CheckersBoard:

    wooden_board = []

    def __init__(self, piece):
        self.wooden_board = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
        self.piece = piece
        self.promoted_piece = {
                'b': 'B',
                'B': 'B',
                'w': 'W',
                'W': 'W'
            }

    def set_pieces_on_board_for_a_new_game(self, initial_white_positions, initial_black_positions):
        self.set_pieces_on_board(initial_white_positions, self.piece['white'])
        self.set_pieces_on_board(initial_black_positions, self.piece['black'])

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
