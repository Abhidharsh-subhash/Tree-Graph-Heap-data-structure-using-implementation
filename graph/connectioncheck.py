class Graph:
    def __init__(self,dict):
        if dict is None:
            dict={}
        else:
            self.dict=dict
    def addvertex(self,vertex):
        if vertex not in self.dict.keys():
            self.dict[vertex]=[]
            return True 
        return False
    def addedge(self,vertex1,vertex2):
        if vertex1 in self.dict.keys() and vertex2 in self.dict.keys():
            if vertex2 not in self.dict[vertex1]:
                self.dict[vertex1].append(vertex2)
            if vertex1 not in self.dict[vertex2]:
                self.dict[vertex2].append(vertex1)
            return True
        return False
    def removevertex(self,vertex):
        if vertex in self.dict.keys():
            for other in self.dict[vertex]:
                self.dict[other].remove(vertex)
            del self.dict[vertex]
            return True
        return False
    def removeedge(self,vertex1,vertex2):
        if vertex1 in self.dict.keys() and vertex2 in self.dict.keys():
            self.dict[vertex1].remove(vertex2)
            self.dict[vertex2].remove(vertex1)
            return True
        return False
    def connectioncheck(self,start,end):
        visited=[start]
        queue=[start]
        while queue:
            x=queue.pop(0)
            for adjacent in self.dict[x]:
                if adjacent not in visited:
                    visited.append(adjacent)
                    queue.append(adjacent)
        if end in visited:
            return True
        return False
customdict={
    'a':['b','c'],
    'b':['a','d'],
    'c':['a','e'],
    'd':['b','e','f'],
    'e':['c','d','f'],
    'f':['d','e']
}
graph=Graph(customdict)
print(graph.connectioncheck('a','e'))