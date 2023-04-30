class Binarytree:
    def __init__(self,size):
        self.maxsize=size
        self.arr=size * [None]
        self.lastusedindex=0

    def insert(self,data):
        if self.lastusedindex+1 == self.maxsize:
            return 'binary tree is full'
        else:
            self.arr[self.lastusedindex+1]=data
            self.lastusedindex+=1
            return 'successfully inserted'
        
    def inorder(self,index):
        if index>self.lastusedindex:
            return
        self.inorder(index*2)
        print(self.arr[index])
        self.inorder((index*2)+1)

binary=Binarytree(10)
binary.insert('drinks')
binary.insert('hot')
binary.insert('cold')
binary.insert('tea')
binary.insert('coffee')
binary.insert('cola')
binary.insert('fanta')
binary.inorder(1)