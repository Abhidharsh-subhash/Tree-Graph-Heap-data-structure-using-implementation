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
    def display(self):
        for vertex in self.adj:
            print(vertex,':',self.adj[vertex])

graph=Graph()
graph.addvertex('a')
graph.addvertex('b')
graph.addvertex('c')
graph.addedge('a','b')
graph.addedge('a','c')
graph.addedge('c','b')
graph.removeedge('c','a')
graph.display()