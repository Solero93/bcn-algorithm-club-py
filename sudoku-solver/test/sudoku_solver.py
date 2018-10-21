from unittest import TestCase

from dlxsudoku import Sudoku

from src.sudoku_solver import sudoku_solver
from test.examples import all_examples
from utils.read_matrix import read_matrix


class SudokuSolverTest(TestCase):
    def test_sudoku_solver(self):
        for example_filename in all_examples():
            dlx_solver = Sudoku.load_file(example_filename)
            dlx_solver.solve(allow_brute_force=True)
            real_solution = dlx_solver._matrix

            our_solution = sudoku_solver(read_matrix(example_filename))

            self.assertEqual(real_solution, our_solution, msg=f'Solution for "{example_filename}" is incorrect')
