class CheckersBoard:
    
    # Member variables
    board = []

    def __init__(self):
        # Representation of board as a list of lists (2D array type)
        self.board  = [[' ','b',' ','b',' ','b',' ','b'],
                       ['b',' ','b',' ','b',' ','b',' '],
                       [' ','b',' ','b',' ','b',' ','b'],
                       [' ',' ',' ',' ',' ',' ',' ',' '],
                       [' ',' ',' ',' ',' ',' ',' ',' '],
                       ['w',' ','w',' ','w',' ','w',' '],
                       [' ','w',' ','w',' ','w',' ','w'],
                       ['w',' ','w',' ','w',' ','w',' ']]

