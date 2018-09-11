from unittest import TestCase

from src.common_subsequence import longest_common_subsequence

cases = [
    (
        "a", "a", "a"
    ),
    (
        "ab", "a", "a"
    ),
    (
        "aba", "ab", "ab"
    ),
    (
        "abac", "bbab", "ba"
    ),
    (
        "abbcddd", "abbecddd", "cddd"
    ),
    (
        "abcd", "bacdb", "cd"
    )
]


class CommonSubsequenceTest(TestCase):
    def test_cases(self):
        for word1, word2, expected in cases:
            self.assertEqual(expected, longest_common_subsequence(word1, word2),
                             msg=f'Output for {word1}, {word2} -> should be {expected}')
