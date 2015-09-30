# Capablanca

[Jose Raúl Capablanca y Graupera](https://en.wikipedia.org/wiki/Jos%C3%A9_Ra%C3%BAl_Capablanca) was one of the greatest chess players in history, and gives name to this little chess experiment. Capablanca was awesome, and as any amazing chess guru, he could think in many different chess plays in advance, in order to bow down his rivals.

This little program tries to emulate him, showing all combinations for a given set of pieces in a scenario where none of them can take any of the others.


### Input

The input given to Capablanca should match the following criteria

- Board dimensions have to be provided (width and height), greater than 0 and smaller than 100
- There are 5 available pieces: King (KI), Queen (Q), Bishop (B) and Knight (KN)
- Number of each piece to be placed has to be provided
- Pieces don't have colours

A set of chess pieces on a chess board with specific dimensions, where none of the pieces can't take any of the others

### Output

Capablanca will show all the unique configurations for the provided pieces, where none of the pieces is in a position to take any of the others


## Execution

First of all, install the needed dependencies via pip

> pip install -r requirements.txt

And that's all! Now, you can play with Capablanca, he will tell you what data he needs at any time.

> python capablanca/play.py

Capablanca also explains what he does!

> python capablanca/play.py --help

After all the data he needs have been provided, Capablanca will draw all possible combinations.

