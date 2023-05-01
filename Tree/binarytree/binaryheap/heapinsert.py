class Heap:
    def __init__(self,size):
        self.size=size+1
        self.arr=(size+1) * [None]
        self.heap=0

def peek(rootnode):
    if not rootnode:
        return
    else:
        return rootnode.arr[1]
def heapsize(rootnode):
    if not rootnode:
        return
    else:
        return rootnode.heap
def traversal(rootnode):
    if not rootnode:
        return
    else:
        for i in range(1,rootnode.heap+1):
            print(rootnode.arr[i])
def heapify(rootnode,index,heaptype):
    if index <=1:
        return
    parent=int(index/2)
    if heaptype == 'Min':
        if rootnode.arr[index] < rootnode.arr[parent]:
            rootnode.arr[index],rootnode.arr[parent]=rootnode.arr[parent],rootnode.arr[index]
        heapify(rootnode,parent,heaptype)
    elif heaptype == 'Max':
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

newheap=Heap(10)
print(insert(newheap,10,'Max'))
print(insert(newheap,13,'Max'))
print(insert(newheap,1,'Max'))
print(insert(newheap,7,'Max'))
print(insert(newheap,20,'Max'))
print(insert(newheap,19,'Max'))
traversal(newheap)
