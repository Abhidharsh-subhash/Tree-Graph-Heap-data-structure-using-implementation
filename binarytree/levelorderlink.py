#implementing level traversal using queue with linked list
import queue as queue

class Treenode:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

tree=Treenode('drinks')
hot=Treenode('hot')
cold=Treenode('cold')
coffee=Treenode('coffee')
tea=Treenode('tea')
cola=Treenode('cola')
fanta=Treenode('fanta')
tree.left=hot
tree.right=cold
hot.left=tea
hot.left=coffee
cold.left=cola
cold.right=fanta

def levelorder(rootnode):
    if not rootnode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootnode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if (root.value.left is not None):
                customQueue.enqueue(root.value.left)
            
            if (root.value.right is not None):
                customQueue.enqueue(root.value.right)

levelorder(tree)
