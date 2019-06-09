#!/usr/bin/python

import random

def swap(a, i, j):
  temp = a[i]
  a[i] = a[j]
  a[j] = temp

def nlargest(a, n):
  """Returns n largest elements from a using bubble sort n times"""

  i = 0 
 
  while i < n:
    j = 0
    
    while j < len(a) - 1:
      if a[j] > a[j + 1]:
        swap(a, j, j + 1)
      j += 1
  
    i += 1    

  return (a[len(a)-n:])

if __name__ == "__main__":
  a = [random.randint(0, 10000) for i in  range(30)]
  print(a)
  print(a)
  print(nlargest(a, 2))
