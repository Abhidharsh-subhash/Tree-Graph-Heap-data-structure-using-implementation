import Queue as queue

class BST:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

def levelorder(rootnode):
    if not rootnode:
        return
    else:
        custom=queue.Queue()
        custom.enqueue(rootnode)
        while not(custom.isEmpty()):
            x=custom.dequeue()
            print(x.value.data)
            if x.value.left is not None:
                custom.enqueue(x.value.left)
            if x.value.right is not None:
                custom.enqueue(x.value.right)


def insert(rootnode,value):
    if rootnode.data is None:
        rootnode.data=value
    elif value < rootnode.data:
        if rootnode.left is None:
            rootnode.left=BST(value)
        else:
            insert(rootnode.left,value)
    else:
        if rootnode.right is None:
            rootnode.right=BST(value)
        else:
            insert(rootnode.right,value)

new=BST(None)
insert(new,90)
insert(new,20)
insert(new,67)
insert(new,55)
insert(new,17)
levelorder(new)