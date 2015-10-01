# -*- coding: utf-8 -*-
# Copyright 2015, Dario Blanco

from capablanca import piece


class ChessPlayer(object):

    def __init__(self, width, height, piece_counts):
        self.width = width
        self.height = height

        self.chess_pieces = {
            'K': piece.King(width, height),
            'Q': piece.Queen(width, height),
            'B': piece.Bishop(width, height),
            'R': piece.Rook(width, height),
            'N': piece.Knight(width, height)
        }

        self.pieces = []
        for name, count in piece_counts.iteritems():
            if count > 0:
                self.pieces += [name for i in range(count)]

    def run(self):
        pass

    def draw_boards(self):
        return ""
