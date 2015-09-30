# -*- coding: utf-8 -*-
# Copyright 2015, Dario Blanco

from capablanca.core import ChessPlayer


def test_chess_player_3x3():
    cp = ChessPlayer(3, 3, {'K': 2, 'Q': 0, 'B': 0, 'R': 1, 'N': 0})
    cp.run()

    assert cp.draw_boards() == ''
