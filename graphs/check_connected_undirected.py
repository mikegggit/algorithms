#!/usr/bin/python

class Graph:

  m = None

  def __init__(this):
    this.m = {}

  def addEdge(this, a, b):
    if not a in this.m:
      this.m[a] = set()
    this.m[a].add(b)

  def addVertex(this, a):
    if a in this.m:
      return
    this.m[a] = set()

  def print(this):
    print("\n".join([str(i[0]) + " -> " + ", ".join(str(j) for j in i[1]) for i in this.m.items()]))

def isConnected(g):
  """
  Simply performs a depth-first traversal and determines whether or not
  all nodes have been visited. 
  """


if __name__ == "__main__":
  # First test an unconnected graph...
  ug = Graph()
  ug.addEdge(
  
