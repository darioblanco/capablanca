# -*- coding: utf-8 -*-
# Copyright 2015, Dario Blanco

import click

from capablanca import custom_types


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

    pieces = {
        'King': 0,
        'Queen': 0,
        'Bishop': 0,
        'Rook': 0,
        'Knight': 0
    }
    pieces['King'] = click.prompt("Please enter number of Kings",
                                  type=custom_types.PieceNumber())
    pieces['Queen'] = click.prompt("Please enter number of Queens",
                                   type=custom_types.PieceNumber())
    pieces['Bishop'] = click.prompt("Please enter number of Bishops",
                                    type=custom_types.PieceNumber())
    pieces['Rook'] = click.prompt("Please enter number of Rooks",
                                  type=custom_types.PieceNumber())
    pieces['Knight'] = click.prompt("Please enter number of Knights",
                                    type=custom_types.PieceNumber())


if __name__ == '__main__':
    play()
