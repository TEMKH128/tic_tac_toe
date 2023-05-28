import sys
import unittest
from io import StringIO
import tic_tac_toe as tactoe
from unittest.mock import patch


class TestTicTacToe(unittest.TestCase):
    sys.stdout = StringIO()

    def test_board_creation(self):
        board = tactoe.create_board()

        expected_board = [
            [1, 2, 3], 
            [4, 5, 6],
            [7, 8, 9],
        ]

        self.assertEqual(expected_board, board)

    def test_board_display_one(self):
        board = [
            [1, 2, 3], 
            [4, 5, 6],
            [7, 8, 9],
        ]

        display = tactoe.board_display(board)

        expected_display = """
\t\t\t1   2   3
\t\t\t4   5   6
\t\t\t7   8   9
"""

        self.assertEqual(expected_display, display)

    def test_board_display_two(self):
        board = [
            ['X', 'O', 3], 
            [4, 'X', 6],
            [7, 8, 'O'],
        ]

        display = tactoe.board_display(board)

        expected_display = """
\t\t\tX   O   3
\t\t\t4   X   6
\t\t\t7   8   O
"""

        self.assertEqual(expected_display, display)

    @patch("sys.stdin", StringIO("1a\n\n10\-1\n3\n"))
    def test_prompt_user_one(self):
        board = [
            ['X', 'O', 3], 
            [4, 'X', 6],
            [7, 8, 'O'],
        ]

        number = tactoe.prompt_user(board, 'X')
        self.assertEqual(3, number)

    @patch("sys.stdin", StringIO("4\n9\n8\n"))
    def test_prompt_user_two(self):
        board = [
            ['X', 'O', 3], 
            ['O', 'X', 6],
            [7, 8, 'O'],
        ]

        number = tactoe.prompt_user(board, 'O')
        self.assertEqual(8, number)

    @patch("sys.stdin", StringIO("4\n9\nQuIt\n\n"))
    def test_prompt_user_quit(self):
        board = [
            ['X', 'O', 3], 
            ['O', 'X', 6],
            [7, 8, 'O'],
        ]

        number = tactoe.prompt_user(board, 'O')
        self.assertEqual(0, number)

    def test_update_board_one(self):
        board = [
            ['X', 'O', 3], 
            ['O', 'X', 6],
            [7, 8, 'O'],
        ]

        new_board = tactoe.update_board(board, 'X', 3)

        expected_board = [
            ['X', 'O', 'X'], 
            ['O', 'X', 6],
            [7, 8, 'O'],
        ]

        self.assertEqual(expected_board, new_board)

    def test_update_board_two(self):
        board = [
            ['X', 'O', 3], 
            [4, 'X', 6],
            [7, 8, 'O'],
        ]

        new_board = tactoe.update_board(board, 'O', 7)

        expected_board = [
            ['X', 'O', 3], 
            [4, 'X', 6],
            ['O', 8, 'O'],
        ]

        self.assertEqual(expected_board, new_board)

    def test_evaluate_draw(self):
        board = [
            ['X', 'O', 'X'], 
            ['O', 'X', 'X'],
            ['O', 'X', 'O'],
        ]

        result = tactoe.evaluate_board(board)
        self.assertEqual("draw", result)

    def test_evaluate_continue(self):
        board = [
            ['X', 'O', 3], 
            ['O', 'X', 6],
            ['X', 8, 'O'],
        ]

        result = tactoe.evaluate_board(board)
        self.assertEqual("continue", result)

    def test_evaluate_win_one(self):
        board = [
            ['O', 'O', 'X'], 
            ['O', 'X', 6],
            ['O', 8, 'X'],
        ]

        result = tactoe.evaluate_board(board)
        self.assertEqual("win", result)

    def test_evaluate_win_two(self):
        board = [
            [1, 'X', 'O'], 
            ['O', 'X', 6],
            ['O', 'X', 9],
        ]

        result = tactoe.evaluate_board(board)
        self.assertEqual("win", result)

    def test_evaluate_win_three(self):
        board = [
            [1, 'X', 'O'], 
            ['X', 5, 'O'],
            [7, 'X', 'O'],
        ]

        result = tactoe.evaluate_board(board)
        self.assertEqual("win", result)

    def test_evaluate_win_four(self):
        board = [
            ['X', 'X', 'X'], 
            ['O', 5, 'O'],
            [7, 8, 'O'],
        ]

        result = tactoe.evaluate_board(board)
        self.assertEqual("win", result)

    def test_evaluate_win_five(self):
        board = [
            ['X', 2, 'X'], 
            ['O', 'O', 'O'],
            [7, 8, 'X'],
        ]

        result = tactoe.evaluate_board(board)
        self.assertEqual("win", result)

    def test_evaluate_win_six(self):
        board = [
            ['O', 2, 3], 
            [4, 'O', 'O'],
            ['X', 'X', 'X'],
        ]

        result = tactoe.evaluate_board(board)
        self.assertEqual("win", result)

    def test_evaluate_win_seven(self):
        board = [
            ['O', 2, 'X'], 
            [4, 'X', 6],
            ['X', 'O', 'O'],
        ]

        result = tactoe.evaluate_board(board)
        self.assertEqual("win", result)

    def test_evaluate_win_eight(self):
        board = [
            ['O', 2, 'X'], 
            [4, 'O', 6],
            ['X', 'X', 'O'],
        ]

        result = tactoe.evaluate_board(board)
        self.assertEqual("win", result)

    def test_swap_turn_x(self):
        turn = 'X'
        turn = tactoe.swap_turn(turn)
        self.assertEqual('O', turn)

    def test_swap_turn_o(self):
        turn = 'O'
        turn = tactoe.swap_turn(turn)
        self.assertEqual('X', turn)


if __name__ == "__main__":
    unittest.main()
