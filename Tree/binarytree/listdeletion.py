class Binarytree:
    def __init__(self,size):
        self.maxsize=size
        self.arr=size*[None]
        self.lastusedindex=0

    def insert(self,value):
        if self.lastusedindex+1 == self.maxsize:
            return 'binary tree is full'
        else:
            self.arr[self.lastusedindex+1]=value
            self.lastusedindex+=1

    def levelorder(self,index):
        if index > self.lastusedindex:
            return
        else:
            for i in range(index,self.lastusedindex+1):
                print(self.arr[i])

    def deletenode(self,node):
        if self.lastusedindex == 0:
            return 'binary tree empty'
        else:
            for i in range(1,self.lastusedindex+1):
                if self.arr[i] == node:
                    self.arr[i]=self.arr[self.lastusedindex]
                    self.arr[self.lastusedindex]=None
                    self.lastusedindex-=1
                    return 'deleted successfully'

binary=Binarytree(20)
binary.insert('drinks')
binary.insert('hot')
binary.insert('cold')
binary.insert('tea')
binary.insert('coffee')
binary.insert('cola')
binary.insert('fanta')
binary.levelorder(1)
print('deletion')
binary.deletenode('coffee')
binary.levelorder(1)
