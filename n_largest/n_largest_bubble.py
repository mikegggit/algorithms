#!/usr/bin/python

import random

def swap(a, i, j):
  temp = a[i]
  a[i] = a[j]
  a[j] = temp

def nlargest(a, k):
  """Returns n largest elements from a using bubble sort n times
  
  Complexity is O(n * k).  Since bubble sort is only run k times.

  Normally, bubble sort runs in O(N^2)."""

  i = 0 
 
  while i < k:
    j = 0
    
    while j < len(a) - 1:
      if a[j] > a[j + 1]:
        swap(a, j, j + 1)
      j += 1
  
    i += 1    

  return (a[len(a)-k:])

if __name__ == "__main__":
  a = [random.randint(0, 10000) for i in  range(30)]
  print(a)
  print(a)
  print(nlargest(a, 2))
