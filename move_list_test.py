import unittest
from assets import *
from checkers_board import *
from movement import *
from move_list import *
from helpers import *

class MoveListTest(unittest.TestCase):
    
    def setUp(self):
        self.checkers_board = CheckersBoard(piece)
        self.checkers_board.set_pieces_on_board_for_a_new_game(initial_white_positions, initial_black_positions)
        self.movement = Movement(self.checkers_board, piece)
        self.move_list = MoveListGenerator(self.checkers_board, piece)
        
    def test_shouldReturnNonCapturingMoveListForAWhitePieceOnBoard(self):
        expected_list_of_moves = ['c3-b4', 'c3-d4']
        list_of_moves = self.move_list.get_move_list('c3')
        self.assertSetEqual(set(expected_list_of_moves), set(list_of_moves))
    
    def test_shouldReturnNonCapturingMoveListForABlackPieceOnBoard(self):
        expected_list_of_moves = ['d6-e5', 'd6-c5']
        list_of_moves = self.move_list.get_move_list('d6')
        self.assertSetEqual(set(expected_list_of_moves), set(list_of_moves))

    def test_shouldReturnEmptyListForAPieceOnBoardIfNoMovesAvailable(self):
        expected_list_of_moves = []
        list_of_moves = self.move_list.get_move_list('c1')
        self.assertSetEqual(set(expected_list_of_moves), set(list_of_moves))

    def test_shouldReturnNonCapturingMoveListForAPieceOnEdgeOfBoard(self):
        expected_list_of_moves = ['a3-b4']
        list_of_moves = self.move_list.get_move_list('a3')
        self.assertSetEqual(set(expected_list_of_moves), set(list_of_moves))
 
    def test_shouldReturnNonCapturingMoveListForAKingPieceOnBoard(self):
        self.checkers_board.set_piece([5, 2], piece['empty'])
        self.checkers_board.set_piece([5, 4], piece['empty'])
        self.checkers_board.set_piece([4, 3], piece['black_king'])
        expected_list_of_moves = ['d4-c3', 'd4-e3', 'd4-c5', 'd4-e5']
        list_of_moves = self.move_list.get_move_list('d4')
        self.assertSetEqual(set(expected_list_of_moves), set(list_of_moves))

    def test_shouldReturnEmptyMoveListForAKingPieceOnBoard(self):
        self.checkers_board.set_piece([7, 4], piece['white_king'])
        expected_list_of_moves = []
        list_of_moves = self.move_list.get_move_list('e1')
        self.assertSetEqual(set(expected_list_of_moves), set(list_of_moves))
        
    def test_shouldReturnCapturingMoveListForANormalPieceOnBoard(self):
        self.checkers_board.set_piece([4, 5], piece['black'])
        expected_list_of_moves = ['g3xe5']
        list_of_moves = self.move_list.get_capturing_move_list('g3')
        self.assertSetEqual(set(expected_list_of_moves), set(list_of_moves))

    def test_shouldReturnCapturingMoveListWithMultipleCaptureForANormalPieceOnBoard(self):
        self.checkers_board.set_piece(position_parser('d4'), piece['black'])
        self.checkers_board.set_piece(position_parser('a7'), piece['empty'])
        expected_list_of_moves = ['e3xc5xa7']
        list_of_moves = self.move_list.get_capturing_move_list('e3')
        self.assertSetEqual(set(expected_list_of_moves), set(list_of_moves))
