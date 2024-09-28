import unittest
from mars_rover import process_grid_size, process_input_line, INPUT_LINE_PATTERN, \
  out_of_bounds, move_forward, turn_left, turn_right, move_rover

class TestProcessGridSize(unittest.TestCase):
  def test_process_grid_size_valid_input(self):
    self.assertEqual(process_grid_size("4 8"), (4, 8))
    self.assertEqual(process_grid_size("10 20"), (10, 20))

  def test_process_grid_size_invalid_format(self):
    with self.assertRaises(ValueError):
      process_grid_size("4")
    with self.assertRaises(ValueError):
      process_grid_size("4 8 12")

  def test_process_grid_size_non_integer_values(self):
    with self.assertRaises(ValueError):
      process_grid_size("4 a")
    with self.assertRaises(ValueError):
      process_grid_size("a 8")

  def test_process_grid_size_non_positive_integers(self):
    with self.assertRaises(ValueError):
      process_grid_size("0 8")
    with self.assertRaises(ValueError):
      process_grid_size("4 0")
    with self.assertRaises(ValueError):
      process_grid_size("-4 8")
    with self.assertRaises(ValueError):
      process_grid_size("4 -8")

class TestProcessInputLine(unittest.TestCase):
  def test_process_input_line_valid_input(self):
    self.assertEqual(process_input_line("(1, 2, N) FFLR", INPUT_LINE_PATTERN), (1, 2, "N", ["F", "F", "L", "R"]))
    self.assertEqual(process_input_line("(0, 0, S) LRLR", INPUT_LINE_PATTERN), (0, 0, "S", ["L", "R", "L", "R"]))

  def test_process_input_line_invalid_format(self):
    with self.assertRaises(ValueError):
      process_input_line("1, 2, N FFLR", INPUT_LINE_PATTERN) # No parentheses
    with self.assertRaises(ValueError):
      process_input_line("(1, 2, N, S) FFLR", INPUT_LINE_PATTERN) # Extra value in parentheses
    with self.assertRaises(ValueError):
      process_input_line("5 (1, 2, N, S) FFLR", INPUT_LINE_PATTERN) # Extra value at start

  def test_process_input_line_invalid_direction(self):
    with self.assertRaises(ValueError):
      process_input_line("(1, 2, X) FFLR", INPUT_LINE_PATTERN)

  def test_process_input_line_invalid_commands(self):
    with self.assertRaises(ValueError):
      process_input_line("(1, 2, N) FFLRZ", INPUT_LINE_PATTERN)

  def test_process_input_line_invalid_starting_coordinate(self):
    with self.assertRaises(ValueError):
      process_input_line("(A, 2, N) FFLR", INPUT_LINE_PATTERN)
    with self.assertRaises(ValueError):
      process_input_line("(1, B, N) FFLR", INPUT_LINE_PATTERN)

class TestOutOfBounds(unittest.TestCase):
  def test_out_of_bounds(self):
    self.assertTrue(out_of_bounds(-1, 0, 5, 5))
    self.assertTrue(out_of_bounds(5, 0, 5, 5))
    self.assertTrue(out_of_bounds(0, -1, 5, 5))
    self.assertTrue(out_of_bounds(0, 5, 5, 5))
    self.assertFalse(out_of_bounds(0, 0, 5, 5))
    self.assertFalse(out_of_bounds(4, 4, 5, 5))

class TestMoveForward(unittest.TestCase):
  def test_move_forward_north(self):
    self.assertEqual(move_forward(0, 0, 'N'), (0, 1))
    self.assertEqual(move_forward(1, 1, 'N'), (1, 2))

  def test_move_forward_east(self):
    self.assertEqual(move_forward(0, 0, 'E'), (1, 0))
    self.assertEqual(move_forward(1, 1, 'E'), (2, 1))

  def test_move_forward_south(self):
    self.assertEqual(move_forward(0, 0, 'S'), (0, -1))
    self.assertEqual(move_forward(1, 1, 'S'), (1, 0))

  def test_move_forward_west(self):
    self.assertEqual(move_forward(0, 0, 'W'), (-1, 0))
    self.assertEqual(move_forward(1, 1, 'W'), (0, 1))

class TestTurnLeft(unittest.TestCase):
  def test_turn_left_north(self):
    self.assertEqual(turn_left('N'), 'W')

  def test_turn_left_west(self):
    self.assertEqual(turn_left('W'), 'S')

  def test_turn_left_south(self):
    self.assertEqual(turn_left('S'), 'E')

  def test_turn_left_east(self):
    self.assertEqual(turn_left('E'), 'N')

class TestTurnRight(unittest.TestCase):
  def test_turn_right_north(self):
    self.assertEqual(turn_right('N'), 'E')

  def test_turn_right_east(self):
    self.assertEqual(turn_right('E'), 'S')

  def test_turn_right_south(self):
    self.assertEqual(turn_right('S'), 'W')

  def test_turn_right_west(self):
    self.assertEqual(turn_right('W'), 'N')

class TestMoveRover(unittest.TestCase):
  def test_move_rover_simple(self):
    self.assertEqual(move_rover(1, 2, 'N', ['F', 'F', 'L', 'R'], 5, 5), '(1, 4, N)')
    self.assertEqual(move_rover(0, 0, 'N', ['L', 'R', 'L', 'R'], 5, 5), '(0, 0, N)')
    self.assertEqual(move_rover(0, 0, 'N', ['F', 'F', 'F', 'F'], 5, 5), '(0, 4, N)')
    self.assertEqual(move_rover(0, 0, 'N', ['F', 'F', 'F', 'F', 'F'], 5, 5), '(0, 4, N) LOST')

  def test_given_test_cases(self):
    self.assertEqual(move_rover(2, 3, 'N', ['F', 'L', 'L', 'F', 'R'], 4, 8), '(2, 3, W)')
    self.assertEqual(move_rover(1, 0, 'S', ['F', 'F', 'R', 'L', 'F', 'R'], 4, 8), '(1, 0, S) LOST')

if __name__ == '__main__':
  unittest.main()
