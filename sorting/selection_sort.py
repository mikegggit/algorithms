#!/usr/bin/python

"""
Given an array of unsorted data, divide the array into sorted and unsorted partitions.

Iteratively build the sorted partition from unsorted by traversing the unsorted partition
in total and identifying the smallest item.  Then, swap the first item in the unsorted partition w/ the smallest item in unsorted, then grow the sorted partition.
"""

def getMinIdx(ar, startIdx):
  min = None
  minIdx = None
  i = startIdx

  while i < len(ar):
    if not min:
      min = ar[i]
      minIdx = i
    elif ar[i] < min:
      min = ar[i]
      minIdx = i

    i += 1
  
  return minIdx

def selectionSort(ar):
  sortedEndIdx = 0

  l = len(ar)
  i = 0

  while i < l:
    minIdx = getMinIdx(ar, i)
    if ar[minIdx] < ar[i]:
      temp = ar[i]
      ar[i] = ar[minIdx]
      ar[minIdx] = temp
    i += 1
 
        
if __name__ == "__main__":
  ar = [6,3,4,7,3,1,3,8,10,235,6,7,5752,47,3,153,5247,7]
  print(ar)
  selectionSort(ar)
  print(ar)
  
