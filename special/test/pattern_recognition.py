from unittest import TestCase

from unsolved.pattern_recognition import check_pattern

cases = [
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
    ),
    (
        "abc", "dog cat fish", True
    ),
    (
        "abcd", "dog cat fish fish", False
    )
]


class PatternRecognitionTest(TestCase):
    def test_cases(self):
        for pattern, text, expected in cases:
            self.assertEqual(expected, check_pattern(pattern, text),
                             msg=f'Output for {pattern}, {text} -> should be {expected}')
