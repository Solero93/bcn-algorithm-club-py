"""
OBJECTIVE: Given a list, sort it from low to high using the HEAP SORT algorithm

Heap sort is a comparison based sorting technique based on Binary Heap data structure.
    It is similar to selection sort where we first find the maximum element and place the maximum element at the end.
    We repeat the same process for remaining element.

What is a Binary Heap?

Let us first define a Complete Binary Tree.
A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled,
    and all nodes are as far left as possible (Source Wikipedia)

A Binary Heap is a Complete Binary Tree where items are stored in a special order such that value in a parent node
    is greater(or smaller) than the values in its two children nodes.
The former is called as max heap and the latter is called min heap.
    The heap can be represented by binary tree or array.


Why array based representation for Binary Heap?
Since a Binary Heap is a Complete Binary Tree, it can be easily represented as array
    and array based representation is space efficient.
If the parent node is stored at index I, the left child can be calculated by
    2 * I + 1 and right child by 2 * I + 2 (assuming the indexing starts at 0).

Heap Sort Algorithm for sorting in increasing order:
1. Build a max heap from the input data.
2. At this point, the largest item is stored at the root of the heap.
    Replace it with the last item of the heap followed by reducing the size of heap by 1.
    Finally, heapify the root of tree.
3. Repeat above steps while size of heap is greater than 1.

https://www.geeksforgeeks.org/heap-sort/
"""


def heap_sort(array: list) -> list:
    return []
