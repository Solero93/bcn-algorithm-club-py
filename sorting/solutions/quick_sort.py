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


# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
def partition(array, low, high):
    i = (low - 1)  # index of smaller element
    pivot = array[high]  # pivot

    for j in range(low, high):
        # If current element is smaller than or
        # equal to pivot
        if array[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return (i + 1)


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort
def quick_sort(array, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(array, low, high)

        # Separately sort elements before
        # partition and after partition
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)
