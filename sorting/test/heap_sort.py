from unittest import TestCase

from src.heap_sort import heap_sort
from test.fixtures import test_cases


class BuiltInSortTest(TestCase):
    def test_sort(self):
        for case in test_cases:
            self.assertEqual(heap_sort(case), sorted(case),
                             msg=f'{case} should be {sorted(case)}')
