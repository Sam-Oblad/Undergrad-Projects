# Graph ADT

- in this project I implemented my own data structure of a weighted diagraph. 

### Methods for my data type:

- add_vertex(label): add a vertex with the specified label. Return the graph. label must be a string or raise ValueError
- add_edge(src, dest, w): add an edge from vertex src to vertex dest with weight w. Return the graph. validate src, dest, and w: raise ValueError if not valid.
- float get_weight(src, dest): Return the weight on edge src-dest (math.inf if no path exists, raise ValueError if src or dest not added to graph).
- dfs(starting_vertex): Return a generator for traversing the graph in depth-first order starting from the specified vertex. Raise a ValueError if the vertex does not exist. Be sure to traverse a vertex's neighbors in alphabetic order.
- bfs(starting_vertex): Return a generator for traversing the graph in breadth-first order starting from the specified vertex. Raise a ValueError if the vertex does not exist. Be sure to traverse a vertex's neighbors in alphabetic order.
- dsp(src, dest): Return a tuple (path length , the list of vertices on the path from src to dest). If no path exists, return the tuple (math.inf, empty list.)
- dsp_all(src): Return a dictionary of the shortest weighted path between src and all other vertices using Dijkstra's Shortest Path algorithm. In the dictionary, the key is the the destination vertex label, the value is a list of vertices on the path from src to dest inclusive.
- __str__: Produce a string representation of the graph that can be used with print(). The format of the graph should be in GraphViz dot notation, which is explained at https://graphs.grevian.org/example and many other places on the web. See Figure 1.