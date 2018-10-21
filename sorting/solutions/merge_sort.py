"""
OBJECTIVE: Given a list, sort it from low to high using the MERGE SORT algorithm

Merge sort is one of the most efficient sorting algorithms. It works on the principle of Divide and Conquer.
Merge sort repeatedly break down a list into several sublists until each sublist consists of a single element
    and merging those sublists in a manner that results into a sorted list.

A merge sort works as follows:
1. Divide the unsorted list into n sublists, each comprising 1 element (a list of 1 element is supposed sorted).
2. Repeatedly merge sublists to produce newly sorted sublists until there is only 1 sublist remaining.
    This will be the sorted list.

Merging of two lists done as follows:
The first element of both lists is compared.
If sorting in ascending order, the smaller element among two becomes a new element of the sorted list.
This procedure is repeated until both the smaller sublists are empty and the newly combined sublist
    covers all the elements of both the sublists.


https://www.geeksforgeeks.org/merge-sort/
"""


# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]
def merge(array, left, middle, right):
    n1 = middle - left + 1
    n2 = right - middle

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = array[left + i]

    for j in range(0, n2):
        R[j] = array[middle + 1 + j]

        # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = left  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        array[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        array[k] = R[j]
        j += 1
        k += 1


# l is for left index and r is right index of the
# sub-array of arr to be sorted
def merge_sort(array, left, right):
    if left < right:
        # Same as (l+r)/2, but avoids overflow for
        # large l and h
        m = (left + (right - 1)) / 2

        # Sort first and second halves
        merge_sort(array, left, m)
        merge_sort(array, m + 1, right)
        merge(array, left, m, right)