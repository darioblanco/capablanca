# -*- coding: utf-8 -*-
# Copyright 2015, Dario Blanco

"""
capablanca.cache
~~~~~~~~~~~~~~~~~
This module contains cache classes for avoiding unnecessary recalculations
"""

from capablanca.piece import King, Queen, Bishop, Rook, Knight


class ThreatCache(object):
    """
    The cache for storing threat coordinates calculated
    for a piece in a specific position
    """
    def __init__(self, height, width):
        """Initializes the piece classes and empty cache"""
        self.chess_pieces = {
            'K': King(height, width),
            'Q': Queen(height, width),
            'B': Bishop(height, width),
            'R': Rook(height, width),
            'N': Knight(height, width)
        }
        self.cache = {}

    def get_threats(self, piece, position):
        """
        Returns a set of threats for a piece in the given position,
        retrieving it from the cache. If it wasn't in the cache, calculates it
        and updates the cache
        """
        threat_hash = "{}:{},{}".format(piece, position[0], position[1])
        try:
            # Cache hit, do not recalculate threat positions
            return self.cache[threat_hash]
        except KeyError:
            # Cache miss, calculate threat and store in the cache
            threats = self.chess_pieces[piece].get_threats(position)
            self.cache[threat_hash] = threats
            return threats

    def clear(self):
        """Empties the cache"""
        self.cache = {}
