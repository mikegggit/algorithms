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

visited = {}

class Stack:
  head = None
    
  class _Node:
    data = None
    next = None

    def __init__(this, data):
      this.data = data

  def __init__(this):
    this.head = None

  def push(this, data):
    n = Stack._Node(data)

    if not this.head:
      this.head = n
    else:
      temp = this.head
      this.head = n
      this.head.next = temp

  def pop(this):
    if not this.head:
      return None

    temp = this.head
    this.head = this.head.next
    return temp 
  
def hasPathDFS(g, a, b):
  if not a in g.m:
    return False
  
  return _hasPathDFS(g, a, b, set()) 
  
def _hasPathDFS(g, a, b, visited):
 
  if a in visited:
    return False

  visited.add(a)

  if a == b:
    return True

  childPathExists = False
  for neighbor in g.m[a]:
    childPathExists = _hasPathDFS(g, neighbor, b, visited)
    if childPathExists:
      return True

  # no child path exists...
  return False
    
if __name__ == "__main__":
  g = Graph()

  g.addEdge(0, 1)
  g.addEdge(0, 2)
  g.addEdge(2, 0)
  g.addEdge(1, 2)
  g.addEdge(2, 3)
  g.addEdge(3, 3)

  g.print()  

  assert hasPathDFS(g, 0, 3)
  assert hasPathDFS(g, 1, 3)
  assert hasPathDFS(g, 1, 0)
  assert hasPathDFS(g, 0, 1)
  assert not hasPathDFS(g, 3, 0)
