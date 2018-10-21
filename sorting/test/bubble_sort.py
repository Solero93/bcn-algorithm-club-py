from unittest import TestCase

from src.bubble_sort import bubble_sort
from test.fixtures import test_cases


class BubbleSortTest(TestCase):
    def test_sort(self):
        for case in test_cases:
            self.assertEqual(bubble_sort(case), sorted(case),
                             msg=f'{case} should be {sorted(case)}')
