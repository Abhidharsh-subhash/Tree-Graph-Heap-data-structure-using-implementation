class BST:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def insert(rootnode,value):
    if rootnode.data is None:
        rootnode.data=value
    elif value<=rootnode.data:
        if rootnode.left is None:
            rootnode.left=BST(value)
        else:
            insert(rootnode.left,value)
    else:
        if rootnode.right is None:
            rootnode.right=BST(value)
        else:
            insert(rootnode.right,value)
    return 'insertion successfull'

def postorder(rootnode):
    if not rootnode:
        return
    postorder(rootnode.left)
    postorder(rootnode.right)
    print(rootnode.data)

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
postorder(new)