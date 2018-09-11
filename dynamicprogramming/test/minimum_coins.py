from unittest import TestCase

from src.minimum_coins import minimum_coins

cases = [
    (
        [1], 1, 1
    ),
    (
        [1], 2, 2
    ),
    (
        [1, 2], 3, 2
    ),
    (
        [1, 2], 4, 2
    ),
    (
        [1, 2], 6, 3
    ),
    (
        [25, 10, 5], 30, 2
    ),
    (
        [9, 6, 5, 1], 11, 2
    )
]


class MinimumCoinsTest(TestCase):
    def test_cases(self):
        for coins, change, expected in cases:
            self.assertEqual(expected, minimum_coins(coins, change),
                             msg=f'Output for {coins}, {change} -> should be {expected}')
