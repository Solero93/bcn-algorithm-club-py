from unittest import TestCase

from src.tasks import least_interval

cases = [
    #  TODO Add more test cases
    (
        ['A', 'A', 'A', 'B', 'B', 'B'], 2, 8
    )
]


class TasksTest(TestCase):

    def test_cases(self):
        for tasks, n, expected in cases:
            self.assertEqual(expected, least_interval(tasks, n),
                             msg=f'Output for {tasks}, {n} -> should be {expected}')
