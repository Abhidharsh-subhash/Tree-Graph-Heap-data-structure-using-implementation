class Trienode:
    def __init__(self):
        self.children={}
        self.endofstring=False

class Trie:
    def __init__(self):
        self.rootnode=Trienode()

new=Trie()
