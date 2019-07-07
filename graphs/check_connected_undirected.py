#!/usr/bin/python

import random

class Graph:

  m = None

  def __init__(this):
    this.m = {}

  def addEdge(this, a, b):
    if not a in this.m:
      this.m[a] = set()
    this.m[a].add(b)
    if not b in this.m:
      this.m[b] = set()
    this.m[b].add(a)
       

  def print(this):
    print("\n".join([str(i[0]) + " -> " + ", ".join(str(j) for j in i[1]) for i in this.m.items()]))

def checkConnected(g):
  """
  Performs a depth-first traversal starting at a random node and
  checks whether or not all vertices have been visited.

  Returns True if all vertices are visited while performing a depth-first traversal
  starting at a random vertex.
  """
 
  root = random.randint(0, len(g.m.keys()) - 1)

  nodes = []
  _checkConnected(g, root, set(), nodes) 
  return len(g.m.keys()) == len(nodes)

def _checkConnected(g, v, visited, nodes):
  if v in visited:
    return 

  nodes.append(v)

  visited.add(v)
  for i in g.m[v]:
    _checkConnected(g, i, visited, nodes)

if __name__ == "__main__":
  g = Graph()

  # First unconnected...
  g.addEdge(1, 2)
  g.addEdge(2, 3)
  g.addEdge(1, 3)
  g.addEdge(4, 5)
  g.addEdge(5, 6)
  g.addEdge(6, 7)
  g.addEdge(7, 8)
  g.addEdge(8, 4)
 
  g.print() 

  print(checkConnected(g))

  # ...then add an edge to connect the two components, making it connected.
  g.addEdge(2, 4)

  g.print()
  
  print(checkConnected(g)) 
