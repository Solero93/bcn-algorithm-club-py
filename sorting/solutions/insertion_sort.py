"""
OBJECTIVE: Given a list, sort it from low to high using the BUBBLE SORT algorithm

Insertion sort is a simple sorting algorithm that works the way we sort playing cards in our hands.

Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the
    sorted list, and inserts it there.
It repeats until no input elements remain.

https://www.geeksforgeeks.org/insertion-sort/
"""


def insertion_sort(array: list) -> list:
    # Traverse through 1 to len(arr)
    for i in range(1, len(array)):
        key = array[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key

    return array
