from unittest import TestCase

from solutions.subset_has_sum import subset_has_sum

cases = [
    (
        [1], 1, True
    ),
    (
        [1], 2, False
    ),
    (
        [1, 2], 3, True
    ),
    (
        [1, 2], 4, False
    ),
    (
        [3, 34, 4, 12, 5, 2], 9, True
    ),
    (
        [3, 34, 4, 12, 5, 2], 1000, False
    )
]


class SubsetHasSumTest(TestCase):
    def test_cases(self):
        for numbers, subset_sum, expected in cases:
            self.assertEqual(expected, subset_has_sum(numbers, subset_sum),
                             msg=f'Output for {numbers}, {subset_sum} -> should be {expected}')
