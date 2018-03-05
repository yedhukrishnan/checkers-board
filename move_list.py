from helpers import *
from assets import *
from checkers_board import CheckersBoard

class MoveListGenerator:

    def get_moves_for_player(self, board, piece_set):
        self.checkers_board = CheckersBoard(board)
        self.piece = self.checkers_board.piece

        # self.checkers_board.initialize_board(board)
        move_list = []
        positions = self.get_piece_positions_of_current_player(piece_set)
        for position in positions:
            move_list.append(self.get_capturing_move_list(readable_position(position)))
            move_list.append(self.get_move_list(readable_position(position)))

        move_list = [item for sublist in move_list for item in sublist]
        capturing_move_list = [move for move in move_list if 'x' in move]
        return capturing_move_list or move_list

    # Private Methods

    def get_move_list(self, position):
        movable_neighbours = self.get_movable_neighbour_cells(position_parser(position))
        move_list = []
        for neighbour in movable_neighbours:
            if self.checkers_board.get_piece(neighbour) == piece['empty']:
                move = position + '-' + readable_position(neighbour)
                move_list.append(move)
        return move_list

    def get_capturing_move_list(self, position):
        self.capture_move_list = []
        [row, column] = position_parser(position)
        piece = self.checkers_board.get_piece([row, column])
        self.get_captures(position, [row, column], piece)
        return self.capture_move_list

    def get_movable_neighbour_cells(self, position):
        [row, column] = position
        piece = self.checkers_board.get_piece(position)
        self.neighbours = []

        # Get neighbours by adding offset. King pieces have two offsets [1, -1]
        for offset in move_offset[piece]:
            self.add_neighbour([row + offset, column + 1])
            self.add_neighbour([row + offset, column - 1])

        return self.neighbours

    def add_neighbour(self, neighbour):
        if self.is_valid(neighbour):
            self.neighbours.append(neighbour)

    def is_valid(self, position):
        [row, column] = position
        return 0 <= row <= 7 and 0 <= column <= 7

    def get_captures(self, move, position, piece):
        [row, column] = position
        capture_neighbours = self.get_capture_neighbour_cells(position, piece)

        for neighbour in capture_neighbours:
            current_position = readable_position(neighbour)
            if current_position in move:
                self.capture_move_list.append(move)
            else:
                move += "x" + current_position
                self.get_captures(move, neighbour, piece)

        if capture_neighbours == []:
            if len(move) != 2:
                self.capture_move_list.append(move)

    def get_capture_neighbour_cells(self, position, piece):
        [row, column] = position
        self.capture_neighbours = []

        for offset in move_offset[piece]:
            self.add_capture_neighbour([row, column], [row + offset, column + 1], [row + 2 * offset, column + 2], piece)
            self.add_capture_neighbour([row, column], [row + offset, column - 1], [row + 2 * offset, column - 2], piece)

        return self.capture_neighbours

    # TODO: Refactoring
    def add_capture_neighbour(self, initial_position, opponent_position, final_position, piece):
        if self.is_valid(initial_position) and self.is_valid(opponent_position) and self.is_valid(final_position):
            opponent_piece = self.checkers_board.get_piece(opponent_position)
            if self.is_opponent(piece, opponent_piece):
                if self.checkers_board.get_piece(final_position) == self.piece['empty']:
                    self.capture_neighbours.append(final_position)

    def is_opponent(self, piece, opponent_piece):
        return (piece in piece_set_one and opponent_piece in piece_set_two) or (piece in piece_set_two and opponent_piece in piece_set_one)

    def get_piece_positions_of_current_player(self, piece_set):
        positions = []
        for i in range(8):
            for j in range(8):
                if self.checkers_board.get_piece([i, j]) in piece_set:
                    positions.append([i, j])
        return positions