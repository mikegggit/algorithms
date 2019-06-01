#!/usr/bin/python

import random

class Node:
  next = None
  data = None

  def __init__(self, v=None):
    self.data = v
  
  def __iter__(self):
    node = self

    while node:
      yield node
      node = node.next
 
def ls(ll, v):
  if ll:
    if ll.data == v:
      return True
  
    cur = ll
   
    while cur.next:
      if cur.next.data == v:
        return True
      else:
        cur = cur.next

    return False

if __name__ == "__main__":
  ll = None
  cur = None
  for i in range(0, 10):
    if ll is None:
      ll = Node(random.randint(0,100))
      cur = ll
    else:
      cur.next = Node(random.randint(0, 100))
      cur = cur.next
    
  for n in ll:
    print(n.data)   
  print(ls(ll, 30))    

 
