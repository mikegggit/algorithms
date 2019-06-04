Heapsort
========
Sorting algorithm based on the heap data-structure.  

Algorithm
---------
To sort a collection of N items, first build a min/max heap.  Then repeatedly remove the root element, re-heapifying the structure following every removal.  The removed items are iteratively added to an array, resulting in a sorted array.

It is a comparison sort.  


Analysis
--------
Building the heap is O(n), with the heap being created initially as an empty heap (array), and built sequentially inserting elements in O(1) each.

Removal is O(1) for removing the item and swapping the root element w/ the last element, then O(ln n) to reheapify the heap (sift down the newly swapped root el), finally removing the last el, resulting in a sorting time of O(n ln n).

# Space
Additional space of size n is required to store the items being removed from the heap.

Building of the heap is done in place.

Uses a complete binary tree represented as an array, with links between nodes implemented mathematically.

Usage
-----
Frequently mentioned as an alternative to quicksort to avoid quicksort's worst case time of O(n^2).  A properly implemented quicksort will rarely ever have this issue, so it's not clear that this is a good reason to use it.

Problems involving k smallest / largest items in a collection.

Sorting a nearly sorted array (to avoid worst case scenarios using something like a BST).

