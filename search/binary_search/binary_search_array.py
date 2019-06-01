#!/usr/bin/python

import random;

def swap(a, i, j):
  temp = a[i]
  a[i] = a[j]
  a[j] = temp

def partition(a, i, j):
  
  li = i
  ri = j - 1
 
  pi = j
  pivot = a[j]
 
  while li <= ri:
    if a[li] <= pivot:
      li += 1
    elif a[ri] >= pivot:
      ri -= 1
    else:
      swap(a, li, ri)

  if a[li] > pivot:
    swap(a, li, pi)

  return li
 
def qs(a, i, j):
  if j <= i:
    return
  
  pi = partition(a, i, j)
  qs(a, i, pi-1)
  qs(a, pi+1, j)

def search(a, v):

  lo = 0
  hi = len(a) - 1

  print("search [v={}]".format(v))

  while hi > lo:
    mid = int((hi - lo) / 2) + lo
    print("...lo={}, mid={}, hi={}, candidate={}".format(lo, mid, hi, a[mid]))
    if a[mid] == v:
      print("...found!")
      return mid
    
    if a[mid] > v:
      hi = mid - 1
    else:
      lo = mid + 1

  print("...missing:(")
  
if __name__ == "__main__":
  
  a = [random.randint(0, 100) for i in range(0, 100)]
  qs(a, 0, len(a) - 1) 
  v = random.randint(0, 100)
  search(a, v)
