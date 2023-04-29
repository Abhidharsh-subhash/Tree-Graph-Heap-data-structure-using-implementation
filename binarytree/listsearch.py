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

binary=Binarytree(10)
binary.insert(90)
binary.insert(99)
binary.insert(0)
binary.insert(78)
binary.insert(80)
print(binary.search(8))     