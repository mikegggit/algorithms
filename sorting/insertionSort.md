Insertion Sort
==============
Simple algorithm for sorting an array of comparable items.

Algorithm
---------
While iterating over the elements of an array, maintain a sorted partition and an unsorted partition.  The sorted partition is to the left of the current item.  For each item, insert into the sorted partition at the appropriate position, shifting greater elements to the right to make space.  If the last element in the sorted partition is less than the current item, the current item is in the correct position, and no insertion is required.

Analysis
--------
Quadratic performance on average.  

Where the array to be sorted is nearly sorted, can be more efficient and approach O(n).  Unlike selection sort, in which every element in the unsorted partition need be compared to determine the minimum, comparisons are limited to those elements greater than the current item plus one more.

Constant space complexity.  All swaps are done in place and little additional memory is required to handle variables for storing temp state.

Good for small datasets, generally ~ 10 items, or between 7 and 50 items.  In these cases, typically faster than even quicksort.  Some quicksort / mergesort algorithms switch to insertion sort when a partition is <= 10.


