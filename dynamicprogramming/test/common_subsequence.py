from unittest import TestCase

from src.common_subsequence import longest_common_subsequence

cases = [
    (
        "ABCDGH", "AEDFHR", 3
    ),
    (
        "AGGTAB", "GXTXAYB", 4
    )
]

class CommonSubsequenceTest(TestCase):
    def test_cases(self):
        for word1, word2, expected in cases:
            self.assertEqual(expected, longest_common_subsequence(word1, word2),
                             msg=f'Output for {word1}, {word2} -> should be {expected}')
