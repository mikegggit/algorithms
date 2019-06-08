Min / Max
=========
Algorithms for determining the min / max of a set of data

Algorithms
----------
Linear search of unsorted array
Sorting an array and choosing the min / max in O(1)
Min / max heap
Other?

Sorted structures
-----------------
If the source structure is already sorted, then the time complexity is O(1).

Sorting an input can be more expensive than using some other algorithm like simple linear search.

Linear search
-------------

Iteration is O(n)

Comparisons is O(n - 1), since you don't need to check the first item (it is the max / min as of that time)

If finding both min / max simultaneously, comparisons are O(2n - 2).


Assignment complexity varies depending on how input data is sorted.

In the best case, the data is sorted.

If finding min, and data is sorted in increasing order, only one min  assignment is required.

If finding max, the opposite is true.

If finding only one or the other, best case is O(1).  Worst case is (N).

If finding both simultaneously, best case is O(N).  Worst case is O(2n).



Min / Max heap
--------------
Building a heap is more expensive than simply scanning a list of items.  