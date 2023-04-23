class Treenode:
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None
tree=Treenode('drinks')
hot=Treenode('hot')
cold=Treenode('cold')
tree.leftchild=hot
tree.rightchild=cold
tea=Treenode('tea')
coffee=Treenode('coffee')
cola=Treenode('cola')
fanta=Treenode('fanta')
hot.leftchild=tea
hot.rightchild=coffee
cold.leftchild=cola
cola.rightchild=fanta

def postorder(rootnode):
    if not rootnode:
        return
    postorder(rootnode.leftchild)
    postorder(rootnode.rightchild)
    print(rootnode.data)

postorder(tree)
