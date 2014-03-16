import unittest
from checkers_board import *
from movement import *
from assets import *

class MovementTest(unittest.TestCase):
    
    def setUp(self):
        self.checkers_board = CheckersBoard(piece)
        self.checkers_board.set_pieces_on_board_for_a_new_game(initial_white_positions, initial_black_positions)
        self.movement = Movement(self.checkers_board, piece)
        
    def test_shouldBeAbleToMakeASimpleMove(self):
        self.assertEqual(self.checkers_board.get_piece([5, 2]), piece['white'])
        self.assertEqual(self.checkers_board.get_piece([4, 3]), piece['empty'])
        
        self.movement.make_simple_move([5, 2], [4, 3])

        self.assertEqual(self.checkers_board.get_piece([5, 2]), piece['empty'])
        self.assertEqual(self.checkers_board.get_piece([4, 3]), piece['white'])

    def test_shouldBeAbleToMakeACapturingMove(self):
        self.checkers_board.set_piece([4, 3], piece['black'])
        
        self.assertEqual(self.checkers_board.get_piece([5, 2]), piece['white'])
        self.assertEqual(self.checkers_board.get_piece([3, 4]), piece['empty'])
        
        self.movement.make_capture_move([5, 2], [3, 4])

        self.assertEqual(self.checkers_board.get_piece([5, 2]), piece['empty'])
        self.assertEqual(self.checkers_board.get_piece([4, 3]), piece['empty'])
        self.assertEqual(self.checkers_board.get_piece([3, 4]), piece['white'])
        
