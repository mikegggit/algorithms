Pigeonhole sort
===============
Distribution sort where inputs capable of being associated w/ a numeric representaion are assigned to buckets associated w/ their numeric representaiton.  


Algorithm
---------

1) Create bucket array capable of holding inputs.

2) Iterate over inputs, assigning each input to a bucket

2) Iterate over non-empty buckets to form a sorted representation


Analysis
--------
Appropriate where the input range isn't too large relative to the number of elements within.  In other words, appropriate for inputs where the range is approximately equal to the number of items.  

The wider tha range of values, the more memory is required to hold the buckets, and the larger the number of elements must be visited to find non-empty buckets to be moved to the sorted array.

The more input elements, the more items must be iterated over to be moved into a bucket.

The larger the range of input values is to the number of input elements, the more time is wasted iterating over empty buckets.  

Performance is O(n + N), where n is the number of elements, and N is the range of element values.
