from unittest import TestCase

from src.quick_sort import quick_sort
from test.fixtures import test_cases


class BuiltInSortTest(TestCase):
    def test_sort(self):
        for case in test_cases:
            self.assertEqual(quick_sort(case), sorted(case),
                             msg=f'{case} should be {sorted(case)}')
