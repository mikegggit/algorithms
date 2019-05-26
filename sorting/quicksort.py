#!/usr/bin/python
def swap(ar, i, j):
      print("swap [l={}, r={}]".format(ar[i], ar[j]))
      temp = ar[i]
      ar[i] = ar[j]
      ar[j] = temp
   
def partition(ar):
  """Picks the last element of the array as a pivot.

  Maintains two pointers, using each to traverse array from opposite directions as part
  of the process of establishing left and right partitions.

  During traversal, swaps values referred to by left and right pointers when left
  refers to an element > the pivot and right refers to an element <= the pivot.

  Once the pointers refer to the same element, swaps the pivot value for the value
  ferferred to by the pointers, returning the pointer index.
  """

  print("partition [ar={}]".format(ar))
  if len(ar) == 0:
    return []

  # get the pivot
  pivotIdx = len(ar) - 1
  pivot = ar[pivotIdx]

  # init left and right pointers used to determine eventual partition index
  il=0
  ir=len(ar) - 2

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
 
def quicksort(ar):
  """sorts ar using quicksort algorithm. 

  recursively partitions ar around a pivot such that elements <= the pivot value are
  in the left partition, the rest to the right.
  """
  if len(ar) <= 1:
    return ar

  i = partition(ar)

  print("partition result={}".format(i))
  return quicksort(ar[0:i]) + [ar[i]] + quicksort(ar[i+1:])

if __name__ == "__main__":
  #a = [5,4,9,1]
  a = [12,21,456,5678,86,343,728,31,54,428,5,32,8,9,764,435,10]
  print(a)
  sorted = quicksort(a)
  print(sorted)
