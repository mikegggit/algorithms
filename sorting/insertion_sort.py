#!/usr/bin/python

def insertionSort(ar):

  for i in range(1, len(ar)):
    v = ar[i]
    j = i

    while j > 0 and ar[j - 1] > v:
      ar[j] = ar[j - 1]
      j -= 1

    # if the item to the right of the sorted array(ar[i]) was already in the correct position, this
    # will be a no-op
    ar[j] = v


if __name__ == "__main__":
  #ar = [43,46,26,7,63,451,65,457,658,3,76,35,1,54,65,8,745,1361,7]
  #ar = [2,3,4,5,6,7,8,9,10,1]
  ar = [1,2,3,4,5,6,7,8,9,10, 1]
  print(ar)
  insertionSort(ar)
  print(ar)

