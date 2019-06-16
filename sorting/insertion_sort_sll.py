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

  def add(this, data):
    n = None
    if this.size == 0:
      n = Node(data)
      this.head = n
      this.tail = this.head
    else:
      temp = this.tail
      n = Node(data)
      this.tail = n
      temp.next = this.tail
    this.size += 1
    return n

  def addAll(this, *data):
    for i in data:
      this.add(i)

  def __str__(this):
    s = ""

    n = this.head
    while n:
      s += " -> "
      s += str(n.data) 
      n = n.next

    return s

  def sort(this):
    """Using insertion sort.

    Uses two pointers, one to track the current item to be inserted,
    the other scanning the ll from left to right for the insertion position.
    """

    print("sort")

    # ll is either empty or size 1
    if this.size <= 1:
      return 

    cur = this.head.next
   
    prev = None 
    while cur:
      search = this.head
      searchp = None
      done = False
      while search and search != cur and not done:
        if cur.data < search.data:       # found insertion point...
          # insert cur before search
          if not searchp:                # we have a new head
            oldhead = this.head
            oldcurnext = cur.next
            this.head = cur
            cur.next = oldhead
            if oldhead.next == cur:      # head needs to point to something new
              oldhead.next = oldcurnext

            if not oldcurnext:
              prev.next = None
              return

            if prev:
              cur = prev
              prev.next = oldcurnext

          else:                          # insert after p, before i
            oldcurnext = cur.next
            cur.next = searchp.next
            searchp.next = cur

            if not oldcurnext:
              prev.next = None
              return

            if prev:
              cur = prev
              prev.next = oldcurnext

          done = True

        else:                            # haven't found insertion pt yet
          searchp = search 
          search = search.next
        
      prev = cur 
      cur = cur.next
      

if __name__ == "__main__":
  l = LL()

  #l.addAll(1,2,3)
  #l.addAll(22, 99, 27)
  #l.addAll(99, 27, 22)

  for i in range(20):
    n = random.randint(0, 100)
    l.add(n)
  
  print("presort={}".format(l))
  l.sort()
  print("sorted={}".format(l))
