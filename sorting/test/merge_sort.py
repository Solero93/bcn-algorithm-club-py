from unittest import TestCase

from src.merge_sort import merge_sort
from test.fixtures import test_cases


class BuiltInSortTest(TestCase):
    def test_sort(self):
        for case in test_cases:
            self.assertEqual(merge_sort(case), sorted(case),
                             msg=f'{case} should be {sorted(case)}')
