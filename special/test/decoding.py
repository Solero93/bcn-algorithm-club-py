from unittest import TestCase

from src.decoding import decode_string

cases = [
    (
        "3[a]", "aaa"
    ),
    (
        "3[a]2[bc]", "aaabcbc"
    ),
    (
        "3[a2[c]]", "accaccacc"
    ),
    (
        "2[abc]3[cd]ef", "abcabccdcdcdef"
    )
]


class DecodingTest(TestCase):
    def test_cases(self):
        for encoded, expected in cases:
            self.assertEqual(expected, decode_string(encoded),
                             msg=f'Output for {encoded} -> should be {expected}')
