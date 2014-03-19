from helpers import *
from assets import *

class MoveList:
    
    def __init__(self, checkers_board, piece):
        self.checkers_board = checkers_board
        self.piece = piece

    def get_move_list(self, position):
        movable_neighbours = self.get_movable_neighbour_cells(position_parser(position))
        move_list = []
        for neighbour in movable_neighbours:
            if self.checkers_board.get_piece(neighbour) == piece['empty']:
                move = position + '-' + readable_position(neighbour)
                move_list.append(move)
        return move_list

    def get_movable_neighbour_cells(self, position):
        [row, column] = position
        piece = self.checkers_board.get_piece(position)
        self.neighbours = []

        self.add_neighbour([row + move_offset[piece], column - 1])
        self.add_neighbour([row + move_offset[piece], column + 1])
        
        return self.neighbours

    def is_valid(self, position):
        [row, column] = position
        return 0 <= row <= 7 and 0 <= column <= 7

    def add_neighbour(self, neighbour):
        if self.is_valid(neighbour):
            self.neighbours.append(neighbour)
        

