from unittest import TestCase

from src.edit_distance import edit_distance


cases = [
    (
        "geek", "gesek", 1
    ),
    (
        "cat", "cut", 1
    ),
    (
        "sunday", "saturday", 3
    ),
    (
        "good", "goodbye", 3
    ),
    (
        "something", "something", 0
    )
]


class EditDistanceTest(TestCase):
    def test_cases(self):
        for word1, word2, expected in cases:
            self.assertEqual(expected, edit_distance(word1, word2),
                             msg=f'Output for {word1}, {word2} -> should be {expected}')
