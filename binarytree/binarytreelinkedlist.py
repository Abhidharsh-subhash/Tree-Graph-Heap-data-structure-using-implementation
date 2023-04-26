#it is just a basic implementation of how the nodes are being created in a binary tree using linked list so it is not working 
class Binarytree:
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None

Btree=Binarytree('drinks')
hot=Binarytree('hot')
cold=Binarytree('cold')
Btree.leftchild=hot
Btree.rightchild=cold
print(Btree)