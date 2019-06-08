Counting Sort
=============
A type of hashing sort where each there is a single bucket for each possible input value.


Algorithm
---------

Given a set of data to be sorted...

1) Create a set of buckets.

   Requires determining the range of items to be sorted.

   The first index in the buckets will be 0, but really represent the min of the range.

   Similarly, the last index in the buckets will represent its value plus the max of the range.

   In other words, there will be (max - min) + 1 buckets

2) For each item in the dataset, assign the item to a bucket, denoting the assignment by incrementing the bucket value by 1.

   This is a type of hashing, where the hash value is the value of the item itself (plus min), and the entry is the number of instances having the hash value.

   If there are multiple instances of a value, the entry for a bucket is > 1

3) Process the bucket list such that each entry is added to the value of the preceding bucket.

4) Create an output array of size equal to input array.

5) Iteratively process the input data...

   For each input value, retrieve the insertion index from bucket, which is the bucket value - 1.

   Insert input into target and reduce bucket value by 1.



Analysis
--------
An unstable sort.

Not in place.

Requires additional space to hold buckets and target sorted data.

More memory is required the wider the range of possible input values.  

The number of buckets is typically equal to the range of input values.

If the max value is 1000 and the min is 5, and there are only three values 5, 400, and 1000, we still need an array of size 996.


Usage
-----
Valuable where memory is cheap.

Only useful for data that can be hashed to a number.

The running time is O(n + k) given a range of n and k input items.  

Each of the k items is assigned a bucket, then the range of buckets is iterated over to reduce into a sorted output.
