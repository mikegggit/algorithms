#!/usr/bin/python

import random

def min(a):
  min = None

  for i in a:
    if min is None:
      min = i
    else:
      if i < min:
        min = i

  return min
 
if __name__ == "__main__":
  a = [random.randint(0, 100) for i in range(0, 20)]

  print(a)
  print(min(a))
