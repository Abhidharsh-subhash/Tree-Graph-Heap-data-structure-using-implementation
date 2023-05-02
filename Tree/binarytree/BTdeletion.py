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
cold.left=cola


def levelorder(rootnode):
    if not rootnode:
        return
    else:
        custom=queue.Queue()
        custom.enqueue(rootnode)
        while not (custom.isEmpty()):
            root=custom.dequeue()
            print(root.value.data)
            if root.value.left is not None:
                custom.enqueue(root.value.left)
            if root.value.right is not None:
                custom.enqueue(root.value.right)
#get the deepest value to in the tree 
def deepest(rootnode):
    if not rootnode:
        return
    else:
        custom=queue.Queue()
        custom.enqueue(rootnode)
        while not (custom.isEmpty()):
            root=custom.dequeue()
            if root.value.left is not None:
                custom.enqueue(root.value.left)
            if root.value.right is not None:
                custom.enqueue(root.value.right)
        deepestnode=root.value
        return deepestnode
    
def deletedeepest(rootnode,node):
    if not rootnode:
        return
    else:
        custom=queue.Queue()
        custom.enqueue(rootnode)
        while not (custom.isEmpty()):
            root=custom.dequeue()
            if root.value is node:
                root.value=None
                return
            if root.value.left:
                if root.value.left is node:
                    root.value.left=None
                    return
                else:
                    custom.enqueue(root.value.left)
            if root.value.right:
                if root.value.right is node:
                    root.value.right=None
                    return
                else:
                    custom.enqueue(root.value.right)

def deletenode(rootnode,node):
    if not rootnode:
        return
    else:
        custom=queue.Queue()
        custom.enqueue(rootnode)
        while not (custom.isEmpty()):
            root=custom.dequeue()
            if root.value.data == node:
                dnode=deepest(rootnode)
                root.value.data=dnode.data
                deletedeepest(rootnode,dnode)
                return 'deleted successfully'
            if root.value.left is not None:
                custom.enqueue(root.value.left)
            if root.value.right is not None:
                custom.enqueue(root.value.right)
        return 'deletion failed'
    
levelorder(drinks)
print('after deletion')
print(deletenode(drinks,'coffee'))
levelorder(drinks)
