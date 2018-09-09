"""
/**
 * 10 points
 *
 *
 * https://leetcode.com/problems/range-sum-query-immutable/description/
 *
 *
 * Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
 *
 *
 * Example:
 * Given nums = [-2, 0, 3, -5, 2, -1]
 *
 *
 * sumRange(0, 2) -> 1
 * sumRange(2, 5) -> -1
 * sumRange(0, 5) -> -3
 *
 *
 * Note:
 * You may assume that the array does not change.
 * !!!!!There are many calls to sumRange function!!!!!!
 */
"""
from typing import List


class Sums:
    def __init__(self, nums: List[int]):
        self.nums: List[int] = nums

    def sum_range(self, i, j):
        return 0
