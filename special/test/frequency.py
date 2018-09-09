from unittest import TestCase

from src.frequency import most_frequent

cases = [
    (
        [], 2, []
    ),
    (
        [1], 0, []
    ),
    (
        [1], 1, [1]
    ),
    (
        [1], 2, [1]
    ),
    (
        [1, 1, 1, 2, 2, 3], 1, [1]
    ),
    (
        [1, 1, 1, 2, 2, 3], 2, [1, 2]
    )
]


class FrequencyTest(TestCase):
    def test_cases(self):
        for numbers, k, expected in cases:
            self.assertCountEqual(expected, most_frequent(numbers, k),
                                  msg=f'Output for {numbers} -> should be {expected}')
