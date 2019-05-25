Selection Sort
==============
A simple algorithm for sorting an array of comparable items in place.

Algorithm
---------
For each element in the array, visits each subsequent element to determine the minimum value of the remaining items.  If that item is less than the element of the array, swaps the items.

Analysis
--------
Quadratic as elements of the array must be repeatedly scanned for each item.  Later iterations are less expensive, however still quadratic with some factor applied in total.

