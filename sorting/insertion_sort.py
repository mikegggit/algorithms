#!/usr/bin/python

def insertionSort(ar):

  for i in range(1, len(ar)):
    v = ar[i]
    j = i

    while j > 0 and ar[j - 1] > v:
      ar[j] = ar[j - 1]
      j -= 1

    ar[j] = v


if __name__ == "__main__":
  ar = [43,46,26,7,63,451,65,457,658,3,76,35,1,54,65,8,745,1361,7]
  print(ar)
  insertionSort(ar)
  print(ar)

