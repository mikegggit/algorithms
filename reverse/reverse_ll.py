#!/usr/bin/python


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

  def print(this):
    n = this.head
    while n:
      print(n.data, end=' -> ')
      n = n.next
    print("")
 
  def reverse(this):
    """Reverses a singly linked list"""
   
    prev = None
    curr = None
    next = None
 
    curr = this.head
    tail = curr
    while curr is not None:
      temp = curr.next
      curr.next = prev
      prev = curr
      curr = temp

    this.head = prev
    this.tail = tail
 
if __name__ == "__main__":
  ll = LL()
  s = "Hello there I am not reversed!"
  for l in s:
    ll.append(l)
  ll.print()
  ll.reverse()
  ll.print()

