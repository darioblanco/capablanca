# -*- coding: utf-8 -*-
# Copyright 2015, Dario Blanco

from capablanca.core import ChessPlayer


def test_chess_player_3x3():
    cp = ChessPlayer(3, 3, {'K': 2, 'Q': 0, 'B': 0, 'R': 1, 'N': 0})
    cp.run()

    assert cp.pieces == ['R', 'K', 'K']
    assert cp.draw_boards() == ''


def test_chess_player_4x4():
    cp = ChessPlayer(4, 4, {'K': 0, 'Q': 0, 'B': 0, 'R': 2, 'N': 4})
    cp.run()

    assert cp.pieces == ['R', 'R', 'N', 'N', 'N', 'N']
    assert cp.draw_boards() == ''


def test_chess_player_7x7():
    cp = ChessPlayer(7, 7, {'K': 2, 'Q': 2, 'B': 2, 'R': 0, 'N': 1})
    cp.run()

    assert cp.pieces == ['Q', 'Q', 'K', 'K', 'B', 'B', 'N']
    assert cp.draw_boards() == ''
