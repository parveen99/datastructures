class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
    def reverselist(self):
        prev=None
        curr=self.head
        while(curr is not None):
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next        
        self.head=prev
        
            
        
        
llist=Linkedlist()
llist.head=Node(8)
b=Node(5)
c=Node(4)
llist.head.next=b
b.next=c
print("Before reversing")
llist.printlist()
llist.reverselist()
print("after reversing")
llist.printlist()
