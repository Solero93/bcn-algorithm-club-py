from unittest import TestCase

from src.builtin_sort_list import builtin_sort_list
from test.fixtures import test_cases


class BuiltInSortTest(TestCase):
    def test_sort(self):
        for case in test_cases:
            self.assertEqual(builtin_sort_list(case), sorted(case),
                             msg=f'{case} should be {sorted(case)}')
