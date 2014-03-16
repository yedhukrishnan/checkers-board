import unittest
from checkers_board import *
from assets import *

class CheckersBoardTest(unittest.TestCase):

    def setUp(self):
        self.checkers_board = CheckersBoard(piece)

    def test_shouldArrangeTheBoardForNewGame(self):
        initial_wooden_board  = [[' ','b',' ','b',' ','b',' ','b'],
                                 ['b',' ','b',' ','b',' ','b',' '],
                                 [' ','b',' ','b',' ','b',' ','b'],
                                 [' ',' ',' ',' ',' ',' ',' ',' '],
                                 [' ',' ',' ',' ',' ',' ',' ',' '],
                                 ['w',' ','w',' ','w',' ','w',' '],
                                 [' ','w',' ','w',' ','w',' ','w'],
                                 ['w',' ','w',' ','w',' ','w',' ']]
        self.checkers_board.set_pieces_on_board_for_a_new_game(initial_white_positions, initial_black_positions)
        self.assertEqual(self.checkers_board.get_wooden_board(), initial_wooden_board)

    def test_shouldSetAndGetPiecesOnTheBoard(self):
        self.assertEqual(self.checkers_board.get_piece([0, 0]), ' ')
        
        self.checkers_board.set_piece([0, 0], piece['black'])
        self.assertEqual(self.checkers_board.get_piece([0, 0]), piece['black'])
        
        self.checkers_board.set_piece([7, 1], piece['white'])
        self.assertEqual(self.checkers_board.get_piece([7, 1]), piece['white'])
        
        
