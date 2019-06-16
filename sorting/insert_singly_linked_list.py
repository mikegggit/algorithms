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

  def add(this, data):
    n = Node(data)
    if not this.head:
      this.head = n
      this.tail = this.head
    else:
      temp = this.tail
      this.tail = n
      temp.next = n
    this.size += 1
    return n

  def addAll(this, *data):
    for d in data:
      this.add(d)

  def insertBefore(this, data, dataAfter):
    """Inserts new node w/ data before node having value dataAfter."""

    if this.size == 1:
      raise Exception("list is empty")

    prev = None

    refNode= this.head
    new = Node(data)
    while refNode:                    # find reference node
      if refNode.data == dataAfter:   # insert before this node
        print("here")
        if not prev:                  # ...this is the head node
          this.head = new
          this.head.next = refNode
        else:
          oldNext = prev.next
          prev.next = new
          new.next = oldNext
        return
      else:                           # this isn't the node we're looking for
        prev = refNode
        refNode = refNode.next 

  def insertAfter(this, data, dataBefore):
    """inserts data after first node having value dataBefore"""
   
    if this.size == 1:
      raise Exception("list is empty")

    refNode = this.head 
    new = Node(data)

    while refNode:                    
      if refNode.data == dataBefore:   # insert after this node...
        oldNext = refNode.next
        refNode.next = new
        new.next = oldNext
        return
      else:
        refNode = refNode.next 
        

  def __str__(this):
    if not this.head:
      return "(empty)"

    s = " -> "

    n = this.head
    while n.next:
      s += str(n.data)
      s += " -> "
      n = n.next
    s += str(n.data)
    s += " -> "
    return s

if __name__ == "__main__":
  ll = LL()

  ll.add(1)
  ll.addAll(4,5,6,7)

  print(ll)

  ll.insertBefore(3, 4)
  print(ll)
  ll.insertAfter(2, 1)
  print(ll)
  ll.insertBefore(0, 1)
  print(ll)
  ll.insertAfter(8, 7)
  print(ll)
