#!/usr/bin/python

import random

def swap(ar, i, j):
  print("swap [i={}, ar[i]={}, j={}, ar[j]={}]".format(i, ar[i], j, ar[j]))
  temp = ar[i]
  ar[i] = ar[j]
  ar[j] = temp

def getPivotMOT(ar, starti, endi):
  """Returns a pivot to use in subsequent partition.

  Uses median of three strategy.  Updates the array in place as a side effect,
  swapping the values at first, last and middle indexes such that they are
  themselves in sorted order.
  """
  if endi - starti <= 1:
    return endi
  
  pi = int((endi - starti) / 2) + starti

  if ar[endi] < ar[starti]:
    swap(ar, endi, starti)
  
  if ar[pi] < ar[starti]:
    swap(ar, pi, starti)

  if ar[endi] < ar[pi]:
    swap(ar, endi, pi)
  return pi

def partition(ar, starti, endi):
  
  pi = getPivotMOT(ar, starti, endi)
 
  # move pivot to the end of the subarray
  swap(ar, endi, pi)

  pivot = ar[endi]

  li = starti
  ri = endi - 1
 
  while li <= ri:
    if ar[li] <= pivot:           # search for left swap index
      li += 1
    elif ar[ri] > pivot:
      ri -= 1
    else:
      swap(ar, li, ri)
  
  if ar[li] > ar[endi]:
    swap(ar, li, endi)

  return li

def qs(ar, start, end):
  """recursively sorts ar between start and end in place"""
  if end - start <= 0:
    return ar

  pi = partition(ar, start, end)
  qs(ar, start, pi-1)
  qs(ar, pi + 1, end)

if __name__ == "__main__":
  ar=[1,2,3,4,5,9,6,7,8,345,10,11,657,12,13,14,677,15,18,16,17]
  print(ar)
  qs(ar, 0, len(ar) - 1)
  print(ar)
