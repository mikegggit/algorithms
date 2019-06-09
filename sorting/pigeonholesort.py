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

  def __init__(this):
    pass

  def append(this, data):
    n = Node(data)
    temp = this.tail
    this.tail = n
    temp.next = this.tail

  
class Node:

  next = None
  
  def __init__(this, data=None):
    this.data = data
     
  

def pigeon(a):
  r = getRange(a)
 
  # build buckets
  buckets = [LL()] * ((r[1] - r[0]) + 1)

  lo = r[0]
 
  for i in a:
    buckets[i - lo].append(i)

  sorted = [None] * len(a)

  j = 0

  for i in buckets:
    if i is not None:
      sorted[j] = i
      j += 1

  return sorted

if __name__ == "__main__":
  a = [random.randint(0, 100) for i in range(0, 10)]
  print(a)
  sorted = pigeon(a)
  print(sorted)
