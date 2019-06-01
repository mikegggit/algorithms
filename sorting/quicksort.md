Quicksort
=========
A recursive comparison sorting algorithm.

Algorithm
---------
Given an unsorted array of values:
 
 - pick a pivot index
 - organize the array with the pivot positioned such that elements to the left of the pivot are <= the pivot value, those to the right are > the pivot value. 
 - recursively partition the sub-arrays until the base case is met, at which case the original array is sorted.


Implementation
--------------
Can be done in place indexing into the original array or using copies and subsequent concatenation.

In place is a slightly more complex algorithm but significantly more space efficient.

The partition is the most complex part of the algorithm.


Picking a pivot
---------------
A typical implementation will choose the last item in the subarray as the pivot.

Typically this will work fine.  

In cases where the original array is almost sorted already, this can lean to worst case complexity of n^2 (quadratic) since the partitioning step will not lead to evenly divided partitions, rather a single partition os size n - 1, which will itself need to be traversed in subsequent recursive calls.

To handle the case where the original array is already largely sorted, it can help to choose a pivot somewhere in the middle of the array.

Median of 3
-----------
A useful pivot selection algorithm.  Takes the median of first, last and middle items of an array to be sorted, with these three values sorted first.


Analysis
--------
Time complexity on average of O(n ln n)

Worst case O(n^2) if a bad pivot is chosen and the array is already largely sorted.

The worst case can be avoided by using a randomized pivot selection algorithm, like median of 3.

Since the algorithm is recursive, there could be a significant amount of time spend sorting small arrays.  A common optimization to avoid this is to switch to a non-recursive sorting algorithm like insertion sort when the array to be sorted is ~7-30 items.

