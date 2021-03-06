from unittest import TestCase

from src.islands import count_islands

cases = [
    (
        [[0]], 0
    ),
    (
        [[1]], 1
    ),
    (
        [[0, 0],
         [0, 0]], 0
    ),
    (
        [[1, 0],
         [0, 1]], 2
    ),
    (
        [[0, 0],
         [1, 1]], 1
    ),
    (
        [[1, 0],
         [1, 0]], 1
    ),
    (
        [[0, 1],
         [0, 1]], 1
    ),
    (
        [[1, 1, 1, 1, 0],
         [1, 1, 0, 1, 0],
         [1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0]], 1
    ),
    (
        [[1, 1, 0, 0, 0],
         [1, 1, 0, 0, 0],
         [0, 0, 1, 0, 0],
         [0, 0, 0, 1, 1]], 3
    ),
    (
        [[1, 1, 0, 0, 0],
         [1, 1, 0, 0, 0],
         [0, 0, 1, 0, 0]], 2
    )
]


class IslandsTest(TestCase):
    def test_cases(self):
        for map_grid, expected in cases:
            self.assertEqual(expected, count_islands(map_grid),
                             msg=f'Output for {map_grid} -> should be {expected}')
