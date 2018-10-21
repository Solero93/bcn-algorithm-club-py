"""
OBJECTIVE: Given a list, sort it from low to high using the BUBBLE SORT algorithm

Bubble Sort is the simplest sorting algorithm that works
    by repeatedly swapping the adjacent elements if they are in wrong order.

https://www.geeksforgeeks.org/bubble-sort/
"""


def bubble_sort(array: list) -> list:
    n = len(array)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array
