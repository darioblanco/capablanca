# -*- coding: utf-8 -*-
# Copyright 2015, Dario Blanco

import pytest

from capablanca.play import play


@pytest.mark.testtype("integration")
def test_8queens_8x8(runner):
    """Should run a game with 8 queens in a 8x8 board"""
    result = runner.invoke(play, input='8\n8\n0\n8\n0\n0\n0\n')

    assert '92 solutions found' in result.output
