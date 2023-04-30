class Node:
    def __init__(self,value):
        self.value=value
        self.ref=value
    def __str__(self):
        return str(self.data)
    
class linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None

class Queue:
    def __init__(self):
        self.linkedlist=linkedlist()
    def __str__(self):
        values=[str(x) for x in self.linkedlist]
        return ' '.join(values)
    def isEmpty(self):
        if self.linkedlist.head is None:
            return True
        else:
            return False
    def enqueue(self,value):
        node=Node(value)
        if self.isEmpty():
            self.linkedlist.head=node
            self.linkedlist.tail=node
        else:
            self.linkedlist.tail.ref=node
            self.linkedlist.tail=node
    def dequeue(self):
        if self.isEmpty():
            return
        else:
            temp=self.linkedlist.head
            if self.linkedlist.head == self.linkedlist.tail:
                self.linkedlist.head=None
                self.linkedlist.tail=None
            else:
                self.linkedlist.head=self.linkedlist.head.ref
            return temp
