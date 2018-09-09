from unittest import TestCase

from src.stones import num_jewels_in_stones

cases = [
    (
        "aA", "aAAbbbb", 3
    ),
    (
        "z", "ZZ", 0
    )
]


class StonesTest(TestCase):
    def test_cases(self):
        for jewels, stones, expected in cases:
            self.assertEqual(expected, num_jewels_in_stones(jewels, stones),
                             msg=f'Output for {jewels}, {stones} -> should be {expected}')
