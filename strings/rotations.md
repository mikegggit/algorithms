Rotations
=========
Process of updating a sequence such that each element is moved some number of positions position left (counter-clockwise) or right (clockwise).

In a left rotation, each element is shifted to the left.  For a rotation by one position, the first element is moved to the end of the sequence.  

In a right rotation, each element is shifted to the right.  For a rotation by one position, the last element is moved to the beginning of the sequence.


What can be rotated?
--------------------
Arrays, strings, matrixes


Use cases
---------
Arrays and strings: ???

Matrixes: Spreadsheets, graphics.


In-place or not
---------------
Arrays can be rotated in place using a minimal amount of extra storage.

Strings are more problematic in that they typically are immutable structures, and hence require additional storage to create a copy.

In place rotations are possible only for square matrixes.  


Analysis
--------
Rotation of an array of size n has complexity O(n).

For arrays, the space complexity is O(1)

For strings, the space complexity is O(n).

