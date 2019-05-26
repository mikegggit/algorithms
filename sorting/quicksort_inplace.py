#!/usr/bin/python
def swap(ar, i, j):
      print("swap [l={}, r={}]".format(ar[i], ar[j]))
      temp = ar[i]
      ar[i] = ar[j]
      ar[j] = temp
   
def partition(ar, istart, iend):
  """Picks the last element of the subarray of boundaries defined by istart 
  and iend as a pivot.

  Maintains two pointers, using each to traverse array from opposite directions as part
  of the process of establishing left and right partitions.

  During traversal, swaps values referred to by left and right pointers when left
  refers to an element > the pivot and right refers to an element <= the pivot.

  Once the pointers refer to the same element, swaps the pivot value for the value
  ferferred to by the pointers, returning the pointer index.
  """

  print("partition [ar={}, istart={}, iend={}]".format(ar, istart, iend))
  if iend <= istart:
    return 

  # get the pivot
  pivotIdx = iend
  pivot = ar[iend]

  # init left and right pointers used to determine eventual partition index
  il=istart
  ir=iend - 1

  while il <= ir:
    if ar[il] <= pivot:
      il += 1
    elif ar[ir] > pivot:
      ir -= 1
    else:
      swap(ar, il, ir)
    print(ar) 
  if ar[il] > ar[pivotIdx]:
    swap(ar, il, pivotIdx)
  print(ar)
  return il
 
def quicksort(ar, istart, iend):
  """an in place quicksort implementation.

  istart - the start of the subarray
  iend - the end of the subarray
  """

  if istart >= iend:
    return ar

  i = partition(ar, istart, iend)

  print("partition result={}".format(i))
  quicksort(ar, istart, i-1)
  quicksort(ar, i, iend)

if __name__ == "__main__":
  #a = [5,4,9,1]
  a = [12,21,456,5678,86,343,728,31,54,428,5,32,8,9,764,435,10]
  print(a)
  quicksort(a, 0, len(a) - 1)
  print(a)
