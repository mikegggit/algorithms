#!/usr/bin/python

import random

def min_max(a):
  """Finds min/max of an array using simple linear search"""
  min = None
  max = None
  
  for i in a:
    if min is None:
      min = i
    else:
      if i < min:
        min = i

    if max is None:
      max = i
    else:
      if i > max:
        max = i

  return (min, max)

if __name__ == "__main__":
  a = [random.randint(0, 100) for i in range(0, 100)]

  print(a)
  print(min_max(a))  
