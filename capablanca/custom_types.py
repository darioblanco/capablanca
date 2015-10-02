# -*- coding: utf-8 -*-
# Copyright 2015, Dario Blanco

import click


class BoardDimension(click.ParamType):
    """Hold validation for width/height console parameters"""
    name = 'dimension'

    def convert(self, value, param, ctx):
        """Returns a dimension (width/height) within the allowed bounds"""

        try:
            dimension = int(value)
        except ValueError:
            self.fail('provided value is not a valid integer')
        else:
            if 0 < dimension < 8:
                return dimension
            else:
                self.fail('dimension {} should be greater than 0 '
                          'and lesser than 8'.format(dimension))

    def __repr__(self):
        return 'DIMENSION'


class PieceNumber(click.ParamType):
    """Hold validation for piece console parameters"""
    name = 'piece_number'

    def convert(self, value, param, ctx):
        """Returns the number of pieces if it fits in the dimension"""

        try:
            n_pieces = int(value)
        except ValueError:
            self.fail('provided value is not a valid integer')
        else:
            if n_pieces <= 10:
                return n_pieces
            else:
                self.fail('piece number {} should be lesser or equals than 10'
                          ''.format(n_pieces))

    def __repr__(self):
        return 'PIECE_NUMBER'
