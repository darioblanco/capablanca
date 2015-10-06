# -*- coding: utf-8 -*-
# Copyright 2015, Dario Blanco

"""
This module tests capablanca.core
"""

from capablanca.core import ChessPlayer


def test_piece_list():
    """Should create a proper piece list from the input"""
    chess_player = ChessPlayer(8, 8, {'K': 2, 'Q': 2, 'B': 2, 'R': 1, 'N': 1})
    assert chess_player.pieces == ['Q', 'Q', 'R', 'B', 'B', 'K', 'K', 'N']

    chess_player = ChessPlayer(2, 2, {'K': 0, 'Q': 0, 'B': 0, 'R': 0, 'N': 0})
    assert chess_player.pieces == []


def test_draw_boards():
    """Should pretty print the board with the expected format"""
    chess_player = ChessPlayer(2, 2, {'K': 0, 'Q': 0, 'B': 0, 'R': 2, 'N': 0})

    chess_player.run()
    chess_player.elapsed_time = 0.000379

    expected_output = (
        '\nSolutions:\n\n'
        '* * * *\n'
        '* R - *\n'
        '* - R *\n'
        '* * * *\n\n'
        '* * * *\n'
        '* - R *\n'
        '* R - *\n'
        '* * * *\n\n'
        '2 solutions found in 0.000379 seconds\n'
    )
    assert chess_player.draw_boards() == expected_output


def test_chess_player_1x3_solutions():
    """Should give 1 solution when giving 2 Kings and 1x3"""
    chess_player = ChessPlayer(1, 3, {'K': 2, 'Q': 0, 'B': 0, 'R': 0, 'N': 0})

    chess_player.run()
    chess_player.draw_boards()

    expected_solutions = [
        ('* * * * *\n'
         '* K - K *\n'
         '* * * * *\n')]
    assert chess_player.solutions == expected_solutions


def test_chess_player_3x3_solutions():
    """Should give four solutions when giving 2 Kings and 1 Rook for 3x3"""
    chess_player = ChessPlayer(3, 3, {'K': 2, 'Q': 0, 'B': 0, 'R': 1, 'N': 0})

    chess_player.run()
    chess_player.draw_boards()

    expected_solutions = [
        ('* * * * *\n'
         '* K - - *\n'
         '* - - R *\n'
         '* K - - *\n'
         '* * * * *\n'),
        ('* * * * *\n'
         '* K - K *\n'
         '* - - - *\n'
         '* - R - *\n'
         '* * * * *\n'),
        ('* * * * *\n'
         '* - R - *\n'
         '* - - - *\n'
         '* K - K *\n'
         '* * * * *\n'),
        ('* * * * *\n'
         '* - - K *\n'
         '* R - - *\n'
         '* - - K *\n'
         '* * * * *\n')]
    assert len(chess_player.solutions) == len(expected_solutions)
    for expected_solution in expected_solutions:
        assert expected_solution in chess_player.solutions


def test_chess_player_4x4_solutions():
    """Should give eight solutions when giving 2 Rooks and 4 Knights for 4x4"""
    chess_player = ChessPlayer(4, 4, {'K': 0, 'Q': 0, 'B': 0, 'R': 2, 'N': 4})

    chess_player.run()
    chess_player.draw_boards()

    expected_solutions = [
        ('* * * * * *\n'
         '* R - - - *\n'
         '* - N - N *\n'
         '* - - R - *\n'
         '* - N - N *\n'
         '* * * * * *\n'),
        ('* * * * * *\n'
         '* N - N - *\n'
         '* - R - - *\n'
         '* N - N - *\n'
         '* - - - R *\n'
         '* * * * * *\n'),
        ('* * * * * *\n'
         '* - - - R *\n'
         '* N - N - *\n'
         '* - R - - *\n'
         '* N - N - *\n'
         '* * * * * *\n'),
        ('* * * * * *\n'
         '* - R - - *\n'
         '* N - N - *\n'
         '* - - - R *\n'
         '* N - N - *\n'
         '* * * * * *\n'),
        ('* * * * * *\n'
         '* - N - N *\n'
         '* - - R - *\n'
         '* - N - N *\n'
         '* R - - - *\n'
         '* * * * * *\n'),
        ('* * * * * *\n'
         '* N - N - *\n'
         '* - - - R *\n'
         '* N - N - *\n'
         '* - R - - *\n'
         '* * * * * *\n'),
        ('* * * * * *\n'
         '* - N - N *\n'
         '* R - - - *\n'
         '* - N - N *\n'
         '* - - R - *\n'
         '* * * * * *\n'),
        ('* * * * * *\n'
         '* - - R - *\n'
         '* - N - N *\n'
         '* R - - - *\n'
         '* - N - N *\n'
         '* * * * * *\n')]
    assert len(chess_player.solutions) == len(expected_solutions)
    for expected_solution in expected_solutions:
        assert expected_solution in chess_player.solutions


def test_chess_player_4_queens():
    """Should solve the 4 queens problem with a 4x4 board"""
    chess_player = ChessPlayer(4, 4, {'K': 0, 'Q': 4, 'B': 0, 'R': 0, 'N': 0})

    chess_player.run()
    chess_player.draw_boards()

    expected_solutions = [
        ('* * * * * *\n'
         '* - Q - - *\n'
         '* - - - Q *\n'
         '* Q - - - *\n'
         '* - - Q - *\n'
         '* * * * * *\n'),
        ('* * * * * *\n'
         '* - - Q - *\n'
         '* Q - - - *\n'
         '* - - - Q *\n'
         '* - Q - - *\n'
         '* * * * * *\n')]
    assert len(chess_player.solutions) == len(expected_solutions)
    for expected_solution in expected_solutions:
        assert expected_solution in chess_player.solutions


def test_chess_player_6_queens():
    """Should solve the 6 queens problem with a 6x6 board"""
    chess_player = ChessPlayer(6, 6, {'K': 0, 'Q': 6, 'B': 0, 'R': 0, 'N': 0})

    chess_player.run()
    chess_player.draw_boards()

    expected_solutions = [
        ('* * * * * * * *\n'
         '* - Q - - - - *\n'
         '* - - - Q - - *\n'
         '* - - - - - Q *\n'
         '* Q - - - - - *\n'
         '* - - Q - - - *\n'
         '* - - - - Q - *\n'
         '* * * * * * * *\n'),
        ('* * * * * * * *\n'
         '* - - Q - - - *\n'
         '* - - - - - Q *\n'
         '* - Q - - - - *\n'
         '* - - - - Q - *\n'
         '* Q - - - - - *\n'
         '* - - - Q - - *\n'
         '* * * * * * * *\n'),
        ('* * * * * * * *\n'
         '* - - - Q - - *\n'
         '* Q - - - - - *\n'
         '* - - - - Q - *\n'
         '* - Q - - - - *\n'
         '* - - - - - Q *\n'
         '* - - Q - - - *\n'
         '* * * * * * * *\n'),
        ('* * * * * * * *\n'
         '* - - - - Q - *\n'
         '* - - Q - - - *\n'
         '* Q - - - - - *\n'
         '* - - - - - Q *\n'
         '* - - - Q - - *\n'
         '* - Q - - - - *\n'
         '* * * * * * * *\n')]
    assert len(chess_player.solutions) == len(expected_solutions)
    for expected_solution in expected_solutions:
        assert expected_solution in chess_player.solutions
