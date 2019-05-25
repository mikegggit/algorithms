#!/usr/bin/python

def swapWithNext(ar, i):
  """swaps array element at i with element at i + 1"""
  temp = ar[i+1]
  ar[i+1] = ar[i]
  ar[i] = temp

def bubblesort_optimized(ar):

  first = True
  l = len(ar)
  while first or numSwaps > 0:
    first = False
    for i in range(0, l):
      numSwaps = 0
      for j in range(0, l - 1 - i):
	if ar[j] > ar[j+1]:
          swapWithNext(ar, j)
	  numSwaps += 1

      print(ar)
      if numSwaps == 0:
        return

if __name__ == "__main__":
  ar = [99999, 234, 341, 2475, 2, 342, 31, 3146, 457, 856, 8, 546, 34, 543, 453, 77, 67564, 24, 7]
  print(ar)
  bubblesort_optimized(ar)
  
