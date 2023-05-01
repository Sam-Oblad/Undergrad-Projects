import math
import heapq
from typing import Tuple, List

class Vertex:
    def __init__(self, label: str):
        self.label = label
    def __lt__(self, other):
        return self.label < other.label

class Graph():
    def __init__(self):
        self.vertices = {}
        self.adjacencyList = {}
        self.edgeWeights = {}

    def add_vertex(self, label: str):
        if type(label) == str:
            newV = Vertex(label)
        else:
            raise ValueError("Label is not type str")
        self.vertices[label] = newV
        self.adjacencyList[newV] = []
        return self.adjacencyList

    def add_edge(self, src: str, dest: str, w):
        try:
            src = self.vertices[src]
            dest = self.vertices[dest]
            self.edgeWeights[(src,dest)] = w
            self.adjacencyList[src].append(dest)
        except KeyError:
            raise ValueError("Invalid vertex passed")
        

    def get_weight(self, src: str, dest: str):
        src = self.vertices[src]
        dest = self.vertices[dest]
        if src not in self.vertices.values() and dest not in self.vertices.values():
                raise ValueError("Vertex doesn't exsist in graph")
        for vertexPair in self.edgeWeights:
            if (src,dest) == vertexPair:
                return float(self.edgeWeights[vertexPair]) 
            else:
                return math.inf

    def dfs(self, starting_vertex: str):
        starting_vertex = self.vertices[starting_vertex]
        if starting_vertex not in self.vertices.values():
            raise ValueError("Vertex does not exist")
        vertex_stack = [starting_vertex]
        visited_set = set()

        while len(vertex_stack) > 0:
            vertex_stack.sort(key=lambda vertex: vertex.label, reverse=True)
            current_vertex = vertex_stack.pop()
            if current_vertex not in visited_set:
                yield current_vertex.label
                visited_set.add(current_vertex)
                for adjacent_vertex in self.adjacencyList[current_vertex]:
                    vertex_stack.append(adjacent_vertex)

    def bfs(self, starting_vertex):
        discoveredSet = set()
        frontierQueue = []
        starting_vertex = self.vertices[starting_vertex]
        if starting_vertex not in self.vertices.values():
            raise ValueError("Vertex does not exist")
        frontierQueue.append(starting_vertex)
        discoveredSet.add(starting_vertex)
        while (len(frontierQueue) > 0):
            current_vertex = frontierQueue.pop(0)
            yield current_vertex.label
            for adjacentVertex in self.adjacencyList[current_vertex]:
                if adjacentVertex not in discoveredSet:
                    frontierQueue.append(adjacentVertex)
                    discoveredSet.add(adjacentVertex)

    def dsp(self, src: str, dest: str) -> Tuple[int, List[str]]:
        src = self.vertices[src]
        dest = self.vertices[dest]
        if src not in self.vertices.values() or dest not in self.vertices.values():
            raise ValueError("Source or destination vertex does not exist")
        distance = {vertex: math.inf for vertex in self.vertices.values()}
        previous = {vertex: None for vertex in self.vertices.values()}
        distance[src] = 0
        heap = [(0, src)]
        while heap:
            (dist, current_vertex) = heapq.heappop(heap)
            if current_vertex == dest:
                path = []
                while current_vertex is not None:
                    path.insert(0, current_vertex.label)
                    current_vertex = previous[current_vertex]
                return (int(dist), path)
            if dist > distance[current_vertex]:
                continue
            for adjacent_vertex in self.adjacencyList[current_vertex]:
                edge_weight = self.edgeWeights[(current_vertex, adjacent_vertex)]
                new_distance = dist + edge_weight
                if new_distance < distance[adjacent_vertex]:
                    distance[adjacent_vertex] = new_distance
                    previous[adjacent_vertex] = current_vertex
                    heapq.heappush(heap, (new_distance, adjacent_vertex))
        return (math.inf, [])

    def dsp_all(self, src):
        src = self.vertices[src]
        if src not in self.vertices.values():
            raise ValueError("Source vertex does not exist")
        distance = {vertex: math.inf for vertex in self.vertices.values()}
        previous = {vertex: None for vertex in self.vertices.values()}
        distance[src] = 0
        heap = [(0, src)]
        while heap:
            (dist, current_vertex) = heapq.heappop(heap)
            for adjacent_vertex in self.adjacencyList[current_vertex]:
                edge_weight = self.edgeWeights[(current_vertex, adjacent_vertex)]
                new_distance = dist + edge_weight
                if new_distance < distance[adjacent_vertex]:
                    distance[adjacent_vertex] = new_distance
                    previous[adjacent_vertex] = current_vertex
                    heapq.heappush(heap, (new_distance, adjacent_vertex))
        result = {}
        for vertex in self.vertices.values():
            if vertex == src:
                result[vertex.label] = [vertex.label]
            elif math.isinf(distance[vertex]):
                result[vertex.label] = None
            else:
                path = []
                current_vertex = vertex
                while current_vertex is not None:
                    path.insert(0, current_vertex.label)
                    current_vertex = previous[current_vertex]
                result[vertex.label] = path
        return result

    def __str__(self):
        outputString = "digraph G {\n"
        for vertex in self.edgeWeights:
            outputString += f"   {vertex[0].label} -> {vertex[1].label} [label=\"{self.edgeWeights[(vertex[0],vertex[1])]}\",weight=\"{self.edgeWeights[(vertex[0],vertex[1])]}\"];\n"
        outputString += "}"
        return outputString
        
def main():
    G = Graph()
    G.add_vertex("A")
    G.add_vertex("B")
    G.add_vertex("C")
    G.add_vertex("D")
    G.add_vertex("E")
    G.add_vertex("F")
    G.add_edge("A", "B", 2.0)
    G.add_edge("A", "F", 9.0)
    G.add_edge("B", "C", 8.0)
    G.add_edge("B", "D", 15.0)
    G.add_edge("B", "F", 6.0)
    G.add_edge("C", "D", 1.0)
    G.add_edge("E", "D", 3.0)
    G.add_edge("E", "C", 7.0)
    G.add_edge("F", "B", 6.0)
    G.add_edge("F", "E", 3.0)
    print(G)

    print("Starting DFS with vertex A")
    for vertex in G.dfs("A"):
        print(vertex, end = "")
    print()

    print("Starting BFS with vertex A")
    for vertex in G.bfs("A"):
        print(vertex, end="")
    print()

    print("Starting DSP")
    print(G.dsp("A", "F"))

    print("Starting DSP ALL from A")
    for vertex, path in G.dsp_all("A").items():
        if path != None:
            string = "{"
            string += (f"{vertex}: {path}")
            string += "}"
            print(string)
if __name__ == "__main__":
    main()