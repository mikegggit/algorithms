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

def printDepthFirst(g, root):
  if not root in g.m:
    raise Error("root not in graph")

  nodes = []
  _printDepthFirst(g, root, set(), nodes)
  print(nodes)
  print(" > ".join([str(n) for n in nodes]))

def _printDepthFirst(g, node, visited, nodes):
  if node in visited:
    return

  visited.add(node)
  nodes.append(node)
  for child in g.m[node]:
    _printDepthFirst(g, child, visited, nodes)

  return
 
def printBreadthFirst(g, root):
  pass
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

  printDepthFirst(g, 0)
  printDepthFirst(g, 1)
  printDepthFirst(g, 2)
  printDepthFirst(g, 3)

