"""
OBJECTIVE: Given a list, sort it from low to high using the SELECTION SORT algorithm

The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order)
    from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.

1) The subarray which is already sorted.
2) Remaining subarray which is unsorted.

In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted subarray
    is picked and moved to the sorted subarray.

https://www.geeksforgeeks.org/selection-sort/
"""


def selection_sort(array: list) -> list:
    # Traverse through all array elements
    for i in range(len(array)):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j

        # Swap the found minimum element with the first element
        array[i], array[min_idx] = array[min_idx], array[i]
    return array
