#!/usr/bin/python

import random

def getRange(a):
  if a is None:
    return None

  if len(a) == 1:
    return (a[0], a[0])

  lo = None
  hi = None

  for i in a:
    if lo is None:
      lo = i
    else:
      if i < lo:
        lo = i

    if hi is None:
      hi = i
    else:
      if i > hi:
        hi = i

  return (lo, hi) 


class LL:
  head = None
  tail = None
  size = 0

  def __init__(this, data = None):
    this.append(data)

  def append(this, data):
    n = Node(data)
    if this.head is None:
      this.head = Node(data)
      this.tail = this.head
    else:
      temp = this.tail
      this.tail = n
      temp.next = this.tail

    this.size += 1

  def isEmpty(this):
    return this.size == 0
 
class Node:

  next = None
  
  def __init__(this, data=None):
    this.data = data
     
  

def pigeon(a):
  r = getRange(a)
 
  # build buckets
  buckets = [None] * ((r[1] - r[0]) + 1)

  lo = r[0]
 
  for i in a:
    if buckets[i - lo] is None:
      buckets[i - lo] = LL(i)
    else:
      buckets[i - lo].append(i)

  sorted = [None] * len(a)

  j = 0

  for i in buckets:
    if i is not None:
      n = i.head
      while n is not None:
        sorted[j] = n.data 
        j += 1
        n = n.next

  return sorted

if __name__ == "__main__":
  a = [random.randint(0, 100) for i in range(0, 10)]
  print(a)
  sorted = pigeon(a)
  print(sorted)
