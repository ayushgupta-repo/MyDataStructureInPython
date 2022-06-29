# Topological Sort Algorithm
# This time we are creating graph using adjacency list but using collections library
from collections import defaultdict

class Graph:
    def __init__(self, numberOfVertices):
        self.graph = defaultdict(list) # using adjacency list
        self.numberOfVertices = numberOfVertices

    def addEdge(self, vertex, edge):
        self.graph[vertex].append(edge)

    # helper method for topologicalSort
    def topologicalSortUtil(self, v, visited, stack):
        # add the currentVertex into visited list
        visited.append(v)

        # now traversing through each adjacent vertices of the currentVertex
        for i in self.graph[v]:
            if i not in visited:
                self.topologicalSortUtil(i, visited, stack)
        
        # adding currentVertex in stack
        stack.insert(0, v) # it works as LIFO

    # main method
    def topologicalSort(self):
        # initializing lists to be used
        visited = []
        stack = []

        # now traversing through keys of dictionary means vertices
        for k in list(self.graph):
            if k not in visited:
                self.topologicalSortUtil(k, visited, stack)

        print(stack)

customGraph = Graph(8) # numberOfVertices passed
customGraph.addEdge('A', 'C')
customGraph.addEdge('C', 'E')
customGraph.addEdge('E', 'H')
customGraph.addEdge('E', 'F')
customGraph.addEdge('F', 'G')
customGraph.addEdge('B', 'D')
customGraph.addEdge('B', 'C')
customGraph.addEdge('D', 'F')

customGraph.topologicalSort()