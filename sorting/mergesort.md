Mergesort
=========
A comparison sort algorithm for sorting arrays.

Algorithm
---------
Recursively split an array into subarrays, then merge them in order to create a sorted result.

Analysis
--------
Requires additional space to hold the merge target.

The split process is O(logn)

The merge process is O(n).

The total process is O(nlogn), even in worst case.  

When concerned about worst case performance, prefer mergesort to quicksort.  Mergesort performs the same whether or not the input is nearly sorted.  

Also a stable sort.  If stability is important, prefer mergesort to quicksort and heapsort, which aren't stable.
It does have a space penalty allocating for the target array.

The quadratic worst case of quicksort _can_ be minimized by using a randomized pivot selection algorithm, like median of 3.



Implementation
--------------
For each recursive merge, allocates a new array equal to the combined size of the inputs.

