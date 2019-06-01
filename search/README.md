Searching
=========
Search algorithms.


Linear vs binary
----------------
A linear search involves traversing some linear structure like a linked list or array one at a time and searching for an item that equals the item being searched for.  Linear search starts at the first element of the dataset and proceeds one at a time until the item is found, or all items have been examined.

A binary search involves traversing a hierarchical reference-based structure like a tree and performing a sequence of comparisons between left and right neighbors.  The search starts at the middle, then proceeds left or right until either the item is found, or the search path has been examined.



Binary search
-------------
Commonly performed on arrays and binary search trees



Choosing between linear and binary
----------------------------------

Use linear if:
  ... data is unsorted and small in size
  ... you won't need to perform a search more than a few times

Use binary if:
  ... you have a lot of data
  ... the data is sorted 
  ...

If data is already sorted, use binary.


Analysis
--------
# Linear
Worst case is O(n) 
Average case is O(n)
Best case is O(1)

# Binary
Worst case is O(n)
Average case is O(ln(n))
Best case is O(1)

