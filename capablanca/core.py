# -*- coding: utf-8 -*-
# Copyright 2015, Dario Blanco

"""
capablanca.core
~~~~~~~~~~~~~~~~~
This module contains the logic that Capablanca uses for solving chess problems
"""

import time
from copy import deepcopy

from capablanca.cache import ThreatCache


class ChessPlayer(object):
    """Create all possible solutions for the given pieces and board size"""

    def __init__(self, height, width, piece_counts):
        """Assigns board size and create piece abstractions"""
        self.height = height
        self.width = width

        self.threat_cache = ThreatCache(height, width)

        self.pieces = []
        # Sorted list of pieces based on how many squares will they cover
        for piece in ['Q', 'R', 'B', 'K', 'N']:
            self.pieces += [piece for i in range(piece_counts[piece])]

        self.solutions = set()
        self.elapsed_time = None  # Problem resolution time in float seconds

    def run(self):
        """
        Starts the backtracking algorithm process from top to down,
        setting the initial state
        """
        start = time.clock()
        free_positions = set()
        # Generate all board position coordinates as tuples
        for i in range(self.height):
            for j in range(self.width):
                free_positions.add((i, j))
        # Start backtracking algorithm
        self._solve(free_positions, set(), {}, 0)
        self.elapsed_time = time.clock() - start

    def _solve(self, free_positions, occupied_positions, assigned_positions,
               piece_index):
        """
        Iterates through the search tree recursively, from the root down,
        in depth-first order, until it finds a valid solution or it runs
        out of elegible chess positions
        """
        if piece_index == len(self.pieces):
            # Found solution as there are no more pieces to assign
            self.solutions.add(self._generate_board(assigned_positions))
            return

        piece = self.pieces[piece_index]  # Retrieve next chess piece
        for free_position in free_positions:
            # Retrieve all positions current piece threatens in this slot
            threatened_positions = set(
                self.threat_cache.get_threats(piece, free_position))
            if threatened_positions & occupied_positions:
                # Current piece threatens a previously placed one: backtrack
                continue

            occupied_copy = occupied_positions.copy()
            assigned_copy = deepcopy(assigned_positions)

            # Occupy that slot for further iterations
            occupied_copy.add(free_position)
            # Add new position to the current piece
            assigned_copy.setdefault(piece, []).append(free_position)

            # Recursive call with updated free, occupied and assigned slots,
            # for the next piece index
            self._solve(free_positions - threatened_positions - occupied_copy,
                        occupied_copy, assigned_copy, piece_index + 1)

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
