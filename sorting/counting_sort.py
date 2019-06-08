#!/usr/bin/python

import random

def getRange(a):
  """Use simple linear search to find range of the array"""
  if a is None:
    return None
 
  if len(a) == 1:
    return (a[0], a[0])

  lo = None
  hi = None
  for i in a:
    if lo is None:
      lo = i
    else:
      if i < lo:
        lo = i

    if hi is None:
      hi = i
    else:
      if i > hi:
        hi = i
  return (lo, hi)
  
def countSort(a):
  minmax = getRange(a)
  lo = minmax[0]
  hi = minmax[1]

  print("lo={}, hi={}".format(lo, hi))
  buckets = [0] * ((hi - lo) + 1)

  # Build buckets
  for i in a:
    buckets[i - lo] += 1
  
  # Sum buckets
  for i in range(0, len(buckets)):
    if i == 0:
      continue
    
    buckets[i] = buckets[i] + buckets[i - 1]
  
  # build sorted result
  sorted = [None] * len(a)
  for i in a:
    idx = buckets[i - lo] - 1
    sorted[idx] = i
    buckets[i-lo] -= 1

  return sorted
if __name__ == "__main__":
  a = [random.randint(-1000, 1000) for i in range(0, 100)]
  print(a)
  sorted = countSort(a)

  print(sorted)
