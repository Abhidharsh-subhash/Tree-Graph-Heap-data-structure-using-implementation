class BST:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

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
            rootnode.right = BST(value)
        else:
            insert(rootnode.right,value)
    return 'success'

def search(rootnode,element):
    if rootnode.data == element:
        print('found')
    elif element < rootnode.data:
        if rootnode.left.data == element:
            print('found')
        else:
            search(rootnode.left,element)
    else:
        if rootnode.right.data == element:
            print('found')
        else:
            search(rootnode.right,element)

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
search(new,99)