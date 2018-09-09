from typing import List, Tuple
from unittest import TestCase

from unsolved.pattern_recognition import check_pattern

cases: List[Tuple[str, str, bool]] = [
    (
       "a", "dog dog", False
    ),
    (
        "aa", "dog", False
    ),
    (
        "abba", "dog cat cat dog", True
    ),
    (
        "abba", "dog cat cat fish", False
    ),
    (
        "aaaa", "dog cat cat dog", False
    ),
    (
        "abba", "dog dog dog dog", False
    ),
    (
        "aaaa", "dog dog dog dog", True
    )
]


class PatternRecognitionTest(TestCase):
    def test_pattern_recognition_cases(self):
        for pattern, text, expected in cases:
            self.assertEqual(expected, check_pattern(pattern, text), msg=f'{pattern}, {text} -> should be {expected}')
