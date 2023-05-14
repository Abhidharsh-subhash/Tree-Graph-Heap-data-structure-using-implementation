def heapify(list,n,i):#n=>no.of elements in the list i=>index in the list
    smallest=i
    left=(2*i)+1
    right=(2*i)+2
    if left<n and list[left]<list[smallest]:
        smallest=left
    if right<n and list[right]<list[smallest]:
        smallest=right
    if smallest != i:
        list[smallest],list[i]=list[i],list[smallest]
        heapify(list,n,smallest)

def heapsort(array):                                #TIME COMPLEXITY:O(NlogN)
    n=len(array)
    #this is for building the min heap
    for i in range(int(n/2),-1,-1):
        heapify(array,n,i)
    #this is for deleting the element from min heap
    for i in range(n-1,0,-1):
        array[i],array[0]=array[0],array[i]
        heapify(array,i,0)
    #array.reverse()

array=[30,17,20,1,5,10]
heapsort(array)
print(array)
 