Bubblesort
==========
A simple comparison sorting algorithm.


Algorithm
---------
Performs a series of traversals of an array until no swaps are needed.

In each traversal, compares the current item with the next, swapping them in place
if the first is greater than the next.

Across traversals, the largest items bubble up into their correct sorted position such that 
on the nth traversal, the top n items are already in sorted position.  



Analysis
--------
One of the worst performing sorting algorithms.  O(n^2).

In place and stable.

Requires minimal extra space to support temp variables.

Efficient implementations will account for the fact that each traversal results in the higher indexed items being correctly positioned.  

