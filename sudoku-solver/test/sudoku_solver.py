from unittest import TestCase

from src.sudoku_solver import sudoku_solver
from test.examples import all_examples
from utils.read_matrix import read_matrix


class SudokuSolverTest(TestCase):
    def test_sudoku_solver(self):
        for example_filename in all_examples():
            sudoku_to_solve = read_matrix(example_filename)
            our_solution = sudoku_solver(sudoku_to_solve)

            def check_row(row, column):
                return all(our_solution[row][column] != our_solution[row][j]
                           for j in range(len(our_solution)) if j != column)

            def check_column(row, column):
                return all(our_solution[row][column] != our_solution[i][column]
                           for i in range(len(our_solution)) if i != row)

            def check_block(row, column):
                beginning_of_block = row - (row % 3), column - (column % 3)
                return all(our_solution[row][column] != our_solution[i][j]
                           for i in range(beginning_of_block[0], beginning_of_block[0] + 2)
                           for j in range(beginning_of_block[1], beginning_of_block[1] + 2)
                           if i != row and j != column)

            for row in range(len(sudoku_to_solve)):
                for column in range(len(sudoku_to_solve)):
                    try:
                        current_value = our_solution[row][column]
                    except:
                        self.fail(msg=f'Cannot access element at {row, column}, '
                                      f'probably because the solution returned is not a 9x9 matrix')

                    self.assertTrue(
                        sudoku_to_solve[row][column] == current_value or sudoku_to_solve[row][column] is None,
                        msg=f'Changed element of original sudoku at {row, column}, '
                            f'value was changed from {sudoku_to_solve[row][column]} to {current_value}')

                    self.assertIsNotNone(current_value,
                                         msg=f'Empty value at {row, column}')

                    self.assertIn(current_value, range(1, 10),
                                  msg=f'Element at {row, column} is not a whole number between 1 and 9, '
                                      f'but {current_value}')

                    self.assertTrue(check_row(row, column),
                                    msg=f'Row check failed at {row, column} value={current_value}')

                    self.assertTrue(check_column(row, column),
                                    msg=f'Column check failed at {row, column} value={current_value}')

                    self.assertTrue(check_block(row, column),
                                    msg=f'Block check failed at {row, column} value={current_value}')
