class Treenode:
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None

btree=Treenode('drinks')
leftchild=Treenode('hot')
rightchild=Treenode('cold')
btree.leftchild=leftchild
btree.rightchild=rightchild
tea=Treenode('tea')
coffee=Treenode('coffee')
cola=Treenode('cola')
fanta=Treenode('fanta')
leftchild.leftchild=tea
leftchild.rightchild=coffee
rightchild.leftchild=cola
rightchild.rightchild=fanta

def preorder(rootnode):
    if not rootnode:
        return None
    print(rootnode.data)
    preorder(rootnode.leftchild)
    preorder(rootnode.rightchild)

preorder(btree)