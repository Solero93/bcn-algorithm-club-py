from unittest import TestCase

from src.paths import has_path_sum

cases = [
    (
        [], 1, False
    ),
    (
        [1], 1, True
    ),
    (
        [1], 2, False
    ),
    (
        [1, [2]], 3, True
    ),
    (
        [1, [2]], 4, False
    ),
    (
        [5, [4, [11, [7], [2]]], [8, [13], [4, [1]]]], 22, True
    ),
    (
        [5, [4, [11, [7], [2]]], [8, [13], [4, [1]]]], 100, False
    )
]


class PathsTest(TestCase):
    def test_cases(self):
        for tree, sum_path, expected in cases:
            self.assertEqual(expected, has_path_sum(tree, sum_path),
                             msg=f'Output for {tree}, {sum_path} -> should be {expected}')
