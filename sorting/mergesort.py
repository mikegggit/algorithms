#!/usr/bin/python

import math

def merge(l, r):
  """Traverses l and r, comparing elements along the way such that they are copied
  appropriately into target array in order.
  """
  print("merge [l={}, r={}]".format(l, r))
  t = [None] * (len(l) + len(r))
  ti = 0
 
  i, j = 0, 0

  while i < len(l) and j < len(r):
    if l[i] <= r[j]:
      t[ti] = l[i]
      i += 1
    else:
      t[ti] = r[j]
      j += 1
    ti += 1

  # copy remaining items from one of either l or r...
  if i < len(l):
    while i < len(l):
      t[ti] = l[i]
      i += 1
      ti += 1
  else:
    while j < len(r):
      t[ti] = r[j]
      j+= 1
      ti += 1

  return t

def mergesort(ar):
  print("mergesort [ar={}]".format(ar))
  if len(ar) == 1:
    return ar

  # split ar into left and right arrays
  pi = int(math.ceil(len(ar) / 2))

  ls = mergesort(ar[0:pi])
  print("ls={}".format(ls))
  rs = mergesort(ar[pi:])
  print("rs={}".format(rs))
  merged = merge(ls, rs)
  
  return merged

if __name__ == "__main__":
  ar=[38, 79, 72, 22, 3, 39, 40, 18, 92, 85, 43, 40, 6, 51, 83, 41, 27, 43, 53, 6]
  print(ar)
  sorted = mergesort(ar)
  print(sorted) 
