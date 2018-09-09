from unittest import TestCase

from src.numbers import self_dividing_numbers

cases = [
    (
        1, 1, [1]
    ),
    (
        1, 2, [1, 2]
    ),
    (
        2, 3, [2, 3]
    ),
    (
        11, 14, [11, 12]
    ),
    (
        1, 22, [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
    ),
]


class NumbersTest(TestCase):
    def test_cases(self):
        for left, right, expected in cases:
            self.assertCountEqual(expected, self_dividing_numbers(left, right),
                                  msg=f'Output for {left}, {right} -> should be {expected}')
