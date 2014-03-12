class CheckersBoard:
    
    # Warriors on the battlefield: our pieces
    white = 'w'
    black = 'b'

    wooden_board = []
    initial_white_positions = ['a1', 'c1', 'e1', 'g1', 'b2', 'd2', 'f2', 'h2', 'a3', 'c3', 'e3', 'g3']
    initial_black_positions = ['b6', 'd6', 'f6', 'h6', 'a7', 'c7', 'e7', 'g7', 'b8', 'd8', 'f8', 'h8']

    def __init__(self):
        # Initialize empty wooden board. Yes, we prefer you to play on wooden board! Classic look!! :-)
        # Representation of our board as a list of lists (2D array type). Still thinking of better a representation.
        self.wooden_board  = [[' ',' ',' ',' ',' ',' ',' ',' '],
                              [' ',' ',' ',' ',' ',' ',' ',' '],
                              [' ',' ',' ',' ',' ',' ',' ',' '],
                              [' ',' ',' ',' ',' ',' ',' ',' '],
                              [' ',' ',' ',' ',' ',' ',' ',' '],
                              [' ',' ',' ',' ',' ',' ',' ',' '],
                              [' ',' ',' ',' ',' ',' ',' ',' '],
                              [' ',' ',' ',' ',' ',' ',' ',' ']]

    def set_pieces_on_board_for_a_new_game(self):
        # We cannot play on an empty wooden board. Let's set the pieces on our board.
        # We use our initial positions list for arranging black and white pieces.
        self.set_pieces_on_board(self.initial_white_positions, self.white)
        self.set_pieces_on_board(self.initial_black_positions, self.black)
        
    def set_pieces_on_board(self, positions, piece):
        # Wrapper method. It takes a list of positions and piece to place on the positions and iterate through it
        for position in positions:
            self.set_piece(position, piece)

    def set_piece(self, position, piece):
        [row, column] = self.position_parser(position)
        self.wooden_board[row][column] = piece

    def get_piece(self, position):
        [row, column] = self.position_parser(position)
        return self.wooden_board[row][column]

    def position_parser(self, position):
        # You prefer a4, b7, e6, ... But being a computer, I prefer row and column.
        # Parser method for converting human readable position into row and column.
        # We convert ASCII characters to integer numbers from 0 to 7. 
        # In our wooden board, row starts from bottom. But in computer, row starts from top!
        column = ord(position[0]) - ord('a')
        row    = 7 - (ord(position[1]) - ord('1'))
        return [row, column]
