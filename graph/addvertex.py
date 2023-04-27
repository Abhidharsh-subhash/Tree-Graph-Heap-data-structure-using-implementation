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

graph=Graph()
graph.addvertex('a')
graph.display()