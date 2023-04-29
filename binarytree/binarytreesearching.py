import queue as queue

class Graph:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

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
hot.right=coffee
cold.left=cola
cold.right=fanta

def findnode(rootnode,node):
    if not rootnode:
        return
    else:
        customqueue=queue.Queue()
        customqueue.enqueue(rootnode)
        while not(customqueue.isEmpty()):
            root=customqueue.dequeue()
            if root.value.data == node:
                return True
            if root.value.left is not None:
                customqueue.enqueue(root.value.left)
            if root.value.right is not None:
                customqueue.enqueue(root.value.right)
        return False
            
print(findnode(drinks,'coffe'))