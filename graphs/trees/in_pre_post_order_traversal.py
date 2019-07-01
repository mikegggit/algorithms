#!/usr/bin/python

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

  def printInOrder(this, n=None):
    if not n:
      n = this.root
    if n.l:
      this.printInOrder(n.l)
    print(n.data)
    if n.r:
      this.printInOrder(n.r)

  def printPreOrder(this, n=None):
    if not n:
      n = this.root

    print(n.data)
    if n.l:
      this.printPreOrder(n.l)
    if n.r:
      this.printPreOrder(n.r)

  def printPostOrder(this, n=None):
    if not n:
      n = this.root

    if n.l:
      this.printPostOrder(n.l)
    if n.r:
      this.printPostOrder(n.r)
    print(n.data)

if __name__ == "__main__":
  bst = BST()
  
  bst.insert(5)
  bst.insert(3)
  bst.insert(6)
  bst.insert(4)
  bst.insert(1)
  bst.insert(10)
  bst.insert(8)

  bst.printInOrder()
  bst.printPreOrder()
  bst.printPostOrder()

