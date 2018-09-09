from unittest import TestCase

from src.sums import Sums

cases = [
    (
        0, 2, 1
    ),
    (
        2, 5, -1
    ),
    (
        0, 5, -3
    )
]


class SumsTest(TestCase):
    def setUp(self):
        self.sums = Sums([-2, 0, 3, -5, 2, -1])

    def test_cases(self):
        for i, j, expected in cases:
            self.assertEqual(expected, self.sums.sum_range(i, j),
                             msg=f'Output for {i}, {j} -> should be {expected}')

    # TODO Test that timing of successive calls should be less
