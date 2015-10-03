# -*- coding: utf-8 -*-
# Copyright 2015, Dario Blanco

"""
capablanca.piece
~~~~~~~~~~~~~~~~~
This module provides the main entry to Capablanca and retrieves console params
"""

import click

from capablanca import custom_types
from capablanca.core import ChessPlayer


@click.command()
def play():
    """
    Asks interactively for user chess parameters and calculates all possible
    chess boards where none of the placed pieces can take any of the others
    """
    width = click.prompt("Please enter board width",
                         type=custom_types.BoardDimension())
    height = click.prompt("Please enter board height",
                          type=custom_types.BoardDimension())

    pieces = {}
    pieces['K'] = click.prompt("Please enter number of Kings",
                               type=custom_types.PieceNumber())
    pieces['Q'] = click.prompt("Please enter number of Queens",
                               type=custom_types.PieceNumber())
    pieces['B'] = click.prompt("Please enter number of Bishops",
                               type=custom_types.PieceNumber())
    pieces['R'] = click.prompt("Please enter number of Rooks",
                               type=custom_types.PieceNumber())
    pieces['N'] = click.prompt("Please enter number of Knights",
                               type=custom_types.PieceNumber())

    cp = ChessPlayer(height, width, pieces)
    cp.run()
    click.echo(cp.draw_boards())


if __name__ == '__main__':
    play()
