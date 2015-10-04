# -*- coding: utf-8 -*-
# Copyright 2015, Dario Blanco

import pytest

from capablanca.play import play


@pytest.mark.testtype("integration")
def test_8queens_8x8(runner):
    """Should run a game with 8 queens in a 8x8 board"""
    result = runner.invoke(play, input='8\n8\n0\n8\n0\n0\n0\n')

    assert '92 solutions found' in result.output


@pytest.mark.testtype("integration")
def test_2k_2q_2b_1n_7x7(runner):
    """
    Should run a game with 2 Kings, 2 Queens, 2 Bishop and 1 Knight
    in a 7x7 board
    """
    result = runner.invoke(play, input='7\n7\n2\n2\n2\n0\n1\n')

    assert '3063828 solutions found' in result.output
