from unittest import TestCase

from src.selection_sort import selection_sort
from test.fixtures import test_cases


class BuiltInSortTest(TestCase):
    def test_sort(self):
        for case in test_cases:
            self.assertEqual(selection_sort(case), sorted(case),
                             msg=f'{case} should be {sorted(case)}')
