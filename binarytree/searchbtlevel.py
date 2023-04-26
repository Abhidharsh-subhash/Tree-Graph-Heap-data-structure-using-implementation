import queue as queue

class Treenode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

tree=Treenode('drinks')
hot=Treenode('hot')
cold=Treenode('cold')
tea=Treenode('tea')
fanta=Treenode('fanta')
cola=Treenode('cola')
tree.right=cold
tree.left=hot

def search(rootnode,value):
    if not rootnode:
        return 'value does not exist' 
    else:
        customqueue=queue.Queue()
        customqueue.enqueue(rootnode)
        while not customqueue.isEmpty():
            root=customqueue.dequeue()
            if root.value.data == value:
                return 'success'
            if root.value.left is not None:
                customqueue.enqueue(root.value.left)
            if root.value.right is not None:
                customqueue.enqueue(root.value.right)
        return 'not found'
    
search(tree,'cola')
