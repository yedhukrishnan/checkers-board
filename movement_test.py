import unittest
from checkers_board import *
from movement import *
from assets import *
from helpers import *

class MovementTest(unittest.TestCase):
    
    def setUp(self):
        self.checkers_board = CheckersBoard(piece)
        self.checkers_board.set_pieces_on_board_for_a_new_game(initial_white_positions, initial_black_positions)
        self.movement = Movement(self.checkers_board, piece)

    def test_shouldBeAbleToMakeARecursiveCapturingMoveOnTheWoodenBoard(self):
        self.checkers_board.set_piece(position_parser('g7'), piece['empty'])
        self.checkers_board.set_piece(position_parser('d4'), piece['black'])

        move = 'c3xe5xg7'
        self.movement.make_capture_move(move)

        for position in ['c3', 'd4', 'e5', 'f6']:
            self.assertEqual(self.checkers_board.get_piece(position_parser(position)), piece['empty'])
        self.assertEqual(self.checkers_board.get_piece(position_parser('g7')), piece['white'])

    def test_shouldBeAbleToMakeASingleNonCapturingMoveOnTheWoodenBoard(self):
        move = 'a3-b4'
        self.movement.make_non_capture_move(move)
        
        self.assertEqual(self.checkers_board.get_piece(position_parser('a3')), piece['empty'])
        self.assertEqual(self.checkers_board.get_piece(position_parser('b4')), piece['white'])


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
        
        self.movement.make_single_capture_move([5, 2], [3, 4])

        self.assertEqual(self.checkers_board.get_piece([5, 2]), piece['empty'])
        self.assertEqual(self.checkers_board.get_piece([4, 3]), piece['empty'])
        self.assertEqual(self.checkers_board.get_piece([3, 4]), piece['white'])
        
