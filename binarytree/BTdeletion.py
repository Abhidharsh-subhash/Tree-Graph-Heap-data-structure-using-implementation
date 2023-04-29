import queue as queue

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

#get the deepest value to in the tree 
def getdeepest(rootnode):
    if not rootnode:
        return
    else:
        customqueue=queue.Queue()
        customqueue.enqueue(rootnode)
        while not (customqueue.isEmpty()):
            root=customqueue.dequeue()
            if root.value.left is not None:
                customqueue.enqueue(root.value.left)
            if root.value.right is not None:
                customqueue.enqueue(root.value.right)
        return root.value.data

print(getdeepest(drinks))