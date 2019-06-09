#!/usr/bin/python

import random

class Node:
  next = None
  def __init__(this, data):
    this.data = data

class LL:
  def __init__(this):
    this.head = None
    this.tail = None
    this.size = 0

  def append(this, data):
    n = Node(data)
    if not this.head:
      this.head = n
      this.tail = this.head
    else:
      temp = this.tail
      this.tail = n
      temp.next = n
    this.size += 1

  def print(this):
    n = this.head
    while n:
      print(n.data, end=' -> ')
      n = n.next
    print("")


def bubblesort(ll):
  """Sorts linked list in place by swapping node values"""
  if not ll or ll.size == 1:
    return ll

  numSwaps = 0
  first = True
  while first or numSwaps > 0:
    first = False
    numSwaps = 0
    l = ll.head
    while l.next:
      r = l.next
      if l.data > r.data:
        temp = l.data
        l.data = r.data
        r.data = temp
        numSwaps += 1
      l = l.next

if __name__ == "__main__":
  a = [random.randint(0, 1000) for i in range(3)]

  ll = LL()
  for i in a:
    ll.append(i)

  ll.print()  

  bubblesort(ll)

  ll.print()
