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
    
    def search(self,target):
        for i in range(len(self.arr)):
            if self.arr[i] == target:
                return 'success'
        return 'not found'   
        
    def preorder(self,index):
        if index > self.lastusedindex:
            return False
        print(self.arr[index])
        self.preorder(index*2)
        self.preorder((index*2)+1)

binary=Binarytree(10)
print(binary.insert('drinks'))
print(binary.insert('cold'))
print(binary.insert('tea'))
print(binary.insert('coffee'))
print(binary.insert('hot'))
print(binary.insert('cola'))
print(binary.insert('fanta'))
binary.preorder(1)