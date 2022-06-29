# Graph: It consists finite set of vertices(or edges) and a set of edges which connect a pair of nodes.

class Graph:
    def __init__(self, gdict=None):
        # if gdict is empty/None then initialize gdict to the empty dictionary
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    
    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)

customDict = {
    'a': ['b', 'c'],
    'b': ['a', 'd', 'e'],
    'c': ['a', 'e'],
    'd': ['b', 'e', 'f'],
    'e': ['d', 'f'],
    'f': ['d', 'e']
}

graph = Graph(customDict)
graph.addEdge('e', 'c')
print(graph.gdict['e']) # ['d', 'f', 'c']