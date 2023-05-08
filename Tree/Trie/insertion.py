#case1 : A trie is blank

class Trienode:
    def __init__(self):
        self.child={}
        self.endofstring=False
class Trie:
    def __init__(self):
        self.rootnode=Trienode()
    def insertion(self,word):
        current=self.rootnode
        for i in word:
            ch=i
            node=current.child.get(ch)
            if node == None:
                node=Trienode()
                current.child.update({ch:node})
            current=node
        current.endofstring=True
        print('inserted successfully')

newtrie=Trie()
newtrie.insertion('hello')
newtrie.insertion('hello world')