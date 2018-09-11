from unittest import TestCase

from src.winter_is_coming import find_radius

cases = [
    (
        [1, 2, 3], [2], 1
    ),
    (
        [1, 2, 3, 4], [1, 4], 1
    ),
    (
        [1, 2, 3, 5, 6, 8, 9], [7, 4], 3
    ),
    (
        [3, 4], [1, 2], 2
    ),
    (
        [1, 2], [5, 6], 4
    )
]


class WinterIsComingTest(TestCase):
    def test_cases(self):
        for houses, heaters, expected in cases:
            self.assertEqual(expected, find_radius(houses, heaters),
                             msg=f'Output for {houses}, {heaters} -> should be {expected}')
