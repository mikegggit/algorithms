#!/usr/bin/python3

import random
import math

class MinHeap:
 
  def __init__(this, capacity):
    this.capacity = capacity
    this.numItems = 0
    this.a = [None] * this.capacity

  def swap(this, i, j):
    temp = this.a[i]
    this.a[i] = this.a[j]
    this.a[j] = temp
 
  def heapifyUp(this):

    if this.numItems <= 1:
      return

    i = this.numItems - 1

    pi = this.parentIdx(i)
    while pi is not None and pi >= 0 and this.a[pi] > this.a[i]:
      this.swap(pi, i)
      i = pi 
      pi = this.parentIdx(i)

     
  def parentIdx(this, i):
    if i <= 0:
      return None

    return int(math.ceil(i/2) - 1)

  def leftIdx(this, i):
    return 2*i + 1

  def rightIdx(this, i):
    return 2*i + 2

  def hasChildren(this, i):
    return this.leftIdx(i) <= this.count() - 1

  def insert(this, data):
    this.numItems += 1
    this.a[this.numItems-1] = data
    this.heapifyUp()


  def count(this):
    return this.numItems

  def heapifyDown(this):
    if this.numItems <= 1:
      return

    i = 0

    while this.hasChildren(i):
      li = this.leftIdx(i)
      ri = this.rightIdx(i)

      if ri > this.count() - 1:
        if this.a[li] < this.a[i]:
          this.swap(li, i)
          i = li
        else:
          return
      else:
        if this.a[ri] < this.a[li] and this.a[ri] < this.a[i]:
          this.swap(ri, i)
          i = ri
        else:
          if this.a[li] < this.a[i]:
            this.swap(li, i)
            i = li
          else:
            return

  def remove(this):
    # Swap root w/ last el
    this.swap(0, this.numItems-1)
    v = this.a[this.numItems - 1]
    this.a[this.numItems - 1] = None
    this.numItems -= 1
    this.heapifyDown()
    return v


def search(a, t):
  l=0
  r = len(a) - 1
 
  while l < r:
    i = int((r - l) / 2) + l
    if a[i] == t:
      return i
    elif a[i] < t:
      l = i + 1
    else:
      r = i - 1

  return -1

if __name__ == "__main__":
  a = [random.randint(0, 100) for i in range(0, 10)]
  #a = [5,4,3,2,1]

  h = MinHeap(10)
  assert h.capacity == 10
  assert h.numItems == 0

  # Build heap
  for i in a:
    h.insert(i)

  i = 0

  sorted = [h.remove() for i in range(0, h.count())]
 
  print(sorted) 

  tgt = random.randint(0, 100)

  print("searching for {} in {}".format(tgt, sorted))
  print(search(sorted, tgt))
 
