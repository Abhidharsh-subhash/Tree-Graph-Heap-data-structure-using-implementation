class Graph:
    def __init__(self):
        self.adjacency_list={}
    def addvertex(self,vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex]=[]
            return True
        return False
    def display(self):
        for vertex in self.adjacency_list:
            print(vertex,':',self.adjacency_list[vertex])
    def addedge(self,vertex1,vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)

graph=Graph()
graph.addvertex('a')
graph.addvertex('b')
graph.addedge('a','b')
graph.display()
    