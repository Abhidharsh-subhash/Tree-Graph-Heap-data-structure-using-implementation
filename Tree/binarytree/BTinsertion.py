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
hot.right=coffee
cold.right=fanta

def display(rootnode):
    if not rootnode:
        return 
    else:
        customqueue=queue.Queue()
        customqueue.enqueue(rootnode)
        while not(customqueue.isEmpty()):
            root=customqueue.dequeue()
            print(root.value.data)
            if root.value.left is not None:
                customqueue.enqueue(root.value.left)
            if root.value.right is not None:
                customqueue.enqueue(root.value.right)

def insertnode(rootnode,newnode):
    if not rootnode:
        rootnode=newnode
    else:
        customqueue=queue.Queue()
        customqueue.enqueue(rootnode)
        while not (customqueue.isEmpty()):
            root=customqueue.dequeue()
            if root.value.left is not None:
                customqueue.enqueue(root.value.left)
            else:
                root.value.left=newnode
                return 'successfully inserted'
            if root.value.right is not None:
                customqueue.enqueue(root.value.right)
            else:
                root.value.right=newnode
                return 'successfully inserted'
            
display(drinks)
print(insertnode(drinks,cola))
display(drinks)
