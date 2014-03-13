# Movement class. Takes care of validation of all the movements (Beware! No cheating!! :-))

class Movement:
    
    def __init__(self, board, piece):
        self.board = board
        self.piece = piece

    def make_simple_move(self, initial_position, final_position):
        # Represents a non-capturing move.
        # Simply makes a movement from initial position to final position
        # leaving the initial position empty.
        current_piece = self.board.get_piece(initial_position)
        self.board.set_piece(piece['empty'])
        self.board.set_piece(final_position, current_piece)

    def make_capture_move(self, initial_position, final_position):
        # Make a capturing move from initial position to final position.
        # This is a single capturing move, to capture one opponent piece.
        self.make_simple_move(initial_position, final_position)
        opponent_position = get_opponent_position(initial_position, final_position)
        self.board.set_piece(opponent_position)
        
    def get_opponent_position(initial_position, final_position):
        # Find the opponent position (row and column) between initial and final position. 
        [initial_row, initial_column] = position_parser(initial_position)
        [final_row, final_column] = position_parser(final_position)
        opponent_row = (initial_row + final_row) / 2
        opponent_column = (initial_column + final_column) / 2
        return [opponent_row, opponent_column]
