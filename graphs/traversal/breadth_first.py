#!/usr/bin/python

class Graph:

  m = None

  def __init__(this):
    this.m = {}

  def addEdge(this, a, b):
    if not a in this.m:
      this.m[a] = set()
    this.m[a].add(b)

  def print(this):
    print("\n".join([str(i[0]) + " -> " + ", ".join(str(j) for j in i[1]) for i in this.m.items()]))


class Queue:
  head = None
  tail = None
 
  class _Node:
    data = None
    next = None

    def __init__(this, data):
      this.data = data

  def __init__(this):
    this.head = None
    this.tail = this.head

  def enqueue(this, data):
    n =Queue._Node(data)

    if not this.head:
      this.head = n
      this.tail = this.head
    else:
      temp = this.tail
      this.tail = n
      temp.next = this.tail

  def dequeue(this):
    if not this.head:
      return None

    temp = this.head
    this.head = this.head.next
    return temp 
 
  def hasNext(this):
    return this.head 

def printBreadthFirst(g, root):
  
  visited = set()

  nextQueue = Queue()

  nextQueue.enqueue(root)
  nodes=[] 
  while nextQueue.hasNext():
    n = nextQueue.dequeue()
    
    if n.data in visited:
      continue

    nodes.append(n.data)

    visited.add(n.data)

    for child in g.m[n.data]:
      nextQueue.enqueue(child)

  print(", ".join([str(n) for n in nodes]))
  
 
   
if __name__ == "__main__":
  g = Graph()

  g.addEdge(0, 1)
  g.addEdge(0, 2)
  g.addEdge(2, 0)
  g.addEdge(1, 2)
  g.addEdge(2, 3)
  g.addEdge(3, 3)

  g.print()  
  printBreadthFirst(g, 0)
  printBreadthFirst(g, 1)
  printBreadthFirst(g, 2)
  printBreadthFirst(g, 3)
