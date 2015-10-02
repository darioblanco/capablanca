# -*- coding: utf-8 -*-
# Copyright 2015, Dario Blanco

import pytest
from click import BadParameter

from capablanca.custom_types import BoardDimension, PieceNumber


@pytest.fixture()
def board_dimension():
    """Creates a new piece number instance for each test that calls it"""
    return BoardDimension()


@pytest.fixture()
def piece_number():
    """Creates a new piece number instance for each test that calls it"""
    return PieceNumber()


def test_board_dimension_success(board_dimension):
    """Should convert a console board dimension parameter to int"""
    assert board_dimension.convert('3', None, None) == 3


def test_board_dimension_not_integer(board_dimension):
    """Should track an error when the board dimension is not an int"""
    with pytest.raises(BadParameter) as excinfo:
        board_dimension.convert('foo', None, None)
    exc_msg = excinfo.exconly(tryshort=True)
    assert exc_msg == 'BadParameter: provided value is not a valid integer'


def test_board_dimension_out_of_bounds(board_dimension):
    """Should track an error when the board dimension is out of bounds"""
    with pytest.raises(BadParameter) as excinfo:
        board_dimension.convert('100', None, None)
    exc_msg = excinfo.exconly(tryshort=True)
    assert exc_msg == ('BadParameter: dimension 100 should be greater than 0 '
                       'and lesser than 100')


def test_piece_number_success(piece_number):
    """Should convert a console piece number parameter to int"""
    assert piece_number.convert('5', None, None) == 5


def test_piece_number_not_integer(piece_number):
    """Should track an error when the piece number is not an int"""
    with pytest.raises(BadParameter) as excinfo:
        piece_number.convert('foo', None, None)
    exc_msg = excinfo.exconly(tryshort=True)
    assert exc_msg == 'BadParameter: provided value is not a valid integer'


def test_piece_number_out_of_bounds(piece_number):
    """Should track an error when the piece number is out of bounds"""
    with pytest.raises(BadParameter) as excinfo:
        piece_number.convert('1000', None, None)
    exc_msg = excinfo.exconly(tryshort=True)
    assert exc_msg == ('BadParameter: piece number 1000 should be '
                       'lesser than 1000')
