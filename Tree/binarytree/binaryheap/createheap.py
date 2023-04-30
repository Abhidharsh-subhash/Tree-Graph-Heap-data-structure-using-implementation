class Heap:
    def __init__(self,size):
        self.arr=size+1 * [None]
        self.heap=0
        self.size=size+1

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