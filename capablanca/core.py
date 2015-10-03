# -*- coding: utf-8 -*-
# Copyright 2015, Dario Blanco

import time
from copy import deepcopy

from capablanca import piece


class ChessPlayer(object):
    """Create all possible solutions for the given pieces and board size"""

    def __init__(self, height, width, piece_counts):
        """Assigns board size and create piece abstractions"""
        self.height = height
        self.width = width

        self.chess_pieces = {
            'K': piece.King(height, width),
            'Q': piece.Queen(height, width),
            'B': piece.Bishop(height, width),
            'R': piece.Rook(height, width),
            'N': piece.Knight(height, width)
        }

        self.pieces = []
        # Sorted list of pieces based on how many squares will they cover
        for p in ['Q', 'R', 'B', 'K', 'N']:
            self.pieces += [p for i in range(piece_counts[p])]

        self.solutions = set()
        self.elapsed_time = None  # Problem resolution time in float seconds

    def run(self):
        """
        Starts the backtracking algorithm process from top to down,
        setting the initial state
        """
        start = time.clock()
        free = set()
        # Generate all board position coordinates as tuples
        for i in range(self.height):
            for j in range(self.width):
                free.add((i, j))
        # Start backtracking algorithm
        self._solve(free, set(), {}, 0)
        self.elapsed_time = time.clock() - start

    def _solve(self, free, occupied, assigned, piece_index):
        """
        Iterates through the search tree recursively, from the root down,
        in depth-first order, until it finds a valid solution or it runs
        out of elegible chess positions
        """
        if piece_index == len(self.pieces):
            # Found solution as there are no more pieces to assign
            self.solutions.add(self._generate_board(assigned))
            return

        p = self.pieces[piece_index]  # Retrieve next chess piece
        for f in free:
            # Retrieve all positions current piece threatens in this slot
            threat_pos = set(self.chess_pieces[p].threatened_positions(f))
            if threat_pos & occupied:
                # Current piece in that position threatens another one: skip
                continue

            o = deepcopy(occupied)  # deep copy of occupied positions set
            a = deepcopy(assigned)  # deep copy of assigned positions dict

            piece_positions = a.get(p, [])
            if f in piece_positions:
                # Current position is already assigned
                continue

            # Occupy that slot for further iterations
            o.add(f)
            # Add position for that piece (for printing purposes)
            a.setdefault(p, []).append(f)

            # Recursive call with updated free, occupied and assigned slots,
            # for the next piece index
            self._solve(free - threat_pos - o, o, a, piece_index + 1)

    def draw_boards(self):
        """Concatenates all tracked unique solution strings"""
        n_solutions = len(self.solutions)
        output = "\nSolutions:\n\n"

        for i, solution in enumerate(self.solutions):  # Show 15 solutions max
            if i == 15:
                break
            else:
                output += "{}\n".format(solution)

        output += "{} solutions found in {} seconds\n".format(
            n_solutions, self.elapsed_time)
        return output

    def _generate_board(self, layout):
        """
        Creates a pretty formatted string from a dictionary of piece types
        assigned to one or more positions
        """
        output = ""
        board = [['-' for x in range(self.width)]
                 for x in range(self.height)]
        for piece_name, positions in layout.iteritems():
            for pos in positions:
                board[pos[0]][pos[1]] = piece_name
        output += "* " * (self.width + 1) + "*\n"
        for row in board:
            output += "* {} *\n".format(" ".join(row))
        output += "* " * (self.width + 1) + "*\n"
        return output
