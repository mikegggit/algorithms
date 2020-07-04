Graph Traversal
===============
Refers to how nodes / edges in a graph are navigated.

Usage
-----
For when you want to want to perform some operation on all nodes of a graph, or want to search for particular nodes to process.

Differences w/ tree traversal
-----------------------------
Trees are undirected acyclical graphs.  Because a graph can contain cycles, graph traversal requires tracking which nodes have already been visited, and that each node is visited only once.

Because a tree is guaranteed acyclic and of known structure, there's no need to track the number of nodes visited.  However, with a graph, because there is no guarantee of connectivity, the total number of nodes in the graph and the number of nodes visied thus far is necessary, as the traversal must continue until the number of nodes visited equals the number of nodes in the graph.

Depth First
-----------

Breadth First
-------------