class Treenode:
    def __init__(self,data):
        self.data=data
        self.rightchild=None
        self.leftchild=None

tree=Treenode('drinks')
hot=Treenode('hot')
cold=Treenode('cold')
tree.leftchild=hot
tree.rightchild=cold
tea=Treenode('tea')
cola=Treenode('cola')
fanta=Treenode('fanta')
hot.leftchild=tea
cold.leftchild=cola
cold.rightchild=fanta

def inorder(rootnode):
    if not rootnode:
        return
    inorder(rootnode.leftchild)
    print(rootnode.data)
    inorder(rootnode.rightchild)

inorder(tree)