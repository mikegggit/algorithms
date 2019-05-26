#!/usr/bin/python

import random

def swap(ar, i, j):
  print("swap [i={}, ar[i]={}, j={}, ar[j]={}]".format(i, ar[i], j, ar[j]))
  temp = ar[i]
  ar[i] = ar[j]
  ar[j] = temp

def partition(ar, starti, endi):
  
  pi = random.randint(starti, endi)
  
  # move pivot to the end of the subarray
  swap(ar, endi, pi)

  pivot = ar[endi]

  li = starti
  ri = endi - 1
 
  print("partition [pivot={}, li={}, ri={},ar={}]".format(pivot, li, ri, ar[starti: endi +1])) 
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
  if end - start <= 0:
    return ar

  pi = partition(ar, start, end)

  qs(ar, start, pi)
  qs(ar, pi + 1, end)


if __name__ == "__main__":
  ar=[1,2,3,4,5,9,6,7,8,345,10,11,657,12,13,14,677,15,18,16,17]
  print(ar)
  qs(ar, 0, len(ar) - 1)
  print(ar)
