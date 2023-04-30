import Queue as queue

class BST:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def insert(rootnode,value):
    if rootnode.data is None:
        rootnode.data=value
    elif value <= rootnode.data:
        if rootnode.left is None:
            rootnode.left=BST(value)
        else:
            insert(rootnode.left,value)
    else:
        if rootnode.right is None:
            rootnode.right = BST(value)
        else:
            insert(rootnode.right,value)
    return 'successfull'

def levelorder(rootnode):
    if not rootnode:
        return
    custom=queue.Queue()
    custom.enqueue(rootnode)
    while not (custom.isEmpty()):
        root=custom.dequeue()
        print(root.value.data)
        if root.value.left is not None:
            custom.enqueue(root.value.left)
        if root.value.right is not None:
            custom.enqueue(root.value.right)


new=BST(None)
print(insert(new,70))
print(insert(new,50))
print(insert(new,90))
print(insert(new,30))
print(insert(new,60))
print(insert(new,80))
print(insert(new,100))
print(insert(new,20))
print(insert(new,40))
levelorder(new)