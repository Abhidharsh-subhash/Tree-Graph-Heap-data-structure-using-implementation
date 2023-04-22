#tree using python list

class TreeNode:
    def __init__(self,data,children = []):
        self.data=data
        self.children=children

    def __str__(self,level=0):
        ret=" "*level+str(self.data)+"\n"
        for child in self.children:
            ret+=child.__str__(level+1)
        return ret
    
    def add(self,Treenode):
        self.children.append(Treenode)

t=TreeNode('drinks',[])
cold=TreeNode('cold',[])
hot=TreeNode('hot',[])
t.add(cold)
t.add(hot)
tea=TreeNode('tea',[])
coffee=TreeNode('coffee',[])
cola=TreeNode('cola',[])
fanta=TreeNode('fanta',[])
hot.add(tea)
hot.add(coffee)
cold.add(cola)
cold.add(fanta)
print(t)