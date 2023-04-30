class BST:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def insertion(rootnode,value):
    if rootnode.data is None:
        rootnode.data=value
    elif value <= rootnode.data:
        if rootnode.left is None:
            rootnode.left=BST(value)
        else:
            insertion(rootnode.left,value)
    else:
        if rootnode.right is None:
            rootnode.right=BST(value)
        else:
            insertion(rootnode.right,value)
    return 'insertion successful'

binary=BST(None)
print(insertion(binary,80))
print(insertion(binary,90))
print(insertion(binary,50))
print(binary.data)
print(binary.left.data)
print(binary.right.data)