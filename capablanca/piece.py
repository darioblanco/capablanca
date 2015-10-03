# -*- coding: utf-8 -*-
# Copyright 2015, Dario Blanco

"""
capablanca.piece
~~~~~~~~~~~~~~~~~
This module contains Chess piece abstractions with their possible movements
"""


class Piece(object):
    """Chess piece abstraction"""

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def get_threats(self, current):
        """Calculates threatened positions from the current one"""
        raise NotImplementedError()

    def remove_invalid_positions(self, positions):
        """Filters out positions outside of the board range"""
        return [p for p in positions
                if p[0] >= 0 and p[1] >= 0 and
                p[0] < self.height and p[1] < self.width]


class King(Piece):
    """
    Chess piece representing the King.
    Moves one square vertically, horizontally and diagonally
    """

    def get_threats(self, current):
        """Calculates King threatened positions from the current one"""
        positions = []

        i, j = current
        positions += [(i-1, j-1), (i, j-1),
                      (i+1, j-1), (i-1, j),
                      (i+1, j), (i-1, j+1),
                      (i, j+1), (i+1, j+1)]

        return set(self.remove_invalid_positions(positions))


class Bishop(Piece):
    """
    Chess piece representing the King.
    Moves diagonally
    """

    def get_threats(self, current):
        """Calculates Bishop threatened positions from the current one"""
        positions = []

        limit = min(self.height, self.width)
        i, j = current
        positions += [
            (i+x, j+x) for x in range(1, limit)
            if 0 <= i < self.height and 0 <= j < self.width
        ]
        positions += [
            (i+x, j-x) for x in range(1, limit)
            if 0 <= i < self.height and 0 <= j < self.width
        ]
        positions += [
            (i-x, j+x) for x in range(1, limit)
            if 0 <= i < self.height and 0 <= j < self.width
        ]
        positions += [
            (i-x, j-x) for x in range(1, limit)
            if 0 <= i < self.height and 0 <= j < self.width
        ]

        return set(self.remove_invalid_positions(positions))


class Rook(Piece):
    """
    Chess piece representing the Rook.
    Moves horizontally and vertically
    """

    def get_threats(self, current):
        """Calculates Rook threatened positions from the current one"""
        positions = []

        i, j = current

        positions += [(i, y) for y in range(j)]
        positions += [(i, y) for y in range(j+1, self.width)]
        positions += [(x, j) for x in range(i)]
        positions += [(x, j) for x in range(i+1, self.height)]

        return set(positions)


class Queen(Bishop, Rook):
    """
    Chess piece representing the Rook.
    Has Bishop and Rook movements
    """

    def get_threats(self, current):
        """Calculates Queen threatened positions from the current one"""
        # Retrieve positions for the Bishop movement
        positions = Queen.__bases__[0].get_threats(self, current)
        # Retrieve positions for the Rook movement
        positions.update(Queen.__bases__[1].get_threats(self, current))
        return positions


class Knight(Piece):
    """
    Chess piece representing the Knight.
    Moves in a 'L' shape (2 squares straight and 1 left or right)
    """

    def get_threats(self, current):
        """Calculates King threatened positions from the current one"""
        positions = []

        i, j = current
        positions += [(i+2, j+1), (i+2, j-1),
                      (i+1, j+2), (i+1, j-2),
                      (i-2, j-1), (i-2, j+1),
                      (i-1, j+2), (i-1, j-2)]

        return set(self.remove_invalid_positions(positions))
