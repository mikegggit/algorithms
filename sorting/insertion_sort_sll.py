#!/usr/bin/python

import random

class Node:
  next = None

  def __init__(this, data):
    this.data = data
    this.next = None

class LL:
  head = None
  tail = None
  size = 0

  def __init__(this):
    this.size = 0

  def append(this, data):
    if this.size == 0:
      this.head = Node(data)
      this.tail = this.head
    else:
      temp = this.tail
      n = Node(data)
      this.tail = n
      temp.next = this.tail
    this.size += 1

  def insertionSort(this):
    sorted = LL()
    
    n = this.head
    
    # iterate over items in unsorted list 
    while n is not None:
      if sorted.head is None:
        sorted.head = Node(n.data)
      elif sorted.head.data >= n.data:
        temp = sorted.head
        sorted.head = Node(n.data)
        sorted.head.next = temp
      else:
        search = sorted.head
        
        while search.next is not None and n.data > search.next.data:
          search = search.next
    
        # either search.next is empty, or n should be inserted before it
        if not search.next:
          search.next = Node(n.data)
        else:
          temp = search.next
          search.next = Node(n.data)
          search.next.next = temp 

      n = n.next
    return sorted

  def print(this):
    n = this.head
 
    while n is not None:
      print(n.data, end=" -> ")
      n = n.next 

    print("")

if __name__ == "__main__":
  l = LL()
  for i in range(100):
    n = random.randint(0, 100)
    l.append(n)
 
  l.print()
  sorted = l.insertionSort()
  sorted.print()
