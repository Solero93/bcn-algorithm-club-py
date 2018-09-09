from typing import List, Tuple
from unittest import TestCase

from unsolved.decoding import decode_string


cases: List[Tuple[str, str]] = [
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
    def test_decoding_cases(self):
        for encoded, expected in cases:
            self.assertEqual(expected, decode_string(encoded), msg=f'{encoded} -> should be {expected}')
