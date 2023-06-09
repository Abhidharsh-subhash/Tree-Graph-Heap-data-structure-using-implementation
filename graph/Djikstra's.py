class edge:
    def __init__(self,weight,start_vertex,target_vertex):
        self.weight=weight
        self.start_vertex=start_vertex
        self.target_vertex=target_vertex

class Node:
    def __init__(self,name):
        self.name=name
        self.visited=False
        #from which node we have come to this node
        self.predecessor=None
        self.neighbours=[]
        self.min_distance=float('inf')
    #normally we can't compare the nodes so inorder to compare the nodes we use the method __lt__
    def __lt__(self,other_node):
        return self.min_distance < other_node.min_distance
    #adding the edge between the nodes
    def addedge(self,weight,destination_vertex):
        edge=edge(weight,self,destination_vertex)
        self.neighbours.append(edge)