# -*- coding: utf-8 -*-
# Copyright 2015, Dario Blanco

import pytest
from click.testing import CliRunner

from capablanca.play import play
from capablanca.core import ChessPlayer


@pytest.fixture()
def runner():
    """Creates a CliRunner instance for any test that needs it"""
    return CliRunner()


@pytest.fixture(autouse=True)
def mock_chess_player(monkeypatch):
    """Mocks ChessPlayer methods, avoiding algorithm execution"""
    monkeypatch.setattr(ChessPlayer, 'run', lambda s: None)
    monkeypatch.setattr(ChessPlayer, 'draw_boards', lambda s: '')


def test_play_success(runner):
    """Should store console parameters when they are correct"""
    # Provide all the parameters correctly at once
    result = runner.invoke(play, input='6\n6\n1\n2\n4\n0\n1\n')
    assert not result.exception
    assert result.exit_code == 0
    assert result.output == (
        'Please enter board width: 6\n'
        'Please enter board height: 6\n'
        'Please enter number of Kings: 1\n'
        'Please enter number of Queens: 2\n'
        'Please enter number of Bishops: 4\n'
        'Please enter number of Rooks: 0\n'
        'Please enter number of Knights: 1\n'
        '\n'
    )


def test_play_width_string(runner):
    """Should show an error when width is a string"""
    # Provide an incorrect width string first time, and correct later
    result = runner.invoke(play, input='foo\n6\n6\n1\n2\n4\n0\n1\n')
    assert not result.exception
    assert result.exit_code == 0
    assert result.output == (
        'Please enter board width: foo\n'
        'Error: provided value is not a valid integer\n'
        'Please enter board width: 6\n'
        'Please enter board height: 6\n'
        'Please enter number of Kings: 1\n'
        'Please enter number of Queens: 2\n'
        'Please enter number of Bishops: 4\n'
        'Please enter number of Rooks: 0\n'
        'Please enter number of Knights: 1\n'
        '\n'
    )


def test_play_invalid_width_number(runner):
    """Should show an error when width is an out of bounds number"""
    # Provide an incorrect width number first time, and correct later
    result = runner.invoke(play, input='0\n6\n6\n1\n2\n4\n0\n1\n')
    assert not result.exception
    assert result.exit_code == 0
    assert result.output == (
        'Please enter board width: 0\n'
        'Error: dimension 0 should be greater than 0 and lesser than 8\n'
        'Please enter board width: 6\n'
        'Please enter board height: 6\n'
        'Please enter number of Kings: 1\n'
        'Please enter number of Queens: 2\n'
        'Please enter number of Bishops: 4\n'
        'Please enter number of Rooks: 0\n'
        'Please enter number of Knights: 1\n'
        '\n'
    )


def test_play_height_string(runner):
    """Should show an error when height is a string"""
    # Provide an incorrect height string first time, and correct later
    result = runner.invoke(play, input='6\nfoo\n6\n1\n2\n4\n0\n1\n')
    assert not result.exception
    assert result.exit_code == 0
    assert result.output == (
        'Please enter board width: 6\n'
        'Please enter board height: foo\n'
        'Error: provided value is not a valid integer\n'
        'Please enter board height: 6\n'
        'Please enter number of Kings: 1\n'
        'Please enter number of Queens: 2\n'
        'Please enter number of Bishops: 4\n'
        'Please enter number of Rooks: 0\n'
        'Please enter number of Knights: 1\n'
        '\n'
    )


def test_play_invalid_height_number(runner):
    """Should show an error when height is an out of bounds number"""
    # Provide an incorrect height number first time, and correct later
    result = runner.invoke(play, input='6\n0\n6\n1\n2\n4\n0\n1\n')
    assert not result.exception
    assert result.exit_code == 0
    assert result.output == (
        'Please enter board width: 6\n'
        'Please enter board height: 0\n'
        'Error: dimension 0 should be greater than 0 and lesser than 8\n'
        'Please enter board height: 6\n'
        'Please enter number of Kings: 1\n'
        'Please enter number of Queens: 2\n'
        'Please enter number of Bishops: 4\n'
        'Please enter number of Rooks: 0\n'
        'Please enter number of Knights: 1\n'
        '\n'
    )


def test_play_piece_number_string():
    """Should show an error when a piece number is a string"""
    runner = CliRunner()
    # Provide a piece number as string, and correct later
    result = runner.invoke(play, input='6\n6\nfoo\n1\n2\n4\n0\n1\n')
    assert not result.exception
    assert result.exit_code == 0
    assert result.output == (
        'Please enter board width: 6\n'
        'Please enter board height: 6\n'
        'Please enter number of Kings: foo\n'
        'Error: provided value is not a valid integer\n'
        'Please enter number of Kings: 1\n'
        'Please enter number of Queens: 2\n'
        'Please enter number of Bishops: 4\n'
        'Please enter number of Rooks: 0\n'
        'Please enter number of Knights: 1\n'
        '\n'
    )


def test_play_invalid_piece_number():
    """Should show an error when a piece number is out of bounds"""
    runner = CliRunner()
    # Provide an incorrect piece number first time, and correct later
    result = runner.invoke(play, input='6\n6\n1000\n1\n2\n4\n0\n1\n')
    assert not result.exception
    assert result.exit_code == 0
    assert result.output == (
        'Please enter board width: 6\n'
        'Please enter board height: 6\n'
        'Please enter number of Kings: 1000\n'
        'Error: piece number 1000 should be lesser or equals than 10\n'
        'Please enter number of Kings: 1\n'
        'Please enter number of Queens: 2\n'
        'Please enter number of Bishops: 4\n'
        'Please enter number of Rooks: 0\n'
        'Please enter number of Knights: 1\n'
        '\n'
    )
