from unittest import TestCase

from src.fibonacci import fibonacci

cases = [
    (n, expected) for n, expected in enumerate([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597])
]


class FibonacciTest(TestCase):
    def test_cases(self):
        for n, expected in cases:
            self.assertEqual(expected, fibonacci(n),
                             msg=f'Output for {n} -> should be {expected}')
