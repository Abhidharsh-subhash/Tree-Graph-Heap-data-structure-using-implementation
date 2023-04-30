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

    def delete(self):
        self.arr=None
        return 'binary tree deleted successfully'
    
binary=Binarytree(20)
binary.insert('drinks')
binary.insert('hot')
binary.insert('cold')
binary.insert('tea')
binary.insert('coffee')
binary.insert('cola')
binary.insert('fanta')
binary.levelorder(1)
print('______________')
print(binary.delete())
binary.levelorder(1)
