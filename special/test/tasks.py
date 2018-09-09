from unittest import TestCase
from src.tasks import least_interval

cases = [
    (
        [], 2, 1
    ),
    (
        2, 5, -1
    ),
    (
        0, 5, -3
    )
]


class TasksTest(TestCase):

    def test_cases(self):
        for tasks, n, expected in cases:
            self.assertCountEqual(expected, least_interval(i, j),
                                  msg=f'Output for {i}, {j} -> should be {expected}')

    # TODO Test that timing of successive calls should be less
