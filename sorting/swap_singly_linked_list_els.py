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

def swap(ll, l, r):
  """swaps l w/ r.
  l and r are references kept by client to nodes themselves, not the contained values.
  """

  if l == r:
    return

  if not ll.head or ll.size == 1:
    return

  # find l
  n = ll.head
  prev = None
  x, y, prevX, prevY = None, None, None, None

  while n and (not x or not y) :
    if n == l:
      prevX = prev
      x = n
    elif n == r:
      prevY = prev
      y = n

    prev = n
    n = n.next
          
  if not x or not y:
    print("Either x or y is not in the list")
    return
  
  print("Found nodes [l={}, r={}]".format(x, y))
  if not prevX:            # l is the head
    ll.head = y
  else:
    prevX.next = y

  oldYnext = y.next
  y.next = x.next
 
  prevY.next = x
  x.next = oldYnext

if __name__ == "__main__":
 
  ll = LL()
  n7 = ll.add(7)
  n6 = ll.add(6)
  n5 = ll.add(5)
  n4 = ll.add(4)
  n3 = ll.add(3)
  n2 = ll.add(2)
  n1 = ll.add(1)


  print(ll)
  swap(ll, n6, n2)
  print(ll) 
  swap(ll, n7, n1)
  print(ll) 
