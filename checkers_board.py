class CheckersBoard:
    
    wooden_board = []

    def __init__(self, piece):
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
        self.piece = piece

    def set_pieces_on_board_for_a_new_game(self, initial_white_positions, initial_black_positions):
        # We cannot play on an empty wooden board. Let's set the pieces on our board.
        # We use the initial positions list for arranging black and white pieces.
        self.set_pieces_on_board(initial_white_positions, self.piece['white'])
        self.set_pieces_on_board(initial_black_positions, self.piece['black'])
        
    def set_pieces_on_board(self, positions, piece):
        # Wrapper method. It takes a list of positions and piece to place on the positions and iterate through it
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
        return 0 <= value <= 8
