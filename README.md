# Project Name
Mars Rover

## Description
Jonathan Lao's submission for Multiverse's Mars Rover take home challenge.

## Installation / How to run
Make sure you have [Python3](https://www.python.org/downloads/) installed locally.

Then run:

`python3 mars_rover.py`

Input can be specified via `input.txt` and be colocated in the same directory.

Output will generated in an `output.txt` file.

## Testing
Run tests via:

`python3 -m unittest test_mars_rover.py`

## Notes / Future Improvements
- TODO - More complicated test cases on larger grids and more commands
- The assignment describes the form of the input, but not where the input comes from - so I just chose to pass it in via an `input.txt` file. We could also pass the input file as a cli argument or via stdin.
- To keep it simple, the algorithm is written procedurally. But if we add more functionality to the mars rover, it may make sense to make this object oriented, with a MarsRover Class, methods for moving and turning, storing its location in internal state, and instantiating a new MarsRover for each line of input.

