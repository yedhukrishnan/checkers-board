# Temporary method for displaying wooden board on screen
# Refactoring pending

# Print the board on terminal
def print_board(wooden_board):
    def print_line():
        print '  ---------------------------------'

    column_list = '    a   b   c   d   e   f   g   h'
    row_num = 8
    for row in wooden_board:
        print_line()
        print row_num,
        for col in row:
            print '|', col,
        print '|'
        row_num = row_num - 1
    print_line()
    print column_list
