# -*- coding: utf-8 -*-
# Copyright 2015, Dario Blanco


class Piece(object):
    """Chess piece abstraction"""

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def threatened_positions(self, current):
        """Calculates threatened positions from the current one"""
        raise NotImplementedError()

    def _is_valid_position(self, pos):
        """Returns True if the given coordinates are inside the board"""
        i, j = pos
        return i >= 0 and j >= 0 and i < self.height and j < self.width

    def remove_invalid_positions(self, positions):
        """Filters out positions outside of the board range"""
        return filter(self._is_valid_position, positions)


class King(Piece):
    """
    Chess piece representing the King.
    Moves one square vertically, horizontally and diagonally
    """

    def threatened_positions(self, current):
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

    def threatened_positions(self, current):
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

    def threatened_positions(self, current):
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

    def threatened_positions(self, current):
        """Calculates Queen threatened positions from the current one"""
        # Retrieve positions for the Bishop movement
        positions = super(Queen, self).threatened_positions(current)
        # Retrieve positions for the Rook movement
        positions.update(super(Bishop, self).threatened_positions(current))
        return positions


class Knight(Piece):
    """
    Chess piece representing the Knight.
    Moves in a 'L' shape (2 squares straight and 1 left or right)
    """

    def threatened_positions(self, current):
        """Calculates King threatened positions from the current one"""
        positions = []

        i, j = current
        positions += [(i+2, j+1), (i+2, j-1),
                      (i+1, j+2), (i+1, j-2),
                      (i-2, j-1), (i-2, j+1),
                      (i-1, j+2), (i-1, j-2)]

        return set(self.remove_invalid_positions(positions))
