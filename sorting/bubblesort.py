#!/usr/bin/python

def bubblesort(ar):
  first=True
  numSwaps = 0

  while first or numSwaps > 0:
    first = False
    numSwaps = 0
    for i in range(len(ar)-1):
      l=ar[i]
      r=ar[i+1]
      if l > r:
	numSwaps += 1
	temp = ar[i+1] #swap
	ar[i+1] = ar[i]
	ar[i] = temp
      i += 1
    print(ar)

if __name__ == "__main__":
  ar = [99999,234,341,2475,2,342,31,3146,457,856,8,546,34,543,453,77,67564,24,7]
  print(ar)
  bubblesort(ar)

