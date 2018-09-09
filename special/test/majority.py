from unittest import TestCase

from src.majority import majority

cases = [
    (
        [1], 1
    ),
    (
        [1, 1], 1
    ),
    (
        [1, 1, 2], 1
    ),
    (
        [1, 2, 1], 1
    ),
    (
        [2, 1, 1], 1
    ),
    (
        [2, 2, 1, 1, 1, 2, 2], 2
    )
]


class MajorityTest(TestCase):
    def test_cases(self):
        for numbers, expected in cases:
            self.assertEqual(expected, majority(numbers),
                             msg=f'Output for {numbers} -> should be {expected}')
