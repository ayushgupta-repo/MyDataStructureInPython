# Using Bellman Ford because Dijkstra not work with Negative-weighted directed graph
# NOTE: It goes to decrease cost everytime traversing so to avoid this we keep tracker
# and it provides the existence of negative cycle.

# In worst case scenario Negative-weighted directed graph will reach every nodes at
# (V-1) times iteration. So, after exceding it will again reduce the cost due to negative
# cycle. So, we iterate upto (V-1) times only

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.nodes = []

    def addNode(self, value):
        self.nodes.append(value)
    
    def addEdge(self, s, d, w):
        self.graph.append([s, d, w])

    def printSolution(self, dist):
        print('Shortest Distance: ')
        for key, value in dist.items():
            print(' ' + key, ': ', value)
        
    def bellmanFord(self, src):
        dist = {i: float('Inf') for i in self.nodes} # setting cost of every node to infinity
        dist[src] = 0 # upating cost of initial node to zero

        for _ in range(self.V-1):
            for s, d, w in self.graph:
                if dist[s] != float('Inf') and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w
        
            # getting check loop
            for s, d, w in self.graph:
                if dist[s] != float('Inf') and dist[s] + w < dist[d]:
                    print('Graph contains negative cycle')
        
        self.printSolution(dist)

# Checking
g = Graph(5)

g.addNode('A')
g.addNode('B')
g.addNode('C')
g.addNode('D')
g.addNode('E')

g.addEdge('A', 'C', 6)
g.addEdge('A', 'D', 6)
g.addEdge('B', 'A', 3)
g.addEdge('C', 'D', 1)
g.addEdge('D', 'C', 2)
g.addEdge('D', 'B', 1)
g.addEdge('E', 'B', 4)
g.addEdge('E', 'D', 2)

g.bellmanFord('E')