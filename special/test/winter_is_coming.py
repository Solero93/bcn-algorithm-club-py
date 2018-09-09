from unittest import TestCase

from src.winter_is_coming import find_radius

cases = [
    #  TODO Add more tests cases
    (
        [1, 2, 3], [2], 1
    ),
    (
        [1, 2, 3, 4], [1, 4], 1
    )
]


class TasksTest(TestCase):
    def test_cases(self):
        for houses, heaters, expected in cases:
            self.assertEqual(expected, find_radius(houses, heaters),
                             msg=f'Output for {houses}, {heaters} -> should be {expected}')
