class Trienode:
    def __init__(self):
        self.child={}
        self.end=False

class Trie:
    def __init__(self):
        self.rootnode=Trienode()
    def insert(self,word):
        current=self.rootnode
        for i in word:
            ch=i
            node=current.child.get(ch)
            if node == None:
                node=Trienode()
                current.child.update({ch:node})
            current=node
        current.end=True
        print('successfully inserted')
    def search(self,word):
        current=self.rootnode
        for i in word:
            node=current.child.get(i)
            if node == None:
                return False
            current=node
        if current.end == True:
            return True
        else:
            return False
        
newtrie=Trie()
newtrie.insert('hell')
newtrie.insert('hello')
print(newtrie.search('hello'))