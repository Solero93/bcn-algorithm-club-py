from functools import reduce
from typing import List

"""
/**
 * 10 points
 *
 *
 * Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.
 * Return a list of all possible strings we could create.
 *
 *
 * Examples:
 * Input: S = "a1b2"
 * Output: ["a1b2", "a1B2", "A1b2", "A1B2"]
 *
 *
 * Input: S = "3z4"
 * Output: ["3z4", "3Z4"]
 *
 *
 * Input: S = "12345"
 * Output: ["12345"]
 */
"""


def letter_case_permutations(string_to_permute: str) -> List[str]:
    case_permutations = [""]
    for character in string_to_permute:
        current_level_permutations = []
        for permutation in case_permutations:
            is_letter = character.isalpha()
            if is_letter:
                current_level_permutations.append(permutation + character.upper())
                current_level_permutations.append(permutation + character.lower())
            else:
                current_level_permutations.append(permutation + character)
        case_permutations = current_level_permutations
    return case_permutations


def letter_case_permutation_pythonic(string_to_permute: str) -> List[str]:
    return list(reduce(lambda current_level_permutations, new_character: reduce(lambda x, y: x + y, map(
        lambda x: [x + new_character.upper(), x + new_character.lower()] if x.isalpha() else x + new_character,
        current_level_permutations)), string_to_permute))
