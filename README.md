# Capablanca
![Build Status](https://travis-ci.org/sharkerz/capablanca.svg?branch=master)

[Jose Raúl Capablanca y Graupera](https://en.wikipedia.org/wiki/Jos%C3%A9_Ra%C3%BAl_Capablanca) was one of the greatest chess players in history, and gives name to this little chess experiment. Capablanca was awesome, and as any amazing chess guru, he could think in many different chess plays in advance, in order to bow down his rivals.

This little program tries to emulate him, showing all combinations for a given set of pieces in a scenario where none of them can take any of the others.


### Input

The input given to Capablanca should match the following criteria

- Board dimensions have to be provided (width and height), greater than 0 and smaller or equals than 10
- There are 5 available pieces: King (KI), Queen (Q), Bishop (B) and Knight (KN)
- Number of each piece to be placed has to be provided (maximum 10 pieces)
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

If you want to run Capablanca without any dependency, you can directly call `capablanca.core.ChessPlayer` from a python interactive shell.


## Development

This project uses `python 2.7`, and `click` as an external library for handling console parameters and the interactive mode.

For proper developing (running tests, style check, coverage...) you have to install the development dependencies:

> pip install -r dev-requirements.txt

I recommend using `virtualenv` and `virtualenvwrapper`. A common set up with both tools is the following

> cd ~/capablanca
> mkvirtualenv -a . capablanca
> add2virtualenv .

With this set up, every time you perform `workon capablanca`, `virtualenvwrapper` will automatically switch to the project folder. `add2virtualenv .` sets up the needed PYTHONPATH for loading Capablanca's modules.

### Test

Tests are using `pytest` framework, for running all unit tests, just execute

> py.test

You can find more information about how to run `pytest` [here](https://pytest.org/latest/usage.html).

Integration tests (under `test_capablanca.py`) are disabled by default, as they can be really slow. In order to allow a `py.test` discovery without having integration tests there, a custom py.test parameter has been created, which has to be provided in order to run them.

You can execute the integration tests with

> py.test --test-type integration

#### Test coverage

This project uses `pytest-cov` for measuring coverage, just append the parameter `--cov=capablanca` to any `pytest` call, for instance

> py.test --cov=capablanca

The test coverage statistics will be shown at the end of the run

### Code Analysis

Code Analysis is performed via `pylint`. In order to rate the code, simply run

> pylint capablanca

### Code Style

The code is following [PEP8](http://www.python.org/dev/peps/pep-0008/) conventions. In order to check for convention violations, just run

> pep8 capablanca/*.py -v

This command will output PEP8 errors found (if any)

### Profiling

In order to measure total and function running time, calls, and other useful parameters for running optimizations, you can use one of the many Python profiler tools available.

For instance, with `cProfile`, you can call capablanca's script adding that module:

> python -m cProfile capablanca/play.py

The profile statistics will be printed out at the end.

## Examples

### 7x7 board with 2 Kings, 2 Queens, 2 Bishops and 1 Knight

```
(capablanca)➜  capablanca git:(master) ✗ python capablanca/play.py
Please enter board width: 7
Please enter board height: 7
Please enter number of Kings: 2
Please enter number of Queens: 2
Please enter number of Bishops: 2
Please enter number of Rooks: 0
Please enter number of Knights: 1

Solutions:

* * * * * * * * *
* K - N - - - - *
* - - - - - - - *
* - - - - - - - *
* B - - - - - - *
* - - - Q - - - *
* - - - - - - Q *
* - - B - K - - *
* * * * * * * * *

* * * * * * * * *
* K - - - - - - *
* - - - - - - Q *
* - - - - Q - - *
* N - B - - - - *
* B - - - - - - *
* - - - - - - - *
* - - - K - - - *
* * * * * * * * *

* * * * * * * * *
* - - - - - - - *
* N - - - B - - *
* - - - - - - - *
* K - - - - - - *
* - - Q - - - - *
* - - - - - Q - *
* - B - K - - - *
* * * * * * * * *

* * * * * * * * *
* - - - - - - - *
* - K - - - K - *
* - - - Q - - - *
* - B - - - - - *
* - - - - - - Q *
* - - - - B - - *
* N - - - - - - *
* * * * * * * * *

* * * * * * * * *
* - Q - - - - - *
* - - - K - - N *
* - - - - - - - *
* - - - B - - - *
* K - - - - - - *
* - - - B - - - *
* - - - - - Q - *
* * * * * * * * *

* * * * * * * * *
* - - - - - - - *
* N - - - - - - *
* - - - - - Q - *
* B - K - - - - *
* - - - - - - Q *
* K - - B - - - *
* - - - - - - - *
* * * * * * * * *

* * * * * * * * *
* - - - - - K - *
* - N - - - - - *
* - B - - - K - *
* - - - - - - - *
* - - - - - - Q *
* - B - - - - - *
* - - - Q - - - *
* * * * * * * * *

* * * * * * * * *
* - B - - - - - *
* - - - - Q - - *
* B - - - - - - *
* - - - K - K - *
* - - - - - - - *
* - - Q - - - - *
* - - - - - - N *
* * * * * * * * *

* * * * * * * * *
* - - - - K - - *
* N - - - - - - *
* B - - - - - K *
* - - - - - - - *
* - - - - - Q - *
* - - Q - - - - *
* - - - - - - B *
* * * * * * * * *

* * * * * * * * *
* - Q - - - - - *
* - - - - - - - *
* - - - - - - K *
* B - - - - - - *
* N - - B - - - *
* - - - - - Q - *
* - - K - - - - *
* * * * * * * * *

* * * * * * * * *
* B - - - - - - *
* - - - - K - K *
* - - - - - - - *
* - - - - - Q - *
* - - - - - - - *
* - Q - - - - - *
* - - - B N - - *
* * * * * * * * *

* * * * * * * * *
* - - - - - - - *
* - - - Q - - - *
* K - - - - - - *
* - - - - - - K *
* - - - - B - - *
* - Q - - - - - *
* - - - - N B - *
* * * * * * * * *

* * * * * * * * *
* - - - - - - - *
* - Q - - - - - *
* - - - K - - - *
* - - - - - Q - *
* B - - - - - - *
* N - B - K - - *
* - - - - - - - *
* * * * * * * * *

* * * * * * * * *
* - - - B - - B *
* - K - - - - - *
* - - - - - - - *
* - - - - - Q - *
* - - - - - - - *
* Q - - - - - - *
* - - - - K - N *
* * * * * * * * *

* * * * * * * * *
* - - - - - N - *
* B - K - - - - *
* - - - - - K - *
* - - - - - - - *
* - - - - - - B *
* - Q - - - - - *
* - - - Q - - - *
* * * * * * * * *

(only showing up to 15 unique solutions)
3063828 solutions found in 211.468422 seconds
```
