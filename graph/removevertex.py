class Graph:
    def __init__(self):
        self.adj={}
    def addvertex(self,vertex):
        if vertex not in self.adj.keys():
            self.adj[vertex]=[]
            return True 
        return False
    def addedge(self,vertex1,vertex2):
        if vertex1 in self.adj.keys() and vertex2 in self.adj.keys():
            self.adj[vertex1].append(vertex2)
            self.adj[vertex2].append(vertex1)
            return True
        return False
    def removeedge(self,vertex1,vertex2):
        if vertex1 in self.adj.keys() and vertex2 in self.adj.keys():
            try:
                self.adj[vertex1].remove(vertex2)
                self.adj[vertex2].remove(vertex1)
            except ValueError:
                pass
            return True 
        return False
    def removevertex(self,vertex):
        if vertex in self.adj.keys():
            for others in self.adj[vertex]:
                self.adj[others].remove(vertex)
            del self.adj[vertex]
            return True
        return False
    def display(self):
        for vertex in self.adj:
            print(vertex,':',self.adj[vertex])
    
graph=Graph()
graph.addvertex('a')
graph.addvertex('b')
graph.addvertex('c')
graph.addvertex('d')
graph.addedge('a','b')
graph.addedge('a','c')
graph.addedge('b','c')
graph.addedge('b','d')
graph.addedge('d','a')
graph.display()
print('removeedge')
graph.removeedge('a','c')
graph.removeedge('d','a')
graph.display()
graph.addedge('a','c')
graph.addedge('d','a')
print('removevertex')
graph.removevertex('d')
graph.display()