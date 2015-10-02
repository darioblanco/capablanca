# -*- coding: utf-8 -*-
# Copyright 2015, Dario Blanco

from capablanca.core import ChessPlayer


def test_draw_boards():
    """Should pretty print the board with the expected format"""
    cp = ChessPlayer(2, 2, {'R': 2})
    assert cp.pieces == ['R', 'R']

    cp.run()
    cp.elapsed_time = 0.000379

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
    assert cp.draw_boards() == expected_output


def test_chess_player_3x3_solutions():
    """Should give four solutions when giving 2 Kings and 1 Rook for 3x3"""
    cp = ChessPlayer(3, 3, {'K': 2, 'Q': 0, 'B': 0, 'R': 1, 'N': 0})
    assert cp.pieces == ['R', 'K', 'K']

    cp.run()

    expected_solutions = set([
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
         '* * * * *\n')])
    assert cp.solutions == expected_solutions


def test_chess_player_4x4_solutions():
    """Should give eight solutions when giving 2 Rooks and 4 Knights for 4x4"""
    cp = ChessPlayer(4, 4, {'K': 0, 'Q': 0, 'B': 0, 'R': 2, 'N': 4})
    assert cp.pieces == ['R', 'R', 'N', 'N', 'N', 'N']

    cp.run()

    expected_solutions = set([
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
         '* * * * * *\n')])
    assert cp.solutions == expected_solutions
