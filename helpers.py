def position_parser(position):
    # You prefer a4, b7, e6, ... But being a computer, I prefer row and column.
    # Parser method for converting human readable position into row and column.
    # We convert ASCII characters to integer numbers from 0 to 7. 
    # In our wooden board, row starts from bottom. But in computer, row starts from top!
    column = ord(position[0]) - ord('a')
    row    = 7 - (ord(position[1]) - ord('1'))
    return [row, column]

