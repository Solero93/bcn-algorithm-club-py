"""
/**
 * 1 point
 *
 *
 * You're given strings J representing the types of stones that are jewels,
 * and S representing the stones you have.  Each character in S is a type of stone you have.
 * You want to know how many of the stones you have are also jewels.
 *
 *
 * The letters in J are guaranteed distinct, and all characters in J and S are letters.
 * Letters are case sensitive, so "a" is considered a different type of stone from "A".
 */
"""


def num_jewels_in_stones(jewels: str, stones: str) -> int:
    number_of_jewels = 0
    for stone in stones:
        if stone in jewels:
            number_of_jewels += 1
    return number_of_jewels


def num_jewels_in_stones_pythonic(jewels: str, stones: str) -> int:
    return sum(map(lambda stone: 1 if stone in jewels else 0, stones))
