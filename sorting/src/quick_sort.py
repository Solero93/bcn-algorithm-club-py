"""
OBJECTIVE: Given a list, sort it from low to high using the QUICK SORT algorithm

Quicksort first divides a large array into two smaller sub-arrays: the low elements and the high elements.
Quicksort can then recursively sort the sub-arrays.

The steps are:

1. Pick an element, called a pivot, from the array.
2. Partitioning: reorder the array so that all elements with values less than the pivot come before the pivot,
    while all elements with values greater than the pivot come after it (equal values can go either way).
    After this partitioning, the pivot is in its final position. This is called the partition operation.
3. Recursively apply the above steps to the sub-array of elements with smaller values
    and separately to the sub-array of elements with greater values.

The base case of the recursion is arrays of size zero or one, which are in order by definition,
    so they never need to be sorted.

https://www.geeksforgeeks.org/quick-sort/
"""


def quick_sort(array: list) -> list:
    return []
