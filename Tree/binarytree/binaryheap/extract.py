class Heap:
    def __init__(self,size):
        self.size=size+1
        self.arr=[None] * (size+1)
        self.heap=0

def traversal(rootnode):
    if rootnode is None:
        return 'empty heap'
    else:
        for i in range(1,rootnode.heap+1):
            print(rootnode.arr[i])

def heapify(rootnode,index,heaptype):
    if index <= 1:
        return
    parent=int(index/2)
    if heaptype == 'Min':
        if rootnode.arr[index] < rootnode.arr[parent]:
            rootnode.arr[index],rootnode.arr[parent]=rootnode.arr[parent],rootnode.arr[index]
        heapify(rootnode,parent,heaptype)
    if heaptype == 'Max':
        if rootnode.arr[index] > rootnode.arr[parent]:
            rootnode.arr[index],rootnode.arr[parent]=rootnode.arr[parent],rootnode.arr[index]
        heapify(rootnode,parent,heaptype)

def insert(rootnode,node,heaptype):
    if rootnode.heap+1 == rootnode.size:
        return 'heap is full'
    rootnode.arr[rootnode.heap+1]=node
    rootnode.heap+=1
    heapify(rootnode,rootnode.heap,heaptype)
    return 'value inserted'

def heapifyextract(rootnode,index,heaptype):
    leftindex=index*2
    rightindex=(index*2)+1
    swapchild=0
    if rootnode.heap < leftindex:
        return
    #for one child
    elif rootnode.heap == leftindex:
        if heaptype == 'Min':
            if rootnode.arr[index] > rootnode.arr[leftindex]:
                rootnode.arr[leftindex],rootnode.arr[index]=rootnode.arr[index],rootnode.arr[leftindex]
            return
        else:
            if rootnode.arr[index] < rootnode.arr[leftindex]:
                rootnode.arr[leftindex],rootnode.arr[index]=rootnode.arr[index],rootnode.arr[leftindex]
            return
    #for two child
    else:
        if heaptype == "Min":
            if rootnode.arr[leftindex] < rootnode.arr[rightindex]:
                swapchild=leftindex
            else:
                swapchild=rightindex
            if rootnode.arr[index] > rootnode.arr[swapchild]:
                rootnode.arr[index],rootnode.arr[swapchild]=rootnode.arr[swapchild],rootnode.arr[index]
        else:
            if rootnode.arr[leftindex] < rootnode.arr[rightindex]:
                swapchild=leftindex
            else:
                swapchild=rightindex
            if rootnode.arr[index] < rootnode.arr[swapchild]:
                rootnode.arr[index],rootnode.arr[swapchild]=rootnode.arr[swapchild],rootnode.arr[index]
    heapifyextract(rootnode,swapchild,heaptype)

def extract(rootnode,heaptype):
    if rootnode.heap


newheap=Heap(10)
print(insert(newheap,10,'Max'))
print(insert(newheap,13,'Max'))
print(insert(newheap,1,'Max'))
print(insert(newheap,7,'Max'))
print(insert(newheap,20,'Max'))
print(insert(newheap,19,'Max'))
traversal(newheap)