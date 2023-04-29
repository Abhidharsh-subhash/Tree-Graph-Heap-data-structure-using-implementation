class Graph:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

drinks=Graph('drinks')
hot=Graph('hot')
cold=Graph('cold')
tea=Graph('tea')
coffee=Graph('coffee')
cola=Graph('cola')
fanta=Graph('fanta')
drinks.right=cold
drinks.left=hot
hot.left=tea
hot.left=coffee
hot.right=coffee
cold.right=fanta

def deletetree(rootnode):
    rootnode.data=None
    rootnode.left=None
    rootnode.right=None
    return 'binary tree deleted'