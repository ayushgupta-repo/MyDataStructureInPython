# Graph: It consists finite set of vertices(or edges) and a set of edges which connect a pair of nodes.

class Graph:
    def __init__(self, gdict=None):
        # if gdict is empty/None then initialize gdict to the empty dictionary
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    
    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)

    def bfs(self, vertex):
        visited = [vertex] # to keep track of visited nodes
        queue = [vertex] # to do enqueue and dequeue operations on vertex

        # while queue is not empty
        while queue:
            deVertex = queue.pop(0) # dequeue operation of particular vertex stored in queue
            print(deVertex)

            # to check adjacentVertex of dequeued Vertex visited or not and perform specific operation
            for adjacentVertex in self.gdict[deVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    queue.append(adjacentVertex)

customDict = {
    'a': ['b', 'c'],
    'b': ['a', 'd', 'e'],
    'c': ['a', 'e'],
    'd': ['b', 'e', 'f'],
    'e': ['d', 'f'],
    'f': ['d', 'e']
}

graph = Graph(customDict)
# graph.addEdge('e', 'c')
# print(graph.gdict['e']) # ['d', 'f', 'c']

graph.bfs('a')