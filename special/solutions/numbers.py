from typing import List

"""
/**
 * 1 point
 *
 *
 * A self-dividing number is a number that is divisible by every digit it contains.
 *
 *
 * For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
 *
 *
 * Also, a self-dividing number is not allowed to contain the digit zero.
 *
 *
 * Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.
 *
 *
 * Example 1:
 * Input:
 * left = 1, right = 22
 * Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
 *
 *
 * Note:
 *
 *
 * The boundaries of each input argument are 1 <= left <= right <= 10000.
 */
"""


def self_dividing_numbers(left: int, right: int) -> List[int]:
    self_diving_array = []
    for candidate in range(left, right + 1):
        does_divide = True
        for digit in [int(character) for character in str(candidate)]:
            if digit == 0 or candidate % digit != 0:
                does_divide = False
                break
        if does_divide:
            self_diving_array.append(candidate)
    return self_diving_array


def self_dividing_numbers_pythonic(left: int, right: int) -> List[int]:
    return list(
        filter(lambda x: all([int(digit) != 0 and x % int(digit) == 0 for digit in str(x)]), range(left, right + 1)))
