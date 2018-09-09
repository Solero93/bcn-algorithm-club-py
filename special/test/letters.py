from unittest import TestCase

from src.letters import letter_case_permutations

cases = [
    (
        "a1b2", ["a1b2", "a1B2", "A1b2", "A1B2"]
    ),
    (
        "3z4", ["3z4", "3Z4"]
    ),
    (
        "1234", ["1234"]
    )
]


class LettersTest(TestCase):
    def test_cases(self):
        for string_to_permute, expected in cases:
            self.assertCountEqual(expected, letter_case_permutations(string_to_permute),
                                  msg=f'Output for {string_to_permute} -> should be {expected}')
