#!/usr/bin/python

class LL:
  head = None
  tail = None

  def __init__(this):
    pass

   
class Queue:
  front = None
  back = None
  size = 0
  ll = LL()

  class _Node:
    next = None
    def __init__(this, data):
      this.data = data

  def enqueue(this, data):
    n = Queue._Node(data)
    if not this.peek():
      this.ll.head = n
      this.ll.tail = this.ll.head
    else:
      temp = this.ll.tail
      temp.next = n
      this.ll.tail = n
    this.size += 1
    return n

  def dequeue(this):
    if this.size == 0:
      return None

    temp = this.ll.head
    this.ll.head = temp.next
    this.size -= 1
    return temp

  def peek(this):
    return this.ll.head

  def hasNext(this):
    return this.peek()

class BST:
  
  class _Node:
    l = None
    r = None
    data = None

    def __init__(this, data):
      this.data = data

  root = None
  
  def __init__(this):
    pass

  def insert(this, data):
    n = BST._Node(data)
   
    if not this.root:
      this.root = n
    else:
      cur = this.root
    
      while cur:
        if data < cur.data:
          if cur.l:
            cur = cur.l
          else:
             cur.l = n
             break
        else:
          if cur.r:
            cur = cur.r
          else:
            cur.r = n
            break

  def printLevelOrder(this):
    q = Queue()
    
    q.enqueue(this.root)
    q.enqueue("null")

    while q.hasNext():
      n = q.dequeue()
      if n.data == "null":
        print("")
        if q.hasNext():
          q.enqueue("null")
      else:
        print(n.data.data, end=" ")
        if n.data.l:
          q.enqueue(n.data.l)
        if n.data.r:
          q.enqueue(n.data.r)
    
if __name__ == "__main__":
  bst = BST()
  
  bst.insert(5)
  bst.insert(3)
  bst.insert(6)
  bst.insert(4)
  bst.insert(1)
  bst.insert(10)
  bst.insert(8)

  bst.printLevelOrder()

