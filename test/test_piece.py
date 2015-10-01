# -*- coding: utf-8 -*-
# Copyright 2015, Dario Blanco

from capablanca import piece


def test_king_positions():
    """Should return proper threat positions when moving a King"""
    k = piece.King(3, 3)

    pos = k.threatened_positions((1, 1))
    assert pos == set([
        (0, 0), (1, 0), (2, 0), (0, 1), (2, 1), (0, 2), (1, 2), (2, 2)
    ])

    pos = k.threatened_positions((0, 0))
    assert pos == set([(1, 0), (0, 1), (1, 1)])

    pos = k.threatened_positions((2, 2))
    assert pos == set([(1, 1), (2, 1), (1, 2)])


def test_bishop_positions():
    """Should return proper threat positions when moving a Bishop"""
    b = piece.Bishop(3, 4)

    pos = b.threatened_positions((1, 2))
    assert pos == set([(2, 3), (2, 1), (0, 3), (0, 1)])

    pos = b.threatened_positions((0, 0))
    assert pos == set([(1, 1), (2, 2)])

    pos = b.threatened_positions((2, 3))
    assert pos == set([(1, 2), (0, 1)])


def test_rook_positions():
    """Should return proper threat positions when moving a Rook"""
    b = piece.Rook(3, 4)

    pos = b.threatened_positions((1, 1))
    assert pos == set([(0, 1), (1, 0), (1, 2), (1, 3), (2, 1)])

    pos = b.threatened_positions((0, 0))
    assert pos == set([(0, 1), (0, 2), (0, 3), (1, 0), (2, 0)])

    pos = b.threatened_positions((2, 3))
    assert pos == set([(0, 3), (1, 3), (2, 0), (2, 1), (2, 2)])


def test_queen_positions():
    """Should return proper threat positions when moving a Queen"""
    q = piece.Queen(6, 6)

    pos = q.threatened_positions((3, 3))
    assert pos == set([
        (4, 4), (5, 5), (4, 2), (5, 1), (2, 4), (1, 5), (2, 2), (1, 1), (0, 0),
        (3, 0), (3, 1), (3, 2), (3, 4), (3, 5), (0, 3), (1, 3), (2, 3), (4, 3),
        (5, 3)
    ])

    pos = q.threatened_positions((0, 0))
    assert pos == set([
        (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (0, 1), (0, 2), (0, 3), (0, 4),
        (0, 5), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0)
    ])

    pos = q.threatened_positions((6, 6))
    assert pos == set([
        (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (0, 6), (1, 6), (2, 6),
        (3, 6), (4, 6), (5, 6)
    ])


def test_knight_positions():
    """Should return proper threat positions when moving a Knight"""
    n = piece.Knight(6, 6)

    pos = n.threatened_positions((3, 3))
    assert pos == set([
        (5, 4), (5, 2), (4, 5), (4, 1), (1, 2), (1, 4), (2, 5), (2, 1)
    ])

    pos = n.threatened_positions((0, 0))
    assert pos == set([(2, 1), (1, 2)])

    pos = n.threatened_positions((6, 6))
    assert pos == set([(4, 5), (5, 4)])
