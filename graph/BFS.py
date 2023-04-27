class Graph:
    def __init__(self,dict):
        if dict is None:
            dict={}
        self.dict=dict
    def addedge(self,vertex,edge):
        self.dict[vertex].append(edge)
    def BFS(self,vertex):
        visited=[vertex]
        queue=[vertex]
        while queue:
            p=queue.pop(0)
            print(p)
            for adjacent in self.dict[p]:
                if adjacent not in visited:
                    visited.append(adjacent)
                    queue.append(adjacent)
customdict={
    'a':['b','c'],
    'b':['a','d','e'],
    'c':['a','e'],
    'd':['b','e','f'],
    'e':['d','f'],
    'f':['d','e']
}

graph=Graph(customdict)
graph.BFS('a')


