class CheckersBoard:

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

    # Print the board on terminal
    def print_board(self):
        def print_line():
            print '  ---------------------------------'

        column_list = '    a   b   c   d   e   f   g   h'
        row_num = 8
        for row in self.board:
            print_line()
            print row_num,
            for col in row:
                print '|', col,
            print '|'
            row_num = row_num - 1
        print_line()
        print column_list

# class CheckersBoard ends

checkers_board = CheckersBoard()
checkers_board.print_board()
