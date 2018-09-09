from collections import Counter
from typing import List

"""
/**
 * 15 points
 *
 *
 * Given a non-empty array of integers, return the k most frequent elements.
 *
 *
 *
 *
 * For example,
 * Given [1,1,1,2,2,3] and k = 2, return [1,2].
 *
 *
 * Note:
 * You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
 * Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
 */
"""


def most_frequent(numbers: List[int], k: int) -> List[int]:
    counter = {}
    for number in numbers:
        counter[number] = counter.get(number, 0) + 1
    return sorted(counter, key=lambda key: counter[key], reverse=True)[:k]


def most_frequent_with_counter(numbers: List[int], k: int) -> List[int]:
    return [elem[0] for elem in Counter(numbers).most_common(k)]
