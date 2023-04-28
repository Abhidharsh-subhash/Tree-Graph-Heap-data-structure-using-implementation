#it is used for finding the shortest path between the two given vertex
class Graph:
    def __init__(self,dict):
        if dict is None:
            dict={}
        self.dict=dict
    def bfs(self,start,end):
        queue=[]
        queue.append([start])
        while queue:
            path=queue.pop(0)
            node=path[-1]
            if node == end:
                return path
            for adjancent in self.dict.get(node,[]):
                new_path=list(path)
                new_path.append(adjancent)
                queue.append(new_path)

customdict={
    'a':['b','c'],
    'b':['d','g'],
    'c':['d','e'],
    'd':['f'],
    'e':['f'],
    'g':['f']
}
graph=Graph(customdict)
print(graph.bfs('a','f'))
print(graph.bfs('a','d'))
