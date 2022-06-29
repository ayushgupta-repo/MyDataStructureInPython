# SSSP: Single Source Shortest Path Problem

class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    
    def bfs(self, start, end):
        # start is source and end is destination
        # creating queue to store paths
        queue = []
        queue.append([start])

        # while queue is not empty
        while queue:
            path = queue.pop(0)

            # to get lastVisitedNode
            node = path[-1]

            # checking if the lastVisitedNode is the destination or not
            if node == end:
                return path
            
            # otherwise go for adjacentVertices check
            for adjacent in self.gdict.get(node, []):
                new_path = list(path)
                new_path.append(adjacent) # adding adjacentVertex in new_path
                queue.append(new_path) # adding new path

customDict = {
    'a': ['b', 'c'],
    'b': ['d', 'g'],
    'c': ['d', 'e'],
    'd': ['f'],
    'e': ['f'],
    'g': ['f']
}

g = Graph(customDict)

print(g.bfs('a', 'e'))