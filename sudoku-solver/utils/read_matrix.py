from typing import List


BLANK_CHARACTER = '*'


def read_matrix(filename: str) -> List[List[int]]:
    with open(filename, 'r') as sudoku_file:
        sudoku_matrix = [[None if x == BLANK_CHARACTER else int(x) for x in line.rstrip('\n')] for line in sudoku_file]
    return sudoku_matrix
