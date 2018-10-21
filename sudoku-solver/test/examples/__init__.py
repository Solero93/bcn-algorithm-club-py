import glob


def all_examples():
    return glob.iglob('./examples/*.sudoku')
