class Graph:
    def __init__(self,gdict):
        if gdict is None:
            gdict={}
        else:
            self.gdict=gdict
    def addEdge(self,vertex,edge):
        self.gdict[vertex].append(edge)

customdict={
    'a':['b','c'],
    'b':['a','d'],
    'c':['a','e'],
    'd':['b','e','f'],
    'e':['c','d','f'],
    'f':['d','e']
}

graph=Graph(customdict)
graph.addEdge('b','e')
print(graph.gdict('b'))