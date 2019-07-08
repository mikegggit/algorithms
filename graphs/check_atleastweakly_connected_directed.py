#!/usr/bin/python

import copy
import random

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

  def deepCopy(this):
    return copy.deepcopy(this)

def checkAtLeastWeaklyConnected(g):
  """
  Creates a copy of g, converts to an undirected graph, and then performs a depth-first
  traversal, checking if all vertices are visited.  
  """
  ug = g.deepCopy()
  
  # Convert to undirected
  for v in ug.m.keys():
    for a in ug.m[v]:
      ug.m[a].add(v)

  # perform df traversal on random vertex
  vi = random.randint(0, len(ug.m.keys()) - 1)
 
  nodes=set()
  _traverseDF(ug, vi, nodes) 
  return len(nodes) == len(ug.m.keys())

def _traverseDF(g, cur, nodes):
  if cur in nodes:
    return
  nodes.add(cur)
  for child in g.m[cur]:
    _traverseDF(g, child, nodes)
 

def _traverseDFR(g, cur, nodes, visited):
  if cur in visited:
    return
  
if __name__ == "__main__":
  g = Graph()
  
  # First make a directed graph... 
  g.addEdge(0, 1)
  g.addEdge(1, 2)
  g.addEdge(2, 3)
  g.addEdge(3, 0)
  g.addEdge(2, 4)
  g.addEdge(4, 2)
  
  print(checkAtLeastWeaklyConnected(g))
  
  g.addEdge(5, 5)

  print(checkAtLeastWeaklyConnected(g))

