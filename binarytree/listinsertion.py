#case1 - binary tree is full
#case2 - we have to look for a first vacant place

class Binarytree:
    def __init__(self,size):
        self.maxsize=size
        self.arr=size * [None]
        self.lastusedindex=0

    def insertnode(self,value):
        if self.lastusedindex+1 == self.maxsize:
            return 'binary tree is full'
        self.arr[self.lastusedindex+1]=value
        self.lastusedindex+=1
        return 'successfully inserted'
    
binary=Binarytree(10)
print(binary.insertnode(90))
print(binary.insertnode(0))
print(binary.insertnode(9))
print(binary.insertnode(900))
print(binary.insertnode(909))