import re
from typing import List, Tuple

INPUT_LINE_PATTERN = re.compile(r'^\((\d+), (\d+), ([NESW])\) ([FLR]+)$')

def process_grid_size(line: str) -> Tuple[int, int]:
  values = line.strip().split()
  if len(values) != 2:
    raise ValueError('The input\'s first line should have exactly two positive integers, i.e. 4 8')
  if not values[0].isdigit() or not values[1].isdigit():
    raise ValueError('The input\'s first line are not positive integers')

  width, height = int(values[0]), int(values[1])
  if width < 1 or height < 1:
    raise ValueError('The height and width are not positive integers')
  return width, height

def process_input_line(line: str, pattern: re.Pattern) -> Tuple[int, int, str, List[str]]:
  match = pattern.match(line)
  if not match:
    raise ValueError('The input line is not in the correct format')

  x, y, orientation, commands = match.groups()
  return int(x), int(y), orientation, [char for char in commands]

def out_of_bounds(x: int, y: int, width: int, height: int) -> bool:
  return x < 0 or x >= width or y < 0 or y >= height

def move_forward(x: int, y: int, orientation: str) -> Tuple[int, int]:
  if orientation == 'N':
    y += 1
  elif orientation == 'E':
    x += 1
  elif orientation == 'S':
    y -= 1
  elif orientation == 'W':
    x -= 1
  return x, y

def turn_right(orientation: str) -> str:
  if orientation == 'N':
    return 'E'
  elif orientation == 'E':
    return 'S'
  elif orientation == 'S':
    return 'W'
  elif orientation == 'W':
    return 'N'

def turn_left(orientation: str) -> str:
  if orientation == 'N':
    return 'W'
  elif orientation == 'W':
    return 'S'
  elif orientation == 'S':
    return 'E'
  elif orientation == 'E':
    return 'N'

def move_rover(x: int, y: int, orientation: str, commands: List[str], width: int, height: int) -> str:
  if out_of_bounds(x, y, width, height):
    raise ValueError('The rover is starting out of bounds')

  prev_x, prev_y = x, y
  for command in commands:
    if command == 'F':
      x, y = move_forward(x, y, orientation)
      if out_of_bounds(x, y, width, height):
        return f'({prev_x}, {prev_y}, {orientation}) LOST'
      prev_x, prev_y = x, y
    elif command == 'L':
      orientation = turn_left(orientation)
    elif command == 'R':
      orientation = turn_right(orientation)
    else:
      raise ValueError('The rover received an invalid command')

  return f'({x}, {y}, {orientation})'

def main() -> None:
  width, height = None, None
  outputs = []
  with open('input.txt', 'r') as file:
    for line in file:
      if not width or not height:
        width, height = process_grid_size(line.strip())
        continue
      x, y, orientation, commands = process_input_line(line.strip(), INPUT_LINE_PATTERN)
      output = move_rover(x, y, orientation, commands, width, height)
      outputs.append(output)

  with open('output.txt', 'w') as file:
    for output in outputs:
      file.write(f'{output}\n')

  return

if __name__ == '__main__':
  main()
