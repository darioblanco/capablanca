# -*- coding: utf-8 -*-
# Copyright 2015, Dario Blanco

from capablanca.core import ChessPlayer


def test_draw_boards():
    """Should pretty print the board with the expected format"""
    cp = ChessPlayer(2, 2, {'R': 2})
    assert cp.pieces == ['R', 'R']

    cp.run()

    expected_output = (
        '\nFound 2 solutions:\n\n'
        '* * * *\n'
        '* R - *\n'
        '* - R *\n'
        '* * * *\n\n'
        '* * * *\n'
        '* - R *\n'
        '* R - *\n'
        '* * * *\n\n'
    )
    assert cp.draw_boards() == expected_output


def test_chess_player_3x3_solutions():
    """Should give four solutions when giving 2 kings and 1 Rook for 3x3"""
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
